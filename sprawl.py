from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QEvent

import processDB
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView
from ui_sprawl import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSearchDownloadURL.clicked.connect(self.searchSeason)
        self.ui.tableSearchURL.cellClicked.connect(self.tableSearchURLClicked)
        self.ui.tableDownload.cellClicked.connect(self.tableDownloadClicked)
        self.ui.tableFavorite.cellClicked.connect(self.tableWidgetCellClicked)
        self.ui.btnInsertDowloadURL.clicked.connect(self.btnInertDowloadURLClicked)
        self.ui.tableSearchURL.cellChanged.connect(self.tableSearchURLitemChanged)

        # 新建窗口完毕
        self.showFavorite()
    # 公用的函数们
    def tableItemChanged(self,table):
        # 如果当前不在双击编辑状态，currentItem就是None，说明这个change不是由用户主动造成的
        if(table.currentItem() == None):
            return None
        rows = table.columnCount()
        row = table.currentItem().row()
        # 得出当前行的dict   如：{'id': 399, '英文名': 'Love, Victor ', '中文名': '爱你，维克托 第二季', '正在追': 0}
        rowdict = dict()
        for i in range(rows):
            rowdict[table.horizontalHeaderItem(i).text()]=table.item(row,i).data(0)
        # print(rowdict)
        print('in tableItemChanged:',rowdict)
        return rowdict


    def writeTable(self, data, table, *HiddenColumns):
        # print(data)
        if(len(data) == None):   # 如果数据为空，则画一个空表
            row = 0
            col = 0
        else:
            for i in range(len(data)):  # 将相关的数据
                data[i] = list(data[i])  # 将获取的数据转为列表形式
            row = len(data)
            col = len(data[0])
        table.setRowCount(row)
        table.setColumnCount(col)
        #写入数据
        for i in range(row):
            for j in range(col):
                # print(i,j,data[i][j])
                # self.Table_Data(table,i, j, data[i][j])
                currdata = data[i][j]
                item = QtWidgets.QTableWidgetItem()
                item.setData(0,currdata)
                table.setItem(i, j, item)
        #处理隐藏列宽
        for hid_col in HiddenColumns:
            table.setColumnHidden(hid_col,True)
        #自动扩展列宽，适应内容
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.show()

    def tableCellOnClick(self, table:QTableWidget):
        # 得出当前item的dict  如： {'row': 2, 'col': 1, 'title': '英文名', 'item': 'Black Love '}
        row = table.currentItem().row()
        col = table.currentItem().column()
        title = table.horizontalHeaderItem(col).text()
        item = table.currentItem().data(0)
        itemdict = {'row':row,'col':col,'title':title,'item':item}
        # print(itemdict)
        # 得出当前行的dict   如：{'id': 399, '英文名': 'Love, Victor ', '中文名': '爱你，维克托 第二季', '正在追': 0}
        rows = table.columnCount()
        rowdict = dict()
        for i in range(rows):
            rowdict[table.horizontalHeaderItem(i).text()]=table.item(row,i).data(0)
        # print(rowdict)
        result = {'itemdict':itemdict,'rowdict':rowdict}
        print('tableCellOnClick:',result)
        return result

    # 具体的控件点击
    def tableSearchURLitemChanged(self):
        rst = self.tableItemChanged(self.ui.tableSearchURL)
        print('准备update或insert URL Xpath:',rst)
        if(rst == None):
            return None
        if(rst['ID'] == -1):  # 新增的空行，默认是-1
            processDB.addDownloadURL(rst['SeasonID'],rst['URL'],rst['Xpath'])
        else:
            processDB.modifyDownloadURL(rst['ID',rst['URL'],rst['Xpath']])



    def btnInertDowloadURLClicked(self):
        #写一个空行  [(1, 274, 'https://www.jsr9.com/subject/29500.html', ' /html/body/div[2]/div[1]/div[2]/div[3]')]
        curr_row = self.ui.tableSearchURL.currentItem().row()
        seasonID = self.ui.tableSearchURL.item(curr_row,0).data(0)
        print(seasonID)
        EmptyLine = [(-1, seasonID, '', '')]
        #读原有的数据
        data = processDB.selectDowloadURLbySeasonID(seasonID)
        print('data:',data)
        # 将空行加到最后一行
        data.extend(EmptyLine)
        print('data',data)
        self.writeTable(data,self.ui.tableDownload,0,1)
    def tableWidgetCellClicked(self):
        self.tableCellOnClick(self.ui.tableFavorite)
    def tableDownloadClicked(self):
        rst = self.tableCellOnClick(self.ui.tableDownload)
        ID = rst['rowdict']['ID']
        SeasonID = rst['rowdict']['SeasonID']
        URL = rst['rowdict']['URL']
        Xpath = rst['rowdict']['Xpath']

    def tableSearchURLClicked(self):
        result = self.tableCellOnClick(self.ui.tableSearchURL)
        seasonID = result['rowdict']['ID']
        print(seasonID)
        rstdata = processDB.selectDowloadURLbySeasonID(seasonID)
        print('selectDowloadURLbySeasonID:',rstdata)
        if(len(rstdata) != 0 ):
            self.writeTable(rstdata,self.ui.tableDownload,0,1)

    def showFavorite(self):
        rstdata = processDB.showFavoriteSeasons()
        self.writeTable(rstdata, self.ui.tableFavorite,0)

    def searchSeason(self):
        rstdata = processDB.selectSeasonByName(self.ui.edtName.text())
        self.writeTable(rstdata,self.ui.tableSearchURL,0)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
