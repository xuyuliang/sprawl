from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import processDB


class SprawlWindow:
    def __init__(self):
        self.ui = QUiLoader().load('ui_sprawl.ui')
        super(SprawlWindow, self).__init__()


def main():
    app = QApplication([])
    wnd = SprawlWindow()
    wnd.ui.show()
    app.exec_()


if __name__ == '__main__':
    main()

    tt = processDB.findBroadcastingSchedule(109)
    for t in tt:
        enName,chName,dueDate,SnEm = t

