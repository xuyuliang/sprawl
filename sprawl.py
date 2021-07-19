import datetime
from time import strftime

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import Qt, QTextDocument, QTextCharFormat, QBrush, QColor, QTextCursor

import processDB
import showHTMLsnippet
import BroadcastingCalendar
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView, QTextBrowser
from ui_sprawl import Ui_MainWindow

# 公用的函数们

def getCurrColumnName(table:QTableWidget):
    current_col = table.horizontalHeaderItem(table.currentColumn()).text()
    # print(current_col)
    return current_col

def appendRow(table:QTableWidget,lineData):
    ''' 在给定的table上新增一个空行 '''
    newrow = table.rowCount()
    print('newrow', newrow)
    table.insertRow(newrow)
    for j in range(len(lineData)):
        # print(i,j,currdata)
        currdata = lineData[j]
        item = QtWidgets.QTableWidgetItem()
        item.setData(0, currdata)
        table.setItem(newrow, j, item)

def write_table_current_line(table:QTableWidget,data:[]):
    ''' 在QTableWidget的当前行写入data中的数据，若没选中行，返回None'''
    if table.currentItem() is None:
        return None
    cols = table.columnCount()
    curr_row = table.currentItem().row()
    try:
        table.blockSignals(True)
        for j in range(cols):
            currdata = data[j]
            item = QtWidgets.QTableWidgetItem()
            item.setData(0, currdata)
            table.setItem(curr_row, j, item)
        return 'good'
    finally:
        table.blockSignals(False)

def read_table_current_line(table: QTableWidget):
    ''' 读取当前QTableWidget选中的行，若没选中，返回空dict{} '''
    if table.currentItem() is None:
        return None
    cols = table.columnCount()
    curr_row = table.currentItem().row()
    # 得出当前行的dict   如：{'id': 399, '英文名': 'Love, Victor ', '中文名': '爱你，维克托 第二季', '正在播': 0}
    row_dict = dict()
    for i in range(cols):
        row_dict[table.horizontalHeaderItem(i).text()] = table.item(curr_row, i).data(0)
    # print(row_dict)
    print('in read_table_current_item ,当前选中的行:', row_dict)
    return row_dict



def readDatafromTable(table: QTableWidget, TableFields):
    ''' 将某个QTableWidget 的所有数据读入一个二维的{[]} 中'''
    cols = table.columnCount()
    rows = table.rowCount()
    data = []
    mydict = {}
    for row in range(rows):
        for col in range(cols):
            mydict[TableFields[col]] = table.item(row,col).data(0)
        data.append(mydict.copy())
    # print('整个表所有的数据：',data)
    return data

def writeTable(data, table : QTableWidget, *HiddenColumns):
    '''把 data [(),()]中的所有数据写入QTableWidget'''
    try:
        table.blockSignals(True)
        print(data)
        if (len(data) == None):  # 如果数据为空，则画一个空表
            row = 0
            col = 0
        else:
            for i in range(len(data)):  # 将相关的数据
                data[i] = list(data[i])  # 将获取的数据转为列表形式
            row = len(data)
            col = len(data[0])
        table.setRowCount(row)
        table.setColumnCount(col)
        # 写入数据
        for i in range(row):
            for j in range(col):
                # print(i,j,data[i][j])
                # self.Table_Data(table,i, j, data[i][j])
                currdata = data[i][j]
                item = QtWidgets.QTableWidgetItem()
                item.setData(0, currdata)
                table.setItem(i, j, item)
        # 处理隐藏列宽
        for hid_col in HiddenColumns:
            table.setColumnHidden(hid_col, True)
        # 自动扩展列宽，适应内容
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.show()
    finally:
        table.blockSignals(False)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSearchDownloadURL.clicked.connect(self.searchSeason)
        self.ui.tableSearchURL.cellClicked.connect(self.tableSearchURLClicked)
        self.ui.tableDownload.cellClicked.connect(self.tableDownloadClicked)
        self.ui.tableFavorite.cellClicked.connect(self.tableFavoriteCellClicked)
        self.ui.btnInsertDowloadURL.clicked.connect(self.btnInertDowloadURLClicked)
        self.ui.btnDeleteDownloadURL.clicked.connect(self.btnDeleteDownloadURLclicked)
        self.ui.btnSaveDownloadURL.clicked.connect(self.btnSaveDownloadURLclicked)
        self.ui.tableDownload.cellChanged.connect(self.tableDownloadCellChanged)
        self.ui.tableSearchURL.cellChanged.connect(self.tableSearchURLCellChanged)
        self.ui.pushButtonAddToFavorite.clicked.connect(self.addtoFavorite)
        self.ui.pushButtonUpdateCalendar.clicked.connect(self.pubshButtonUpdateCalendarClicked)
        self.ui.pushButtonViewCalendar.clicked.connect(self.viewCalendar)
        self.ui.pushButtonSearchCalendar.clicked.connect(self.searchCalendar)
        # 新建窗口完毕
        self.showFavorite()


    # 具体的控件点击
    def searchCalendar(self):
        print('正在搜索',self.ui.edtSearchCalendar.text())
        self.highlightWord(self.ui.edtSearchCalendar.text(),self.ui.textBrowserUpdateCalendar)
    def highlightWord(self,myword:str,textbrowser:QTextBrowser):
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 25))
        brush.setColor(Qt.yellow)
        color_format = QTextCharFormat()
        color_format.setBackground(brush)

        # highlight_cursor = textbrowser.document().find(myword, QTextDocument.FindWholeWords)
        highlight_cursor = QTextCursor()
        while (highlight_cursor != None) and ( not highlight_cursor.atEnd()):
            print('atend:',highlight_cursor.atEnd(),'cursor:',highlight_cursor)
            highlight_cursor = textbrowser.document().find(myword, highlight_cursor, QTextDocument.FindWholeWords)
            highlight_cursor.mergeCharFormat(color_format)



    def viewCalendar(self):
        valueofdateEdit = self.ui.dateEditYearMonth.date()
        # print(valueofdateEdit.year(),valueofdateEdit.month())
        displayWidget = self.ui.textBrowserUpdateCalendar
        BroadcastingCalendar.viewCalendar(valueofdateEdit.year(),valueofdateEdit.month(),displayWidget)
        # self.highlightWord('Big',displayWidget)



    def pubshButtonUpdateCalendarClicked(self):
        valueofdateEdit = self.ui.dateEditYearMonth.date()
        # print(valueofdateEdit.year(),valueofdateEdit.month())
        displayWidget = self.ui.textBrowserUpdateCalendar
        BroadcastingCalendar.refreshCalendar(valueofdateEdit.year(),valueofdateEdit.month(),displayWidget)


    def addtoFavorite(self):
        rst = read_table_current_line(self.ui.tableSearchURL)
        processDB.addPlay(rst['ID'],rst['英文名'],rst['中文名'])


    def tableSearchURLCellChanged(self):
        table = self.ui.tableSearchURL
        try:
            table.blockSignals(True)  # 避免自我触发
            rst = read_table_current_line(table)  # 假如鼠标被移到其他行了，这里读到也是刚刚被更改的行，而不是当前行
            print('准备update URL Xpath:', rst)
            processDB.updateSeason(rst['ID'], rst['英文名'], rst['中文名'], rst['正在播'])
        finally:
            table.blockSignals(False)

    def btnSaveDownloadURLclicked(self):
        ''' 事实上这个功能是不需要的，每次cellchange后都存盘了 '''
        TableFields = ['ID','seasonID','URL','Xpath_title','Xpath_link']
        data = readDatafromTable(self.ui.tableDownload,TableFields)
        # print(data)
        for curr_row in data:
            processDB.modifyDownloadURL(curr_row['ID'],curr_row['URL'],curr_row['Xpath_title'],curr_row['Xpath_link'])

    def btnDeleteDownloadURLclicked(self):
        table = self.ui.tableDownload
        self.blockSignals(True)
        try:
            rst = read_table_current_line(table)
            print('准备delete:', rst)
            if rst is None:
                return None
            self.ui.tableDownload.removeRow(table.currentItem().row())
            processDB.deleteDownloadbyID(rst['ID'])
        finally:
            self.blockSignals(False)


    def tableDownloadCellChanged(self):
        table = self.ui.tableDownload
        try:
            table.blockSignals(True) #避免自我触发
            rst = read_table_current_line(table) # 假如鼠标被移到其他行了，这里读到也是刚刚被更改的行，而不是当前行
            print('准备update URL Xpath:', rst)
            if rst is None: # 这一行其实永远不会None
                return None
            processDB.modifyDownloadURL(rst['ID'], rst['URL'], rst['Xpath_title'],rst['Xpath_link'])
        finally:
            table.blockSignals(False)

    def btnInertDowloadURLClicked(self):
        table = self.ui.tableDownload
        table.blockSignals(True)
        try:
            # 先获取当前的seasonID
            curr_row = self.ui.tableSearchURL.currentItem().row()
            seasonID = self.ui.tableSearchURL.item(curr_row, 0).data(0)
            print(seasonID)
            ID = processDB.addDownloadURL(seasonID,'','')
            # 写一个空行  [1, 274, 'https://www.jsr9.com/subject/29500.html', ' /html/body/div[2]/div[1]/div[2]/div[3]','/html/body/div[5]/a[@href]']
            EmptyLine = [ID, seasonID, '', '','']
            appendRow(table,EmptyLine)

        finally:
            table.blockSignals(False)


    def tableFavoriteCellClicked(self):
        # self.tableCellOnClick(self.ui.tableFavorite)
        read_table_current_line(self.ui.tableFavorite)

    def tableDownloadClicked(self):
        # 如果点击在URL上，则显示所有两个Xpath zip后的结果，如果点击在单个Xpath上，则显示它自身的结果
        self.setCursor(Qt.BusyCursor)
        self.ui.tableDownload.edit = True
        rst = read_table_current_line(self.ui.tableDownload)
        print('tableDownloadClicked: 当前行：',rst['URL'],rst['Xpath_title'],rst['Xpath_link'])
        current_col = getCurrColumnName(self.ui.tableDownload)
        # current_col = self.ui.tableDownload.horizontalHeaderItem(self.ui.tableDownload.currentColumn()).text()
        # print(current_col)
        try:
            if current_col == 'URL':
                titles_links = showHTMLsnippet.outputXpath(rst['URL'],rst['Xpath_title'],rst['Xpath_link'])
            else: # 当前点击的列是 Xpath_title 或者 Xpath_link
                titles_links = showHTMLsnippet.outputXpath(rst['URL'], rst[current_col])
        except Exception as e:
            self.ui.textBrowserDownload.setText('Xpath有错误，无法解析 \n\r'+repr(e))
            return
        finally:
            self.unsetCursor()
        txt = ''
        for title_link in titles_links:
            txt = txt + title_link['title']+ '\n\r' + title_link['link'] + '\n\r' +'------------------------------------\n\r'
        self.ui.textBrowserDownload.setText(txt)





    def tableSearchURLClicked(self):
        result = read_table_current_line(self.ui.tableSearchURL)
        seasonID = result['ID']
        print(seasonID)
        # show tableDownload
        rstdata = processDB.selectDowloadURLbySeasonID(seasonID)
        print('selectDowloadURLbySeasonID:', rstdata)
        if (len(rstdata) != 0):
            writeTable(rstdata, self.ui.tableDownload, 0, 1)

    def showFavorite(self):
        rstdata = processDB.showFavoritesWithChaseDate()
        print(rstdata)
        writeTable(rstdata, self.ui.tableFavorite, 0)
        #设置节目播出表时间选择框的默认日期
        today = datetime.date.today()
        self.ui.dateEditYearMonth.setDate(today)

    def searchSeason(self):
        rstdata = processDB.selectSeasonByName(self.ui.edtName.text())
        print('testtttt',rstdata)
        writeTable(rstdata, self.ui.tableSearchURL, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
