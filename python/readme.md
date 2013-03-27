一个基于pyxmpp的GTalk的客户端，制作了一个基于访问Redis数据库访问获取通讯录的自动应答机器人。

gtalk.ini 配置文件样例：
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

上述内容的gtalk.ini文件存放到gtalk.py相同目录下，即可！
