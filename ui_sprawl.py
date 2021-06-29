# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_sprawl.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 886)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableFavorite = QTableWidget(self.tab_2)
        if (self.tableFavorite.columnCount() < 4):
            self.tableFavorite.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableFavorite.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableFavorite.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableFavorite.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableFavorite.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableFavorite.setObjectName(u"tableFavorite")

        self.verticalLayout_4.addWidget(self.tableFavorite)

        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout_4.addWidget(self.textBrowser)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 220))
        self.tableSearchURL = QTableWidget(self.groupBox_2)
        if (self.tableSearchURL.columnCount() < 4):
            self.tableSearchURL.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableSearchURL.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableSearchURL.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableSearchURL.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableSearchURL.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableSearchURL.setObjectName(u"tableSearchURL")
        self.tableSearchURL.setGeometry(QRect(10, 50, 731, 161))
        self.tableSearchURL.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableSearchURL.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btnSearchDownloadURL = QPushButton(self.groupBox_2)
        self.btnSearchDownloadURL.setObjectName(u"btnSearchDownloadURL")
        self.btnSearchDownloadURL.setGeometry(QRect(10, 25, 75, 24))
        self.btnSearchDownloadURL.setContextMenuPolicy(Qt.PreventContextMenu)
        self.edtName = QLineEdit(self.groupBox_2)
        self.edtName.setObjectName(u"edtName")
        self.edtName.setGeometry(QRect(91, 26, 133, 21))

        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.btnDeleteDownloadURL = QPushButton(self.groupBox_3)
        self.btnDeleteDownloadURL.setObjectName(u"btnDeleteDownloadURL")
        self.btnDeleteDownloadURL.setGeometry(QRect(100, 24, 75, 24))
        self.btnInsertDowloadURL = QPushButton(self.groupBox_3)
        self.btnInsertDowloadURL.setObjectName(u"btnInsertDowloadURL")
        self.btnInsertDowloadURL.setGeometry(QRect(19, 24, 75, 24))
        self.tableDownload = QTableWidget(self.groupBox_3)
        if (self.tableDownload.columnCount() < 4):
            self.tableDownload.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableDownload.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableDownload.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableDownload.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableDownload.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.tableDownload.setObjectName(u"tableDownload")
        self.tableDownload.setGeometry(QRect(20, 60, 721, 121))
        self.btnSaveDownloadURL = QPushButton(self.groupBox_3)
        self.btnSaveDownloadURL.setObjectName(u"btnSaveDownloadURL")
        self.btnSaveDownloadURL.setGeometry(QRect(181, 24, 75, 24))
        self.textBrowserDownload = QTextBrowser(self.groupBox_3)
        self.textBrowserDownload.setObjectName(u"textBrowserDownload")
        self.textBrowserDownload.setGeometry(QRect(20, 190, 721, 351))
        self.textBrowserDownload.setOpenExternalLinks(True)

        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.edtName.returnPressed.connect(self.btnSearchDownloadURL.click)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableFavorite.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableFavorite.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u82f1\u6587\u540d", None));
        ___qtablewidgetitem2 = self.tableFavorite.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\u540d", None));
        ___qtablewidgetitem3 = self.tableFavorite.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None));
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6211\u7684\u6536\u85cf", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        ___qtablewidgetitem4 = self.tableSearchURL.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.tableSearchURL.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u82f1\u6587\u540d", None));
        ___qtablewidgetitem6 = self.tableSearchURL.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\u540d", None));
        ___qtablewidgetitem7 = self.tableSearchURL.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5728\u8ffd", None));
        self.btnSearchDownloadURL.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.btnDeleteDownloadURL.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.btnInsertDowloadURL.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
        ___qtablewidgetitem8 = self.tableDownload.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.tableDownload.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"SeasonID", None));
        ___qtablewidgetitem10 = self.tableDownload.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtablewidgetitem11 = self.tableDownload.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Xpath", None));
        self.btnSaveDownloadURL.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
    # retranslateUi

