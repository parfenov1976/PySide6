# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainwindow.ui'
#
# Created by: Qt User Interface Compiler version 6.4.0
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QLineEdit, QListView, QPushButton, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(428, 435)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.todo_view = QListView(self.centralwidget)
        self.todo_view.setObjectName(u"todo_view")
        self.todo_view.setGeometry(QRect(10, 20, 400, 251))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 280, 411, 51))
        self.del_button = QPushButton(self.widget)
        self.del_button.setObjectName(u"del_button")
        self.del_button.setGeometry(QRect(20, 10, 171, 24))
        self.comp_button = QPushButton(self.widget)
        self.comp_button.setObjectName(u"comp_button")
        self.comp_button.setGeometry(QRect(210, 10, 180, 24))
        self.todo_edit = QLineEdit(self.centralwidget)
        self.todo_edit.setObjectName(u"todo_edit")
        self.todo_edit.setGeometry(QRect(30, 340, 371, 21))
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(30, 380, 371, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Todo List", None))
        self.del_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.comp_button.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add Todo", None))
    # retranslateUi

