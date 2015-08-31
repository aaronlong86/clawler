__author__ = 'Administrator'
#!/usr/bin/env python
# coding:utf-8
import pymysql
from pymysql.connections import err
import requests
import datetime

# Connect to the database

def clawdailyweather(weatherstationcode,urlstart,urlend,year,month,prestatus):
    try:
        cnx,cursor = connectmysql()
        r = requests.get(urlstart+str(year)+'/'+str(month)+urlend)
        data = r.text
        recordlist = []
        dataempty = True
        for weather in data.split('<br />')[1:-1]:
            record = weather.split(',')
            record[0] = datetime.datetime.strptime(record[0],'\n%Y-%m-%d')
            for i in range(1,len(record)):
                if record[i]=='':
                    record[i] = None
                else:
                    dataempty = False
            record.append(weatherstationcode)
            param = tuple(record)
            recordlist.append(param)
        #prestatus(-1:never claw,0:claw success,1:fail 1 time,i:fail i times)
        if not dataempty:
            if prestatus!=0:
                insertstr = 'insert into weatherday VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                cursor.executemany(insertstr,tuple(recordlist))
                updatestr = 'update clawlog set status=%s where weatherstationcode=%s and year=%s and month=%s;'
                print(weatherstationcode,year,month,0)
                cursor.execute(updatestr,(0,weatherstationcode,year,month))
        else:
            if prestatus==-1:
                updatestr = 'update clawlog set status=%s where weatherstationcode=%s and year=%s and month=%s;'
                print(weatherstationcode,year,month,1)
                cursor.execute(updatestr,(1,weatherstationcode,year,month))
            elif prestatus!=0:
                updatestr = 'update clawlog set status=%s where weatherstationcode=%s and year=%s and month=%s;'
                print(weatherstationcode,year,month,prestatus+1)
                cursor.execute(updatestr,(str(prestatus+1),weatherstationcode,year,month))
        cnx.commit()
        cursor.close()
    finally:
        cnx.close()

def connectmysql():
    try:
        cnx = pymysql.connect(host='192.168.0.132',
                             user='root',
                             password='spjkyyzx2015',
                             db='basicdata',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = cnx.cursor()
        return cnx,cursor
    except err:
        print(err)

def startmission(weatherstationcode):
    try:
        cnx,cursor = connectmysql()
        querystr = 'select * from clawlog where weatherstationcode=%s;'
        cursor.execute(querystr,weatherstationcode)
        result = cursor.fetchall()
        param =[]
        if len(result)==0:
            for i in range(1996,2016):
                for j in range(1,13):
                    record = (weatherstationcode,i,j,-1)
                    param.append(record)
            inserstr = 'insert into clawlog VALUES (%s,%s,%s,%s)'
            cursor.executemany(inserstr,tuple(param))
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            querystr = 'select * from clawlog where weatherstationcode=%s and status<>%s;'
            cursor.execute(querystr,(weatherstationcode,0))
            for record in cursor.fetchall():
                param.append((record['weatherstationcode'],record['year'],record['month'],record['status']))
        return param
    except err:
        print(err)

#timesout:尝试timesout次后仍然失败停止
def clawall(weatherstationcode,urlstart,urlend,timesout):
    missions = startmission(weatherstationcode)
    for mission in missions:
        if mission[3]<timesout:
            clawdailyweather(mission[0],urlstart,urlend,mission[1],mission[2],mission[3])
"""
nanningurlstart = 'http://www.wunderground.com/history/airport/ZGNN/'
nanningurlend = '/15/MonthlyHistory.html?req_city=Nanning&req_state=&req_statename=China&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'
liuzhouurlstart = 'http://www.wunderground.com/history/wmo/59046/'
liuzhouurlend = '/15/MonthlyHistory.html?req_city=柳州市&req_state=GX&req_statename=Guangxi&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=59046&format=1'
nanningcode = 59431
liuzhoucode = 59046
timesout = 5
clawall(nanningcode,nanningurlstart,nanningurlend,timesout)
clawall(liuzhoucode,liuzhouurlstart,liuzhouurlend,timesout)
"""
wuzhouurlstart = 'http://www.wunderground.com/history/wmo/59265/'
wuzhouurlend = '/15/MonthlyHistory.html?req_city=梧州&req_state=GX&req_statename=Guangxi&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=59265&format=1'
wuzhoucode = 59265
timesout = 5
clawall(wuzhoucode,wuzhouurlstart,wuzhouurlend,timesout)

guilinstart = 'http://www.wunderground.com/history/airport/ZGKL/'
guilinend = '/15/MonthlyHistory.html?req_city=桂林&req_state=GX&req_statename=Guangxi&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=57957&format=1'
guilincode = 57957
clawall(guilincode,guilinstart,guilinend,timesout)