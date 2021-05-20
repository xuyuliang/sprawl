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

### 处理play表
# （1）写入一本剧
# （2）删除一本剧，连带删除相关的所有season
# （3）显示一本剧，连带显示所有的season
# （4） 显示你收藏的所有剧

def addPlay(ID,name,memotxt):
    sql = "insert into play(ID,name,memotxt) values(?,?,?)"
    cur.execute(sql, [ID,name,memotxt])
    conn.commit()

def deletePlay(ID):
    sql1 = "delete from play where ID = ?"
    sql2 = "delete from season where playID = ?"
    cur.execute(sql1,[ID])
    cur.execute(sql2,[ID])
    conn.commit()

def fetchPlayandSeasons(ID):
    sql1 = "select name,memotxt from play where ID = ?"
    sql2 = "select ID,name from season where playID = ?"
    cur.execute(sql1,[ID])
    result1 = cur.fetchall()
    cur.execute(sql2,[ID])
    result2 = cur.fetchall()
    print("play:",result1)
    print("seasons:",result2)
    return (result1,result2)

# addPlay(1,'Young Sheldon','备注 小谢尔顿')
# s1,s2 = fetchPlayandSeasons(1)
# print(s1)  # [('Young Sheldon', '备注 小谢尔顿')]
# print(s2)  # [(4, 'Young Sheldon 第四季'), (5, 'Young Sheldon 第三季')]

### 处理season表
# （1）写入一个新season ， 需要传入playID，season的name，
# （2）修改 ；不要修改了，删了重写
# （3）删除

def addSeason(name,playID):
    sql = "insert into season(name,playID) values(?,?)"
    cur.execute(sql,[name,playID])
    conn.commit()

def deleteSeason(ID):
    sql = "delete from season where ID = ? "
    cur.execute(sql,[ID])
    conn.commit()

# addSeason('Young Sheldon 第一季',1)
# fetchPlayandSeasons(1)
deleteSeason(6)
fetchPlayandSeasons(1)
