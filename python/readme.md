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

