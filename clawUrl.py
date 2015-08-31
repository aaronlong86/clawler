__author__ = 'Administrator'
# coding:utf-8
import re
import requests

# 获取网页内容
r = requests.get('http://www.baidu.com')
data = r.text

# 利用正则查找所有链接
link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
for i,url in enumerate(link_list):
    print(i,url)

