from PySide6 import QtWidgets, QtCore

import processDB
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from ui_sprawl import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSearchDownloadURL.clicked.connect(self.searchSeason)
        self.ui.tableSearchURL.cellClicked.connect(self.tableSearchURLClicked)
        self.ui.tableWidget.cellClicked.connect(self.tableWidgetCellClicked)
        # 新建窗口完毕
        self.showFavorite()

    def writeTable(self, data, table):
        print(data)
        for i in range(len(data)):  # 将相关的数据
            data[i] = list(data[i])  # 将获取的数据转为列表形式
        row = len(data)
        col = len(data[0])
        table.setRowCount(row)
        table.setColumnCount(col)

        for i in range(row):
            for j in range(col):
                # print(i,j,data[i][j])
                # self.Table_Data(table,i, j, data[i][j])
                currdata = data[i][j]
                item = QtWidgets.QTableWidgetItem()
                item.setData(0,currdata)
                table.setItem(i, j, item)
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
        print(result)
        return result

    @QtCore.Slot()  # 防止点两次
    def tableWidgetCellClicked(self):
        self.tableCellOnClick(self.ui.tableWidget)

    def tableSearchURLClicked(self):
        result = self.tableCellOnClick(self.ui.tableSearchURL)
        seasonID = result['rowdict']['ID']
        print(seasonID)
        rstdata = processDB.selectDowloadURLbySeasonID(seasonID)
        print(rstdata)
        self.writeTable(rstdata,self.ui.tableDownload)

    def showFavorite(self):
        rstdata = processDB.showFavoriteSeasons()
        self.writeTable(rstdata, self.ui.tableWidget)

    def searchSeason(self):
        rstdata = processDB.selectSeasonByName(self.ui.edtName.text())
        self.writeTable(rstdata,self.ui.tableSearchURL)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
