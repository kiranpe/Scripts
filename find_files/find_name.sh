name=`find . -name file.txt -type f -exec grep kiran {} \;` 

echo $name

if [ $? -eq 0 ];then
echo "Hello $name!!"
fi
