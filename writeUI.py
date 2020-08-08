# -*- coding: utf-8 -*-
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, Signal)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class CustomScrollArea(QScrollArea):
    resized=Signal(QSize)
    def resizeEvent(self,event):
        super().resizeEvent(event)
        self.resized.emit(event.size())

class Ui_write(object):
    def setupUi(self, write):
        write.resize(800, 600)
        
        #action for menu
        self.acLoad = QAction(write)
        self.acLoad.setObjectName(u"acLoad")
        self.acSave = QAction(write)
        self.acSave.setObjectName(u"acSave")
        self.acSaveAs = QAction(write)
        self.acSaveAs.setObjectName(u"acSaveAs")
        self.acExport = QAction(write)
        self.acExport.setObjectName(u"acExport")
        self.acExit = QAction(write)
        self.acExit.setObjectName(u"acExit")
        self.acActive = QAction(write)
        self.acActive.setObjectName(u"acActive")
        self.acActive.setCheckable(True)
        self.acInfo = QAction(write)
        self.acInfo.setObjectName(u"acInfo")
        
        self.centralwidget = QWidget(write)
        self.glCentral = QGridLayout(self.centralwidget)
        
        sizePolicy_PF = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy_PF.setHorizontalStretch(0)
        sizePolicy_PF.setVerticalStretch(0)
        
        sizePolicy_FF = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy_FF.setHorizontalStretch(0)
        sizePolicy_FF.setVerticalStretch(0)
        
        sizePolicy_EI = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy_EI.setHorizontalStretch(0)
        sizePolicy_EI.setVerticalStretch(0)
        
        #Main Scoll Area
        self.scMain = CustomScrollArea(self.centralwidget)
        self.scMain.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        self.scwMain = QWidget()
        self.scwMain.setGeometry(QRect(0, 0, 755, 2000))
        
        self.glMain = QGridLayout(self.scwMain)

        self.lbTitleNum = QLabel(self.scwMain)
        sizePolicy_PF.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy_PF)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleNum, 0, 0, 1, 1)

        self.lbTitleCount = QLabel(self.scwMain)
        sizePolicy_PF.setHeightForWidth(self.lbTitleCount.sizePolicy().hasHeightForWidth())
        self.lbTitleCount.setSizePolicy(sizePolicy_PF)
        self.lbTitleCount.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleCount, 0, 1, 1, 1)

        self.lbTitleContent = QLabel(self.scwMain)
        sizePolicy_PF.setHeightForWidth(self.lbTitleContent.sizePolicy().hasHeightForWidth())
        self.lbTitleContent.setSizePolicy(sizePolicy_PF)
        self.lbTitleContent.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleContent, 1, 0, 1, 2)

        self.lbNo1 = QLabel(self.scwMain)
        sizePolicy_PF.setHeightForWidth(self.lbNo1.sizePolicy().hasHeightForWidth())
        self.lbNo1.setSizePolicy(sizePolicy_PF)
        self.lbNo1.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbNo1, 2, 0, 1, 1)

        self.lbCount1 = QLabel(self.scwMain)
        sizePolicy_FF.setHeightForWidth(self.lbCount1.sizePolicy().hasHeightForWidth())
        self.lbCount1.setSizePolicy(sizePolicy_FF)
        self.lbCount1.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCount1, 2, 1, 1, 1)

        self.pteNo1 = QPlainTextEdit(self.scwMain)
        sizePolicy_EI.setHeightForWidth(self.pteNo1.sizePolicy().hasHeightForWidth())
        self.pteNo1.setSizePolicy(sizePolicy_EI)
        self.glMain.addWidget(self.pteNo1, 3, 0, 1, 2)

        self.lbNo2 = QLabel(self.scwMain)
        sizePolicy_PF.setHeightForWidth(self.lbNo2.sizePolicy().hasHeightForWidth())
        self.lbNo2.setSizePolicy(sizePolicy_PF)
        self.lbNo2.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbNo2, 4, 0, 1, 1)

        self.lbCount2 = QLabel(self.scwMain)
        sizePolicy_FF.setHeightForWidth(self.lbCount2.sizePolicy().hasHeightForWidth())
        self.lbCount2.setSizePolicy(sizePolicy_FF)
        self.lbCount2.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCount2, 4, 1, 1, 1)

        self.pteNo2 = QPlainTextEdit(self.scwMain)
        sizePolicy_EI.setHeightForWidth(self.pteNo2.sizePolicy().hasHeightForWidth())
        self.pteNo2.setSizePolicy(sizePolicy_EI)
        self.glMain.addWidget(self.pteNo2, 5, 0, 1, 2)
        
        self.lbNo3 = QLabel(self.scwMain)
        sizePolicy_PF.setHeightForWidth(self.lbNo3.sizePolicy().hasHeightForWidth())
        self.lbNo3.setSizePolicy(sizePolicy_PF)
        self.lbNo3.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbNo3, 6, 0, 1, 1)

        self.lbCount3 = QLabel(self.scwMain)
        sizePolicy_FF.setHeightForWidth(self.lbCount3.sizePolicy().hasHeightForWidth())
        self.lbCount3.setSizePolicy(sizePolicy_FF)
        self.lbCount3.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCount3, 6, 1, 1, 1)

        self.pteNo3 = QPlainTextEdit(self.scwMain)
        sizePolicy_EI.setHeightForWidth(self.pteNo3.sizePolicy().hasHeightForWidth())
        self.pteNo3.setSizePolicy(sizePolicy_EI)
        self.glMain.addWidget(self.pteNo3, 7, 0, 1, 2)

        self.scMain.setWidget(self.scwMain)
        self.glCentral.addWidget(self.scMain, 0, 0, 1, 1)
    
        #Menu Widget
        self.widMenu = QWidget(self.centralwidget)
        self.glMenu = QGridLayout(self.widMenu)
        
        self.btnSave = QPushButton(self.widMenu)
        sizePolicy_FF.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy_FF)
        self.glMenu.addWidget(self.btnSave, 0, 0, 1, 1)
        
        '''
        self.btnExport = QPushButton(self.widMenu)
        sizePolicy_FF.setHeightForWidth(self.btnExport.sizePolicy().hasHeightForWidth())
        self.btnExport.setSizePolicy(sizePolicy_FF)
        self.glMenu.addWidget(self.btnExport, 0, 0, 1, 1)
        
        self.btnLoad = QPushButton(self.widMenu)
        sizePolicy_FF.setHeightForWidth(self.btnLoad.sizePolicy().hasHeightForWidth())
        self.btnLoad.setSizePolicy(sizePolicy_FF)
        self.glMenu.addWidget(self.btnLoad, 0, 1, 1, 1)
        
        self.btnSaveAs = QPushButton(self.widMenu)
        sizePolicy_FF.setHeightForWidth(self.btnSaveAs.sizePolicy().hasHeightForWidth())
        self.btnSaveAs.setSizePolicy(sizePolicy_FF)
        self.glMenu.addWidget(self.btnSaveAs, 0, 3, 1, 1)
        '''
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.glMenu.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.chkAutoSave = QCheckBox(self.widMenu)
        sizePolicy_FF.setHeightForWidth(self.chkAutoSave.sizePolicy().hasHeightForWidth())
        self.chkAutoSave.setSizePolicy(sizePolicy_FF)
        self.glMenu.addWidget(self.chkAutoSave, 0, 5, 1, 1)

        self.spTime = QSpinBox(self.widMenu)
        sizePolicy_FF.setHeightForWidth(self.spTime.sizePolicy().hasHeightForWidth())
        self.spTime.setSizePolicy(sizePolicy_FF)
        self.spTime.setMinimum(1)
        self.spTime.setMaximum(60)
        self.glMenu.addWidget(self.spTime, 0, 6, 1, 1)

        self.btnExit = QPushButton(self.widMenu)
        sizePolicy_FF.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy_FF)
        self.glMenu.addWidget(self.btnExit, 0, 7, 1, 1)

        self.glCentral.addWidget(self.widMenu, 1, 0, 1, 1)

        write.setCentralWidget(self.centralwidget)
        
        #menu
        self.menubar = QMenuBar(write)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.save = QMenu(self.menubar)
        self.save.setObjectName(u"save")
        self.config = QMenu(self.menubar)
        self.config.setObjectName(u"config")
        self.subAutoSave = QMenu(self.config)
        self.subAutoSave.setObjectName(u"subAutoSave")
        self.info = QMenu(self.menubar)
        self.info.setObjectName(u"info")
        write.setMenuBar(self.menubar)

        self.menubar.addAction(self.save.menuAction())
        self.menubar.addAction(self.config.menuAction())
        self.menubar.addAction(self.info.menuAction())
        self.save.addAction(self.acLoad)
        self.save.addAction(self.acSave)
        self.save.addSeparator()
        self.save.addAction(self.acSaveAs)
        self.save.addAction(self.acExport)
        self.save.addSeparator()
        self.save.addAction(self.acExit)
        self.config.addAction(self.subAutoSave.menuAction())
        self.subAutoSave.addAction(self.acActive)
        self.info.addAction(self.acInfo)

        self.retranslateUi(write)

        QMetaObject.connectSlotsByName(write)
    # setupUi

    def retranslateUi(self, write):
        write.setWindowTitle(QCoreApplication.translate("write", u"자기소개서 작성 보조", None))
        self.lbNo3.setText(QCoreApplication.translate("write", u"3번: 학교 생활 중 배려, 나눔, 협력, 갈등 관리 등을\n실천한 사례를 들고, 그 과정을 통해 배우고 느낀점을 중심으로 기술", None))
        self.lbCount1.setText("")
        self.lbTitleNum.setText(QCoreApplication.translate("write", u"\ubc88\ud638", None))
        self.lbTitleCount.setText(QCoreApplication.translate("write", u"\uae00\uc790\uc218", None))
        self.lbNo2.setText(QCoreApplication.translate("write", u"2번: 고등학교 재학기간 중 본인이 의미를 두고 노력했던\n교내 활동(3개 이내)을 통해 배우고 느낀점을 중심으로 기술", None))
        self.lbNo1.setText(QCoreApplication.translate("write", u"1번: 고등학교 재학기간 중 학업에 기울인\n노력과 학습 경험을 통해, 배우고 느낀점을 중심으로 기술", None))
        self.lbCount2.setText("")
        self.lbCount3.setText("")
        self.lbTitleContent.setText(QCoreApplication.translate("write", u"\ub0b4\uc6a9", None))
        
        self.btnSave.setText(QCoreApplication.translate("write", u"\uc800\uc7a5", None))
        '''
        self.btnSaveAs.setText(QCoreApplication.translate("write", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc800\uc7a5", None))
        self.btnLoad.setText(QCoreApplication.translate("write", u"\ubd88\ub7ec\uc624\uae30", None))
        self.btnExport.setText(QCoreApplication.translate("write", u"\ub0b4\ubcf4\ub0b4\uae30", None))
        '''
        self.btnExit.setText(QCoreApplication.translate("write", u"\uc885\ub8cc", None))
        self.spTime.setSuffix(QCoreApplication.translate("write", u"\ubd84", None))
        self.chkAutoSave.setText(QCoreApplication.translate("write", u"\uc790\ub3d9 \uc800\uc7a5", None))
        
        
        self.acLoad.setText(QCoreApplication.translate("write", u"\ubd88\ub7ec\uc624\uae30", None))
        self.acSave.setText(QCoreApplication.translate("write", u"\uc800\uc7a5", None))
        self.acSaveAs.setText(QCoreApplication.translate("write", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc800\uc7a5", None))
        self.acExport.setText(QCoreApplication.translate("write", u"\ub0b4\ubcf4\ub0b4\uae30", None))
        self.acExit.setText(QCoreApplication.translate("write", u"\uc885\ub8cc", None))
        self.acActive.setText(QCoreApplication.translate("write", u"\uc2dc\uac04", None))
        self.acInfo.setText(QCoreApplication.translate("write", u"\uc815\ubcf4", None))
        self.save.setTitle(QCoreApplication.translate("write", u"\ud30c\uc77c", None))
        self.config.setTitle(QCoreApplication.translate("write", u"\uc124\uc815", None))
        self.subAutoSave.setTitle(QCoreApplication.translate("write", u"\uc790\ub3d9 \uc800\uc7a5", None))
        self.info.setTitle(QCoreApplication.translate("write", u"\uc815\ubcf4", None))
    # retranslateUi