# 출처 [http://pythonstudy.xyz/, 예제로 배우는 파이썬 프로그래밍]


# [목차]

# [Python 기초]
# Python 소개
# Python 설치
# Python 시작하기
# Python 간단한 프로그램
# Python 편집기
# Python 코딩의 기초
# 기본 데이타 타입
# 연산자
# 문자열과 바이트
# 조건문
# 반복문
# 컬렉션: List
# 컬렉션: Tuple
# 컬렉션: Dictionary
# 컬렉션: Set
# 함수
# 모듈 (Module)
# 패키지
# 클래스
# 예외처리
# 유닛 테스트
# Python Comprehension
# Iterator와 Generator
# 쓰레드 (Thread)

# [Python 데이타]
# Python DB API
# MySQL 쿼리
# MySQL DML
# SQLite 사용
# MSSQL 사용
# JSON 데이타
# 파일 데이타 처리
# CSV 파일 사용하기

# [Python 활용]
# 정규 표현식 Regex
# numpy 사용하기
# 파이썬 Web Scraping
# 파이썬 Selenium 사용하기
# 파이썬 엑셀 사용하기
# Matplotlib 차트/플롯 그리기
# pandas 데이타 분석
# 파이썬 이미지 처리 (Pillow)
# 파이썬 영상 처리 (OpenCV)
# 파이썬에서 SSH 클라이언트 사용

# [Python 팁]
# Python Tools for Visual Studio
# 기존 Python코드를 VS 프로젝트로
# Visual Studio Code 사용
# pip 패키지 관리자
# Python 디버깅 (PDB)
# 파이썬 가상환경
# 파일과 디렉토리
# 메일 보내기 (SMTP)
# 난수 (random)
# 직렬화와 역직렬화
# 파이썬 코딩 스타일
# 파이썬 Object Interning
# 아나콘다 (Anaconda)
# Jupyter Notebook
# 정수 / HexString 변환
# 문자열/바이트배열 변환


# [Python 기초]

# [Python 소개]
# 1. Python 언어
# 파이썬 (Python)은 범용 프로그래밍 언어로서 코드 가독성(readability)와 간결한 코딩을 강조한 언어이다.
# 파이썬은 인터프리터(interpreter) 언어로서, 리눅스, Mac OS X, 윈도우즈 등 다양한 시스템에 널리 사용된다.
# Python은 원래 그리스 신화에서 그리스 중부 델파이를 지배하였던 큰 뱀인데, 제우스의 아들 아폴로에 의해 화살을 맞고 죽게된다.
# 2. Python의 간단한 역사
# Python은 1989년 12월 네델란드 개발자 Guido van Rossum 에 의해 개발되기 시작하여, 약 1년 간 개발하여 1991년 처음 Python 0.9 버전을 세상에
# 내놓았다. 그후 정식 Python 1.0 버젼은 1994년에 출시되었으며, Python 2.0은 2000년에, Python 3.0은 2008년에 각각 출시되었다.
# Guido van RossumGuido van Rossum 1956년 생의 네델란드 개발자로서 Python 창시자. 네델란드 CWI, 미국 NIST 등의 여러 연구소에서 근무하였으며, 
# 구글에서 약 7년간 근무, 현재는 Dropbox에서 일하고 있다.
# Python이 구글에서 상당히 많은 프로젝트에 쓰여지고 있다는 점과 Dropbox의 많은 코드가 Python으로 작성되었다는 점은 아마 우연이 아닐 것이다.
# Guido는 파이썬의 개발 동기에 대해 이렇게 말하고 있다.
# "약 6년 전인 1989년 12월, 크리스마스를 전후하여 취미로 만들어 볼 프로그래밍 프로젝트를 찾고 있었죠. 그 때 사무실은 잠겨있어지만, 집에
# 컴퓨터가 있었고, 뭐 특별히 할 일도 없었죠. 그래서 그 때 당시 한동안 생각하고 있었던 새 스크립트 언어에 대한 인터프리터를 만들어 보기로 했죠.
# 유닉스/C 해커들에게 어필할 수 있는, ABC 언어로부터 파생된 언어말이죠. 나는 그 프로젝트명으로 Python이라는 이름을 선택했는데, 그 당시 약간은 
# 불손한 기분이 들어서이기도 했고, 또한 당시 Monty Python's Flying Circus(BBC 코메디)에 열성팬이기도 하여..."
# - 1996, Guido

# [Python 설치]
# Python은 윈도우즈, Mac, 리눅스 등에 설치하여 사용할 수 있다. 다음은 각 OS별 간단한 설치 방법을 설명한 것이다. 널리 사용되는 Python 버젼으로,
# 실무에서 많이 사용되었던 Python 2 버전 (예: v2.7)과 새로운 기능을 계속 업그레이드하고 있는 Python 3 버전 (예: v3.7)이 있는데, 이 두 버전 간의
# 호환성 문제가 존재한다. 여기서는 Python 3 버전를 사용한다.
# 1. 윈도우즈에서 Python 설치
# 브라우저에서 https://www.python.org/downloads/ 방문
# 윈도우즈용 Python 3 버젼 다운 받아 설치
# 설치마법사에서 Custom 설치를 선택, 옵션에서 "Python 경로 환경변수에 추가"를 선택하면 편리
# 2. Mac OSX에서 Python 설치
# 브라우저에서 https://www.python.org/downloads/ 방문
# Mac 용 Python 3 버젼 패키지 다운
# 패키지를 오픈해서 설치
# Python 실행파일 경로는 PATH에 자동으로 추가된다(.bash_profile)
# 3. Linux에서 Python 설치 (Centos)
# 리눅스 설치 방법은 여러 방법이 있는데, 아래는 이중 한 예로 Centos 7에서 수작업으로 최신 버젼을 다운받아 설치하는 예이다.
# 아래 URL에서 압축파일 다운로드
# $ wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
# 압축해제
# $ tar xf Python-3.5.1.tar.xz
# 빌드
# $ cd ./Python-3.5.1
# $ ./configure   #빌드 준비
# $ make          #빌드
# 설치: 디폴트로 설치된 2.7버젼과 병행하여 사용하기 위해, 아래와 같이 make install (기존 2.7을 덮어씀) 대신 make altinstall을 사용한다.
# $ make altinstall   
# 실행 테스트
# $ python3.5

# [Python 시작하기]
# Python 시작하기
# 파이썬 설치가 끝났으면, Python을 실행하고 간단한 테스트를 실행해 보자.
# 1. 윈도우즈에서 Python 실행
# 윈도우즈에서 Python을 실행하기 위해서는, [시작] - [프로그램] - [Python 3.5]에서 "Python 3.5 (32bit)" 콘솔프로그램 혹은
# "IDLE (Python 3.5 32-bit)" 윈도우 프로그램을 실행한다. 이 프로그램들은 흔히 대화형 인터프리터 혹은 Python Shell 이라고 불리운다.
# 아래는 "Python 3.5 (32bit)" 프로그램을 실행한 예인데, str이라는 변수에 Hello World를 넣고, 이를 프린트하는 예제이다.
# 여기서 처음 나오는 >>> 는 Python 인터프리터의 프롬프트(Prompt)로서 사용자 입력을 기다리는 표시이다. 이 프롬프트에 입력된 문장들은 파이썬 
# 인터프리터가 해석하고 실행하게 되고, 결과를 출력해 주게 된다. 이렇게 사용자로부터 입력을 받아 (Read), 문장을 즉시 해석하고 평가하며 
# (Evaluate), 그 출력 결과를 표시한 후(Print), 다시 프롬프트로 돌아가는 (Loop) 프로그램을 흔히 REPL 툴이라 부른다.
# Python을 마치고 빠져나오기 위해서는 윈도우즈에서 Ctrl+Z를 사용한다 (Mac 혹은 리눅스는 Ctrl+D를 사용한다). OS와 상관없이 종료하기 위해서는
# 프롬프트에서 exit() 을 사용할 수 있다.
# 2. Mac에서 Python 실행
# Mac에서 Python을 실행하기 위해서는, 터미널(Terminal) 프로그램을 실행하고, "python3.5"를 실행한다. 실행파일에 대한 PATH는 설치시 .bash_profile에
# 설정된다. Mac에는 python 2.7이 Built-in 되어 있으며, "python"을 실행하면 2.7 버전이 실행된다.
# 3. 리눅스에서 Python 실행
# 리눅스에서 Python을 실행하기 위해서는 프롬프트에서 "python3.5"를 실행한다. 리눅스에 python 2.7이 Built-in 되어 있는 경우, "python"을 실행하면
# 2.7 버전이 실행된다. (단, 설치에서 설명하였듯이, 2.7 버전을 Overwrite하여 인스톨하지 않은 경우)

# [Python 간단한 프로그램]
# Python 간단한 프로그램 작성
# 일반적으로 실제 파이썬으로 프로그래밍을 하기 위해서는 대화형 인터프리터를 사용하지 않고, 여러 종류의 에디터를 사용하여 파이썬 프로그램 파일을
# 작성한 후 이를 실행하게 된다.
# 우선 Notepad와 같은 간단한 에디터로 다음과 같은 코드를 작성하고 이를 test.py 파일로 저장해 보자. 파이썬 프로그램 파일은 관례적으로 .py 확장자를
# 사용한다.
# a = 1
# b = 2
# c = a + b
# print(c)
# 파이썬 파일 test.py를 실행하기 위해서는 python.exe 뒤에 해당 파이썬 파일을 주고 다음과 같이 실행하게 된다.
# C:\Test> python test.py
# 3
''' a = 1
b = 2
c = a + b
print(c) '''

# [Python 편집기]
# Python 편집기/IDE 소개
# 파이썬 프로그래밍을 보다 편리하게 하기 위하여 파이썬 전용 에디터 혹은 IDE를 설치하여 사용할 수 있다. 파이썬 편집기/IDE로는 PyCharm, 
# Visual Studio Code, Eclipse/PyDev, Eric, Python Tools for Visual Studio, Komodo, Atom 등 매우 다양한 툴들이 있는데, 여기서는 
# Cross Platform에서 동작하면서 많이 사용되는 JetBrains의 PyCharm를 사용해 보자. 참고로 윈도우즈 Visual Studio에 익숙한 개발자는 
# Python Tools for Visual Studio 를 사용하면 편리하다.
# PyCharm을 설치하기 위해서는 https://www.jetbrains.com/pycharm/download 에서 PyCharm Community Edition을 다운받아 설치한다.
# 설치후에 PyCharm을 실행하고, [Create New Project]를 선택한다. 새 프로젝트 위치를 지정한다.
# [File] -> [New...] -> [Python File]을 선택한다. 파일명(예: test.py)를 적고 새 파일을 생성한다.
# 에디터에 코드를 쓰고, 저장한다. 오른쪽 마우스 버튼을 누르고 [Run] 메뉴를 선택한다.

# [Python 코딩의 기초]
# 1. 코딩블럭 들여쓰기 (Identation)
# 파이썬은 코딩블럭을 표시하기 위해 들여쓰기(Identation)를 사용한다. 이는 보통 Curly Bracket ({...})을 사용하는 C,C#,Java 등의 다른 언어들과는
# 매우 다른 독특한 스타일이다. 코딩블럭을 시작하는 문장들 예를 들어 if, for, def 문들의 끝에는 아래 예제에서 보듯이, 콜론(:)을 사용하고 
# 내부의 코딩블럭은 동일한 들여쓰기를 사용한다.
# 일반적으로 들여쓰기에는 4개의 공백을 사용할 것을 권장하는데, 동일한 블럭의 들여쓰기는 모두 동일한 수의 공백을 사용해야 한다. 즉, 모두 4개의
# 공백을 사용하다가 하나만 5개의 공백을 사용하면, IndentationError: unexpected indent라는 에러가 발생한다. 이는 파이썬 컴파일러가 올바른 
# 들여쓰기를 강제하는 것으로, 코드를 일관되고 명료하게 하기 위함이다. 또한 추가로 한가지 주의할 점은 공백과 탭을 혼용해서 사용하지 말아야 
# 한다는 것이다.
# 2. 파이썬 표준 라이브러리
# 파이썬은 상당히 많은 표준 라이브러리들을 제공하고 있는데, 이 표준 라이브러리를 불러다 쓰기 위해서는 import문을 사용한다. 예를 들어, 표준
# 라이브러리 중의 하나인 math에 있는 sqrt()라는 함수를 불러다 쓰기 위해서는, 아래 예제와 같이 "import math" 를 실행하고, math.sqrt() 함수를 
# 호출하면 된다.
# import math
# n = math.sqrt(9.0)
# print(n)   # 3.0 출력
# 3. 코멘트
# 파이썬에서 코멘트를 표시하기 위하여 파운드(#) 사인을 사용한다. 코멘트는 라인의 처음에 올 수도 있고, 라인의 문장이 끝난 부분에 올 수도 있다. 
# 표준 코딩 스타일에서는 # 사인 뒤에 하나의 공백을 두는 것을 권장한다.
# # 코멘트1
# run(1) 
# run(2) # 코멘트2
# 4. PEP
# PEP 이란 Python Enhancement Proposals 의 약자로서 파이썬을 개선하기 위한 제안서를 의미한다. 이러한 PEP은 다음과 같이 크게 3 종류로 구분할
# 수 있으며, Python Software Foundation의 공식 웹사이트인 python.org 에서 관리한다.
# 파이썬에 새로운 기능(Feature)을 추가하거나 구현 방식을 제안하는 Standard Track PEP
# 파이썬 디자인 이슈를 설명하거나 일반적인 가이드라인 혹은 정보를 커뮤니티에 제공하는 Informational PEP
# 파이썬을 둘러싼 프로세스를 설명하거나 프로세스 개선을 제안하는 Process PEP. 예를 들어, 프로세스 절차, 가이드라인, 의사결정 방식의 개선,
# 파이썬 개발 도구 및 환경의 변경 등등.
# PEP은 파이썬 언어 자체 뿐만 아니라 코딩 표준, 커뮤니티 이슈 등을 담고 있는 유용한 자료이므로 파이썬을 배우면서 자주 참고하면 좋다. 
# PEP은 각 문서마다 번호가 지정되어 있는데, PEP 번호별 내용은 https://www.python.org/dev/peps/ 에서 찾아 볼 수 있다.
# 특히, 파인썬 코딩과 관련한 코딩 표준(Coding Convention)에 관한 문서는 PEP 8 (https://www.python.org/dev/peps/pep-0008) 에 정의되어 있는데,
# 파이썬의 기초를 익힌 후 참조하면 파이썬 코딩 스타일을 익히는데 도움이 된다.
''' import math
n = math.sqrt(9.0)
print(n)   # 3.0 출력 '''

# [기본 데이타 타입]
# 1. Python 기본 데이타 타입
# 파이썬에 사용되는 기본 데이타 타입(Scalar Data Type)에는 아래와 같은 타입들이 있다.
# 타입	설명	표현 예
# int	정수형 데이타	100, 0xFF (16진수), 0o56 (8진수)
# float	소숫점을 포함한 실수	a = 10.25
# bool	참, 거짓을 표현하는 부울린	a = True
# None	Null과 같은 표현	a = None
# 정수형은 소숫점을 갖지 않는 정수를 갖는 데이타 타입이며, float는 소숫점을 갖는 데이타 타입이다. bool 타입은 True 혹은 False 만을 갖는
# 타입이고, None은 아무 데이타를 갖지 않는다는 것을 표현하는 것으로 타 언어의 Null과 같은 개념이다. 정수형에 리터럴 데이타를 넣을 때, 
# 10진수 이외에 16진수 혹은 8진수를 위의 예와 같이 사용할 수 있다.
# 리터럴 데이타를 특정 타입으로 변경하기 위하여 int(), float(), bool() 등과 같은 타입 생성자를 사용할 수 있다. 예를 들어, int(3.5)는 
# float 데이타를 정수형으로 변경하여 정수값 3 을 리턴한다. float("1.6")은 float형 1.6을 리턴한다.
# int(3.5)      # 3
# 2e3           # 2000.0
# float("1.6")  # 1.6
# float("inf")  # 무한대
# float("-inf") # -무한대
# bool(0)       # False. 숫자에서 0만 False임,
# bool(-1)      # True
# bool("False") # True
# a = None      # a는 None
# a is None     # a가 None 이므로 True
# 위의 예제에서 리터럴 2e3 (혹은 2E3 도 같은 표현)은 2 * (10 ** 3)과 같은 표현이다. 또한, bool 타입은 숫자의 경우 0 만이 거짓이 되고, 
# 0이 아니면 참이 된다. bool() 안에 문자형이나 컬렉션 타입들이 있을 경우 비어있으면 거짓이 되고 값이 있으면 참이된다. 즉, 위의 마지막 
# 예인 bool("False")는 문자열이 비어있지 않으므로 참이 된다.
# 2. 복소수
# 파이썬은 복소수 타입을 지원하는데, 복소수는 a+bj 와 같이 표현된다 (수학에서 복소수를 표현할 때 i 를 사용하지만 파이썬에서는 j 를 사용한다). 
# 실수부의 값을 얻기 위해서는 복소수 변수명.real을, 허수부의 값을 얻기 위해선 변수명.imag 를 사용한다.
# v = 2 + 3j
# v.real  # 2
# v.imag  # 3
''' v = 2 + 3j
print(v.real)  # 2
print(v.imag)  # 3 '''

# [연산자]
# 연산자
# 파이썬은 산술연산자, 비교연산자, 할당연산자, 논리연산자, Bitwise 연산자, 멤버쉽연산자, Identity연산자를 지원한다.
# 1. 산술연산자
# 산술연산자에는 (1) 사칙연산자 +, -, *, / 와 (2) 제곱을 나타내는 **, (3) 나머지를 산출하는 % (Modulus), 그리고 (4) 나누기에 소숫점 이하를
# 버리는 // 연산자(Floor Division) 등이 있다.
# 5 % 2   # 1
# 5 // 2  # 2
# 2. 비교연산자
# 비교연산자는 관계연산자로도 불리우는데, 여기에는 등호(==), 같지 않음(!=), 부등호(<, >, <=, >=) 등이 있다.
# if a != 1:
#    print("1이 아님")
# 3. 할당연산자
# 할당연산자는 변수에 값을 할당하기 위하여 사용되는데, 기본적으로 = (Equal Sign)을 사용한다. 산술연산자와 함께 사용되어 할당을 보다 간결히
# 하기 위해 사용되는 +=, -=, *=, /=, %=, //= 등과 같은 연산자도 할당연산자에 해당된다.
# a = a * 10
# a *= 10     # 위와 동일한 표현
# 4. 논리연산자
# 논리연산자에는 and, or, not 이 있는데, and 는 양쪽의 값이 모두 참인 경우만 참이 되고, or 는 어느 한쪽만 참이면 참이된다. not 은 참이면 
# 거짓으로 거짓이면 참이 된다. 아래 예제는 No가 출력된다.
# x = True
# y = False
# if x and y:
#     print("Yes")
# else:
#     print("No")
# 5. Bitwise 연산자
# Bitwise연산자에는 & (AND), | (OR), ^ (XOR), ~ (Complement), <<, >> (Shift)가 있는데, 이 연산자는 비트단위의 연산을 하는데 사용된다.
# a = 8     # 0000 1000
# b = 11    # 0000 1011
# c = a & b # 0000 1000  (8)
# d = a ^ b # 0000 0011  (3)
# print(c)
# print(d)
# 6. 멤버쉽 연산자
# 멤버쉽연산자에는 in, not in 이 있는데, 이는 좌측 Operand가 우측 컬렉션에 속해 있는지 아닌지를 체크한다.
# a = [1,2,3,4]
# b = 3 in a    # True
# print(b)
# 6. Identity 연산자
# Identity연산자에는 is, is not 이 있는데, 이는 양쪽 Operand가 동일한 Object를 가리키는지 아닌지를 체크한다.
# a = "ABC"
# b = a
# print(a is b)  # True
''' a = 0
if a != 1:
   print("1이 아님")
x = True
y = False
if x and y:
    print("Yes")
else:
    print("No")
a = 8     # 0000 1000
b = 11    # 0000 1011
c = a & b # 0000 1000  (8)
d = a ^ b # 0000 0011  (3)
print(c)
print(d)
a = [1,2,3,4]
b = 3 in a    # True
print(b)
a = "ABC"
b = a
print(a is b)  # True '''

# [문자열과 바이트]
# 1. 문자열
# 파이썬에서 문자열은 단일인용부호(') 혹은 이중인용부호(") 를 사용하여 표현한다.
# 예를 들어, 아래 표현은 s 라는 변수에 가나다 라는 문자열을 할당하는 것으로 동일한 표현이다.
# s = '가나다'
# s = "가나다"
# 만약 여러 라인에 걸쳐 있는 문자열을 표현하고 싶다면, ''' ''' 또는 """ """"처럼 3개의 인용부호를 사용한다.
# s = """아리랑
# 아리랑
# 아라리요
# """
# print(s)
# 복수 라인 문자열을 한 라인으로 표현하고 싶다면, Escape Sequence (\n)를 사용하면 된다. 즉, 다음 표현은 위와 동일한 표현이다.
# 실제 리눅스나 Mac OS에서는 Newline이 \n으로 표현되지만, 윈도우즈에서 \r\n을 사용한다. 하지만, 파이썬에서는 Universal Newline이 지원되어 
# 모든 OS에서 공히 \n을 사용한다.
# s = '아리랑\n아리랑\n아라리요'
# print(s)
# 물론 문자열에서 사용되는 Escape Sequence에는 타 언어와 비슷하게 여러 가지를 사용할 수 있다. 예를 들어 탭은 \t, 이중따옴표는 \", 백슬래쉬는
# \\ 등과 같이 표현한다.
# 문자열 포맷팅
# 일정한 포맷에 맞춰 문자열을 조합하는 것을 문자열 포맷팅이라하는데, 문자열 포맷 템플릿 안에 대입값이 들어갈 자리를 지정해 두고 나중에 그 값을
# 채워 넣는 방식이다. 예를 들어, "답: %s" % "A" 와 같은 표현에서 % 앞 부분은 포맷 템플릿이고, % 뒤는 실제 대입할 값이다. 이때 % 를 포맷팅 
# 연산자 (Formatting Operator)라 부른다. % 앞뒤로 각각 하나의 값만을 받아들이므로 만약 % 뒤의 값이 복수 개이면 튜플로 묶어주어야 한다.
# p = "이름: %s 나이: %d" % ("김유신", 65)
# print(p)
# # 출력: 이름: 김유신 나이: 65
# p = "X = %0.3f, Y = %10.2f" % (3.141592, 3.141592)
# print(p)
# # 출력: X = 3.142, Y =       3.14
# % (Formatting Operator) 앞의 포맷 템플릿에는 %s, %d 등과 같이 대입값 형식을 지정해 주는데 이를 변환 지시어(Conversion Specifier)라 부른다. 
# 아래 표는 Conversion Specifier 들의 의미를 설명한 것이다.
# Conversion Specifier	의미
# %s	문자열 (파이썬 객체를 str()을 사용하여 변환)
# %r	문자열 (파이썬 객체를 repr()을 사용하여 변환)
# %c	문자(char)
# %d 또는 %i	정수 (int)
# %f 또는 %F	부동소수 (float) (%f 소문자 / %F 대문자)
# %e 또는 %E	지수형 부동소수 (소문자 / 대문자)
# %g 또는 %G	일반형: 값에 따라 %e 혹은 %f 사용 (소문자 / 대문자)
# %o 또는 %O	8진수 (소문자 / 대문자)
# %x 또는 %X	16진수 (소문자 / 대문자)
# %%	% 퍼센트 리터럴
# Conversion Specifier는 % 와 Conversion 문자(예: s, d, f) 사이에 전체 자릿수와 소숫점 뒤자리수를 지정할 수 있다. 예를 들어 %10.2f 는 전체
# 10자리이고 값이 적으면 앞에 빈칸을 채우게 되고, .2 는 소수점 2째 자리까지만 표시한다는 것을 의미한다. 만약 %-10.2f 처럼 마이너스로 표현하면
# 전체 10자리인데 왼쪽으로 정렬한다는 의미이다.
# 2. str (문자열 클래스)
# 문자열은 내부적으로 str 이라는 클래스 타입인데, 파이썬의 문자열은 기본적으로 유니코드이고, 한번 설정되면 다시 변경시킬 수 없는 Immutable 
# 타입이다.
# 문자열은 인덱스를 사용하여 문자열 중 특정위치의 문자를 표현할 수 있다. 인덱스는 0로부터 시작하는데, 문자열 s 에 대하여 첫번째 문자는 s[0], 
# 두번째 문자는 s[1] 과 같이 표현된다.
# s = "ABC"
# type(s)      # class 'str'
# v = s[1]     # B
# type(s[1])   # class 'str'
# 파이썬에는 C, C# 등에서 존재하는 문자(char) 타입이 존재하지 않는다. 따라서, 위의 예에서 s[1]의 타입이 char가 아닌 문자열 str 타입이 된다.
# 참고로 type(변수명)은 해당 변수의 타입을 리턴한다.
# 문자열을 표현할 때, r'문자열' 과 같이 사용하면, 이는 Escape Sequence를 표현하지 않고 Raw String을 직접 사용한다는 것을 의미한다. 예를 들어, 
# 윈도우즈에서 파일경로를 간략히 표현하기 위해 아래와 같이 Raw String 표현을 사용할 수 있다.
# path = r'C:\Temp\test.csv'
# print(path)
# 3. 자주 사용되는 str 메서드
# 문자열 str 클래스에는 여러 유용한 메서드들이 제공되고 있는데, 이 중 흔히 사용되는 몇가지만 소개한다.
# str.join()
# 우선 여러 개의 문자열을 하나로 결합하는 join() 메서드가 있는데, join() 메서드는 문자열을 결합하는데 사용되는 Separator를 join 메서드 앞에
# 사용한다. 아래 예제에 보듯이, 콤마를 사용하여 문자열 리스트 요소들을 결합할 수도 있으며, 또한 빈 문자열을 사용하여 문자열들을 결합하는 
# 방법도 자주 사용된다.
# s = ','.join(['가나','다라','마바'])
# print(s)
# # 출력: 가나,다라,마바
# s = ''.join(['가나','다라','마바'])
# print(s)
# # 출력 : 가나다라마바
# str.split()
# split() 메서드는 join() 메서드의 반대로서 특정 separator를 기준으로 문자열을 분리하여 리스트를 리턴한다. 아래 예제에서 split() 메서드는 
# 하나의 문자열을 콤마로 분리해서 3개의 요소를 갖는 리스트를 리턴한다.
# items = '가나,다라,마바'.split(',')
# print(items)
# # 출력 : ['가나', '다라', '마바']
# str.partition()
# partition() 메서드는 문자열을 partition() 메서드의 첫번째 파라미터로 분리하여 그 앞부분(prefix), partition 분리자(separator), 뒷부분
# (suffix) 등 3개의 값을 Tuple로 리턴한다. 아래 예제는 Dash (-) 로 문자열을 분리하여 3개의 값을 리턴하는 코드이다. 일반적으로 separator는
# 사용하지 않아서 _ 를 사용하였다.
# departure, _, arrival = "Seattle-Seoul".partition('-')
# print(departure)
# # 출력 : Seattle
# str.format()
# 마지막으로 str 클래스에서 가장 많이 사용되는 메서드 중의 하나로 format() 메소드를 들 수 있다. format() 메서드는 다양한 방식의 문자열 포맷팅을
# 지원하는데, 아래는 흔히 사용되는 3가지 방식을 예시하고 있다. 먼저 위치를 기준으로한 포맷팅은 {0},{1},... 등의 필드들을 format() 파라미터들의
# 순서대로 치환하게 된다. 두번째 필드명을 기준으로 한 포맷팅은 {name}, {age}와 같이 임의의 필드명을 지정하고 format() 파라미터에 이들 필드명을 
# 사용하여 값을 지정하는 것이다. 그리고 세번째 인덱스 및 키 사용 방식은 Python 오브젝트가 format()의 파라미터로 지정되고, 포맷에서 이 오브젝트의 
# 인덱스(컬렉션의 경우) 혹은 속성, 키 등을 이용하는 것이다.
# # 위치를 기준으로 한 포맷팅
# s = "Name: {0}, Age: {1}".format("강정수", 30)
# print(s)  #출력: Name: 강정수, Age: 30
# # 필드명을 기준으로 한 포맷팅
# s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
# print(s) #출력: Name: 강정수, Age: 30
# # object의 인덱스 혹은 키를 사용하여 포맷팅
# area = (10, 20)
# s = "width: {x[0]}, height: {x[1]}".format(x = area)
# print(s) #출력: width: 10, height: 20
# 4. bytes (바이트 클래스)
# bytes 클래스는 일련의 바이트들을 표현하는 클래스로서 bytes는 한번 설정되면 다시 변경할 수 없는 Immutable 타입이다. bytes 클래스와 비슷한 
# 클래스로 bytearray 클래스가 있는데, 차이점은 bytearray는 바이트 객체의 요소를 변경할 수 있는 Mutable 타입이라는 점이다.
# 문자들을 바이트들로 표현하기 위해 b'문자들'과 같이 접두어 b를 앞에 붙인다. 이렇게 접두어 b를 붙여 바이트 리터럴을 만들때, 각 문자는 
# ASCII 코드를 갖는 문자로 처리된다.
# str 타입의 문자열을 bytes 타입의 바이트들로 변경하기 위해 str 클래스의 인코딩 메서드 encode()를 사용한다. 반대로 bytes 타입의 바이트 
# 객체을 str 타입의 문자열로 변경하기 위해 bytes 클래스의 디코딩 메서드 decode()를 사용한다. encode(), decode() 를 사용하여 문자열과 
# 바이트들 간의 인코딩/디코딩을 할 때, 특별히 파라미터를 지정하지 않으면 디폴트 인코딩을 사용하지만, 필요시 어떤 인코딩 방식을 사용할 
# 지를 지정할 수 있다. 예를 들어, encode("UTF-8")과 같이 UTF8 인코딩 방식을 사용하도록 지정할 수 있다.
# s = "Hello"
# b = s.encode()
# print(b)    # b'Hello'
# s2 = b.decode()  
# print(s2)   # 'Hello'
# # 특정 인코딩 방식을 지정한 경우
# x = "안녕".encode("UTF-8")
# y= x.decode("UTF-8")
# 문자열 안에서 유니코드값을 사용하려면, \u 에 이어 유니코드값을 적으면 된다. 아래 예제는 문자열 s1을 UTF-8 인코딩을 사용하여 바이트들로
# 변경하고, 이를 다시 문자열로 디코딩하는 예제이다.
''' s = """아리랑
아리랑
아라리요
"""
print(s)
s = '아리랑\n아리랑\n아라리요'
print(s)
p = "이름: %s 나이: %d" % ("김유신", 65)
print(p)
p = "X = %0.3f, Y = %10.2f" % (3.141592, 3.141592)
print(p)
s = "ABC"
type(s)      # class 'str'
v = s[1]     # B
type(s[1])   # class 'str'
path = r'C:\Temp\test.csv'
print(path)
s = ','.join(['가나','다라','마바'])
print(s)
s = ''.join(['가나','다라','마바'])
print(s)
items = '가나,다라,마바'.split(',')
print(items)
departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)
s = "Name: {0}, Age: {1}".format("강정수", 30)
print(s)  #출력: Name: 강정수, Age: 30
s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
print(s) #출력: Name: 강정수, Age: 30
area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s) #출력: width: 10, height: 20
s = "Hello"
b = s.encode()
print(b)    # b'Hello'
s2 = b.decode()  
print(s2)   # 'Hello'
x = "안녕".encode("UTF-8")
print(x)
y= x.decode("UTF-8")
print(y) '''

# [조건문]
# 조건문 : if
# 파이썬에서 조건문을 사용하기 위하여 if 문을 사용한다. if 키워드 다음에 조건식을 적게 되고, 조건식 다음에 콜론(:) 을 써서 if 조건식 끝을 
# 표현한다 (if문은 한 라인에 모두 쓸 수 있으므로 문법상 조건식 뒤에 콜론 사용).
# if x < 10:
#     print(x)
#     print("한자리수")
# # 한 라인에서 표현된 if 문 
# if x < 100:  print(x)
# if 문 조건식이 참이 아닐 때, 다음 if 문을 체크하기 위해서 elif 문을 사용할 수 있고, 모든 if 문이 거짓일 때 else 문 블럭을 실행할 수 있다. 
# 아래 예제는 if...elif...else 를 모두 사용한 예이다. 파이썬에는 다른 언어에 있는 switch 문이 존재하지 않으므로, switch 문 기능은 
# if...elif...elif... 문으로 수행한다.
# x = 10
# if x < 10:
#     print("한자리수")
# elif x < 100:
#     print("두자리수")
# else:
#     print("세자리 이상")
# if 조건문 안에서 특정 블럭/문장을 수행하지 않고 그냥 Skip하기 위하여 pass 라는 키워드를 사용할 수 있다. 아래 예제는 n 이 10보다 작은 경우는
# 아무 문장도 실행하지 않고 지나가고, 10보다 크거나 같을 때는 n 값을 출력한다.
''' n=5
if n < 10:
    pass
else:
    print(n)
x=7
if x < 10:
    print(x)
    print("한자리수")
if x < 10:  print(x)
if x < 10:
    print("한자리수")
elif x < 100:
    print("두자리수")
else:
    print("세자리 이상")
if n < 10:
    pass
else:
    print(n) '''

# [반복문]
# 1. 반복문 : while
# 파이썬에서 반복되는 루프를 만들기 위해 while 문이나 for 문을 사용할 수 있다. 먼저 while문은 while 키워드 다음의 조건식이 참일 경우 계속
# while 안의 블력을 실행한다. 예를 들어, 아래의 예제를 보면 while의 조건식은 i가 10보다 작거나 같은 경우인데, i 값이 이 조건하에 있으면 
# 계속 루프를 돌게 된다. 따라서, 아래 예제는 1부터 10까지 값을 출력하게 된다.
# i=1
# while i <= 10:
#     print(i)
#     i += 1
# 2. 반복문 : for
# 반복문 for는 C#, Java 에서의 foreach 와 비슷한 것으로, 컬렉션으로부터 하나씩 요소(element)를 가져와, 루프 내의 문장들을 실행하는 것이다. 
# 리스트, Tuple, 문자열 등의 컬렉션은 "for 요소변수 in 컬렉션" 형식에서 in 뒤에 놓게 된다.
# 아래 예제는 0부터 10까지를 더하는 코드이다. 파이썬 내장함수인 range(n) 함수는 0 부터 n-1 까지의 숫자를 갖는 리스트를 리턴한다. for 루프는
# 이 리스트 컬렉션으로부터 요소를 하나씩 가져와서 for 블럭의 문장을 실행하게 된다.
# sum = 0
# for i in range(11):
#     sum += i
# print(sum)
# 아래 예제는 문자열 요소를 갖는 리스트로부터 각 문자열들을 순차적으로 출력하는 예이다.
# list = ["This", "is", "a", "book"]
# for s in list:
#     print(s)
# for 루프는 이 밖에도 리스트 안에 내포되어 사용될 수도 있는데, 이는 리스트 컬렉션 편에서 자세히 설명한다.
# 3. break / continue
# 반복문 안에서 루프를 빠져나오기 위해 break 문을 사용할 수 있다. 또한, continue문을 사용하면 루프 블럭의 나머지 문장들을 실행하지 않고 
# 다음 루프로 직접 돌아가게 할 수 있다. 아래 예제는 break와 continue문을 사용 예시를 위한 것으로, i가 5인 경우는 continue가 실행되어 직접
# 다시 while문으로 이동하여 밑의 합계에 포함되지 않는다. 또한, i가 10보다 큰 경우 while 루프를 빠져나오게 된다. 따라서, 이 예제는 1부터 
# 10까지 합을 구하는데, 5인 경우만 제외한 값 즉 50을 출력한다.
# i = 0
# sum = 0
# while True:
#     i += 1
#     if i == 5:
#         continue
#     if i > 10:
#         break
#     sum += i
# print(sum)
# 4. range
# 반복문과 직접적인 연관은 없지만, 흔히 반복문과 연동되어 많이 사용되는 range에 대해 간략히 소개한다. range() 함수는 보통 아래와 같이
# 1~3개의 파라미터를 갖는데, 파라미터는 파라미터 갯수에 따라 아래와 같이 다른 의미를 갖는다.
# 예제	파라미터 의미	리턴값
# range(3)	Stop	0, 1, 2
# range(3,6)	Start, Stop	3, 4, 5
# range(2,11,2)	Start, Stop, Step	2, 4, 6, 8, 10
# numbers = range(2, 11, 2)
# for x in numbers:
#     print(x)
# # 출력: 각 라인에 2 4 6 8 10 출력
# 특히, for 반복문에서 몇 번 루프를 도는가를 표시하기 위해 range() 함수를 종종 함께 사용한다. 예를 들어, 아래는 Hello 문자열을 10번
# (0부터 9까지) 출력하는 예제이다.
# for i in range(10):
#     print("Hello")
''' i=1
while i <= 10:
    print(i)
    i += 1
sum = 0
for i in range(11):
    sum += i
print(sum)
list = ["This", "is", "a", "book"]
for s in list:
    print(s)
i = 0
sum = 0
while True:
    i += 1
    if i == 5:
        continue
    if i > 10:
        break
    sum += i
print(sum)
numbers = range(2, 11, 2)
for x in numbers:
    print(x)
for i in range(10):
    print("Hello") '''

# [컬렉션: List]
# 1. 리스트 (List)
# 리스트는 여러 요소들을 갖는 집합(컬렉션)으로 새로운 요소를 추가하거나 갱신, 삭제하는 일이 가능하다. 파이썬의 리스트는 동적배열(Dynamic Array)
# 로서 자유롭게 확장할 수 있는 구조를 갖는다. 리스트는 그 안의 요소(element)들은 그 값을 자유롭게 변경할 수 있는 Mutable 데이타 타입이다.
# 리스트의 요소들은 Square bracket([ ])으로 둘러쌓여 컬렉션을 표현하는데, 각 요소들은 서로 다른 타입이 될 수 있으며, 컴마(,)로 구분한다.
# 요소가 없는 빈 리스트는 "[]"와 같이 표현한다.
# a = []     # 빈 리스트
# a = ["AB", 10, False]
# 2. 리스트 인덱싱(Indexing)
# 리스트의 특정 한 요소만을 선택하기 위하여 인덱싱(Indexing)을 사용하는데, 첫번째요소는 "리스트[0]", 두번째 요소는 "리스트[1]" 처럼 표현한다. 
# 즉, 아래 예제에서 처럼 리스트 a 가 있을 때, a[1] 는 두번째 요소 10을 가리킨다. 파이썬 인덱싱에서 한가지 특별한 표현은 인덱스에 -1, -2 같은
# 음수를 사용할 수 있다는 점이다. 이 때, -1은 현재 리스트의 마지막 요소를, -2는 뒤에서 두번째 요소를 가리킨다.
# a = ["AB", 10, False]
# x = a[1]        # a의 두번째 요소 읽기
# a[1] = "Test"   # a의 두번째 요소 변경
# y = a[-1]       # False
# 3. 리스트 슬라이싱(Slicing)
# 리스트에서 일부 부분 요소들을 선택하기 위하여 슬라이스(Slice)를 사용한다. 슬라이스는 "리스트[처음인덱스:마지막인덱스]"와 같이 인덱스 표현에서
# 부분집합의 범위를 지정하는 것이다. 인덱스는 0 부터 시작하며, 마지막 인덱스를 원하는 "마지막 요소의 인덱스 + 1"을 의미한다. 만약 처음인덱스가
# 생략되면, 0 부터 시작되며, 마지막 인덱스가 생략되면, 리스트의 끝까지 포함됨을 의미한다.
# a = [1, 3, 5, 7, 10]
# x = a[1:3]     # [3, 5]
# x = a[:2]      # [1, 3]
# x = a[3:]      # [7, 10]
# 4. 리스트 요소 추가,수정,삭제
# 리스트에 새로운 요소를 추가하기 위해서는 "리스트.append()"를 사용한다. 리스트 요소를 갱신하기 위해서는 리스트 인덱싱을 사용하여 특정요소에
# 새 값을 넣는다. 리스트 요소를 삭제하기 위해서는 "del 요소"와 같이 특정 요소를 지운다.
# a = ["AB", 10, False]
# a.append(21.5)  # 추가
# a[1] = 11       # 변경
# del a[2]        # 삭제
# print(a)        # ['AB', 11, 21.5]
# 5. 리스트 병합과 반복
# 두 개의 리스트를 병합하기 위해서는 플러스(+)를 사용한다. 이 때 두 리스트는 순서대로 병합된 새로운 하나의 리스트가 된다. 하나의 리스트를 N 번
# 반복하기 위해서는 "리스트 * N"와 같이 표현할 수 있다. 이는 동일한 리스트를 계속 반복한 새 리스트를 만들게 된다.
# # 병합
# a = [1, 2]
# b = [3, 4, 5]
# c = a + b
# print(c)   # [1, 2, 3, 4, 5]
# # 반복
# d = a * 3
# print(d)   # [1, 2, 1, 2, 1, 2]
# 6. 리스트 검색
# 리스트 안에 특정 요소를 검색하기 위해서 index() 메서드를 사용한다. 또한 특정 요소가 몇 개 있는지 체크하기 위해서 count() 메서드를 
# 사용할 수 있다.
# mylist = "This is a book That is a pencil".split()
# i = mylist.index('book')  # i = 3
# n = mylist.count('is')    # n = 2
# print(i, n)
# 7. List Comprehension
# 리스트의 [...] 괄호 안에 for 루프를 사용하여 반복적으로 표현식(expression)을 실행해서 리스트 요소들을 정의하는 특별한 용법이 있는데, 
# 이를 List Comprehension 이라 부른다. 이는 아래와 같은 문법으로 컬렉션으로부터 요소를 하나씩 가져와 표현식을 실행하여 그 결과를 리스트에 
# 담는 방식이다. 여기서 if 조건식은 옵션으로 추가될 수 있는데 for 루프에서 이 조건식에 맞는 요소만 표현식을 실행하게 된다.
# [표현식 for 요소 in 컬렉션 [if 조건식]]
# 아래 예제는 0부터 9까지 숫자들중 3으로 나눈 나머지가 0인 숫자에 대해 그 제곱에 대한 리스트를 구한 예이다.
# list = [n ** 2 for n in range(10) if n % 3 == 0]
# print(list)
# # 출력: [0, 9, 36, 81]
''' a = ["AB", 10, False]
a.append(21.5)  # 추가
a[1] = 11       # 변경
del a[2]        # 삭제
print(a)        # ['AB', 11, 21.5]
# 병합
a = [1, 2]
b = [3, 4, 5]
c = a + b
print(c)   # [1, 2, 3, 4, 5]
# 반복
d = a * 3
print(d)   # [1, 2, 1, 2, 1, 2]
mylist = "This is a book That is a pencil".split()
i = mylist.index('book')  # i = 3
n = mylist.count('is')    # n = 2
print(i, n)
list = [n ** 2 for n in range(10) if n % 3 == 0]
print(list)
# 출력: [0, 9, 36, 81] '''

# [컬렉션: Tuple]
# 1. 튜플 (Tuple)
# Tuple은 리스트와 비슷하게 여러 요소들을 갖는 컬렉션이다. 리스트와 다른 점은 Tuple은 새로운 요소를 추가하거나 갱신, 삭제하는 일을 할 수 없다.
# 즉, Tuple은 한변 결정된 요소를 변경할 수 없는 Immutable 데이타 타입이다. 따라서, Tuple은 컬렉션이 항상 고정된 요소값을 갖기를 원하거나 
# 변경되지 말아야 하는 경우에 사용하게 된다.
# 튜플의 요소들은 둥근 괄호(...) 를 사용하여 컬렉션을 표현하는데, 각 요소들은 서로 다른 타입이 될 수 있으며, 컴마(,)로 구분한다. 요소가 없는 
# 빈 튜플은 "()"와 같이 표현한다.
# t = ("AB", 10, False)
# print(t)
# 특히 요소가 하나일 경우에는 요소 뒤에 콤마를 붙여 명시적으로 Tuple임을 표시해야 한다. 아래 예제를 보면 첫번째 (123) 의 경우, 이는 산술식의 
# 괄호로 인식하여 t1의 타입이 정수가 된다. 이러한 혼동을 방지하기 위해 t2 에서 처럼 (123,) 콤마를 붙여 명시적으로 Tuple임을 표시한다.
# t1 = (123)
# print(t1)  # int 타입
# t2 = (123,)
# print(t2)  # tuple 타입
# 2. Tuple 인덱싱과 슬라이싱
# Tuple은 리스트와 마찬가지로 한 요소를 리턴하는 인덱싱과 특정 부분집합을 리턴하는 슬라이싱을 지원한다. 단, 요소값을 변경하거나 추가 혹은
# 삭제하는 일은 할 수 없다.
# t = (1, 5, 10)
# # 인덱스
# second = t[1]      # 5
# last = t[-1]       # 10
# # 슬라이스
# s = t[1:2]		   # (5)
# s = t[1:]		   # (5, 10)
# 3. Tuple 병합과 반복
# Tuple은 리스트와 마찬가지로 두 개의 튜플을 병합하기 위해 플러스(+)를 사용하고, 하나의 튜플을 N 번 반복하기 위해서는 "튜플 * N"와 같이
# 표현한다.
# # 병합
# a = (1, 2)
# b = (3, 4, 5)
# c = a + b
# print(c)   # (1, 2, 3, 4, 5)
# # 반복
# d = a * 3  # 혹은 "d = 3 * a" 도 동일
# print(d)   # (1, 2, 1, 2, 1, 2)
# 4. Tuple 변수 할당
# Tuple 데이타를 변수에 할당할 때, 각 요소를 각각 다른 변수에 할당할 수도 있다. 예를 들어, 아래 예제에서 첫번째 예의 name 변수는 튜플 전체를
# 할당받는 변수이지만, 두번째의 firstname, lastname 변수는 튜플에 있는 각 요소를 하나씩 할당받는 변수들이다.
# name = ("John", "Kim")
# print(name)
# # 출력: ('John', 'Kim')
# firstname, lastname = ("John", "Kim")
# print(lastname, ",", firstname)
# # 출력: Kim, John
''' t = ("AB", 10, False)
print(t)
t1 = (123)
print(t1)  # int 타입
t2 = (123,)
print(t2)  # tuple 타입
# 병합
a = (1, 2)
b = (3, 4, 5)
c = a + b
print(c)   # (1, 2, 3, 4, 5)
# 반복
d = a * 3  # 혹은 "d = 3 * a" 도 동일
print(d)   # (1, 2, 1, 2, 1, 2)
name = ("John", "Kim")
print(name)
# 출력: ('John', 'Kim')
firstname, lastname = ("John", "Kim")
print(lastname, ",", firstname)
# 출력: Kim, John '''

# [컬렉션: Dictionary]
# 1. Dictionary (dict)
# Dictionary는 "키(Key) - 값(Value)" 쌍을 요소로 갖는 컬렉션이다. Dictionary는 흔히 Map 이라고도 불리우는데, 키(Key)로 신속하게 값(Value)을
# 찾아내는 해시테이블(Hash Table) 구조를 갖는다.
# 파이썬에서 Dictionary는 "dict" 클래스로 구현되어 있다. Dictionary의 키(key)는 그 값을 변경할 수 없는 Immutable 타입이어야 하며, Dictionary 
# 값(value)은 Immutable과 Mutable 모두 가능하다. 예를 들어, Dictionary의 키(key)로 문자열이나 Tuple은 사용될 수 있는 반면, 리스트는 키로 
# 사용될 수 없다.
# Dictionary의 요소들은 Curly Brace "{...}" 를 사용하여 컬렉션을 표현하는데, 각 요소들은 "Key:Value"" 쌍으로 되어 있으며, 요소간은 콤마로 
# 구분한다. 요소가 없는 빈 Dictionary는 "{}"와 같이 표현한다. 특정 요소를 찾아 읽고 쓰기 위해서는 "Dictionary변수[키]"와 같이 키를 인덱스처럼
# 사용한다.
# scores = {"철수": 90, "민수": 85, "영희": 80}
# v = scores["민수"]   # 특정 요소 읽기
# scores["민수"] = 88  # 쓰기
# print(t)
# 파이썬의 Dictionary는 생성하기 위해 위의 예제와 같이 {...} 리터럴(Literal)을 사용할 수도 있지만, 또한 dict 클래스의 dict() 생성자를 사용할
# 수도 있다. dict() 생성자는 (아래 첫번째 예처럼) Key-Value 쌍을 갖는 Tuple 리스트를 받아들이거나 (두번째 예처럼) dict(key=value, key=value, ...) 식의 키-값을 직접 파라미터로 지정하는 방식을 사용할 수 있다.
# # 1. Tuple List로부터 dict 생성
# persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
# mydict = dict(persons)
# age = mydict["홍대길"]
# print(age)   # 35
# # 2. Key=Value 파라미터로부터 dict 생성
# scores = dict(a=80, b=90, c=85)
# print(scores['b'])  #90
# 2. 추가,수정,삭제,읽기
# Dictionary 요소를 수정하기 위해서는 "Dictionary[키]=새값"와 같이 해당 키 인덱스를 사용하여 새 값을 할당하면 된다. Dictionary에 새로운 요소를
# 추가하기 위해서는 수정 때와 마찬가지로 ("맵[새키]=새값") 새 키에 새 값을 할당한다. Dictionary 요소를 삭제하기 위해서는 "del 요소"와 같이 하여
# 특정 요소를 지운다.
# scores = {"철수": 90, "민수": 85, "영희": 80}
# scores["민수"] = 88   # 수정
# scores["길동"] = 95   # 추가
# del scores["영희"]
# print(scores)
# # 출력 {'철수': 90, '길동': 95, '민수': 88}
# Dictionary에 있는 값들을 모두 출력하기 위해서는 다음과 같이 루프를 사용할 수 있다. 아래 예제에서 for 루프는 scores 맵으로부터 키를 하나씩
# 리턴하게 된다. 이때 키는 랜덤하게 리턴되는데, 이는 해시테이블의 속성이다. 각 키에 따른 값을 구하기 위해서는 scores[key]와 같이 사용한다.
# scores = {"철수": 90, "민수": 85, "영희": 80}
# for key in scores:
#     val = scores[key]
#     print("%s : %d" % (key, val))
# 3. 유용한 dict 메서드
# Dictonary와 관련하여 dict 클래스에는 여러 유용한 메서드들이 있다. dict 클래스의 keys()는 Dictonary의 키값들로 된 dict_keys 객체를 리턴하고,
# values()는 Dictonary의 값들로 된 dict_values 객체를 리턴한다.
# scores = {"철수": 90, "민수": 85, "영희": 80}
# # keys
# keys = scores.keys()
# for k in keys:
#     print(k)
# # values
# values = scores.values()
# for v in values:
#     print(v)
# dict의 items()는 Dictonary의 키-값 쌍 Tuple 들로 구성된 dict_items 객체를 리턴한다. 참고로 dict_items 객체를 리스트로 변환하기 위해서는
# list()를 사용할 수 있다. 이는 dict_keys, dict_values 객체에도 공히 적용된다.
# scores = {"철수": 90, "민수": 85, "영희": 80}
# items = scores.items()
# print(items)
# # 출력: dict_items([('민수', 85), ('영희', 80), ('철수', 90)])
# # dict_items를 리스트로 변환할 때
# itemsList = list(items)
# dict.get() 메서드는 특정 키에 대한 값을 리턴하는데, 이는 Dictionary[키]를 사용하는 것과 비슷하다. 단, Dictionary[키]를 사용하면 키가 없을 때
# 에러(KeyError)를 리턴하는 반면, get()은 키가 Dictionary에 없을 경우 None을 리턴하므로 더 유용할 수 있다. 물론 get()을 사용하는 대신 해당 키가
# Dictionary에 존재하는지 체크하고 Dictionary[키]를 사용하는 방법도 있다. 키가 Dictionary에 존재하는지를 체크하지 위해서는 멤버쉽연산자 in 을 
# 사용하면 된다.
# scores = {"철수": 90, "민수": 85, "영희": 80}
# v = scores.get("민수")  # 85
# v = scores.get("길동")  # None
# v = scores["길동"]      # 에러 발생
# # 멤버쉽연산자 in 사용
# if "길동" in scores:
#     print(scores["길동"])
# scores.clear()  # 모두 삭제
# print(scores)
# dict.update() 메서드는 Dictionary 안의 여러 데이타를 한꺼번에 갱신하는데 유용한 메서드이다. 아래 예제에서 처럼, update() 안에 Dictionary
# 형태로 여러 데이타의 값을 변경하면, 해당 데이타들이 update() 메서드에 의해 한꺼번에 수정된다.
# persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
# mydict = dict(persons)
# mydict.update({'홍대길':33,'강찬수':26})
''' scores = {"철수": 90, "민수": 85, "영희": 80}
v = scores["민수"]   # 특정 요소 읽기
scores["민수"] = 88  # 쓰기
print(scores)
persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)
age = mydict["홍대길"]
print(age)   # 35
scores = dict(a=80, b=90, c=85)
print(scores['b'])  #90
scores = {"철수": 90, "민수": 85, "영희": 80}
scores["민수"] = 88   # 수정
scores["길동"] = 95   # 추가
del scores["영희"]
print(scores)
for key in scores:
    val = scores[key]
    print("%s : %d" % (key, val))
# keys
scores = {"철수": 90, "민수": 85, "영희": 80}
keys = scores.keys()
for k in keys:
    print(k)
# values
values = scores.values()
for v in values:
    print(v)
scores = {"철수": 90, "민수": 85, "영희": 80}
items = scores.items()
print(items)
scores = {"철수": 90, "민수": 85, "영희": 80}
v = scores.get("민수")  # 85
v = scores.get("길동")  # None
# v = scores["길동"]      # 에러 발생
# 멤버쉽연산자 in 사용
if "길동" in scores:
    print(scores["길동"])
scores.clear()  # 모두 삭제
print(scores)
persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)
mydict.update({'홍대길':33,'강찬수':26})
print(mydict) '''

# [컬렉션: Set]
# 1. Set
# Set은 중복이 없는 요소들 (unique elements)로만 구성된 집합 컬렉션이다. Set은 Curly Brace { } 를 사용하여 컬렉션을 표현하는데, 내부적으로 
# 요소들을 순서대로 저장하기 않기 때문에, 순서에 의존하는 기능들을 사용할 수 없다. 만약 set을 정의할 때, 중복된 값을 입력하는 경우, set은
# 중복된 값을 한번만 가지고 있게 된다. 리스트나 튜플 등을 set으로 변경하기 위해서는 set() 생성자를 사용한다. 이는 리스트에 중복된 값들이 
# 있을 때, 중복 없이 Unique한 값만을 얻고자 할 때 유용하다.
# # set 정의
# myset = { 1, 1, 3, 5, 5 }
# print(myset)    # 출력: {1, 3, 5}
# # 리스트를 set으로 변환
# mylist = ["A", "A", "B", "B", "B"]
# s = set(mylist)
# print(s)        # 출력: {'A', 'B'}
# 2. Set에서의 추가 및 삭제
# Set에 하나의 새로운 요소를 추가하기 위해서는 set 클래스의 add() 메서드를 사용하고, 여러 개의 요소들을 한께번에 추가하기 위해서는 update() 
# 메서드를 사용한다. 또한 Set에서 하나의 요소를 삭제하기 위해서는 remove() 혹은 discard() 메서드를 사용하고, 전체를 모두 지우기 위해서는
# clear() 메서드를 사용한다.
# myset = {1, 3, 5}
# # 하나만 추가
# myset.add(7)
# print(myset)
# # 여러 개 추가
# myset.update({4,2,10})
# print(myset)
# # 하나만 삭제
# myset.remove(1)
# print(myset)
# # 모두 삭제
# myset.clear()
# print(myset)
# 3. 집합 연산
# 수학에서 두개의 집합 간의 연산으로 교집합, 합집합, 차집합이 있는데, set 클래스는 이러한 집합 연산 기능을 제공한다. 즉, a와 b가 set 일 때, 
# 교집합은 a & b (혹은 a.intersection(b)), 합집합은 a | b (혹은 a.union(b)), 차집합은 a - b (혹은 a.differene) 와 같이 구할 수 있다.
# a = {1, 3, 5}
# b = {1, 2, 5}
# # 교집합
# i = a & b
# # i = a.intersection(b)
# print(i)
# # 합집합
# u = a | b
# # u = a.union(b)
# print(u)
# # 차집합
# d = a - b
# # d = a.difference(b)
# print(d)
''' # set 정의
myset = { 1, 1, 3, 5, 5 }
print(myset)    # 출력: {1, 3, 5}
# 리스트를 set으로 변환
mylist = ["A", "A", "B", "B", "B"]
s = set(mylist)
print(s)        # 출력: {'A', 'B'}
myset = {1, 3, 5}
# 하나만 추가
myset.add(7)
print(myset)
# 여러 개 추가
myset.update({4,2,10})
print(myset)
# 하나만 삭제
myset.remove(1)
print(myset)
# 모두 삭제
myset.clear()
print(myset)
a = {1, 3, 5}
b = {1, 2, 5}
# 교집합
i = a & b
# i = a.intersection(b)
print(i)
# 합집합
u = a | b
# u = a.union(b)
print(u)
# 차집합
d = a - b
# d = a.difference(b)
print(d) '''

# [함수]
# 함수(function)은 일정한 작업을 수행하는 코드블럭으로 보통 반복적으로 계속 사용되는 코드들을 함수로 정의하여 사용하게 된다. 
# 파이썬에서 함수는 def 키워드를 사용하여 정의되며, 다음과 같은 문법을 갖는다. 여기서 입력파라미터나 리턴값은 구현하는 내용에 따라 
# 있을 수도 있고, 없을 수도 있다.
# def 함수명(입력파라미터):
#     문장1
#     문장2
#     [return 리턴값]
# 파라미터 전달방식
# 파이썬 함수에서 입력 파라미터는 Pass by Assignment에 의해 전달된다. 즉, 호출자(Caller)는 입력 파라미터 객체에 대해 레퍼런스를
# 생성하여 레퍼런스 값을 복사하여 전달한다. 또한 전달되는 입력파라미터는 Mutable일 수도 있고, Immutable일 수도 있으므로 각 경우에
# 따라 다른 결과가 일어난다.
# 만약 입력파라미터가 Mutable 객체이고, 함수가 그 함수 내에서 해당 객체의 내용을 변경하면, 이러한 변경 사항은 호출자(caller)에게 
# 반영된다. 하지만, 함수 내에서 새로운 객체의 레퍼런스를 입력파라미터에 할당한다면, 레퍼런스 자체는 복사하여 전달되었으므로, 
# 호출자에서는 새로운 레퍼런스에 대해 알지 못하게 되고, 호출자 객체는 아무런 변화가 없게 된다.
# 만약 입력파라미터가 Immutable 객체이면, 입력파라미터의 값이 함수 내에서 변경될 수 없으며, 함수 내에서 새로운 객체의 레퍼런스를
# 입력파라미터에 할당되어도 함수 외부(Caller)의 값은 변하지 않는다.
# 위의 예제에서 함수 f()는 하나의 정수(i)와 하나의 리스트(mylist)를 입력받아, 함수 내에서 그 값들을 변경한다. 정수는 Immutable 
# 타입이므로 함수 내에서 변경된 것이 호출자에 반영되지 않으며, 리스트는 Mutable 타입이므로 추가된 요소가 호출자에서도 반영된다.
# 가변길이 파라미터
# 함수의 입력파라미터의 갯수를 미리 알 수 없거나, 0부터 N개의 파라미터를 받아들이도록 하고 싶다면, 가변길이 파라미터를 사용할 수 있다.
# 가변길이 파라미터는 파라미터명 앞에 * 를 붙여 가변길이임을 표시한다. 아래 예제에서 *numbers는 가변길이 파라미터이므로, total()을 호출할 때, 
# 임의의 숫자의 파라미터들을 지정할 수 있다.
# 리턴값
# 함수로부터 호출자로 리턴하기 위해서는 return 문을 사용한다. return문은 단독으로 쓰이면 아무 값을 호출자에게 전달하지 않으며, 
# "return 리턴값" 처럼 쓰이면, 값을 호출자에게 전달한다. 함수에서 리턴되는 값은 하나 이상일 수 있는데, 필요한 수만큼 return 키워드
# 다음에 콤마로 구분하여 적는다. 예를 들어, return a,b,c 는 3개의 값을 리턴한다. 하지만, 기술적으로 좀 더 깊이 설명하면, 
# 이는 (a,b,c) 세개의 값을 포함하는 Tuple 하나를 리턴하는 것으로 함수는 항상 하나의 리턴값을 전달한다고 볼 수 있다.
# 함수내에서 i, mylist 값 변경
''' def f(i, mylist):
     i = i + 1
    mylist.append(0)
k = 10       # k는 int (immutable)
m = [1,2,3]  # m은 리스트 (mutable)
f(k, m)      # 함수 호출
print(k, m)  # 호출자 값 체크
출력: 10 [1, 2, 3, 0]
def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot
t = total(1,2)
print(t)
t = total(1,5,2,6)
print(t)
def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot
count, sum = calc(1,5,2,6)  # (count, tot) 튜플을 리턴
print(count, sum) '''

# [모듈}
# 모듈(Module)은 파이썬 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것으로, 보통 하나의 파이썬 .py 파일이 하나의 모듈이 된다.
# 모듈 안에는 함수, 클래스, 혹은 변수들이 정의될 수 있으며, 실행 코드를 포함할 수도 있다.
# 파이썬은 기본적으로 상당히 많은 표준 라이브러리 모듈들을 제공하고 있으며, 3rd Party에서도 많은 파이쎤 모듈들을 제공하고 있다.
# 이러한 모듈들을 사용하기 위해서는 모듈을 import하여 사용하면 되는데, import 문은 다음과 같이 하나 혹은 복수의 모듈을 불러들일 수 있다.
# import 모듈1[, 모듈2[,... 모듈N]
# 예를 들어, 아래 예제는 표준 라이브러리 중 수학과 관련된 함수들을 모아 놓은 "math" 모듈을 import 하여 그 모듈 안에 있는 
# factorial() 함수를 사용하는 예이다.
# 하나의 모듈 안에는 여러 함수들이 존재할 수 있는데, 이 중 하나의 함수만을 불러 사용하기 위해서는 아래와 같이 "from 모듈명 import 함수명"이라는
# 표현을 사용할 수 있다. 이렇게 from...import... 방식으로 import 된 함수는 호출시 "모듈명.함수명"이 아니라 직접 "함수명"만을 사용한다.
# 하나의 모듈 안에는 있는 여러 함수를 사용하기 위해 from... import (함수1, 함수2) 와 같이 import 뒤에 사용할 함수를 나열할 수도 있다. 
# 또한, 모든 함수를 불러 사용하기 위해서는 "from 모듈명 import *" 와 같이 asterisk(*)를 사용할 수 있다. 
# 이렇게 from...import... 방식으로 import 된 함수는 호출시 모듈명 없이 직접 함수명을 사용한다.
# 함수의 이름이 길거나 어떤 필요에 의해 함수의 이름에 Alias를 주고 싶은 경우가 있는데, 
# 이 때는 아래와 같이 "함수명 as Alias" 와 같은 표현을 사용할 수 있다.
# 모듈의 위치
# 파이썬에서 모듈을 import 하면 그 모듈을 찾기 위해 다음과 같은 경로를 순서대로 검색한다.
# 1.현재 디렉토리
# 2.환경변수 PYTHONPATH에 지정된 경로
# 3.Python이 설치된 경로 및 그 밑의 라이브러리 경로
# 이러한 경로들은 모두 취합되어 시스템 경로인 sys.path에 리스트 형태로 저장된다. 따라서, 모듈이 검색되는 검색 경로는 
# sys.path를 체크하면 쉽게 알 수 있다. 
# 모듈을 import 하면 sys.path에 있는 경로 순서대로 모듈을 찾아 import하다가 만약 끝까지 찾지 못하면 에러가 발생된다.
# sys.path를 사용하기 위해서는 sys라는 시스템 모듈을 import 해야 하며, sys.path는 임의로 수정할 수도 있다. 
# 예를 들어, 기존 sys.path에 새 경로를 추가(append)하면, 추가된 경로도 이후 모듈 검색 경로에 포함된다
# 아래는 sys.path를 출력해 본 예인데, sys.path[0]의 값은 빈 문자열(empty string)로 이는 현재 디렉토리를 가리킨다. 
# 즉, 먼저 현재 디렉토리부터 찾는다는 뜻이다. 마지막 라인은 sys.path.append()를 사용하여 새 경로를 추가하는 예를 든 것이다.
# 파이썬 모듈 .py 파일은 import 하여 사용할 수 있을 뿐만 아니라, 해당 모듈 파일 안에 있는 스크립트 전체를 바로 실행할 수도 있다. 
# 파이썬에서 하나의 모듈을 import 하여 사용할 때와 스크립트 전체를 실행할 때를 동시에 지원하기 위하여 흔히 관행적으로 
# 모듈 안에서 __name__ 을 체크하곤 한다. 파이썬에서 모듈을 import해서 사용할 경우 그 모듈 안의 __name__ 은 해당 모듈의 이름이 되며, 
# 모듈을 스크립트로 실행할 경우 그 모듈 안의 __name__ 은 "__main__" 이 된다. 예를 들어, run.py이라는 모듈을 import 하여 사용할 경우
# __name__ 은 run.py가 되며, "python3.5 run.py"와 같이 인터프리터로 스크립트를 바로 실행할 때 __name__ 은 __main__ 이 된다.
''' import math
n = math.factorial(5)
# factorial 함수만 import
from math import factorial  
n = factorial(5) / factorial(3)
# 여러 함수를 import
from math import (factorial,acos)
n = factorial(3) + acos(1)
# 모든 함수를 import
from math import *
n = sqrt(5) + fabs(-12.5)
# factorial() 함수를 f()로 사용 가능
from math import factorial as f
n = f(5) / f(3)
# run.py
import sys
def openurl(url):
    #..본문생략..
    print(url)
if __name__ == '__main__':
    openurl(sys.argv[0]) '''

# [패키지]
# 패키지
# 파이썬에서 모듈은 하나의 .py 파일을 가리키며, 패키지는 이러한 모듈들을 모은 컬렉션을 가리킨다. 파이썬의 패키지는 하나의 디렉토리에
# 놓여진 모듈들의 집합을 가리키는데, 그 디렉토리에는 일반적으로 __init__.py 라는 패키지 초기화 파일이 존재한다 
# (주: Python 3.3 이후부터는 init 파일이 없어도 패키지로 인식이 가능하다).
# 패키지는 모듈들의 컨테이너로서 패키지 안에는 또다른 서브 패키지를 포함할 수도 있다. 파일시스템으로 비유하면 패키지는 일반적으로 
# 디렉토리에 해당하고, 모듈은 디렉토리 안의 파일에 해당한다.
# 파이썬으로 큰 프로젝트를 수행하게 될 때, 모든 모듈을 한 디렉토리에 모아 두기 보다는 계층적인 카테고리로 묶어서 패키지별로 관리하는
# 것이 편리하고 효율적이다. 파이썬 프로젝트의 루트로부터 각 영역별로 디렉토리/서브디렉토리를 만들고 그 안에 논리적으로 동일한 기능을 
# 하는묶을 모듈들을 같이 두어 패키지를 만들 수 있다. 이때 패키지는 "디렉토리.서브디렉토리"와 같이 엑세스하고 패키지내 모듈은 
# "디렉토리.서브디렉토리.모듈" 과 같이 엑세스할 수 있다. 즉, 각 디렉토리 및 모듈 사이에 점(.)을 사용한다.
# 간단한 예로 다음 그림과 같이 models/account 폴더를 만들고, 그 안에 bill.py 라는 모듈이 있다고 가정하자. models/account 폴더에는
# 그 폴더가 일반 폴더가 아닌 패키지임을 표시하기 위해 빈 __init__.py 파일을 만들었다 (버젼 3.3+ 에선 Optional).
# 패키지 안에 있는 모듈을 import 하여 사용하기 위해서는 일반 모듈처럼 import문 혹은 from...import... 문을 사용한다. 먼저 import문을 
# 보면 import문은 모듈을 import 하는 것이므로, 패키지내 모듈을 import하기 위해서는 "import 패키지명.모듈명"과 같이 패키지명을 앞에 
# 붙여 사용한다. 아래 예제에서 보면, bill.py 모듈을 import 하기 위해 "import models.account.bill" 와 같이 전체 패키지명을 함께
# 표시하였음을 볼 수 있다. 또한 모듈내 함수를 사용하기 위하여 models.account.bill.charge()와 같이 패키지명과 모듈명도 함께 
# 써 주어야 한다.
# 다음으로 from ... import ... 문을 살펴보자. 먼저 패키지 모듈을 import 하기 위해 "from 패키지명 import 모듈명" 문을 사용할 수 있다. 
# 아래 예제를 보면, from 뒤에 패키지명 models.account을 사용하였고, import 다음 모듈명 bill을 사용하였다. 
# 이 방식은 해당 모듈 내의 모든 함수를 사용할 수 있는데, bill.charge()와 같이 모듈명.함수명()으로 함수를 호출한다.
# 만약 패키지 모듈 내의 특정 함수만 import하여 사용하고 싶다면, "from 패키지명.모듈명 import 함수명" 과 같이 from 에 "패키지명.모듈명"을
# 적고 import 뒤에 함수명을 적는다.
# _init__.py
# 패키지에는 __init__.py 라는 특별한 파일이 있는데, 이 파일은 기본적으로 그 폴더가 일반 폴더가 아닌 패키지임을 표시하기 위해 사용될 
# 뿐만 아니라, 패키지를 초기화하는 파이썬 코드를 넣을 수 있다. 버젼 3.3 이상에서는 이 파일이 없어도 패키지로 사용할 수 있지만, 호환성을
# 위해 두는 것이 좋다. __init__.py 파일에서 중요한 변수로 __all__ 이라는 리스트 변수가 있는데, 이 변수는 "from 패키지명 import *" 문을 
# 사용할 때, 그 패키지 내에서 import 가능한 모듈들의 리스트를 담고 있다. 즉, __all__ 에 없는 모듈은 import 되지 않고 에러가 발생한다.
# 아래 예제는 __init__.py 파일 안에 bill 모듈을 허락한 후, from ... import * 를 사용하여 해당 패지키로부터 허락된 모든 모듈을 
# import 한 후 bill.charge() 함수를 사용하는 예이다.
''' # 모듈 import 
# import 패키지.모듈
import models.account.bill
models.account.bill.charge(1, 50)
# 모듈안의 모든 함수 import
# from 패키지명 import 모듈명
from models.account import bill
bill.charge(1, 50)
# 특정 함수만 import
# from 패키지명.모듈명 import 함수명
from models.account.bill import charge
charge(1, 50)
# __init__.py 파일의 내용
__all__ = ['bill']
# 패지키내 모든 모듈 import
# from 패키지명 import *
from models.account import *
bill.charge(1, 50) '''

# [클래스]
# 파이썬은 객체지향 프로그래밍(OOP, Object Oriented Programming)을 기본적으로 지원하고 있다. 파이썬에서 객체지향 프로그래밍의 기본 
# 단위인 클래스를 만들기 위해서는 아래와 같이 "class 클래스명" 을 사용하여 정의한다. 클래스명은 PEP 8 Coding Convention에 가이드된
# 대로 각 단어의 첫 문자를 대문자로 하는 CapWords 방식으로 명명한다. 아래 예제는 MyClass라는 클래스를 정의한 것으로 별도의 클래스 
# 멤버를 정의하지 않은 가장 간단한 빈 클래스이다. 클래스 정의 내의 pass문은 빈 동작 혹은 아직 구현되지 않았음을 의미하는 것으로
# 여기서는 빈 클래스를 의미한다.
# 클래스 멤버
# 클래스는 데이타를 표현하는 속성(attribute)과 행위를 표현하는 메서드(method)를 포함하는 논리적인 컨테이너이다. 
# 클래스는 세부적으로 메서드(method), 프로퍼티(property), 클래스 변수(class variable), 인스턴스 변수(instance variable),
# 초기자(initializer), 소멸자(destructor) 등 다양한 종류의 멤버들로 구분할 수 있다. 파이썬에서 클래스는 전통적으로 크게 
# 속성(attribute)과 메서드(method)를 갖는 논리적 단위이지만, 메서드를 특히 Callable attribute로 볼 수도 있기 때문에 속성과 메서드 
# 모두를 그 클래스의 attribute 라고 생각할 수도 있다. 또한, 다른 OOP 언어와 달리, 파이썬은 동적 언어(Dynamic Language)로서 새로운
# attribute를 실행 중 동적으로 추가할 수 있다.
# 메서드
# 메서드는 클래스의 행위를 표현하는 것으로 클래스 내의 함수로 볼 수 있다. 파이썬에서 메서드는 크게 인스턴스 메서드(instance method), 
# 클래스 메서드(class method), 정적 메서드(static method)가 있다. 가장 흔히 쓰이는 인스턴스 메서드는 인스턴스 변수에 엑세스할 수 
# 있도록 메서드의 첫번째 파라미터에 항상 객체 자신을 의미하는 "self"라는 파라미터를 갖는다. 아래 예제에서 calcArea()가 인스턴스
# 메서드에 해당된다. 인스턴스 메서드는 여러 파라미터를 가질 수 있지만, 첫번째 파라미터는 항상 self 를 갖는다.
# 클래스 변수
# 클래스 정의에서 메서드 밖에 존재하는 변수를 클래스 변수(class variable)라 하는데, 이는 해당 클래스를 사용하는 모두에게 공용으로
# 사용되는 변수이다. 클래스 변수는 클래스 내외부에서 "클래스명.변수명" 으로 엑세스 할 수 있다. 위의 예제에서 count는 클래스변수로서 
# "Rectangle.count"와 같이 엑세스할 수 있다.
# 인스턴스 변수
# 하나의 클래스로부터 여러 객체 인스턴스를 생성해서 사용할 수 있다. 클래스 변수가 하나의 클래스에 하나만 존재하는 반면, 
# 인스턴스 변수는 각 객체 인스턴스마다 별도로 존재한다. 클래스 정의에서 메서드 안에서 사용되면서 "self.변수명"처럼 사용되는
# 변수를 인스턴스 변수(instance variable)라 하는데, 이는 각 객체별로 서로 다른 값을 갖는 변수이다. 인스턴스 변수는 클래스 내
# 부에서는 self.width 과 같이 "self." 을 사용하여 엑세스하고, 클래스 밖에서는 "객체변수.인스턴스변수"와 같이 엑세스 한다.
# Python은 다른 언어에서 흔히 사용하는 public, protected, private 등의 접근 제한자 (Access Modifier)를 갖지 않는다.
# Python 클래스는 기본적으로 모든 멤버가 public이라고 할 수 있다. Python 코딩 관례(Convention)상 내부적으로만 사용하는 변수 혹은
# 메서드는 그 이름 앞에 하나의 밑줄(_) 을 붙인다. 하지만 이는 코딩 관례에 따른 것일 뿐 실제 밑줄 하나를 사용한 멤버도 public 이므로 
# 필요하면 외부에서 엑세스할 수 있다.
# 만약 특정 변수명이나 메서드를 private으로 만들어야 한다면 두개의 밑줄(__)을 이름 앞에 붙이면 된다.
# Initializer (초기자)
# 클래스로부터 새 객체를 생성할 때마다 실행되는 특별한 메서드로 __init__() 이라는 메서드가 있는데, 이를 흔히 클래스 Initializer 라 
# 부른다 (주: 파이썬에서 두개의 밑줄 (__) 시작하고 두개의 밑줄로 끝나는 레이블은 보통 특별한 의미를 갖는다).
# Initializer는 클래스로부터 객체를 만들 때, 인스턴스 변수를 초기화하거나 객체의 초기상태를 만들기 위한 문장들을 실행하는 곳이다.
# 위의 __init__() 예제를 보면, width와 height라는 입력 파라미터들을 각각 self.width와 self.height라는 인스턴스변수에 할당하여
# 객체 내에서 계속 사용할 수 있도록 준비하고 있다.
# (주: Python의 Initializer는 C#/C++/Java 등에서 일컫는 생성자(Constructor)와 약간 다르다. Python에서 클래스 생성자(Constructor)는
# 실제 런타임 엔진 내부에서 실행되는데, 이 생성자(Constructor) 실행 도중 클래스 안에 Initializer가 있는지 체크하여 만약 있으면
# Initializer를 호출하여 객체의 변수 등을 초기화한다.).
# 정적 메서드와 클래스 메서드
# 인스턴스 메서드가 객체의 인스턴스 필드를 self를 통해 엑세스할 수 있는 반면, 정적 메서드는 이러한 self 파라미터를 갖지 않고 인스턴스
# 변수에 엑세스할 수 없다. 따라서, 정적 메서드는 보통 객체 필드와 독립적이지만 로직상 클래스내에 포함되는 메서드에 사용된다. 
# 정적 메서드는 메서드 앞에 @staticmethod 라는 Decorator를 표시하여 해당 메서드가 정적 메서드임을 표시한다.
# 클래스 메서드는 메서드 앞에 @classmethod 라는 Decorator를 표시하여 해당 메서드가 클래스 메서드임을 표시한다. 
# 클래스 메서드는 정적 메서드와 비슷한데, 객체 인스턴스를 의미하는 self 대신 cls 라는 클래스를 의미하는 파라미터를 전달받는다.
# 정적 메서드는 이러한 cls 파라미터를 전달받지 않는다. 클래스 메서드는 이렇게 전달받은 cls 파라미터를 통해 클래스 변수 등을 엑세스할 수 있다.
# 일반적으로 인스턴스 데이타를 엑세스 할 필요가 없는 경우 클래스 메서드나 정적 메서드를 사용하는데, 이때 보통 클래스 변수를 엑세스할
# 필요가 있을 때는 클래스 메서드를, 이를 엑세스할 필요가 없을 때는 정적 메서드를 사용한다.
# 아래 예제에서 isSquare() 메서드는 정적 메서드로서 cls 파라미터를 전달받지 않고 메서드 내에서 클래스 변수를 사용하지 않고 있다.
# 반면, printCount() 메서드는 클래스 메서드로서 cls 파라미터를 전달받고 메서드 내에서 클래스 변수 count 를 사용하고 있다.
# Special Method (Magic Method)
# 파이썬에는 Initializer 이외에도 객체가 소멸될 때 (Garbage Collection 될 때) 실행되는 소멸자(__del__) 메서드, 
# 두 개의 객체를 ( + 기호로) 더하는 __add__ 메서드, 두 개의 객체를 ( - 기호로) 빼는 __sub__ 메서드,
# 두 개의 객체를 비교하는 __cmp__ 메서드, 문자열로 객체를 표현할 때 사용하는 __str__ 메서드 등 많은 특별한 용도의 메서드들이 있는데,
# 이러한 메서드들을 Special Method 혹은 매직메서드(Magic Method)라고 부른다. 아래 예제는 이 중 __add__() 메서드에 대한 예이다.
# 클래스 인스턴스의 생성과 사용
# 클래스를 사용하기 위해서는 먼저 클래스로부터 인스턴스(객체)를 생성해야 한다. 파이썬에서 인스턴스를 생성하기 위해서는
# "객체변수명 = 클래스명()"과 같이 클래스명을 함수 호출하는 것처럼 사용하면 된다. 만약 __init__() 함수가 있고, 
# 그곳에 입력 파라미터들이 지정되어 있다면, "클래스명(입력파라미터들)"과 같이 파라미터를 괄호 안에 전달한다. 
# 이렇게 전달된 파라미터들은 Initializer 에서 사용된다.
# 아래 예제를 보면, Rectangle 클래스로부터 r 이라는 클래스 인스턴스를 생성 하고 있는데, Rectangle(2, 3)와 같이 2개의 파라미터를
# 전달하고 있다. 이는 Rectangle 초기자에서 각각 width와 height 인스턴스 변수를 초기화하는데 사용된다.
# 클래스로부터 생성된 클래스 인스턴스(객체)로부터 클래스 멤버들을 호출하거나 엑세스할 수 있다. 
# 인스턴스 메서드는 "객체변수.메서드명()"과 같이 호출할 수 있는데, 위의 예제에선 r.calcArea() 이 메서드 호출에 해당된다. 
# 인스턴스 변수는 "객체변수.인스턴스변수" 으로 표현되며, 값을 읽거나 변경하는 일이 가능하다. 위의 예제 r.width = 10 은 
# 인스턴스변수 width 에 새 값을 할당하는 예이다.
# 파이썬에서 특히 클래스 변수를 엑세스할 때, "클래스명.클래스변수명" 혹은 "객체명.클래스변수명"을 둘 다 허용하기 때문에 약간의
# 혼란을 초래할 수 있다. 예를 들어, 위의 예제에서 Rectangle.count 혹은 r.count은 모두 클래스 변수 count를 엑세스하는 경우로서
# 이 케이스에는 동일한 값을 출력한다.
# 하지만, 아래 예제와 같이 Rectangle 클래스의 클래스 변수 count를 Rectangle.count로 할당하지 않고 객체 r 로부터 할당하면 혼돈스러운
# 결과를 초래하게 된다.
# 파이썬에서 한 객체의 attribute에 값이 할당되면 (예를 들어, r.count = 10), 먼저 해당 객체에 이미 동일한 attribute가 있는지 체크해서
# 있으면 새 값으로 치환하고, 만약 그 attribute가 없으면 객체에 새로운 attribute를 생성하고 값을 할당한다. 즉, r.count = 10 의 경우
# 클래스 변수인 count를 사용하는 것이 아니라 새로 그 객체에 추가된 인스턴스 변수를 사용하게 되므로 클래스 변수값은 변경되지 않는다.
# 파이썬에서 한 객체의 attribute를 읽을 경우에는 먼저 그 객체에서 attribute를 찾아보고, 없으면 그 객체의 소속 클래스에서 찾고,
# 다시 없으며 상위 Base 클래스에서 찾고, 그래도 없으면 에러를 발생시킨다. 따라서, 위 예제에서 클래스 변수값이 출력된 이유는 값을
# 할당하지 않고 읽기만 했기 때문에, r 객체에 새 인스턴스 변수를 생성하지 않게 되었고, 따라서 객체의 attribute가 없어서 클래스의 
# attribute를 찾았기 때문이다.
# 이러한 혼돈을 피하기 위해 클래스 변수를 엑세스할 때는 클래스명을 사용하는 것이 좋다.
# 클래스 상속과 다형성
# 파이썬은 객체지향 프로그래밍의 상속(Inheritance)을 지원하고 있다. 클래스를 상속 받기 위해서는 파생클래스(자식클래스)에서 클래스명
# 뒤에 베이스클래스(부모클래스) 이름을 괄호와 함께 넣어 주면 된다. 즉, 아래 예제에서 Dog 클래스는 Animal 클래스로부터 파생된
# 파생클래스이며, Duck 클래스도 역시 Animal 베이스클래스로부터 파생되고 있다. (주: 파이썬은 복수의 부모클래스로부터 상속 받을 수
# 있는 Multiple Inheritance를 지원하고 있다.)
# 파생클래스는 베이스클래스의 멤버들을 호출하거나 사용할 수 있으며, 물론 파생클래스 자신의 멤버들을 사용할 수 있다.
# 파이썬은 객체지향 프로그래밍의 다형성(Polymorphism)을 또한 지원하고 있다. 아래 예제는 animals 라는 리스트에 Dog 객체와 
# Duck 객체를 넣고 이들의 speak() 메서드를 호출한 예이다. 코드 실행 결과를 보면 객체의 타입에 따라 서로 다른 speak() 메서드가 
# 호출됨을 알 수 있다.
''' class MyClass:
    pass
class Rectangle:
    count = 0  # 클래스 변수
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1
    # 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        return area
    # 정적 메서드
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight   
    # 클래스 메서드
    @classmethod
    def printCount(cls):
        print(cls.count)   
# 테스트
square = Rectangle.isSquare(5, 5)        
print(square)   # True        
rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.printCount()  # 2
def __add__(self, other):
    obj = Rectangle(self.width + other.width, self.height + other.height)
    return obj
# 사용 예
r1 = Rectangle(10, 5)
r2 = Rectangle(20, 15)
# 인스턴스 생성
r = Rectangle(2, 3)
# 메서드 호출
area = r.calcArea()
print("area = ", area)
# 인스턴스 변수 엑세스
r.width = 10
print("width = ", r.width)
# 클래스 변수 엑세스
print(Rectangle.count)
print(r.count)
r = Rectangle(2, 3)
Rectangle.count = 50
r.count = 10   # count 인스턴스 변수가 새로 생성됨
print(r.count, Rectangle.count)  # 10  50 출력
class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass
class Dog (Animal):
    def speak(self):
        print("bark")
class Duck (Animal):
    def speak(self):
        print("quack")
dog = Dog("doggy") # 부모클래스의 생성자
n = dog.name # 부모클래스의 인스턴스변수
dog.move()   # 부모클래스의 메서드
dog.speak()  # 파생클래스의 멤버
animals = [Dog('doggy'), Duck('duck')]
for a in animals:
    a.speak() '''

# [예외처리}
# 프로그램에서 에러가 발생했을 때, 에러를 핸들링하는 기능으로 try...except 문을 사용할 수 있다. 즉, try 블럭 내의 어느 문장에서 에러가
# 발생하면, except 문으로 이동하고 예외 처리를 할 수 있다. try 문은 또한 finally 문을 가질 수도 있는데, finally 블럭은 try 블럭이 
# 정상적으로 실행되든, 에러가 발생하여 except 블럭이 실행되든 상관없이 항상 마지막에 실행된다.
# try:
#   문장1
#   문장2
# except:
#   예외처리
# finally:
#   마지막에 항상 수행
# 위의 except 문은 except 뒤에 아무것도 쓰지 않았는데, 이는 어떤 에러이든 발생하면 해당 except 블럭을 수행하라는 의미이다.
# except 뒤에 "에러타입"을 적거나 "에러타입 as 에러변수"를 적을 수가 있는데, 이는 특정한 타입의 에러가 발생했을 때만 해당 except
# 블럭을 실행하라는 뜻이다. 에러변수까지 지정했으면, 해당 에러변수를 excep 블럭 안에서 사용할 수 있다. 아래 예제를 보면, except가
# 2개 있는데, 첫번째는 IndexError가 발생했을 때만 그 블럭을 실행하며, 두번째는 일반적인 모든 Exception 이 발생했을 때 해당 블럭을 
# 실행하라는 의미이다. 즉, 먼저 IndexError 인지 검사하고, 아니면 다음 except를 계속 순차적으로 체크하게 된다. except가 여러 개인 
# 경우는 범위가 좁은 특별한 에러타입을 앞에 쓰고 보다 일반적인 에러타입을 뒤에 쓰게 된다.
# 또한, 위의 예제에서 else문 있는데, 이는 에러가 발생하지 않을 때 실행하게 되는 블럭이다. 그리고 finally 블럭은 항상 마지막에 
# 실행되는 코드 블럭이다.
# 만약 복수 Exception들이 동일한 except 블럭을 갖는다면, 아래와 같이 이들 Expception들을 하나의 except 문에 묶어서 쓸 수도 있다.
# 에러무시와 에러생성
# 발생된 Exception을 그냥 무시하기 위해서는 보통 pass 문을 사용하며, 또한 개발자가 에러를 던지기 위해서는 raise문을 사용한다.
# raise 뒤에 아무것도 없는 경우는 현재 Exception을 그대로 던지게 된다. 또한 raise 뒤에 특정한 에러타입과 에러메시지 (Optional)를
# 넣어 개발자가 정의한 에러를 발생시킬 수 있다. 예를 들어 아래 예제는 raise 뒤에 Exception 에러타입과 에러메시지를 넣어 특별한
# 에러메시지를 전달하고 있다.
# 파일 에러 처리 예제
# 아래 예제는 전형적인 파일 에러 처리를 보여주는 코드이다. 파일을 오픈할 때 에러가 발생하면, except IOError 블록을 실행한다. 
# 파일오픈을 성공하면, try 블럭을 실행하고, finally 블럭에서 파일을 닫게 된다.
# 참고로 다음은 with 문을 써서 해당 블럭이 끝나면 자동으로 파일을 닫는 코드의 예이다. Python의 with 문은 C샵의 using 문과 비슷한
# 것으로 with 블럭이 끝날 때 자동으로 리소스를 해제하는 역활을 하는데, 특히 주목할 점은 with 블럭 내에서 어떤 Exception이 발생하더라도
# 반드시 리소스를 해제한다는 점이다.
''' def calc(values):
    sum = None
    # try...except...else
    try:
       sum = values[0] + values[1] + values[2]
    except IndexError as err:
        print('인덱스에러')
    except Exception as err:
        print(str(err))
    else:
        print('에러없음')
    finally:
        print(sum)
# 테스트
calc([1, 2, 3, 6]) # 출력: 에러없음 6
calc([1, 2])       # 출력: 인덱스에러 None
def calc(values):
    sum = None
    try:
       sum = values[0] + values[1] + values[2]
    except (IndexError, ValueError):
        print('오류발생')
    print(sum)
# raise 를 사용한 예
total=1
if total < 0:
    raise Exception('Total Error')
try:
   fp = open("test.txt", "r")
   try:
      lines = fp.readlines()
      print(lines)
   finally:
      fp.close()
except IOError:
   print('파일에러')
with open('test.txt', 'r') as fp:
   lines = fp.readlines()
   print(lines) '''

# [유닛테스트]
# Python 에서 유닛 테스트를 수행하기 위해 기본적으로 제공되는 unittest 모듈 (Unit testing framework)을 사용할 수 있다. 
# 유닛 테스트 코드를 작성하기 위해서는 일반적으로 다음과 같은 절차를 따른다.
# 1.먼저 unittest 모듈을 import 한 후,"unittest.TestCase"로부터 파생된 사용자 테스트 클래스를 만든다.
# 2.테스트 클래스 안에 "test" 로 시작하는 테스트 메서드를 생성한다. 테스드 메서드에서는 일반적으로 테스트하고자 하는 함수나 메서드를
#   호출하고 그 결과값을 self.assert*() 메서드를 사용하여 확인한다
#   (assertEqual, assertTrue, assertFalse, assertRaises, assertRegex 등 다양한 assert 메서들을 사용할 수 있다).
# 3.테스트 클래스가 완성되었으면, unittest.main()을 호출하여 테스트를 실행시킨다.
# 예를 들어, myCalc.py 라는 파일 안에 아래 두 함수가 있다고 가정하고, 이 함수들에 대한 유닛 테스트를 작성해 보자.
# 아래는 유닛 테스트를 위한 코드로서 unittest.TestCase 로부터 파생된 MyCalcTest 클래스를 작성하였다. 그리고, test_add 와
# test_substract 테스트 메서드를 작성하였고, 그 안에서 myCalc 함수를 실행한 결과를 self.assertEqual()를 사용하여 검사하였다. 
# 마지막 라인에 unittest.main() 이 실행되면, 테스트 메서드들이 실행되게 된다.
# 파이썬 unittest는 위 그림 하단 좌측에서 보듯이, 전체 스크립트 단위, 테스트 클래스 단위 또는 메서드/함수 단위로 실행할 수 있다.
# Test Fixture
# 테스트 시나리오에 따라 어떤 경우는 테스트 전에 테스트를 위한 사전 준비 작업을 할 필요가 있다. 또한 테스트가 끝난 후 Clean up을
# 해야하는 경우도 있을 수 있다. unittest는 이렇게 사전 준비 작업을 위해 setUp() 이라는 메서드를, 사후 Clean up 처리를 위해 tearDown()
# 이라는 메서드를 사용할 수 있도록 있다. 이러한 setUp, tearDown 기능을 Test Fixture라 하며, Fixture는 각각의 테스트 메서드가 실행되기 
# 전과 후에 매번 실행된다.
# 예를 들어, 아래와 같은 간단한 유틸러티 모듈(myUtil.py)이 있다고 하고, 이에 대한 유닛 테스트를 진행한다고 가정해 보자.
# 아래 MyUtilTest 라는 유닛 테스트 클래스는 test_filelen(), test_count_in_file() 두 개의 테스트 메서드를 가지고 있다. 이들 각각의 
# 테스트 메서드가 실행되기 전에 항상 setUp() 메서드가 실행되어 테스트 파일을 생성하고, 테스트 실행후 tearDown() 메서드가 실행하여 
# 사용한 테스트 파일을 지우게 된다.
# myCalc.py
''' def add(a, b):
    return a + b
def substract(a, b):
    return a - b
# tests.py
import unittest
import myCalc
class MyCalcTest(unittest.TestCase):
    def test_add(self):
        c = myCalc.add(20, 10)
        self.assertEqual(c, 30)
    def test_substract(self):
        c = myCalc.substract(20, 10)
        self.assertEqual(c, 10)
if __name__ == '__main__':
    unittest.main()
# myUtil.py
import os
def filelen(filename):
    f = open(filename, "r")
    f.seek(0, os.SEEK_END)
    return f.tell()
def count_in_file(filename, char_to_find):
    count = 0
    f = open(filename, "r")
    for word in f:
        for char in word:
            if char == char_to_find:
                count += 1
    return count
import unittest
import os
import myUtil
class MyUtilTest(unittest.TestCase):
    testfile = 'test.txt'
    # Fixture
    def setUp(self):
        f = open(MyUtilTest.testfile, 'w')
        f.write('1234567890')
        f.close()
    def tearDown(self):
        try:
            os.remove(MyUtilTest.testfile)
        except:
            pass
    def test_filelen(self):
        leng = myUtil.filelen(MyUtilTest.testfile)
        self.assertEqual(leng, 10)
    def test_count_in_file(self):
        cnt = myUtil.count_in_file(MyUtilTest.testfile, '0')
        self.assertEqual(cnt, 1)
if __name__ == '__main__':
    unittest.main() '''

# [Python Comprehension]
# Python의 Comprehension은 한 Sequence가 다른 Sequence (Iterable Object)로부터 (변형되어) 구축될 수 있게한 기능이다. 
# Python 2 에서는 List Comprehension (리스트 내포)만을 지원하며, Python 3 에서는 Dictionary Comprehension과 Set Comprehension을 
# 추가로 지원하고 있다. 또한, 종종 Generator Comprehension이라고 일컫어 지는 Generator Expression이 있는데, 이는 다음 아티클에서 
# Generator와 함께 설명한다.
# List Comprehension
# List Comprehension (리스트 내포)는 입력 Sequence로부터 지정된 표현식에 따라 새로운 리스트 컬렉션을 빌드하는 것으로, 아래와 같은 문법을
# 갖는다.
# [출력표현식 for 요소 in 입력Sequence [if 조건식]]
# 여기서 입력 Sequence는 입력으로 사용되는 Iteration이 가능한 데이타 Sequence 혹은 컬렉션이다. 입력 Sequence는 for 루프를 돌며 각각의
# 요소를 하나씩 가져오게 되고, if 조건식이 있으면 해당 요소가 조건에 맞는지 체크하게 된다. 만약 조건에 맞으면 출력 
# 표현식(Output Expression)에 각 요소를 대입하여 출력 결과를 얻게 된다. 이러한 과정을 모든 요소에 대해 실행하여 결과를 리스트로 
# 리턴하게 된다. 쉽게 설명하면 for 루프를 돌면 특정 조건에 있는 입력데이타를 변형하여 리스트로 출력하는 코드를 간단한 문법으로 표현한 것이다.
# 아래 예제에서 입력 Sequence (oldlist)는 숫자, 문자 그리고 Boolean 요소를 모두 갖는 리스트이다. List Comprehension 문장을 보면 
# 이 입력 Sequence "oldlist"로부터 요소 i 를 하나씩 가져와 이 i의 타입이 정수형인지 체크하고, 만약 그렇다면 표현식 "i * i" 를 실행하여
# i의 제곱을 계산한다. 이렇게 모든 요소에 대해 계산하면 [1, 4, 9] 라는 결과 리스트(newlist)를 얻게 된다.
# Set Comprehension
# Set Comprehension은 입력 Sequence로부터 지정된 표현식에 따라 새로운 Set 컬렉션을 빌드하는 것으로, 아래와 같은 문법을 갖는다. 
# List Comprehension과 거의 비슷하지만, 결과가 Set {...}으로 리턴된다는 점이 다르다.
# {출력표현식 for 요소 in 입력Sequence [if 조건식]}
# 아래 예제에서 입력 Sequence (oldlist)는 중복된 숫자를 갖는 리스트이다. 결과 Set은 중복을 허용하지 않으므로 중복된 데이타는 자연스럽게
# 제거된다. 또한 Set은 요소의 순서를 보장하지 않으므로, 아래 결과에서 보듯이 순서가 랜덤하게 바뀐 결과를 출력하게 된다.
# Dictionary Comprehension
# Dictionary Comprehension은 입력 Sequence로부터 지정된 표현식에 따라 새로운 Dictionary 컬렉션을 빌드하는 것으로, 아래와 같은 문법을 
# 갖는다. Set Comprehension과 거의 비슷하지만, 출력표현식이 Key:Value Pair로 표현된다는 점이 다르며, 결과로 dict 가 리턴된다.
# {Key:Value for 요소 in 입력Sequence [if 조건식]}
# 아래 예제는 Id로 이름을 찾는 Dictionary (id_name) 를 반대로 Lookup 하기 위해 Key와 Value 서로 바꾼 새로운 Dictionary (name_id)를
# 만든 예이다. 새 Dictionary "name_id"는 이름으로 Id를 찾는 Dictionary이다.
# 또 다른 예제로 아래는 if 조건식 안에 필터링 함수를 사용한 경우이다. 복잡한 조건식일 경우에는 이처럼 필터링 함수를 사용하면 편리하다.
# 아래 예제는 1부터 100까지 홀수를 Dictionary Key로 하고, 그 홀수의 제급을 Value로 하는 dict 객체를 생성한다.
''' oldlist = [1, 2, 'A', False, 3]
newlist = [i*i for i in oldlist if type(i)==int]
print(newlist)
# 출력: [1, 4, 9]
oldlist = [1, 1, 2, 3, 3, 4]
newlist = {i*i for i in oldlist}
print(newlist)
# 출력 : {16, 1, 9, 4}
id_name = {1: '박진수', 2: '강만진', 3: '홍수정'}
name_id = {val:key for key,val in id_name.items()}
print(name_id)
# 출력 : {'박진수': 1, '강만진': 2, '홍수정': 3}
def isodd(val):
    return val % 2 == 1
mydict = {x:x*x for x in range(101) if isodd(x)}
print(mydict) '''

# [Iterator와 Generator]
# 리스트, Set, Dictionary와 같은 컬렉션이나 문자열과 같은 문자 Sequence 등은 for 문을 써서 하나씩 데이타를 처리할 수 있는데,
# 이렇게 하나 하나 처리할 수 있는 컬렉션이나 Sequence 들을 Iterable 객체(Iterable Object)라 부른다.
# 내장 함수 iter()는 "iter(Iterable객체)" 와 같이 사용하여 그 Iterable 객체의 iterator를 리턴한다. 
# Iterable 객체에서 실제 Iteration을 실행하는 것은 iterator로서, iterator는 next 메서드를 사용하여 다음 요소(element)를 가져온다.
# 만약 더이상 next 요소가 없으면 StopIteration Exception을 발생시킨다.
# Iterator의 next 메서드로서 Python 2에서는 "iterator객체.next()" 를 사용하고, Python 3에서는 "iterator객체.__next__()" 메서드를
# 사용한다. 또한, 버전에 관계없이 사용할 수 있는 방식으로 내장 함수 "next(iterator객체)" 를 사용할 수 있다. 
# 아래는 한 리스트에 대해 list iterator를 구한 후, next() 함수를 계속 호출해 본 예이다.
# 어떤 클래스를 Iterable 하게 하려면, 그 클래스의 iterator를 리턴하는 __iter__() 메서드를 작성해야 한다. 이 __iter__() 메서드가
# 리턴하는 iterator는 동일한 클래스 객체가 될 수도 있고, 별도로 작성된 iterator 클래스의 객체가 될 수도 있다. 
# 어떠한 경우든 Iterator가 되는 클래스는 __next()__ 메서드 (Python 2 인 경우 next() 메서드) 를 구현해야 한다. 
# 실제 for 루프에 Iterable Object를 사용하면, 해당 Iterable의 __iter__() 메서드를 호출하여 iterator를 가져온 후 그 iterator의 next() 
# 메서드를 호출하여 루프를 돌게 된다.
# 아래 예제는 간단한 Iterator를 예시한 것으로 __iter__() 메서드에서 self 를 리턴함으로써 Iterable과 동일한 클래스에 Iterator를
# 구현했음을 표시하였고, 그 클래스 안에 Iterator로서 필요한 __next__() 메서드 (Python 3)를 구현하였다.
# Generator
# Generator는 Iterator의 특수한 한 형태이다.
# Generator 함수(Generator function)는 함수 안에 yield 를 사용하여 데이타를 하나씩 리턴하는 함수이다. Generator 함수가 처음 호출되면,
# 그 함수 실행 중 처음으로 만나는 yield 에서 값을 리턴한다. Generator 함수가 다시 호출되면, 직전에 실행되었던 yield 문 다음부터 
# 다음 yield 문을 만날 때까지 문장들을 실행하게 된다. 이러한 Generator 함수를 변수에 할당하면 그 변수는 generator 클래스 객체가 된다.
# 아래 예제는 간단한 Generator 함수와 그 호출 사례를 보인 것이다. 여기서 gen() 함수는 Generator 함수로서 3개의 yield 문을 가지고 있다. 
# 따라서 한번 호출시마다 각 yield 문에서 실행을 중지하고 값을 리턴하게 된다.
# 위의 예에서 g = gen() 문은 Generator 함수를 변수 g 에 할당한 것인데, 이때 g는 generator 라는 클래스의 객체로서 next() 내장함수를
# 사용하여 Generator의 다음 값을 계속 가져올 수 있다. Generator는 물론 예제의 마지막 부분과 같이 for 루프에서 사용될 수 있다.
# 리스트나 Set과 같은 컬렉션에 대한 iterator는 해당 컬렉션이 이미 모든 값을 가지고 있는 경우이나, Generator는 모든 데이타를 갖지 않은
# 상태에서 yield에 의해 하나씩만 데이타를 만들어 가져온다는 차이점이 있다. 이러한 Generator는 데이타가 무제한이어서 모든 데이타를 
# 리턴할 수 없는 경우나, 데이타가 대량이어서 일부씩 처리하는 것이 필요한 경우, 혹은 모든 데이타를 미리 계산하면 속도가 느려서 그때 
# 그때 On Demand로 처리하는 것이 좋은 경우 등에 종종 사용된다.
# Generator Expression
# Generator Expression은 Generator Comprehension으로도 불리우는데, List Comprehension과 외관상 유사하다. List Comprehension은 앞뒤를
# [...] 처럼 대괄호로 표현한다면, Generator Expression (...) 처럼 둥근 괄호를 사용한다. 하지만 Generator Expression은 List 
# Comprehension과 달리 실제 리스트 컬렉션 데이타 전체를 리턴하지 않고, 그 표현식만을 갖는 Generator 객체만 리턴한다.
# 즉 실제 실행은 하지 않고, 표현식만 가지며 위의 yield 방식으로 Lazy Operation을 수행하는 것이다.
# 아래 예제는 1부터 1000개까지의 숫자에 대한 제곱값을 Generator Expression으로 표현한 것으로 여기서 Generator Expression을 할당받은 
# 변수 g는 Generator 타입 객체이다. 첫번째 for 루프를 사용하여 10개의 next() 문을 실행하여 처음 10개에 대한 제곱값만을 실행하였다. 
# 두번째 for 루프에서는 11번째부터 마지막까지 모두 실행하게 된다. Generator 객체 g는 상태를 유지하고 있으므로 두번째 for 루프에서
# 다음 숫자 11부터 계산을 수행한 것이다.
# 리스트 및 문자열 Iterable
''' for n in [1,2,3,4,5]:
    print(n)
for c in "Hello World":
    print(c)
class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index >= self.size:
            raise StopIteration
        n = self.data[self.index]
        self.index += 1
        return n
coll = MyCollection()
for x in coll:
    print(x)
# Generator 함수
def gen():
    yield 1
    yield 2
    yield 3
# Generator 객체
g = gen()
print(type(g))  # <class 'generator'>
# next() 함수 사용
n = next(g); print(n)  # 1
n = next(g); print(n)  # 2
n = next(g); print(n)  # 3
# for 루프 사용 가능
for x in gen():
    print(x)
# Generator Expression
g = (n*n for n in range(1001))
# g는 generator 객체
print(type(g))  # <class 'generator'>
# 리스트로 일괄 변환시
# mylist = list(g)
# 10개 출력
for i in range(10):
    value = next(g)
    print(value)
# 나머지 모두 출력 
for x in g:
    print(x) '''

# [쓰레드 (Thread)]
# 파이썬 프로그램은 기본적으로 하나의 쓰레드(Single Thread)에서 실행된다. 즉, 하나의 메인 쓰레드가 파이썬 코드를 순차적으로 실행한다. 
# 코드를 병렬로 실행하기 위해서는 별도의 쓰레드(Subthread)를 생성해야 하는데, 파이썬에서 쓰레드를 생성하기 위해서는 threading 모듈
# (High 레벨) 혹은 thread 모듈 (Low 레벨)을 사용할 수 있다. 일반적으로 쓰레드 처리를 위해서는 thread 모듈 위에서 구현된 threading
# 모듈을 사용하고 있으며, thread 모듈은 (deprecate 되어) 거의 사용하고 있지 않다.
# 파이썬(오리지날 파이썬 구현인 CPython)은 전역 인터프리터 락킹(Global Interpreter Lock) 때문에 특정 시점에 하나의 파이썬 코드만을
# 실행하게 되는데, 이 때문에 파이썬은 실제 다중 CPU 환경에서 동시에 여러 파이썬 코드를 병렬로 실행할 수 없으며 인터리빙(Interleaving)
# 방식으로 코드를 분할하여 실행한다. 다중 CPU 에서 병렬 실행을 위해서는 다중 프로세스를 이용하는 multiprocessing 모듈을 사용한다.
# threading 모듈
# 파이썬에서 쓰레드를 실행하기 위해서는, threading 모듈의 threading.Thread() 함수를 호출하여 Thread 객체를 얻은 후 Thread 객체의 
# start() 메서드를 호출하면 된다. 서브쓰레드는 함수 혹은 메서드를 실행하는데, 일반적인 구현방식으로 (1) 쓰레드가 실행할 함수 혹은
# 메서드를 작성하거나 또는 (2) threading.Thread 로부터 파생된 파생클래스를 작성하여 사용하는 방식 등이 있다.
# 먼저 첫번째 함수 및 메서드 실행 방식은 쓰레드가 실행할 함수 (혹은 메서드)를 작성하고 그 함수명을 hreading.Thread() 함수의 target
# 아큐먼트에 지정하면 된다. 예를 들어, 아래 예제에서 sum 이라는 함수를 쓰레드가 실행하도록 threading.Thread() 함수의 파라미터로 
# target=sum 을 지정하였다. 여기서 한가지 주의할 점은 target=sum() 처럼 지정하면, 이는 sum() 함수를 실행하여 리턴한 결과를 target에 
# 지정하는 것이므로 잘못된 결과를 초래할 수 있다. 만약 쓰레드가 실행하는 함수(혹은 메서드)에 입력 파라미터를 전달해야 한다면,
# args (혹은 키워드 아규먼트인 경우 kwargs) 에 필요한 파라미터를 지정하면 된다. args는 튜플로 파라미터를 전달하고, kwargs는 dict로 
# 전달한다. 아래 예제에서 sum() 함수는 두 개의 파라미터를 받아들이기 때문에 "args=(1, 100000)" 와 같이 입력파라미터를 지정하였다.
# threading.Thread 로부터 파생클래스를 만드는 방식은 Thread 클래스를 파생하여 쓰레드가 실행할 run() 메서드를 재정의해서 사용하는 
# 방식이다. Thread 클래스에서 run() 메서드는 쓰레드가 실제 실행하는 메서드이며, start() 메서드는 내부적으로 이 run() 메서드를 
# 호출한다. 예를 들어, 아래 예제(A)는 getHtml() 라는 함수를 사용한 방식인데 이를 예제(B)와 같이 파생클래스를 사용하는 방식으로
# 바꿔 쓸 수 있다. 예제(B)에서 t.start()는 HtmlGetter 클래스에서 재정의된 run() 메서드를 호출하게 된다. 
# (주: requests는 외부 HTTP 라이브러리로서 http://pythonstudy.xyz/python/article/403 아티클을 참고하십시오)
# 데몬 쓰레드
# Thread 클래스에서 daemon 속성은 서브쓰레드가 데몬 쓰레드인지 아닌지를 지정하는 것인데, 데몬 쓰레드란 백그라운드에서 실행되는
# 쓰레드로 메인 쓰레드가 종료되면 즉시 종료되는 쓰레드이다. 반면 데몬 쓰레드가 아니면 해당 서브쓰레드는 메인 쓰레드가 종료할 지라도
# 자신의 작업이 끝날 때까지 계속 실행된다.
# 아래 예제는 데몬 쓰레드를 예시하기 위한 것으로 Thread 객체의 daemon 속성을 True로 설정한 후 start() 하면, 해당 서브쓰레드는 
# 데몬 쓰레드가 되고 아래와 같이 메인 쓰레드가 곧바로 종료되면 getHtml 메서드를 마저 실행하지 못하고 바로 데몬 쓰레드를 종료하게 된다. 
# daemon 속성은 디폴트로 False 이므로 별도로 지정하지 않으면 메인 쓰레드가 종료되어도 서브쓰레드는 끝까지 작업을 수행한다.
''' import threading
def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)
t = threading.Thread(target=sum, args=(1, 100000))
t.start()
print("Main Thread")
# 예제(A)
import threading, requests, time
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()
print("### End ###")
# 예제(B)
import threading, requests, time
class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self) 
        self.url = url
    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')
t = HtmlGetter('http://google.com')
t.start()
print("### End ###")
import threading, requests, time
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
# 데몬 쓰레드
t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.daemon = True 
t1.start()
print("### End ###") '''


# [Python 데이터]

# [Python DB API]
# Python에서 데이타베이스를 엑서스하기 위한 한 방법으로 Python DB API를 사용할 수 있다. Python DB API는 여러 데이타베이스를
# 엑세스하는 표준 API 로서 여러 DB 엑세스 모듈에서 이 최소한의 API 인터페이스 표준을 따르고 있다. 표준 API는 크게 데이타
# 베이스를 연결하고, SQL 문을 실행하고, 연결을 닫는 등의 기본적인 DB 작업과 관련된 기능들을 정의하고 있다. Python DB API는
# 현재 버전 2.0을 사용하는데, 스펙은 PEP 249에 자세히 소개되어 있다.
# (주: 데이타베이스를 엑세스하는 또 다른 방식으로 ORM (Object Relational Mapping)이 있는데, 예를 들어 Django ORM, PonyORM,
# peewee 등이 ORM 방식을 사용한 데이타 엑세스를 제공한다.)
# Python에서 지원하는 데이타베이스는 매우 다양하기 때문에, Python에서 각 데이타베이스를 사용하기 위해서는 각각의 DB에
# 상응하는 별도의 DB 모듈을 다운받아야 한다 (주: sqlite3 는 Python 2.5 이상에서 기본 내장). 하지만 수많은 DB 모듈들이
# 있지만, 이들이 거의 모두 Python DB API 표준을 따르고 있으므로, 동일한 API를 사용해 데이타베이스를 사용할 수 있다. 
# Python에서는 거의 모든 데이타베이스를 사용할 수 있는데, 예를 들어 MySQL, PostgreSQL, MSSQL, Sqlite, Oracle, Sybase,
# Informix, mSQL 등과 같은 대표적인 DB 들이 모두 지원된다.

# [MySQL 쿼리]
# 1. MySQL DB 모듈
# Python에서 MySQL 데이타베이스를 사용하기 위해 우선 Python DB API 표준을 따르는 MySQL DB 모듈을 다운받아 설치한다.
# MySQL DB 를 지원하는 Python 모듈은 여러 가지가 있는데, 여기서는 PyMySql 이라는 모듈을 사용해 본다. 참고로 앞 아티클에서
# 언급하였듯이 다른 MySQL 모듈을 사용하더라도 동일한 API를 사용하게 된다.
# MySQL DB 모듈 중 하나인 PyMySql 모듈을 다음과 같이 설치한다.
# $ pip install PyMySQL
# 2. MySql 사용 절차
# Python에서 MySQL에 있는 데이타를 사용하는 일반적인 절차는 다음과 같다.
# PyMySql 모듈을 import 한다
# pymysql.connect() 메소드를 사용하여 MySQL에 Connect 한다. 호스트명, 로그인, 암호, 접속할 DB 등을 파라미터로 지정한다.
# DB 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져온다. DB 커서는 Fetch 동작을
# 관리하는데 사용되는데, 만약 DB 자체가 커서를 지원하지 않으면, Python DB API에서 이 커서 동작을 Emulation 하게 된다.
# Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보낸다.
# SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 데이타를 서버로부터 가져온 후,
# Fetch 된 데이타를 사용한다.
# 삽입, 갱신, 삭제 등의 DML(Data Manipulation Language) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 Connection 객체의
# commit() 메서드를 사용하여 데이타를 확정 갱신한다.
# Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫는다.
# 아래 예제들의 기본 샘플 데이타로 아래와 같은 customer 테이블이 있다고 가정하자.
# 3. MySql 쿼리
# SQL 쿼리는 SELECT 문을 작성하여 execute() 메서드를 실행하면 된다. 아래 예제는 위에서 설명한 일반적인 MySql 사용 절차를
# 따른 것으로, 간단한 SELECT 문을 실행한 후, 전체 ROW 데이타를 출력하는 예이다.
# import pymysql
# # MySQL Connection 연결
# conn = pymysql.connect(host='localhost', user='tester', password='',
#                        db='testdb', charset='utf8')
# # Connection 으로부터 Cursor 생성
# curs = conn.cursor()
# # SQL문 실행
# sql = "select * from customer"
# curs.execute(sql)
# # 데이타 Fetch
# rows = curs.fetchall()
# print(rows)     # 전체 rows
# # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')
# # Connection 닫기
# conn.close()
# 위의 예제에서 몇가지 주목할 점은
# (1) connect() 메서드에서 charset을 명시한 점이다. 종종 클라이언트의 charset이 제대로 설정되지 않으면 한글이 깨지는
#     경우가 발생할 수 있다.
# (2) 커서의 fetchall() 메서드는 모든 데이타를 한꺼번에 클라이언트로 가져올 때 사용된다. 또다른 fetch 메서드로서 fetchone()
#     은 한번 호출에 하나의 Row 만을 가져올 때 사용된다. fetchone()을 여러 번 호출하면, 호출 때 마다 한 Row 씩 데이타를 
#     가져오게 된다. 그리고 fetchmany(n) 메서드는 n개 만큼의 데이타를 한꺼번에 가져올 때 사용된다.
# (3) print(rows) 문은 전체 row들을 Tuple의 Tuple로서 출력하게 되고, row[0], row[1]와 같이 인덱스를 지정하면, 첫번째,
#     두번째 row 등을 가리키게 된다. 각 row는 Tuple로 리턴되며, 컬럼 순서대로 데이타가 표시된다 (주: 이러한 디폴트 Row 
#     데이타 형식을 흔히 Array based cursor라 부르고, 이는 connect() 혹은 cursor() 메서드에서 옵션으로 변경할 수 있다. 아래 참조.).
# 4. Parameter Placeholder
# 실제 업무에서 대부분의 SQL 문장에는 동적으로 컬럼 데이타값을 집어 넣어야 하는 경우가 상당히 많다. 동적 SQL문을 구성하기 위해서
# 파라미터값이 들어가는 위치에 Parameter Placeholder인 %s (MySql의 경우)를 넣고, execute() 메서드의 두번째 파라미터에 실제 
# 파라미터값들의 Tuple을 넣어 주면 된다. 예를 들어, 아래 예제에서 SELECT 문의 WHERE 절을 보면 category와 region 값이 들어가는
# 곳에 각각 %s 를 넣어 주었다. 그리고 execute() 메서드에서 첫번째 파라미터에는 SQL문을, 두번째 파라미터에는 (1, '서울') 이라는
# 파라미터값 튜플을 넣어 주었다. 튜플 안의 데이타는 SQL문에서 순서대로 적용되게 되는데, 특히 문자열의 경우 단일인용부호
# (Single Quote)와 같은 특수 문자들이 자동으로 Escape 되어 처리된다.
# Parameter Placeholder로 %s 를 사용하는데, 이 %s 는 일반 문자열 포맷팅에 사용하는 %s, %d 등과는 다른 것이다. 
# Parameter Placeholder에서는 문자열이건 숫자이건 모두 %s 를 사용하며, 문자열이라도 %s를 인용부호로 둘러싸지 않는다. 
# 또한 한가지 주의할 점은 Placeholder는 컬럼값을 대치할 때만 사용될 수 있다. 즉 테이블이나 기타 문장에 Placeholder 를 
# 사용할 수 없다.
# import pymysql
# # MySQL Connection 연결
# conn = pymysql.connect(host='localhost', user='tester', password='7890',
#                        db='testdb', charset='utf8')
# # Connection 으로부터 Dictoionary Cursor 생성
# curs = conn.cursor(pymysql.cursors.DictCursor)
# # SQL문 실행
# sql = "select * from customer where category=%s and region=%s"
# curs.execute(sql, (1, '서울'))
# # 데이타 Fetch
# rows = curs.fetchall()
# for row in rows:
#     print(row)
#     # 출력 : {'category': 1, 'id': 1, 'region': '서울', 'name': '김정수'}
#     print(row['id'], row['name'], row['region'])
#     # 1 김정수 서울
# # Connection 닫기
# conn.close()
# 만약 Python 문자열에서 사용하는 기본 String Interpolation을 사용하면 데이타에 특수 문자가 있는 경우 SQL문 문법 오류를 
# 발생시킬 수 있다. 예를 들어, 아래는 기본 String Interpolation을 사용한 예인데, 변수 data 안에 단일 인용부호가 있는 경우 
# SQL Syntax 에러를 유발시키게 된다. 또한 이러한 String Interpolation 혹은 문자열 결합(Concatenation)을 통해 동적 SQL 문을 
# 만드는 방법은 SQL Injection 공격에 쉽게 노출되는 문제점이 있다.
# # 잘못된 표현
# data = '서\'울'
# sql = "select * from customer where category=%s and region=%s" % (1, data)
# curs.execute(sql)
# 5. Dictionary 커서
# 위의 예제에서 또 한가지 주목할 점은 라인 8에 있는 cursor() 메서드이다. 이 cursor() 메서드 안에 DictCursor를 파라미터로
# 지정하였는데, 이는 디폴트인 Array based cursor가 아닌 Dictionary based cursor를 사용하겠다는 것을 의미한다. 디폴트 Array
# based cursor는 Row의 결과값을 배열로 (PyMyMsql에서 정확히는 튜플) 리턴하는데, cursor 생성시 DictCursor 옵션을 주면, Row 
# 결과를 Dictionary 형태로 리턴한다.
# curs = conn.cursor(pymysql.cursors.DictCursor)
# # ...생략...
# rows = curs.fetchall()
# for row in rows:
#   print(row)
#   # 출력 : {'category': 1, 'id': 1, 'region': '서울', 'name': '김정수'}
#   print(row['id'], row['name'], row['region'])
#   # 1 김정수 서울
# 위의 예에서 커서가 DictCursor이므로 for 루프 안의 print(row)는 Dictionary 형태로 Row 데이타를 출력하게 된다. 
# 또한 Row 데이타가 Dictionary이므로 row["id"], row["name"] 과 같이 컬럼명을 써서 컬럼값을 구할 수 있다. 
# 이렇게 컬럼인덱스 대신 컬럼명으로 컬럼을 찾게 되면 코드 가독성을 높일 수 있고, 특히 컬럼수가 많을 경우 유용하게 사용될 수 있다.
''' import pymysql
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='tester', password='',
                       db='testdb', charset='utf8')
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
# SQL문 실행
sql = "select * from customer"
curs.execute(sql)
# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows
# print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')
# Connection 닫기
conn.close() '''

# [MySQL DML]
# 1. MySQL DML
# SQL에서 데이타 조작하는 INSERT, UPDATE, DELETE 문을 DML(Data Manipulation Language)이라 한다. MySQL에서 INSERT, UPDATE, 
# DELETE를 사용하는 일반적인 절차는 앞 아티클 (MySQL 쿼리)과 유사하다.
# MySQL에 DML을 사용하는 일반적인 절차는 다음과 같다.
# PyMySql 모듈을 import 한다
# pymysql.connect() 메소드를 사용하여 MySQL에 Connect 한다. 호스트명, 로그인, 암호, 접속할 DB 등을 파라미터로 지정한다.
# DB 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져온다.
# Cursor 객체의 execute() 메서드를 사용하여 INSERT, UPDATE 혹은 DELETE 문장을 DB 서버에 보낸다.
# 삽입, 갱신, 삭제 등이 모두 끝났으면 Connection 객체의 commit() 메서드를 사용하여 데이타를 Commit 한다. 
# 디폴트로 Autocommit 이 아니므로 commit()을 명시적으로 호출한다. 자동커밋을 원하는 경우, connect() 메서드 호출시
# autocommit=True 를 지정한다.
# Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫는다.
# 2. INSERT 문
# 데이타를 테이블에 추가하기 위해 INSERT문을 사용한다. INSERT문에 사용하는 각 컬럼값들은 직접 값을 지정(Hard code)하거나 
# Parameter Placeholder를 사용할 수 있다.
# 아래 예제는 두 개의 데이타를 INSERT 하고 Commit 하는 예이다. 여기서 한가지 주의할 점은 데이타 INSERT만 실행하고 Commit하지 
# 않으면, 테이블의 데이타는 변경되지 않는다는 점이다.
# import pymysql
# conn = pymysql.connect(host='localhost', user='tester', password='7890',
#                        db='testdb', charset='utf8')
# curs = conn.cursor()
# sql = """insert into customer(name,category,region)
#          values (%s, %s, %s)"""
# curs.execute(sql, ('홍길동', 1, '서울'))
# curs.execute(sql, ('이연수', 2, '서울'))
# conn.commit()
# conn.close()
# execute() 메서드는 하나의 Row (하나의 Tuple 데이타)를 치환하여 실행하는 반면, executemany() 메소드는 복수개의 Tuple
# 데이타 (즉, Tuple of Tuples)를 하나의 DML 문에 적용하게 된다. 아래 예제에서 executemany()는 3개의 INSERT 문을 수행하는 
# 것과 동일한 효과를 갖는다.
# data = (
#     ('홍진우', 1, '서울'),
#     ('강지수', 2, '부산'),
#     ('김청진', 1, '서울'),
# )
# sql = """insert into customer(name,category,region)
#          values (%s, %s, %s)"""
# curs.executemany(sql, data)
# conn.commit()
# 3. UPDATE, DELETE 문
# 기존의 데이타를 수정하기 위해 UPDATE 문을 사용하고, 삭제하기 위해서 DELETE 문을 사용한다. UPDATE, DELETE 문에 사용하는 각 
# 컬럼값들은 직접 값을 지정(Hard code)하거나 Parameter Placeholder를 사용할 수 있다.
# 아래 예제는 하나의 UPDATE 문과 하나의 DELETE 문을 실행하고, Commit하는 예이다. UPDATE 문은 Region이 "서울"인 데이타를
# 모두 "서울특별시"로 변경하는 것이고, DELETE 문은 id가 6인 customer 데이타를 삭제하는 것이다.
# import pymysql
# conn = pymysql.connect(host='localhost', user='tester', password='7890',
#                        db='testdb', charset='utf8')
# curs = conn.cursor()
# sql = """update customer
#          set region = '서울특별시'
#          where region = '서울'"""
# curs.execute(sql)
# sql = "delete from customer where id=%s"
# curs.execute(sql, 6)
# conn.commit()
# conn.close()
# 4. try와 with 문의 사용
# SQL Connection을 열고 프로그램 중간에서 에러가 발생하면, Connection은 그대로 열려 있는 상태로 있을 수 있다. 이렇게 오픈되어
# 있는 Connection이 증가하면, 나중에 새로운 Connection을 오픈할 수 없게 되는데, 이를 Connection Leak 이라 부른다. 이러한 
# Connection Leak을 막기 위하여 아래 예제와 같이 try...finally 블력을 사용하여 finally에서 항상 Conneciton을 Close해 주는 
# 것이 좋다.
# import pymysql
# conn = pymysql.connect(host='localhost', user='tester', password='7890',
#                        db='testdb', charset='utf8')
# try:
#     # INSERT
#     with conn.cursor() as curs:
#         sql = "insert into customer(name,category,region) values (%s, %s, %s)"
#         curs.execute(sql, ('이광수', 1, '서울'))
#     conn.commit()
#     # SELECT
#     with conn.cursor() as curs:
#         sql = "select * FROM customer"
#         curs.execute(sql)
#         rs = curs.fetchall()
#         for row in rs:
#             print(row)
# finally:
#     conn.close()
# 위 예제의 try 블럭을 보면, INSERT와 SELECT 문을 각기 다른 커서에서 사용하고 있다. 첫번째 INSERT 실행 시 with 문으로 커서를 
# 만들어 자동으로 커서 리소스가 해제되도록 하였고, 두번째 SELECT 시에도 with 문으로 해당 커서가 자동 해제되도록 하였다. 
# 이러한 예제에서 보듯이, SQL 객체들을 다룰 때 try...finally 나 with 문을 적절히 사용하여 리소스를 해제해 주는 것이 좋다.
''' import pymysql
conn = pymysql.connect(host='localhost', user='tester', password='7890',
                       db='testdb', charset='utf8')
try:
    # INSERT
    with conn.cursor() as curs:
        sql = "insert into customer(name,category,region) values (%s, %s, %s)"
        curs.execute(sql, ('이광수', 1, '서울'))
    conn.commit()
    # SELECT
    with conn.cursor() as curs:
        sql = "select * FROM customer"
        curs.execute(sql)
        rs = curs.fetchall()
        for row in rs:
            print(row)
finally:
    conn.close() '''

# [SQLite 사용]
# 1. sqlite3 소개
# SQLite는 별도의 DB 서버가 필요없이 DB 파일에 기초하여 데이타베이스 처리를 구현한 Embedded SQL DB 엔진이다. SQLite는 별도의 
# 복잡한 서버 설치가 필요 없고, 쉽고 편리하게 사용할 수 있다는 점에서 널리 사용되고 있다. 오늘날 대부분의 Mac OS X 나
# 리눅스에서는 SQLite을 기본적으로 내장하고 있지만, 만약 시스템에 내장되어 있지 않는 경우는 http://www.sqlite.org 에서
# 다운받아 설치할 수 있다. SQLite는 기본적으로 SQLite DB 엔진과 "sqlite3" 라는 Command line tool 을 갖고 있다.
# 다음은 sqlite3 커맨드 라인 툴을 사용하여 샘플 DB (test.db)를 만들고 customer 테이블을 생성하고, 데이타를 INSERT/SELECT 해 본
# 예이다. "sqlite3 test.db" 명령문은 만약 test.db 파일이 있으면 해당 파일을 오픈하고, 파일이 없으면 새 파일을 생성한다.
# 2. pysqlite
# Python에서 SQLite 을 사용하기 위해서는 보통 pysqlite 으로 불리우는 Language binding (주: SQLite 라이브러리를 내부에서 사용)을 
# 사용하는데, pysqlite 은 Python 2.5 이상에서 기본적으로 내장되어 있다.
# pysqlite 를 import 하기 위해서는 아래와 같이 "import sqlite3" 를 사용한다.
# $ python
# Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 19 2015, 20:19:30)
# [GCC 4.2.1 (Apple Inc. build 5577)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import sqlite3
# >>> sqlite3.version
# '2.6.0'
# >>>
# 3. SQLite 쿼리
# SQLite를 사용하기 위해서는 우선 사용할 db 파일 (예: test.db)을 sqlite3.connect() 메서드로 오픈하고, SQL 쿼리를 실행하여
# 데이타를 사용한 후, 마지막에 Connection을 닫으면 된다. DB Connection이 연결되면 Connection 객체가 리턴되는데, 이 객체로부터 
# 커서를 생성하고 커서 객체의 execute() 명령을 실행하여 SQL 쿼리를 실행한다. 아래 예제는 간단한 SELECT 문을 실행한 후, 전체 ROW
# 데이타를 출력하는 예이다.
# import sqlite3
# # SQLite DB 연결
# conn = sqlite3.connect("test.db")
# # Connection 으로부터 Cursor 생성
# cur = conn.cursor()
# # SQL 쿼리 실행
# cur.execute("select * from customer")
# # 데이타 Fetch
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# # Connection 닫기
# conn.close()
# 4. Parameterized Query
# 실제 업무에서 대부분의 SQL 문장에는 동적으로 컬럼 데이타값을 집어 넣어야 하는 경우가 많은데, 이때 Parameterized Query를 
# 사용한다. SQLite에서는 두 가지 방식으로 Parameterized Query를 만들 수 있다. 즉, ? (물음표)를 Placeholder로 사용하는 방식와
# ":Id" 처럼 파라미터 이름을 명식하는 Named Placeholder 방식이 있다. 동적 SQL문을 구성하기 위해선 파라미터값이 들어가는 위치에
# Parameter Placeholder를 넣고, execute() 메서드의 두번째 파라미터에 실제 파라미터값들의 Tuple을 넣어 주면 된다.
# Parameterized Query는 문자열 결합이나 문자열 Interpolation에서 발생할 수 있는 SQL Injection 문제를 해결하는 방식으로
# 알려져 있다.
# Parameter Placeholder에서는 문자열이건 숫자이건 모두 ? (혹은 Named Placeholder) 를 사용하며, 문자열이라도 Placeholder를 
# 인용부호로 둘러싸지 않는다. 또한 한가지 주의할 점은 Placeholder는 컬럼값을 대치할 때만 사용될 수 있다. 즉 테이블이나 기타 
# 문장에 Placeholder 를 사용할 수 없다.
# ? Placeholder
# 아래 예제에서 SELECT 문의 WHERE 절을 보면 category와 region 값이 들어가는 곳에 각각 ? 마크를 넣어 주었다. 그리고 execute() 
# 메서드에서 첫번째 파라미터에는 SQL문을, 두번째 파라미터에는 (1, 'SEA') 이라는 파라미터값 튜플을 넣어 주었다. 튜플 안의 
# 데이타는 SQL문에서 순서대로 적용되게 되는데, 특히 문자열의 경우 단일인용부호(Single Quote)와 같은 특수 문자들이 자동으로 
# Escape 되어 처리된다.
# import sqlite3
#  conn = sqlite3.connect("test.db")
#  cur = conn.cursor()
# sql = "select * from customer where category=? and region=?"
# cur.execute(sql, (1, 'SEA'))
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# conn.close()
# Named Placeholder
# 아래 예제는 Named Placeholder를 사용한 예로서, where 절의 :Id 가 Named Placeholder이다. 이 Id의 값은 execute() 메서드의 
# 두번째 파라미터에 지정되는데, 이 값은 Tuple이 아닌 Dictionary 형태로 Id 값이 지정된다.
# sql = "select * from customer where id = :Id"
# cur.execute(sql, {"Id": 1})
# 5. DML (INSERT, UPDATE, DELETE)
# SQL에서 데이타 조작하는 INSERT, UPDATE, DELETE 문을 DML(Data Manipulation Language)이라 한다. DML문을 사용하는 방식은
# 위의 쿼리를 사용하는 방식과 거의 비슷하다. INSERT, UPDATE, DELETE 문에서도 Parameterized Query를 사용한다. 단, DML은 
# 리턴되는 데이타가 없으므로 fetch 를 사용하지 않는다. 또한 디폴트로 Autocommit 이 아니기 때문에, execute() 로 DML 문장을 
# 실행한 후에, Connection 객체의 commit() 메서드를 호출해야 한다. Autocommit 을 사용할 경우에는 아래 connect() 에서
# 예시하였듯이, isolation_level 을 None 으로 설정한다.
# import sqlite3
# conn = sqlite3.connect("test.db")
# # Autocommit 사용시:
# # conn = sqlite3.connect("test.db", isolation_level=None)
# cur = conn.cursor()
# sql = "insert into customer(name,category,region) values (?, ?, ?)"
# cur.execute(sql, ('홍길동', 1, '서울'))
# conn.commit()
# conn.close()
# DML에서 사용하면 유용한 메서드로 executemany() 메소드가 있다. executemany() 메소드는 복수 개의 Row 데이타를 한꺼번에
# 처리하는데 유용하다. 아래 예제는 executemany() 메서드를 사용하여 3개의 Row들을 INSERT 하는 효과를 갖는다.
# import sqlite3
# conn = sqlite3.connect("test.db")
# cur = conn.cursor()
# data = (
#     ('홍진우', 1, '서울'),
#     ('강지수', 2, '부산'),
#     ('김청진', 1, '서울'),
# )
# sql = "insert into customer(name,category,region) values (?, ?, ?)"
# cur.executemany(sql, data)
# conn.commit()
# conn.close()
# 6. try와 with 문의 사용
# Connection, Cursor 와 같은 리소스들이 Leak 되는 것을 방지하기 위하여 try...finally 혹은 with 문을 사용할 수 있다.
# try...finally와 with 문은 블럭 내 에러가 발생하더라도 마지막 항상 리소스를 해제하는 역활을 하기 때문에, 데이타베이스 
# 코딩에서 자주 사용된다. 아래 예제는 Connection 리소스를 닫기 위해 with 문을 사용하는 예이다.
# import sqlite3
# conn = sqlite3.connect("test.db")
# with conn:
#     cur = conn.cursor()
#     cur.execute("select * from customer")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
''' import sqlite3
conn = sqlite3.connect("test.db")
cur = conn.cursor()
data = (
    ('홍진우', 1, '서울'),
    ('강지수', 2, '부산'),
    ('김청진', 1, '서울'),
)
sql = "insert into customer(name,category,region) values (?, ?, ?)"
cur.executemany(sql, data)
conn.commit()
conn.close() '''

# [MSSQL 사용] 
# 1. Microsoft SQL Server DB 모듈
# Python에서 Microsoft SQL Server 데이타베이스를 사용하기 위해 우선 Python DB API 표준을 따르는 MSSQL DB 모듈을 다운받아 
# 설치한다. MSSQL DB 를 지원하는 Python 모듈은 여러 가지가 있는데, 여기서는 pymssql 이라는 모듈을 사용해 본다. pymssql은
# Python DB API (PEP-249) 스펙을 따르는 FreeTDS 위에 구현된 파이썬 모듈이다.
# MSSQL DB 모듈 중 하나인 pymssql 모듈을 다음과 같이 설치한다.
# $ pip install pymssql
# 2. MSSQL 사용 절차
# Python에서 MSSQL에 있는 데이타를 사용하는 일반적인 절차는 다음과 같다.
# pymssql 모듈을 import 한다
# pymssql.connect() 메소드를 사용하여 MSSQL에 Connect 한다. 호스트명, 로그인, 암호, 접속할 DB 등을 파라미터로 지정할 수 있다.
# DB 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져온다. DB 커서는 Fetch 동작을 관리하는데
# 사용된다.
# Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보낸다.
# SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 데이타를 서버로부터 가져온 후,
# Fetch 된 데이타를 사용한다.
# 삽입, 갱신, 삭제 등의 DML(Data Manipulation Language) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 Connection 객체의 
# commit() 메서드를 사용하여 데이타를 확정 갱신한다.
# Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫는다.
# 아래 예제들의 기본 샘플 데이타로 아래와 같은 Customer 테이블이 있다고 가정하자.
# 3. MSSQL 쿼리
# SQL 쿼리는 SELECT 문을 작성하여 execute() 메서드를 실행하면 된다. 아래 예제는 위에서 설명한 일반적인 MSSQL 사용 절차를 따른 
# 것으로, 간단한 SELECT 문을 실행한 후, 전체 ROW 데이타를 출력하는 예이다.
# # pymssql 패키지 import
# import pymssql
# # MSSQL 접속
# conn = pymssql.connect(host=r"(local)", database='MyDB', charset='utf8')
# # Connection 으로부터 Cursor 생성
# cursor = conn.cursor()
# # SQL문 실행
# cursor.execute('SELECT * FROM Customer;')
# # 데이타 하나씩 Fetch하여 출력
# row = cursor.fetchone()
# while row:
#     print(row[0], row[1])
#     row = cursor.fetchone()
# 연결 끊기
# conn.close()            
# 위의 예제에서 몇가지 주목할 점은
# (1) connect() 메서드에서 host와 database 만을 지정하였는데, 이는 기본적으로 Windows Authentication 을 사용하여 SQL Server에 
# 접속하게 된다. 만약 SQL Authentication을 사용할 경우는 아래처럼 user와 password 를 지정한다.
#     conn = pymssql.connect(host=r"(local)", user='sa', password='pwd', database='MyDB')
# 또한, 한글이 깨지는 경우 charset을 UTF8으로 지정하면 된다.
# (2) 커서의 fetchone() 메서드는 데이타를 클라이언트로 하나씩 가져올 때 사용된다. fetchone()을 여러 번 호출하면, 호출 때 마다 
# 한 Row 씩 데이타를 가져오게 된다. 그리고, 모든 데이타를 한꺼번에 클라이언트로 가져올 때는 fetchall()을, n개 만큼의 데이타만
# 가져올 때는 fetchmany(n)를 사용한다.
# (3) DB 사용이 끝난 경우 close() 메서드를 호출하여 연결을 끊어 준다.
''' import pymssql
# MSSQL 접속
conn = pymssql.connect(host=r"(local)", database='MyDB', charset='utf8')
# Connection 으로부터 Cursor 생성
cursor = conn.cursor()
# SQL문 실행
cursor.execute('SELECT * FROM Customer;')
# 데이타 하나씩 Fetch하여 출력
row = cursor.fetchone()
while row:
    print(row[0], row[1])
    row = cursor.fetchone()
연결 끊기
conn.close() '''  

# [JSON 데이타]
# 1. JSON
# JSON은 JavaScript Object Notation의 약자로서 JavaScript 문법에 영향을 받아 개발된 Lightweight한 데이타 표현 방식이다. 
# JSON은 데이타를 교환하는 한 포맷으로서 그 단순함과 유연함 때문에 널리 사용되고 있다. 특히 웹 브라우져와 웹서버 사이에
# 데이타를 교환하는데 많이 사용되고 있다. 가장 많이 사용되는 JSON 포맷은 Key-Value Pair의 컬렉션이다.
# Python은 기본적으로 JSON 표준 라이브러리(json)를 제공하고 있는데, "import json" 을 사용하여 JSON 라이브러리를 사용할 수 있다 
# (주: Python 2.6 이상).
# JSON 라이브러리를 사용하면, Python 타입의 Object를 JSON 문자열로 변경할 수 있으며(JSON 인코딩), 또한 JSON 문자열을 다시 
# Python 타입으로 변환할 수 있다 (JSON 디코딩).
# 2. JSON 인코딩
# Python Object (Dictionary, List, Tuple 등) 를 JSON 문자열로 변경하는 것을 JSON Encoding 이라 부른다. JSON 인코딩을 위해서는
# 우선 json 라이브러리를 import 한 후, json.dumps() 메서드를 써서 Python Object를 문자열로 변환하면 된다.
# 예를 들어, 아래 코드는 customer 라는 Python Dictionary 객체를 JSON 문자열로 인코딩하는 예이다. 결과물 jsonString은 JSON 표현을
# 갖는 문자열(str 타입)이다.
# import json
# # 테스트용 Python Dictionary
# customer = {
#     'id': 152352,
#     'name': '강진수',
#     'history': [
#         {'date': '2015-03-11', 'item': 'iPhone'},
#         {'date': '2016-02-23', 'item': 'Monitor'},
#     ]
# }
# # JSON 인코딩
# jsonString = json.dumps(customer)
# # 문자열 출력
# print(jsonString)
# print(type(jsonString))   # class str
# 위의 코드를 실행하면 JSON 문자열이 한 줄로 길게 표현됨을 알 수 있다. 이렇게 축약된 JSON 문자열은 다른 컴퓨터나 네트워크 상에
# 보낼 때 유용하지만, 화면에 표시할 필요가 있을 경우는 읽기가 불편하다. JSON 문자열을 읽기 편하게 할 필요가 있을 경우에는,
# 아래와 같이 "indent" 옵션을 json.dumps() 메서드 안에 지정하면 된다. 코드 아래는 Identation 이 사용된 JSON 문자열 표현이다.
# jsonString = json.dumps(customer, indent=4)
# print(jsonString)
# {
#     "history": [
#         {
#             "date": "2015-03-11",
#             "item": "iPhone"
#         },
#         {
#             "date": "2016-02-23",
#             "item": "Monitor"
#         }
#     ],
#     "id": 152352,
#     "name": "\uac15\uc9c4\uc218"
# }
# 3. JSON 디코딩
# JSON 문자열을 Python 타입 (Dictionary, List, Tuple 등) 으로 변경하는 것을 JSON Decoding 이라 부른다. JSON 디코딩은 
# json.loads() 메서드를 사용하여 문자열을 Python 타입으로 변경하게 된다.
# 아래 예제는 JSON 문자열을 Python Dictionary로 변경한 예이다.
# import json
# # 테스트용 JSON 문자열
# jsonString = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, 
# {"date": "2016-02-23", "item": "Monitor"}]}'
# # JSON 디코딩
# dict = json.loads(jsonString)
# # Dictionary 데이타 체크
# print(dict['name'])
# for h in dict['history']:
#     print(h['date'], h['item'])
''' import json
# 테스트용 Python Dictionary
customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}
# JSON 인코딩
jsonString = json.dumps(customer)
print(jsonString)
print(type(jsonString))   # class str
jsonString = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'
# JSON 디코딩
dict = json.loads(jsonString)
# Dictionary 데이타 체크
print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item']) '''

# [파일 데이타 처리]
# 1. 텍스트 파일
# Python에서 파일을 처리하기 위해선 - 다른 언어에서와 마찬가지로 - 파일을 오픈하고, 데이타를 읽거나 쓴 후, 파일을 닫으면 된다.
# 파일을 오픈하기 위해서는 내장함수 open()을 사용하는데, 첫번째 파라미터로 오픈할 파일명을 지정하면 된다. open() 함수는 다양한 
# 파라미터를 지정할 수 있는데, 흔히 사용되는 파라마터로 파일모드를 결정하는 mode 와 파일인코딩 방식을 지정하는 encoding 등을 
# 들 수 있다.
# 파일을 오픈한 후, 파일을 읽기 위해서는 read(), readline(), readlines() 등의 메서드를 사용하고, 쓰기 위해서는 write(), 
# writelines() 등의 메서드를 사용한다. 여기서 한가지 주목할 점은 writeline() 메서드가 없다는 점인데, 다음 라인으로 가기 
# 위해서는 write() 메서드에서 "\n" 를 지정해 주어야 한다. Python은 Universal Newline 이라고 하여 플랫폼에 상관없이 라인
# Delimeter로 "\n"을 사용한다. 실행 플랫폼이 윈도우즈의 경우 이 Universal Newline은 CRLF (\r\n) 으로 변경되고, 맥이나 
# 리눅스에서는 LF (\n)로 자동으로 사용된다.
# 아래 예제는 텍스트 파일에 간단히 두 라인의 텍스트를 쓰는 코드이다.
# f = open('test.txt', mode='wt', encoding='utf-8')
# f.write("Hello, World\n");
# f.write("안녕하세요?")
# f.close()
# 파일모드
# 파일모드는 파일을 읽을 것인지 쓸 것인지 혹윽 텍스트 파일인지 바이너리 파일인지 등을 지정할 때 사용한다. 파일모드에는 
# 읽기(r), 쓰기(w 혹은 x), 추가(a), 수정(+) 모드를 지정할 수 있으며, 텍스트 파일(t), 바이너리 파일(b) 를 지정할 수 있다.
# 특히, w 모드는 파일이 이미 있으면, 먼저 그 내용을 삭제하고 새로 시작하지만, x 모드는 파일이 이미 있으면, FileExistsError 를
# 발생시킨다. 만약 파일모드를 지정하지 않으면, 디폴트로 텍스트 읽기 (rt) 모드가 설정된다.
# 파일인코딩
# Python의 문자열을 파일로 쓸 때 문자열은 바이트로 변경되는데, 이때 인코딩 방식에 따라 다른 바이트 결과를 가질 수 있다. 
# 또한 파일을 읽어 들일 때 인코딩 방식에 따라 다른 문자열로 읽혀 들일 수 있다. 따라서, 파일을 오픈할 때 encoding 파라미터를
# 지정해서 어떤 인코딩 방식을 사용하는지 명시적으로 지정는 것이 좋다. 위의 예제에서는 흔히 많이 사용되는 UTF-8 인코딩 방식을 
# 설정하였다.
# 만약 encoding 파라미터를 지정하지 않으면 시스템 디폴트 인코딩 방식을 사용한다. 시스템 디폴트 인코딩 방식은 아래와 같이 확인할
# 수 있다.
# 또 다른 예제로서 아래는 텍스트 파일을 읽는 예이다. 첫번째 [예제 A]는 readline() 메서드를 사용하여 각 라인을 읽어 들여 
# 프린트한 예이다. 이때 첫라인의 데이타를 갖는 s1 은 맨끝에 \n 값을 가지고 있음에 유의하자. 즉, readline() 메서드는 CR/LF 
# 라인 문자를 모두 리턴한다. 따라서 [예제 A]에서 print() 출력을 하게 되면, Hello World 다음에 한 줄이 더 생기게 된다
# (print가 마지막에 새 라인으로 이동하므로). 이를 방지하기 위해 [예제 B] 처럼 sys.stdout.write() 를 사용할 수 있다.
# [예제 B]는 파일객체와 함께 for 루프를 사용한 예제로서, open() 함수부터 리턴된 파일 Object를 사용하여 for 루프를 돌리면, 
# 파일로부터 한 라인씩 리턴하게 된다.
# # 예제 A
# f = open('test.txt', mode='rt', encoding='utf-8')
# s1 = f.readline()  # Hello, World\n
# s2 = f.readline()  # 안녕하세요?
# print(s1)
# print(s2)
# f.close()
# # 예제 B
# import sys
# f = open('test.txt', mode='rt', encoding='utf-8')
# for line in f:
#     sys.stdout.write(line)
# f.close()
# 2. try...finally 와 with 문
# 파일을 오픈한 후에는 사용 후 반드시 닫아주어야 하는데, 중간에 에러가 발생하더라도 반드시 닫아주기 위해 아래 예제와
# 같이 try...finally 를 사용할 수 있다.
# try:
#     f = open('test.txt', mode='rt', encoding='utf-8')
#     for line in f:
#         print(line)
# finally:
#     f.close()
# try...finally 를 보다 간결하게 표현하기 위해 아래와 같이 with 문을 사용할 수 있다. 아래 예제에서 with 블력을 벗어나면
# 파일객체 f 는 자동으로 close된다.
# with open('test.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         print(line)
# 3. 바이너리 파일
# 바이너리 파일을 읽기 위해서는 파일모드를 rb 로, 쓰기 위해서는 wb 로 지정한다. 파일을 처리를 위해 흔히 사용되는 메서드들로서,
# read(n) 매소드는 n 바이트만큼의 데이타를 읽어 들이고, ftell() 은 현재의 파일 위치를 리턴하고, fseek()는 특정 위치로 파일 
# 포인터를 옮기는 일을 한다. (주: read(n) 메서드가 텍스트 파일에 사용되면 n 개의 (바이트가 아닌) 문자를 읽어 들인다. 만약 n 을
# 생략하면 모든 데이타를 읽어 들인다.)
# 바이너리 파일은 그 자체가 바이트를 처리하는 것이므로 텍스트 파일에서 사용하는 Universal Newline 변환이나 인코딩을 사용하지 
# 않는다.
# 아래 예제는 이미지 바이너리 파일을 읽어 한 바이트씩 프린트하는 예이다.
# with open("test.png", "rb") as f:
#     byte = f.read(1)
#     while byte != b"":
#         print(byte)
#         byte = f.read(1)
# 또다른 예제로서 아래는 정수 리스트를 바이너리 파일에 출력한 후, 다시 읽어 들여 프린트 해보는 예제이다. 바이너리 파일로 부터
# 데이타를 읽고 쓸 때는 기본적으로 bytes 클래스를 사용하게 된다. 아래 예제를 보면, 리스트를 파일에 쓰기 전에 bytes()를 
# 호출하여 bytes 타입으로 변경했음을 볼 수 있다. 또한 두번째 바이너리 읽기 예제에서 보듯이 read() 메서드를 써서 리턴되는 
# 객체(content)의 타입은 bytes 클래스이다.
# # 바이너리 쓰기
# data = [1, 2, 3, 4, 5]
# with open("test.bin", "wb") as f:
#     f.write(bytes(data))
# # 바이너리 읽기
# with open("test.bin", "rb") as f:
#     content = f.read()   # 모두 읽음
#     print(type(content)) # bytes class
#     for b in content:
#         print(b)
''' f = open('test.txt', mode='wt', encoding='utf-8')
f.write("Hello, World\n");
f.write("안녕하세요?")
f.close()
f = open('test.txt', mode='rt', encoding='utf-8')
s1 = f.readline()  # Hello, World\n
s2 = f.readline()  # 안녕하세요?
print(s1)
print(s2)
f.close()
import sys
f = open('test.txt', mode='rt', encoding='utf-8')
for line in f:
    sys.stdout.write(line)
f.close()
try:
    f = open('test.txt', mode='rt', encoding='utf-8')
    for line in f:
        print(line)
finally:
    f.close()
data = [1, 2, 3, 4, 5]
with open("test.bin", "wb") as f:
    f.write(bytes(data))
# 바이너리 읽기
with open("test.bin", "rb") as f:
    content = f.read()   # 모두 읽음
    print(type(content)) # bytes class
    for b in content:
        print(b) '''

# [CSV 파일 사용하기]
# 1. CSV 파일
# CSV란 Comma-separated values의 약자로서 CSV 파일은 각 라인의 컬럼들이 콤마로 분리된 텍스트 파일 포맷이다. 가장 간단한 형태의
# CSV 파일은 문자열을 콤마로 Split 하여 처리하면 되지만, 간혹 컬럼 데이타에 콤마가 있을 경우 이중인용부호로 감싸서 데이타 내의
# 콤마를 Escape하기 (예: "Lee, Alex") 때문에, 파이썬에 내장된 csv 모듈을 사용하여 .csv 파일을 처리하는 것이 좋다.
# 2. CSV 파일 읽기
# CSV 파일을 읽기 위해서는 먼저 파이썬에 기본 내장된 csv 모듈을 import 한다. 다음 .csv 파일을 오픈하고 파일객체를
# csv.reader(파일객체) 에 넣으면 된다. csv.reader() 함수는 Iterator 타입인 reader 객체를 리턴하므로 for 루프를 돌며 한 
# 라인씩 가져올 수 있다. 이때 리턴되는 각 라인은 컬럼들을 나열한 리스트(list) 타입이다.
# 아래 예제는 data.csv 라는 CSV 파일을 읽어 각 라인을 출력하는 예이다.
# import csv
# f = open('data.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# for line in rdr:
#     print(line)
# f.close()    
# (입력 : data.csv 파일 내용)
# 1,김정수,2017-01-19 11:30:00,25
# 2,박민구,2017-02-07 10:22:00,35
# 3,정순미,2017-03-22 09:10:00,33
# (출력)
# ['1', '김정수', '2017-01-19 11:30:00', '25']
# ['2', '박민구', '2017-02-07 10:22:00', '35']
# ['3', '정순미', '2017-03-22 09:10:00', '33']    
# 3. CSV 파일 쓰기
# CSV 파일을 쓰기 위해서는 .csv 파일을 쓰기모드로 오픈하고 파일객체를 csv.writer(파일객체) 에 넣으면 된다. 
# CSV writer는 writerow() 라는 메서드를 통해 list 데이타를 한 라인 추가하게 된다. 윈도우즈의 경우 csv 모듈에서 데이타를
# 쓸 때 각 라인 뒤에 빈 라인이 추가되는 문제가 있는데, 이를 없애기 위해 (파이썬 3 에서) 파일을 open 할 때 newline='' 와 같은
# 옵션을 지정한다 (주: 파이썬 2의 경우는 newline 옵션 없이 바이너리 모드로 오픈할 것).
# 아래 예제는 output.csv 라는 CSV 파일에 2개 라인을 추가하는 예이다.
# import csv    
# f = open('output.csv', 'w', encoding='utf-8', newline='')
# wr = csv.writer(f)
# wr.writerow([1, "김정수", False])
# wr.writerow([2, "박상미", True])
# f.close()
# 4. TSV 파일
# CSV 파일과 비슷하지만, 콤마 대신 Tab으로 컬럼을 분리하는 파일포맷을 TSV 파일이라 한다. TSV 파일은 컬럼 delimiter만 차이가 
# 나므로, csv 모듈의 reader() 혹은 writer() 함수에서 delimiter='\t' 옵션만 지정해 주면 나머지는 CSV와 동일하다.
# import csv
# # .tsv 쓰기    
# f = open('test.tsv', 'w', encoding='utf-8', newline='')
# wr = csv.writer(f, delimiter='\t')
# wr.writerow([1, "김정수", False])
# wr.writerow([2, "박상미", True])
# f.close()
# # .tsv 읽기
# f = open('test.tsv', 'r', encoding='utf-8')
# rdr = csv.reader(f, delimiter='\t')
# r = list(rdr)
# print("Id=%s : Name=%s" % (r[0][0], r[0][1]))
# f.close()
# 특히, 위 예제에서 csv.reader()로부터 리턴된 객체를 list(reader객체)와 같이 리스트로 변환하였는데, 이는 데이타 양이 적을 때
# 데이타를 메모리로 한꺼번에 가져와 처리할 때 편리하다.
''' import csv
f = open('data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    print(line)
f.close()
import csv    
f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "김정수", False])
wr.writerow([2, "박상미", True])
f.close()
import csv
# .tsv 쓰기    
f = open('test.tsv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f, delimiter='\t')
wr.writerow([1, "김정수", False])
wr.writerow([2, "박상미", True])
f.close()
# .tsv 읽기
f = open('test.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)
print("Id=%s : Name=%s" % (r[0][0], r[0][1]))
f.close() '''


# [Python 활용]

# [정규 표현식 Regex]
# 1. 정규 표현식 (Regular Expression)
# 정규 표현식은 특정한 규칙을 가진 문자열의 패턴을 표현하는 데 사용하는 표현식(Expression)으로 텍스트에서 특정 문자열을
# 검색하거나 치환할 때 흔히 사용된다. 예를 들어, 웹페이지에서 전화번호나 이메일 주소를 발췌한다거나 로그파일에서 특정
# 에러메시지가 들어간 라인들을 찾을 때 정규 표현식을 사용하면 쉽게 구현할 수 있다. 정규 표현식은 간단히 정규식, Regex 
# 등으로 불리우곤 한다.
# 2. 정규 표현식 사용
# 정규식에서 가장 단순한 것은 특정 문자열을 직접 리터럴로 사용하여 해당 문자열을 검색하는 것이다. 예를 들어, 로그 파일에
# "에러 1033" 이라는 문자열을 검색하여 이 문자열이 있으면 이를 출력하고 없으면 None을 리턴하는 경우이다. 이러한 간단한 검색을
# 파이썬에서 실행하는 방법은 아래와 같다.
# 먼저 파이썬에서 정규표현식을 사용하기 위해서는 Regex를 위한 모듈인 re 모듈을 사용한다.
# re 모듈의 compile 함수는 정규식 패턴을 입력으로 받아들여 정규식 객체를 리턴하는데, 즉 re.compile(검색할문자열) 와 같이 함수를
# 호출하면 정규식 객체 (re.RegexObject 클래스 객체)를 리턴하게 된다.
# re.RegexObject 클래스는 여러 메서드들을 가지고 있는데, 이 중 여기서는 특정 문자열을 검색하여 처음 맞는 문자열을 리턴하는
# search() 메서드를 사용해 본다. 이 search() 는 처음 매칭되는 문자열만 리턴하는데, 매칭되는 모든 경우를 리턴하려면 findall() 을
# 사용한다. search()는 검색 대상이 있으면 결과를 갖는 MatchObject 객체를 리턴하고, 맞는 문자열이 없으면 None 을 리턴한다.
# MatchObject 객체로부터 실제 결과 문자열을 얻기 위해서는 group() 메서드를 사용한다.
# import re
# text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
# regex = re.compile("에러 1033")
# mo = regex.search(text)
# if mo != None:
#     print(mo.group()) 
# 3. 전화번호 발췌하기
# 정규 표현식은 단순한 리터럴 문자열을 검색하는 것보다 훨씬 많은 기능들을 제공하는데, 즉 특정 패턴의 문자열을 검색하는데 매우
# 유용하다. 그 한가지 예로 웹페이지나 텍스트에서 특정 패턴의 전화번호를 발췌하는 기능에 대해 알아보자. 전화번호의 패턴은
# 032-232-3245 와 같이 3자리-3자리-4자리로 구성되어 있다고 가정하자. 정규식에서 숫자를 의미하는 기호로 \d 를 사용한다. 
# 여기서 d는 digit 을 의미하고 0 ~ 9 까지의 숫자 중 아무 숫자나 될 수 있다. 따라서, 위 전화번호 패턴을 정규식으로 표현하면
#  \d\d\d-\d\d\d-\d\d\d\d 와 같이 될 수 있다. 아래는 이러한 패턴을 사용하여 전화번호를 발췌하는 예이다.
# import re
# text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
# regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# matchobj = regex.search(text)
# phonenumber = matchobj.group()
# print(phonenumber)    
# 위 예제에서 re.compile(전화번호패턴) 함수는 전화번호 패턴에 갖는 정규식 객체를 리턴하게 되고, search()를 사용하여 첫번째 
# 전화번호 패턴에 매칭되는 번호를 리턴한다. 그리고 이로부터 실제 전화번호를 얻기 위해서는 group() 메서드를 사용하였다.
# 4. 다양한 정규식 패턴 표현
# 위의 전화번호 예제에서는 숫자를 표현하는 \d 만을 살펴보았는데, 정규 표현식에는 매우 다양한 문법과 기능들이 제공되고 있다. 
# 아래는 이러한 다양한 정규식 표현 중 자주 사용되는 패턴들을 정리한 것이다.
# 패턴	설명	예제
# ^	이 패턴으로 시작해야 함	^abc : abc로 시작해야 함 (abcd, abc12 등)
# $	이 패턴으로 종료되어야 함	xyz$ : xyz로 종료되어야 함 (123xyz, strxyz 등)
# [문자들]	문자들 중에 하나이어야 함. 가능한 문자들의 집합을 정의함.	[Pp]ython : "Python" 혹은 "python"
# [^문자들]	[문자들]의 반대로 피해야할 문자들의 집합을 정의함.	[^aeiou] : 소문자 모음이 아닌 문자들
# |	두 패턴 중 하나이어야 함 (OR 기능)	a | b : a 또는 b 이어야 함
# ?	앞 패턴이 없거나 하나이어야 함 (Optional 패턴을 정의할 때 사용)	\d? : 숫자가 하나 있거나 없어야 함
# +	앞 패턴이 하나 이상이어야 함	\d+ : 숫자가 하나 이상이어야 함
# *	앞 패턴이 0개 이상이어야 함	\d* : 숫자가 없거나 하나 이상이어야 함
# 패턴{n}	앞 패턴이 n번 반복해서 나타나는 경우	\d{3} : 숫자가 3개 있어야 함
# 패턴{n, m}	앞 패턴이 최소 n번, 최대 m 번 반복해서 나타나는 경우 (n 또는 m 은 생략 가능)	\d{3,5} : 숫자가 3개,
# 4개 혹은 5개 있어야 함
# \d	숫자 0 ~ 9	\d\d\d : 0 ~ 9 범위의 숫자가 3개를 의미 (123, 000 등)
# \w	문자를 의미	\w\w\w : 문자가 3개를 의미 (xyz, ABC 등)
# \s	화이트 스페이스를 의미하는데, [\t\n\r\f] 와 동일	\s\s : 화이트 스페이스 문자 2개 의미 (\r\n, \t\t 등)
# .	뉴라인(\n) 을 제외한 모든 문자를 의미	.{3} : 문자 3개 (F15, 0x0 등)
# 정규식 패턴의 한 예로 "에러 {에러번호}"와 같은 형식을 띄는 부분을 발췌해 내는 예제를 살펴보자. 여기서 에러 패턴은 
# "에러" 라는 리터럴 문자열과 공백 하나, 그 뒤에 1개 이상의 숫자이다. 이를 표현하면 아래와 같다.
# import re
# text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
# regex = re.compile("에러\s\d+")
# mc = regex.findall(text)
# print(mc)
# # 출력: ['에러 1122', '에러 1033']
# 위 예제는 첫번째 패턴 매칭값을 리턴하는 search() 메서드 대신 패턴에 매칭되는 모든 결과를 리턴하는 findall()을 사용하였다.
# findall()는 결과 문자열들의 리스트(list)를 리턴한다.
# 5. 정규식 그룹(Group)
# 정규 표현식에서 ( ) 괄호는 그룹을 의미한다. 예를 들어, 전화번호의 패턴을 \d{3}-\d{3}-\d{4} 와 같이 표현하였을 때, 지역번호 
# 3자를 그룹1으로 하고 나머지 7자리를 그룹2로 분리하고 싶을 때, (\d{3})-(\d{3}-\d{4}) 와 같이 둥근 괄호로 묶어 두 그룹으로 
# 분리할 수 있다.
# 이렇게 분리된 그룹들은 MatchObject의 group() 메서드에서 그룹 번호를 파라미터로 넣어 값을 가져올 수 있는데, 첫번째 그룹 
# 지역번호는 group(1) 으로, 두번째 그룹은 group(2) 와 같이 사용한다. 그리고 전체 전화번호를 가져올 때는 group() 혹은 group(0)
# 을 사용한다.
# import re
# text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
# regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
# matchobj = regex.search(text)
# areaCode = matchobj.group(1)
# num = matchobj.group(2)
# fullNum = matchobj.group()
# print(areaCode, num) # 032 232-3245
# 그룹을 위와 같이 숫자로 인덱싱하는 대신 그룹이름을 지정할 수도 있는데 이를 정규식에서 Named Capturing Group 이라 한다. 
# 파이썬에서 Named Capturing Group을 사용하는 방법은 (?P<그룹명>정규식) 와 같이 정규식 표현 앞에 ?P<그룹명>을 쓰면 된다. 
# 그리고 이후 MatchObject에서 group('그룹명') 을 호출하면 캡쳐된 그룹 값을 얻을 수 있다.
# import re
# text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
# regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})')
# matchobj = regex.search(text)
# areaCode = matchobj.group("area")
# num = matchobj.group("num")
# print(areaCode, num)  # 032 232-3245
''' import re
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
    print(mo.group()) 
import re
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)   
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러\s\d+")
mc = regex.findall(text)
print(mc)
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num) # 032 232-3245
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group("area")
num = matchobj.group("num")
print(areaCode, num)  # 032 232-3245 '''

# [numpy 사용하기]
# 1. numpy 패키지
# numpy는 과학 계산을 위한 라이브러리로서 다차원 배열을 처리하는데 필요한 여러 유용한 기능을 제공하고 있다.
# numpy는 pip을 사용하여 아래와 같이 간단히 설치할 수 있다.
# $ pip install numpy    
# 2. numpy 배열
# numpy에서 배열은 동일한 타입의 값들을 가지며, 배열의 차원을 rank 라 하고, 각 차원의 크기를 튜플로 표시하는 것을 shape 라 한다.
# 예를 들어, 행이 2이고 열이 3인 2차원 배열에서 rank는 2 이고, shape는 (2, 3) 이 된다.
# numpy 배열을 생성하는 방법은 파이썬 리스트를 사용하는 방법과 numpy에서 제공하는 함수를 사용하는 방법이 있다. 아래 예제에서 
# list1은 4개의 요소를 갖는 리스트인데, 이를 array() 함수에 넣어 numpy 배열을 생성하는데, 이 배열의 rank는 1이 되고, 
# shape는 (4, ) 가 된다. 튜플에 하나의 요소만 있으면 문법상 콤마를 뒤에 붙인다. 두번째 배열 b는 2x3 배열로서 shape는 (2, 3)이 
# 되는데, 한가지 주의할 점은 array() 안에 하나의 리스트만 들어가므로 리스트의 리스트를 넣어야 한다.
# import numpy as np
# list1 = [1, 2, 3, 4]
# a = np.array(list1)
# print(a.shape) # (4, )
# b = np.array([[1,2,3],[4,5,6]])
# print(b.shape) # (2, 3)
# print(b[0,0])  # 1    
# numpy에서 제공하는 함수를 사용하여 numpy 배열을 만드는 방법을 살펴보자. 이러한 기능을 제공하는 함수로는 zeros(), ones(),
# full(), eye() 등이 있는데, zeros()는 해당 배열에 모두 0을 집어 넣고, ones()는 모두 1을 집어 넣는다. full()은 배열에
# 사용자가 지정한 값을 넣는데 사용하고, eye()는 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성한다.
# 아래 예제는 이들 함수들을 사용하여 numpy 배열을 생성한 예이다. 그리고 마지막 예는 0부터 n-1 까지의 숫자를 생성하는 
# range(n) 함수와 배열을 다차원으로 변형하는 reshape()를 통해 간단하게 샘플 배열을 생성해 본 것이다.
# import numpy as np
# a = np.zeros((2,2))
# print(a)
# # 출력:
# # [[ 0.  0.]
# #  [ 0.  0.]]
# a = np.ones((2,3))
# print(a)
# # 출력:
# # [[ 1.  1.  1.]
# #  [ 1.  1.  1.]]
# a = np.full((2,3), 5)
# print(a)
# # 출력:
# # [[5 5 5]
# #  [5 5 5]]
# a = np.eye(3)
# print(a)
# # 출력:
# # [[ 1.  0.  0.]
# #  [ 0.  1.  0.]
# #  [ 0.  0.  1.]]
# a = np.array(range(20)).reshape((4,5))
# print(a)
# # 출력:
# # [[ 0  1  2  3  4]
# #  [ 5  6  7  8  9]
# #  [10 11 12 13 14]
# #  [15 16 17 18 19]]
# 3. numpy 슬라이싱
# numpy 배열은 파이썬 리스트와 마찬가지로 슬라이스(Slice)를 지원한다. numpy 배열을 슬라이싱하기 위해서는 각 차원별로 슬라이스
# 범위를 지정한다.
# import numpy as np
# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# arr = np.array(lst)
# # 슬라이스
# a = arr[0:2, 0:2]
# print(a)
# # 출력:
# # [[1 2]
# #  [4 5]]
# a = arr[1:, 1:]
# print(a)
# # 출력:
# # [[5 6]
# #  [8 9]]
# 4. numpy 정수 인덱싱 (integer indexing)
# numpy 슬라이싱이 각 배열 차원별 최소-최대의 범위를 정하여 부분 집합을 구하는 것이라면, 정수 인덱싱은 각 차원별로 선택되어지는
# 배열요소의 인덱스들을 일렬로 나열하여 부분집합을 구하는 방식이다. 즉, 임의의 numpy 배열 a 에 대해 a[[row1, row2], [col1, col2]] 와 
# 같이 표현하는 것인데, 이는 a[row1, col1] 과 a[row2, col2] 라는 두 개의 배열요소의 집합을 의미한다.
# 예를 들어, 아래 예제에서 a[[0, 2], [1, 3]] 은 정수 인덱싱으로서 이는 a[0, 1] 과 a[2, 3] 등 2개의 배열요소를 가리킨다.
# import numpy as np
# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# a = np.array(lst)
# # 정수 인덱싱
# s = a[[0, 2], [1, 3]]
# print(s)
# # 출력
# # [2 12]
# 5. numpy 부울린 인덱싱 (boolean indexing)
# numpy 부울린 인덱싱은 배열 각 요소의 선택여부를 True, False로 표현하는 방식이다. 만약 배열 a 가 2 x 3 의 배열이이라면, 부울린
# 인덱싱을 정의하는 numpy 배열도 2 x 3 으로 만들고 선택할 배열요소에 True를 넣고 그렇지 않으면 False를 넣으면 된다.
# 예를 들어, 아래 예제에서 3 x 3 배열 a 중 짝수만 뽑아내는 부울린 인덱싱 배열(numpy 배열)을 사용하여 짝수 배열 n 을 만드는
# 예이다.
# import numpy as np
# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# a = np.array(lst)
# bool_indexing_array = np.array([
#     [False,  True, False],
#     [True, False,  True],
#     [False,  True, False]
# ])
# n = a[bool_indexing_array];
# print(n)    
# 부울린 인덱싱 배열에 True/False 값을 일일이 지정하는 방법 이외에 표현식을 사용하여 부울린 인덱싱 배열을 생성하는 방법이 있다.
# 예를 들어, 배열 a 에 대해 짝수인 배열요소만 True로 만들고 싶다면, bool_indexing = (a % 2 == 0) 와 같이 표현할 수 있다.
# 아래 예제는 이러한 표현을 사용하는 것을 예시한 것이고, 특히 마지막에 a[ a % 2 == 0 ] 와 같이 부울린 인덱싱 표현식을 배열 
# 인덱스안에 넣어 간단하게 표현할 수도 있다.
# import numpy as np
# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# a = np.array(lst)
# # 배열 a 에 대해 짝수면 True, 홀수면 False 
# bool_indexing = (a % 2 == 0)
# print(bool_indexing)
# # 출력: 부울린 인덱싱 배열
# # [[False  True False]
# #  [ True False  True]
# #  [False  True False]]
# # 부울린 인덱스를 사용하여 True인 요소만 뽑아냄
# print(a[bool_indexing])
# # 출력:
# # [2 4 6 8]
# # 더 간단한 표현
# n = a[ a % 2 == 0 ]
# print(n)
# 6. numpy 연산
# numpy를 사용하면 배열간 연산을 쉽게 실행할 수 있다. 연산은 +, -, *, / 등의 연산자를 사용할 수도 있고, add(), substract(),
# multiply(), divide() 등의 함수를 사용할 수도 있다. 예를 들어, 아래 예제와 같이 배열 a 와 b 가 있을때, a + b를 하면 각 배열
# 요소의 합을 구하는데 즉 a[0]+b[0], a[1]+b[1], ... 과 같은 방식으로 결과를 리턴하게 된다.
# import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# # 각 요소 더하기
# c = a + b
# # c = np.add(a, b)
# print(c)  # [5 7 9]
# # 각 요소 빼기
# c = a - b
# # c = np.subtract(a, b)
# print(c)  # [-3 -3 -3]
# # 각 요소 곱하기
# # c = a * b
# c = np.multiply(a, b)
# print(c)  # [4 10 18]
# # 각 요소 나누기
# # c = a / b
# c = np.divide(a, b)
# print(c)  # [0.25 0.4 0.5]
# numpy에서 vector와 matrix의 product를 구하기 위해서 dot() 함수를 사용한다. 아래 예제는 두 matrix의 product를 구한 예이다.
# import numpy as np
# lst1 = [
#     [1,2],
#     [3,4]
# ]
# lst2 = [
#     [5,6],
#     [7,8]
# ]
# a = np.array(lst1)
# b = np.array(lst2)
# c = np.dot(a, b)
# print(c)
# # 출력:
# # [[19 22]
# #  [43 50]]    
# numpy은 배열간 연산을 위한 위해 많은 함수들을 제공하는데, 예를 들어, 각 배열 요소들을 더하는 sum() 함수, 각 배열 요소들을 곱하는 prod() 함수 등을 사용할 수 있다. 이들 함수에 선택옵션으로 axis 을 지정할 수 있는데, 예를 들어 sum()에서 axis가 1 이면 행끼리 더하는 것이고, axis가 0 이면 열끼리 더하는 것이다.
# import numpy as np
# a = np.array([[1,2],[3,4]])
# s = np.sum(a)
# print(s)   # 10
# # axis=0 이면, 컬럼끼리 더함
# # axis=1 이면, 행끼리 더함
# s = np.sum(a, axis=0)
# print(s)   # [4 6]
# s = np.sum(a, axis=1)
# print(s)   # [3 7]
# s = np.prod(a)
# print(s)   # 24
''' import numpy as np
list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a.shape) # (4, )
b = np.array([[1,2,3],[4,5,6]])
print(b.shape) # (2, 3)
print(b[0,0])  # 1    
a = np.zeros((2,2))
print(a)
a = np.ones((2,3))
print(a)
a = np.full((2,3), 5)
print(a)
a = np.eye(3)
print(a)
a = np.array(range(20)).reshape((4,5))
print(a)
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
# 슬라이스
a = arr[0:2, 0:2]
print(a)
a = arr[1:, 1:]
print(a)
lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)
# 정수 인덱싱
s = a[[0, 2], [1, 3]]
print(s)
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
bool_indexing_array = np.array([
    [False,  True, False],
    [True, False,  True],
    [False,  True, False]
])
n = a[bool_indexing_array];
print(n)    
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
# 배열 a 에 대해 짝수면 True, 홀수면 False 
bool_indexing = (a % 2 == 0)
print(bool_indexing)
print(a[bool_indexing])
# 더 간단한 표현
n = a[ a % 2 == 0 ]
print(n)
a = np.array([1,2,3])
b = np.array([4,5,6])
# 각 요소 더하기
c = a + b
# c = np.add(a, b)
print(c)  # [5 7 9]
# 각 요소 빼기
c = a - b
# c = np.subtract(a, b)
print(c)  # [-3 -3 -3]
# 각 요소 곱하기
# c = a * b
c = np.multiply(a, b)
print(c)  # [4 10 18]
# 각 요소 나누기
# c = a / b
c = np.divide(a, b)
print(c)  # [0.25 0.4 0.5]
lst1 = [
    [1,2],
    [3,4]
]
lst2 = [
    [5,6],
    [7,8]
]
a = np.array(lst1)
b = np.array(lst2)
c = np.dot(a, b)
print(c)
a = np.array([[1,2],[3,4]])
s = np.sum(a)
print(s)   # 10
# axis=0 이면, 컬럼끼리 더함
# axis=1 이면, 행끼리 더함
s = np.sum(a, axis=0)
print(s)   # [4 6]
s = np.sum(a, axis=1)
print(s)   # [3 7]
s = np.prod(a)
print(s)   # 24 '''

# [파이썬 Web Scraping]
# 1. 파이썬 Web Scraping
# 웹사이트에서 HTML을 읽어와 필요한 데이타를 긁어오는 것을 Web Scraping이라 한다. 이 과정은 크게 웹페이지를 읽어오는 과정과 
# 읽어온 HTML 문서에서 필요한 데이타를 뽑아내는 과정으로 나뉠 수 있다.
# 웹페이지를 읽어오는 일은 여러 모듈을 사용할 수 있는데, 파이썬에서 기본적으로 제공하는 urllib, urllib2 을 사용하거나 편리한 
# HTTP 라이브러리로 많이 쓰이고 있는 requests 를 설치해 사용할 수 있다. 만약 기존 코드를 유지보수하는 일이 아니라면 requests 
# 를 사용할 것을 권장한다.
# 2. requests - 웹페이지 읽어오기
# HTTP 라이브러리인 requests를 사용하기 위해서는 먼저 아래와 같이 pip을 이용하여 requests 패키지를 설치한다.
# pip install requests
# 기본적인 requests 기능을 먼저 살펴보면, requests는 HTTP GET, POST, PUT, DELETE 등을 사용할 수 있으며, 편리한 데이타 인코딩
# 기능을 제공하고 있다. 즉, 데이타를 Dictionary로 만들어 GET, POST 등에서 사용하면 필요한 Request 인코딩을 자동으로 처리해 준다.
# import requests
# # GET
# resp = requests.get('http://httpbin.org/get')
# print(resp.text)
# # POST
# dic = {"id": 1, "name": "Kim", "age": 10}
# resp = requests.post('http://httpbin.org/post', data=dic)
# print(resp.text)
# resp = requests.put('http://httpbin.org/put')
# resp = requests.delete('http://httpbin.org/delete')    
# requests.get(url) 함수를 사용하면 해당 웹페이지 호출 결과를 가진 Response 객체를 리턴한다. Response 객체는 HTML Response와
# 관련된 여러 attribute들을 가지고 있는데, 예를 들어, Response의 status_code 속성을 체크하여 HTTP Status 결과를 체크할 수 있고,
# Response 에서 리턴된 데이타를 문자열로 리턴하는 text 속성이 있으며, Response 데이타를 바이트(bytes)로 리턴하는 content 속성
# 등이 있다. 또한, 만약 Response에서 에러가 있을 경우 프로그램을 중단하도록 할 때는 Response 객체의 raise_for_status() 메서드를 
# 호출할 수 있다.
# 아래 예제는 다음 홈페이지에 접속해서 HTML 문서를 가져와 화면에 출력하는 예이다.
# import requests
# resp = requests.get( 'http://daum.net' )
# # resp.raise_for_status()
# if (resp.status_code == requests.codes.ok):
#     html = resp.text
#     print(html)
# requests 에서의 한글 깨짐 문제
# 여기서 간혹 겪게되는 한글 깨짐 문제에 대해 잠깐 집고 넘어가자. requests 에서 웹 호출을 진행한 후 결과는 Response 객체에 담기게
# 되는데, Response의 text 속성은 str 클래스 타입으로서 보통 requests 모듈에서 자동으로 데이타를 인코딩해 준다. 즉, requests는
# HTTP 헤더를 통해 결과 데이타의 인코딩 방식을 추측하여 Response 객체의 encoding 속성에 그 값을 지정하고, text 속성을 엑세스할
# 때 이 encoding 속성을 사용한다. 만약 인코딩 방식을 변경해야 한다면, text 속성을 읽기 전에 Response의 encoding 속성을 변경하면
# 된다.
# 이제 실제 예를 들어 보면, 네이버 홈페이지는 한글 출력에 문제가 없지만, 네이버 증권사이트 웹페이지는 (영문 OS에서 테스트한 결과)
# 한글이 깨져 보이게 된다. 원인을 찾아보기 위해 Response 객체가 어떤 인코딩인지 체크해 보았다. 네이버 홈페이지는 UTF-8을 
# 사용하고, 네이버 증권사이트는 ISO-8859-1을 사용하고 있다.
# >>> resp = requests.get('http://naver.com') # 네이버 홈
# >>> resp.encoding
# 'UTF-8'
# >>> resp = requests.get('http://finance.naver.com') # 증권
# >>> resp.encoding
# 'ISO-8859-1'
# 인코딩이 유니코드 인코딩(예: UTF-8 등)이거나 한글 인코딩(예: EUC-KR)이면 일반적으로 한글이 깨지지 않지만, ISO-8859-1와 같이
# 영문 인코딩이면 한글이 깨지게 된다. 이를 해결하는 방법은 미리 Response 객체의 encoding 을 한글인코딩(예: EUC-KR)이나 
# None (인코딩 추즉을 하지 않도록) 으로 지정한 후, text 속성을 읽으면 된다. 예를 들어, 아래 예제는 네이버 증권사이트의
# ISO-8859-1 인코딩 문제를 처리한 코드이다.
# import requests
# resp = requests.get('http://finance.naver.com/')
# resp.raise_for_status()
# resp.encoding=None   # None 으로 설정
# #resp.encoding='euc-kr'  # 한글 인코딩
# html = resp.text
# print(html)
# 3. BeautifulSoup - 웹페이지 파싱
# 웹페이지 HTML 문서를 파싱(Parsing)하기 위해서는 BeautifulSoup 라는 모듈을 사용할 수 있다. 먼저 BeautifulSoup 를 아래와 같이 
# 설치한다.
# pip install beautifulsoup4
# BeautifulSoup를 사용하기 위해서는 먼저 BeautifulSoup 모듈을 import하여야 하는데 모듈명은 bs4 이다. bs4 모듈이 import 된 후, 
# bs4.BeautifulSoup(HTML문서) 생성자를 호출하여 BeautifulSoup 객체를 생성한다.
# import bs4
# html = "<html><body>...생략...</body></html>"
# bs = bs4.BeautifulSoup(html, 'html.parser')
# BeautifulSoup 객체에서 특정 HTML 태그(들)을 찾기 위해 select() 메서드를 사용하는데, 이 메서드의 파라미터로 어떤 태크(들)을
# 찾을 지를 CSS 스타일의 Selector로 지정하면 된다. 예를 들어, select('.news li') 는 news 라는 CSS 클래스 안이 모든 li 태그들을
# 리턴하게 된다.
# 리턴된 결과는 태그(s4.element.Tag)들의 리스트(list) 인데, 각 태그 요소(bs4.element.Tag)로부터 태그내 문자열을 리턴하기 
# 위해서는 getText()를, 특정 태그 attribute를 얻기 위해서는 get('attribute명') 메서드 등을 사용할 수 있다.
# 아래 예제는 네이버 증권사이트에서 주요 Top 뉴스 제목을 발췌하는 코드이다.
# # -*- coding: utf-8 -*-
# import requests, bs4
# resp = requests.get('http://finance.naver.com/')
# resp.raise_for_status()
# resp.encoding='euc-kr'
# html = resp.text
# bs = bs4.BeautifulSoup(html, 'html.parser')
# tags = bs.select('div.news_area h2 a') # Top 뉴스
# title = tags[0].getText()
# print(title)
''' import requests
# GET
resp = requests.get('http://httpbin.org/get')
print(resp.text)
# POST
dic = {"id": 1, "name": "Kim", "age": 10}
resp = requests.post('http://httpbin.org/post', data=dic)
print(resp.text)
resp = requests.get('http://finance.naver.com/')
resp.raise_for_status()
resp.encoding=None   # None 으로 설정
#resp.encoding='euc-kr'  # 한글 인코딩
html = resp.text
print(html)
import requests, bs4
resp = requests.get('http://finance.naver.com/')
resp.raise_for_status()
resp.encoding='euc-kr'
html = resp.text
bs = bs4.BeautifulSoup(html, 'html.parser')
tags = bs.select('div.news_area h2 a') # Top 뉴스
title = tags[0].getText()
print(title) '''

# [파이썬 Selenium 사용하기]
# 1. Selenium 소개
# Selenium은 웹 브라우져를 컨트롤하여 웹 UI 를 Automation 하는 도구 중의 하나이다. Selenium은 Selenium Server와 Selenium Client가
# 있는데, 로컬 컴퓨터의 웹 브라우져를 컨트롤하기 위해서는 Selenium Client 를 사용한다 (여기서는 Selenium 3 사용). Selenium 
# Client는 WebDriver라는 공통 인터페이스(Common interface)와 각 브라우져 타입별(IE, Chrome, FireFox 등)로 하나씩 있는 Browser
# Driver로 구성되어 있다.
# 2. Selenium 설치
# Selenium을 설치하기 위해서는 먼저 아래와 같이 pip 을 사용하여 Selenium Client 모듈을 설치한다.
# pip install selenium
# 다음으로 사용할 브라우저별 Selenium 드라이버를 설치한다. 드라이버가 설치된 후, 해당 드라이버의 경로를 실행 PATH에 넣어 준다.
# 아래는 대표적인 브라우저별 설치 링크이다. 특별한 이유가 없다면 Selenium이 가장 잘 동작하는 Firefox를 사용하는 것이 좋다.
# Firefox : https://github.com/mozilla/geckodriver/releases
# Chrome : https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# 3. Selenium 사용법
# Selenium을 사용하기 위해서는 먼저 selenium.webdriver 모듈을 import 한 후, webdriver.Firefox() 를 호출하여 브라우져를 
# 실행시킨다. 만약 크롬을 사용할 경우 webdriver.Chrome()을 호출하고, Edge를 사용할 경우 webdriver.Edge()을 호출한다.
# 브라우져를 띄운 상태에서 특정 웹사이트로 이동하기 위해서는 아래와 같이 browser 객체의 get() 메서드를 사용한다.
# from selenium import webdriver
# browser = webdriver.Firefox()
# # browser = webdriver.Chrome()
# browser.get("http://python.org")  
# Selenium은 웹페이지 내의 특정 요소(들)을 찾는 많은 메서드들을 제공하고 있는데, 이들은 보통 한 요소를 리턴하는 
# find_element_*() 혹은 복수 요소를 리턴하는 find_elements_*() 메서드로 구분된다. 자주 사용되는 몇가지 검색 메서드를 예를 들면,
# 특정 태그 id 로 검색하는 find_element_by_id(), 특정 태그 name 속성으로 검색하는 find_element_by_name(), CSS 클래스명으로
# 검색하는 find_element_by_class_name(), CSS selector를 사용해 검색하는 find_element_by_css_selector() 등이 있는데, 예상되는
# 결과가 복수이면 find_element_* 대신 find_elements_* 를 사용한다.
# 검색 결과 리턴되는 객체는 FirefoxWebElement 와 같이 *WebElement 타입의 객체가 되는데, 리턴된 요소는 WebElement 타입 타입의 
# 속성이나 메서드를 사용하여 데이타를 얻거나 특정 행위를 할 수 있다. 예를 들어, WebElement의 text는 요소 내의 문자열을 리턴하고,
# tag_name 은 해당 요소의 태크명 (예: a, span) 을 리턴하며, clear() 메서드를 호출하면 text 입력 영역을 초기화하고, click() 
# 메서드를 호출하면 해당 요소를 클릭한다.
# 아래 예제는 python.org 웹사이트를 방문해서 상단 메인 메뉴 문자열을 출력하고, PyPI 메뉴를 클릭한 후 5초 후에 브라우저를 
# 종료하는 예이다.
# from selenium import webdriver
# import time
# browser = webdriver.Firefox()
# browser.get("http://python.org")
# menus = browser.find_elements_by_css_selector('#top ul.menu li')
# pypi = None
# for m in menus:
#     if m.text == "PyPI":
#         pypi = m
#     print(m.text)
# pypi.click()  # 클릭
# time.sleep(5) # 5초 대기
# browser.quit() # 브라우저 종료
''' from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://python.org")
menus = browser.find_elements_by_css_selector('#top ul.menu li')
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)
pypi.click()  # 클릭
time.sleep(5) # 5초 대기
browser.quit() # 브라우저 종료 '''

# [파이썬 엑셀 사용하기]
# 1. 파이썬에서 엑셀 사용하기
# 파이썬에서 엑셀 데이타를 핸들링하기 위해서는 openpyxl, xlrd, xlrw 등의 외부 패키지를 설치해서 사용한다. 여기서는 openpyxl 
# 패키지를 아래와 같이 설치하여 사용한다.
#     pip install openpyxl
# 2. 엑셀 데이타 읽고 쓰기
# 엑셀을 다루는 가장 기초적인 부분은 데이타를 읽고 쓰는 동작이므로, 먼저 엑셀 파일을 열고 그 안의 데이타를 읽고 몇 개의 데이타를
# 쓰는 동작을 살펴 보자. 아래 예제는 국영수 점수를 담은 엑셀 파일을 읽어 각 학생별 국영수 합계를 구하여 다시 저장하는 예이다.
# 엑셀 입력 파일은 아래와 같다고 가정한다. 합계 부분은 추가해야 하는 부분이다.
# import openpyxl
# # 엑셀파일 열기
# wb = openpyxl.load_workbook('score.xlsx')
# # 현재 Active Sheet 얻기
# ws = wb.active
# # ws = wb.get_sheet_by_name("Sheet1")
# # 국영수 점수를 읽기
# for r in ws.rows:
#     row_index = r[0].row   # 행 인덱스
#     kor = r[1].value
#     eng = r[2].value
#     math = r[3].value
#     sum = kor + eng + math
#      # 합계 쓰기
#     ws.cell(row=row_index, column=5).value = sum
#     print(kor, eng, math, sum)
# # 엑셀 파일 저장
# wb.save("score2.xlsx")
# wb.close()
# 먼저 엑셀 파일을 오픈하기 위해 openpyxl.load_workbook(엑셀파일명) 함수를 호출하여 Workbook 객체를 얻는다. 하나의 Workbook에는
# 여러 개의 Worksheet 들이 있는데 통상 엑셀은 기본으로 Sheet1, Sheet2, Sheet3 등 3개의 시트를 생성한다. 엑셀 파일을 열면 보통
# 첫번째 시트가 Active Sheet가 되므로 Worksheet 객체의 active 를 통해 현재 워크시트를 가져올 수 있지만, 엑셀은 이전 저장시
# 마지막에 선택된 시트를 Active Sheet로 하므로 wb.get_sheet_by_name(시트명) 을 사용하는 것이 더 안전하다.
# 워크시트는 행(Row)과 열(Column)로 구성되어 있는데, 시트 내에 데이타가 있는 부분의 행들은 시트객체.rows 를 통해 엑세스할 수 
# 있고, 마찬가지로 시트객체.columns는 유효 컬럼들을 엑세스하는데 사용한다. 위의 예제에서 각 행을 하나씩 가져오기 위해 for 루프로
# ws.rows로부터 한 row씩 가져오고 있다. 각 row는 그 행 안에 있는 cell 들의 집합으로 처음 cell은 r[0]과 같이 인덱스 0을 사용한다.
# 첫 cell 즉 r[0]의 값을 리턴하기 위해 r[0].value 을 사용한다.
# 특정 cell 에 값을 지정하기 위해 cell.value 에 값을 넣으면 되는데, 시트에서 cell을 지정하기 위해 ws["A1"]과 같이 엑셀식 cell 
# 지정법을 사용할 수 있고, 또한 행열 인덱스를 사용하여 ws.cell(row=행인덱스, column=열인덱스) 표현을 사용할 수도 있다.
# 엑셀의 변경 내용을 저장하기 위해서는 Workbook 객체에서 save() 메서드를 사용하며, 엑셀 사용이 모두 끝난 경우 close() 메서드를 
# 호출한다.
''' import openpyxl
# 엑셀파일 열기
wb = openpyxl.load_workbook('score.xlsx')
# 현재 Active Sheet 얻기
ws = wb.active
# ws = wb.get_sheet_by_name("Sheet1")
# 국영수 점수를 읽기
for r in ws.rows:
    row_index = r[0].row   # 행 인덱스
    kor = r[1].value
    eng = r[2].value
    math = r[3].value
    sum = kor + eng + math
     # 합계 쓰기
    ws.cell(row=row_index, column=5).value = sum
    print(kor, eng, math, sum)
# 엑셀 파일 저장
wb.save("score2.xlsx")
wb.close() '''

# [Matplotlib 차트/플롯 그리기]
# 1. Matplotlib 개요
# Matplotlib는 파이썬에서 데이타를 차트나 플롯(Plot)으로 그려주는 라이브러리 패키지로서 가장 많이 사용되는 데이타 
# 시각화(Data Visualization) 패키지로 알려져 있다.
# Matplotlib는 라인 플롯, 바 차트, 파이차트, 히스토그램, Box Plot, Scatter Plot 등을 비롯하여 다양한 차트와 플롯 스타일을
# 지원하며, Matplotlib.org 갤러리 웹페이지에서 다양한 샘플 차트를 볼 수 있다.
# Matplotlib를 이용하여 데이타 시각화(Data Visualization)를 사용하기 위해서 과학용 파이썬 배포판인 아나콘다(Anaconda)를 설치해서 
# upyter Notebook을 사용하면 편리하다.
# 2. Matplotlib 사용법
# Matplotlib를 사용하기 위해서는 먼저 matplotlib.pyplot 을 아래와 같이 import 한다. pyplot을 다른 이름으로 사용할 수 있지만 
# 통상 plt 라는 alias를 사용한다. 다음 plt.plot()은 라인 플롯을 그리는 함수인데, 아래는 X축값 1,2,3과 Y축값 110,130,120을 
# 가지고 라인 플롯을 그리는 예제이다. 마지막으로 실제 그림을 표시하는 함수인 plt.show()을 호출한다.
# from matplotlib import pyplot as plt
# plt.plot([1,2,3], [110,130,120])
# plt.show()
# Jupyter Notebook에서 위 코드를 실행하기 위해서는 코드 셀에서 Shift + Enter를 치면 아래와 같이 출력란에 차트가 그려진다.
# 만약 아래 첫번째 라인에서와 같이 "%matplotlib inline" 를 넣게 되면, Shift + Enter를 치지 않고 Run 버튼을 눌러 실행하여 
# 그래프를 얻을 수 있다. 이러한 % 명령은 Cell Magic 명령어라고 불리우는 것으로 이는 파이썬 코드가 아니라 Jupyter에게 특정 
# 기능을 수행하도록 하는 명령이다. %matplotlib inline 명령은 Jupyter에게 matplotlib 그래프를 출력 영역에 표시할 것을 지시하는
# 명령이다.
# 3. 제목과 축 레이블
# 플롯에 X,Y 축 레이블이나 제목을 붙이기 위해서는 plt.xlabel(축이름), plt.ylabel(축이름), plt.title(제목) 등의 함수를 사용하면 
# 된다.
# from matplotlib import pyplot as plt
# plt.plot(["Seoul","Paris","Seattle"], [30,25,55])
# plt.xlabel('City')
# plt.ylabel('Response')
# plt.title('Experiment Result')
# plt.show()
# 4. 범례 추가
# 플롯에 여러 개의 라인들을 추가하기 위해서는 plt.plot()을 plt.show() 이전에 여러 번 사용하면 된다. 또한, 각 라인에 대한 
# 범례를 추가하기 위해서는 plt.legend([라인1범례, 라인2범례]) 함수를 사용하여 각 라인에 대한 범례를 순서대로 지정하면 된다.
# from matplotlib import pyplot as plt
# plt.plot([1,2,3], [1,4,9])
# plt.plot([2,3,4],[5,6,7])
# plt.xlabel('Sequence')
# plt.ylabel('Time(secs)')
# plt.title('Experiment Result')
# plt.legend(['Mouse', 'Cat'])
# plt.show()
# 5. 다양한 차트 및 플롯
# Matplotlib는 위에서 예시한 라인 플롯 이외에 여러 다양한 차트/플롯을 그릴 수 있는데, 각 차트/플롯마다 다른 함수들을 사용한다.
# 예를 들어, Bar 차트를 그리기 위해서는 plt.bar() 함수를 사용하고, Pie 차트를 그리기 위해서는 plt.pie()를, 히스토그램을 그리기 
# 위해선 plt.hist() 함수를 사용한다.
# 아래는 Bar 차트를 예시한 것으로, plt.bar()를 호출하여 바차트를 그리고 있다.
# from matplotlib import pyplot as plt
# y = [5, 3, 7, 10, 9, 5, 3.5, 8]
# x = range(len(y))
# plt.bar(x, y, width=0.7, color="blue")
# plt.show()
''' from matplotlib import pyplot as plt
plt.plot([1,2,3], [110,130,120])
plt.show()
plt.plot(["Seoul","Paris","Seattle"], [30,25,55])
plt.xlabel('City')
plt.ylabel('Response')
plt.title('Experiment Result')
plt.show()
plt.plot([1,2,3], [1,4,9])
plt.plot([2,3,4],[5,6,7])
plt.xlabel('Sequence')
plt.ylabel('Time(secs)')
plt.title('Experiment Result')
plt.legend(['Mouse', 'Cat'])
plt.show()
y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.bar(x, y, width=0.7, color="blue")
plt.show() '''

# [pandas 데이타 분석]
# 1. pandas 개요
# pandas는 데이타 분석(Data Analysis)을 위해 널리 사용되는 파이썬 라이브러리 패키지이다. pandas는 과학용 파이썬 배포판인 
# 아나콘다(Anaconda)에 기본적으로 제공되지만, 아나콘다를 사용하지 않을 경우에는 pip install pandas 를 통해 설치할 수 있다.
# 이 아티클에서는 pandas의 기본적인 개념과 기초적인 샘플들을 소개한다.
# 2. pandas 사용법
# pandas를 사용하기 위해서는 먼저 pandas를 아래와 같이 import 한다. pandas는 크게 세가지의 자료구조를 지원하고 있는데, 
# 1차원 자료구조인 Series, 2차원 자료구조인 DataFrame, 그리고 3차원 자료구조인 Panel을 지원한다.
# Series
# 가장 간단한 1차원 자료구조인 Series는 배열/리스트와 같은 일련의 시퀀스 데이타를 받아들이는데, 별도의 인덱스 레이블을 
# 지정하지 않으면 자동적으로 0부터 시작되는 디폴트 정수 인덱스를 사용한다.
# import pandas as pd
# data = [1, 3, 5, 7, 9]
# s = pd.Series(data)
# DataFrame
# 2차원 자료구조인 DataFrame는 행과 열이 있는 테이블 데이타(Tabular Data)를 받아들이는데, 아래 예제는 그 한가지 방법으로서
# 열(column)을 dict의 Key로, 행(row)을 dict의 Value로 한 Dictionary 데이타를 pd.DataFrame()을 사용하여 pandas의 Data Frame
# 자료구조로 변환한 예이다.
# import pandas as pd
# data = {
#     'year': [2016, 2017, 2018],
#     'GDP rate': [2.8, 3.1, 3.0],
#     'GDP': ['1.637M', '1.73M', '1.83M']
# }
# df = pd.DataFrame(data)
# Panel
# 3차원 자료구조인 Panel은 Axis 0 (items), Axis 1 (major_axis), Axis 2 (minor_axis) 등 3개의 축을 가지고 있는데, Axis 0은
# 그 한 요소가 2차원의 DataFrame 에 해당되며, Axis 1은 DataFrame의 행(row)에 해당되고, Axis 2는 DataFrame의 열(column)에 
# 해당된다.
# 아래 예제는 numpy를 사용하여 3차원 난수를 발생시킨 후, 이를 pandas.Panel() 에 적용한 예이다. 출력 결과에 보면, 
# 2 (items) x 3 (major_axis) x 4 (minor_axis) 크기의 Panel 객체가 생성되었음을 알 수 있다. Panel 객체 p로부터 p[0]을 
# 조회하면, Axis 0 의 첫번째 요소인 DataFrame이 출력됨을 볼 수 있다.
# 3. 데이타 엑세스
# pandas에서 Series, DataFrame, Panel 등의 자료구조를 만든 후, 다양한 방법을 통해 데이타를 엑세스할 수 있다.
# 가장 간단한 방식으로 pandas 자료구조에 대해 인덱싱 혹은 속성(Attribute)을 사용하는 것인데, 예를 들어 위에서 생성한 
# DataFrame인 df 에 대해 year 행을 가져오기 위해 df["year"] 혹은 df.year 를 사용할 수 있다. 또한, 부울린 인덱싱 
# (boolean indexing)을 사용하여 특정 조건의 데이타만 필터링 할 수도 있는데, df[df['year'] > 2016]은 2016년 초과인 데이타만
# 필터링해서 표시한다.
# 데이타량이 많은 경우는 df.head() 함수를 사용하면 처음 5개 row를 표시해 주며, df.tail() 함수를 사용하면 마찬가지로 마지막 
# 5개 row를 표시해 준다.
# pandas는 데이타에 대한 다양한 연산 함수들을 제공하고 있는데, 예를 들어 합계 구하는 sum(), 평균을 구하는 mean(), 최소를 
# 구하는 min(), 최대를 구하는 max() 등을 사용할 수 있다. 또한, 위 그림에서 보듯이, 기본적인 통계치를 모두 표시하기 위해 
# describe() 함수를 사용할 수 있다.
# 4. 외부 데이타 읽고 쓰기
# pandas는 CSV 파일, 텍스트 파일, 엑셀 파일, SQL 데이타베이스, HDF5 포맷 등 다양한 외부 리소스에 데이타를 읽고 쓸 수 있는 
# 기능을 제공한다. 아래 예제는 엑셀 파일파일로부터 데이타를 읽어 오는 기능을 예시한 것이다.
# 그리고, CSV 파일을 읽고 쓰기 위해서는 아래와 같이 read_csv() 와 to_csv() 함수를 사용할 수 있다.
# import pandas as pd
# df = pd.read_csv('C:\Temp\Test.csv')  # csv 읽기
# df.to_csv('C:\Temp\Output.csv')  # csv 쓰기

# [파이썬 이미지 처리 (Pillow)]
# 1. 파이썬에서의 이미지 처리
# 파이썬에서 이미지를 처리하고 핸들링하기 위해서는 Pillow, OpenCV, PIL 등의 외부 패키지를 설치해서 사용한다. 여기서는 PIL로부터
# 계승되어 많이 사용되는 Pillow 패키지를 사용한다. Pillow는 pip을 통해 아래와 같이 설치한다.
#     pip install Pillow
# Pillow는 파이썬 이미징 라이브러리로서 여러 이미지 파일 포맷을 지원하고, 이미지 내부 데이타를 엑세스할 수 있게 하며, 다양한
# 이미지 처리 기능을 제공하고 있다. 예를 들어, 이 패키지를 사용하면, 이미지로부터 Thumbnail 이미지를 만들다거나 다른 이미지
# 포맷으로 변환할 수 있고 이미지를 프린트하는 일들을 할 수 있다. 또한, 이미지 크기를 변형하거나 회전 및 Transform, 그리고 
# 필터링 등 다양한 이미지 프로세싱 작업들을 할 수 있다.
# 2. 이미지 파일 읽고 쓰기
# Pillow 패키지에서 가장 중요한 클래스는 이미지를 표현하는 Image 클래스이다. Image.open() 메서드는 기존 이미지 파일을 열 때 
# 사용하고, Image.new() 메서드는 새로운 이미지 파일을 생성할 때 사용하며, Image.save() 메서드는 이미지 파일을 저장할 때 사용한다.
# Image.open() 로부터 리턴된 이미지 객체의 size 속성은 이미지의 크기를 리턴한다. 아래 예제는 한 이미지 파일을 열어 크기를 출력한
# 후, 다른 포맷의 이미지 파일로 저장하는 예이다. (아래 예와 같이 설치시에는 Pillow 패키지를 설치하지만, import 시에는
# "import PIL"과 같이 PIL을 사용한다.)
# from PIL import Image
# # 이미지 열기
# im = Image.open('python.png')
# # 이미지 크기 출력
# print(im.size)
# # 이미지 JPG로 저장
# im.save('python.jpg')
# 큰 이미지 파일의 Thumbnail 이미지를 만들기 위해서는 Image 객체에서 thumbnail() 메서드를 호출하면 된다. 예를 들어, 
# Thumbnail 이미지를 최대 64 x 64 크기로 만들고 싶으면 아래와 같이 thumbnail(크기) 메서드를 호출한다.
# from PIL import Image
# im = Image.open('python.png')
# # Thumbnail 이미지 생성
# size = (64, 64)
# im.thumbnail(size)  
# im.save('python-thumb.jpg')
# 3. 이미지 부분 잘라내기
# 이미지의 일부를 잘라내는 것을 Cropping 이라 부르는데, 이미지 객체에서 crop() 메서드를 사용하여 일부 영역을 잘라내는데,
# crop() 메서드에서 리턴된 이미지는 부분 이미지로서 이를 저장하면 잘라낸 이미지만 저장된다. crop()의 파라미터는
# (좌, 상, 우, 하) 위치를 갖는 튜플로 지정한다.
# from PIL import Image
# im = Image.open('python.png')
# cropImage = im.crop((100, 100, 150, 150))
# cropImage.save('python-crop.jpg')
# Image 클래스에서는 crop() 이외에도 이미지를 복사하는 copy(), 이를 붙여넣는 paste() 등의 유용한 메서드들이 있다.
# 4. 이미지 회전 및 Resize
# 이미지를 회전하기 위해서는 이미지 객체에서 rotate(회전각도) 메서드를 호출하면 된다. 또한, 이미지의 크기를 확대/축소하기 
# 위해서는 이미지 객체에서 resize(크기튜플) 메서드를 호출한다.
# from PIL import Image
# im = Image.open('python.png')
# # 크기를 600x600 으로
# img2 = im.resize((600, 600))
# img2.save('python-600.jpg')
# # 90도 회전
# img3 = im.rotate(90)
# img3.save('python-rotate.jpg')
# 5. 이미지 필터링
# Pillow 패키지는 이미지를 필터링하기 위한 여러 기본적인 필터들을 제공하고 있다. 이미지 필터를 위해서는 이미지 객체에서 
# filter(필터종류) 메서드를 호출하면 되는데, 필터종류는 ImageFilter 모듈을 import 하여 지정한다. 예를 들어, Blur 이미지를
# 위해서는 ImageFilter.BLUR 를 사용하고, 윤곽만 표시하기 위해서는 ImageFilter.CONTOUR 를 사용한다.
# from PIL import Image, ImageFilter
# im = Image.open('python.png')
# blurImage = im.filter(ImageFilter.BLUR)
# blurImage.save('python-blur.png')

# [파이썬 영상 처리 (OpenCV)]
# 1. OpenCV 소개
# OpenCV (Open source Computer Vision)는 실시간 컴퓨터 비젼을 처리하는 목적으로 만들어진 라이브러리로서, 인텔에 의해 처음 
# 만들어져서 현재는 Itseez (2016년 인텔에 편입)에 의해 지원되고 있다. OpenCV는 크로스 플랫폼 라이브러리로서 윈도우즈, 리눅스, 
# Max 등에서 무료로 사용할 수 있다. OpenCV는 기본적으로 C++로 쓰여져 있는데, 이 라이브러리는 C/C++, Python, Java, C#, Ruby 등
# 여러 언어에서 사용할 수 있다. OpenCV는 이미지, 영상처리, Object Detection, Motion Detecton 등 매우 다양한 기능들을 제공하고
# 있는데, 여기서는 기초적인 기능들을 일부 소개한다.
# 파이썬에서 OpenCV는 pip을 통해 아래와 같이 설치할 수 있다.
#     pip install opencv-python
# 2. 이미지 파일 읽고 쓰기
# OpenCV에서 이미지를 읽기 위해서는 imread() 함수를 사용하고, 이미지를 저장하기 위해서는 imwrite() 함수를 사용한다. 또한, 
# 이미지를 화면에 표시하기 위해서는 imshow() 함수를 사용하는데, 이 함수를 사용하면 OpenCV가 새 윈도우 창을 만들고 해당 
# 이미지를 보여준다. 아래 예제는 한 이미지 파일을 읽어 들여 이를 화면에 출력한 후, 다른 파일명으로 이미지를 저장하는 코드이다.
# import cv2
# # 이미지 읽기
# img = cv2.imread('test.jpg', 1)
# # 이미지 화면에 표시
# cv2.imshow('Test Image', img)
# cv2.waitKey(0)
# # 이미지 윈도우 삭제
# cv2.destroyAllWindows()
# # 이미지 다른 파일로 저장
# cv2.imwrite('test2.png', img)
# 3. 카메라 영상 처리
# OpenCV에서 카메라(웹캠)로부터 영상을 전달받아 처리하기 위해서는 VideoCapture 클래스를 사용한다. VideoCapture 클래스의 
# 인스턴스를 생성할 때, 컴퓨터에 카메라가 여러 개 있을 수 있으므로, 어떤 카메라를 사용할 지를 카메라 아이디로 전달하는데,
# 일반적으로 0 을 쓰면 첫번째 카메라(디폴트 카메라)를 사용하게 된다. 만약 두번째 카메라를 사용하려면 1을, 세번째 카메라를 
# 사용하려면 2를 사용한다.
# VideoCapture 클래스 인스턴스를 생성한 후, VideoCapture 클래스의 read() 메서드를 호출하여 카메라 이미지(프레임)을 가져올 수
# 있다. read() 메서드는 2개의 값을 리턴하는데, 첫번째는 프레임을 성공적으로 읽었는지를 표시하고, 두번째는 프레임 자체를
# 리턴한다. 프레임을 화면에 출력하기 위해서는 cv2.imshow() 함수를 사용하면 되는데, 이 함수의 첫번째 파라미터로 윈도우 창제목을 
# 적고, 두번째 파라미터에 카메라에서 전달받을 프레임을 넣으면 된다. VideoCapture 클래스의 isOpened() 메서드는 카메라 영상
# 캡쳐가 초기화되었는지 여부를 리턴하며, 카메라 사용을 종료하기 위해서는 release() 메서드를 사용하면 된다.
# import cv2
# cap = cv2.VideoCapture(0)   # 0: default camera
# #cap = cv2.VideoCapture("test.mp4") #동영상 파일에서 읽기
# while cap.isOpened():
#     # 카메라 프레임 읽기
#     success, frame = cap.read()
#     if success:
#         # 프레임 출력
#         cv2.imshow('Camera Window', frame)
#          # ESC를 누르면 종료
#         key = cv2.waitKey(1) & 0xFF
#         if (key == 27): 
#             break
# cap.release()
# cv2.destroyAllWindows()
# 만약 카메라가 아니라 동영상 파일에서 영상 데이타를 가져오기 위해서는 VideoCapture 인스턴스를 생성할 때 카메라 Device Id 대신 
# 동영상 파일명을 지정하면 된다. 예를 들어, cap = cv2.VideoCapture("test.mp4") 와 같이 사용한다.
# 4. 카메라 영상 저장하기
# OpenCV에서 카메라(웹캠)로부터 전달받은 영상을 저장하기 위해서는 VideoWriter 클래스를 사용한다. VideoWriter 클래스의 
# 인스턴스를 생성할 때, 영상 저장과 관련된 몇 개의 파라미터를 전달해야 하는데, 첫번째로 영상을 저장할 파일명을 지정하고,
# 두번째로 영상을 어떤 포맷을 저장할 지를 표시하는 fourcc ID를 지정한다. fourcc는 four character code의 약자로서, 비디오
# 코덱(Codec)을 지정하는 4 바이트 코드이다. 아래 예제에서는 fourcc로 XVID MPEG-4 코덱을 표시하는 "XVID"을 사용하였다.
# 다음으로, VideoWriter() 의 세번째 파라미터로 프레임수를 지정하고, 네번째 파라미터로 영상 크기 즉 프레임의 너비와 높이를 
# 튜플로 지정한다. 영상 크기는 VideoCapture 클래스의 get() 메서드를 사용하여 프레임 너비와 높이를 가져올 수 있다.
# 실제 프레임 저장은 VideoWriter 클래스의 write() 메서드를 사용하며, 저장이 모두 끝나면 release() 메서드를 호출하여 파일을
# 닫아 준다.
# import cv2
# cap = cv2.VideoCapture(0); 
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print("size: {0} x {1}".format(width, height))
# # 영상 저장을 위한 VideoWriter 인스턴스 생성
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# writer = cv2.VideoWriter('test.avi', fourcc, 24, (int(width), int(height)))
# while cap.isOpened():
#     success, frame = cap.read()
#     if success:
#         writer.write(frame)  # 프레임 저장
#         cv2.imshow('Video Window', frame)
#         # q 를 누르면 종료
#         if cv2.waitKey(1) & 0xFF == ord('q'): 
#             break
#     else:
#         break
# cap.release()
# writer.release()  # 저장 종료
# cv2.destroyAllWindows()
# 5. OpenCV와 Matplotlib 활용
# Matplotlib는 파이썬에서 데이타를 차트나 플롯(Plot)으로 그려주는 2D 라이브러리 패키지인데, 여기서는 OpenCV에서 읽어들인 
# 이미지를 Matplotlib 에서 보여주는 기능에 대해 알아본다. OpenCV에서 img = cv2.imread()를 통해 이미지를 읽어 들인 후, 이어 
# Matplotlib의 pyplot.imshow(img)로 호출하면 이미지를 pyplot으로 그릴 준비를 하게 되고, pyplot.show() 를 호출하면 이미지를
# 화면에 출력하게 된다. 한가지 참고할 사항은 OpenCV 의 imread()는 BGR 포맷으로 이미지를 읽어들이고, pyplot은 RGB 포맷을 
# 사용하므로 원래의 이미지 색을 표현하기 위해서는 cv2.cvtColor() 를 사용하여 BGR 포맷을 RGB 포맷으로 변환해 주는 작업이 
# 필요하다.
# import cv2
# from matplotlib import pyplot as plt
# img = cv2.imread('happyfish.jpg', 1)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()
# 아래는 위 프로그램을 실행하여 matplotlib으로 이미지를 그린 결과이다. matplotlib에서 생성한 이 윈도우에서는 이미지를 
# 파일로 저장하거나 이미지 좌표를 체크할 수도 있으며, 이미지를 확대 축소하는 등의 기능들을 사용할 수도 있다.

# [파이썬에서 SSH 클라이언트 사용]
# 1. SSH (Secure Shell)
# SSH는 다른 컴퓨터에 Secure한 방식으로 연결하여 명령을 수행할 수 있는 네트워트 기능으로 telnet을 대체하는 보다 안전한 방식의
# 터미널 기능이다. Telnet의 모든 데이타는 Clear Text로 통신되는 반면, SSH의 데이타는 Public Key Encryption을 사용하여 모두
# 암호화된다. SSH는 디폴트로 포트 22를 사용하고, Telnet은 디폴트로 포트 23을 사용한다.
# 2. SSH 파이썬 패키지
# SSH는 클라이언트/서버 방식으로 통신하는데, SSH Client가 SSH Server에 연결하여 데이타를 주고 받는다. 파이썬에서 SSH를 사용하기
# 위해서는 paramiko, netmiko 등과 같은 파이썬 패키지를 사용할 수 있다. 여기서는 paramiko 패키지를 사용해 보는데, 아래는 pip을 
# 사용하여 paramiko 패키지를 설치하는 명령이다.
# pip install paramiko
# 3. SSH 클라이언트
# paramiko 패키지에서 SSH 클라이언트를 사용하기 위해서는 기본적으로 다음과 같은 스텝을 밟는다.
# paramiko.SSHClient 클래스의 인스턴스를 만들고,
# SSHClient 인스턴스로부터 connect() 메서드를 호출하여 서버에 연결한 후,
# SSHClient 인스턴스로부터 명령을 보내고 결과를 리턴받는다.
# SSHClient 인스턴스로부터 close() 메서드를 호출하여 연결을 닫는다.
# 아래 예제는 SSH로 서버에 연결한 후 해당 로그인 계정의 홈 디렉토리의 파일 리스트를 출력해 보는 코드이다. 서버명, 로그인명,
# 암호 등은 프로그램 실행시 콘솔에 입력받도록 하였는데, 특히 암호는 입력되는 문자를 숨기기 위해 getpass() 함수를 사용하였다.
# import paramiko
# import getpass
# cli = paramiko.SSHClient()
# cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# server = input("Server: ")  # 호스트명이나 IP 주소
# user = input("Username: ")  
# pwd = getpass.getpass("Password: ") # 암호입력 숨김
# cli.connect(server, port=22, username=user, password=pwd)
# stdin, stdout, stderr = cli.exec_command("ls -la")
# lines = stdout.readlines()
# print(''.join(lines))
# cli.close()
# 위 예제는 paramiko.SSHClient 클래스로부터 cli 라는 인스턴스를 생성한 후, cli.connect() 메서드를 사용하여 SSH 서버에 접속한다.
# connect() 메서드는 여러 가지 파라미터들을 받아들일 수 있는데, 기본적으로 호스트명과 사용자 및 암호 등을 지정하고, 추가적으로
# 포트번호, 타임아웃, 압축기능 등을 지정할 수 있다. SSH는 접속시 known_hosts에 등록된 호스트키를 체크하는데 만약 접속하는 서버의
# 호스트키가 없으면 접속을 거부하게 된다. 만약 이러한 보안 기능을 사용하지 않고, 자동으로 새 호스트키를 추가하도록 하기 위해서는
# cli.set_missing_host_key_policy() 을 사용하여 AutoAddPolicy 를 지정하면 된다.
# exec_command() 메서드는 SSH 서버에 어떤 명령을 실행하도록 할 때 사용된다. 예를 들어, 위의 예제에서는 "ls -la" 명령을 실행하여 
# 그 실행 결과를 표준콘솔입력(stdin), 표준콘솔출력(stdout), 표준에러출력(stderr)에 리턴한다. 이어 표준출력으로 전달된 stdout으로
# 부터 readlines()를 통해 출력 결과를 라인별로 읽어들이고, 이를 화면에 출력(print)한다.
# 마지막으로 SSHClient 인스턴스의 사용을 마친 후에는 close()를 메서드를 호출하여 연결을 종료해 주어야 한다.
# 또 다른 예제로서 아래는 exec_command() 대신 invoke_shell()을 사용한 방식으로 이 invoke_shell() 메서드는 서버에 새로운
# interactive shell session 을 생성하고 채널을 리턴한다. 클라이언트는 이 채널을 통해 계속 명령을 송신하고 결과를 수신할 수 
# 있다. invoke_shell() 메서드가 실행되면 새로운 쉘이 생성되어 화면에 표시된다.
# import paramiko
# import getpass
# import time
# cli = paramiko.SSHClient()
# cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# cli.connect("test.com", username="user", password="pwd")
# # 새로운 interactive shell session 생성
# channel = cli.invoke_shell()
# # 명령 송신
# channel.send("ls -la\n")
# time.sleep(1.0)
# # 결과 수신
# output = channel.recv(65535).decode("utf-8")
# print(output)
# cli.close()
# 채널에 명령을 보내기 위해 send() 메서드를 사용하며, 결과를 수신하기 위해 recv() 메서드를 사용한다. recv() 메서드의 
# 파라미터인 65535는 수신받는 최대 바이트수를 가리키며, recv()가 바이트스트림을 리턴하므로 이를 적절히 디코딩할 필요가
# 있을 수 있다. 여기서는 decode()를 사용하여 UTF-8으로 디코딩하였다.


# [Python 팁]

# [Python Tools for Visual Studio]
# 1. Python Tools for Visual Studio (PTVS) 소개
# Visual Studio에서 Python을 사용하기 위해 Python Tools for Visual Studio (PTVS) 라는 플러그인을 설치할 수 있다. PTVS는 
# 무료이며, 오픈소스 플러그인이다. PTVS는 CPython, IronPython, PyPy 등을 지원하며, 코딩을 편리하게 하는 인텔리센스 기능을 
# 제공한다. PTVS는 강력한 디버깅 기능을 제공하며, Python/C++ 혼합 디버깅과 원격 리눅스/Mac 디버깅 등도 함께 지원한다. 
# 또한, PTVS는 Django, Flask 와 같은 웹 개발 프레임워크들을 지원하여, PTVS를 사용하면 편리하게 웹 프로젝트를 개발할 수 있다.
# 2. PTVS 설치
# PTVS는 Visual Studio 2013 이상 버전이 설치된 상태에서 https://microsoft.github.io/PTVS/ 로부터 플러그인을 다운받아 설치한다.
# PTVS는 MSI 를 통해 설치되며, 설치 마법사를 통해 아래와 같은 컴포넌트를 설치한다. 설치된 PTVS를 Uninstall하기 위해서는 
# 제어판(Control Panel)의 프로그램 및 기능(Programs and Features) 을 사용한다.
# 3. PTVS 사용
# Visual Studio를 실행하고, 새 프로젝트 (File -> New Project)를 실행한 후, 아래 그림과 같이 Python 언어를 선택하면, 
# 다양한 프로젝트 유형을 선택할 수 있게 된다. VS와 PTVS는 Python 인터프리터를 사용하는데, 이 Python 인터프리터는 별도로 
# 설치하여야 한다.
# 새 프로젝트로서 Python Project를 선택하고 아래 그림처럼 간단하게 for 루프를 작성해 보았다. 파이썬 코드를 실행하기 위해서는
# F5 혹은 Start 툴바를 누르면 된다.
# Python이 이미 설치되어 있는 경우, 자동으로 Python Environment를 탐지하지만, 만약 Python을 늦게 설치하였거나 여러 Python이 
# 설치되어 있는 경우, [Solution Explorer]의 [Python Environments] 노드에서 추가, 변경할 수 있다.
# 4. Django 프로젝트 생성
# Django 프로젝트를 만들기 위해서는 VS 새 프로젝트 선택 화면에서 [Django Web Project] 를 선택한다. 이어 PTVS는 아래와 같이 
# External Package들을 어디에 설치할 지를 묻게되는데, 권장사항대로 첫번째를 선택한다 (주: 필요에 따라 개발자가 다른 옵션 
# 선택할 수 있음)
# 곧이어 가상환경(Virtual Environment)를 추가하는 다이얼로그가 나오는데, 여기서 가상환경의 이름과 디렉토리 위치를 선택할 수 
# 있고, 어떤 Python 인터프리터를 사용하는지 선택하게 된다. 이러한 사항들을 선택한 후 Create 버튼을 누르면, 가상환경과 Django
# 프로젝트, 디폴트 Django App 등이 자동으로 생성된다.
# 아래 화면은 VS/PTVS가 디폴트로 자동 생성한 Django 프로젝트의 디렉토리 구조이다. PTVS는 Django 프로젝트 개발에 필요한 모든 
# 기본적인 구조와 환경을 자동으로 생성해 주기 때문에 편리하다.

# [기존 Python코드를 VS 프로젝트로]
# 기존 Python 코드를 PTVS 프로젝트로
# 기존에 다른 OS 혹은 편집기에서 작성한 Python 프로젝트를 Python Tools for Visual Studio (PTVS) 에서 사용하기 위해서는 
# Visual Studio에서 VS용 새 Python 프로젝트(*.pyproj)를 생성해야 한다. 그 절차는 아래와 같다.
# VS에서 File - New Project를 선택하고, Python 언어 템플릿 중 "From Existing Python Code"를 선택한다. 
# 위저드 화면이 나오면, 기존 파이썬 코드가 있는 폴더를 선택하고 Next를 누른다. 
# 다음 사용할 Python 인터프리터 버젼을 선택한다. 가상환경이 없다면, 나중에 만들 수 있다. 
# 새로 생성할 VS용 Python 프로젝트 파일(.pyproj) 이름을 선택한다. 위저드를 종료하면 새 프로젝트 파일이 생성된다. 

# [Visual Studio Code 사용]
# 1. Visual Studio Code 소개
# Visual Studio Code (VS Code)는 크로스 플랫폼 소스 편집기로서 윈도우즈, 리눅스, Mac OS 에서 무료로 사용할 수 있다. 
# Visual Studio Code를 설치한 후 여러 Extension들을 설치할 수 있는데, 파이썬 Extension을 설치하면, 파이썬 프로그래밍과 
# 디버깅을 할 수 있다.
# 2. VS Code 설치
# VS Code는 https://code.visualstudio.com 사이트에서 다운받아 설치한다. VS Code를 설치하여 실행한 후 View 메뉴에서 
# [Command Palette] 메뉴를 누르고 아래와 같이 ext install 을 치면 Extension을 설치하는 메뉴 (Install Extensions) 가 나온다.
# 위 그림에서 [Install Extensions]를 선택하면, 아래와 같이 [Extensions] 선택화면이 나오는데, 여기서 "python" 이라고 치고 
# 원하는 파이썬 Extension을 선택하여 설치한다. 참고로, Extensions 선택화면을 나오게 하기 위해 좌측에 있는 Extensions 버튼을 
# 사용할 수도 있다. 이렇게 파이썬 Extension을 설치 완료하면 파이썬 프로그래밍을 진행할 수 있다.
# 3. 파이썬 파일 작성과 실행
# VS Code에서 파이썬 코드를 작성하기 위해서는 확장자 .py 를 가진 임의의 파이썬 파일을 생성하면 된다. [File] 메뉴에서 
# [New File]을 눌러 새 파일을 만들어도 되지만, VS Code의 기능을 100% 활용하기 위해서는 [File] 메뉴에서 [Open Folder]를 사용하여
# 작업 폴더를 지정하고 사용하는 것이 좋다. 이 작업 폴더에 새 .py 파일을 생성하고 에디터에서 코드를 작성한다.
# 코드 작성 완료 후 프로그램을 실행하기 위해서는 [Debug] 메뉴의 [Start Debugging (F5)] 나 [Start without Debugging (Ctrl+F5)]를
# 누르면 된다. 특히 F5를 눌러 디버깅 모드로 실행하면, 로컬변수, 콜스택 등 여러 디버깅 정보를 이용할 수 있으며, Step Over, 
# Step Into 등의 디버거 컨트롤을 사용할 수 있다.
# 4. 파이썬 터미널에서 실행
# 파이썬 파일에 코드를 작성한 후, VS Code 에디터에서 우측 마우스 버튼을 클릭 [Run Python File in Terminal] 메뉴를 선택하면
# 하단에 터미날 창이 생기고 파이썬 프로그램을 인터프리터와 함께 실행해 준다.

# [pip 패키지 관리자]
# 1. pip 패키지 관리자
# pip은 파이썬 패키지를 설치하고 관리하는 패키지 관리자(Package Manager)이다. pip은 "Pip Installs Packages"의 약자로서 재귀적인
# 약어이다.
# pip은 Python 2.7.9+와 Python 3.4+에서 디폴트로 설치되어 있다. 만약 pip이 시스템에 설치되지 않은 경우는 다음과 같이 설치할 수
# 있다.
# curl https://bootstrap.pypa.io/get-pip.py | python
# 2. pip 패키지 설치와 제거
# pip을 이용하면 패키지를 쉽게 설치할 수 있다. pip으로 설치할 수 패키지들의 목록은 Python Package Index (PyPI)에서 찾아 볼 수
# 있다. 다음은 패키지를 설치하는 pip install 명령이다.
# pip install 패키지명
# ex)
# $ pip install django
# $ pip install numpy
# $ pip install matplotlib
# 설치된 패키지를 Uninstall하기 위해서는 아래와 같은 pip uninstall 명령을 사용한다.
# pip uninstall 패키지명
# ex)
# $ pip uninstall django
# 현재 pip으로 설치된 패키지들의 리스트를 보기 위해서는 pip list 명령을 사용한다.
# $ pip list
# certifi (2017.7.27.1)
# chardet (3.0.4)
# cytoolz (0.8.2)
# Django (1.11.2)
# ethereum-abi-utils (0.4.3)
# ethereum-utils (0.5.1)
# idna (2.6)
# pip (9.0.1)
# pkg-resources (0.0.0)
# pysha3 (1.0.2)
# pytz (2017.2)
# requests (2.18.4)
# setuptools (20.7.0)
# toolz (0.8.2)
# urllib3 (1.22)
# 이미 설치된 패키지를 최신 버전으로 업그레이드하기 위해서는 아래와 같이 --upgrade 옵션을 지정한다.
# $ pip install django --upgrade
# 3. pip: requirements 파일 생성과 사용
# pip을 이용하면 일련의 패키지 그룹을 묶어서 설치할 수도 있다. 즉, requirements.txt 파일에 설치할 패키지 리스트를 정의한 후, 
# 아래와 같은 명령으로 전체를 한꺼번에 설치할 수 있다. 실제 "pip install 패지키명" 을 사용하여 패키지를 하나 하나 설치하는 
# 것보다, requirements.txt를 만들어 패키지 리스트를 이 파일에서 관리하고 이 파일을 통해 pip 설치 수행하는 것이 더 좋은 방법이다.
# $ pip install -r requirements.txt
# 하지만 경우에 따라 requirements.txt를 미리 만들지 않고, 개발서버의 가상환경에 여러 패키지를 이미 설치했을 수도 있다. 이런
# 경우는 아래와 같은 pip freeze 명령을 사용하여 requirements.txt 파일을 만들 수 있다. 이러한 기능은 개발서버의 가상환경을
# Production 가상환경으로 Deployment 하는데 유용하게 쓰일 수 있다.
# $ pip freeze > requirements.txt
# 4. 윈도우즈에서의 pip 사용
# 윈도우즈에서 pip 을 사용하기 위해서는 python 설치 폴더 밑의 Scripts 서브디렉토리에서 pip을 실행한다.

# [Python 디버깅 (PDB)]
# 1. Python 디버깅
# Python은 디버깅을 위해 pdb 라는 Python Debugger 모듈을 제공하고 있다. 이 디버거는 Step over/Step into, 중단점(breakpoint)
# 설정, 콜스택 검사, 소스 리스팅, 변수 치환 등 다양한 기능을 가지고 있다.
# Python 디버깅에서 사용되는 방법 중 하나로 아래와 같이 "python -m pdb 파이선파일.py" 를 사용하는 방법이 있다. "-m pdb" 를 
# 사용하게 되면, 디버거 하에서 파이선 파일을 실행하게 된다. 예를 들어, 아래 예를 보면 test1.py라는 파이썬 모듈의 첫번째 
# 라인에서 프로그램을 중단하고 디버거 프롬프트인 (Pdb) 를 표시함을 볼 수 있다. (밑에서 설명하지만 아래는 Pdb 프롬프트에서 
# list를 사용하여 test1.py의 소스코드를 출력하였다)
# Python 디버깅에서 흔히 사용되는 두번째 디버깅 방법은 pdb 모듈을 import 한 후, pdb.set_trace()를 중단하고 싶은 곳에 넣는 
# 방식이다. 이렇게 하면 파이썬 프로그램 실행시 pdb.set_trace() 문장이 있는 곳에서 실행을 중지하고 디버거 세션을 시작하게 한다.
# 아래 그림을 보면 pdb.set_trace() 다음 문장에서 (Pdb) 프롬프트가 표시되어 있음을 볼 수 있다.
# # test2.py 소스
# import pdb
# def sum(x, y):
#     z = x + y
#     return z
# a = 10
# pdb.set_trace()  # 이곳에서 프로그램 중단
# b = 20
# c = sum(a, b)
# print(c)
# 2. PDB 사용법
# PDB를 사용하여 디버깅 모드로 진입하게 되면, (Pdb) 프롬프트가 나오게 되는데 여기서 여러 PDB 명령을 사용할 수 있다. 즉, 다음
# 문장을 실행하거나(next), 변수 값을 프린트하거나(print), 소스코드를 리스팅하거나(list), 함수 안으로 들어가거나(step into) 하는
# 일들을 PDB 명령을 사용하여 실행할 수 있다.
# 다음은 자주 사용되는 PDB 명령들을 요약한 것이다. 명령어를 단어 전체를 사용해도 되지만, 보통 약어로 앞의 한 글자만 사용할 
# 수 있다. 즉, next 대신 n 을 사용할 수 있다.
# PDB 명령어	실행내용
# help	도움말
# next	다음 문장으로 이동
# print	변수값 화면에 표시
# list	소스코드 리스트 출력. 현재 위치 화살표로 표시됨
# where	콜스택 출력
# continue	계속 실행. 다음 중단점에 멈추거나 중단점 없으면 끝까지 실행
# step	Step Into 하여 함수 내부로 들어감
# return	현재 함수의 리턴 직전까지 실행
# !변수명 = 값	변수에 값 재설정
# 3. IDE 디버깅
# PyCharm, PTVS, Spyder와 같은 IDE는 UI에서 쉽게 디버깅을 할 수 있는 기능을 제공하고 있다. 일반적으로 코드 상에 
# 중단점(Breakpoint)를 걸고 디버깅 실행 버튼을 눌러 디버깅을 시작하고, Step Over, Step Into 등의 버튼을 사용하여 한
# 라인씩 디버깅해 나갈 수 있다.

# [파이썬 가상환경]
# 1. 파이썬 가상환경 (Virtual Environment)
# 하나의 물리적인 머신에 여러 개의 가상 머신을 올릴 수 있듯이, 한 머신에 여러 개의 파이썬 가상환경을 만들 수 있다. 이러한
# 가상환경은 파이썬 개발 환경을 독립적으로 만들기 위한 것으로, 각 개발환경마다 다른 파이썬 버전을 사용할 수도 있고 다른 
# 패키지를 설치할 수 있다. 가상환경은 그 안에 파이썬 개발환경과 관련된 모든 것을 가지고 있다 (Self-contained 환경). 만약 
# 프로젝트마다 서로 다른 버전의 파이썬을 사용한다거나 각 프로젝트에 필요한 패키지가 다를 경우 혹은 개발환경을 그대로 나중에
# 실제 서버에 옮기고 싶을 경우 가상환경을 사용하면 편리하다.
# 2. 가상환경 만들기
# 파이썬 3.3 버전 이상에서 가상환경을 사용하기 위해서는 pyvenv 를 사용한다. 참고로 가상환경을 만드는 다른 방법으로
# virtualenv를 사용할 수 있는데, 이는 pypi.python.org 로부터 다운받아 사용한다.
# 여기서는 pyvenv 를 사용하여 가상환경을 만들어 보자. 가상환경은 하나의 디렉토리 밑에 생성되는데, 가상환경을 만들 디렉토리로 
# 이동한 후 아래와 같은 절차를 따른다. 먼저 리눅스나 Mac OS에서 venv1 이라는 가상환경을 만드는 과정을 살펴본다.
# 가상환경 생성: 아래는 현재 디렉토리 밑에 venv1 이라는 폴더를 만들고 venv1 이라는 가상환경을 만드는 것이다.
# $ pyvenv venv1
# 가상환경 활성화: 가상환경이 생성된 후, 그 가상환경으로 들어가기 위해 아래와 같이 activate 를 실행하여 가상환경을 활성화를
# 해주어야 한다.
# $ source venv1/bin/activate
# 다음 윈도우즈에서 venv1 이라는 가상환경을 만드는 과정은 다음과 같다.
# 가상환경 생성: 아래는 C:\PyApp 디렉토리 밑에 venv1 이라는 폴더를 만들고 venv1 이라는 가상환경을 만드는 것이다.
# C:\Python35> python .\Tools\scripts\pyvenv.py C:\PyApp\venv1
# 가상환경 활성화: 먼저 가상환경 디렉토리로 이동하여 Scripts 폴더로 가서 activate를 실행한다.
# C:\PyApp\venv1\Scripts> activate.bat
# 참고로 가상환경의 파이썬 버전 정보는 가상환경 디렉토리 안의 pyvenv.cfg 파일을 살펴보면 알 수 있다.
# 3. 가상환경에 패키지 설치 및 파이썬 실행
# 가상환경을 활성화한 후에 필요한 패키지를 설치하기 위해 pip과 같은 패키지 매니저를 사용할 수 있다. 예를 들어, 아래는
# 가상환경 venv1 에 numpy 를 설치하는 예이다. 이렇게 설치된 numpy 는 해당 가상환경 내에서만 유효하며 시스템이나 다른 
# 가상환경에 영향을 미치지 않는다.
# ~/venv1/bin$ . activate
# (venv1) ~/venv1/bin$ pip install numpy    
# 가상환경에서 파이썬을 실행하는 것은 간단하다. 가상환경 프롬프트에서 "python" 을 실행하면 된다.
# (venv1) ~/venv1$ python 
# Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 19 2015, 20:19:30) 
# [GCC 4.2.1 (Apple Inc. build 5577)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>>

# [파일과 디렉토리]
# 파이썬에서 파일과 디렉토리 경로 다루기
# 파이썬에서 디렉토리와 파일경로를 다루는 주요 함수들에 대해 알아보자. 디렉토리 및 파일 경로에 대한 함수들은 os 모듈에
# 있으므로, os 모듈을 import 한 것을 전제로 한다. 특히, os.path 모듈은 파일명과 파일경로에 대한 유용한 함수들을 많이
# 제공하고 있다.
# 용도	함수 예제
# 현재 작업 폴더 얻기	os.getcwd()
# # "C:\Temp"
# 디렉토리 변경	os.chdir("C:\Tmp")
# 특정 경로에 대해 절대 경로 얻기	os.path.abspath(".\\Scripts")
# # "C:\Python35\Scripts"
# 경로 중 디렉토리명만 얻기	os.path.dirname("C:/Python35/Scripts/pip.exe")
# # "C:/Python35/Scripts"
# 경로 중 파일명만 얻기	if os.path.isfile("C:/Python35/Scripts/pip.exe"):
#    print(os.path.basename("C:/Python35/Scripts/pip.exe"))
# # "pip.exe"
# 경로 중 디렉토리명과 파일명을 나누어 얻기	dir, file = os.path.split("C:/Python35/Scripts/pip.exe")
# 파일 각 경로를 나눠 리스트로 리턴하기
# os.path.sep은 OS별 경로 분리자	"C:\Python35\Scripts\pip.exe".split(os.path.sep)
# # ['C:', 'Python35', 'Scripts', 'pip.exe']
# 경로를 병합하여 새 경로 생성	os.path.join('C:\Tmp', 'a', 'b')
# # "C:\Tmp\a\b"
# 디렉토리 안의 파일/서브디렉토리 리스트	os.listdir("C:\Python35")
# 파일 혹은 디렉토리 경로가 존재하는지 체크하기	os.path.exists("C:\Python35")
# 디렉토리 경로가 존재하는지 체크하기	os.path.isdir("C:\Python35")
# 파일 경로가 존재하는지 체크하기	os.path.isfile("C:\Python35\python.exe")
# 파일의 크기	os.path.getsize("C:\Python35\python.exe")

# [메일 보내기 (SMTP)]
# 메일 보내기 (SMTP Mail)
# 파이썬에서 이메일을 보내기 위해서는 파이썬에 기본 내장된 smtplib 라는 모듈을 사용한다. SMTP는 Simple Mail Transfer
# Protocol의 약자로서 메일을 보내는데 사용되는 프로토콜이다. 개인이나 회사가 SMTP 서버를 설치해서 이를 통해 메일을 발송할
# 수 있지만, 요즘은 구글, 마이크로소프트 등 많은 회사들이 SMTP 서버를 사용할 수 있도록 오픈하고 있기 때문에 이들 SMTP 서버를
# 사용해서 메일을 발송할 수 있다.
# 메일 Provider	SMTP 서버명, 포트
# Live	smtp.live.com, 587
# GMail	smtp.gmail.com, 587
# 파이썬에서 SMTP 서버에 접속하기 위해서는 smtplib 모듈을 import 한 후, SMTP 서버와 포트로 SMTP 객체를 생성한다. SMTP 서버의
# Encryption 방식에 따라 TTL 혹은 SSL을 사용하는데, TLS을 사용하는 경우 smtplib.SMTP()를, SSL을 사용하는 경우 smtplib.SMTP_SSL()
# 을 사용한다. TLS는 보통 포트 587을, SSL은 465를 사용한다.
# SMTP 객체를 생성한 후에는 프로토콜 상 가장 먼저 SMTP 서버에 Hello 메시지를 보내는데, ehlo() 메서드가 이 기능을 한다. 
# Hello 메시지 이후, TLS 인 경우는 starttls() 를 실행하여 TLS Encryption을 시작하는데, SSL인 경우에는 이 메서드를 호출하지
# 않는다.
# # -*- coding:utf-8 -*-
# import smtplib
# from email.mime.text import MIMEText
# smtp = smtplib.SMTP('smtp.live.com', 587)
# smtp.ehlo()      # say Hello
# smtp.starttls()  # TLS 사용시 필요
# smtp.login('lee@live.com', 'password')
# msg = MIMEText('본문 테스트 메시지')
# msg['Subject'] = '테스트'
# msg['To'] = 'kim@naver.com'
# smtp.sendmail('lee@live.com', 'kim@naver.com', msg.as_string())
# smtp.quit()
# 이렇게 기본 연결을 마친 후, login(계정, 암호) 메서드를 호출하여 계정과 암호를 넣고 사용자 인증을 받게 된다. 이후, 
# sendmail(송신자, 수신자, 메시지) 메서드를 사용하여 메일을 보내게 되는데, 여기서 메시지는 간단한 메시지의 경우는
# email.mime.text.MIMEText 을, 좀 더 복잡한 메시지의 경우는 email.mime.multipart.MIMEMultipart 등을 사용할 수 있다. 
# 마지막으로 SMTP와 연결을 끊고 종료하기 위해서는 quit() 메서드를 호출한다.

# [난수 (random)]
# 난수 (random)
# 파이썬에서 난수(random number)를 사용하기 위해서는 기본적으로 제공되는 random 모듈을 사용한다. random 모듈에서 자주 사용되는
# 함수는 다음과 같다.
# randint(최소, 최대) : 입력 파라미터인 최소부터 최대까지 중 임의의 정수를 리턴한다
# random() : 0 부터 1 사이의 부동소수점(float) 숫자를 리턴한다
# uniform(최소, 최대) : 입력 파라미터인 최소부터 최대까지 중 임의의 부동소수점(float) 숫자를 리턴한다
# randrange(시작,끝[,간격]) : 입력 파라미터인 시작부터 끝값까지 (지정된 간격으로 나열된) 숫자 중 임의의 정수를 리턴한다
# from random import *
# i = randint(1, 100)  # 1부터 100 사이의 임의의 정수
# print(i)
# f = random()   # 0부터 1 사이의 임의의 float
# print(f)
# f = uniform(1.0, 36.5)   # 1부터 36.5 사이의 임의의 float
# print(f)
# i = randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
# print(i)
# i = randrange(10)  # 0부터 9 사이의 임의의 정수
# print(i)
# 아래는 난수를 사용한 간단한 예제로서 난수를 생성한 후 어떤 숫자인지 맞추는 프로그램이다. 즉, 사용자가 입력한 숫자가 난수보다
# 큰지 작은지를 알려주고 계속 추측해서 난수값을 맞추게하는 예제이다.
# from random import randint
# n = randint(1, 100)
# while True:
#     ans = input("Guess my number (Q to exit): ")
#     if ans.upper() == "Q":
#         break
#     ians = int(ans)
#     if (n == ians):
#         print("Correct!")
#         break
#     elif (n > ians):
#         print("Choose higher number")
#     else:
#         print("Choose lower number")
# 샘플링 (sample)
# random 모듈에서 또 한가지 유용한 기능은 리스트, set, 튜플 등과 같은 컬렉션으로부터 일부를 샘플링해서 뽑아내는 기능이다. 
# random 모듈에서 sample(컬렉션, 샘플수) 함수는 지정된 컬렉션으로부터 샘플수만큼 랜덤 추출을 하는 함수이고, 이보다 좀 더 복잡한 
# choices() 함수는 샘플링에 가중치를 주어 추출하는 기능을 가지고 있다. 아래 예제는 (1) 숫자 리스트로부터 3개를 랜덤하게 
# 샘플링하고 (2) 튜플에서 2개의 문자열을 샘플링하는 예이다.
# import random
# # (1) 숫자리스트 샘플링
# numlist = [1,2,3,4,5,6,7,8,9]
# s = random.sample(numlist, 3)
# print(s)  # [1, 2, 8]
# # (2) 튜플 샘플링
# frutes = ('사과', '귤', '포도', '배')
# s = random.sample(frutes, 2)
# print(s)  # ['배', '사과']
''' from random import *
i = randint(1, 100)  # 1부터 100 사이의 임의의 정수
print(i)
f = random()   # 0부터 1 사이의 임의의 float
print(f)
f = uniform(1.0, 36.5)   # 1부터 36.5 사이의 임의의 float
print(f)
i = randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
print(i)
i = randrange(10)  # 0부터 9 사이의 임의의 정수
print(i)
from random import randint
n = randint(1, 100)
while True:
    ans = input("Guess my number (Q to exit): ")
    if ans.upper() == "Q":
        break
    ians = int(ans)
    if (n == ians):
        print("Correct!")
        break
    elif (n > ians):
        print("Choose higher number")
    else:
        print("Choose lower number")
import random
# (1) 숫자리스트 샘플링
numlist = [1,2,3,4,5,6,7,8,9]
s = random.sample(numlist, 3)
print(s)  # [1, 2, 8]
# (2) 튜플 샘플링
frutes = ('사과', '귤', '포도', '배')
s = random.sample(frutes, 2)
print(s)  # ['배', '사과'] '''

# [직렬화와 역직렬화]
# 직렬화와 역직렬화
# 파이썬의 객체를 일련의 바이트들로 변환한 후 나중에 다시 파이썬 객체로 복원하게 할 수 있는데, 이렇게 파이썬 객체를 일련의 
# 바이트들로 변환하는 것을 직렬화(Serialization)라 하고, 다시 바이트들을 파이썬 객체로 메모리 상에 복원하는 것을
# 역직렬화(Deserialization)이라 한다. 직렬화된 바이트들은 외부 장치에 저장하거나 다른 시스템으로 전송할 수 있으며, 파이썬을 
# 사용하는 다른 시스템은 (OS와 같은 플랫폼 환경에 상관없이) 다시 이를 파이썬 객체로 역직렬화할 수 있다.
# 파이썬에서 직렬화(Serialization)와 역직렬화(Deserialization)를 사용하기 위해서는 pickle 모듈 혹은 cPickle 모듈을 사용한다.
# (참고: pickle 모듈은 파이썬으로 작성되었으며 cPickle 모듈은 C로 작성되어 있는데, cPickle 모듈이 더 빠르기 때문에 성능이 
# 중요한 경우 cPickle 을 사용하는 것이 좋다. 하지만, cPickle은 서브클래스를 만들 수 없기 때문에, 서브클래스를 작성할 필요가 
# 있으면 pickle 을 사용해야 한다. cPickle은 Python 2 에선 "import cPickle"을 사용하여 import 하고, Python 3에서는
#  "import _pickle"을 사용한다.)
# 아래 예제는 사각형 클래스의 객체를 이진 파일에 직렬화한 후 이를 다시 읽어들여 사각형 객체로 복원하는 역직렬화 과정을 
# 예시한 것이다. 직렬화하면 바이너리 형태이므로 이진 파일 모드로 파일을 열어야 한다. 아래 예제에서 복원된 객체 r 은 width,
# height 등의 attribute를 이전에 저장한 값 그대로 가지고 있다.
''' import pickle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
rect = Rectangle(10, 20)
# 사각형 rect 객체를 직렬화 (Serialization)
with open('rect.data', 'wb') as f:
    pickle.dump(rect, f)
# 역직렬화 (Deserialization)
with open('rect.data', 'rb') as f:
    r = pickle.load(f)
print("%d x %d" % (r.width, r.height)) '''

# [PEP 8 파이썬 코딩 스타일]
# Python Enhancement Proposal 8 (PEP 8)은 파이썬 코딩 스타일에 대한 가이드를 제시하고 있다. 
# PEP 8은 2001년 귀도 반 로썸에 의해 처음 제안되었으며, python.org 의 PEP 링크에 자세히 소개되어 있다.
# 파이썬 프로그래머들은 일반적으로 이러한 PEP 8 코딩 스타일에 따라 프로그래밍을 하고 있는데, 이러한 일관된 
# 코딩 스타일을 적용하는 것은 자신의 코드를 명료하게 할 뿐만 아니라 특히 다른 개발자 혹은 커뮤니티간 코딩을 공유할 때 매우
# 효율적이다.

# [PEP 8 의 중요한 부분에 대한 요약]
# 1.코드 레이아웃	
#   들여쓰기를 할 때 Tab 대신 공백(Space)을 사용한다. 특히 Python 3는 Tab과 공백을 혼용해서 사용하는 것을 허용하지 않는다.
#   문법적으로 들여쓰기를 할 때는 4개의 공백을 사용한다
#   각 라인은 79자 이하로 한다. 라인이 길어서 다음 라인으로 넘어갈 때는 원래 들여쓰기 자리에서 4개 공백을 더 들여쓴다.
#   함수나 클래스는 2개의 공백 라인을 추가하여 구분한다. 메서드는 한 개의 공백 라인으로 구분한다.
#   import는 (여러 모듈을 콤마로 연결하지 말고) 한 라인에 하나의 모듈을 import한다.
#   No: import os, sys
#   Yes: import os
#        import sys
#   컬렉션 인덱스나 함수 호출, 함수 파라미터 등에서 불필요한 공백을 넣지 않는다.
#   No: spam( ham[ 1 ], { eggs: 2 } )
#       bar = (0, )
#       spam (1)
#   Yes: spam(ham[1], {eggs: 2})
#        bar = (0,)
#        spam(1)
#   변수 할당시 할당자 앞뒤로 하나의 공백만 넣는다.
#   No: i=i+1
#   Yes: i = i + 1
#   2.명명규칙
#     함수, 변수, Attribute는 소문자로 단어 간은 밑줄(_)을 사용하여 연결한다
#     클래스는 단어 첫 문자마다 대문자를 써서 연결하는 CapWords 포맷으로 명명한다
#     모듈명은 짧게 소문자로 사용하며 밑줄을 쓸 수 있다. 패키지명 역시 짧게 소문자를 사용하지만 밑줄은 사용하지 않는다.
#     모듈 상수는 모두 대문자를 사용하고 단어마다 밑줄로 연결하는 ALL_CAPS 포맷으로 명명한다
#     클래스의 public attribute는 밑줄로 시작하지 말아야 한다
#     클래스의 protected instance attribute는 하나의 밑줄로 시작한다
#     클래스의 private instance attribute는 2개의 밑줄로 시작한다
#     인스턴스 메서드는 (객체 자신을 가리키기 위해) self 를 사용한다
#     클래스 메서드는 (클래스 자신을 가리키기 위해) cls 를 사용한다
#   3.문장과 표현식
#     if, for, while 블럭 문장을 한 라인으로 작성하지 말 것. 여러 라인에 걸쳐 사용하는 것이 더 명료함
#     a는 b가 아니다를 표현할 때 a is not b 를 사용한다. not a is b 를 사용하지 말 것
#     값이 비어있는지 아닌지를 검사하기 위해 길이를 체크하는 방식을 사용하지 말 것. 대신 if mylist 와 같이 표현함
#     import 문은 항상 파일의 상단에 위치하며, 표준 라이브러리 모듈, 3rd Party 모듈, 그리고 자신의 모듈 순으로 import 한다
#     모듈 import시 절대 경로를 사용할 것을 권장한다. 예를 들어, sibling 모듈이 현재 모듈과 같은 폴더에 있더라도 패키지명부터 
#     절대 경로를 사용함.
#     단, 복잡한 패키지 경로를 갖는 경우 상대경로(.)를 사용할 수 있다.

# [PEP]
# PEP 이란 Python Enhancement Proposals 의 약자로서 파이썬을 개선하기 위한 제안서를 의미한다.
# 이러한 PEP은 다음과 같이 크게 3 종류로 구분할 수 있으며, Python Software Foundation의 공식 웹사이트인 python.org 에서 관리한다.
# 1.파이썬에 새로운 기능(Feature)을 추가하거나 구현 방식을 제안하는 Standard Track PEP
# 2.파이썬 디자인 이슈를 설명하거나 일반적인 가이드라인 혹은 정보를 커뮤니티에 제공하는 Informational PEP
# 3.파이썬을 둘러싼 프로세스를 설명하거나 프로세스 개선을 제안하는 Process PEP. 예를 들어, 프로세스 절차, 가이드라인, 의사결정 방식의 개선,
# 파이썬 개발 도구 및 환경의 변경 등등.
# PEP은 파이썬 언어 자체 뿐만 아니라 코딩 표준, 커뮤니티 이슈 등을 담고 있는 유용한 자료이므로 파이썬을 배우면서 자주 참고하면 좋다. 
# PEP은 각 문서마다 번호가 지정되어 있는데, 
# PEP 번호별 내용은 https://www.python.org/dev/peps/ 에서 찾아 볼 수 있다.
# 특히, 파인썬 코딩과 관련한 코딩 표준(Coding Convention)에 관한 문서는 PEP 8 (https://www.python.org/dev/peps/pep-0008) 에 정의되어 있는데,
# 파이썬의 기초를 익힌 후 참조하면 파이썬 코딩 스타일을 익히는데 도움이 된다.

# [파이썬 Object Interning]
# 파이썬 Object Interning
# Interning이란 이미 생성된 객체(object)를 재사용(reuse)하는 것을 말하는데, 보통 Immutable 객체에 대해 Interning을 사용한다. 
# 파이썬은 기본적으로 몇가지 제한된 경우에 대해 디폴트로 Interning을 사용하고 있으며, 또한 개발자가 필요한 경우 함수를 써서
# Interning을 지정할 수도 있다.
# 아주 많이 사용되는 Immutable 객체의 경우 Interning을 사용하게 되면 메모리를 줄일 수 있는 효과가 있다.
# 파이썬 디폴트 Interning
# 파이썬은 기본적으로 몇가지 경우에 대해 시스템 디폴트로 Object Interning을 사용한다. 구체적으로 어떤 경우에 Interning을
# 사용하는가는 CPython, PyPy, Jython, IronPython 같은 각 구현체마다 다를 수 있지만, 기본이 되는 CPython의 경우 아래 조건에
# 해당될 경우 Object Interning을 사용한다.
# 문자열: 20자 미만의 공백을 포함하지 않는 문자열
# 정수: -5 부터 256 사이의 정수
# 예를 들어, 아래의 경우 처음 "Test" 문자열이 a 에 할당될 때, 이 문자열은 20자 미만 공백이 없는 문자열에 해당하므로 파이썬은 
# 이 문자열을 Intern 컬렉션에 넣고 그 주소를 a 에 할당한다. 이 a 의 메모리 주소를 알기 위해 id(a)와 같이 함수 id() 를 사용하였다.
# 다음 b 에 문자열 "Test"를 할당할 때, 파이썬은 먼저 Intern 컬렉션에서 "Test"라는 문자열이 있는지 검색하고, 만약 있으면 그 
# 메모리 주소를 b 에 할당한다. 하지만 만약 Intern 컬렉션에 해당 문자열이 없으면, 새로 Intern 컬렉션 안에 해당 문자열을 생성하고
# 그 주소를 b 에 할당한다.
# a = "Test"   # string intern
# b = "Test"   # string intern
# x = id(a)
# y = id(b)    # x,y 는 동일한 메모리 가리킴
# print(x, y)  # 2611825223136 2611825223136
# 또 다른 예제로 정수의 경우를 들어보면, 아래의 i, j는 -5 ~ 256 사이의 정수로 자동으로 Interning이 사용되고, 동일한 메모리를
# 사용하게 된다. i is j 는 i 와 j가 동일한 객체를 가리키는지를 체크하는 표현이다. 아래 x,y 는 256을 초과했으므로 Interning 이
# 사용되지 않았고, 서로 다른 메모리에 할당되었다.
# i = 10
# j = 10
# print(id(i), id(j), i is j) #2008444256 2008444256 True
# x = 257
# y = 257
# print(id(x), id(y), x is y) #2611825055632 2611825055568 False
# 파이썬 intern() 함수
# 파이썬의 intern() 함수는 문자열을 Interning하는 함수이다. 개발자는 자주 사용되는 문자열을 intern() 함수를 사용하여 Intern 
# 컬렉션에 저장해 놓고 사용할 수 있다. 파이썬 2 에서는 Built-in된 intern() 함수를 사용하고, 파이썬 3 에서는 sys 패키지의 
# intern() 함수를 사용한다.
# from sys import intern  # Python 3
# c = intern("Alex Lee")
# d = "Alex Lee"
# print(id(c), id(d), c is d) # 2987210077360 2987210078704 False
# e = intern("Alex Lee")
# print(id(c), id(e), c is e) # 2987210077360 2987210077360 True
''' a = "Test"   # string intern
b = "Test"   # string intern
x = id(a)
y = id(b)    # x,y 는 동일한 메모리 가리킴
print(x, y)  # 2611825223136 2611825223136
i = 10
j = 10
print(id(i), id(j), i is j) #2008444256 2008444256 True
x = 257
y = 257
print(id(x), id(y), x is y) #2611825055632 2611825055568 False
from sys import intern  # Python 3
c = intern("Alex Lee")
d = "Alex Lee"
print(id(c), id(d), c is d) # 2987210077360 2987210078704 False
e = intern("Alex Lee")
print(id(c), id(e), c is e) # 2987210077360 2987210077360 True '''

# [아나콘다(Anaconda)]
# 아나콘다(Anaconda)는 수학과 과학 분야에서 사용되는 여러 패키지들을 묶어 놓은 파이썬 배포판으로서 SciPy, Numpy, Matplotlib, Pandas 등을
# 비롯한 많은 패키지들을 포함하고 있다. Anaconda는 특히 최근에 데이타 사이언스와 머신 러닝 분야에서 파이썬을 사용하기 위해 기본적으로 설치하는 배포판이 되었다.
# Anaconda를 설치하기 위해서는 https://www.anaconda.com/ 웹사이트에서 자신의 OS에 맞는 프로그램을 다운받아 설치하면 된다. 통상 Python 3.x 버전을 선택한다.
# Anaconda 구성요소
# Anaconda는 아래 그림과 같이 크게 4 부분으로 나뉘는데, 이 중 Data Science 라이브러리와 Anaconda Navigator를 주목할 만하다. 
# Data Science 라이브러리는 (a) Jupyter와 같은 IDE 개발도구, (b) Numpy, SciPy 같은 과학 분석용 라이브러리,
# (c) Matplotlib 같은 데이타 시각화 (Data Visualization) 라이브러리, (d) TensorFlow 같은 머신 러닝(Machine Learning) 라이브러리 등을 포함하고 있다.
# Anaconda Navigator는 UI 클라이언트로서 하부 컴포넌트를 쉽게 사용하도록 한 데스크탑 포털 기능을 담당한다. 
# 예를 들어, Jupyter나 Spyder 같은 개발도구를 이곳에서 Launch할 수 있다.

# [Jupyter Notebook]
# 주피터 노트북(Jupyter Notebook)은 웹 브라우저에서 파이썬 코드를 작성하고 실행해 볼 수 있는 개발도구이다.
# 일반적으로 아나콘다(Anaconda)를 설치하면 Jupyter Notebook이 함께 설치되어 Jupyter를 사용할 수 있다. 
# 물론 Anaconda를 사용하지 않는 경우 pip 을 통해 Jupyter 패키지를 설치할 수도 있지만, 통상 Anaconda를 설치해서 사용할 것을 권장한다.
# Anaconda가 설치된 후, Anaconda 메뉴중 Jupyter Notebook을 선택하거나 Anaconda Navigator에서 Jupyter Notebook 메뉴를 선택하면 Jupyter를 실행할 수 있다.
# Anaconda 메뉴중 Jupyter Notebook을 선택한 경우, Jupyter Notebook 서버 (콘솔 프로그램)와 클라이언트로 사용되는 웹 브라우저 등 2개의 프로그램이
# 실행된다. Notebook 서버 프로그램은 백그라운드에서 실행되는 파이썬 프로그램으로 웹 브라우저 클라이언트가 접속하는 서버 프로그램이며 실제 파이썬
# 코드 실행은 여기에서 일어난다. 그리고, 웹 브라우저는 파이썬 코드를 입력받고, 실행해 볼 수 있는 UI를 제공하는 클라이언트로서 코드를 Notebook 서버에 보내
# 결과를 다시 웹 브라우저에 뿌려 주게 된다.
# Anaconda Navigator에서 Jupyter Notebook 메뉴를 선택한 경우에는 윈도우즈의 경우 Notebook 서버 콘솔 프로그램이 백그운드 프로세스로 실행되어 화면에 보이지 않으며,
# 클라이언트인 웹 브라우저만 화면에 나타난다. 하지만, 동작 방식은 기본적으로 동일하다.
# Jupyter Notebook 서버 프로그램은 디폴트로 웹 포트 8888 을 오픈하여 사용하며, 따라서 Jupyter Notebook 웹 브라우저는
# http://localhost:8888 을 통해 접속한다.

# [정수 / HexString 변환]
# 1. 정수를 16진수 문자열(Hex)로 변환하기
# Python 3는 정수를 16진수 문자열로 변환하는 hex() 라는 내장함수를 제공한다. hex() 함수는 정수를 입력받아 그 정수에 상응하는
# 16진수 문자열(hex string)을 리턴하는데, 문자열 앞에 자동으로 0x를 붙인다. 예를 들어, hex(123)은 '0x7b' 으로 변환된다.
# i = 123
# hexStr = hex(i)
# print(hexStr)  # '0x7b'
# 2. 문자를 ASCII 16진수 문자열(Hex)로 변환하기
# 영문자에 대한 ASCII 코드는 ord() 함수를 사용하여 구할 수 있다. 예를 들어, 문자 'A'에 대한 ASCII 코드는 ord('A') 를 
# 사용하여 65를 구할 수 있다. ASCII 코드에 대한 16진수 문자열(Hex String)을 구하기 위해서는 위에 말한 hex()를 사용하면 된다.
# a = hex(ord('A'))
# print(a)  # '0x41'
# 3. 16진수 문자열(Hex)을 정수로 변환하기
# 16진수 문자열을 정수로 변환하기 위해서는 int() 라는 내장함수를 사용할 수 있다. int() 함수의 첫번째 파라미터에는 16진수
# 문자열을 지정하고, 두번째 파라미터에는 이 문자열이 16진수(hexadecimal)로 되어 있음을 표시하는 16을 넣으면 된다.
# hexStr = '0x7b'
# i = int(hexStr, 16) # 16진수로 해석
# print(i)  # 123 출력
''' i = 123
hexStr = hex(i)
print(hexStr)  # '0x7b'
a = hex(ord('A'))
print(a)  # '0x41'
hexStr = '0x7b'
i = int(hexStr, 16) # 16진수로 해석
print(i)  # 123 출력 '''

# [문자열/바이트배열 변환]
# 1. 일정한 크기의 바이트배열 초기화
# 일정한 크기의 바이트 배열을 만들기 위해서는 bytearray() 함수에 원하는 크기를 지정하면 된다. 함수는 0x00을 요소로 갖는 바이트 
# 배열은 생성한다.
# a = bytearray(5)
# print(a) # bytearray(b'\x00\x00\x00\x00\x00')
# 2. 문자열을 바이트배열로 변환하기
# 문자열은 여러 가지 방식으로 인코딩 될 수 있기 때문에, 문자열은 지정된 인코딩을 통해 바이트배열로 변환하게 된다. 
# bytearray() 함수의 첫번째 파라미터에 문자열을 지정하고, 두번째 파라미터에 어떤 방식으로 인코딩했었는지를 지정하면, 문자열을
# 지정된 인코딩 방식으로 해석하여 바이트배열로 변환하게 된다. 아래 예제는 문자열을 UTF-8 방식으로 바이트배열로 변환하는 예이다.
# s = "Hi 서울"
# arr = bytearray(s, 'utf-8')
# print(arr) # bytearray(b'Hi \xec\x84\x9c\xec\x9a\xb8')
# 3. byte 리터럴을 바이트배열로 사용하기
# bytearray() 함수는 byte 리터럴(byte literal)을 전달받아 바이트배열로 사용할 수 있다. 예를 들어, 아래 b'Hello'와 같이 앞에
# b 접두어를 붙이면 byte literal이 되는데, bytearray() 함수는 이를 입력받아 배열처럼 사용할 수 있다.
# arr = bytearray(b'Hello')
# for elem in arr:
#     print(elem, end=' ') 
# # 출력: 72 101 108 108 111
''' a = bytearray(5)
print(a) # bytearray(b'\x00\x00\x00\x00\x00')
s = "Hi 서울"
arr = bytearray(s, 'utf-8')
print(arr) # bytearray(b'Hi \xec\x84\x9c\xec\x9a\xb8')
arr = bytearray(b'Hello')
for elem in arr:
    print(elem, end=' ') 
# 출력: 72 101 108 108 111 '''