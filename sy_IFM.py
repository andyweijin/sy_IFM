# coding:utf-8

from DNSYM import *
from DKSM import *
import time,sys
from urlparse import urlparse
from colour import *
from BTXS import *

printBlue('''
/¯¯¯¯¯/ '|¯¯¯|¯¯¯|    O    \¯¯¯|¯¯¯/|    /¯¯¯¯¯| |¯¯¯\|¯¯¯| 
\ __¯¯¯\' |       |°|¯¯¯¯|  \     /    /   !   | |       '||
/______/||___|___|  |____|   |___|'  /___/¯|__'| |___|\___| 

''')
# url = 'http://sh1yan.top/'
_ym = "%s" %(sys.argv[1])
a = urlparse(_ym)
b = a.netloc
ks = BTXS(b)
ks.bt_xs()
time.sleep(1)
printGreen(u'[+] 正在探测域名IP地址和物理地址中...')
time.sleep(1)
c = DNSYM(b)
c.DNS_ip()
c.IP_dZ()
printGreen(u'[-] 正在扫描域名开放端口中...')
cc = c.IP()
d = DKSM(cc,'0-100')
d.host_tc()
printGreen(u'[+] 结束所有探测')
