#!/bin/bash
# 由于RedHat 6.3版本在Hyper-V上运行并且有两个网卡
# 系统重启后设备名称会发生变化，例如第一次是eth1,eth2结果重启几次之后就是eth7,eth8了。
# 此脚本用于测试网络是否通畅，如果不通畅，则获取eth开头的网卡设备，并设置IP地址
# 由于两张网卡，可能会由于地址不对应而无法正常工作，因此请修改IP和掩码的数组对调前后两个配置的顺序
# 复制成另外一个脚本，并设置crontab定时计划任务，可以间隔10分钟调用对应的脚本，然后登陆即可！

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
