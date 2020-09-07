# -*- coding: utf-8 -*-
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, Signal)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

FONT_MIN_SIZE = 7
FONT_MAX_SIZE = 13

class CustomScrollArea(QScrollArea):
    resized=Signal(QSize)
    def resizeEvent(self,event):
        super().resizeEvent(event)
        self.resized.emit(event.size())

class Ui_write(object):
    def setupUi(self, write, font_default_size):
        write.resize(1000, 750)
        
        #action group
        acGroupFont=QActionGroup(write)
        acGroupFont.setExclusive(True)
        
        #action for menu
        self.acLoad = QAction(write)
        self.acLoad.setObjectName(u"acLoad")
        self.acSave = QAction(write)
        self.acSave.setObjectName(u"acSave")
        self.acSaveAs = QAction(write)
        self.acSaveAs.setObjectName(u"acSaveAs")
        self.acSaveCopy = QAction(write)
        self.acSaveCopy.setObjectName(u"acSaveCopy")
        self.acExport_Ent = QAction(write)
        self.acExport_Ent.setObjectName(u"acExport_Ent")
        self.acExport_NoEnt = QAction(write)
        self.acExport_NoEnt.setObjectName(u"acExport_NoEnt")
        self.acExit = QAction(write)
        self.acExit.setObjectName(u"acExit")
        
        self.acDoubleSpace = QAction(write)
        self.acDoubleSpace.setObjectName(u"acDoubleSpace")
        self.acConfig = QAction(write)
        self.acConfig.setObjectName(u"acConfig")
        
        self.acNotice = QAction(write)
        self.acNotice.setObjectName(u"acNotice")
        self.acInfo = QAction(write)
        self.acInfo.setObjectName(u"acInfo")
        
        #set action enable
        self.acConfig.setEnabled(False)
        
        self.centralwidget = QWidget(write)
        self.glCentral = QGridLayout(self.centralwidget)
        
        self.sizePolicy_PF = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.sizePolicy_PF.setHorizontalStretch(0)
        self.sizePolicy_PF.setVerticalStretch(0)
        
        self.sizePolicy_FF = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy_FF.setHorizontalStretch(0)
        self.sizePolicy_FF.setVerticalStretch(0)
        
        self.sizePolicy_EP = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.sizePolicy_EP.setHorizontalStretch(0)
        self.sizePolicy_EP.setVerticalStretch(0)
        
        #Main Scoll Area
        self.scMain = CustomScrollArea(self.centralwidget)
        self.scMain.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        self.scwMain = QWidget(self.scMain)
        self.glMain = QGridLayout(self.scwMain)

        self.lbTitleNum = QLabel(self.scwMain)
        self.sizePolicy_PF.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(self.sizePolicy_PF)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleNum, 0, 0, 1, 1)

        self.lbTitleCount = QLabel(self.scwMain)
        self.sizePolicy_PF.setHeightForWidth(self.lbTitleCount.sizePolicy().hasHeightForWidth())
        self.lbTitleCount.setSizePolicy(self.sizePolicy_PF)
        self.lbTitleCount.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleCount, 0, 1, 1, 1)

        self.lbTitleContent = QLabel(self.scwMain)
        self.sizePolicy_PF.setHeightForWidth(self.lbTitleContent.sizePolicy().hasHeightForWidth())
        self.lbTitleContent.setSizePolicy(self.sizePolicy_PF)
        self.lbTitleContent.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleContent, 1, 0, 1, 2)
        
        self.scMain.setWidget(self.scwMain)
        self.glCentral.addWidget(self.scMain, 0, 0, 1, 1)
    
        #Menu Widget
        self.widMenu = QWidget(self.centralwidget)
        self.glMenu = QGridLayout(self.widMenu)
        
        self.btnSave = QPushButton(self.widMenu)
        self.sizePolicy_FF.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(self.sizePolicy_FF)
        self.glMenu.addWidget(self.btnSave, 0, 0, 1, 1)
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.glMenu.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.chkAutoSave = QCheckBox(self.widMenu)
        self.sizePolicy_FF.setHeightForWidth(self.chkAutoSave.sizePolicy().hasHeightForWidth())
        self.chkAutoSave.setSizePolicy(self.sizePolicy_FF)
        self.glMenu.addWidget(self.chkAutoSave, 0, 5, 1, 1)

        self.spTime = QSpinBox(self.widMenu)
        self.sizePolicy_FF.setHeightForWidth(self.spTime.sizePolicy().hasHeightForWidth())
        self.spTime.setSizePolicy(self.sizePolicy_FF)
        self.spTime.setMinimum(1)
        self.spTime.setMaximum(60)
        self.glMenu.addWidget(self.spTime, 0, 6, 1, 1)

        self.btnExit = QPushButton(self.widMenu)
        self.sizePolicy_FF.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(self.sizePolicy_FF)
        self.glMenu.addWidget(self.btnExit, 0, 7, 1, 1)

        self.glCentral.addWidget(self.widMenu, 1, 0, 1, 1)

        write.setCentralWidget(self.centralwidget)
        
        #menu
        self.menubar = QMenuBar(write)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.save = QMenu(self.menubar)
        self.save.setObjectName(u"save")
        self.tools = QMenu(self.menubar)
        self.tools.setObjectName(u"tools")
        self.export = QMenu(self.menubar)
        self.export.setObjectName(u"export")
        self.fontSize = QMenu(self.menubar)
        self.fontSize.setObjectName(u"fontSize")
        self.info = QMenu(self.menubar)
        self.info.setObjectName(u"info")
        write.setMenuBar(self.menubar)
        
        self.export.addAction(self.acExport_Ent)
        self.export.addAction(self.acExport_NoEnt)
        
        self.save.addAction(self.acLoad)
        self.save.addAction(self.acSave)
        self.save.addSeparator()
        self.save.addAction(self.acSaveAs)
        self.save.addAction(self.acSaveCopy)
        self.save.addAction(self.export.menuAction())
        self.save.addSeparator()
        self.save.addAction(self.acExit)
        
        def mkaction(k):
            fontAction = QAction(write)
            fontAction.setObjectName(u"fontAction")
            self.fontSize.addAction(fontAction)
            fontAction.setActionGroup(acGroupFont)
            fontAction.setCheckable(True)
            fontAction.setText(
                QCoreApplication.translate("write",f'{k} (기본값)' if k==font_default_size else str(k),None)
            )
            fontAction.font_size_of_this=k
            self.fontAction.append(fontAction)
        
        for k in range(FONT_MIN_SIZE,FONT_MAX_SIZE+1):
            mkaction(k)
        
        self.tools.addAction(self.acDoubleSpace)
        self.tools.addAction(self.fontSize.menuAction())
        self.save.addSeparator()
        self.tools.addAction(self.acConfig)
        
        self.info.addAction(self.acNotice)
        self.info.addAction(self.acInfo)

        self.menubar.addAction(self.save.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.info.menuAction())

        self.retranslateUi(write)

        QMetaObject.connectSlotsByName(write)
    # setupUi

    def retranslateUi(self, write):
        write.setWindowTitle(QCoreApplication.translate("write", u"\uc790\uae30\uc18c\uac1c\uc11c \uc791\uc131 \ubcf4\uc870", None))
        self.lbTitleNum.setText(QCoreApplication.translate("write", u"\ubc88\ud638", None))
        self.lbTitleCount.setText(QCoreApplication.translate("write", u"\uae00\uc790\uc218", None))
        self.lbTitleContent.setText(QCoreApplication.translate("write", u"\ub0b4\uc6a9", None))
        
        self.btnSave.setText(QCoreApplication.translate("write", u"\uc800\uc7a5", None))
        self.btnExit.setText(QCoreApplication.translate("write", u"\uc885\ub8cc", None))
        self.spTime.setSuffix(QCoreApplication.translate("write", u"\ubd84", None))
        self.chkAutoSave.setText(QCoreApplication.translate("write", u"\uc790\ub3d9 \uc800\uc7a5", None))
        
        self.acLoad.setText(QCoreApplication.translate("write", u"\ubd88\ub7ec\uc624\uae30", None))
        self.acSave.setText(QCoreApplication.translate("write", u"\uc800\uc7a5", None))
        self.acSaveAs.setText(QCoreApplication.translate("write", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc800\uc7a5", None))
        self.acSaveCopy.setText(QCoreApplication.translate("write", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc0ac\ubcf8 \uc800\uc7a5", None))
        self.acExport_Ent.setText(QCoreApplication.translate("write", u"\ub0b4\ubcf4\ub0b4\uae30\u0028\uc904\ubc14\uafc8 \ud3ec\ud568\u0029", None))
        self.acExport_NoEnt.setText(QCoreApplication.translate("write", u"\ub0b4\ubcf4\ub0b4\uae30\u0028\uc904\ubc14\uafc8 \uc81c\uc678\u0029", None))
        self.acExit.setText(QCoreApplication.translate("write", u"\uc885\ub8cc", None))
        self.acDoubleSpace.setText(QCoreApplication.translate("write", u"\ub2e4\uc911 \uacf5\ubc31 \uc81c\uac70", None))
        self.acConfig.setText(QCoreApplication.translate("write", u"\uc124\uc815", None))
        self.acNotice.setText(QCoreApplication.translate("write", u"오픈 소스 라이선스", None))
        self.acInfo.setText(QCoreApplication.translate("write", u"\uc815\ubcf4", None))
        
        self.save.setTitle(QCoreApplication.translate("write", u"\ud30c\uc77c", None))
        self.tools.setTitle(QCoreApplication.translate("write", u"\ub3c4\uad6c", None))
        self.export.setTitle(QCoreApplication.translate("write", u"\ub0b4\ubcf4\ub0b4\uae30", None))
        self.fontSize.setTitle(QCoreApplication.translate("write", u"글자 크기", None))
        self.info.setTitle(QCoreApplication.translate("write", u"\uc815\ubcf4", None))
    # retranslateUi