__author__ = 'Administrator'

file = open("e:\\2.txt",'r')

i=1
w=''
for f in file.readlines():
    if i!=5:
        if i==4:
            w=w+f[:-1]+'\')'
        if i==3:
            w=w+f[:-1]+',\''
        if i==2:
            w=w+f[:-1]+'\','
        if i==1:
            w=w+f[:-1]+',\''
        i=i+1
    else:
        i=2
        print('INSERT INTO basicdata.weatherstation VALUES (',w)
        w=f[:-1]+',\''
file.close()
