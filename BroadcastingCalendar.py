import datetime
import calendar
import time

from PySide6.QtWidgets import QTextBrowser, QApplication

import processDB
import requests
from lxml import etree
def viewCalendar(year,month,displayWidget:QTextBrowser,searchWord=None):
    rst = processDB.viewCalendarbyMonth(year,month)
    displayWidget.clear()
    oldDate = None
    for item in rst:
        shortDate = item[0][0:10] #截取前10位
        if shortDate != oldDate: # 当前日期变了
            displayWidget.append(shortDate)
        displayWidget.append('            ' + ' | ' + item[1] + ' | ' + item[2] + ' | ' + item[3])
        oldDate = shortDate



def refreshCalendar(year,month,displayWidget:QTextBrowser):
    strYearMonth1 = str(year)+'-'+str(month)+'-01'
    url = 'http://huo720.com/calendar?date='+strYearMonth1
    r = requests.get(url)
    # time.sleep(13)
    displayWidget.clear()
    displayWidget.append("访问网址："+url+"返回状态："+str(r.status_code))
    QApplication.processEvents()

    html = r.text
    txt = etree.HTML(html)
    theMonth, monthCountDay = calendar.monthrange(datetime.datetime.now().year, month)
    for idays in range(0, monthCountDay):
        currday = (datetime.datetime.strptime(strYearMonth1,"%Y-%m-%d") + datetime.timedelta(days=idays)).strftime('%Y-%m-%d')
        riqi ='"'+currday+'"'
        date_riqi = datetime.datetime.strptime(strYearMonth1,"%Y-%m-%d") + datetime.timedelta(days=idays)
        print(riqi)
        chNames = txt.xpath('//*[@id='+riqi+']/a/div/b/text()')
        enNames = txt.xpath('//*[@id='+riqi+']/a/div/div[1]/text()')
        SnEm = txt.xpath('//*[@id='+riqi+']/a/div/div[2]/div[1]/text()')
        ziped = zip(chNames,enNames,SnEm)
        for item in ziped:
            # print(item)
            chName,enName,sn = item
            if  len(chName)==0 or chName.isspace() :
                chName = enName
            if  len(enName)==0 or enName.isspace():  #网站会出现enName是空的，但是chName中写了英文名的情况
                print('哎呀哎呀')
                enName = chName
            processDB.addRecord_Calendar(date_riqi,enName,chName,sn)
            displayWidget.append(currday+"|"+ chName + "|"+ enName +"|"+sn)
            QApplication.processEvents()
            # print(currday+"|"+ chName + "|"+ enName +"|"+sn)

#测试
# refreshCalendar(2021,8)