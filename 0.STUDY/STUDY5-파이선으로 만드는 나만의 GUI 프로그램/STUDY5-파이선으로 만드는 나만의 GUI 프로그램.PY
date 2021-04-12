# 출처 [https://wikidocs.net/book/2165, PyQt5 Tutorial 파이썬으로 만드는 나만의 GUI 프로그램]


# [기초 (Basics)]

# (3-9.날짜와 시간 표시하기)
# QtCore 모듈의 QDate, QTime, QDateTime 클래스를 이용해서 어플리케이션에 날짜와 시간을 표시할 수 있습니다.
# 각 클래스에 대한 자세한 설명은 아래 링크를 참고합니다.
# QDate 공식 문서: 링크
# QTime 공식 문서: 링크
# QDateTime 공식 문서: 링크
# 날짜 표시하기(QDate)
# QDate 클래스는 날짜와 관련된 기능들을 제공합니다.
# 현재 날짜 출력하기
# 우선 QDate 클래스를 이용해서 날짜를 출력해 보겠습니다.
# from PyQt5.QtCore import QDate
# now = QDate.currentDate()
# print(now.toString())
# currentDate() 메서드는 현재 날짜를 반환합니다.
# toString() 메서드를 통해 현재 날짜를 문자열로 출력할 수 있습니다.
# 결과는 아래와 같습니다.
# 수 1 2 2019
# 날짜 형식 설정하기
# toString() 메서드의 format 파라미터를 설정함으로써 날짜의 형식을 정할 수 있습니다.
# from PyQt5.QtCore import QDate, Qt
# now = QDate.currentDate()
# print(now.toString('d.M.yy'))
# print(now.toString('dd.MM.yyyy'))
# print(now.toString('ddd.MMMM.yyyy'))
# print(now.toString(Qt.ISODate))
# print(now.toString(Qt.DefaultLocaleLongDate))
# 'd'는 일(day), 'M'은 달(month), 'y'는 연도(year)를 나타냅니다. 각 문자의 개수에 따라 날짜의 형식이 다르게 출력됩니다.
# Qt.ISODate, Qt.DefaultLocaleLongDate를 입력함으로써 ISO 표준 형식 또는 어플리케이션의 기본 설정에 맞게 출력할 수 있습니다. 결과는 아래와 같습니다.
# 2.1.19
# 02.01.2019
# 수.1월.2019
# 2019-01-02
# 2019년 1월 2일 수요일
# 자세한 내용은 아래의 표 또는 공식 문서를 참고합니다.
# 시간 표시하기(QTime)
# QTime 클래스를 사용해서 현재 시간을 출력할 수 있습니다.
# 현재 시간 출력하기
# from PyQt5.QtCore import QTime
# time = QTime.currentTime()
# print(time.toString())
# currentTime() 메서드는 현재 시간을 반환합니다.
# toString() 메서드는 현재 시간을 문자열로 반환합니다. 결과는 아래와 같습니다.
# 15:41:22
# 시간 형식 설정하기
# from PyQt5.QtCore import QTime, Qt
# time = QTime.currentTime()
# print(time.toString('h.m.s'))
# print(time.toString('hh.mm.ss'))
# print(time.toString('hh.mm.ss.zzz'))
# print(time.toString(Qt.DefaultLocaleLongDate))
# print(time.toString(Qt.DefaultLocaleShortDate))
# 'h'는 시간(hour), 'm'은 분(minute), 's'는 초(second), 그리고 'z'는 1000분의 1초를 나타냅니다.
# 또한 날짜에서와 마찬가지로 Qt.DefaultLocaleLongDate 또는 Qt.DefaultLocaleShortDate 등으로 시간의 형식을 설정할 수 있습니다.
# 결과는 아래와 같습니다.
# 16.2.3
# 16.02.03
# 16.02.03.610
# 오후 4:02:03
# 오후 4:02
# 자세한 내용은 아래의 표 또는 공식 문서를 참고합니다.
# 날짜와 시간 표시하기(QDateTime)
# QDateTime 클래스를 사용해서 현재 날짜와 시간을 함께 출력할 수 있습니다.
# 현재 날짜와 시간 출력하기
# from PyQt5.QtCore import QDateTime
# datetime = QDateTime.currentDateTime()
# print(datetime.toString())
# currentDateTime() 메서드는 현재의 날짜와 시간을 반환합니다.
# toString() 메서드는 날짜와 시간을 문자열 형태로 반환합니다.
# 날짜와 시간 형식 설정하기
# from PyQt5.QtCore import QDateTime, Qt
# datetime = QDateTime.currentDateTime()
# print(datetime.toString('d.M.yy hh:mm:ss'))
# print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
# print(datetime.toString(Qt.DefaultLocaleLongDate))
# print(datetime.toString(Qt.DefaultLocaleShortDate))
# 위의 예제에서와 마찬가지로 날짜에 대해 'd', 'M', 'y', 시간에 대해 'h', 'm', 's' 등을 사용해서 날짜와 시간이 표시되는 형식을 설정할 수 있습니다.
# 또한 Qt.DefaultLocaleLongDate 또는 Qt.DefaultLocaleShortDate를 입력할 수 있습니다.
# 상태표시줄에 날짜 표시하기
# 상태표시줄에 오늘의 날짜를 출력해보겠습니다.
# currentDate() 메서드를 통해 현재 날짜를 얻고 showMessage() 메서드로 상태표시줄에 현재 날짜를 표시했습니다.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# (3-8.창을 화면의 가운데로)
# 창이 화면의 정가운데에 띄워집니다.
# self.center()
# center() 메서드를 통해서 창이 화면의 가운데에 위치하게 됩니다.
# qr = self.frameGeometry()
# frameGeometry() 메서드를 이용해서 창의 위치와 크기 정보를 가져옵니다.
# cp = QDesktopWidget().availableGeometry().center()
# 사용하는 모니터 화면의 가운데 위치를 파악합니다.
# qr.moveCenter(cp)
# 창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
# self.move(qr.topLeft())
# 현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.
# 결과적으로 현재 창의 중심이 화면의 중심과 일치하게 돼서 창이 가운데에 나타나게 됩니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center()
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (3-7.툴바 만들기)
# 메뉴(menu)가 어플리케이션에서 사용되는 모든 명령의 모음이라면, 툴바(toolbar)는 자주 사용하는 명령들을 더 편리하게 사용할 수 있도록 해줍니다.
# (QToolBar 공식 문서 참고)
# 폴더 안에 툴바의 각 기능에 해당하는 아이콘들을 저장해 둡니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAction = QAction(QIcon('C:\\Users\\PROCESSOR\\Desktop\\EXE\\PYTHON\\0.STUDY\\STUDY5-파이선으로 만드는 나만의 GUI 프로그램\\ICON\\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (3-6.메뉴바 만들기)
# GUI 어플리케이션에서 메뉴바(menu bar)는 흔하게 사용됩니다.
# 다양한 명령들의 모음이 메뉴바에 위치합니다. (QMenuBar 공식 문서 참고)
# macOS에서는 메뉴바를 다르게 다루는데, 아래 예제에서 볼 수 있듯이 한 줄의 코드(menubar.setNativeMenuBar(False))를 추가함으로써 macOS에서도
# Windows 환경과 동일한 결과를 얻을 수 있습니다.
# 우선 폴더 안에 아래와 같이 메뉴에 해당하는 아이콘(exit.png)을 저장해 둡니다.
# 한 개의 메뉴를 갖는 메뉴바를 만들었습니다.
# 이 메뉴는 클릭했을 때 어플리케이션을 종료하는 기능을 갖고 있습니다. 또한 이 기능은 단축키 (Ctrl+Q)로도 실행이 가능합니다.
# exitAction = QAction(QIcon('exit.png'), 'Exit', self)
# exitAction.setShortcut('Ctrl+Q')
# exitAction.setStatusTip('Exit application')
# 이 세 줄의 코드를 통해 아이콘 (exit.png)과 'Exit' 라벨을 갖는 하나의 동작 (action)을 만들고, 이 동작에 대해 단축키 (shortcut)를 정의합니다.
# 또한 메뉴에 마우스를 올렸을 때, 상태바에 나타날 상태팁을 setStatusTip() 메서드를 사용하여 설정했습니다.
# exitAction.triggered.connect(qApp.quit)
# 이 동작을 선택했을 때, 생성된 (triggered) 시그널이 QApplication 위젯의 quit() 메서드에 연결되고, 어플리케이션을 종료시키게 됩니다.
# menubar = self.menuBar()
# menubar.setNativeMenuBar(False)
# fileMenu = menubar.addMenu('&File')
# fileMenu.addAction(exitAction)
# menuBar() 메서드는 메뉴바를 생성합니다. 이어서 'File' 메뉴를 하나 만들고, 거기에 'exitAction' 동작을 추가합니다.
# '&File'의 앰퍼샌드 (ampersand, &)는 간편하게 단축키를 설정하도록 해줍니다.
# 'F' 앞에 앰퍼샌드가 있으므로 'Alt+F'가 File 메뉴의 단축키가 됩니다. 만약 'i'의 앞에 앰퍼샌드를 넣으면 'Alt+I'가 단축키가 됩니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAction = QAction(QIcon('C:\\Users\\PROCESSOR\\Desktop\\EXE\\PYTHON\\0.STUDY\\STUDY5-파이선으로 만드는 나만의 GUI 프로그램\\ICON\\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (3-5.상태바 만들기)
# 메인창(Main window)은 메뉴바, 툴바, 상태바를 갖는 전형적인 어플리케이션 창입니다. (QMainWindow 공식 문서 참고)
# 메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 레이아웃을 갖고 있습니다.
# 또한 가운데 영역(QDockWidget 내)에 중심위젯(Central widget)을 위한 영역을 갖고 있습니다. 여기에는 어떠한 위젯도 들어올 수 있습니다.
# QMainWindow 클래스를 이용해서 메인 어플리케이션 창을 만들 수 있습니다.
# 우선 QStatusBar를 이용해서 메인 창에 상태바(status bar)를 하나 만들어 보겠습니다.
# 상태바는 어플리케이션의 상태를 알려주기 위해 어플리케이션의 하단에 위치하는 위젯입니다. (QStatusBar 공식 문서 참고)
# 상태바에 텍스트를 표시하기 위해서는 showMessage() 메서드를 사용합니다.
# 텍스트가 사라지게 하고 싶으면, clearMessage() 메서드를 사용하거나, showMessage() 메서드에 텍스트가 표시되는 시간을 설정할 수 있습니다.
# 현재 상태바에 표시되는 메세지 텍스트를 갖고 오고 싶을 때는 currentMessage() 메서드를 사용합니다.
# QStatusBar 클래스는 상태바에 표시되는 메세지가 바뀔 때 마다 messageChanged() 시그널을 발생합니다.
# self.statusBar().showMessage('Ready')
# 상태바는 QMainWindow 클래스의 statusBar() 메서드를 이용해서 만드는데, statusBar() 메서드를 최초로 호출함으로써 만들어집니다.
# 그 다음 호출부터는 상태바 객체를 반환합니다.
# showMessage() 메서드를 통해 상태바에 보여질 메세지를 설정할 수 있습니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (3-4.툴팁 나타내기)
# 툴팁은 어떤 위젯의 기능을 설명하는 등의 역할을 하는 말풍선 형태의 도움말입니다. (QToolTip 공식 문서 참고)
# 위젯에 있는 모든 구성 요소에 대해서 툴팁(tooltip)이 나타나도록 할 수 있습니다.
# 이번에는 setToolTip() 메서드를 이용해서 위젯에 툴팁을 만들어 보겠습니다.
# 이 예제에서는 두 개의 PyQt5 위젯에 대한 툴팁을 보여줍니다.
# 푸시버튼(btn)과 창(MyApp) 위젯에 마우스를 올리면 각각 설정한 텍스트가 툴팁으로 나타납니다.
# QToolTip.setFont(QFont('SansSerif', 10))
# self.setToolTip('This is a <b>QWidget</b> widget')
# 먼저 툴팁에 사용될 폰트를 설정합니다. 여기에서는 10px 크기의 'SansSerif' 폰트를 사용합니다.
# 툴팁을 만들기 위해서는 setToolTip() 메서드를 사용해서, 표시될 텍스트를 입력해줍니다.
# btn = QPushButton('Button', self)
# btn.setToolTip('This is a <b>QPushButton</b> widget')
# 푸시버튼을 하나 만들고, 이 버튼에도 툴팁을 달아줍니다.
# btn.move(50, 50)
# btn.resize(btn.sizeHint())
# 버튼의 위치와 크기를 설정합니다.
# sizeHint() 메서드는 버튼을 적절한 크기로 설정하도록 도와줍니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (3-3.창 닫기)
# 창을 닫는 가장 간단한 방법은 타이틀바의 오른쪽 (Windows) 또는 왼쪽 (macOS) 'X' 버튼을 클릭하는 것입니다.
# 이번에는 프로그래밍을 통해 창을 닫는 법을 알아보겠습니다.
# 시그널(Signal)과 슬롯(Slot)에 대해서도 간단하게 다뤄보겠습니다.
# 'Quit' 버튼을 만들었습니다.
# 이제 이 버튼을 클릭하면 어플리케이션이 종료됩니다.
# from PyQt5.QtCore import QCoreApplication
# QtCore 모듈의 QCoreApplication 클래스를 불러옵니다.
# btn = QPushButton('Quit', self)
# 푸시버튼을 하나 만듭니다. 이 버튼(btn)은 QPushButton 클래스의 인스턴스입니다.
# 생성자(QPushButton())의 첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력하고, 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력합니다.
# 푸시버튼 위젯에 대한 자세한 설명은 QPushButton 페이지를 참고하세요.
# btn.clicked.connect(QCoreApplication.instance().quit)
# PyQt5에서의 이벤트 처리는 시그널과 슬롯 메커니즘으로 이루어집니다.
# 버튼(btn)을 클릭하면 'clicked' 시그널이 만들어집니다.
# instance() 메서드는 현재 인스턴스를 반환합니다.
# 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됩니다.
# 이렇게 발신자(Sender)와 수신자 (Receiver), 두 객체 간에 커뮤니케이션이 이루어집니다.
# 이 예제에서 발신자는 푸시버튼(btn)이고, 수신자는 어플리케이션 객체(app)입니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
class MyApp(QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()
  def initUI(self):
      btn = QPushButton('Quit', self)
      btn.move(250, 180)
      btn.resize(50,20) # btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)
      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)
      self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (3-2.어플리케이션 아이콘 넣기)
# self.setWindowIcon(QIcon('web.png'))
# setWindowIcon() 메서드는 어플리케이션 아이콘을 설정하도록 합니다.
# 이를 위해서 QIcon 객체를 생성하였습니다. QIcon()에 보여질 이미지('web.png')를 입력합니다.
# 이미지 파일을 다른 폴더에 따로 저장해 둔 경우에는 경로까지 함께 입력해주면 됩니다.
# self.setGeometry(300, 300, 300, 200)
# setGeometry() 메서드는 창의 위치와 크기를 설정합니다.
# 앞의 두 매개변수는 창의 x, y 위치를 결정하고, 뒤의 두 매개변수는 각각 창의 너비와 높이를 결정합니다.
# 이 메서드는 창 띄우기 예제에서 사용했던 move()와 resize() 메서드를 하나로 합쳐놓은 것과 같습니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class MyApp(QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()
  def initUI(self):
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('C:\\Users\\PROCESSOR\\Desktop\\EXE\\PYTHON\\0.STUDY\\STUDY5-파이선으로 만드는 나만의 GUI 프로그램\\ICON\\web.png'))
      self.setGeometry(300, 300, 300, 200)
      self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (3-1.창 띄우기)
# QApplication
# Qt라이브러리의 기본이 되는 클래스로서, 이곳에 각종 위젯을 채워 넣는다.
# 어플 내에서 반드시 하나만 존재해야 한다. 기본이 되는 클래스이므로, 당연히 가장 먼저 만들어져야 한다.
# 이 클래스는 콘솔에서 입력된 각종 변수를 저장하는데, 이때 쓰이는게 sys.argv이다.
# 따라서 콘솔에서 코드를 직섭 실행하는 경우, 각종 변수를 함께 넣으면 모든 변수가 argv에 저장되고,
# 이게 QApplication의 기본 변수로 쓰이게 된다.
# QWidget()
# 우리가 입력할 각종 마우스, 키보드 입력에 의한 다양한 이벤트 작동에 기본을 담당할 위젯을 생성하는 클래스이다.
# 각종 위젯을 만들수 있으며, 높이 순서대로 정렬된다.(Z-order) 부모 클래스가 존재하는 위젯(Non-window widget:nww)과 그렇지 않은 경우로 나뉘는데,
# 부모가 존재하는 위젯(widget widout aparent:wwp)이란 창 안에 존재하는 작은 위젯들이고 생각하면 된다.
# 부모가 존재하지 않는 위젯 그 자체가 바로 창이 된다.
# self.setWindowTitle('My First Application')
# 윈도우 위젯의 타이틀을 설정한다. 만약 타이틀을 설정하지 않을 경우 setWindowTitle함수가 자동으로 실행되어서, 
# 코드파일이 저장되어 있는 상위 폴더이름이 윈도우 타이틀이 된다.
# move(x1,y1)
# 기준점(창의 왼쪽 위)을 기준으로 지정 좌표로 창을 이동시킨다.여기서는 위젯을 스크린의 x=300px, y=300px의 위치로 이동
# resize(x,y)
# 앞서 만든 부모가 존재하는 위젯(wwp)의 크기를 재조정함. 여기서는 위젯의 크기를 너비 400px, 높이 200px로 조절
# self.show()
# 작성된 어플이케이션을 화면에 출력한다. 이외에도 showFullScreen(), showMaximized() 등이 있다. 특히, showFullScreen()에서 다시 이전으로 화면
# 크기를 되돌리기 위해서는 showNormal()을 선언해야 한다.
# __name__
# 모듈의 이름이 저장되는 변수이며 import로 모듈을 가져왔을 때 모듈의 이름이 들어갑니다.
# 하지만 파이썬 인터프리터로 스크립트 파일을 직접 실행했을 때는 모듈의 이름이 아니라 '__main__'이 들어갑니다.
# 만약 'moduleA.py'라는 코드를 import해서 예제 코드를 수행하면 __name__ 은 'moduleA'가 됩니다.
# 그렇지 않고 코드를 직접 실행한다면 __name__ 은 __main__ 이 됩니다.
# if __name__ == '__main__':
# __name__ 변수의 값이 '__main__'인지 확인하는 코드는 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업입니다. 
# 즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도입니다.
# 따라서 이 한 줄의 코드를 통해 프로그램이 직접 실행되는지 혹은 모듈을 통해 실행되는지를 확인합니다.
# 파이썬은 왜 프로그램의 시작점이 정해져 있지 않나요?
# 파이썬이 처음에 개발 될 당시에는 리눅스/유닉스에서 사용하는 스크립트 언어 기반이었기 때문에 프로그램의 시작점이 따로 정해져 있지 않았습니다. 
# 보통 리눅스/유닉스의 스크립트 파일은 파일 한 개로 이루어진 경우가 많은데, 이 스크립트 파일 자체가 하나의 프로그램이다 보니 시작점이
# 따로 필요하지 않습니다. 하지만 C 언어나 자바같은 언어는 처음 만들어질 때부터 소스 파일을 여러 개 사용했기 때문에 여러 소스 파일의
# 함수들 중에서도 시작 함수(main)를 따로 정해 놓았습니다.
# sys.exit(app.exec_())
# 어플리케이션이 실행되면, 코드는 그 자체로는 일단 임무가 끝나게 된다. 따라서 애써 만들어 놓았던 윈도우가 바로 닫혀버린다. 
# 이것을 방지하기 위해서는, 코드가 실행된 후 무언가를 입력할 때 까지는 가만히 있도록(idle)하는 장치가 필요한데, 이를 Mainloop이라고 한다.
# app.exec_()를 씀으로써 PyQt5의 mainloop를 형성한다.
# 단, 파이선 자체가 함수 중에 이미 exec가 있으므로, PyQt5에서는 exec_로 쓴다. app.exec_()는 int변수 0을 반환한다.
# 여기서 중요한게 sys.exit이다. 이 함수는 파이썬 코드를 종료시키는 기능인데, 변수로 0을 입력하면(즉, sys.exit(0)) 컴퓨터가 이를 프로그램 종료로
# 받아들이고 실행중인 코드를 중단시킨다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300) 
        self.resize(400, 400)
        self.show()
if __name__ == '__main__': 
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_()) '''