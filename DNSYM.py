# coding:utf-8

import socket
import requests
import re
from colour import *

class DNSYM(object):

    def __init__(self,ip):
        self.ip = ip

    def DNS_ip(self):
        IP = socket.gethostbyname(self.ip)
        # return IP
        printGreen(u"[-] 域名IP地址")
        print IP

    def IP(self):
        IP = socket.gethostbyname(self.ip)
        return IP

    def IP_dZ(self):
        IP = socket.gethostbyname(self.ip)
        _ipdz = "http://ip.chinaz.com/?ip={}"
        _ipqq = _ipdz.format(IP)
        _jddz = requests.get(_ipqq)
        ip_text = _jddz.text
        zz = "<span class=\"Whwtdhalf w50-0\">(.*?)</span>"
        f = re.findall(zz, ip_text)
        for i in f:
            if re.findall('IP',i):
                ipcl = u'[+] ' + i
                printGreen(ipcl)
            else:
                print i
