import lxml
import requests
from lxml import etree
# 函数化



def outputXpath(URL,*Xpaths):
    '''
    如果给两个Xpath，则返回[{'title':'标题','link':'链接'}]
    如果参数只有一个Xpath，后面是空的 [{'title':'标题','link':''}]
    '''

    r = requests.get(URL)
    url_rst = r.status_code
    if url_rst != 200:
        return [{'title':'URL错误：','link':url_rst}]
    html = r.text
    txt = etree.HTML(html)

    dt = {}
    rst = [dt]
    titles = txt.xpath(Xpaths[0])
    if len(Xpaths)>1:
        links = txt.xpath(Xpaths[1])
        titles_links = zip(titles, links)
        for title, link in titles_links:
            dt['title'] = title.xpath('string(.)')
            dt['link'] = link.xpath('string(.)')
            rst.append(dt)
            # print(title.xpath('string(.)') + link.xpath('string(.)'))
            # print(rst)
    else: # 只有一个参数
        for title in titles:
            dt['title'] = title.xpath('string(.)')
            dt['link'] = ''
            rst.append(dt)

    return rst


#测试
# 两个参数
# rst = outputXpath('https://www.jsr9.com/subject/29500.html',"/html/body/div[@class='mb cl']/div[@class='ml']/div[@class='viewbox']/div[@class='sl cl']/div[@class='tinfo']/a/p[@class='torrent']","/html/body/div[@class='mb cl']/div[@class='ml']/div[@class='viewbox']/div[@class='sl cl']/div[@class='tinfo']/ul[@class='btTree treeview']")
# print(rst)
# 一个参数
# rst = outputXpath('https://www.jsr9.com/subject/29500.html',"/html/body/div[@class='mb cl']/div[@class='ml']/div[@class='viewbox']/div[@class='sl cl']/div[@class='tinfo']/a/p[@class='torrent']")
# print(rst)