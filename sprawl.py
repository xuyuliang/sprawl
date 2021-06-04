#import processDB
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_sprawl import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.test)
    def test(self):
        self.ui.lineEdit_2.setText('你好，新的')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec())