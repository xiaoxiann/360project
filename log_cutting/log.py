利用mrjob框架编写mapreduce任务，实现日志中快速获取访问流量，用户IP信息，连接数分钟统计。
安装mrjob:   pip install mrjob
下面是一个例子，实现从日志中访问流量的统计
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
运行结果：
[root@desktop0 answer]# python log.py /var/log/httpd/access_log-20160313 -o output.txt
[root@desktop0 answer]# cat output.txt/part-00000 
"05:58"	3985
"05:59"	198
"06:00"	198
"22:40"	3989
"22:40"	3967
"22:40"	3989
"22:40"	3981
"22:40"	3995
"23:03"	174676
"03:01"	4171104
"03:01"	899592

实现对网站来源IP的统计：
#!/usr/bin/env python
#coding=utf-8
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
   
 运行结果：
 python log_ip.py /var/log/httpd/access_log-20160322 -o output.txt2
[root@desktop0 answer]# cat output.txt2/part-00000 
"1.8.7.352"	12
"127.0.0.1"	43
"172.25.254.112"	20
"172.25.254.224"	31
"172.25.254.5"	52

项目解析：
Mrjob支持四种运行方式，內嵌（-r inline）,本地（-r local） ,hadoop(-r hadoop) ,Amazon(-r  emr). 默认为-r inline可以省略
当web日志数量较大的时候，可以采用定期上传web日志到HDFS存储平台，实现分布式计算：
安装jdk环境，搭建hadoop平台，
部署hadoop:
1）安装部署实现master主机访问slave主机无密码登录（配置帐号公钥）
2）修改四个核心文件：
Hadoop_env.sh: hadoop环境变量配置文件，指定JAVA_HOME
Core-site.xml: 主要针对Common组件的属性配置，
Hdfs-site.xml: hadoop的HDFS组件的配置项，包括Namenode,datanode
Mapred-site.xml: 配置map-reduce组件的属性，包括jobtracker和tasktracker.
Master和slave分别写入对应主机IP
HDFS上传文件例如：bin/hadoop fs -put /home/test/hadoop/*.txt  /data/root/test

缺点：如果需要大量的计算的话，python可能会慢很多（语言级别上的慢）。

同样实现对日志的分割也可以用awk实现，awk是一个强大的报告生成器

例如实现对文件中IP的访问量
[root@server0 httpd]#   awk '{count[$1]++} END {for(ip in count) {printf "%-10s%s\n",ip,count[ip]}}' access_log-20160319
172.25.254.1802
172.25.254.1532

 
 


