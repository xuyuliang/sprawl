from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QEvent, QObject

import processDB
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView
from ui_sprawl import Ui_MainWindow


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

def read_table_current_item(table: QTableWidget):
    ''' 读取当前QTableWidget选中的行，若没选中，返回空dict{} '''
    if table.currentItem() is None:
        return None
    cols = table.columnCount()
    curr_row = table.currentItem().row()
    # 得出当前行的dict   如：{'id': 399, '英文名': 'Love, Victor ', '中文名': '爱你，维克托 第二季', '正在追': 0}
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
        # print(data)
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

        # 新建窗口完毕
        self.showFavorite()

    # 公用的函数们





    # 具体的控件点击

    def btnSaveDownloadURLclicked(self):
        TableFields = ['ID','seasonID','URL','Xpath']
        data = readDatafromTable(self.ui.tableDownload,TableFields)
        # print(data)
        for item in data:
            processDB.insert_modifyDownloadURL(item['ID'],item['seasonID'],item['URL'],item['Xpath'])

    def btnDeleteDownloadURLclicked(self):
        table = self.ui.tableDownload
        self.blockSignals(True)
        try:
            rst = read_table_current_item(table)
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
            rst = read_table_current_item(table) # 假如鼠标被移到其他行了，这里读到也是刚刚被更改的行，而不是当前行
            print('准备update或insert URL Xpath:', rst)
            if rst is None: # 这一行其实永远不会None
                return None
            data = processDB.insert_modifyDownloadURL(rst['ID'], rst['SeasonID'], rst['URL'], rst['Xpath'])
            if data is None:  #说明是modify
                data=[(rst['ID'], rst['SeasonID'], rst['URL'], rst['Xpath'])]
            print('insert的结果', data[0])
            write_table_current_line(table,list(data[0]))
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
            # 写一个空行  [1, 274, 'https://www.jsr9.com/subject/29500.html', ' /html/body/div[2]/div[1]/div[2]/div[3]']
            EmptyLine = [-1, seasonID, '', '']
            appendRow(table,EmptyLine)
        finally:
            table.blockSignals(False)


    def tableFavoriteCellClicked(self):
        # self.tableCellOnClick(self.ui.tableFavorite)
        read_table_current_item(self.ui.tableFavorite)

    def tableDownloadClicked(self):
        # self.ui.tableDownload.cellChanged.connect(self.tableDownloadCellChanged)
        # self.ui.tableDownload.edit = True
        rst = read_table_current_item(self.ui.tableDownload)
        print('tableDownloadClicked: 当前行：',rst)



    def tableSearchURLClicked(self):
        result = read_table_current_item(self.ui.tableSearchURL)
        seasonID = result['ID']
        print(seasonID)
        # show tableDownload
        rstdata = processDB.selectDowloadURLbySeasonID(seasonID)
        print('selectDowloadURLbySeasonID:', rstdata)
        if (len(rstdata) != 0):
            writeTable(rstdata, self.ui.tableDownload, 0, 1)

    def showFavorite(self):
        rstdata = processDB.showFavoriteSeasons()
        writeTable(rstdata, self.ui.tableFavorite, 0)

    def searchSeason(self):
        rstdata = processDB.selectSeasonByName(self.ui.edtName.text())
        writeTable(rstdata, self.ui.tableSearchURL, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
