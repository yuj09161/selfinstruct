# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'write.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glCentral = QGridLayout(self.centralwidget)
        self.glCentral.setObjectName(u"glCentral")
        self.scMain = QScrollArea(self.centralwidget)
        self.scMain.setObjectName(u"scMain")
        self.scMain.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scMain.setWidgetResizable(True)
        self.scwMain = QWidget()
        self.scwMain.setObjectName(u"scwMain")
        self.scwMain.setGeometry(QRect(0, 0, 755, 493))
        self.glMain = QGridLayout(self.scwMain)
        self.glMain.setObjectName(u"glMain")
        self.lbNo3 = QLabel(self.scwMain)
        self.lbNo3.setObjectName(u"lbNo3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbNo3.sizePolicy().hasHeightForWidth())
        self.lbNo3.setSizePolicy(sizePolicy)
        self.lbNo3.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbNo3, 6, 0, 1, 1)

        self.lbCount1 = QLabel(self.scwMain)
        self.lbCount1.setObjectName(u"lbCount1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbCount1.sizePolicy().hasHeightForWidth())
        self.lbCount1.setSizePolicy(sizePolicy1)
        self.lbCount1.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCount1, 2, 1, 1, 1)

        self.lbTitleNum = QLabel(self.scwMain)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleNum, 0, 0, 1, 1)

        self.lbTitleCount = QLabel(self.scwMain)
        self.lbTitleCount.setObjectName(u"lbTitleCount")
        sizePolicy.setHeightForWidth(self.lbTitleCount.sizePolicy().hasHeightForWidth())
        self.lbTitleCount.setSizePolicy(sizePolicy)
        self.lbTitleCount.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleCount, 0, 1, 1, 1)

        self.lbNo2 = QLabel(self.scwMain)
        self.lbNo2.setObjectName(u"lbNo2")
        sizePolicy.setHeightForWidth(self.lbNo2.sizePolicy().hasHeightForWidth())
        self.lbNo2.setSizePolicy(sizePolicy)
        self.lbNo2.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbNo2, 4, 0, 1, 1)

        self.lbNo1 = QLabel(self.scwMain)
        self.lbNo1.setObjectName(u"lbNo1")
        sizePolicy.setHeightForWidth(self.lbNo1.sizePolicy().hasHeightForWidth())
        self.lbNo1.setSizePolicy(sizePolicy)
        self.lbNo1.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbNo1, 2, 0, 1, 1)

        self.lbCount2 = QLabel(self.scwMain)
        self.lbCount2.setObjectName(u"lbCount2")
        sizePolicy1.setHeightForWidth(self.lbCount2.sizePolicy().hasHeightForWidth())
        self.lbCount2.setSizePolicy(sizePolicy1)
        self.lbCount2.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCount2, 4, 1, 1, 1)

        self.lbCount3 = QLabel(self.scwMain)
        self.lbCount3.setObjectName(u"lbCount3")
        sizePolicy1.setHeightForWidth(self.lbCount3.sizePolicy().hasHeightForWidth())
        self.lbCount3.setSizePolicy(sizePolicy1)
        self.lbCount3.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCount3, 6, 1, 1, 1)

        self.pteNo2 = QPlainTextEdit(self.scwMain)
        self.pteNo2.setObjectName(u"pteNo2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pteNo2.sizePolicy().hasHeightForWidth())
        self.pteNo2.setSizePolicy(sizePolicy2)

        self.glMain.addWidget(self.pteNo2, 5, 0, 1, 2)

        self.pteNo1 = QPlainTextEdit(self.scwMain)
        self.pteNo1.setObjectName(u"pteNo1")
        sizePolicy2.setHeightForWidth(self.pteNo1.sizePolicy().hasHeightForWidth())
        self.pteNo1.setSizePolicy(sizePolicy2)

        self.glMain.addWidget(self.pteNo1, 3, 0, 1, 2)

        self.pteNo3 = QPlainTextEdit(self.scwMain)
        self.pteNo3.setObjectName(u"pteNo3")
        sizePolicy2.setHeightForWidth(self.pteNo3.sizePolicy().hasHeightForWidth())
        self.pteNo3.setSizePolicy(sizePolicy2)

        self.glMain.addWidget(self.pteNo3, 7, 0, 1, 2)

        self.lbTitleContent = QLabel(self.scwMain)
        self.lbTitleContent.setObjectName(u"lbTitleContent")
        sizePolicy.setHeightForWidth(self.lbTitleContent.sizePolicy().hasHeightForWidth())
        self.lbTitleContent.setSizePolicy(sizePolicy)
        self.lbTitleContent.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleContent, 1, 0, 1, 2)

        self.scMain.setWidget(self.scwMain)

        self.glCentral.addWidget(self.scMain, 0, 0, 1, 1)

        self.widMenu = QWidget(self.centralwidget)
        self.widMenu.setObjectName(u"widMenu")
        self.glMenu = QGridLayout(self.widMenu)
        self.glMenu.setObjectName(u"glMenu")
        self.btnSaveAs = QPushButton(self.widMenu)
        self.btnSaveAs.setObjectName(u"btnSaveAs")
        sizePolicy1.setHeightForWidth(self.btnSaveAs.sizePolicy().hasHeightForWidth())
        self.btnSaveAs.setSizePolicy(sizePolicy1)

        self.glMenu.addWidget(self.btnSaveAs, 0, 3, 1, 1)

        self.btnSave = QPushButton(self.widMenu)
        self.btnSave.setObjectName(u"btnSave")
        sizePolicy1.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy1)

        self.glMenu.addWidget(self.btnSave, 0, 2, 1, 1)

        self.spTime = QSpinBox(self.widMenu)
        self.spTime.setObjectName(u"spTime")
        sizePolicy1.setHeightForWidth(self.spTime.sizePolicy().hasHeightForWidth())
        self.spTime.setSizePolicy(sizePolicy1)
        self.spTime.setMinimum(1)
        self.spTime.setMaximum(60)

        self.glMenu.addWidget(self.spTime, 0, 6, 1, 1)

        self.btnExit = QPushButton(self.widMenu)
        self.btnExit.setObjectName(u"btnExit")
        sizePolicy1.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy1)

        self.glMenu.addWidget(self.btnExit, 0, 7, 1, 1)

        self.btnLoad = QPushButton(self.widMenu)
        self.btnLoad.setObjectName(u"btnLoad")
        sizePolicy1.setHeightForWidth(self.btnLoad.sizePolicy().hasHeightForWidth())
        self.btnLoad.setSizePolicy(sizePolicy1)

        self.glMenu.addWidget(self.btnLoad, 0, 1, 1, 1)

        self.btnExport = QPushButton(self.widMenu)
        self.btnExport.setObjectName(u"btnExport")
        sizePolicy1.setHeightForWidth(self.btnExport.sizePolicy().hasHeightForWidth())
        self.btnExport.setSizePolicy(sizePolicy1)

        self.glMenu.addWidget(self.btnExport, 0, 0, 1, 1)

        self.chkAutoSave = QCheckBox(self.widMenu)
        self.chkAutoSave.setObjectName(u"chkAutoSave")
        sizePolicy1.setHeightForWidth(self.chkAutoSave.sizePolicy().hasHeightForWidth())
        self.chkAutoSave.setSizePolicy(sizePolicy1)

        self.glMenu.addWidget(self.chkAutoSave, 0, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glMenu.addItem(self.horizontalSpacer, 0, 4, 1, 1)


        self.glCentral.addWidget(self.widMenu, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbNo3.setText(QCoreApplication.translate("MainWindow", u"3\ubc88: \ud559\uad50 \uc0dd\ud65c \uc911 \ubc30\ub824, \ub098\ub214, \ud611\ub825, \uac08\ub4f1 \uad00\ub9ac \ub4f1\uc744\n"
"	\uc2e4\ucc9c\ud55c \uc0ac\ub840\ub97c \ub4e4\uace0, \uadf8 \uacfc\uc815\uc744 \ud1b5\ud574 \ubc30\uc6b0\uace0 \ub290\ub080\uc810", None))
        self.lbCount1.setText("")
        self.lbTitleNum.setText(QCoreApplication.translate("MainWindow", u"\ubc88\ud638", None))
        self.lbTitleCount.setText(QCoreApplication.translate("MainWindow", u"\uae00\uc790\uc218", None))
        self.lbNo2.setText(QCoreApplication.translate("MainWindow", u"2\ubc88: \uace0\ub4f1\ud559\uad50 \uc7ac\ud559\uae30\uac04 \uc911 \ubcf8\uc778\uc774 \uc758\ubbf8\ub97c \ub450\uace0 \ub178\ub825\ud588\ub358\n"
"	\uad50\ub0b4 \ud65c\ub3d9(3\uac1c \uc774\ub0b4)\uc744 \ud1b5\ud574 \ubc30\uc6b0\uace0 \ub290\ub080\uc810", None))
        self.lbNo1.setText(QCoreApplication.translate("MainWindow", u"1\ubc88: \uace0\ub4f1\ud559\uad50 \uc7ac\ud559\uae30\uac04 \uc911 \ud559\uc5c5\uc5d0 \uae30\uc6b8\uc778\n"
"	\ub178\ub825\uacfc \ud559\uc2b5 \uacbd\ud5d8\uc744 \ud1b5\ud574, \ubc30\uc6b0\uace0 \ub290\ub080\uc810", None))
        self.lbCount2.setText("")
        self.lbCount3.setText("")
        self.lbTitleContent.setText(QCoreApplication.translate("MainWindow", u"\ub0b4\uc6a9", None))
        self.btnSaveAs.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc800\uc7a5", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.spTime.setSuffix(QCoreApplication.translate("MainWindow", u"\ubd84", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.btnExport.setText(QCoreApplication.translate("MainWindow", u"\ub0b4\ubcf4\ub0b4\uae30", None))
        self.chkAutoSave.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub3d9 \uc800\uc7a5", None))
    # retranslateUi

