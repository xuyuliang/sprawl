import sqlite3
conn = sqlite3.connect("play.db")
cur = conn.cursor()

def createTables():
    # （1）当季剧表season
    sql= "create table season(ID integer primary key,name text,calendarID integer,downloadID integer,mainID integer);"
    cur.execute(sql)
    # （2）剧表play
    # ID、seasonID、name、memotxt 下一季什么时候开始等等
    sql = "create table play(ID integer primary key,seasonID integer,name text,memotxt text);"
    cur.execute(sql)
    # （3）日期表calendar
    # seasonID、dueDate计划播出日期
    sql = "create table calendar(seasonID integer,dueDate date); "
    cur.execute(sql)
    # （4）下载网址表 dowload
    # seasonID、Xpath
    sql = "create table dowload(seasonID integer,Xpath text); "
    cur.execute(sql)
    # （5）
    sql = 'CREATE TABLE progress(playID INTEGER,seasonID INTEGER,currDate date);'
    cur.execute(sql)

def test_insert():
    #sql = "insert into season(ID,name,calendarID,downloadID,mainID) values(null,'Young Sheldon 第四季',1,1,1);"
    sql = "insert into progress(seasonID,currDate) values(?,?);"
    cur.execute(sql,(1,'2021-05-22'))
    conn.commit()

# 测试

def test_select():
    # sql ="select * from season;"
    sql = "select * from progress;"
    cur.execute(sql)
    print(cur.fetchall())


# createTables()
test_insert()
# test_select()

