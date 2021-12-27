#!/usr/bin/env python3
#Written by Kiran Peddineni
#Automating shell script using Python

import os
import subprocess
import requests
from rich.theme import Theme
from rich.console import Console

custome_theme = Theme({"success": "green", "fail": "red"})
console = Console(theme=custome_theme)

def check_service_status(firewall):
  service_is_active=os.popen("sudo systemctl is-active {}".format(firewall)).read().strip()
  if service_is_active in "active":
   console.print("[success]{} is active and running[/success]\n".format(firewall))
  else:
   console.print("[fail]{} is not active/running[/fail]\n".format(firewall)) 

def is_firewalld_rule_configured(firewall_port):
  firewalld_ports=subprocess.run("""sudo firewall-cmd --list-all --zone=public | grep ports | grep {}""".format(firewall_port), shell=True)
  if firewalld_ports.returncode == 0:
   console.print("[success]FirewallD has port {} configured[/success]\n".format(firewall_port))
  else:
   console.print("[fail]FirewallD port {} is not configured[/fail]\n".format(firewall_port))

def install_firewalld():
  console.print("[success]Installing FirewallD..[/success]")
  os.system("sudo yum install -y firewalld")
  os.system("sudo service firewalld start")
  os.system("sudo systemctl enable firewalld")

  check_service_status(firewall = "firewalld") 

install_firewalld()

def install_mariadb():
  console.print("[success]Installing MariaDB Server..[/success]")
  os.system("sudo yum install -y mariadb-server")
  os.system("sudo service mariadb start")
  os.system("sudo systemctl enable mariadb")

  check_service_status(firewall = "mariadb")

install_mariadb()

def configure_firewall_rules():
  console.print("[success]Configuring FirewallD rules for database..[/success]")
  os.system("sudo firewall-cmd --permanent --zone=public --add-port=3306/tcp")
  os.system("sudo firewall-cmd --reload")
  
  is_firewalld_rule_configured(firewall_port = 3306) 

configure_firewall_rules()

def db_setup():
  console.print("[success]Setting up database..[/success]")
  os.system("sudo mysql < setup-db.sql")
   
db_setup()

def loading_inventory():
  console.print("[success]Loading inventory data into database[/success]")
  os.system("sudo mysql < db-load-script.sql")

loading_inventory()

def check_db():
  status = subprocess.run('sudo mysql -e "use ecomdb; select * from products;"', shell=True)
  if status.returncode == 0:
   console.print("[success]Inventory data loaded into MySQl!![/success]\n")
  else:
   console.print("[fail]Inventory data not loaded into MySQl!![/fail]\n")

check_db()

console.print("[success]---------------- Setup Database Server - Finished ------------------[/success]\n")
console.print("[success]---------------- Setup Web Server ------------------[/success]")

def configure_webservers():
  console.print("[success]Installing Web Server Packages...[/success]")
  os.system("sudo yum install -y httpd php php-mysql")

configure_webservers()

def configure_webserver_firewall_rule():
  console.print("[success]Configuring FirewallD rules for webserver..[/success]")
  os.system("sudo firewall-cmd --permanent --zone=public --add-port=80/tcp")
  os.system("sudo firewall-cmd --reload")

  is_firewalld_rule_configured(firewall_port = 80)

configure_webserver_firewall_rule()

def start_httpd():
  console.print("[success]Start httpd service..[/success]")
  os.system("sudo service httpd start")
  os.system("sudo systemctl enable httpd")
  
  check_service_status(firewall = "httpd") 

start_httpd()

def downlod_code():
  console.print("[success]Install GIT..[/success]")
  os.system("sudo yum install -y git")
  console.print("[success]Clone Git Repo..[/success]")
  os.system("sudo git clone https://github.com/kodekloudhub/learning-app-ecommerce.git /var/www/html/")
  console.print("[success]Updating index.php..[/success]")
  os.system("sudo sed -i 's/172.20.1.101/localhost/g' /var/www/html/index.php")

downlod_code()

console.print("[success]---------------- Setup Web Server - Finished ------------------[/success]\n")
console.print("[success]---------------- Starting some Sanity Test ------------------[/success]\n")

def check_item_on_page():
  web_page = requests.get("http://localhost")
  content = web_page.content
  items = ["Laptop", "Drone", "VR", "Watch", "Phone", "TV"] 
  for item in items:
   if item in str(content):
     console.print("[success]Item {} is present on the web page!![/success]".format(item)) 
   else:
     console.print("[fail]Item {} is not present on the web page!![/fail]".format(item))

check_item_on_page()
