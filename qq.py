#!/usr/bin/env python
import os
import json
import subprocess
import urllib

#### init

poll=raw_input("poll:")+" 2>/dev/null"

send_hello=raw_input("send_hello:")+" 2>/dev/null"

s1,s2=send_hello.split("hello")

print "\n\n"

#### send message

def esc(t):
 while t[-1]==' ' or t[-1]=='\n' or t[-1]=='\t' or t[-1]=='\r':
  t=t[:-1]
 t=json.dumps(json.dumps(t,ensure_ascii=False),ensure_ascii=False)[3:-3]#not available for utf8
 t=urllib.quote(t)
 t=t.replace('<','%3C').replace('>','%3E')
 return t

def send(s,t):
 if s=='':
  return 0
 try : s=s.encode('utf8')
 except : pass
 if t:
  s=esc(s)
 print s
 os.system(s1+s+s2)
 return 0

#### analize poll

def ana(s):
 t=True
 if s=="tool" or s=="tools":
  return "http://trumpet-tools.cn.labxnow.org/"
 if s[0]=="#":
  s=subprocess.check_output(["curl http://trumpet-tools.cn.labxnow.org/python?run="+urllib.quote(s[1:])+" 2>/dev/null"],shell=True)
 if s[0]=="=":
  s=subprocess.check_output(["curl http://trumpet-mathkernel.cn.labxnow.org/?run="+urllib.quote(s[1:])+" 2>/dev/null"],shell=True)
 return s,t

def anapoll(i):
 if i["poll_type"]=="discu_message":
  if i["value"]["from_uin"]==711963687:
   s=i["value"]["content"][1].encode('utf8')
   s=s.replace('&lt;','<').replace('&gt;','>')
   s,t=ana(s)
   send(s,t)
 return 0

#### main

if __name__=="__main__":
 while True:
  d=subprocess.check_output([poll],shell=True)
  print d
  try:
   data=json.loads(d)
   pr=data['result']
  except:
   continue
  for i in pr:
   try:
    anapoll(i)
   except Exception,e:
    print e

