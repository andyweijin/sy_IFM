# coding:utf-8

import nmap

class DKSM(object):

    def __init__(self,ip,dk):
        self.ip = ip
        self.dk = dk
        self.nm = nmap.PortScanner()
        self.nm.scan(self.ip, self.dk)

    def host_nm(self):
        h_n = self.nm.all_hosts()
        return h_n

    def host_xy(self):
        h_x = self.nm[self.ip].all_protocols()
        return h_x

    def host_tc(self):
        for ipdz in self.host_nm():
            for xy in self.host_xy():
                dk_list = self.nm[ipdz][xy].keys()
                dk_list.sort()
                for port in dk_list:
                    print u'端口 : %s\t探测结果 : %s' % (port, self.nm[ipdz][xy][port]['state'])
