# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(279, 432)
        font = QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.info = QAction(MainWindow)
        self.info.setObjectName(u"info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.toolButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lockhand = QCheckBox(self.groupBox)
        self.lockhand.setObjectName(u"lockhand")

        self.gridLayout.addWidget(self.lockhand, 0, 0, 1, 1)

        self._2_3 = QRadioButton(self.groupBox)
        self._2_3.setObjectName(u"_2_3")

        self.gridLayout.addWidget(self._2_3, 0, 1, 1, 1)

        self._1_2 = QRadioButton(self.groupBox)
        self._1_2.setObjectName(u"_1_2")

        self.gridLayout.addWidget(self._1_2, 2, 0, 1, 1)

        self._1_3 = QRadioButton(self.groupBox)
        self._1_3.setObjectName(u"_1_3")

        self.gridLayout.addWidget(self._1_3, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.convert_button = QPushButton(self.centralwidget)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setMinimumSize(QSize(0, 81))

        self.verticalLayout.addWidget(self.convert_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 279, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.info)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"4kto7k", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None))
        self.label.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u952e\u578b", None))
        self.lockhand.setText(QCoreApplication.translate("MainWindow", u"\u9501\u624b", None))
        self._2_3.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6307\u65e0\u540d\u6307", None))
        self._1_2.setText(QCoreApplication.translate("MainWindow", u"\u98df\u6307\u4e2d\u6307", None))
        self._1_3.setText(QCoreApplication.translate("MainWindow", u"\u98df\u6307\u65e0\u540d\u6307", None))
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"\u5236\u4f5c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u672c", None))
    # retranslateUi

