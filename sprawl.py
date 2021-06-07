from PySide6 import QtWidgets

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
        self.ui.pushButton_2.clicked.connect(self.test)

    def Table_Data(self,table, i, j, data_ij):
        item = QtWidgets.QTableWidgetItem(data_ij)
        table.setItem(i, j, item)
        # item = table.item(i, j)
        # item.setText(self._translate("Form", str(data)))

    def writeTable(self,data,table):
        for i in range(len(data)):  # 将相关的数据
            data[i] = list(data[i])  # 将获取的数据转为列表形式
        row = len(data)
        col = len(data[0])
        table.setHorizontalHeaderLabels(["enName","chName","date","episode"])
        table.setRowCount(row)
        table.setColumnCount(col)

        for i in range(row):
            for j in range(col):
                print(i,j,data[i][j])
                self.Table_Data(table,i, j, data[i][j])
        table.show()


    def test(self):
        # 遍历二维元组, 将 id 和 name 显示到界面表格上
        rstdata = processDB.findBroadcastingSchedule(109)
        self.writeTable(rstdata,self.ui.tableWidget)
        x = 0
        for i in rstdata:
            y = 0
            for j in i:
                print(str(rstdata[x][y]))
                y = y + 1
            x = x + 1



    def on_pushButton2_clicked(self, value):
        print("hello 你好")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())