import datetime

import requests
from lxml import etree
r = requests.get('http://huo360.cc/calendar?date=2021-06-01')
print(r.status_code)
html = r.text
txt = etree.HTML(html)

currday = (datetime.datetime.now() + datetime.timedelta(days=12)).strftime('%Y-%m-%d')
riqi ='"'+currday+'"'
print(riqi)
chNames = txt.xpath('//*[@id='+riqi+']/a/div/b/text()')
enNames = txt.xpath('//*[@id="2021-06-02"]/a/div/div[1]/text()')
SnEm = txt.xpath('//*[@id="2021-06-02"]/a/div/div[2]/div[1]/text()')
for item in chNames, enNames, SnEm:
    # print(item)
    print(item[0])
