__author__ = 'Administrator'
#!/usr/bin/env python
# coding:utf-8
import time
import os
import re
from pymysqldb import connectmysql

def get_log_status():  #得到日志表的status,weatherday的行数
    cnx,cursor = connectmysql()
    querystr = 'select DISTINCT status from clawlog;'
    cursor.execute(querystr)
    statusset = set()
    for cur in cursor:
        statusset.add(cur['status'])
    continueclaw = ({0,5}|statusset!={0,5})
    if statusset==set():
        continueclaw = True
    querystr = 'select count(*) from weatherday;'
    cursor.execute(querystr)
    for cur in cursor:
        weatherdaycount = cur['count(*)']
    return continueclaw,weatherdaycount


def get_pid(py_name):  #得到下载程序的pid
    command = 'ps axu|grep ' + py_name
    r = os.popen(command)
    mi = r.readlines()
    pid_key = ''
    pid_value = ''
    pid = {}
    for line in mi:
        line = line.strip('\r\n')
        if 'python' in line:
            pid_key = line.split('/')[-1]
            if re.findall(r'clawWeather3.py', line)!=[]:
                pid_value = re.findall(r'\s+(\d+)', line)[0]  #need change the name of user
                pid[pid_key] = pid_value
    if py_name in pid:
        return pid[py_name]
    else:
        return -1

py_name = 'clawWeather3.py'  #守护的下载数据的那个程序的文件名
i_count = 0
while 1:  #条件一直为真，循环运行这部分程序
    continueclaw1,weatherdaycount1 = get_log_status()  #第一次得到日志表的status,weatherday的行数
    print('get_log_1:',continueclaw1,weatherdaycount1)
    time.sleep(30)  #间隔时间，秒
    continueclaw2,weatherdaycount2 = get_log_status()  #第二次得到日志表的status,weatherday的行数
    print('get_log_2:',continueclaw2,weatherdaycount2)
    my_pid = get_pid(py_name)
    print('2 times is same?:',weatherdaycount1 == weatherdaycount2,'my_pid:',my_pid)
    if continueclaw2 and weatherdaycount1 == weatherdaycount2 and my_pid != -1:  #如果两次内容相同
        os.system('kill ' + str(my_pid))  #中断下载程序
        os.system('/usr/bin/python /home/clawweather/' + py_name + '&')  #重新运行，这里的'&'是必须的
        i_count += 1
        print('kill,this is the ' + str(i_count) + ' times to restart!')
    elif continueclaw2 and weatherdaycount1 == weatherdaycount2 and my_pid == -1:
        os.system('/usr/bin/python /home/clawweather/' + py_name + '&')  #重新运行，这里的'&'是必须的
        i_count += 1
        print('no kill,this is the ' + str(i_count) + ' times to restart!')
    elif not continueclaw2 and weatherdaycount1 == weatherdaycount2 and my_pid == -1:
        break
    print('the ' + str(i_count) + ' times is running...')
