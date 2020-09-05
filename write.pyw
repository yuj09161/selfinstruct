# -*- coding: utf-8 -*-
from PySide2.QtCore import Qt, QRect, QTimer
from PySide2.QtGui import QFont, QIcon, QCloseEvent, QKeySequence
from PySide2.QtWidgets import *
import writeUI

import os,sys,json,datetime,re,argparse

#Config
HISTORY=True
#end Config

#constants
NL='\n'
CURRENT_PATH=os.path.dirname(os.path.abspath('__file__'))+'\\'
DEFAULT_PATH=CURRENT_PATH+'last.selfinstruct'
FILTER_EXPORT=('텍스트 파일 (*.txt)','Excel 호환 (*.tsv)')

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
        def do_connect_of_font(k):
            ac=self.fontAction[k]
            ac.triggered.connect(lambda: self.__set_font(ac.font_size_of_this))
            if ac.font_size_of_this==9:
                ac.setChecked(True)
        
        super().__init__()
        
        self.article_count=0
        self.__font_size=9
        self.__oldpath=file
        self.__font=None
        
        self.lbNo=[]
        self.lbCount=[]
        self.pte=[]
        self.fontAction=[]
        
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
        
        self.setupUi(self)
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
        QShortcut(QKeySequence.fromString('Ctrl+D'),self).activated.connect(rm_dspace)
        
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
        self.acExport_Ent.triggered.connect(lambda: self.__export(True))
        self.acExport_NoEnt.triggered.connect(lambda: self.__export(False))
        for k in range(len(self.fontAction)):
            do_connect_of_font(k)
        self.acExit.triggered.connect(self.close)
        self.acDoubleSpace.triggered.connect(rm_dspace)
        #self.acConfig.triggered.connect(self.__config)
        #self.acInfo.triggered.connect(self.__info)

        self.scMain.resized.connect(resize) #adjust length at resize
    
    def __count(self,n=-1):
        if n<0:
            for k in range(self.article_count):
                tmp=self.pte[k].toPlainText()
                self.lbCount[k].setText(f'{len(tmp)}/{self.article[k][2]}{NL}({len(tmp.replace(NL,""))})')  
        else:
            self.__saved=False
            self.btnSave.setStyleSheet('color:red')
            tmp=self.pte[n].toPlainText()
            self.lbCount[n].setText(f'{len(tmp)}/{self.article[n][2]}{NL}({len(tmp.replace(NL,""))})')
    
    def __set_font(self,size=None):
        if not size:
            size=self.__font_size
        else:
            self.__font_size=size
        font=QFont("Gulim",pointSize=size,weight=QFont.Light)
        for k in range(self.article_count):
            self.pte[k].setFont(font)
    
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
        path,_=QFileDialog.getOpenFileName(self,'불러오기',CURRENT_PATH,';;'.join(self.__file_filter),self.__file_filter[0])
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
        def do_connect(k):
            try:
                self.pte[k].textChanged.disconnect()
            except:
                pass
            self.pte[k].textChanged.connect(lambda: self.__count(k))
        
        self.article=[]
        oldcnt=self.article_count
        self.article_count=len(data)-1
        self.__article_height_multi=data[-1][2]
        self.__extension=data[-1][3:5]
        
        if self.article_count>oldcnt: #if needs more article(s)
            for k in range(oldcnt,self.article_count): #generate widget(s)
                lbNo = QLabel(self.scwMain)
                self.sizePolicy_PF.setHeightForWidth(lbNo.sizePolicy().hasHeightForWidth())
                lbNo.setSizePolicy(self.sizePolicy_PF)
                lbNo.setAlignment(Qt.AlignCenter)
                self.glMain.addWidget(lbNo, 2*k+2, 0, 1, 1)
                self.lbNo.append(lbNo)

                lbCount = QLabel(self.scwMain)
                self.sizePolicy_FF.setHeightForWidth(lbCount.sizePolicy().hasHeightForWidth())
                lbCount.setSizePolicy(self.sizePolicy_FF)
                lbCount.setAlignment(Qt.AlignCenter)
                lbCount.setMinimumHeight(32)
                self.glMain.addWidget(lbCount, 2*k+2, 1, 1, 1)
                self.lbCount.append(lbCount)

                pte = QPlainTextEdit(self.scwMain)
                self.sizePolicy_EP.setHeightForWidth(pte.sizePolicy().hasHeightForWidth())
                pte.setSizePolicy(self.sizePolicy_EP)
                self.glMain.addWidget(pte, 2*k+3, 0, 1, 2)
                self.pte.append(pte)
        elif self.article_count<oldcnt: #if needs less article(s)
            for k in range(oldcnt-1,self.article_count-1,-1): #remove widget(s)
                self.glMain.removeWidget(self.lbNo[k])
                self.glMain.removeWidget(self.lbCount[k])
                self.glMain.removeWidget(self.pte[k])
                
                self.lbNo[k].setParent(None)
                self.lbCount[k].setParent(None)
                self.pte[k].setParent(None)
                
                del self.lbNo[k]
                del self.lbCount[k]
                del self.pte[k]
        
        for k in range(self.article_count):
            #get article
            self.article.append(data[k][:3])
            #set text of title QLabel
            self.lbNo[k].setText(': '.join(data[k][:2]))
            #adjust height of QPlainTextEdit
            self.pte[k].setMaximumHeight(data[k][2]*self.__article_height_multi)
            self.pte[k].setMinimumHeight(data[k][2]*self.__article_height_multi)
            #set text of QPlainTextEdit
            self.pte[k].setPlainText(data[k][3])
            do_connect(k)
        #set autosave state
        self.chkAutoSave.setChecked(data[-1][0])
        self.spTime.setValue(data[-1][1])
        #set window title&file extension
        self.setWindowTitle(self.__extension[0]+' \uc791\uc131 \ubcf4\uc870')
        self.__file_filter=(f'{self.__extension[0]} 파일 (*.{self.__extension[1]})','모든 파일 (*.*)')
        #adjust height of scroll area widget&Scroll up
        app.processEvents()
        self.scwMain.setGeometry(QRect(0, 0, 755, self.scwMain.sizeHint().height()))
        v_scbar=self.scMain.verticalScrollBar()
        v_scbar.setValue(v_scbar.minimum())
        #count words
        self.__count()
    
    def __save_as(self,change_path=True):
        path,_=QFileDialog.getSaveFileName(self,'저장',CURRENT_PATH,';;'.join(self.__file_filter[:-1]),self.__file_filter[0])
        if path:
            self.__save(dst=path,change_path=change_path,force=True)
    
    def __save_history(self):
        if not 'history' in os.listdir():
            os.mkdir(CURRENT_PATH+'history')
        name=datetime.datetime.now().strftime('%m-%d_%H-%M-%S')
        self.__save(dst=f'{CURRENT_PATH}history\\{name}.{self.__extension[1]}',do_history=False)
    
    def __save(self,*,dst=None,do_history=True,change_path=True,force=False):
        if not self.__saved or force:
            if not dst:
                dst=self.__oldpath
            #pack data
            res=[]
            for k in range(self.article_count):
                res.append((*self.article[k],self.pte[k].toPlainText()))
            res.append(
                (
                    self.chkAutoSave.isChecked(),
                    self.spTime.value(),
                    self.__article_height_multi,
                    *self.__extension
                )
            )
            #write data
            try:
                save_data(res,dst)
            except json.JSONDecodeError as e:
                reply=QMessageBox.warning(self,'Save Error','데이터 쓰기 오류 발생\nTraceBack:\n%s\n재시도?' %str(e),QMessageBox.Retry|QMessageBox.Cancel)
                if reply==QMessageBox.Retry:
                    self.__save(dst=dst,do_history=do_history,change_path=change_path,force=force)
            else:
                if HISTORY:
                    if do_history:
                        self.__save_history()
                        self.btnSave.setStyleSheet('')
                        self.__saved=True
                    else:
                        self.btnSave.setStyleSheet('color:blue')
                else:
                    self.btnSave.setStyleSheet('')
                    self.__saved=True
                if change_path:
                    self.__oldpath=dst
    
    def __export(self,include_ent):
        path,ext=QFileDialog.getSaveFileName(self,'저장',CURRENT_PATH,';;'.join(FILTER_EXPORT),FILTER_EXPORT[0])
        if FILTER_EXPORT.index(ext)==0:
            lnsep='\n\n'
            enc='utf-8'
        elif FILTER_EXPORT.index(ext)==1:
            lnsep='\n'
            enc='cp949'
        else:
            raise ValueError
        if path:
            with open(path,'w',encoding=enc) as file:
                for k in range(self.article_count):
                    if include_ent:
                        content=self.pte[k].toPlainText()
                    else:
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
    
    parser=argparse.ArgumentParser()
    parser.add_argument('file_name',help='불러올 파일',nargs='?',default=DEFAULT_PATH)
    parsed_args=parser.parse_args()
    
    app=QApplication(sys.argv[1:])
    
    Write(parsed_args.file_name)
    sys.exit(app.exec_())