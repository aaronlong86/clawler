__author__ = 'Administrator'
# coding:utf-8
import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='aaronlong',
                              host='127.0.0.1',
                              database='basicdata')
    cursor = cnx.cursor()
    cursor.execute("select * from weatherstation;")
    #这种方式必须要列出所有的返回列，否则报错
    for (idweatherstation,province,stationcode,stationname) in cursor:
        print("{}在{}省，代码为：{}".format(stationname,province,stationcode))
    cursor.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
  cnx.close()