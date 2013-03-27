#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import logging
import locale
import codecs

import redis.client 
import redis
from redis.exceptions import (RedisError,ConnectionError,ResponseError,InvalidResponse,AuthenticationError,NoScriptError,ExecAbortError,)

from pyxmpp.all import JID,Iq,Presence,Message,StreamError
from pyxmpp.jabber.client import JabberClient
from pyxmpp.interface import implements
from pyxmpp.interfaces import *
from pyxmpp.streamtls import TLSSettings

class EchoHandler(object):
    implements(IMessageHandlersProvider, IPresenceHandlersProvider)
    def __init__(self,client):
        self.client=client

    def get_message_handlers(self):
        return [("normal",self.message)]

    def get_presence_handlers(self):
        return [
                (None,self.presence),
                ('unavailable',self.presence),
                ('subscribe',self.presence_control),
                ('subscribed',self.presence_control),
                ('unsubscribe',self.presence_control),
                ('unsubscribed',self.presence_control)]

    def message(self,stanza):
        subject=stanza.get_subject()
        body=stanza.get_body()
        t=stanza.get_type()
        print u'收到[%s]的信息.' % (unicode(stanza.get_from(),)),
        if subject:
            print u'主题:"%s"' % (subject,),
        if body:
            print u'正文:"%s"' % (body,),
        if t:
            print u'类型:"%s"' % (t,)
        else:
            print u'类型:"正常"'


        if stanza.get_type()=='headline':
            return True

        if subject:
            subject=u'Re: '+subject

        client=redis.Redis(host='localhost',port=6336,db=4,password='XShell4')

        try:
            body+=(":"+client.get(body).decode('utf-8'))
        except Exception,e:
            body=u'您查询的"%s"无记录。' % (body,)

        m=Message(
                to_jid=stanza.get_from(),
                from_jid=stanza.get_to(),
                stanza_type=stanza.get_type(),
                subject=subject,
                body=body)
        if body:
            p=Presence(status=u'海上升明月，天涯共此时！')
            return [m,p]
        return m

    def presence(self,stanza):
        msg=u'%s has become ' % (stanza.get_from())
        t=stanza.get_type()
        if t== 'unavailable':
            msg+=u'离线'
        else:
            msg+=u'上线'

        show=stanza.get_show()

        if show:
            msg+=u'(%s)' % (show,)

        status=stanza.get_status()

        if status:
            msg+=u': '+status
        print msg

    def presence_control(self,stanza):
        msg=unicode(stanza.get_from())
        t=stanza.get_type()
        if t=='subscribe':
            msg+=u' has requested presence subscription.'
        elif t== 'subscribed':
            msg+=u' has accepted our presence subscription request.'
        elif t =='unsubscribe':
            msg += u' has canceled his subscription of our.'
        elif t == 'unsubscribed':
            msg += u' has canceled our subscription of his presence.'
        print msg
        return stanza.make_accept_response()


class VersionHandler(object):
    implements(IIqHandlersProvider,IFeaturesProvider)

    def __init__(self,client):
        self.client=client

    def get_features(self):
        return ["jabber:iq:version"]

    def get_iq_get_handlers(self):
        return [ ("query","jabber:iq:version",self.get_version),]

    def get_iq_set_handlers(self):
        return []

    def get_version(self,iq):
        iq=iq.make_result_response()
        q=iq.new_query("jabber:iq:version")
        q.newTextChild(q.ns(),"name","Echo component")
        q.newTextChild(q.ns(),"version","1.0")
        return iq


class Client(JabberClient):
    def __init__(self,jid,password):
        if not jid.resource:
            jid=JID(jid.node,jid.domain,"rbot")

        tls=TLSSettings(require=True,verify_peer=False)
        auth=['sasl:PLAIN']

        JabberClient.__init__(self,jid,password,disco_name='rbot',disco_type='bot',tls_settings=tls,auth_methods=auth)
        self.interface_providers=[VersionHandler(self),EchoHandler(self),]

    def stream_state_changed(self,state,arg):
        print "*** State changed: %s %r ***" % (state,arg)

    def print_roster_item(self,item):
        if item.name:
            name=item.name
        else:
            name=u''

        print (u'%s "%s" 订阅=%s 群组%s' % (unicode(item.jid),name,item.subscription,u','.join(item.groups)))


    def roster_updated(self,item=None):
        if not item:
            print u'花名册'
            for item in self.roster.get_items():
                self.print_roster_item(item)
            return
        print u'花名册更新完毕'
        self.print_roster_item(item)


def main():
    locale.setlocale(locale.LC_CTYPE,"")
    encoding=locale.getlocale()[1]
    if not encoding:
        encoding="us-ascii"
    sys.stdout=codecs.getwriter(encoding)(sys.stdout,errors="replace")
    sys.stderr=codecs.getwriter(encoding)(sys.stderr,errors="replace")

    if len(sys.argv) < 3:
        print u"Usage:"
        print "\t%s JID password" % (sys.argv[0],)
        print "example:"
        print "\t%s test@localhost verysecret" %(sys.argv[0],)
        sys.exit(1)

    print u'创建爱你客户端实例'
    c=Client(JID(sys.argv[1]),sys.argv[2])

    print u'开始连接服务器'
    c.connect()

    print u'开始监控'
    try:
        c.loop(1)
    except KeyboardInterrupt:
        print u'与服务器断开连接'
        c.disconnect()

    print u'退出程序'





if __name__ == "__main__":
    main()
