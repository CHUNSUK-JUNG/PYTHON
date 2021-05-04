import inspect, os, random, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class MemoPad(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, flags=Qt.Window)
        self.initUi()

    def initUi(self):
        self.menu_bar = MenuBar()
        self.status_bar = StatusBar()
        self.translator = QTranslator()  # I18N 관련
        self.filename = str()
        self.change_locale("translate\\" + QLocale.system().name() + ".qm")  # 시스템 로케일 사용
        self.document_prt = QPrinter()
        self.init_setting()
        self.init_window()

    def change_locale(self, filename): # 번역 파일을 받아서 로드
        global app
        app.removeTranslator(self.translator)
        self.translator.load(filename)
        app.installTranslator(self.translator)

    def changeEvent(self, event): # 언어의 변화를 감시
        if event.type() == QEvent.LanguageChange: # 들어온 이벤트 중 언어가 바뀌었는지 검사
            self.retranslate_ui()
        QMainWindow.changeEvent(self, event)  # 나머지 일을 할 수 있게 넘겨줌

    def retranslate_ui(self):
        self.set_window_title()
        self.menu.retranslate_ui()

    def init_setting(self):
        self.filename = str()
        self.set_window_title()
        self.textedit.clear()
        self.menu.act_save_file.setEnabled(False)
        self.is_saved = True

    def init_window(self):
        self.set_window_title() #
        self.setWindowIcon(QIcon('Window.png')) #
        self.setGeometry(300, 300, 600, 600) #
        self.init_window_center() #
        self.setMenuBar(self.menu_bar) 
        self.toolBar()
        self.textEdit() #
        self.setStatusBar(self.status_bar) #
        self.init_signal() #

    def set_window_title(self):
        filename = self.filename
        if not self.filename:
            filename = self.tr("untitled")
        else:
            filename = filename[filename.rfind('/') + 1:]
        self.setWindowTitle("{0} - {1}".format(filename, self.tr("Notepad")))

    def init_window_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def textEdit(self):
        self.textedit = QTextEdit()
        self.textedit.setStyleSheet('border-style : solid;' 'border-width : 2px;'
                                    'border-color : black;' 'border-radius : 5px')
        self.setCentralWidget(self.textedit)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.saveAction()
            event.accept()
        else:
            event.ignore()

    def init_signal(self):
        self.textedit.textChanged.connect(self.slot_contents_changed)
        self.textedit.cursorPositionChanged.connect(lambda: self.status_bar.change_cursor_info(self.textedit.textCursor()))
        self.menu.sig_status_bar.connect(self.status_bar.setVisible)
        self.menu.sig_new_file.connect(self.slot_new)
        self.menu.sig_open_file.connect(self.slot_open)
        self.menu.sig_save_file.connect(self.slot_save)
        self.menu.sig_page_setup.connect(self.slot_page_setup)
        self.menu.sig_print.connect(self.slot_print)
        self.menu.sig_status_bar.connect(self.slot_status_bar)

    @pyqtSlot()
    def slot_contents_changed(self):
        self.is_saved = False
        self.menu.act_save_file.setEnabled(True)

    @pyqtSlot()
    def slot_new(self):
        if not self.is_saved:
            reply = QMessageBox.information(
                self, self.tr("Save"), self.tr("작성한 내용을 저장하시겠습니까?"),
                QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Save)
            if reply == QMessageBox.Save:
                if not self.slot_save():
                    return
            elif reply == QMessageBox.No:
                pass
            else:
                return
        self.init_setting()

    @pyqtSlot()
    def slot_open(self):
        fdial = QFileDialog(self)
        fdial.setAcceptMode(QFileDialog.AcceptOpen)
        file_name = fdial.getOpenFileName(self, self.tr("Open File"), filter='*.txt')[0]
        if file_name == '':
            return False
        fd = open(file_name, "r")
        buf = fd.read()
        fd.close()
        self.textedit.clear()
        self.textedit.insertPlainText(buf)
        self.filename = file_name
        self.set_window_title()
        self.is_saved = True
        return True

    @pyqtSlot()
    def slot_save(self):
        buf = self.textedit.toPlainText()
        fdial = QFileDialog(self)
        fdial.setAcceptMode(QFileDialog.AcceptSave)
        file_name = self.filename
        if not self.filename:
            file_name = fdial.getSaveFileName(self, self.tr("Save File"), filter='*.txt')[0]
        if not file_name:
            return False
        fd = open(file_name, 'w')
        fd.write(buf)
        fd.close()
        self.filename = file_name
        self.menu.act_save_file.setEnabled(False)
        self.set_window_title()
        return True

    @pyqtSlot()
    def slot_page_setup(self):
        page_dialog = QPageSetupDialog(self.document_prt)
        if page_dialog.exec() != QDialog.Accepted:
            return
        self.document_prt = page_dialog.printer()

    @pyqtSlot()
    def slot_print(self):
        printer = QPrintDialog(self.document_prt)
        if printer.exec() != QDialog.Accepted:
            return
        doc = QTextDocument()
        doc.setPlainText(self.editor.toPlainText())
        doc.print(self.document_prt)

    @pyqtSlot()
    def slot_quit(self):
        pass

    @pyqtSlot(bool)
    def slot_status_bar(self, status):
        print(status)
        pass




    def toolBar(self):
        self.fileToolbar()
        self.formatToolbar()

    def fileToolbar(self):
        self.toolbar = self.addToolBar('File')
        newaction = QAction(QIcon('New.png'), 'New', self)
        newaction.setStatusTip('New')
        newaction.triggered.connect(self.newAction)
        self.toolbar.addAction(newaction)
        openaction = QAction(QIcon('Open.png'), 'Open', self)
        openaction.setStatusTip('Open')
        openaction.triggered.connect(self.openAction)
        self.toolbar.addAction(openaction)
        saveaction = QAction(QIcon('Save.png'), 'Save', self)
        saveaction.setStatusTip('Save')
        saveaction.triggered.connect(self.saveAction)
        self.toolbar.addAction(saveaction)
        printaction = QAction(QIcon('Print.png'), 'Print', self)
        printaction.setStatusTip('Print')
        printaction.triggered.connect(self.printAction)
        self.toolbar.addAction(printaction)
        exitaction = QAction(QIcon('Exit.png'), 'Exit', self)
        exitaction.setStatusTip('Exit')
        exitaction.triggered.connect(qApp.exit)
        self.toolbar.addAction(exitaction)

    def formatToolbar(self):
        self.toolbar = self.addToolBar('Format')
        fontaction = QAction(QIcon('Font.png'), 'Font', self)
        fontaction.setStatusTip('Font')
        fontaction.triggered.connect(self.fontAction)
        self.toolbar.addAction(fontaction)
        fontcoloraction = QAction(QIcon('FontColor.png'), 'Font Color', self)
        fontcoloraction.setStatusTip('Color')
        fontcoloraction.triggered.connect(self.fontcolorAction)
        self.toolbar.addAction(fontcoloraction)
        backgroundcoloraction = QAction(QIcon('BackgroundColor.png'), 'Background Color', self)
        backgroundcoloraction.setStatusTip('Background Color')
        backgroundcoloraction.triggered.connect(self.backgroundcolorAction)
        self.toolbar.addAction(backgroundcoloraction)





class MenuBar(QMenuBar):
    sig_new_file = pyqtSignal()
    sig_open_file = pyqtSignal()
    sig_save_file = pyqtSignal()
    sig_page_setup = pyqtSignal()
    sig_print = pyqtSignal()
    sig_exit = pyqtSignal()
    sig_status_bar = pyqtSignal(bool)

    def __init__(self):
        QMenuBar.__init__(self)
        self.init_menu_file()
        self.init_menu_edit()
        self.init_menu_format()
        self.init_menu_view()
        self.init_menu_help()
        self.set_all_text()

    def init_menu_file(self):
        # Action 설정
        # 새 파일
        self.act_new_file = QAction(self)
        self.act_new_file.setShortcut(QKeySequence('Ctrl+N'))
        self.act_new_file.triggered.connect(lambda : self.sig_new_file.emit())
        # self.act_new_file.triggered.emmit(self.slot_new)
        # 열기
        self.act_open_file = QAction(self)
        self.act_open_file.setShortcut(QKeySequence('Ctrl+O'))
        self.act_open_file.triggered.connect(lambda : self.sig_open_file.emit())
        # 저장
        self.act_save_file = QAction(self)
        self.act_save_file.setShortcut(QKeySequence('Ctrl+S'))
        self.act_save_file.triggered.connect(lambda : self.sig_save_file.emit())
        # 다른 이름으로 저장
        self.act_save_as_file = QAction(self)
        self.act_save_as_file.triggered.connect(self.slot_save_as)
        # 페이지 설정
        self.act_page_setup = QAction(self)
        self.act_page_setup.setShortcut(QKeySequence('Ctrl+S'))
        self.act_page_setup.triggered.connect(lambda : self.sig_page_setup.emit())
        # 프린트
        self.act_print = QAction(self)
        self.act_print.setShortcut(QKeySequence('Ctrl+P'))
        self.act_print.triggered.connect(lambda : self.sig_print.emit())
        # 끝내기
        self.act_quit = QAction(self.tr('Exit') + "(&X)", self)
        self.act_quit.triggered.connect(lambda : self.sig_exit.emit())
        # 메뉴바 생성 및 액션 적용
        # addAction한 차례로 삽입

        self.menu_file = self.addMenu(self.tr("File") + "(&F)")
        self.menu_file.addAction(self.act_new_file)
        self.menu_file.addAction(self.act_open_file)
        self.menu_file.addAction(self.act_save_file)
        self.menu_file.addAction(self.act_save_as_file)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_page_setup)
        self.menu_file.addAction(self.act_print)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_quit)

    def init_menu_edit(self):
        # 실행취소
        self.act_undo = QAction(self)
        self.act_undo.setShortcut(QKeySequence('Ctrl+Z'))
        self.act_undo.triggered.connect(self.slot_undo)
        # 잘라내기
        self.act_cut = QAction(self)
        self.act_cut.setShortcut(QKeySequence('Ctrl+X'))
        self.act_cut.triggered.connect(self.slot_cut)
        # 복사
        self.act_copy = QAction(self)
        self.act_copy.setShortcut(QKeySequence('Ctrl+C'))
        self.act_copy.triggered.connect(self.slot_copy)
        # 붙여넣기
        self.act_paste = QAction(self)
        self.act_paste.setShortcut(QKeySequence('Ctrl+V'))
        self.act_paste.triggered.connect(self.slot_paste)
        # 삭제
        self.act_del = QAction(self)
        self.act_del.setShortcut(QKeySequence('Del'))
        self.act_del.triggered.connect(self.slot_del)
        # 찾기
        self.act_find = QAction(self)
        self.act_find.setShortcut(QKeySequence('Ctrl+F'))
        self.act_find.triggered.connect(self.slot_find)
        # 다음찾기
        self.act_find_next = QAction(self)
        self.act_find_next.setShortcut(QKeySequence('F3'))
        self.act_find_next.triggered.connect(self.slot_find_next)
        # 바꾸기
        self.act_replace = QAction(self)
        self.act_replace.setShortcut(QKeySequence('Ctrl+H'))
        self.act_replace.triggered.connect(self.slot_replace)
        # 이동
        self.act_go_to = QAction(self)
        self.act_go_to.setShortcut(QKeySequence('Ctrl+G'))
        self.act_go_to.triggered.connect(self.slot_go_to)
        # 모두선택
        self.act_select_all = QAction(self)
        self.act_select_all.setShortcut(QKeySequence('Ctrl+A'))
        self.act_select_all.triggered.connect(self.slot_select_all)
        # 시간날짜
        self.act_time_date = QAction(self)
        self.act_time_date.setShortcut(QKeySequence('F5'))
        self.act_time_date.triggered.connect(self.slot_time_date)

        self.menu_edit = self.addMenu(self.tr('Edit') + "(&E)")
        self.menu_edit.addAction(self.act_undo)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.act_cut)
        self.menu_edit.addAction(self.act_copy)
        self.menu_edit.addAction(self.act_paste)
        self.menu_edit.addAction(self.act_del)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.act_find)
        self.menu_edit.addAction(self.act_find_next)
        self.menu_edit.addAction(self.act_replace)
        self.menu_edit.addAction(self.act_go_to)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.act_select_all)
        self.menu_edit.addAction(self.act_time_date)

    def init_menu_format(self):
        # 자동 줄 바꾹
        self.act_word_wrap = QAction(self)
        self.act_word_wrap.triggered.connect(self.slot_word_wrap)
        # 글꼴
        self.act_font = QAction(self)
        self.act_font.triggered.connect(self.slot_font)

        self.menu_format = self.addMenu(self.tr('Format') + "(&O)")
        self.menu_format.addAction(self.act_word_wrap)
        self.menu_format.addAction(self.act_font)

    def init_menu_view(self):
        self.act_status_bar = QAction(self)
        self.act_status_bar.setCheckable(True)
        self.act_status_bar.triggered.connect(lambda : self.sig_status_bar.emit(self.act_status_bar.isChecked()))

        self.menu_view = self.addMenu(self.tr('View') + "(&V)")
        self.menu_view.addAction(self.act_status_bar)

    def init_menu_help(self):
        self.act_help = QAction(self)
        self.act_help.triggered.connect(self.slot_help)
        # 메모장 정보
        self.act_about = QAction(self)
        self.act_about.triggered.connect(self.slot_about)

        self.menu_help = self.addMenu(self.tr('Help') + "(&H)")
        self.menu_help.addAction(self.act_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.act_about)

    @pyqtSlot()
    def slot_save_as(self):
        pass

    @pyqtSlot()
    def slot_undo(self):
        pass

    @pyqtSlot()
    def slot_cut(self):
        pass

    @pyqtSlot()
    def slot_copy(self):
        pass

    @pyqtSlot()
    def slot_paste(self):
        pass

    @pyqtSlot()
    def slot_del(self):
        pass

    @pyqtSlot()
    def slot_find(self):
        pass

    @pyqtSlot()
    def slot_find_next(self):
        pass

    @pyqtSlot()
    def slot_replace(self):
        pass

    @pyqtSlot()
    def slot_go_to(self):
        pass

    @pyqtSlot()
    def slot_select_all(self):
        pass

    @pyqtSlot()
    def slot_time_date(self):
        pass

    @pyqtSlot()
    def slot_word_wrap(self):
        pass

    @pyqtSlot()
    def slot_font(self):
        pass

    @pyqtSlot()
    def slot_help(self):
        pass

    @pyqtSlot()
    def slot_about(self):
        pass

    def set_all_text(self):
        self.menu_file.setTitle(self.tr("File") + "(&F)")
        self.act_new_file.setText(self.tr('New') + "(&N)")
        self.act_open_file.setText(self.tr('Open...') + "(&O)")
        self.act_save_file.setText(self.tr('Save') + "(&S)")
        self.act_save_as_file.setText(self.tr('Save as...') + "(&A)")
        self.act_page_setup.setText(self.tr('Page Setup...') + "(&U)")
        self.act_print.setText(self.tr('Print...') + "(&P)")

        self.menu_edit.setTitle(self.tr('Edit') + "(&E)")
        self.act_undo.setText(self.tr('Undo'))
        self.act_cut.setText(self.tr('Cut'))
        self.act_copy.setText(self.tr('Copy'))
        self.act_paste.setText(self.tr('Paste'))
        self.act_del.setText(self.tr('Del'))
        self.act_find.setText(self.tr('Find...'))
        self.act_find_next.setText(self.tr('Find Next'))
        self.act_replace.setText(self.tr('Replace...'))
        self.act_go_to.setText(self.tr('Go To...'))
        self.act_select_all.setText(self.tr('Select All'))
        self.act_time_date.setText(self.tr('Time/Date'))

        self.menu_format.setTitle(self.tr('Format') + "(&O)")
        self.act_word_wrap.setText(self.tr('Word Wrap'))
        self.act_font.setText(self.tr('Font...'))

        self.menu_view.setTitle(self.tr('View') + "(&V)")
        self.act_status_bar.setText(self.tr('Status Bar'))

        self.menu_help.setTitle(self.tr('Help') + "(&H)")
        self.act_help.setText(self.tr('Help'))
        self.act_about.setText(self.tr('About'))

    def retranslate_ui(self):
        self.set_all_text()









    def windowMenubar(self):
        self.fileMenu()
        self.editMenu()
        self.formatMenu()
        self.viewMenu()
        self.helpMenu()

    def fileMenu(self):
        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File(F)')
        newaction = QAction('&New(N)', self)
        newaction.setShortcut('Ctrl+N')
        newaction.setStatusTip('New')
        newaction.triggered.connect(self.newAction)
        filemenu.addAction(newaction)
        openaction = QAction('&Open(O)', self)
        openaction.setShortcut('Ctrl+O')
        openaction.setStatusTip('Open')
        openaction.triggered.connect(self.openAction)
        filemenu.addAction(openaction)
        newwindowaction = QAction('New &Window(W)', self)
        newwindowaction.setShortcut('Ctrl+W')
        newwindowaction.setStatusTip('New Window')
        newwindowaction.triggered.connect(self.newwindowAction)
        filemenu.addAction(newwindowaction)
        saveaction = QAction('&Save(S)', self)
        saveaction.setShortcut('Ctrl+S')
        saveaction.setStatusTip('Save')
        saveaction.triggered.connect(self.saveAction)
        filemenu.addAction(saveaction)
        saveasaction = QAction('Save &As(A)', self)
        saveasaction.setShortcut('Ctrl+Shift+A')
        saveasaction.setStatusTip('Save As')
        saveasaction.triggered.connect(self.saveAction)
        filemenu.addAction(saveasaction)
        printaction = QAction('&Print(P)', self)
        printaction.setShortcut('Ctrl+P')
        printaction.setStatusTip('Print')
        printaction.triggered.connect(qApp.exit)
        filemenu.addAction(printaction)
        importmenu = QMenu('&Import/Export(I)', self)
        importaction = QAction('&Import(I)', self)
        importaction.setShortcut('Ctrl+Shift+I')
        importaction.setStatusTip('Import')
        importaction.triggered.connect(qApp.exit)
        exportaction = QAction('&Export(E)', self)
        exportaction.setShortcut('Ctrl+Shift+E')
        exportaction.setStatusTip('Export')
        exportaction.triggered.connect(qApp.exit)
        importmenu.addAction(importaction)
        importmenu.addAction(exportaction)
        filemenu.addMenu(importmenu)
        exitaction = QAction('&Exit(E)', self)
        exitaction.setShortcut('Ctrl+E')
        exitaction.setStatusTip('Exit')
        exitaction.triggered.connect(self.closeEvent)
        filemenu.addAction(exitaction)

    def newAction(self):
        self.textedit.setText("")
        with open('./1.MEMOPAD/untitled.txt', 'w') as f:
                texteditcontent = self.textedit.toPlainText()
                f.write(texteditcontent)

    def openAction(self):
        self.openfile = QFileDialog.getOpenFileName(self, 'Open File', './1.MEMOPAD/')
        if self.openfile[0]:
            with open(self.openfile[0], 'r') as f:
                texteditcontent = f.read()
                self.textedit.setText(texteditcontent)
        else:
            pass

    def newwindowAction(self):
        self.dialog = MemoPad()
        self.dialog.setWindowTitle('New Window')
        self.dialog.setWindowIcon(QIcon('./1.MEMOPAD/icon/Title.png'))
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.setGeometry(300, 300, 600, 600)
        self.dialog.show()

    def saveAction(self):
        savefile = QFileDialog.getSaveFileName(self, 'Save File', './1.MEMOPAD/')
        if savefile[0]:
            with open(savefile[0], 'w') as f:
                texteditcontent = self.textedit.toPlainText()
                f.write(texteditcontent)
        else:
            pass

    def printAction(self):
        printer = QPrinter()
        printdialog = QPrintDialog(printer, self)
        if printdialog.exec() == QDialog.Accepted:
            painter = QPainter()
            painter.begin(printer)
            # 여백 조정 및 중앙으로 출력하기
            wgap = printer.pageRect().width()*0.2
            hgap = printer.pageRect().height()*0.2
            xscale = (printer.pageRect().width()-wgap)/self.textedit.width()
            yscale = (printer.pageRect().height()-hgap)/self.textedit.height()
            scale = xscale if xscale < yscale else yscale        
            painter.translate(printer.paperRect().x() + printer.pageRect().width()/2, printer.paperRect().y() + printer.pageRect().height()/2)
            painter.scale(scale, scale);
            painter.translate(-self.textedit.width()/2, -self.textedit.height()/2);  
            self.textedit.render(painter)
            painter.end()
        else:
            pass

    def editMenu(self):
        menubar = self.menuBar()
        editmenu = menubar.addMenu('&Edit(E)')
        undoaction = QAction('&Undo(U)', self)
        undoaction.setShortcut('Ctrl+Z')
        undoaction.setStatusTip('Undo')
        undoaction.triggered.connect(qApp.exit)
        editmenu.addAction(undoaction)
        redoaction = QAction('&Redo(R)', self)
        redoaction.setShortcut('Ctrl+R')
        redoaction.setStatusTip('Redo')
        redoaction.triggered.connect(qApp.exit)
        editmenu.addAction(redoaction)
        cutaction = QAction('Cu&t(T)', self)
        cutaction.setShortcut('Ctrl+X')
        cutaction.setStatusTip('Cut')
        cutaction.triggered.connect(qApp.exit)
        editmenu.addAction(cutaction)
        copyaction = QAction('&Copy(C)', self)
        copyaction.setShortcut('Ctrl+C')
        copyaction.setStatusTip('Copy')
        copyaction.triggered.connect(qApp.exit)
        editmenu.addAction(copyaction)
        pasteaction = QAction('&Paste(P)', self)
        pasteaction.setShortcut('Ctrl+V')
        pasteaction.setStatusTip('Paste')
        pasteaction.triggered.connect(qApp.exit)
        editmenu.addAction(pasteaction)
        deleteaction = QAction('De&lete(L)', self)
        deleteaction.setShortcut('Del')
        deleteaction.setStatusTip('Delete')
        deleteaction.triggered.connect(qApp.exit)
        editmenu.addAction(deleteaction)
        findaction = QAction('&Find(F)', self)
        findaction.setShortcut('Ctrl+F')
        findaction.setStatusTip('Find')
        findaction.triggered.connect(qApp.exit)
        editmenu.addAction(findaction)
        replaceaction = QAction('R&eplace(E)', self)
        replaceaction.setShortcut('Ctrl+H')
        replaceaction.setStatusTip('Replace')
        replaceaction.triggered.connect(qApp.exit)
        editmenu.addAction(replaceaction)
        moveaction = QAction('&Move(M)', self)
        moveaction.setShortcut('Ctrl+M')
        moveaction.setStatusTip('Move')
        moveaction.triggered.connect(qApp.exit)
        editmenu.addAction(moveaction)

    def formatMenu(self):
        menubar = self.menuBar()
        formatmenu = menubar.addMenu('F&ormat(O)')
        fontaction = QAction('&Font(F)', self)
        fontaction.setShortcut('Ctrl+Shift+F')
        fontaction.setStatusTip('Font')
        fontaction.triggered.connect(self.fontAction)
        formatmenu.addAction(fontaction)
        colormenu = QMenu('&Color(C)', self)
        fontcoloraction = QAction('&Font Color(F)', self)
        fontcoloraction.setShortcut('Ctrl+Shift+C')
        fontcoloraction.setStatusTip('Font Color')
        fontcoloraction.triggered.connect(self.fontcolorAction)
        backgroundcoloraction = QAction('&Background Color(B)', self)
        backgroundcoloraction.setShortcut('Ctrl+Shift+B')
        backgroundcoloraction.setStatusTip('Background Color')
        backgroundcoloraction.triggered.connect(self.backgroundcolorAction)
        colormenu.addAction(fontcoloraction)
        colormenu.addAction(backgroundcoloraction)
        formatmenu.addMenu(colormenu)

    def fontAction(self):
        fontdialog, ok = QFontDialog.getFont()
        if ok:
           self.textedit.setFont(fontdialog)
        else:
            pass

    def fontcolorAction(self):
        fontcolordialog = QColorDialog.getColor()
        if fontcolordialog.isValid():
            self.textedit.setStyleSheet('color:{};'.format(fontcolordialog.name()))
        else:
            pass

    def backgroundcolorAction(self):
        backgroundcolordialog = QColorDialog.getColor()
        if backgroundcolordialog.isValid():
            self.textedit.setStyleSheet('background-color:{};'.format(backgroundcolordialog.name()))
        else:
            pass

    def viewMenu(self):
        menubar = self.menuBar()
        formatmenu = menubar.addMenu('&View(V)')
        zoominoutmenu = QMenu('&Zoon In/Zoon Out(Z)', self)
        zoominaction = QAction('Zoom &In(I)', self)
        zoominaction.setShortcut('Ctrl++')
        zoominaction.setStatusTip('Zoom In')
        zoominaction.triggered.connect(qApp.exit)
        zoomoutaction = QAction('Zoom &Out(O)', self)
        zoomoutaction.setShortcut('Ctrl+-')
        zoomoutaction.setStatusTip('Zomm Out')
        zoomoutaction.triggered.connect(qApp.exit)
        zoominoutmenu.addAction(zoominaction)
        zoominoutmenu.addAction(zoomoutaction)
        formatmenu.addMenu(zoominoutmenu)

    def helpMenu(self):
        menubar = self.menuBar()
        helpmenu = menubar.addMenu('&Help(H)')
        helpaction = QAction('&Help(H)', self)
        helpaction.setShortcut('F1')
        helpaction.setStatusTip('Help')
        helpaction.triggered.connect(qApp.exit)
        helpmenu.addAction(helpaction)
        versionaction = QAction('&Version(V)', self)
        versionaction.setShortcut('Ctrl+Shift+V')
        versionaction.setStatusTip('Version')
        versionaction.triggered.connect(qApp.exit)
        helpmenu.addAction(versionaction)






















class StatusBar(QStatusBar):
    self.date = QDate.currentDate()
    self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
    @pyqtSlot(QTextCursor)
    def __init__(self):
        QStatusBar.__init__(self)
        self.setVisible(False)

    def change_cursor_info(self, data:QTextCursor):
        ss = data.selectionStart()
        se = data.selectionEnd()
        selected_info = ""
        if se - ss:
            selected_info = "{0}{1} 선택됨.".format(se - ss, "문자" if (se-ss) == 1 else "문자열")
        self.showMessage("{0} {1}행:{2}열".format(selected_info, data.blockNumber()+1, data.columnNumber()))


def main():
    app = QApplication(sys.argv)
    memopad = MemoPad()
    memopad.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
