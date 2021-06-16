import requests
from lxml import etree
# 函数化
def showHTMLsnippet(URL,Xpath):
    r = requests.get(URL)
    print(r.status_code)
    html = r.text
    txt = etree.HTML(html)
    txt2 = txt.xpath(Xpath)
    dt=[]
    for t in txt2[0:]:
        row = []
        title1 = t.xpath('p/text()[1]')[0]
        title2 = t.xpath('p/em/text()')[0]
        title = title1+title2
        # print(title)

        url = t.xpath('@href')[0]
        row.append(title)
        row.append(url)
        dt.append(row)

    for item in dt :
        print(item)
#测试
showHTMLsnippet('https://www.jsr9.com/subject/29500.html','/html/body/div[2]/div[1]/div[2]/div[3]/div/a')