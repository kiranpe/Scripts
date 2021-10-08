today_date=`date "+%b %-d"`
file_date=`ls -lrth tmp | awk -F" " '{print $6 " " $7}'`

if [ "$today_date" = "$file_date" ];then
echo "File is latest one..Checking Time"

   current_time=`date "+%R"`
   file_time=`ls -lrth tmp | awk -F" " '{print $8}'` 
  
   if [ "$current_time" = "$file_time" ];then
   echo "File is getting updated regularly"
   else
   echo "File is not getting updated.. please check the script"
   fi 

else
echo "File is old one"
fi
