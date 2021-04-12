# 출처 [https://wikidocs.net/book/2165, PyQt5 Tutorial 파이썬으로 만드는 나만의 GUI 프로그램]

# [기초 (Basics)]
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
    sys.exit(app.exec_())

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
      self.setWindowIcon(QIcon('web.png'))
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