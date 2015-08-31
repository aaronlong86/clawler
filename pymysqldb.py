__author__ = 'Administrator'
#!/usr/bin/env python
# coding:utf-8
import pymysql
from pymysql.connections import err
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