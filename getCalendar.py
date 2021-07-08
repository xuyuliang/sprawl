import datetime
import calendar
import time

import processDB
import requests
from lxml import etree
def refreshCalendar(year,month):
    strYearMonth1 = str(year)+'-'+str(month)+'-01'
    url = 'http://huo720.com/calendar?date='+strYearMonth1
    r = requests.get(url)
    # time.sleep(13)
    print(r.status_code)

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
            print(item)
            chName,enName,sn = item
            processDB.addRecord_Calendar(date_riqi,enName,chName,sn)
            print(currday+"|"+ chName + "|"+ enName +"|"+sn)

#测试
refreshCalendar(2021,8)