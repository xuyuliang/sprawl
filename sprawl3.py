import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_sprawl import Ui_MainWindow

app = QApplication(sys.argv)

window = QMainWindow()
Ui_MainWindow().setupUi(window)

window.show()
app.exec_()