#!/bin/sh
new_end=$(tail -1 ipv6-prefix.cfg | awk -F"," '{print $1}' | sed -n 1p | sed 's/\//\\\//g')
new_start=$(tail -1 ipv6-prefix.cfg | awk -F"," '{print $2}' | sed -n 1p | sed 's/ ^*//g' | sed 's/\//\\\//g')

exist_end=$(sed -n 549p xz.yaml | awk -F": " '{print $2}' | sed 's/\//\\\//g')
exist_start=$(sed -n 550p xz.yaml | awk -F": " '{print $2}' | sed 's/\//\\\//g')

sed -n 549p xz.yaml | sed "s/$exist1/\"$line1\"/g" xz.yaml
sed -n 550p xz.yaml | sed "s/$exist2/\"$line2\"/g" xz.yaml

#line3=$(cat abc.cfg | awk -F"," '{print $1}' | sed -n 2p)
#line4=$(cat abc.cfg | awk -F"," '{print $2}' | sed -n 2p | sed 's/ ^*//g' | sed 's/\//\\\//g')

#exist3=$(sed -n 7p xz.yaml | awk -F": " '{print $2}')
#exist4=$(sed -n 8p xz.yaml | awk -F": " '{print $2}' | sed 's/\//\\\//g')

#sed -n 7p xz.yaml | sed -i "s/$exist3/\"$line3\"/g" xz.yaml
#sed -n 8p xz.yaml | sed -i "s/$exist4/\"$line4\"/g" xz.yaml
