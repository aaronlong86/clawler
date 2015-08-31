__author__ = 'Administrator'
#coding=utf-8
import urllib.request
import re
"""
urllib.request模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据。
首先，我们定义了一个getHtml()函数:urllib.request.urlopen()方法用于打开一个URL地址。
read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来。
"""
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode('utf-8')
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)#把正则表达式编译成一个正则表达式对象
    imglist = re.findall(imgre,html)#读取html 中包含 imgre（正则表达式）的数据
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)#将远程数据下载到本地
        x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print(getImg(html))
