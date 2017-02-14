import os,sys,string
import poplib
import libgmail
from httplib2 import socks
import socket
socket.socket = socks.socksocket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",1080)

host = "pop.gmail.com"

username = "******"

password = "******"

pp = poplib.POP3_SSL(host)

# pp.set_debuglevel(1)

pp.user(username)

pp.pass_(password)

# print pp.list()

last_mail = pp.retr(151)
print 'lines:',len(last_mail)

for line in last_mail[1]:
    print line 


pp.quit()