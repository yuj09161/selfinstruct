
class Converter:
    def __init__(self):
        
    
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