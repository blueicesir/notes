## pcsensor-0.0.1
这个家伙官网上已经没有了，不知道是更换了地址还是其它
http://lineurepoye.net/brol/
http://lineurepoye.net/brol/temper-1.0/
打包下载地址
http://lineurepoye.net/brol/pcsensor-0.0.1.tgz

## 安装方法:
把USB设备描述文件复制到<br>
sudo cp 99-tempsensor.rules /etc/udev/rules.d/<br>
* 重新加载USB设备库信息
sudo udevadm control --reload-rules
* 如果没有下面这个命令就重启设备吧，我的是RaspberryPi
sudo start_udev

* 编译时如果提示usb.h文件找不到，需要安装这个包
sudo apt-get install libusb-dev

然后到源码目录下执行
make
即可！

如果没有start_udev命令需重启，否则会提示没有配置设备。


## getTemp.py是支持www.yeelink.net物联网图表数据上传的脚本，只实现了上传。
* 其中由于yeelink的告警功能延时比较大，因此自己写了一个POST到特定网站
* getTemp.ini中配置yeelink的开发者API和DEVICE_ID以及SENSOR_ID。
* 支持写本地sqlite3数据库，以便使用类似RRDTools这样的图表工具重建可视化曲线图。


## 注意:这个目录下的pcsensor是在RaspberryPi设备上编译的，不适合x86平台。需要请自行编译！
