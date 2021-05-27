import sys
from PySide2 import QtWidgets,QtGui,QtCore
import ui_sprawl

class SprawlWindow(ui_sprawl.Ui_Form,QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(SprawlWindow,self).__init__(parent)

def main():
    app = QtWidgets.QApplication(sys.argv)
    wnd = SprawlWindow()
    wnd.show()
    app.exec_()

if __name__ == '__main__':
    main()