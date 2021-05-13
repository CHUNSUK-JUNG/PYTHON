import inspect, os, random, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class MemoPad(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUi()

    def initUi(self):
        self.windowInit()
        self.windowCenter()
        self.textEdit()
        self.windowMenubar()
        self.windowToolbar()
        self.windowStatusbar()

    def windowInit(self):
        self.setWindowTitle('Memo Pad')  # 열려져 있는 파일 이름 표기방법 추가
        self.setWindowIcon(QIcon('./1.MEMOPAD/Window.png'))
        self.setGeometry(300, 300, 600, 600)

    def windowCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def textEdit(self):
        self.textedit = QTextEdit()
        self.textedit.setStyleSheet('border-style : solid;' 'border-width : 2px;'
                                    'border-color : black;' 'border-radius : 5px')
        self.setCentralWidget(self.textedit)

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
        self.dialog.setWindowIcon(QIcon('./1.MEMOPAD/Window.png'))
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

    def windowToolbar(self):
        self.fileToolbar()
        self.formatToolbar()

    def fileToolbar(self):
        self.toolbar = self.addToolBar('File')
        newaction = QAction(QIcon('./1.MEMOPAD/New.png'), 'New', self)
        newaction.setStatusTip('New')
        newaction.triggered.connect(self.newAction)
        self.toolbar.addAction(newaction)
        openaction = QAction(QIcon('./1.MEMOPAD/Open.png'), 'Open', self)
        openaction.setStatusTip('Open')
        openaction.triggered.connect(self.openAction)
        self.toolbar.addAction(openaction)
        saveaction = QAction(QIcon('./1.MEMOPAD/Save.png'), 'Save', self)
        saveaction.setStatusTip('Save')
        saveaction.triggered.connect(self.saveAction)
        self.toolbar.addAction(saveaction)
        printaction = QAction(QIcon('./1.MEMOPAD/Print.png'), 'Print', self)
        printaction.setStatusTip('Print')
        printaction.triggered.connect(self.printAction)
        self.toolbar.addAction(printaction)
        exitaction = QAction(QIcon('./1.MEMOPAD/Exit.png'), 'Exit', self)
        exitaction.setStatusTip('Exit')
        exitaction.triggered.connect(qApp.exit)
        self.toolbar.addAction(exitaction)

    def formatToolbar(self):
        self.toolbar = self.addToolBar('Format')
        fontaction = QAction(QIcon('./1.MEMOPAD/Font.png'), 'Font', self)
        fontaction.setStatusTip('Font')
        fontaction.triggered.connect(self.fontAction)
        self.toolbar.addAction(fontaction)
        fontcoloraction = QAction(QIcon('./1.MEMOPAD/FontColor.png'), 'Font Color', self)
        fontcoloraction.setStatusTip('Color')
        fontcoloraction.triggered.connect(self.fontcolorAction)
        self.toolbar.addAction(fontcoloraction)
        backgroundcoloraction = QAction(QIcon('./1.MEMOPAD/BackgroundColor.png'), 'Background Color', self)
        backgroundcoloraction.setStatusTip('Background Color')
        backgroundcoloraction.triggered.connect(self.backgroundcolorAction)
        self.toolbar.addAction(backgroundcoloraction)

    def windowStatusbar(self):
        self.date = QDate.currentDate()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    memopad = MemoPad()
    memopad.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
