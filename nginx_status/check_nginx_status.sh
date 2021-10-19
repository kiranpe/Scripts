#!/bin/sh

status=$(ps -ef | grep -i [n]ginx | grep master)

if [ $? = "0" ];then
  echo "Nginx is up and running.." > /dev/null 2>&1
else
  echo "Nginx is Down on `hostname`.. Starting Nginx Web Server" | mailx -s "Nginx status on `hostname`" kiranpeddineni@gmail.com 
  sudo systemctl start nginx > /dev/null 2>&1
  new_status=$(ps -ef | grep -i [n]ginx | grep master)
    if [ -z "$new_status" ];then
      echo "Nginx is still Down.. Check configuration once.." | mailx -s "Nginx status on `hostname`" kiranpeddineni@gmail.com
    else
      echo "Nginx is Up and Running Now on `hostname`" |  mailx -s "Nginx status on `hostname`" kiranpeddineni@gmail.com
fi fi
