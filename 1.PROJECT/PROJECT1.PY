import sys #1
from PyQt5.QtWidgets import * 
# QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QComboBox #2
from PyQt5.QtGui import *
# QIcon, QFont
from PyQt5.QtCore import *
# QCoreApplication, QDate, Qt
class MyApp(QMainWindow):
    def __init__(self): #3
        super().__init__() 
        self.date = QDate.currentDate()
        self.initUI()
    def initUI(self):
        # 윈도우 창의 제목 만들기
        self.setWindowTitle('PROJECT') #4
        # 윈도우 창 제목에 아이콘 넣기
        self.setWindowIcon(QIcon('WindowIcon.png')) #5
        # 윈도우 창의 시작 위치 및 크기 지정
        self.setGeometry(300, 300, 400, 400) #6 - self.move(300, 300)와 self.resize(400, 400)를 합쳐 놓은 의미임

        # 메뉴바 만들기
        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        exitAction = QAction(QIcon('exit.png'), '&Exit', self) #아이콘, 제목 및 단축키
        exitAction.setShortcut('Ctrl+Q') #단축키
        exitAction.setStatusTip('Exit') #상태바에 나타낼 내용
        exitAction.triggered.connect(qApp.quit)
        filemenu.addAction(exitAction)
        importmenu = QMenu('Import', self)
        importact = QAction('Import mail', self)
        exportact = QAction('Export mail', self)
        importmenu.addAction(importact)
        importmenu.addAction(exportact)
        filemenu.addMenu(importmenu)

        filemenu = menubar.addMenu('&Edit')
        editAction = QAction(QIcon('edit.png'), '&Edit', self) #아이콘, 제목 및 단축키
        editAction.setShortcut('Ctrl+E') #단축키
        editAction.setStatusTip('Edit') #상태바에 나타낼 내용
        filemenu.addAction(editAction)
        
        filemenu = menubar.addMenu('&Option')
        printAction = QAction(QIcon('print.png'), '&Print', self) #아이콘, 제목 및 단축키
        printAction.setShortcut('Ctrl+P') #단축키
        printAction.setStatusTip('Print') #상태바에 나타낼 내용
        filemenu.addAction(printAction)
      
        filemenu = menubar.addMenu('&Help')
        helpAction = QAction(QIcon('print.png'), '&Help', self) #아이콘, 제목 및 단축키
        helpAction.setShortcut('Ctrl+H') #단축키
        helpAction.setStatusTip('Help') #상태바에 나타낼 내용
        filemenu.addAction(helpAction)

        # 툴바 만들기
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(editAction)
        self.toolbar.addAction(printAction)
        self.toolbar.addAction(helpAction)
        
        # 상태바 만들기
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) # self.statusBar().showMessage('Ready')

        # 버튼 만들기
        quitbtn = QPushButton('Quit', self) #6
        QToolTip.setFont(QFont('SansSerif', 10))
        quitbtn.setToolTip('<b>QuitButton</b>')
        quitbtn.move(350, 100)
        quitbtn.resize(50, 20) #quitbtn.resize(quitbtn.sizeHint())
        ex1 = Calculator()
        quitbtn.clicked.connect(Calculator) #7

        # 화면을 중앙에 위치 시키기
        self.center()
        # 화면에 보여주기
        self.show() #7
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 닫힘 이벤트
    def closeEvent(self, event):    
        reply = QMessageBox.question(self, '닫힘', "진짜 닫을 거임?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    

class Calculator(QWidget): 
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()



def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    ex1 = Calculator()
    sys.exit(app.exec_())

if __name__ == '__main__': #8
    main()