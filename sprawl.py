import sys
from PySide2.QtWidgets import QMainWindow,QApplication
from ui_sprawl import Ui_Form

class SprawlWindow(QMainWindow):
    def __init__(self):
        super(SprawlWindow,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    wnd = SprawlWindow()
    wnd.show()
    app.exec_()

if __name__ == '__main__':
    main()