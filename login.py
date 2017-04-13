# -*- coding:utf-8 -*-
import requests
import getpass
print"Username:",
name = raw_input()
passwd = getpass.getpass('Password:')
payload = {'action': 'login', 'ac_id': '1','username': name,'password': passwd,'save_me':'0'}
r = requests.post('https://ipgw.neu.edu.cn/srun_portal_pc.php?url=&ac_id=1', data=payload)
res = r.text

if res.find(u'网络已连接'):
        print 'You are connected.'
else:
        print 'Unknown error'
