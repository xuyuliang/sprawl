from PySide6 import QtWidgets, QtCore

import processDB
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_sprawl import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton2_clicked)
        self.ui.tableWidget.cellClicked.connect(self.tableWidgetCellClicked)
        # 新建窗口完毕
        self.showFavorite()

    def writeTable(self, data, table):
        print(data)
        for i in range(len(data)):  # 将相关的数据
            data[i] = list(data[i])  # 将获取的数据转为列表形式
        row = len(data)
        col = len(data[0])
        # table.setHorizontalHeaderLabels(["enName","chName","date","episode"])
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

    def tableCellOnClick(self, table):
        row = table.currentItem().row()
        print("row=", row)
        col = table.currentItem().column()
        print("col=", col)
        title = table.horizontalHeaderItem(col).text()
        print("title=", title)
        item = table.currentItem().data(0)
        print("item=", item)


    @QtCore.Slot()  # 防止点两次
    def tableWidgetCellClicked(self):
        self.tableCellOnClick(self.ui.tableWidget)

    def showFavorite(self):
        rstdata = processDB.showFavoriteSeasons()
        self.writeTable(rstdata, self.ui.tableWidget)

    def on_pushButton2_clicked(self, value):
        print("hello 你好")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
