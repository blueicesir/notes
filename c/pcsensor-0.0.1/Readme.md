pcsensor-0.0.1
这个家伙官网上已经没有了，不知道是更换了地址还是其它，在http://lineurepoye.net/brol/
找到了！
http://lineurepoye.net/brol/temper-1.0/
打包下载地址
http://lineurepoye.net/brol/pcsensor-0.0.1.tgz

把USB设备描述文件复制到
sudo cp 99-tempsensor.rules /etc/udev/rules.d/
重新加载USB设备库信息
sudo udevadm control --reload-rules
重启，如果没有这个命令就重启RaspberryPi吧
sudo start_udev

如果提示usb.h文件找不到，就按照这个包
sudo apt-get install libusb-dev

然后到源码目录下执行
make
即可！

如果没有start_udev命令需呀重启，否则会提示没有配置设备。
