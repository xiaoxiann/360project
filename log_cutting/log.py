
#实现从日志中访问流量的统计
#!/usr/bin/env python
#coding=utf-8
import re
from mrjob.job import MRJob
class MYCounter(MRJob):
    def mapper(self,Key,line):
	    i=0
	    for flow in line.split():
		if i==3: #获取时间字段，位于日志的第4列   
		    timerow=flow.split(":")
		    hm=timerow[1]+":"+timerow[2] #获取“小时:分钟”，作为key
		if i==9 and re.match(r"\d{1,}",flow):   #获取日志的第十列-发送字节数
		    yield hm,int(flow)  #相同key "小时:分钟"的value作累加操作
		i+=1
def reducer(self,key,occ):
    yield key,sum(occ)
if __name__=="__main__":
    MYCounter.run() 




 


