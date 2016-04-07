#!/usr/bin/python
import os
key=[]
ip=[]
key_ip={}
filename=os.popen('ifconfig')
lines=filename.readlines()
for line in lines:
    if line[0]!=' ' and line[0]!='\n':
        key1=line.split(':')
        key.append(key1[0])
for line in lines:
    if 'netmask' in line:
        row=line.strip()
        ip1=row.split()
        ip.append(ip1[1])
for i in range(len(key)):
    key_ip[key[i]]=ip[i]
print key_ip

运行结果：
root@server0 mimi`]# python ifconfig.py
{'lo': '127.0.0.1', 'ens7': '172.25.254.1', 'eth0': '172.25.254.180'}
