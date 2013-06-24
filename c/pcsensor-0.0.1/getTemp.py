#!/usr/bin/env python
#-*- coding:utf-8 -*-
# json='{"tempstamp":"2013-06-04T12:13:14","value":39.5}'

import base64
import urllib
import urllib2
import httplib
import sys,os
import subprocess
import re
import sqlite3
import json

import prowlpy


if sys.version[0]=='2':
    import ConfigParser
else:
    import configparser as ConfigParser

def iOSPushMsg(apikey,json_str,top_level):
    c1=float(json_decode(json_str)['c'])
    print "[%s]-> iOS PushMsg input c=%f"%(getTime(),c1,)
    if float(c1)<float(top_level):
        return None
    else:
        print "[%s]-> Call iOSPushMsg to Prowl"%(getTime(),)
    p=prowlpy.Prowl(apikey)
    try:
        p.add(u'温度告警',u'Warning',"Content", 1, None, "http://www.yeelink.net/devices/3291/")
        return True
    except Exception,msg:
        print "[%s]-> iOSPushMsg Except:%s"%(getTime(),msg,)
        return None

def warning_rpc(enable,warn_uri,json_str,warn_level,warn_addr):
    if int(enable)==0:
        return False

    ct=json_decode(json_str)
    if float(ct['c'])<float(warn_level):
        return None
    else:
        print "[%s]-> Call Warning RCP (%f)"%(getTime(),float(ct['c']),)

    try:
        warn_req=urllib2.Request(warn_uri)
        warn_req.get_method=lambda:'POST'
        warn_req.add_header('User-Agent','RaspberryPi')
        post_data=urllib.urlencode({'tempstamp':ct['t'],'value':ct['c'],'addr':warn_addr})
        warn_resp=urllib2.urlopen(warn_req,post_data,timeout=10)
        if warn_resp.getcode()==200:
            return True
        else:
            return None
    except urllib2.HTTPError,e:
        print "[%s]-> Warning RPC Call Response fail,error code %i " % (getTime(),e.code,)


def post_data(json):
    ConfigParser.RawConfigParser.OPTCRE=re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
    CONFIG=ConfigParser.ConfigParser()
    CONFIG_FILENAME=os.path.splitext(os.path.abspath(__file__))[0]+'.ini'
    CONFIG.read(CONFIG_FILENAME)
    sqlite_file=CONFIG.get('history','sqlite_db')
    sqlite_table=CONFIG.get('history','table_name')

    warning_enable=CONFIG.getint('warning','enable')
    warning_eq_max=CONFIG.get('warning','top')
    warning_uri=CONFIG.get('warning','uri')
    warning_addr=CONFIG.get('warning','addr')

    prowl_apikey=CONFIG.get('prowl','apikey')

    log_localdb(sqlite_file,sqlite_table,json)
    warning_rpc(warning_enable,warning_uri,json,warning_eq_max,warning_addr)
    iOSPushMsg(prowl_apikey,json,warning_eq_max)


    device_id=CONFIG.get('device','id')
    sensor_id=CONFIG.get('sensor','id')
    api_key_val=CONFIG.get('api','key')
    api_key="U-ApiKey"
    uri="http://api.yeelink.net/v1.0/device/%s/sensor/%s/datapoints" %(device_id,sensor_id)

    try:
        print "[%s]-> %s"% (getTime(),uri,)
        print "[%s]-> %s" %(getTime(),json,)
        request=urllib2.Request(uri,data=json)
        request.get_method=lambda:'POST'
        request.add_header(api_key,api_key_val)
        request.add_header('Content-Type','application/json')
        response=urllib2.urlopen(request,timeout=10)
        if response.getcode()==200:
            return True
        else:
            print "[%s]-> Response return code %i"%(getTime(),response.getcode(),)
            print "[%s]-> Response Content-Text:%s"%(getTime(),response.read().strip(),)
            return None
    except urllib2.HTTPError,e:
        print "[%s]-> Response fail,error code %i " % (getTime(),e.code,)
        return None

def getTime():
    import time
    Now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return Now

def readTemp():
    output=subprocess.Popen(["/bin/pcsensor","-c"],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
    if output not in "failed":
        output2=output.split()
        date=output2[0].replace('/','-')
        time="%sT%s"%(date,output2[1],)
        tempC=output2[3].replace('C','')
        return '{"tempstamp":"%s","value":%s}' % (time,tempC,)
    else:
        return None

def json_decode(json_str):
    js=json.JSONDecoder()
    myval=js.raw_decode(json_str)
    return {"t":myval[0]['tempstamp'],"c":str(myval[0]['value'])}

def log_localdb(db_file,db_table,json_str):
    db=sqlite3.connect(db_file)
    cur=db.cursor()
    cur.execute("select count(*) from sqlite_master where type='table' and name='%s'"%(db_table,))
    numbers=cur.fetchone()
    if numbers[0]==0:
        print "create table %s in %s data file." %(db_tables,db_file,)
        cur.execute("create table %s (tempstamp varchar(19) PRIMARY KEY,c text)"%(db_table,))
    dumy=json_decode(json_str)
    cur.execute("insert into %s (tempstamp,c) values('%s','%s')"%(db_table,dumy['t'],dumy['c']))
    db.commit()
    db.close()
    print "[%s]-> Write Data to local sqlite."%(getTime(),)


if __name__=="__main__":
    r=readTemp()
    if r:
        if post_data(r):
            print "[%s]-> Push data successful" %(getTime(),)
        else:
            print "[%s]-> Push data fail"%(getTime(),)
    else:
        print "[%s]-> Read Templater fail"%(getTime(),)
