# -*- coding: utf-8 -*-
from PySide2.QtCore import QRect, QTimer
from PySide2.QtGui import QFont, QIcon, QCloseEvent, QKeySequence
from PySide2.QtWidgets import *
import writeUI

import os,sys,json,datetime,re

#Config
HISTORY=True
#end Config

NL='\n'
CURRENT_PATH=os.path.dirname(os.path.abspath('__file__'))+'\\'
DEFAULT_PATH=CURRENT_PATH+'last.selfinstruct'
FILTERS=('텍스트 파일 (*.txt)','Excel 호환 (*.tsv)')
#data={'1':'', '2':'', '3':'', 'auto_save':[True,1]}
#LENGTH=['1000','1500','1000']

LOGO='''
writed with:
###############################

 H   H Y   Y   SSS   `s
 H   H  Y Y   S      self
 HHHHH   Y     SSS   자기소개서
 H   H   Y        S  instruct
 H   H   Y     SSS   helper

###############################
'''


def load_data(path):
    with open(path,'r',encoding='utf-8') as file:
        res=json.load(file)
    return res


def save_data(data,path):
    with open(path,'w',encoding='utf-8') as file:
        json.dump(data,file,indent=4,ensure_ascii=False)



class Write(QMainWindow,writeUI.Ui_write):
    def __init__(self,file=DEFAULT_PATH):
        def resize(size):
            self.scwMain.resize(size.width(),self.scwMain.height())
        def rm_dspace():
            for pte in self.pte:
                pte.setPlainText(re.sub(' +',' ',pte.toPlainText()))
        
        super().__init__()
        self.__oldpath=file
        
        if os.path.isfile(file):
            while True:
                try:
                    data=load_data(file)
                except json.JSONDecodeError as e:
                    reply=QMessageBox.warning(self,'Load Error','이전 데이터에 오류 발생\nTraceBack:\n%s\n재시도?' %str(e),QMessageBox.Retry|QMessageBox.Cancel)
                    if reply==QMessageBox.Cancel:
                        self.destroy()
                        sys.exit(1)
                else:
                    break
        else:
            QMessageBox.critical(self,'File not exist','없는 파일')
            self.destroy()
            sys.exit(2)
        
        self.article=[]
        for k in range(len(data)-1):
            self.article.append(data[k][:3])
        
        self.setupUi(self,self.article)
        self.__loader(data)
        
        self.__tmr=QTimer()
        self.__tmr.timeout.connect(lambda: self.__save(do_history=False))
        if self.chkAutoSave.isChecked():
            self.__tmr.setInterval(self.spTime.value()*1000*60)
            self.__tmr.start()
        
        self.__saved=True
        self.spTime.setEnabled(self.chkAutoSave.isChecked())
        
        self.show()
        
        #register shortcuts
        QShortcut(QKeySequence.fromString('Ctrl+S'),self).activated.connect(self.__save)
        
        #callback_button
        self.btnSave.clicked.connect(self.__save)
        self.btnExit.clicked.connect(self.close)
        
        #callback
        self.chkAutoSave.stateChanged.connect(lambda x: self.__auto_save(bool(x)))
        self.spTime.valueChanged.connect(self.__auto_save)
        
        #callback_menu
        self.acLoad.triggered.connect(self.__load_as)
        self.acSave.triggered.connect(self.__save)
        self.acSaveAs.triggered.connect(lambda: self.__save_as(True))
        self.acSaveCopy.triggered.connect(lambda: self.__save_as(False))
        self.acExport.triggered.connect(self.__export)
        self.acExit.triggered.connect(self.close)
        self.acDoubleSpace.triggered.connect(rm_dspace)
        #self.acConfig.triggered.connect(self.__config)
        #self.acInfo.triggered.connect(self.__info)

        self.scMain.resized.connect(resize) #adjust length at resize
    
    def __count(self,n=None):
        if not n:
            for k in range(self.article_count):
                tmp=self.pte[k].toPlainText()
                self.lbCount[k].setText(f'{len(tmp)}/{self.article[k][2]}{NL}({len(tmp.replace(NL,""))})')  
        else:
            tmp=self.pte[n].toPlainText()
            self.lbCount[n].setText(f'{len(tmp)}/{self.article[n][2]}{NL}({len(tmp.replace(NL,""))})')
    
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
        path,_=QFileDialog.getOpenFileName(self,'불러오기',CURRENT_PATH,'자기소개서 파일 (*.selfinstruct)','자기소개서 파일 (*.selfinstruct)')
        if path:
            try:
                data=load_data(path)
            except json.JSONDecodeError as e:
                reply=QMessageBox.warning(self,'Load Error','데이터 불러오기 오류 발생\nTraceBack:\n%s\n재시도?' %str(e),QMessageBox.Retry|QMessageBox.Cancel)
                if reply==QMessageBox.Retry:
                    self.__load_as()
            else:
                self.__loader(data)
                self.__oldpath=path
    
    def __loader(self,data):
        def count(n):
            self.__saved=False
            self.btnSave.setStyleSheet('color:red')
            self.__count(n)
        
        def do_connect(k):
            self.pte[k].textChanged.connect(lambda: count(k))
        
        self.article=[]
        self.article_count=len(data)-1
        for k in range(self.article_count):
            self.article.append(data[k][:3])
            self.pte[k].setPlainText(data[k][3])
            do_connect(k)
        self.chkAutoSave.setChecked(data[-1][0])
        self.spTime.setValue(data[-1][1])
        self.__count()
    
    def __save_as(self,change_path=True):
        path,_=QFileDialog.getSaveFileName(self,'저장',CURRENT_PATH,'자기소개서 파일 (*.selfinstruct)','자기소개서 파일 (*.selfinstruct)')
        if path:
            self.__save(dst=path,change_path=change_path,force=True)
    
    def __save_history(self):
        if not 'history' in os.listdir():
            os.mkdir(CURRENT_PATH+'history')
        name=datetime.datetime.now().strftime('%m-%d_%H-%M-%S')
        self.__save(dst=CURRENT_PATH+'history\\'+name+'.selfinstruct',do_history=False)
    
    def __save(self,*,dst=None,do_history=True,change_path=True,force=False):
        if not self.__saved or force:
            if not dst:
                dst=self.__oldpath
            #pack data
            res=[]
            for k in range(self.article_count):
                res.append((*self.article[k],self.pte[k].toPlainText()))
            res.append((self.chkAutoSave.isChecked(), self.spTime.value()))
            #write data
            try:
                save_data(res,dst)
            except json.JSONDecodeError as e:
                reply=QMessageBox.warning(self,'Save Error','데이터 쓰기 오류 발생\nTraceBack:\n%s\n재시도?' %str(e),QMessageBox.Retry|QMessageBox.Cancel)
                if reply==QMessageBox.Retry:
                    self.__save(dst=dst,do_history=do_history,change_path=change_path,force=force)
            else:
                if do_history and HISTORY:
                    self.__save_history()
                    self.btnSave.setStyleSheet('')
                    self.__saved=True
                else:
                    self.btnSave.setStyleSheet('color:blue')
                if change_path:
                    self.__oldpath=dst
    
    def __export(self):
        path,ext=QFileDialog.getSaveFileName(self,'저장',CURRENT_PATH,';;'.join(FILTERS),FILTERS[0])
        if FILTERS.index(ext)==0:
            lnsep='\n\n'
            enc='utf-8'
        elif FILTERS.index(ext)==1:
            lnsep='\n'
            enc='cp949'
        else:
            raise ValueError
        if path:
            with open(path,'w',encoding=enc) as file:
                for k in range(self.article_count):
                    content=self.pte[k].toPlainText().replace('\n','')
                    file.write(f'#####{self.article[k][0]} / 글자수: {len(content)}/{self.article[k][2]}#####'+lnsep)
                    file.write(content+lnsep)
                file.write(LOGO)
    
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
        write=Write(DEFAULT_PATH)
    
    sys.exit(app.exec_())