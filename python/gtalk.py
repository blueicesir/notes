#!/usr/bin/env python
# -*- coding:utf-8 -*-

__version__ = '0.1.20'

import sys
import os
import platform
import logging
import locale
import codecs
import ConfigParser
import re
import string

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
    def __init__(self,client,ini):
        self.client=client
        self.ini=ini

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


        if t=="chat" and body==None:
            return True


        if stanza.get_type()=='headline':
            return True

        if subject:
            subject=u'Re: '+subject


        if self.ini:
            db_host=self.ini['redis_host']
            db_port=self.ini['redis_port']
            db_num=self.ini['redis_dbid']
            db_auth=self.ini['redis_auth']
#            print "Redis DB %s:%s database index %s auth %s" %(db_host,db_port,db_num,db_auth)
        else:
            print "Redis DB not configuration"
            sys.exit(0)


        try:
            cmd=body
            regexp=re.compile('(get|keys)\s(.*)',re.I)
            key=regexp.match(body)  # 由于直接访问group(2)，如果成员不存在会抛出异常
            if key:
                key=key.group(2)
                db_num=6

            if cmd.startswith('get'):
                client=redis.Redis(host=db_host,port=db_port,db=db_num,password=db_auth)
                if key:
                    if client.exists(key):
                        body=client.get(key)
                    else:
                        body="get key not exists."
                else:
                    body="get execute fail"
            elif cmd.startswith('keys'):
                client=redis.Redis(host=db_host,port=db_port,db=db_num,password=db_auth)
                if key:
                    body=client.keys(key)
                    if len(body)!=0:
                        ret="\r".join(body)
                        body=ret
                    else:
                        body="key is not exists."
                else:
                    body="keys execute fail"
            else:
                print 'search chinese name'
                db_num=4
                client=redis.Redis(host=db_host,port=db_port,db=db_num,password=db_auth)
                body+=(":"+client.get(body).decode('utf-8'))
        except Exception,e: # 这种写法是不安全的，这样会淹没所有try到except中的异常，而且看不到那里出现的错误。
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
    def __init__(self,jid,password,ini):
        if not jid.resource:
            jid=JID(jid.node,jid.domain,"rbot")

        if ini:
            self.ini=ini

        tls=TLSSettings(require=True,verify_peer=False)
        auth=['sasl:PLAIN']

        JabberClient.__init__(self,jid,password,disco_name='rbot',disco_type='bot',tls_settings=tls,auth_methods=auth)
        self.interface_providers=[VersionHandler(self),EchoHandler(self,ini),]

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

    print u'创建客户端实例'
    ini=ParseIni()
    c=Client(JID(ini['name']),ini['password'],ini)
    print u'开始连接服务器'
    c.connect()

    print u'开始监控'
    try:
        c.loop(1)
    except KeyboardInterrupt:
        print u'与服务器断开连接'
        c.disconnect()

    print u'退出程序'


def ParseIni():
    ConfigParser.RawConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
    CFG=ConfigParser.ConfigParser()
    CFG_FILENAME=os.path.splitext(os.path.abspath(__file__))[0]+'.ini'
    CFG.read(CFG_FILENAME)
    gtalk_account=CFG.get('gtalk','account')
    gtalk_password=CFG.get('gtalk','password')
    db_host=CFG.get('redis','host')
    db_port=CFG.getint('redis','port')
    db_idx=CFG.getint('redis','db')
    db_auth=CFG.get('redis','auth')
    return {'name':gtalk_account,'password':gtalk_password,'redis_host':db_host,'redis_port':db_port,'redis_dbid':db_idx,'redis_auth':db_auth}




if __name__ == "__main__":
    main()
