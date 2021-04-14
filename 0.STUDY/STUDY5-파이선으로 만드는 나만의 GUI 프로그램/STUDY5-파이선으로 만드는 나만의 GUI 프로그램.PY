# 출처 [https://wikidocs.net/book/2165, PyQt5 Tutorial 파이썬으로 만드는 나만의 GUI 프로그램]


# [9.실행파일 만들기 (PyInstaller)]
# PyInstaller를 이용하면 파이썬과 PyQt5로 제작한 GUI 프로그램을 간단하게 실행파일 (exe)로 만들 수 있습니다. (PyInstaller 홈페이지)
# 실행파일은 파이썬이 설치되어 있지 않은 pc에서도 프로그램을 실행할 수 있도록 해줍니다.
# 1.PyInstaller 설치
#   우선 명령프롬프트에서 아래의 명령어를 통해 PyInstaller 패키지를 설치합니다.
#   pip install pyinstaller
# 2.실행파일 만들기
#   Python 파일이 있는 폴더로 이동한 다음, 아래 명령어를 입력하면 해당 폴더에 실행파일이 만들어집니다.
#   pyinstaller qtextbrowser_advanced.py
# 3.만들어진 폴더에서 dist로 이동해서, 한 번 더 들어가면 아래 그림과 같이 실행파일을 찾을 수 있습니다.
#   더블클릭해서 실행을 해보면 아래 그림과 같이 콘솔창이 함께 출력됩니다.  
#   콘솔창 출력되지 않도록 하기
#   콘솔창이 출력되지 않게 하려면 아래와 같이 명령어에 '-w' 또는 '--windowed'를 추가해줍니다.
#   pyinstaller -w qtextbrowser_advanced.py
#   실행파일 하나만 생성하기 
#   실행파일 하나만 생성하기 위해서는 아래와 같이 명령어에 ‘-F’ 또는 ‘–onefile’을 추가합니다.
#   pyinstaller -w -F qtextbrowser_advanced.py
#   실행파일 생성이 완료되었습니다.
#   다시 dist 폴더로 이동하면 실행파일 하나만 생성된 것을 볼 수 있습니다.
#   이제 PyQt5와 BeautifulSoup을 이용해서 작성한 코드를 실행파일을 이용해서 실행할 수 있습니다.



# [8.그림 그리기 (Painting)]
# PyQt5.QtGui의 QPainter 클래스는 GUI 프로그램에서 필요한 ‘그리기’와 관련한 기능들을 제공합니다.
# 간단한 점, 선에서 다각형, 타원과 같은 여러 도형, 텍스트까지 다양한 방식으로 그릴 수 있습니다.
# 예제를 통해 PyQt5의 다양한 그림 그리기 작업에 대해 다뤄 보겠습니다.

# (8-3.직사각형 그리기 (drawRect))
''' import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawRect')
        self.show()
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()
    # def draw_rect(self, qp):
    #     qp.setBrush(QColor(180, 100, 160))
    #     qp.setPen(QPen(QColor(60, 60, 60), 3))
    #     qp.drawRect(20, 20, 100, 100)
    #     qp.setBrush(QColor(40, 150, 20))
    #     qp.setPen(QPen(Qt.blue, 2))
    #     qp.drawRect(180, 120, 50, 120)
    #     qp.setBrush(Qt.yellow)
    #     qp.setPen(QPen(Qt.red, 5))
    #     qp.drawRect(280, 30, 80, 40)
    def draw_rect(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 10, 100, 60)
        qp.drawText(20, 90, 'Qt.SolidPattern')
        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(150, 10, 100, 60)
        qp.drawText(150, 90, 'Qt.Dense1Pattern')
        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(280, 10, 100, 60)
        qp.drawText(280, 90, 'Qt.Dense2Pattern')
        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 110, 100, 60)
        qp.drawText(20, 190, 'Qt.HorPattern')
        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(150, 110, 100, 60)
        qp.drawText(150, 190, 'Qt.VerPattern')
        brush = QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawRect(280, 110, 100, 60)
        qp.drawText(280, 190, 'Qt.CrossPattern')
        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 210, 100, 60)
        qp.drawText(20, 290, 'Qt.BDiagPattern')
        brush = QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(150, 210, 100, 60)
        qp.drawText(150, 290, 'Qt.FDiagPattern')
        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(280, 210, 100, 60)
        qp.drawText(280, 290, 'Qt.DiagCrossPattern')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (8-2.직선 그리기 (drawLine))
''' import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawLine')
        self.show()
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()
    # def draw_line(self, qp):
    #     qp.setPen(QPen(Qt.blue, 8))
    #     qp.drawLine(30, 230, 200, 50)
    #     qp.setPen(QPen(Qt.green, 12))
    #     qp.drawLine(140, 60, 320, 280)
    #     qp.setPen(QPen(Qt.red, 16))
    #     qp.drawLine(330, 250, 40, 190)
    def draw_line(self, qp):
        qp.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        qp.drawLine(20, 20, 380, 20)
        qp.drawText(30, 40, 'Qt.SolidLine')
        qp.setPen(QPen(Qt.black, 3, Qt.DashLine))
        qp.drawLine(20, 70, 380, 70)
        qp.drawText(30, 90, 'Qt.DashLine')
        qp.setPen(QPen(Qt.black, 3, Qt.DotLine))
        qp.drawLine(20, 120, 380, 120)
        qp.drawText(30, 140, 'Qt.DotLine')
        qp.setPen(QPen(Qt.black, 3, Qt.DashDotLine))
        qp.drawLine(20, 170, 380, 170)
        qp.drawText(30, 190, 'Qt.DashDotLine')
        qp.setPen(QPen(Qt.black, 3, Qt.DashDotDotLine))
        qp.drawLine(20, 220, 380, 220)
        qp.drawText(30, 240, 'Qt.DashDotDotLine')
        pen = QPen(Qt.black, 3, Qt.CustomDashLine)
        pen.setDashPattern([4, 3, 2, 5])
        qp.setPen(pen)
        qp.drawLine(20, 270, 380, 270)
        qp.drawText(30, 290, 'Qt.CustomDashLine')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (8-1.점 그리기 (drawPoint))
# QPainter의 동작은 일반적으로 위젯의 페인트 이벤트 (paint event)를 통해 이루어집니다.
# 아래의 예제에서는 drawPoint() 메서드를 이용해서 위젯에 다양한 방식으로 점을 그려 보겠습니다.
''' import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
import numpy as np
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawPoint')
        self.show()
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()
    def draw_point(self, qp):
        pen = QPen()
        colors = ['#D83C5F', '#3CD88F', '#AA5CE3',
                  '#DF4A26', '#AE85F6', '#F7A82E',
                  '#406CF3', '#E9F229', '#29ACF2']
        for i in range(1000):
            pen.setWidth(np.random.randint(1, 15))
            pen.setColor(QColor(np.random.choice(colors)))
            qp.setPen(pen)
            rand_x = 100 * np.random.randn()
            rand_y = 100 * np.random.randn()
            qp.drawPoint(self.width() / 2 + rand_x, self.height() / 2 + rand_y)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''



# [7.시그널과 슬롯 (Signal & Slot)]
# PyQt에서는 이벤트 처리에 있어서 시그널과 슬롯이라는 독특한 메커니즘을 사용합니다.
# 간단한 예제들을 통해 시그널과 슬롯의 연결에 대해 알아보겠습니다.

# (7-5.사용자 정의 시그널)
# 지정되어 있는 시그널 말고, 새로 원하는 시그널을 만들어서 사용할 수도 있습니다.
# 이번 예제에서는 pyqtSignal()을 이용해서 사용자 정의 시그널을 만들고, 특정 이벤트가 발생했을 때 이 시그널이 방출되도록 해보겠습니다.
# closeApp이라는 시그널을 하나 만들었습니다.
# 이 시그널은 마우스 클릭 시 발생해서 QMainWindow의 close() 슬롯에 연결되어 프로그램을 종료합니다.
# class Communicate(QObject):
#     closeApp = pyqtSignal()
# pyqtSignal()을 가지고 Communicate 클래스의 속성으로서 closeApp이라는 시그널을 하나 만들었습니다.
# self.c = Communicate()
# self.c.closeApp.connect(self.close)
# Communicate 클래스의 closeApp 시그널은 MyApp 클래스의 close() 슬롯에 연결됩니다.
# def mousePressEvent(self, e):
#     self.c.closeApp.emit()
# mousePressEvent 이벤트 핸들러를 사용해서, 마우스를 클릭했을 때 closeApp 시그널이 방출되도록 했습니다.
''' import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow
class Communicate(QObject):
    closeApp = pyqtSignal()
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def mousePressEvent(self, e):
        self.c.closeApp.emit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (7-4.이벤트 핸들러 재구성하기2)
# 이번에는 mouseMoveEvent를 이용해서 마우스의 위치를 트래킹해서 출력해보겠습니다.
# 위젯 안에서 마우스를 움직이면 이벤트가 발생하고, 재구성한 이벤트 핸들러를 통해 마우스의 위치를 출력합니다.
# self.text = 'x: {0}, y: {1}'.format(x, y)
# self.label = QLabel(self.text, self)
# self.label.move(20, 20)
# x, y의 값을 self.text로 저장하고, self.label의 텍스트로 설정합니다.
# 위치를 x=20, y=20 만큼 이동해줍니다.
# self.setMouseTracking(True)
# setMouseTracking을 True로 설정해주면, 마우스의 위치를 트래킹합니다.
# 디폴트는 setMouseTracking(False) 상태이며, 마우스 버튼을 클릭하거나 뗄 때만 mouseEvent가 발생합니다.
# def mouseMoveEvent(self, e):
#     x = e.x()
#     y = e.y()
#     text = 'x: {0}, y: {1}'.format(x, y)
#     self.label.setText(text)
#     self.label.adjustSize()
# 이벤트 e는 이벤트에 대한 정보를 갖고 있는 하나의 객체입니다. 이 이벤트 객체 (event object)는 생성된 이벤트의 유형에 따라 다릅니다.
# e.x(), e.y()는 위젯 안에서 이벤트가 발생했을 때 마우스 커서의 위치를 반환합니다.
# 만약 e.globalX(), e.globalY()로 설정해주면, 화면 전체에서 마우스 커서의 위치를 반환하게 됩니다.
# self.label.adjustSize() 메서드로 라벨의 크기를 자동으로 조절하도록 합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        x = 0
        y = 0
        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)
        self.setMouseTracking(True)
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text)
        self.label.adjustSize()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (7-3.이벤트 핸들러 재구성하기)
# 아래와 같이 자주 쓰이는 이벤트 핸들러는 이미 만들어져 있는 경우가 많습니다.
# 이벤트 핸들러	설명
# keyPressEvent	키보드를 눌렀을 때 동작합니다.
# keyReleaseEvent	키보드를 눌렀다가 뗄 때 동작합니다.
# mouseDoubleClickEvent	마우스를 더블클릭할 때 동작합니다.
# mouseMoveEvent	마우스를 움직일 때 동작합니다.
# mousePressEvent	마우스를 누를 때 동작합니다.
# mouseReleaseEvent	마우스를 눌렀다가 뗄 때 동작합니다.
# moveEvent	위젯이 이동할 때 동작합니다.
# resizeEvent	위젯의 크기를 변경할 때 동작합니다.
# keyPressEvent 이벤트 핸들러를 수정해서, 특정 키를 눌렀을 때 위젯을 종료하거나 최대화, 보통 크기로 조절하는 기능을 구현해보겠습니다.
# 'esc', 'F', 'N' 키를 클릭하면 창이 종료되거나 최대화, 보통 크기가 되도록 이벤트 핸들러를 재구성했습니다.
# def keyPressEvent(self, e):
#     if e.key() == Qt.Key_Escape:
#         self.close()
#     elif e.key() == Qt.Key_F:
#         self.showFullScreen()
#     elif e.key() == Qt.Key_N:
#         self.showNormal()
# keyPressEvent 이벤트 핸들러는 키보드의 이벤트를 입력으로 받습니다.
# e.key()는 어떤 키를 누르거나 뗐는지를 반환합니다.
# 'esc' 키를 눌렀다면, self.close()를 통해 위젯이 종료됩니다.
# 'F' 키 또는 'N' 키를 눌렀다면, 위젯의 크기가 최대화되거나 보통 크기가 됩니다.
''' import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (7-2.이벤트 핸들러 만들기)
# PyQt에서 이벤트(시그널) 처리를 할 때 사용되는 함수를 이벤트 핸들러 (슬롯)라고 합니다.
# 'Big', 'Small' 버튼을 클릭(시그널이 발생)했을 때, 창의 크기가 바뀌도록 하는 함수(슬롯)를 정의해보겠습니다.
# 'Big' 버튼과 'Small' 버튼을 눌러서 창의 크기를 확대, 축소할 수 있습니다.
# btn1.clicked.connect(self.resizeBig)
# btn2.clicked.connect(self.resizeSmall)
# btn1과 btn2는 각각 resizeBig, resizeSmall 슬롯에 연결되어 있습니다.
# def resizeBig(self):
#     self.resize(400, 500)
# def resizeSmall(self):
#     self.resize(200, 250)
# resizeBig() 메서드는 화면 크기를 가로 400px, 세로 500px로 확대, resizeSmall() 메서드는 화면 크기를 가로 200px, 세로 250px로 축소하는 기능을 가지게 됩니다.
''' import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Small', self)
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)
        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()
    def resizeBig(self):
        self.resize(400, 500)
    def resizeSmall(self):
        self.resize(200, 250)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (7-1.연결하기)
# 다이얼 위젯으로 조절한 값을 화면에 출력하는 프로그램을 만들어 보겠습니다.
# 다이얼의 값이 변할 때 발생하는 시그널이 LCD 화면에 숫자를 표시하는 슬롯과 연결됩니다.
# 다이얼을 움직이면 그 값에 맞춰서 LCD에 숫자가 표시됩니다.
# lcd = QLCDNumber(self)
# dial = QDial(self)
# QLCDNumber 위젯은 LCD 화면과 같이 숫자를 표시합니다.
# QDial은 회전해서 값을 조절하는 위젯입니다.
# vbox = QVBoxLayout()
# vbox.addWidget(lcd)
# vbox.addWidget(dial)
# self.setLayout(vbox)
# 수직 박스 레이아웃(박스 레이아웃 참고)을 하나 만들어서 QLCDNumber와 QDial 위젯을 넣어줍니다.
# 그리고 MyApp 위젯의 레이아웃으로 설정합니다.
# dial.valueChanged.connect(lcd.display)
# QDial 위젯은 몇 가지 시그널을 갖고 있습니다(QSlider, QDial 참고).
# 여기서는 valueChanged 시그널을 lcd의 display 슬롯에 연결합니다. display 슬롯은 숫자를 받아서 QLCDNumber 위젯에 표시하는 역할을 합니다.
# 여기서 시그널을 보내는 객체인 송신자 (sender)는 dial, 시그널을 받는 객체인 수신자 (receiver)는 lcd입니다.
# 슬롯 (slot)은 시그널에 어떻게 반응할지를 구현한 메서드입니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)
        dial.valueChanged.connect(lcd.display)
        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''



# [6.다이얼로그 (Dialog)]
# 다이얼로그는 대화창이라고도 부르며 GUI 프로그래밍에서 없어서는 안될 요소입니다. 이름에서 알 수 있듯이 사용자가 어플리케이션 안에서 어플리케이션과 
# '대화'하는데 사용됩니다.
# 다시 말해서 다이얼로그는 사용자가 데이터를 입력, 수정하거나, 어플리케이션의 설정을 변경하는 등의 작업을 하는데 사용됩니다.
# 예제를 통해 다양한 다이얼로그를 사용하는 방법에 대해 알아보겠습니다.

# (6-5.QMessageBox)
# QMessageBox 클래스는 사용자에게 정보를 제공하거나 질문과 대답을 할 수 있는 대화창을 제공합니다.
# 흔히 어떤 동작에 대해 확인이 필요한 경우에 메세지 박스를 사용합니다. (QMessageBox 공식 문서 참고)
# 메세지 박스에서는 사용자에게 상황을 설명하는 기본 텍스트를 표시합니다. 그 다음 정보를 전달하거나 사용자의 의사를 묻는 텍스트를 표시할 수 있습니다.
# 마지막으로 더욱 자세히 상황을 설명하기 위한 세부적인 텍스트를 표시할 수 있습니다.
# 이러한 각각의 텍스트를 표시하기 위해 setText()/setInformativeText()/setDetailedText() 메서드를 사용할 수 있습니다.
# 이제 창을 닫을 때, 이 동작을 한 번 더 확인하기 위한 메세지 박스가 나타나게 됩니다.
# QWidget을 종료할 때, QCloseEvent가 생성되어 위젯에 전달됩니다.
# 위젯의 동작을 수정하기 위해 closeEvent() 이벤트 핸들러를 수정해야합니다.
# reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
#                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
# 두번째 매개변수는 타이틀바에 나타날 문자열 ('Message'), 세번째 매개변수는 대화창에 나타날 문자열 ('Are you sure to quit?')을 입력합니다.
# 네 번째에는 대화창에 보여질 버튼의 종류를 입력하고, 마지막으로 디폴트로 선택될 버튼을 설정해줍니다.
# QMessageBox.No로 설정할 경우, 메세지 박스가 나타났을 때 'No' 버튼이 선택되어 있습니다.
# 반환값은 reply 변수에 저장됩니다.
# if reply == QMessageBox.Yes:
#     event.accept()
# else:
#     event.ignore()
# 'Yes' 버튼을 클릭했을 경우, 이벤트를 받아들이고 위젯을 종료합니다.
# 'No' 버튼을 클릭하면, 이벤트를 무시하고 위젯을 종료하지 않습니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_()) '''

# (6-4.QFileDialog)
# QFileDialog는 사용자가 파일 또는 경로를 선택할 수 있도록 하는 다이얼로그입니다.
# 사용자는 선택한 파일을 열어서 수정하거나 저장할 수 있습니다. (QFileDialog 공식 문서 참고)
# 메뉴바, 텍스트 편집, 상태바 위젯을 배치했습니다. 메뉴에는 파일을 선택하기 위한 'Open' 메뉴가 있습니다.
# 선택한 파일의 내용을 텍스트 편집 위젯으로 불러옵니다.
# fname = QFileDialog.getOpenFileName(self, 'Open file', './')
# QFileDialog를 띄우고, getOpenFileName() 메서드를 사용해서 파일을 선택합니다.
# 세 번째 매개변수를 통해 기본 경로를 설정할 수 있습니다. 또한 기본적으로 모든 파일( * )을 열도록 되어있습니다.
# if fname[0]:
#     f = open(fname[0], 'r')
#     with f:
#         data = f.read()
#         self.textEdit.setText(data)
# 선택한 파일을 읽어서, setText() 메서드를 통해 텍스트 편집 위젯에 불러옵니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (6-3.QFontDialog)
# 폰트 다이얼로그 (QFontDialog)는 폰트를 선택할 수 있게 해주는 다이얼로그입니다. (QFontDialog 공식 문서 참고)
# 시 버튼 하나와 라벨 하나를 만들었습니다.
# QFontDialog를 사용해서, 라벨의 폰트를 바꿀 수 있습니다.
# font, ok = QFontDialog.getFont()
# 폰트 다이얼로그를 띄우고, getFont() 메서드를 사용해서 선택한 폰트와 불 값을 반환받습니다.
# 앞의 예제와 마찬가지로 'OK' 버튼을 클릭하면 True를, 'Cancel' 버튼을 클릭하면 False를 반환합니다.
# if ok:
#     self.lbl.setFont(font)
# setFont() 메서드를 사용해서 선택한 폰트를 라벨의 폰트로 설정해줍니다.
''' import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout
, QPushButton, QSizePolicy, QLabel, QFontDialog)
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)
        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        self.lbl = QLabel('The quick brown fox jumps over the lazy dog', self)
        self.lbl.move(130, 20)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        self.setWindowTitle('Font Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()
    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
           self.lbl.setFont(font)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (6-2.QColorDialog)
# 컬러 다이얼로그 (QColorDialog)는 색상을 선택할 수 있는 다이얼로그입니다. (QColorDialog 공식 문서 참고)
# 우선 푸시 버튼 하나와 QFrame 하나를 만들고, QFrame 위젯의 배경색은 검정색으로 설정했습니다.
# QColorDialog를 사용해서, 배경색을 바꿀 수 있습니다.
# col = QColor(0, 0, 0)
# QColor를 사용해서 배경색인 검정색을 만들었습니다.
# col = QColorDialog.getColor()
# QColorDialog를 띄우고, getColor() 메서드를 통해 색상을 저장합니다.
# if col.isValid():
#     self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
# 색상을 선택하고 'OK' 버튼을 눌렀다면, col.isValid()의 불 값이 True이고, 'Cancel' 버튼을 눌렀다면, 불 값이 False가 됩니다.
# 선택한 색상이 프레임의 배경색으로 설정됩니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        col = QColor(0, 0, 0)
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)
        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130, 35, 100, 100)
        self.setWindowTitle('Color Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()
    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (6-1.QInputDialog)
# 입력 다이얼로그 (QInputDialog)는 사용자가 간단한 값을 입력할 때 사용하는 다이얼로그입니다.
# 입력값은 숫자, 문자열, 리스트에서 선택한 항목 등이 될 수 있습니다. (QInputDialog 공식 문서 참고)
# 입력값의 형태에 따라 아래와 같이 다섯 개의 유용한 함수가 제공됩니다.
# getText()
# getMultiLineText()
# getInt()
# getDouble()
# getItem()
# 예제에서는 getText() 메서드를 사용합니다.
# 푸시 버튼 (QPushButton)과 줄 편집 (QLineEdit) 위젯을 하나씩 만들었습니다.
# 버튼을 누르면 입력 대화창 (input dialog)이 나타나고, 텍스트를 입력받아서 줄 편집 위젯에 표시합니다.
# text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
# 이 코드를 통해 입력 대화창이 나타납니다.
# 두 번째 매개변수는 대화창의 타이틀, 세 번째 매개변수는 대화창 안에 보여질 메세지를 의미합니다. 입력 대화창은 입력한 텍스트와 불 (Boolean) 값을 반환합니다.
# 텍스트를 입력한 후 'OK' 버튼을 누르면 불 값은 True, 'Cancel' 버튼을 누르면 불 값은 False가 됩니다.
# if ok:
#     self.le.setText(str(text))
# 입력한 값을 setText() 메서드를 통해 줄 편집 위젯에 표시되도록 합니다.
''' import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog)
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)
        self.le = QLineEdit(self)
        self.le.move(120, 35)
        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''



# [5.위젯 (Widget)]
# 위젯은 어플리케이션을 이루는 기본적인 구성 요소입니다.
# PyQt 툴킷은 간단하게 사용할 수 있는 다양한 위젯을 제공합니다.

# (5-20.QTextEdit)
# QTextEdit 클래스는 플레인 텍스트 (plain text)와 리치 텍스트 (rich text)를 모두 편집하고 표시할 수 있는 편집기를 제공합니다.
# 두 개의 라벨과 하나의 텍스트 편집기를 이용해서 단어수를 표시하는 간단한 프로그램을 만들어 보겠습니다.
# 텍스트 편집기에 텍스트를 입력하면, 아래에 단어수를 표시합니다.
# self.lbl1 = QLabel('Enter your sentence:')
# self.te = QTextEdit()
# self.te.setAcceptRichText(False)
# self.lbl2 = QLabel('The number of words is 0')
# QTextEdit() 클래스를 이용해서 텍스트 편집기 하나를 만들었습니다.
# setAcceptRichText를 False로 하면, 모두 플레인 텍스트로 인식합니다.
# 아래의 라벨은 단어수를 표시합니다.
# self.te.textChanged.connect(self.text_changed)
# 텍스트 편집기의 텍스트가 수정될 때마다 text_changed 메서드가 호출됩니다.
# vbox = QVBoxLayout()
# vbox.addWidget(self.lbl1)
# vbox.addWidget(self.te)
# vbox.addWidget(self.lbl2)
# vbox.addStretch()
# self.setLayout(vbox)
# 수직 박스 레이아웃을 이용해서, 두 개의 라벨과 하나의 텍스트 편집기를 수직 방향으로 배치합니다.
# def text_changed(self):
#     text = self.te.toPlainText()
#     self.lbl2.setText('The number of words is ' + str(len(text.split())))
# text_changed 메서드가 호출되면, toPlainText() 메서드를 이용해서 텍스트 편집기 (self.te)에 있던 텍스트를 text 변수에 저장합니다.
# split()은 문자열의 단어들을 리스트 형태로 바꿔줍니다.
# len(text.split())은 text의 단어수입니다.
# setText()를 이용해서 두 번째 라벨에 단어수를 표시합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('The number of words is 0')
        self.te.textChanged.connect(self.text_changed)
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()
        self.setLayout(vbox)
        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-19.QTextBrowser)
# QTextBrowser 클래스는 하이퍼텍스트 내비게이션을 포함하는 리치 텍스트 (서식있는 텍스트) 브라우저를 제공합니다.
# 이 클래스는 읽기 전용이며, QTextEdit의 확장형으로서 하이퍼텍스트 문서의 링크들을 사용할 수 있습니다.
# 편집 가능한 리치 텍스트 편집기를 사용하기 위해서는 QTextEdit을 사용해야 합니다.
# 또한 하이퍼텍스트 네비게이션이 없는 텍스트 브라우저를 사용하기 위해서는 QTextEdit을 setReadOnly()를 사용해서 편집이 불가능하도록 해줍니다.
# 짧은 리치 텍스트를 표시하기 위해서는 QLabel을 사용할 수 있습니다.
# 줄 편집기와 텍스트 브라우저가 창에 나타납니다.
# self.le = QLineEdit()
# self.le.returnPressed.connect(self.append_text)
# 줄편집기 하나를 만들었습니다.
# Enter키를 누르면 append_text 메서드가 호출됩니다.
# self.tb = QTextBrowser()
# self.tb.setAcceptRichText(True)
# self.tb.setOpenExternalLinks(True)
# QTextBrowser() 클래스를 이용해서 텍스트 브라우저를 하나 만들었습니다.
# setAcceptRichText()를 True로 설정해주면, 서식 있는 텍스트 (Rich text)를 사용할 수 있습니다.
# 디폴트로 True이기 때문에 없어도 되는 부분입니다.
# setOpenExternalLinks()를 True로 설정해주면, 외부 링크로의 연결이 가능합니다.
# self.clear_btn = QPushButton('Clear')
# self.clear_btn.pressed.connect(self.clear_text)
# clear_btn을 클릭하면, clear_text 메서드가 호출됩니다.
# def append_text(self):
#     text = self.le.text()
#     self.tb.append(text)
#     self.le.clear()
# append_text 메서드는 줄편집기에 작성된 텍스트 (self.le.text())를 텍스트 브라우저 (self.tb)에 append 해주는 기능을 합니다.
# 텍스트가 텍스트 브라우저에 추가되면, clear 메서드를 이용해서 줄편집기에 있던 텍스트는 없애줍니다.
# def clear_text(self):
#     self.tb.clear()
# clear_text 메서드가 호출되면, clear 메서드를 이용해서 텍스트 브라우저 (self.tb)에 있던 텍스트를 없애줍니다.
# Plain Text
# <b>Bold</b>
# <i>Italic</i>
# <p style="color: red">Red</p>
# <p style="font-size: 20px">20px</p>
# <a href="https://www.naver.com">Naver</a>
# 줄편집기에 위의 텍스트를 순서대로 입력하고 엔터키를 이용해서 텍스트 브라우저에 추가합니다.
''' import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)
        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)
        self.setLayout(vbox)
        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()
    def clear_text(self):
        self.tb.clear()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-18.QDateTimeEdit)
# QDateTimeEdit 위젯은 사용자에게 날짜와 시간을 선택, 편집하도록 할 때 사용합니다.
# 예제에서 QDateTimeEdit 객체를 하나 만들고, 현재 날짜와 시간으로 표시되도록 설정해보겠습니다.
# 자세한 내용은 QDateTimeEdit 공식 문서에서 확인할 수 있습니다.
# 날짜, 시간 편집 위젯 (QDateTimeEdit)이 창에 나타납니다.
# datetimeedit = QDateTimeEdit(self)
# datetimeedit.setDateTime(QDateTime.currentDateTime())
# datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
# QDateTimeEdit 클래스를 이용해서 날짜, 시간 편집 위젯(datetimeedit)을 하나 만들어줍니다.
# setDateTime 메서드에 QDateTime.currentDateTime()을 입력해서 프로그램이 실행될 때 현재 날짜와 시간으로 표시되도록 합니다.
# setDateTimeRange를 이용하면 사용자가 선택할 수 있는 시간의 범위를 제한할 수 있습니다.
# datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')
# setDisplayFormat 메서드를 이용해서 시간이 'yyyy.MM.dd hh:mm:ss'의 형식으로 표시되도록 설정했습니다.
# vbox = QVBoxLayout()
# vbox.addWidget(lbl)
# vbox.addWidget(datetimeedit)
# vbox.addStretch()
# self.setLayout(vbox)
# 수직 박스 레이아웃을 이용해서 라벨과 날짜, 시간 편집 위젯을 수직으로 배치하고, 전체 위젯의 레이아웃으로 설정합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateTimeEdit, QVBoxLayout
from PyQt5.QtCore import QDateTime
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lbl = QLabel('QTimeEdit')
        datetimeedit = QDateTimeEdit(self)
        datetimeedit.setDateTime(QDateTime.currentDateTime())
        datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')
        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(datetimeedit)
        vbox.addStretch()
        self.setLayout(vbox)
        self.setWindowTitle('QDateTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-17.QTimeEdit)
# QTimeEdit 위젯은 사용자에게 시간을 선택, 편집하도록 할 때 사용합니다.
# 예제에서 QTimeEdit 객체를 하나 만들고, 현재 시간으로 표시되도록 설정해보겠습니다.
# 자세한 내용은 QTimeEdit 공식 문서에서 확인할 수 있습니다.
# 시간 편집 위젯 (QTimeEdit)이 창에 나타납니다.
# timeedit = QTimeEdit(self)
# timeedit.setTime(QTime.currentTime())
# timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
# QTimeEdit 클래스를 이용해서 시간 편집 위젯(timeedit)을 하나 만들어줍니다.
# setTime 메서드에 QTime.currentTime()를 입력해서 프로그램이 실행될 때 현재 시간으로 표시되도록 합니다.
# setTimeRange 이용하면 사용자가 선택할 수 있는 시간의 범위를 제한할 수 있습니다.
# 최소 시간은 디폴트로 00시 00분 00초 000밀리초로 설정되어 있고, 최대 시간은 23시 59분 59초 999밀리초로 설정되어 있습니다.
# timeedit.setDisplayFormat('hh:mm:ss')
# setDisplayFormat 메서드를 이용해서 시간이 'hh:mm:ss'의 형식으로 표시되도록 설정했습니다.
# vbox = QVBoxLayout()
# vbox.addWidget(lbl)
# vbox.addWidget(timeedit)
# vbox.addStretch()
# self.setLayout(vbox)
# 수직 박스 레이아웃을 이용해서 라벨과 시간 편집 위젯을 수직으로 배치하고, 전체 위젯의 레이아웃으로 설정합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QVBoxLayout
from PyQt5.QtCore import QTime
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lbl = QLabel('QTimeEdit')
        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        timeedit.setDisplayFormat('hh:mm:ss')
        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(timeedit)
        vbox.addStretch()
        self.setLayout(vbox)
        self.setWindowTitle('QTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-16.QDateEdit)
# QDateEdit 위젯은 사용자에게 날짜를 선택, 편집하도록 할 때 사용합니다.
# 예제에서 QDateEdit 객체를 하나 만들고, 현재 날짜로 표시되도록 설정해보겠습니다.
# 자세한 내용은 QDateEdit 공식 문서에서 확인할 수 있습니다.
# 날짜 편집 위젯 (QDateEdit)이 창에 나타납니다.
# dateedit = QDateEdit(self)
# dateedit.setDate(QDate.currentDate())
# dateedit.setMinimumDate(QDate(1900, 1, 1))
# dateedit.setMaximumDate(QDate(2100, 12, 31))
# QDateEdit 클래스를 이용해서 날짜 편집 위젯을 하나 만들어줍니다.
# setDate 메서드에 QDate.currentDate()를 입력해서 프로그램이 실행될 때 현재 날짜로 표시되도록 합니다.
# setMinimumDate와 setMaximumDate를 이용하면 사용자가 선택할 수 있는 날짜의 범위를 제한할 수 있습니다.
# 최소 날짜는 디폴트로 1752년 9월 14일로 설정되어 있고, 최대 날짜는 9999년 12월 31일로 설정되어 있습니다.
# 최소 날짜는 최소 100년 1월 1일 이상이어야합니다.
# # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
# setDateRange 메서드는 setMinimumDate와 setMaximumDate를 동시에 사용하는 것과 같습니다.
# vbox = QVBoxLayout()
# vbox.addWidget(lbl)
# vbox.addWidget(dateedit)
# vbox.addStretch()
# self.setLayout(vbox)
# 수직 박스 레이아웃을 이용해서 라벨과 날짜 편집 위젯을 수직으로 배치하고, 전체 위젯의 레이아웃으로 설정합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit, QVBoxLayout
from PyQt5.QtCore import QDate
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lbl = QLabel('QDateEdit')
        dateedit = QDateEdit(self)
        dateedit.setDate(QDate.currentDate())
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))
        # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()
        self.setLayout(vbox)
        self.setWindowTitle('QDateEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-15.QDoubleSpinBox)
# QDoubleSpinBox 클래스는 실수를 선택, 조절하도록 하는 더블 스핀 박스 위젯을 제공합니다.
# 자세한 내용은 QDoubleSpinBox 공식 문서에서 확인할 수 있습니다.
# 라벨 두 개 (self.lbl1, self.lbl2)와 더블 스핀 박스 위젯 (self.spinbox)이 창에 나타납니다.
# self.dspinbox = QDoubleSpinBox()
# self.dspinbox.setRange(0, 100)
# self.dspinbox.setSingleStep(0.5)
# QDoubleSpinBox 객체 (self.dspinbox)를 하나 만듭니다.
# setRange() 메서드를 이용해서 선택 범위를 제한할 수 있습니다. 최소값은 0.0, 최대값은 99.99가 디폴트입니다.
# setSingleStep() 메서드를 이용해서 한 스텝을 0.5로 설정해줍니다.
# self.dspinbox.setPrefix('$ ')
# self.dspinbox.setDecimals(1)
# setPrefix()를 이용해서, 숫자 앞에 올 문자를 설정할 수 있습니다. setSuffix()는 숫자 뒤에 문자가 오도록 합니다.
# setDecimals()를 이용해서 소수점 아래 표시될 자리수를 정해줍니다.
# self.dspinbox.valueChanged.connect(self.value_changed)
# 더블 스핀 박스 위젯의 값이 변경될 때 발생하는 시그널 (valueChanged)을 self.value_changed 메서드에 연결합니다.
# vbox = QVBoxLayout()
# vbox.addWidget(self.lbl1)
# vbox.addWidget(self.dspinbox)
# vbox.addWidget(self.lbl2)
# vbox.addStretch()
# self.setLayout(vbox)
# 수직 박스 레이아웃을 이용해서 라벨 두 개와 스핀 박스 위젯을 수직으로 배치하고, 전체 위젯의 레이아웃으로 설정합니다.
# def value_changed(self):
#     self.lbl2.setText('$ '+str(self.dspinbox.value()))
# 더블 스핀 박스의 값이 변경될 때, self.lbl2의 텍스트를 더블 스핀 박스의 값 (self.dspinbox.value())으로 설정하도록 합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDoubleSpinBox, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl1 = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.setDecimals(1)
        self.lbl2 = QLabel('$ 0.0')
        self.dspinbox.valueChanged.connect(self.value_changed)
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()
        self.setLayout(vbox)
        self.setWindowTitle('QDoubleSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def value_changed(self):
        self.lbl2.setText('$ ' + str(self.dspinbox.value()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-14.QSpinBox)
# QSpinBox 클래스는 정수를 선택, 조절하도록 하는 스핀 박스 위젯을 제공합니다.
# 자세한 내용은 QSpinBox 공식 문서에서 확인할 수 있습니다.
# 라벨 두 개 (self.lbl1, self.lbl2)와 스핀 박스 위젯 (self.spinbox)이 창에 나타납니다.
# self.spinbox = QSpinBox()
# self.spinbox.setMinimum(-10)
# self.spinbox.setMaximum(30)
# QSpinBox 객체 (self.spinbox)를 하나 만듭니다.
# setMinimum()과 setMaximum() 메서드를 이용해서 선택 범위를 제한할 수 있습니다. 최소값은 0, 최대값은 99가 디폴트입니다.
# self.spinbox.setRange(-10, 30)
# setRange() 메서드는 setMinimum()과 setMaximum()을 합쳐놓은 것과 같습니다.
# self.spinbox.setSingleStep(2)
# setSingleStep()을 이용해서 한 스텝을 2로 설정합니다.
# 스핀 박스의 경우, 한 스텝으로 설정할 수 있는 최소값은 1입니다.
# self.spinbox.valueChanged.connect(self.value_changed)
# 스핀 박스 위젯의 값이 변경될 때 발생하는 시그널 (valueChanged)을 self.value_changed 메서드에 연결합니다.
# vbox = QVBoxLayout()
# vbox.addWidget(self.lbl1)
# vbox.addWidget(self.spinbox)
# vbox.addWidget(self.lbl2)
# vbox.addStretch()
# self.setLayout(vbox)
# 수직 박스 레이아웃을 이용해서 라벨 두 개와 스핀 박스 위젯을 수직으로 배치하고, 전체 위젯의 레이아웃으로 설정합니다.
# def value_changed(self):
#     self.lbl2.setText(str(self.spinbox.value()))
# 스핀 박스의 값이 변경될 때, self.lbl2의 텍스트를 스핀 박스의 값 (self.spinbox.value())으로 설정하도록 합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        self.spinbox.setRange(-10, 30)
        self.spinbox.setSingleStep(2)
        self.lbl2 = QLabel('0')
        self.spinbox.valueChanged.connect(self.value_changed)
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()
        self.setLayout(vbox)
        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-13.QCalendarWidget)
# QCalendarWidget을 이용해서 사용자가 날짜를 선택할 수 있도록 달력을 표시할 수 있습니다.
# 달력은 월 단위로 표시되고, 처음 실행될 때 현재의 연도, 월, 날짜로 선택되어 있습니다.
# 자세한 내용은 QCalendarWidget 공식 문서에서 확인할 수 있습니다.
# 달력 하나와 날짜를 표시하는 라벨 하나가 위젯 창에 나타납니다.
# 설명
# cal = QCalendarWidget(self)
# cal.setGridVisible(True)
# cal.clicked[QDate].connect(self.showDate)
# QCalenderWidget의 객체(cal)를 하나 만듭니다.
# setGridVisible(True)로 설정하면, 날짜 사이에 그리드가 표시됩니다.
# 날짜를 클릭했을 때 showDate 메서드가 호출되도록 연결해줍니다.
# self.lbl = QLabel(self)
# date = cal.selectedDate()
# self.lbl.setText(date.toString())
# selectedDate는 현재 선택된 날짜 정보를 갖고 있습니다. (디폴트는 현재 날짜)
# 현재 날짜 정보를 라벨에 표시되도록 해줍니다.
# vbox = QVBoxLayout()
# vbox.addWidget(cal)
# vbox.addWidget(self.lbl)
# 수직 박스 레이아웃을 이용해서, 달력과 라벨을 수직으로 배치해줍니다.
# def showDate(self, date):
#     self.lbl.setText(date.toString())
# showDate 메서드에서, 날짜를 클릭할 때마다 라벨 텍스트가 선택한 날짜(date.toString())로 표시되도록 합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()
    def showDate(self, date):
        self.lbl.setText(date.toString())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-12.QPixmap)
# QPixmap은 이미지를 다룰 때 사용되는 위젯입니다.
# 지원하는 파일 형식은 아래와 같습니다. 어떤 이미지 형식은 '읽기'만 가능합니다.
# QPixmap을 이용해서 창에 하나의 이미지를 나타내 보겠습니다.
# 이미지 하나가 위젯 창에 나타납니다.
# pixmap = QPixmap('landscape.jpg')
# 파일 이름을 입력해주고, QPixmap 객체 (pixmap)를 하나 만듭니다.
# lbl_img = QLabel()
# lbl_img.setPixmap(pixmap)
# 라벨을 하나 만들고, setPixmap을 이용해서 pixmap을 라벨에 표시될 이미지로 설정해줍니다.
# lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
# lbl_size.setAlignment(Qt.AlignCenter)
# width()와 height()는 이미지의 너비, 높이를 반환합니다.
# 너비, 높이를 표시하는 라벨 (lbl_size)를 하나 만들고, setAlignment 메서드를 이용해서 가운데 정렬로 설정합니다.
# vbox = QVBoxLayout()
# vbox.addWidget(lbl)
# self.setLayout(vbox)
# 수평 박스 레이아웃을 하나 만들고 라벨을 배치합니다.
# setLayout()을 이용해서 수평 박스(hbox)를 창의 레이아웃으로 지정해줍니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        pixmap = QPixmap('C:\\Users\\PROCESSOR\\Desktop\\EXE\\PYTHON\\0.STUDY\\STUDY5-파이선으로 만드는 나만의 GUI 프로그램\\ICON\\4_12_qpixmap.png')
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)
        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-11.QTabWidget)
# GUI 프로그램을 사용하다보면 위의 그림과 같이 탭(Tab)이 있는 창을 볼 수 있습니다.
# 이러한 탭은 프로그램 안의 구성요소들이 많은 면적을 차지하지 않으면서, 그것들을 카테고리에 따라 분류할 수 있기 때문에 유용하게 사용될 수 있습니다.
# 간단한 예제를 통해 두 개의 탭을 갖는 위젯을 하나 만들어보겠습니다.
# 두 개의 탭을 갖는 작은 위젯이 하나 만들어집니다.
# 설명
# tab1 = QWidget()
# tab2 = QWidget()
# 각 탭에 위치할 두 개의 위젯을 만들었습니다.
# tabs = QTabWidget()
# tabs.addTab(tab1, 'Tab1')
# tabs.addTab(tab2, 'Tab2')
# QTabWidget()을 이용해서 탭을 만들어주고, addTab()을 이용해서 'Tab1'과 'Tab2'를 tabs에 추가해줍니다.
# vbox = QVBoxLayout()
# vbox.addWidget(tabs)
# self.setLayout(vbox)
# 수직 박스 레이아웃을 하나 만들어서 탭 위젯 (tabs)을 넣어줍니다.
# 그리고 수직 박스(vbox)를 위젯의 레이아웃으로 설정합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        tab1 = QWidget()
        tab2 = QWidget()
        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)
        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-10.QGroupBox)
# 그룹 박스는 상단 타이틀과 단축키 (shortcut)를 제공하며, 그 안에 다양한 위젯들을 나타낼 수 있습니다. (QGroupBox 공식 문서 참고)
# QGroupBox 클래스는 제목과 제목의 정렬을 설정하도록 해줍니다. 그룹 박스는 체크 가능하도록 설정할 수 있는데, 그룹 박스의 체크 여부에 따라 
# 그 그룹 박스 안에 있는 위젯들이 사용 가능하거나 불가능해집니다.
# 공간을 절약하기 위해 flat 속성을 활성화할 수 있는데, 보통 프레임의 왼쪽, 오른쪽, 아래쪽 가장자리가 없게 표됩니다.
# 위 그림과 같이 QGroupBox 위젯은 제목을 갖는 그룹 박스 프레임을 제공합니다
# QGroupBox 클래스를 이용해서 버튼의 종류에 따라 네 개의 그룹 박스를 만들었습니다.
# 설명
# grid = QGridLayout()
# grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
# grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
# grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
# grid.addWidget(self.createPushButtonGroup(), 1, 1)
# self.setLayout(grid)
# 그리드 레이아웃을 이용해서 그룹박스를 배치합니다.
# 각 메서드를 통해 만들어지는 그룹박스가 addWidget()을 통해 각 위치로 배치됩니다.
# def createFirstExclusiveGroup(self):    
#     groupbox = QGroupBox('Exclusive Radio Buttons')
#     radio1 = QRadioButton('Radio1')
#     radio2 = QRadioButton('Radio2')
#     radio3 = QRadioButton('Radio3')
#     radio1.setChecked(True)
#     vbox = QVBoxLayout()
#     vbox.addWidget(radio1)
#     vbox.addWidget(radio2)
#     vbox.addWidget(radio3)
#     groupbox.setLayout(vbox)
#     return groupbox
# createFirstExclusiveGroup() 메서드는 배타적인 라디오버튼을 갖는 그룹박스를 만듭니다.
# 메서드는 먼저 그룹박스 (groupbox)를 하나 만들고, 버튼을 만든 다음 수직 박스 레이아웃을 통해 배치합니다.
# 마지막으로 수직 박스 레이아웃 (vbox)를 그룹 박스의 레이아웃으로 설정합니다.
# 세 개의 라디오버튼을 만들고 수직으로 배치했습니다.
# def createSecondExclusiveGroup(self):
#     groupbox = QGroupBox('Exclusive Radio Buttons')
#     groupbox.setCheckable(True)
#     groupbox.setChecked(False)
# createSecondExclusiveGroup() 메서드는 세 개의 라디오버튼과 한 개의 체크박스를 갖는 그룹박스를 만듭니다.
# setCheckable() 메서드를 이용해서 groupbox도 선택 가능하도록 할 수 있습니다.
# def createNonExclusiveGroup(self):
#     groupbox = QGroupBox('Non-Exclusive Checkboxes')
#     groupbox.setFlat(True)
# createNonExclusiveGroup() 메서드는 배타적이지 않은 체크박스들을 갖는 그룹박스를 만듭니다.
# setFlat()을 이용해서 그룹박스를 평평하게 보이도록 합니다.
# def createPushButtonGroup(self):
#     groupbox = QGroupBox('Push Buttons')
#     groupbox.setCheckable(True)
#     groupbox.setChecked(True)
# createPushButtonGroup() 메서드는 여러 개의 푸시버튼을 갖는 그룹 박스를 만듭니다.
# setCheckable()과 setChecked()를 이용해서, 그룹 박스를 선택 가능하게, 그리고 실행했을 때 선택되어 있도록 설정합니다.
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton
, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout)
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)
        self.setLayout(grid)
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()
    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')
        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)
        return groupbox
    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)
        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)
        return groupbox
    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True)
        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)
        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)
        return groupbox
    def createPushButtonGroup(self):
        groupbox = QGroupBox('Push Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)
        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('Popup Button')
        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)
        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)
        return groupbox
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# (5-9.QSplitter)
# QSplitter 클래스는 스플리터 위젯을 구현합니다.
# 스플리터 (splitter)는 경계를 드래그해서 자식 위젯의 크기를 조절할 수 있도록 합니다.
# 예제를 통해 위젯을 네 개의 작은 영역으로 쪼개어 보겠습니다.
# 창이 네 개의 작은 영역으로 나누어졌습니다.
# 각 영역의 프레임의 스타일을 다르게 설정할 수 있습니다.
# top = QFrame()
# top.setFrameShape(QFrame.Box)
# midleft = QFrame()
# midleft.setFrameShape(QFrame.StyledPanel)
# midright = QFrame()
# midright.setFrameShape(QFrame.Panel)
# bottom = QFrame()
# bottom.setFrameShape(QFrame.WinPanel)
# bottom.setFrameShadow(QFrame.Sunken)
# 각 영역에 들어갈 프레임을 만들어줍니다. 프레임의 형태와 그림자의 스타일을 setFrameShape과 setFrameShadow를 이용해서 설정할 수 있습니다.
# 예제에서와 같이 setFrameShape에는 NoFrame/Box/Panel/StyledPanel/HLine/VLine/WinPanel을, setFrameShadow에는 Plain/Raised/Sunken 상수를 사용할 수 있습니다.
# 각 상수의 사용에 대한 설명과 결과는 아래의 이미지를 참고하세요.
# 프레임의 형태를 설정하는 상수
# 프레임의 그림자를 설정하는 상수
# 프레임의 형태와 그림자
# splitter1 = QSplitter(Qt.Horizontal)
# splitter1.addWidget(midleft)
# splitter1.addWidget(midright)
# splitter2 = QSplitter(Qt.Vertical)
# splitter2.addWidget(top)
# splitter2.addWidget(splitter1)
# splitter2.addWidget(bottom)
# QSplitter를 이용해서 수평 방향으로 쪼개고, 왼쪽에는 midleft, 오른쪽에는 midright 프레임 위젯을 넣어줍니다.
# 다음, 수직 방향으로 쪼개고, top, splitter1, bottom 3개의 프레임 위젯을 넣어줍니다.
# hbox.addWidget(splitter2)
# self.setLayout(hbox)
# splitter2 위젯을 수평 박스 레이아웃에 넣어주고, 전체의 레이아웃으로 설정합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        hbox = QHBoxLayout()
        top = QFrame()
        top.setFrameShape(QFrame.Box)
        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)
        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-8.QSlider & QDial)
# QSlider는 수평 또는 수직 방향의 슬라이더를 제공합니다.
# 슬라이더는 제한된 범위 안에서 값을 조절하는 위젯입니다. (QSlider 공식 문서 참고)
# 슬라이더의 틱(tick)의 간격을 조절하기 위해서는 setTickInterval() 메서드, 틱(tick)의 위치를 조절하기 위해서는 setTickPosition() 메서드를 사용합니다.
# setTickInterval() 메서드의 입력값은 픽셀이 아니라 값을 의미합니다.
# setTickPosition() 메서드의 입력값과 기능은 아래의 표와 같습니다. (예시: setTickPosition(QSlider.NoTicks) 또는 setTickPosition(0))
# 상수	값	설명
# QSlider.NoTicks	0	틱을 표시하지 않습니다.
# QSlider.TicksAbove	1	틱을 (수평) 슬라이더 위쪽에 표시합니다.
# QSlider.TicksBelow	2	틱을 (수평) 슬라이더 아래쪽에 표시합니다.
# QSlider.TicksBothSides	3	틱을 (수평) 슬라이더 양쪽에 표시합니다.
# QSlider.TicksLeft	TicksAbove	틱을 (수직) 슬라이더 왼쪽에 표시합니다.
# QSlider.TicksRight	TicksBelow	틱을 (수직) 슬라이더 오른쪽에 표시합니다.
# QDial은 슬라이더를 둥근 형태로 표현한 다이얼 위젯이며, 기본적으로 같은 시그널과 슬롯, 메서드들을 공유합니다. (QDial 공식 문서 참고)
# 위의 그림처럼 다이얼 위젯에 노치(notch)를 표시하기 위해서는 setNotchesVisible() 메서드를 사용합니다. 
# True로 설정하면 둥근 다이얼을 따라서 노치들이 표시됩니다. 기본적으로 노치는 표시되지 않도록 설정되어 있습니다.
# QSlider과 QDial 위젯에서 가장 자주 쓰이는 시그널은 아래와 같습니다. 예제에서는 valueChanged 시그널을 사용해보겠습니다.
# 시그널	설명
# valueChanged()	슬라이더의 값이 변할 때 발생합니다.
# sliderPressed()	사용자가 슬라이더를 움직이기 시작할 때 발생합니다.
# sliderMoved()	사용자가 슬라이더를 움직이면 발생합니다.
# sliderReleased()	사용자가 슬라이더를 놓을 때 발생합니다.
# 슬라이더, 다이얼 위젯과 푸시 버튼을 하나 만들었습니다.
# 슬라이더와 다이얼은 서로 연결되어 있어서 항상 같은 값을 가지고, 푸시 버튼을 누르면 두 위젯의 값이 모두 0이 됩니다.
# self.slider = QSlider(Qt.Horizontal, self)
# QSlider 위젯을 하나 만들었습니다. Qt.Horizontal 또는 Qt.Vertical을 입력해줌으로써 수평 또는 수직 방향을 설정합니다.
# self.slider.setRange(0, 50)
# self.slider.setSingleStep(2)
# setRange() 메서드로 값의 범위를 0에서 50까지로 설정합니다. setSingleStep() 메서드는 조절 가능하는 최소 단위를 설정합니다.
# self.dial = QDial(self)
# QDial 위젯을 하나 만들었습니다.
# self.dial.setRange(0, 50)
# 슬라이더와 마찬가지로 setRange() 메서드로 범위를 정해줍니다.
# self.slider.valueChanged.connect(self.dial.setValue)
# self.dial.valueChanged.connect(self.slider.setValue)
# 슬라이더와 다이얼의 값이 변할 때 발생하는 시그널을 각각 다이얼과 슬라이더의 값을 조절해주는 메서드 (setValue)에 서로 연결함으로써
# 두 위젯의 값이 언제나 일치하도록 해줍니다.
# btn.clicked.connect(self.button_clicked)
# 'Default' 푸시 버튼을 클릭하면 발생하는 시그널을 button_clicked 메서드에 연결합니다.
# def button_clicked(self):
#     self.slider.setValue(0)
#     self.dial.setValue(0)
# button_clicked() 메서드는 슬라이더와 다이얼의 값을 모두 0으로 조절합니다.
# 따라서 'Default' 푸시 버튼을 클릭하면, 슬라이더와 다이얼의 값이 0으로 초기화됩니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)
        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)
        btn = QPushButton('Default', self)
        btn.move(35, 160)
        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)
        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()
    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-7.QProgressBar)
# 위의 그림은 각각 macOS와 Windows7의 기본적인 진행 표시줄(progress bar)을 나타냅니다. 진행 표시줄은 시간이 걸리는 작업에 사용되는 위젯입니다.
# (QProgressBar 공식 문서 참고)
# QProgressBar 위젯은 수평, 수직의 진행 표시줄을 제공합니다. setMinimum()과 setMaximum() 메서드로 진행 표시줄의 최소값과 최대값을 설정할 수 있으며, 
# 또는 setRange() 메서드로 한 번에 범위를 설정할 수도 있습니다. 기본값은 0과 99입니다.
# setValue() 메서드로 진행 표시줄의 진행 상태를 특정 값으로 설정할 수 있고, reset() 메서드는 초기 상태로 되돌립니다.
# 진행 표시줄의 최소값과 최대값을 모두 0으로 설정하면, 진행 표시줄은 위의 그림과 같이 항상 진행 중인 상태로 표시됩니다. 
# 이 기능은 다운로드하고 있는 파일의 용량을 알 수 없을 때 유용하게 사용할 수 있습니다.
# 수평의 진행 표시줄과 푸시 버튼을 하나씩 만들었습니다.
# 푸시 버튼을 통해 진행 표시줄을 시작하고 멈출 수 있습니다.
# self.pbar = QProgressBar(self)
# QProgressBar 생성자로 진행 표시줄을 하나 만들어줍니다.
# self.timer = QBasicTimer()
# 진행 표시줄을 활성화하기 위해, 타이머 객체를 사용합니다.
# self.timer.start(100, self)
# 타이머 이벤트를 실행하기 위해, start() 메서드를 호출합니다.
# 이 메서드는 두 개의 매개변수를 갖는데, 첫 번째는 종료시간이고 두 번째는 이벤트가 수행될 객체입니다.
# def timerEvent(self, e):
#     if self.step >= 100:
#         self.timer.stop()
#         self.btn.setText('Finished')
#         return
#     self.step = self.step + 1
#     self.pbar.setValue(self.step)
# 각각의 QObject와 그 자손들은 timerEvent() 이벤트 핸들러를 갖습니다. 타이머 이벤트에 반응하기 위해, 이벤트 핸들러를 재구성해줍니다.
# def doAction(self):
#     if self.timer.isActive():
#         self.timer.stop()
#         self.btn.setText('Start')
#     else:
#         self.timer.start(100, self)
#         self.btn.setText('Stop')
# doAction() 메서드 안에서, 타이머를 시작하고 멈추도록 해줍니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0
        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-6.QLineEdit)
# QLineEdit은 한 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯입니다. (QLineEdit 공식 문서 참고)
# echoMode()를 설정함으로써 '쓰기 전용' 영역으로 사용할 수 있습니다. 이 기능은 비밀번호와 같은 입력을 받을 때 유용하게 사용됩니다.
# setEchoMode() 메서드로 이러한 모드를 설정할 수 있으며, 입력값과 기능은 아래 표와 같습니다.
# Normal 모드를 가장 흔하게 사용하며, 기본 설정값이기도 합니다. (예시: setEchoMode(QLineEdit.Normal) 또는 setEchoMode(0))
# 상수	값	설명
# QLineEdit.Normal	0	입력된 문자를 표시합니다. (기본값)
# QLineEdit.NoEcho	1	문자열을 표시하지 않습니다. 이 설정은 비밀번호의 글자수도 공개하지 않을 때 유용합니다.
# QLineEdit.Password	2	입력된 문자 대신 비밀번호 가림용 문자를 표시합니다.
# QLineEdit.PasswordEchoOnEdit	3	입력할 때만 문자를 표시하고, 수정 중에는 다른 문자를 표시합니다.
# maxLength() 메서드로 입력되는 텍스트의 길이를 제한할 수 있고, setValidator() 메서드로 입력되는 텍스트의 종류를 제한할 수도 있습니다.
# setText() 또는 insert() 메서드로, 텍스트를 편집할 수 있고, text() 메서드로 입력된 텍스트를 가져올 수 있습니다. 만약 echoMode에 의해 입력되는 텍스트와 표시되는 텍스트가 다르다면, displayText() 메서드로 표시되는 텍스트를 가져올 수도 있습니다.
# setSelection(), selectAll() 메서드로 텍스트를 선택하거나, cut(), copy(), paste() 메서드를 통해 잘라내기, 복사하기, 붙여넣기 등의 동작을 수행할 수 있습니다. 또한 setAlignment() 메서드로 텍스트의 정렬을 설정할 수 있습니다.
# 텍스트가 변경되거나 커서가 움직일 때, textChanged(), cursorPositionChanged()와 같은 시그널이 발생합니다.
# 자주 사용되는 시그널은 아래와 같습니다.
# 시그널	설명
# cursorPositionChanged()	커서가 움직일 때 발생하는 신호를 발생합니다.
# editingFinished()	편집이 끝났을 때 (Return/Enter 버튼이 눌릴 때) 신호를 발생합니다.
# returnPressed()	Return/Enter 버튼이 눌릴 때 신호를 발생합니다.
# selectionChanged()	선택 영역이 바뀔 때 신호를 발생합니다.
# textChanged()	텍스트가 변경될 때 신호를 발생합니다.
# textEdited()	텍스트가 편집될 때 신호를 발생합니다.
# 위젯에 하나의 라벨과 하나의 QLineEdit 위젯이 포함됩니다.
# QLineEdit 위젯에서 입력되고 수정되는 텍스트가 라벨에 즉시 표시됩니다.
# 설명
# qle = QLineEdit(self)
# QLineEdit 위젯을 만들었습니다.
# qle.textChanged[str].connect(self.onChanged)
# qle의 텍스트가 바뀌면, onChanged() 메서드를 호출합니다.
# def onChanged(self, text):
#     self.lbl.setText(text)
#     self.lbl.adjustSize()
# onChanged() 메서드 안에서, 입력된 'text'를 라벨 위젯(lbl)의 텍스트로 설정하도록 합니다.
# 또한 adjustSize() 메서드로 텍스트의 길이에 따라 라벨의 길이를 조절해주도록 합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)
        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)
        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-5.QComboBox)
# QComboBox는 작은 공간을 차지하면서, 여러 옵션들을 제공하고 그 중 하나의 옵션을 선택할 수 있도록 해주는 위젯입니다. (QComboBox 공식 문서 참고)
# 하나의 라벨과 콤보박스 위젯을 만들고, 콤보박스에서 선택한 항목이 라벨에 나타나도록 했습니다.
# cb = QComboBox(self)
# cb.addItem('Option1')
# cb.addItem('Option2')
# cb.addItem('Option3')
# cb.addItem('Option4')
# cb.move(50, 50)
# QComboBox 위젯을 하나 만들고, addItem() 메서드를 이용해서 선택 가능한 4개의 옵션들을 추가했습니다.
# cb.activated[str].connect(self.onActivated)
# 옵션을 선택하면, onActivated() 메서드가 호출됩니다.
# def onActivated(self, text):
#     self.lbl.setText(text)
#     self.lbl.adjustSize()
# 선택한 항목의 텍스트가 라벨에 나타나도록 하고, adjustSize() 메서드를 이용해서 라벨의 크기를 자동으로 조절하도록 합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)
        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)
        cb.activated[str].connect(self.onActivated)
        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-4.QRadioButton)
# QRadioButton 위젯은 사용자가 선택할 수 있는 버튼을 만들 때 사용합니다. 이 버튼에도 체크 박스와 마찬가지로 텍스트 라벨이 하나 포함됩니다.
# (QRadioButton 공식 문서 참고)
# 라디오 버튼은 일반적으로 사용자에게 여러 개 중 하나의 옵션을 선택하도록 할 때 사용됩니다. 그래서 한 위젯 안에 여러 라디오 버튼은 기본적으로
# autoExclusive로 설정되어 있습니다. 하나의 버튼을 선택하면 나머지 버튼들은 선택 해제가 됩니다.
# 한 번에 여러 버튼을 선택할 수 있도록 하려면 setAutoExclusive() 메서드에 False를 입력해주면 됩니다.
# 또한 한 위젯 안에 여러 개의 exclusive 버튼 그룹을 배치하고 싶다면 QButtonGroup() 메서드를 사용할 수 있습니다. (QButtonGroup 공식 문서 참고)
# 체크 박스와 마찬가지로 버튼의 상태가 바뀔 때, toggled() 시그널이 발생합니다. 또한 특정 버튼의 상태를 가져오고 싶을 때, 
# isChecked() 메서드를 사용할 수 있습니다.
# 자주 쓰이는 QRadioButton의 메서드는 아래와 같습니다.
# 자주 쓰이는 메서드
# 메서드	설명
# text()	버튼의 텍스트를 반환합니다.
# setText()	라벨에 들어갈 텍스트를 설정합니다.
# setChecked()	버튼의 선택 여부를 설정합니다.
# isChecked()	버튼의 선택 여부를 반환합니다.
# toggle()	버튼의 상태를 변경합니다.
# 자주 쓰이는 메서드
# 메서드	설명
# pressed()	버튼을 누를 때 신호를 발생합니다.
# released()	버튼에서 뗄 때 신호를 발생합니다.
# clicked()	버튼을 클릭할 때 신호를 발생합니다.
# toggled()	버튼의 상태가 바뀔 때 신호를 발생합니다.
# 두 개의 라디오버튼을 만들었습니다.
# rbtn1 = QRadioButton('First Button', self)
# QRadioButton을 하나 만듭니다. 라벨에 들어갈 텍스트와 부모 위젯을 입력합니다.
# rbtn1.setChecked(True)
# setChecked()를 True로 설정하면 프로그램이 실행될 때 버튼이 선택되어 표시됩니다.
# rbtn2.setText('Second Button')
# setText() 메서드를 통해서도 라벨의 텍스트를 설정할 수 있습니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)
        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''
 
# (5-3.QCheckBox)
# QCheckBox 위젯은 on(체크됨)/off(체크안됨)의 두 상태를 갖는 버튼을 제공합니다. 이 위젯은 하나의 텍스트 라벨과 함께 체크 박스를 제공합니다.
# (QCheckBox 공식 문서 참고)
# 체크 박스가 선택되거나 해제될 때, stateChanged() 시그널을 발생합니다. 체크 박스의 상태가 변할 때마다 어떠한 동작을 발생시키고 싶을 때, 
# 이 시그널을 특정 슬롯에 연결할 수 있습니다.
# 또한 체크 박스의 선택 여부를 확인하기 위해서, isChecked() 메서드를 사용할 수 있습니다. 선택 여부에 따라 boolean 값을 반환합니다.
# 일반적인 체크 박스는 선택/해제 상태만을 갖지만, setTristate() 메서드를 사용하면 '변경 없음(no change)' 상태를 가질 수 있습니다. 
# 이 체크 박스는 사용자에게 선택하거나 선택하지 않을 옵션을 줄 때 유용합니다.
# 세 가지 상태를 갖는 체크 박스의 상태를 얻기 위해서는 checkState() 메서드를 사용합니다. 선택/변경 없음/해제 여부에 따라 각각 2/1/0 값을 반환합니다.
# QButtonGroup 클래스를 사용하면 여러 개의 버튼을 묶어서 exclusive/non-exclusive 버튼 그룹을 만들 수 있습니다. 
# exclusive 버튼 그룹은 여러 개 중 하나의 버튼만 선택할 수 있습니다. (QButtonGroup 공식 문서 참고)
# QCheckBox 위젯과 함께 자주 쓰이는 메서드는 아래 표와 같습니다.
# 자주 쓰이는 메서드
# 메서드	설명
# text()	체크 박스의 라벨 텍스트를 반환합니다.
# setText()	체크 박스의 라벨 텍스트를 설정합니다.
# isChecked()	체크 박스의 상태를 반환합니다. (True/False)
# checkState()	체크 박스의 상태를 반환합니다. (2/1/0)
# toggle()	체크 박스의 상태를 변경합니다.
# 자주 쓰이는 시그널
# 시그널	설명
# pressed()	체크 박스를 누를 때 신호를 발생합니다.
# released()	체크 박스에서 뗄 때 신호를 발생합니다.
# clicked()	체크 박스를 클릭할 때 신호를 발생합니다.
# stateChanged()	체크 박스의 상태가 바뀔 때 신호를 발생합니다.
# 체크박스를 하나 만들고, 체크가 되어 있을 때 타이틀바에 'QCheckBox' 글자가 나타나도록 했습니다.
# 체크박스의 상태에 따라 타이틀이 나타나고 사라집니다.
# cb = QCheckBox('Show title', self)
# 'Show title'이라는 텍스트 라벨을 갖는 체크박스를 하나 만듭니다.
# cb.toggle()
# 체크박스는 디폴트로 체크가 되어있지 않은 off 상태로 나타나기 때문에 on 상태로 바꾸기 위해 toggle() 메서드를 사용했습니다.
# cb.stateChanged.connect(self.changeTitle)
# 체크박스의 상태가 바뀔 때 발생하는 시그널 (stateChanged)을 우리가 정의한 changeTitle() 메서드에 연결합니다.
# def changeTitle(self, state):
#     if state == Qt.Checked:
#         self.setWindowTitle('QCheckBox')
#     else:
#         self.setWindowTitle(' ')
# 체크박스의 상태 (state)가 changeTitle() 메서드의 매개변수로 주어집니다.
# 체크가 되어있으면 타이틀을 'QCheckBox'로, 그렇지 않으면 빈 문자열로 나타내게 됩니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-2.QLabel)
# QLabel 위젯은 텍스트 또는 이미지 라벨을 만들 때 쓰입니다. 사용자와 어떤 상호작용을 제공하지는 않습니다. (QLabel 공식 문서 참고)
# 라벨은 기본적으로 수평 방향으로는 왼쪽, 수직 방향으로는 가운데 정렬이지만 setAlignment() 메서드를 통해 조절할 수 있습니다.
# label1 = QLabel('First Label', self)
# label1.setAlignment(Qt.AlignCenter)
# QLabel 위젯을 하나 만들었습니다. 생성자에 라벨 텍스트와 부모 위젯을 입력해줍니다.
# setAlignment() 메서드로 라벨의 배치를 설정할 수 있습니다.
# Qt.AlignCenter로 설정해주면 수평, 수직 방향 모두 가운데 위치하게 됩니다.
# font1 = label1.font()
# font1.setPointSize(20)
# 라벨에 사용될 폰트를 하나 만들었습니다.
# setPointSize() 메서드로 폰트의 크기를 설정해줍니다.
# label2 = QLabel('Second Label', self)
# label2.setAlignment(Qt.AlignVCenter)
# 두번째 라벨을 만들고, 이번에는 수직 방향으로만 가운데 (Qt.AlignVCenter)로 설정해줍니다.
# 수평 방향으로 가운데로 설정하려면 Qt.AlignHCenter를 입력해주면 됩니다.
# font2 = label2.font()
# font2.setFamily('Times New Roman')
# font2.setBold(True)
# 두번째 라벨에 설정할 폰트를 하나 만들고, setFamily() 메서드로 폰트의 종류를 'Times New Roman'으로 설정해줍니다.
# setBold(True)로 폰트를 진하게 설정합니다.
# 이번에는 폰트의 크기를 설정하지 않았기 때문에 디폴트 크기인 13으로 설정됩니다.
# 라벨을 하나 만들고, 라벨의 스타일과 관련된 몇 개의 메서드들을 사용해 보겠습니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)
        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignVCenter)
        font1 = label1.font()
        font1.setPointSize(20)
        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)
        label1.setFont(font1)
        label2.setFont(font2)
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        self.setLayout(layout)
        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (5-1.QPushButton)
# 푸시 버튼(push button) 또는 명령 버튼(command button)은 사용자가 프로그램에 명령을 내려서 어떤 동작을 하도록 할 때 사용되는 버튼이며, 
# GUI 프로그래밍에서 가장 흔하게 사용되고 중요한 위젯입니다.
# QPushButton 클래스로 만들 수 있는데, 푸시 버튼과 함께 자주 쓰이는 메서드와 시그널을 아래 표에 정리했습니다. (QPushButton 공식 문서 참고)
# - 자주 쓰이는 메서드
# 메서드	설명
# setCheckable()	True 설정 시, 누른 상태와 그렇지 않은 상태를 구분합니다.
# toggle()	상태를 바꿉니다.
# setIcon()	버튼의 아이콘을 설정합니다.
# setEnabled()	False 설정 시, 버튼을 사용할 수 없습니다.
# isChecked()	버튼의 선택 여부를 반환합니다.
# setText()	버튼에 표시될 텍스트를 설정합니다.
# text()	버튼에 표시된 텍스트를 반환합니다.
# - 자주 쓰이는 시그널.
# 시그널	설명
# clicked()	버튼을 클릭할 때 발생합니다.
# pressed()	버튼이 눌렸을 때 발생합니다.
# released()	버튼을 눌렀다 뗄 때 발생합니다.
# toggled()	버튼의 상태가 바뀔 때 발생합니다.
# 이제 QPushButton 클래스를 이용해서 푸시 버튼을 만들어보겠습니다.
# 세 개의 다양한 푸시 버튼을 만들었습니다.
# 설명
# btn1 = QPushButton('&Button1', self)
# btn1.setCheckable(True)
# btn1.toggle()
# QPushButton 클래스로 푸시 버튼을 하나 만듭니다. 첫 번째 파라미터로는 버튼에 나타날 텍스트, 두 번째는 버튼이 속할 부모 클래스를 지정해줍니다.
# 버튼에 단축키(shortcut)를 지정하고 싶으면 아래와 같이 해당 문자 앞에 ampersand('&')를 넣어주면 됩니다. 이 버튼의 단축키는 'Alt+b'가 됩니다.
# setCheckable()을 True로 설정해주면, 선택되거나 선택되지 않은 상태를 유지할 수 있게 됩니다.
# toggle() 메서드를 호출하면 버튼의 상태가 바뀌게 됩니다. 따라서 이 버튼은 프로그램이 시작될 때 선택되어 있습니다.
# btn2 = QPushButton(self)
# btn2.setText('Button&2')
# setText() 메서드로도 버튼에 표시될 텍스트를 지정할 수 있습니다.
# 또한 이 버튼의 단축키는 'Alt+2'가 됩니다.
# btn3 = QPushButton('Button3', self)
# btn3.setEnabled(False)
# setEnabled()를 False로 설정하면, 버튼을 사용할 수 없게 됩니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()
        btn2 = QPushButton(self)
        btn2.setText('Button&2')
        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''



# [4.레이아웃 (Layout)]
# 레이아웃 (Layout)은 어플리케이션 창에 위젯들을 배치하는 방식입니다.
# 레이아웃 관리는 GUI 프로그래밍에서 매우 중요한 요소입니다.
# PyQt5의 위젯들을 배치하는 방식에는 절대적 배치, 박스 레이아웃, 그리드 레이아웃 방식이 있습니다.
# 예제를 통해 세 가지 방식에 대해 살펴보겠습니다

# (4-3.그리드 레이아웃)
# 가장 일반적인 레이아웃 클래스는 '그리드 레이아웃(grid layout)'입니다. 이 레이아웃 클래스는 위젯의 공간을 행 (row)과 열 (column)로 구분합니다.
# 그리드 레이아웃을 생성하기 위해 QGridLayout 클래스를 사용합니다.
# 그리드 레이아웃.
# 위 예시 다이얼로그의 경우, 세 개의 행(Row)과 다섯 개의 열(Column)로 구분되어 있고, 필요한 위치에 위젯을 배치했습니다.
# 세 개의 라벨, 두 개의 라인 에디터, 하나의 텍스트 에디터를 그리드 형태로 배치했습니다.
# 설명
# grid = QGridLayout()
# self.setLayout(grid)
# QGridLayout을 만들고, 어플리케이션 창의 레이아웃으로 설정합니다.
# grid.addWidget(QLabel('Title:'), 0, 0)
# grid.addWidget(QLabel('Author:'), 1, 0)
# grid.addWidget(QLabel('Review:'), 2, 0)
# addWidget() 메서드의 첫 번째 위젯은 추가할 위젯, 두, 세 번째 위젯은 각각 행과 열 번호를 입력합니다.
# 세 개의 라벨을 첫 번째 열에 수직으로 배치합니다.
# grid.addWidget(QTextEdit(), 2, 1)
# QTextEdit() 위젯은 QLineEdit() 위젯과 달리 여러 줄의 텍스트를 수정할 수 있는 위젯입니다. 세 번째 행, 두 번째 열에 배치합니다.
''' import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)
        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (4-2.박스 레이아웃)
# 박스 레이아웃 클래스를 이용하면 훨씬 유연하고 실용적인 레이아웃을 할 수 있습니다. (QBoxLayout 공식 문서 참고)
# QHBoxLayout, QVBoxLayout은 여러 위젯을 수평으로 정렬하는 레이아웃 클래스 입니다.
# QHBoxLayout, QVBoxLayout 생성자는 수평, 수직의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수도 있고 위젯을 배치할 수도 있습니다.
# 예제 코드에서 위젯의 가운데 아래 부분에 두 개의 버튼을 배치하기 위해 수평, 수직의 박스를 하나씩 사용합니다.
# 필요한 공간을 만들기 위해 addStretch() 메서드를 사용하고, 'stretch factor'를 조절해 보겠습니다.
# 창의 가운데 아래에 두 개의 버튼을 배치시킵니다.
# 두 개의 버튼은 창의 크기를 변화시켜도 같은 자리에 위치합니다.
# 설명
# okButton = QPushButton('OK')
# cancelButton = QPushButton('Cancel')
# 두 개의 버튼을 만들었습니다.
# hbox = QHBoxLayout()
# hbox.addStretch(1)
# hbox.addWidget(okButton)
# hbox.addWidget(cancelButton)
# hbox.addStretch(1)
# 수평 박스를 하나 만들고, 두 개의 버튼과 양 쪽에 빈 공간을 추가합니다.
# 이 addStretch() 메서드는 신축성있는 빈 공간을 제공합니다.
# 두 버튼 양쪽의 stretch factor가 1로 같기 때문에 이 두 빈 공간의 크기는 창의 크기가 변화해도 항상 같습니다.
# vbox = QVBoxLayout()
# vbox.addStretch(3)
# vbox.addLayout(hbox)
# vbox.addStretch(1)
# 다음으로 수평 박스(hbox)를 수직 박스(vbox)에 넣어줍니다.
# 수직 박스의 stretch factor는 수평 박스를 아래쪽으로 밀어내서 두 개의 버튼을 창의 아래쪽에 위치하도록 합니다.
# 이 때에도 수평 박스 위와 아래의 빈 공간의 크기는 항상 3:1을 유지합니다. stretch factor를 다양하게 바꿔보면, 의미를 잘 이해할 수 있습니다.
# self.setLayout(vbox)
# 최종적으로 수직 박스를 창의 메인 레이아웃으로 설정합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

# (4-1.절대적 배치)
# 절대적 배치(Absolute positioning) 방식은 각 위젯의 위치와 크기를 픽셀 단위로 설정해서 배치합니다.
# 절대 배치 방식을 사용할 때는 다음의 제약을 이해하고 있어야 합니다.
# 창의 크기를 조절해도 위젯의 크기와 위치는 변하지 않는다.
# 다양한 플랫폼에서 어플리케이션이 다르게 보일 수 있다.
# 어플리케이션의 폰트를 바꾸면 레이아웃이 망가질 수 있다.
# 레이아웃을 바꾸고 싶다면 완전히 새로 고쳐야 하며, 이는 매우 번거롭다.
# 두 개의 라벨과 두 개의 푸시버튼 위젯을 절대적 배치 방식으로 배치해 보겠습니다.
# 위젯의 위치를 설정하기 위해 move() 메서드를 사용합니다.
# 라벨(label1, label2)과 푸시버튼(btn1, btn2)의 x, y 좌표를 설정함으로써 위치를 조절합니다.
# 좌표계는 왼쪽 상단 모서리에서 시작합니다. x 좌표는 왼쪽에서 오른쪽으로 갈수록 커지고, y 좌표는 위에서 아래로 갈수록 커집니다.
# 설명
# label1 = QLabel('Label1', self)
# label1.move(20, 20)
# 라벨을 하나 만들고, x=20, y=20에 위치하도록 옮겨줍니다.
# btn1 = QPushButton('Button1', self)
# btn1.move(80, 13)
# 푸시버튼을 하나 만들고, x=80, y=13에 위치하도록 옮겨줍니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)
        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)
        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''



# [3.기초 (Basics)]
# (3-10.스타일 꾸미기)
# setStyleSheet()을 이용하면 어플리케이션 안의 다양한 구성 요소들의 스타일을 자유롭게 꾸밀 수 있습니다.
# 세 개의 라벨 위젯을 여러 스타일로 꾸밉니다.
# 설명
# lbl_red = QLabel('Red')
# lbl_green = QLabel('Green')
# lbl_blue = QLabel('Blue')
# QLabel 클래스를 이용해서 세 개의 라벨 위젯을 만듭니다.
# 라벨 텍스트는 각각 'Red', 'Green', 'Blue'로 설정합니다.
# lbl_red.setStyleSheet("color: red;"
#                       "border-style: solid;"
#                       "border-width: 2px;"
#                       "border-color: #FA8072;"
#                       "border-radius: 3px")
# setStyleSheet() 메서드를 이용해서 글자색을 빨간색(red)으로, 경계선을 실선(solid)으로, 경계선 두께를 2px로, 경계선 색을
# FA8072로, 경계선의 모서리를 3px만큼 둥글게 설정합니다.
# lbl_green.setStyleSheet("color: green;"
#                         "background-color: #7FFFD4")
# 마찬가지로, lbl_green 라벨의 글자색을 녹색(green)으로, 배경색을 7FFFD4로 설정합니다.
# lbl_blue.setStyleSheet("color: blue;"
#                        "background-color: #87CEFA;"
#                        "border-style: dashed;"
#                        "border-width: 3px;"
#                        "border-color: #1E90FF")
# lbl_blue 라벨의 글자색을 파란색(blue)으로, 배경색을 87CEFA으로, 경계선을 대쉬 스타일로, 경계선 두께를 3px로, 경계선 색을 1E90FF으로 설정합니다.
# vbox = QVBoxLayout()
# vbox.addWidget(lbl_red)
# vbox.addWidget(lbl_green)
# vbox.addWidget(lbl_blue)
# self.setLayout(vbox)
# 수직 박스 레이아웃(QVBoxLayout())을 이용해서 세 개의 라벨 위젯을 수직으로 배치합니다.
# 수직 박스 레이아웃에 대한 설명은 박스 레이아웃 페이지설명을 참고합니다.
# 더 다양한 스타일 항목은 스타일 시트 Reference 페이지 설명를 참고합니다.
''' import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')
        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)
        self.setLayout(vbox)
        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) '''

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
''' import sys
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
    sys.exit(app.exec_()) '''

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