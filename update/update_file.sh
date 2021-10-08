count=`cat abc.cfg | wc -l`

if [ $count = 2 ];then
line1=`sed -sn 1p abc.cfg`
line2=`sed -sn 2p abc.cfg`

sed -i -e "s/\"address\" : .*/\"address\" : $line1, $line2/g" xz.yaml 
fi
