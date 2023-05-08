#!/bin/bash

cd /root/MyProjects/GetImages/
for i in {1..100}
do
python many.py
source show.sh
read -p "" s
[ -z $s ] && continue
if [ $s == "q" ]
then 
    exit
fi
done
