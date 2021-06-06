import processDB
import sys

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtSql import QSqlQueryModel
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_sprawl import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.test)
        self.ui.pushButton_2.clicked.connect(self.on_pushButton2_clicked)
        self.ui.tableView.setModel()

    def test(self):
        self.ui.lineEdit.setText('你好，新的')


    @pyqtSlot(bool)
    def on_pushButton2_clicked(self, value):
        print("hello 你好")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec())