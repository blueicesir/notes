#!/bin/bash
# 由于RedHat 6.3版本在Hyper-V上运行并且有两个网卡
# 系统重启后设备名称会发生变化，例如第一次是eth1,eth2结果重启几次之后就是eth7,eth8了。
# 此脚本用于测试网络是否通畅，如果不通畅，则获取eth开头的网卡设备，并设置IP地址
# 由于两张网卡，可能会由于地址不对应而无法正常工作，因此请修改IP和掩码的数组对调前后两个配置的顺序
# 复制成另外一个脚本，并设置crontab定时计划任务，可以间隔10分钟调用对应的脚本，然后登陆即可！
# 由于RedHat 6.3 Ent版本运行在Hyper-V虚拟机上，且配置了动态mac地址的网卡策略，因此多次重启后
# 系统的网卡mac地址会发生变化，导致RedHat的系统认为不是同一张网卡，而导致eth设备号递增现象。
# 直接联系后台管理员让网卡mac地址固定，并删除/etc/init.d/9*network*pers*开头的一个脚本即可。
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
