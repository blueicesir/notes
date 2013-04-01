# 防止ssh爆破的iptables策略。

###对于新发起的连接请求加入到最近列表中
iptables -I INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent --set

###如果最近的连接表中，并且60秒内到达或者超过四次，则丢弃数据
iptables -I INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP


###来自127.0.0.1的目标端口是6900到6901的进行限速，每秒只接受一个数据包。
iptables -A INPUT -s 127.0.0.1 -p tcp -d 127.0.0.1 --dport 6900:6901 -m limit --limit 1/s -j ACCEPT 

###当上一个策略没有匹配到时就是没有接受时，多余的数据包进行丢弃。
iptables -A INPUT -s 127.0.0.1 -p tcp -d 127.0.0.1 --dport 6900:6901 -j DROP


