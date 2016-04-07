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


