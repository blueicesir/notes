#!/bin/bash
TARGET="192.168.1.1"
result=`ping -c 5 $TARGET | grep "5 packets transmitted" | awk -F "," '{print $3}' | awk '{print $1}'`
RS=${result/%%/}

if [ $RS -eq 100 ]; then
	echo "100% packet loss"
        IF_NAMES=`/sbin/ifconfig | /bin/grep eth | /bin/awk '{print $1}'`;
        IP=([0]="192.168.100.10" [1]="192.168.200.10");
        MASK=([0]="255.255.255.0" [1]="255.255.255.240");
        index=0;
        for v in $IF_NAMES; do
                /sbin/ifconfig $v ${IP[$index]} netmask ${MASK[$index]} up
                ((index+=1));
        done;
        /sbin/route add -net 0.0.0.0/0 gw 192.168.1.1
else
	echo "network ok."
fi
