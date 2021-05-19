import datetime
import sqlite3
conn = sqlite3.connect("play.db")
cur = conn.cursor()

### 处理当前进度
def recordCurrPos(seasonID):
    sql = "insert into progress(seasonID,currDate) values(?,?)"
    currDate = datetime.datetime.now().strftime('%Y-%m-%d')
    print(currDate)
    cur.execute(sql, [seasonID, currDate])
    conn.commit()

def delCurrPos(seasonID,currDate):
    sql = "delete from progress where seasonID = ? and currDate = ?"
    tup = (seasonID,currDate)
    cur.execute(sql,tup)
    conn.commit()

# recordCurrPos('21')
# delCurrPos(1, '2021-05-22')

### 处理下载网址
# （1）写入下载网址
# （2）修改下载网址
# （3）根据id删除某个网址
# （4）删除某个seasonID的所有网址
# 因为有ID，所以可以写多个网址

def addDownloadURL(seasonID,URL,Xpath):
    sql = "insert into download(seasonID,URL,Xpath) values(?,?,?)"
    cur.execute(sql, [seasonID, URL,Xpath])
    conn.commit()

def modifyDownloadURL(ID,URL,Xpath):
    print(URL)
    print(Xpath)
    sql = "update download set URL=? , Xpath=? where ID = ?"
    cur.execute(sql,[URL,Xpath,ID])
    conn.commit()

def deleteDownloadbyID(ID):
    sql = "delete from download where ID = ?"
    cur.execute(sql,[ID])
    conn.commit()

def deleteDownloadbySeasonID(seasonID):
    sql = "delete from download where SeasonID = ?"
    cur.execute(sql,[seasonID])
    conn.commit()

# addDownloadURL(1,r"http://www.slupro.com/meiju/328724",r"/html/body/div[1]/div/ul[2]")
# modifyDownloadURL(1,r'https://www.jsr9.com/subject/29500.html',r'/html/body/div[2]/div[1]/div[2]/div[3]/div/a')
# deleteDownloadbyID(1)
# deleteDownloadbySeasonID(1)

