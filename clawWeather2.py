# coding:utf-8
__author__ = 'Administrator'
import requests
import mysql.connector
from mysql.connector import errorcode
import datetime

# 获取网页内容
nanningurlstart = 'http://www.wunderground.com/history/airport/ZGNN/'
nanningurlend = '/15/MonthlyHistory.html?req_city=Nanning&req_state=&req_statename=China&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'
url1 = 'http://www.wunderground.com/history/wmo/54324/2007/2/15/MonthlyHistory.html?req_city=朝阳市&req_state=LN&req_statename=Liaoning&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=54324'
url2 = 'http://www.wunderground.com/history/wmo/54324/2007/2/15/MonthlyHistory.html?req_city=朝阳市&req_state=LN&req_statename=Liaoning&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=54324&format=1'
try:
    cnx = mysql.connector.connect(user='root', password='aaronlong',
                              host='127.0.0.1',
                              database='basicdata')
    cursor = cnx.cursor()
    for i in range(2000,2001):
        for j in range(2,4):
            r = requests.get(nanningurlstart+str(i)+'/'+str(j)+nanningurlend)
            data = r.text
            for weather in data.split('<br />')[1:-1]:
                record = weather.split(',')
                print(record)
                insertstr = 'insert into weatherday VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                record[0] = datetime.datetime.strptime(record[0],'\n%Y-%m-%d')
                record.append(59431)
                param = tuple(record)
                cursor.execute(insertstr,param)
                cnx.commit()

    cursor.close()
    cnx.close()
except requests.RequestException as e:
    print(e)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

