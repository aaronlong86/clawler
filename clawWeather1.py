#! /usr/bin/python
# coding=utf-8
__author__ = 'Administrator'
import urllib.request
import json

def getweatherInfo(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode('utf-8')
    weatherJSON = json.JSONDecoder().decode(html)
    weatherInfo = weatherJSON['weatherinfo']
    return weatherInfo

def printweather(weatherInfo):
    print('')
    print('城市：\t',weatherInfo['city'])
    print('更新时间：',weatherInfo['time'])
    print('实时温度：\t', weatherInfo['temp'])
    print('风向：\t', weatherInfo['WD'])
    print('风速：\t', weatherInfo['WS'])
    print('湿度：\t', weatherInfo['SD'])


weatherInfo = getweatherInfo('http://www.weather.com.cn/adat/sk/101010100.html')
printweather(weatherInfo)
weatherInfo = getweatherInfo('http://www.weather.com.cn/adat/sk/101030100.html')
printweather(weatherInfo)
weatherInfo = getweatherInfo('http://www.weather.com.cn/adat/sk/101300101.html')
printweather(weatherInfo)

