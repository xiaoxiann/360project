#!/usr/bin/env python
#coding=utf-8
#实现对网站来源IP的统计
import re
from mrjob.job import MRJob
IP_RE=re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")  #定义IP正则表达式匹配
class Counter(MRJob):
    def mapper(self,key,line):
        for ip in IP_RE.findall(line): #匹配IP正则表达式以后生成key:value,其中key 为IP地址，value初始值为1
            yield ip,1

    def reducer(self,ip,occ):
        yield ip,sum(occ)
if __name__=="__main__":
    Counter.run()
~                                                                               
~             
