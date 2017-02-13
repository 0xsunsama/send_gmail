import smtplib
from httplib2 import socks
import socket
socket.socket = socks.socksocket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",1080)
# The below code never changes, though obviously those variables need values.
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login("********", "*******")
 
headers = "\r\n".join(["from: " + "********",
            "subject: " + "hello"
            "to: " + "*******",
            "mime-version: 1.0",
            "content-type: text/html"])
 
# body_of_email can be plaintext or html!          
content = headers + "\r\n\r\n" + "hello"
session.sendmail("sunsama1995@gmail.com", "691367132@qq.com", content)
