# coding:utf-8

import re
import requests

class BTXS(object):

    def __init__(self,ip):
        self.ip = ip

    def bt_xs(self):
        requ_http = 'http://'+ self.ip
        requ = requests.get(requ_http)
        requ_txt = requ.text
        regz = '<title>(.*?)</title>'
        requ_re = re.findall(regz,requ_txt)
        for i in requ_re:
            print '+ - + - + - + - + - + - + - + - + - + - + - +'
            print '测试 URL：',self.ip
            print '网站名称：',i
            print '+ - + - + - + - + - + - + - + - + - + - + - +'
