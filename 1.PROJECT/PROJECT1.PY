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
        # 메뉴바에 Exit 메뉴 추가   
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # 메뉴바 만들기
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        # 툴바 만들기
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        # 상태바 만들기
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) # self.statusBar().showMessage('Ready')

        # tab1 = QWidget()
        # tab2 = QWidget()
        # tabs = QTabWidget()
        # tabs.addTab(tab1, 'Tab1')
        # tabs.addTab(tab2, 'Tab2')
        # vbox = QVBoxLayout()
        # vbox.addWidget(tabs)
        # self.setLayout(vbox)


        # 프로그레스바
    #     self.pbar = QProgressBar(self)
    #     self.pbar.setGeometry(30, 40, 200, 25)
    #     self.btn = QPushButton('Start', self)
    #     self.btn.move(40, 80)
    #     self.btn.clicked.connect(self.doAction)
    #     self.timer = QBasicTimer()
    #     self.step = 0
    # def timerEvent(self, e):
    #     if self.step >= 100:
    #         self.timer.stop()
    #         self.btn.setText('Finished')
    #         return
    #     self.step = self.step + 1
    #     self.pbar.setValue(self.step)
    # def doAction(self):
    #     if self.timer.isActive():
    #         self.timer.stop()
    #         self.btn.setText('Start')
    #     else:
    #         self.timer.start(100, self)
    #         self.btn.setText('Stop')

    #     슬라이드바
    #     self.slider = QSlider(Qt.Horizontal, self)
    #     self.slider.move(30, 30)
    #     self.slider.setRange(0, 50)
    #     self.slider.setSingleStep(2)
    #     self.dial = QDial(self)
    #     self.dial.move(30, 50)
    #     self.dial.setRange(0, 50)
    #     btn = QPushButton('Default', self)
    #     btn.move(35, 160)
    #     self.slider.valueChanged.connect(self.dial.setValue)
    #     self.dial.valueChanged.connect(self.slider.setValue)
    #     btn.clicked.connect(self.button_clicked)
    #     self.setWindowTitle('QSlider and QDial')
    #     self.setGeometry(300, 300, 400, 200)
    #     self.show()
    # def button_clicked(self):
    #     self.slider.setValue(0)
    #     self.dial.setValue(0)

        # label1 = QLabel('First Label', self)
        # label1.setAlignment(Qt.AlignCenter)
        # label2 = QLabel('Second Label', self)
        # label2.setAlignment(Qt.AlignVCenter)
        # font1 = label1.font()
        # font1.setPointSize(20)
        # font2 = label2.font()
        # font2.setFamily('Times New Roman')
        # font2.setBold(True)
        # label1.setFont(font1)
        # label2.setFont(font2)
        # layout = QVBoxLayout()
        # layout.addWidget(label1)
        # layout.addWidget(label2)
        # self.setLayout(layout)

        # 체크박스
    #     cb = QCheckBox('Show title', self)
    #     cb.move(20, 20)
    #     cb.toggle()
    #     cb.stateChanged.connect(self.changeTitle)
    # def changeTitle(self, state):
    #     if state == Qt.Checked:
    #         self.setWindowTitle('QCheckBox')
    #     else:
    #         self.setWindowTitle(' ')

        # hbox = QHBoxLayout()
        # top = QFrame()
        # top.setFrameShape(QFrame.Box)
        # midleft = QFrame()
        # midleft.setFrameShape(QFrame.StyledPanel)
        # midright = QFrame()
        # midright.setFrameShape(QFrame.Panel)
        # bottom = QFrame()
        # bottom.setFrameShape(QFrame.WinPanel)
        # bottom.setFrameShadow(QFrame.Sunken)
        # splitter1 = QSplitter(Qt.Horizontal)
        # splitter1.addWidget(midleft)
        # splitter1.addWidget(midright)
        # splitter2 = QSplitter(Qt.Vertical)
        # splitter2.addWidget(top)
        # splitter2.addWidget(splitter1)
        # splitter2.addWidget(bottom)
        # hbox.addWidget(splitter2)
        # self.setLayout(hbox)



        # btn1 = QPushButton('&Button1', self)
        # btn1.setCheckable(True)
        # btn1.toggle()
        # btn2 = QPushButton(self)
        # btn2.setText('Button&2')
        # btn3 = QPushButton('Button3', self)
        # btn3.setEnabled(False)
        # vbox = QVBoxLayout()
        # vbox.addWidget(btn1)
        # vbox.addWidget(btn2)
        # vbox.addWidget(btn3)
        # self.setLayout(vbox)

        # 그리드 레이아웃
        # grid = QGridLayout()
        # self.setLayout(grid)
        # grid.addWidget(QLabel('Title:'), 0, 0)
        # grid.addWidget(QLabel('Author:'), 1, 0)
        # grid.addWidget(QLabel('Review:'), 2, 0)
        # grid.addWidget(QLineEdit(), 0, 1)
        # grid.addWidget(QLineEdit(), 1, 1)
        # grid.addWidget(QTextEdit(), 2, 1)

        # 레이블 및 버튼 만들기
        # label1 = QLabel('입력하기', self)
        # label1.move(100, 100)
        # label2 = QLabel('출력하기', self)
        # label2.move(100, 150)
        # btn1 = QPushButton('입력', self)
        # btn1.move(150, 100)
        # btn2 = QPushButton('출력', self)
        # btn2.move(150, 150)

        # 버튼
        # okButton = QPushButton('OK')
        # cancelButton = QPushButton('Cancel')
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)
        # hbox.addStretch(1)
        # vbox = QVBoxLayout()
        # vbox.addStretch(3)
        # vbox.addLayout(hbox)
        # vbox.addStretch(1)
        # self.setLayout(vbox)

        # 레이블
        # lbl_red = QLabel('Red')
        # lbl_red.setStyleSheet("color: red;"
        #                      "border-style: solid;"
        #                      "border-width: 2px;"
        #                      "border-color: #FA8072;"
        #                      "border-radius: 3px")
        # lbl_green = QLabel('Green')
        # lbl_green.setStyleSheet("color: green;"
        #                        "background-color: #7FFFD4")
        # lbl_blue = QLabel('Blue')
        # lbl_blue.setStyleSheet("color: blue;"
        #                       "background-color: #87CEFA;"
        #                       "border-style: dashed;"
        #                       "border-width: 3px;"
        #                       "border-color: #1E90FF")
        # vbox = QVBoxLayout()
        # vbox.addWidget(lbl_red)
        # vbox.addWidget(lbl_green)
        # vbox.addWidget(lbl_blue)
        # self.setLayout(vbox)

        # 버튼 만들기
        # quitbtn = QPushButton('Quit', self) #6
        # QToolTip.setFont(QFont('SansSerif', 10))
        # quitbtn.setToolTip('<b>QuitButton</b>')
        # quitbtn.move(350, 0)
        # quitbtn.resize(50, 20) #quitbtn.resize(quitbtn.sizeHint())
        # quitbtn.clicked.connect(QCoreApplication.instance().quit) #7
        
        # 라이오버튼
        # rbtn1 = QRadioButton('First Button', self)
        # rbtn1.move(50, 50)
        # rbtn1.setChecked(True)
        # rbtn2 = QRadioButton(self)
        # rbtn2.move(50, 70)
        # rbtn2.setText('Second Button')

    #     self.lbl = QLabel('Option1', self)
    #     self.lbl.move(50, 150)
    #     cb = QComboBox(self)
    #     cb.addItem('Option1')
    #     cb.addItem('Option2')
    #     cb.addItem('Option3')
    #     cb.addItem('Option4')
    #     cb.move(50, 50)
    #     cb.activated[str].connect(self.onActivated)
    # def onActivated(self, text):
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()


    #     self.lbl = QLabel(self)
    #     self.lbl.move(60, 40)
    #     qle = QLineEdit(self)
    #     qle.move(60, 100)
    #     qle.textChanged[str].connect(self.onChanged)
    # def onChanged(self, text):
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()

        # 화면을 중앙에 위치 시키기
        self.center()
        # 화면에 보여주기
        self.show() #7
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__': #8
   app = QApplication(sys.argv) #9
   # MyApp 객체를 생성한다.
   ex = MyApp()
   # 화면을 지속적으로 띄워준다
   sys.exit(app.exec_()) #10