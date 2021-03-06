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
def selectDowloadURLbySeasonID(SeasonID:int):
    sql = "select id,seasonid,URL, Xpath_title, Xpath_link from download where seasonid = ? "
    cur.execute(sql,[SeasonID])
    return cur.fetchall()
# print( selectDowloadURLbySeasonID(274) )

def insert_modifyDownloadURL(ID,seasonID,URL,Xpath_title,Xpath_link):
    ''' 若已经存在id，就modify，返回None; 否则insert，返回insert的结果。 '''
    sql = "select * from download where ID = ?"
    cur.execute(sql,[ID])
    rst = cur.fetchall()
    print(rst,len(rst) == 0)
    if (len(rst) == 0) :
        rst = addDownloadURL(seasonID,URL,Xpath_title,Xpath_link)
    else:
        modifyDownloadURL(ID,URL,Xpath_title,Xpath_link)
        rst = None
    return rst


def addDownloadURL(seasonID,URL,Xpath_title,Xpath_link):
    '''  返回表的第一个元素即ID '''
    sql = "insert into download(seasonID,URL,Xpath_title,Xpath_link) values(?,?,?,?)"
    cur.execute(sql, [seasonID, URL, Xpath_title, Xpath_link])
    conn.commit()
    sql = "select ID,seasonID,URL, Xpath_title, Xpath_link from download where seasonID=? and URL=? and Xpath_title=? and Xpath_link=?"
    cur.execute(sql,[seasonID, URL, Xpath_title, Xpath_link])
    rst = cur.fetchone()
    # print('addDownloadURL的ID',rst[0])
    return rst[0]


def modifyDownloadURL(ID,URL, Xpath_title, Xpath_link):
    print(URL)
    print( Xpath_title, Xpath_link)
    sql = "update download set URL=? ,Xpath_title=?, Xpath_link=? where ID = ?"
    cur.execute(sql,[URL, Xpath_title, Xpath_link,ID])
    conn.commit()

def deleteDownloadbyID(ID):
    sql = "delete from download where ID = ?"
    cur.execute(sql,[ID])
    conn.commit()

def deleteDownloadbySeasonID(seasonID):
    sql = "delete from download where SeasonID = ?"
    cur.execute(sql,[seasonID])
    conn.commit()

# addDownloadURL(1,r"http://www.slupro.com/meiju/328724",r"/html/body/div[1]/div/ul[2]",r"/下载链接")
# modifyDownloadURL(1,r'https://www.jsr9.com/subject/29500.html',r'/html/body/div[2]/div[1]/div[2]/div[3]/div/a',r'什么什么')
# deleteDownloadbyID(1)
# deleteDownloadbySeasonID(1)
# insert_modifyDownloadURL(-1,274,'xxx','yyy','new')

### 处理play表
# （1）写入一本剧，表示我正在追这本剧
# （2）删除一本剧，表示不追了
# （3）更新一本剧
# （4）显示所有收藏的剧集并联动下载打卡日期

def addPlay(seasonID,name,memotxt):
    sql1 = "insert into play(name,memotxt) values(?,?)"
    cur.execute(sql1, [name,memotxt])
    playid = cur.lastrowid
    sql2 = "update season set playid=? where ID =? "
    cur.execute(sql2,[playid,seasonID])

    conn.commit()

def deletePlay(ID):
    sql1 = "delete from play where ID = ?"
    cur.execute(sql1,[ID])
    conn.commit()

def updatePlay(ID,name,memotxt):
    sql = "update play set name=? , memotxt = ? where ID = ?"
    cur.execute(sql,[name,memotxt,ID])
    conn.commit()

def showFavoritesWithChaseDate():
    sql = ''' 
    SELECT p.ID, p.name, p.memotxt, min(c.dueDate) as due, pg.currDate
    from play as p INNER JOIN season as s on p.id = s.playID 
	LEFT OUTER JOIN progress as pg on s.id = pg.seasonID
	INNER JOIN calendar as c on s.id = c.seasonID
	where c.dueDate > CURRENT_DATE
	group by p.id
    '''
    cur.execute(sql)
    rst = cur.fetchall()
    print(rst)
    return rst

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

# addPlay(274,'Young Sheldon','备注 小谢尔顿')
showFavoritesWithChaseDate()
# s1,s2 = fetchPlayandSeasons(1)
# print(s1)  # [('Young Sheldon', '备注 小谢尔顿')]
# print(s2)  # [(4, 'Young Sheldon 第四季'), (5, 'Young Sheldon 第三季')]

### 处理season表
#  (0) 默认显示收藏的剧集
# （1）写入一个新season ， 需要传入playID，season的name，
# （2）修改 ；不要修改了，删了重写
# （3）删除
def showFavoriteSeasons():
    sql = '''
    select  s.ID ,s.enName,s.chName,c.dueDate 
    from (Season s inner join calendar c on s.id = c.seasonid ) 
    INNER join progress p on s.id = p.seasonID 
    where S.valid is true 
    and p.currDate < c.dueDate 
    and c.dueDate < ?
    '''
    # currDate = datetime.datetime.now().strftime('%Y-%m-%d')
    currDate = datetime.datetime.now()
    cur.execute(sql,[currDate])
    rows = cur.fetchall()
    return rows

# rows = showFavoriteSeasons()
# print(rows)
# for r in rows:
#     print(r)
def selectSeasonByName(name):
    sql = "select id,enName,chName,valid from season " \
    "where enName like ? or chName like ?"
    cur.execute(sql,["%"+name+"%","%"+name+"%"])
    rows = cur.fetchall()
    return rows

# print(selectSeasonByName('love'))

def addSeason(enName,chName):
    sql = "select ID from season where enName=? and chName=?"
    cur.execute(sql,[enName,chName])
    rows = cur.fetchone()
    # print('addSeason',rows,rows[0])
    seasonID = 9999
    if rows is None:  # 没有
        sql = "insert into season(enName,chName) values(?,?)"
        cur.execute(sql,[enName,chName])
        seasonID = cur.lastrowid
        print('in addSeason, lastrowid:',seasonID)
        conn.commit()
    else:
        seasonID = rows[0]
    return seasonID

def deleteSeason(ID):
    sql = "delete from season where ID = ? "
    cur.execute(sql,[ID])
    conn.commit()

def updateSeason(ID,enName,chName,valid):
    sql = "update season set enName=? , chName=? , valid=? where ID =?"
    cur.execute(sql,[enName,chName,valid,ID])
    conn.commit()


# n = addSeason('breaking bad','极品毒师')
# print(n)
# fetchPlayandSeasons(1)
# deleteSeason(6)
# fetchPlayandSeasons(1)
# updateSeason(274,'Young Sheldon season 4','小谢尔顿 第四季','1')
### 处理日历calendar
# 写入一条记录
def direct_insert_calendar(seasonID,dueDate,SnEm):
    sql = "select * from calendar where seasonID=? and dueDate =? and SnEM=?"
    print('direct_insert_calendar',seasonID,dueDate,SnEm)
    cur.execute(sql,[seasonID,dueDate,SnEm])
    re = cur.fetchall()
    if len(re) > 0 :
        return
    sql = "insert into calendar(seasonID,dueDate,SnEm) values(?,?,?)"
    cur.execute(sql,[seasonID,dueDate,SnEm])
    conn.commit()

def addRecord_Calendar(dueDate, enName, chName, sn):
    seasonID = addSeason(enName,chName)
    direct_insert_calendar(seasonID,dueDate,sn)


def viewCalendarbyMonth(year,month):
    sql = '''
    select  c.dueDate, s.enName,s.chName, c.SnEm 
    from calendar c INNER JOIN season s 
    on c.seasonID = s.id
    where c.dueDate >= ? and c.dueDate < ?
    ORDER by c.dueDate ,enName,chName,SnEm
    '''
    beginDate = datetime.date(year,month,1)
    if month == 12:
        endDate = datetime.date(year+1,1,1)
    else:
        endDate = datetime.date(year,month+1,1)
    cur.execute(sql,[beginDate,endDate])
    rst = cur.fetchall()
    return rst

# a = viewCalendarbyMonth(2021,8)
# for i in a:
#     print(i)

# sriqi = "2021-06-01"
# addRecord_Calendar(sriqi,"Young Sheldon 第四季","洋谢尔顿 第四季","s4e5")
# direct_insert_calendar(1,sriqi,'haha')

### 多表组合查询

def findBroadcastingSchedule(seasonID):
    sql = ''' select enName,chName,dueDate,SnEm from season 
              INNER join calendar on season.ID = calendar.seasonID 
              and seasonID = ? '''
    cur.execute(sql,[seasonID])
    result = cur.fetchall()
    return result

# tt = findBroadcastingSchedule(109)
# for t in tt:
#     print(t)