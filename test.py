# coding:utf-8
__author__ = 'Administrator'
"""
import re
import datetime
nanningurlstart = 'http://www.wunderground.com/history/airport/ZGNN/'
nanningurlend = '/15/MonthlyHistory.html?req_city=Nanning&req_state=&req_statename=China&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'
url1 = 'http://www.wunderground.com/history/wmo/54324/2007/2/15/MonthlyHistory.html?req_city=朝阳市&req_state=LN&req_statename=Liaoning&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=54324'
url2 = 'http://www.wunderground.com/history/wmo/54324/2007/2/15/MonthlyHistory.html?req_city=朝阳市&req_state=LN&req_statename=Liaoning&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=54324&format=1'
for i in range(1997,2015):
    for j in range(1,13):
        s=(nanningurlstart+str(i)+'/'+str(j)+nanningurlend)
        print(s)
record = ["2017-2-1"]
print(record[0])
recordday = datetime.datetime.strptime(record[0],"%Y-%m-%d")
print(recordday)
"""
from clawWeather3 import clawall

urlstart = 'http://www.wunderground.com/history/wmo/59046/'
urlend = '/15/MonthlyHistory.html?req_city=柳州市&req_state=GX&req_statename=Guangxi&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=59046&format=1'
weatherstationcode = 59046
timesout = 5
clawall(weatherstationcode,urlstart,urlend,timesout)
