# -*- coding: utf-8 -*-
from PySide2.QtCore import QRect, QTimer
from PySide2.QtGui import QFont, QIcon, QCloseEvent, QKeySequence
from PySide2.QtWidgets import *
import writeUI

import os,sys,json,datetime

HISTORY=True

CURRENT_PATH=os.path.dirname(os.path.abspath('__file__'))+'\\'
LENGTH=['1000','1500','1000']
path=CURRENT_PATH+'last.selfinstruct'
data={'1':'', '2':'', '3':'', 'auto_save':[True,1]}


def load_data(path):
    with open(path,'r',encoding='utf-8') as file:
        res=json.load(file)
    return res


def save_data(data,path):
    with open(path,'w',encoding='utf-8') as file:
        json.dump(data,file,indent=4,ensure_ascii=False)


class Write(QMainWindow,writeUI.Ui_write):
    def __init__(self,file=None):
        def count(n):
            self.__saved=False
            self.btnSave.setStyleSheet('color:red')
            self.__count(n)
        def resize(size):
            self.scwMain.resize(size.width(),self.scwMain.height())
        
        super().__init__()
        self.setupUi(self)
        
        if file:
            global path
            path=file
        
        if os.path.isfile(path):
            while True:
                try:
                    data=load_data(path)
                except json.JSONDecodeError as e:
                    reply=QMessageBox.warning(self,'Load Error','이전 데이터에 오류 발생\nTraceBack:\n%s\n재시도?' %str(e),QMessageBox.Retry|QMessageBox.Cancel)
                    if reply==QMessageBox.Cancel:
                        self.show()
                        break
                else:
                    self.__load(data)
                    break
        
        self.__tmr=QTimer()
        self.__tmr.timeout.connect(lambda: self.__save(do_history=False))
        if self.chkAutoSave.isChecked():
            self.__tmr.setInterval(self.spTime.value()*1000*60)
            self.__tmr.start()
        
        self.__count()
        
        self.__saved=True
        self.spTime.setEnabled(self.chkAutoSave.isChecked())
        
        self.show()
        
        #register shortcuts
        QShortcut(QKeySequence.fromString('Ctrl+S'),self).activated.connect(self.__save)
        
        #callback_button
        self.btnExport.clicked.connect(self.__export)
        self.btnLoad.clicked.connect(self.__load_as)
        self.btnSave.clicked.connect(self.__save)
        self.btnSaveAs.clicked.connect(self.__save_as)
        self.btnExit.clicked.connect(self.close)
        
        #callback
        self.chkAutoSave.stateChanged.connect(lambda x: self.__auto_save(bool(x)))
        self.spTime.valueChanged.connect(self.__auto_save)
        self.pteNo1.textChanged.connect(lambda: count(1))
        self.pteNo2.textChanged.connect(lambda: count(2))
        self.pteNo3.textChanged.connect(lambda: count(3))
        
        #callback_menu
        self.acLoad.triggered.connect(self.__load_as)
        self.acSave.triggered.connect(self.__save)
        self.acSaveAs.triggered.connect(self.__save_as)
        self.acExport.triggered.connect(self.__export)
        self.acExit.triggered.connect(self.close)
        #self.acActive.triggered.connect()
        #self.acInfo.triggered.connect()

        
        self.scMain.resized.connect(resize) #adjust length at resize
    
    def __count(self,n=None):
        if not n:
            a=len(self.pteNo1.toPlainText())
            b=len(self.pteNo2.toPlainText())
            c=len(self.pteNo3.toPlainText())
            self.lbCount1.setText(str(a)+'/'+LENGTH[0])
            self.lbCount2.setText(str(b)+'/'+LENGTH[1])
            self.lbCount3.setText(str(c)+'/'+LENGTH[2])
        elif n==1:
            a=len(self.pteNo1.toPlainText())
            self.lbCount1.setText(str(a)+'/'+LENGTH[0])
        elif n==2:
            b=len(self.pteNo2.toPlainText())
            self.lbCount2.setText(str(b)+'/'+LENGTH[1])
        elif n==3:
            c=len(self.pteNo3.toPlainText())
            self.lbCount3.setText(str(c)+'/'+LENGTH[2])
        else:
            raise ValueError
    
    def __auto_save(self,arg):
        if type(arg) is int:
            self.__tmr.stop()
            self.__tmr.setInterval(arg*1000*60)
            self.__tmr.start()
            self.__save(do_history=False)
        elif type(arg) is bool:
            self.spTime.setEnabled(arg)
            if arg:
                self.__tmr.setInterval(self.spTime.value()*1000*60)
                self.__tmr.start()
            else:
                self.__tmr.stop()
            self.__save(do_history=False)
        else:
            raise ValueError
    
    def __load_as(self):
        global path
        oldpath=path
        path,_=QFileDialog.getOpenFileName(self,'불러오기',CURRENT_PATH,'자기소개서 파일 (*.selfinstruct)','자기소개서 파일 (*.selfinstruct)')
        if path:
            try:
                data=load_data(path)
            except json.JSONDecodeError as e:
                reply=QMessageBox.warning(self,'Load Error','데이터 불러오기 오류 발생\nTraceBack:\n%s\n재시도?' %str(e),QMessageBox.Retry|QMessageBox.Cancel)
                if reply==QMessageBox.Retry:
                    self.__load_as()
            else:
                self.__load(data)
        else:
            path=oldpath
    
    def __load(self,data):
        self.pteNo1.setPlainText(data['1'])
        self.pteNo2.setPlainText(data['2'])
        self.pteNo3.setPlainText(data['3'])
        self.chkAutoSave.setChecked(data['save'][0])
        self.spTime.setValue(data['save'][1])
    
    def __save_as(self):
        global path
        oldpath=path
        path,_=QFileDialog.getSaveFileName(self,'저장',CURRENT_PATH,'자기소개서 파일 (*.selfinstruct)','자기소개서 파일 (*.selfinstruct)')
        if path:
            self.__save()
        else:
            path=oldpath
    
    def __save_history(self):
        if not 'history' in os.listdir():
            os.mkdir('history')
        name=datetime.datetime.now().strftime('%m-%d_%H-%M-%S')
        self.__save(CURRENT_PATH+'history\\'+name+'.selfinstruct',do_history=False)
    
    def __save(self,dst=None,*,do_history=True):
        if not dst:
            dst=path
        #pack data
        res={
            '1'    : str(self.pteNo1.toPlainText()),
            '2'    : str(self.pteNo2.toPlainText()),
            '3'    : str(self.pteNo3.toPlainText()),
            'save' : [self.chkAutoSave.isChecked(), self.spTime.value()]
        }
        #write data
        try:
            save_data(res,dst)
        except json.JSONDecodeError as e:
            reply=QMessageBox.warning(self,'Save Error','데이터 쓰기 오류 발생\nTraceBack:\n%s\n재시도?' %str(e),QMessageBox.Retry|QMessageBox.Cancel)
            if reply==QMessageBox.Retry:
                self.__save(dst)
        else:
            if HISTORY and do_history:
                self.__save_history()
                self.btnSave.setStyleSheet('')
            else:
                self.btnSave.setStyleSheet('color:blue')
            self.__saved=True
    
    def __export(self):
        path,_=QFileDialog.getSaveFileName(self,'저장',CURRENT_PATH,'텍스트 파일 (*.txt)','텍스트 파일 (*.txt)')
        if path:
            with open(path,'w') as file:
                file.write('#'*5+'1번 문항 / 글자수: %s/%s' %(len(self.pteNo1.toPlainText()),LENGTH[0])+'#'*5+'\n')
                file.write(self.pteNo1.toPlainText()+'\n')
                file.write('#'*5+'2번 문항 / 글자수: %s/%s' %(len(self.pteNo2.toPlainText()),LENGTH[1])+'#'*5+'\n')
                file.write(self.pteNo2.toPlainText()+'\n')
                file.write('#'*5+'3번 문항 / 글자수: %s/%s' %(len(self.pteNo3.toPlainText()),LENGTH[2])+'#'*5+'\n')
                file.write(self.pteNo3.toPlainText()+'\n')
    
    def closeEvent(self,event):
        if self.__saved:
            event.accept()
        else:
            reply=QMessageBox.question(self,'종료','저장하지 않고 종료?',QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel)
            if reply==QMessageBox.Save:
                self.__save()
                event.accept()
            elif reply==QMessageBox.Discard:
                event.accept()
            elif reply==QMessageBox.Cancel:
                event.ignore()


if __name__=='__main__':
    import ctypes
    myappid = 'hys.selfinstruct'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    app=QApplication(sys.argv[1:])
    
    if len(sys.argv)>1 and os.path.isfile(sys.argv[1]):
        write=Write(sys.argv[1])
    else:
        write=Write()
    
    sys.exit(app.exec_())