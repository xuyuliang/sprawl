import lxml
import requests
from lxml import etree
# 函数化



def outputXpath(URL,Xpath_title,Xpath_link):
    ''' 返回一个[{'title':'标题','link':'链接'}] '''
    r = requests.get(URL)
    print(r.status_code)
    html = r.text
    txt = etree.HTML(html)

    titles = txt.xpath(Xpath_title)
    links = txt.xpath(Xpath_link)
    titles_links = zip(titles,links)
    dt = {}
    rst = [dt]
    for title,link in titles_links:
        dt['title'] = title.xpath('string(.)')
        dt['link'] = link.xpath('string(.)')
        rst.append(dt)
        # print(title.xpath('string(.)') + link.xpath('string(.)'))
        # print(rst)
    return rst


#测试

outputXpath('https://www.jsr9.com/subject/29500.html',"/html/body/div[@class='mb cl']/div[@class='ml']/div[@class='viewbox']/div[@class='sl cl']/div[@class='tinfo']/a/p[@class='torrent']","/html/body/div[@class='mb cl']/div[@class='ml']/div[@class='viewbox']/div[@class='sl cl']/div[@class='tinfo']/ul[@class='btTree treeview']")
