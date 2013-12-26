# GTalk机器人，可以根据用户输入内容进行相应的反馈


一个基于pyxmpp的GTalk的客户端，制作了一个基于访问Redis数据库访问获取通讯录的自动应答机器人。

gtalk.ini 配置文件样例：
---
==============================================================
* [gtalk]
+ account = your@gmail.com
+ password = your mail password

* [redis]
+ host = localhost
+ port = 6336
+ db = 1
+ auth = Redis_Connect_Password

==============================================================
---
上述内容的gtalk.ini文件存放到gtalk.py相同目录下，即可！


2013年4月1日 - iOS上的GTalk客户端会在发送信息后，还有一个类型为chat但body内容为None的包，因此增加了GTalk.py对这种特殊情况的判断和忽略。



---
#
AutoRecord.py
运行在Windows下，为了创建AutoIT3的键盘脚本录制而编写。
由于找到的AutoIT3的AutoRecord工具是使用c#编写的，而且稳定性很不好。
无奈之下使用Python的pyHook模块编写了一个自动录制屏幕并生成AutoIT3的脚本。
使用方法：
一、支持鼠标左键的点击记录。
二、支持键盘录入文字的记录。
三、如果按鼠标中间键将终止记录。
四、自动生成的脚本在D:\autoit_xxxx.au3中，用户函数为EnumUser()

## 当前不支持鼠标右键记录（主要我使用的BSS系统在浏览器中操作，没有右键的需求）
