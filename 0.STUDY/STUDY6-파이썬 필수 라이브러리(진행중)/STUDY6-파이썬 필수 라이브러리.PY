# 출처 [https://wikidocs.net/book/5445, 파이썬 필수 라이브러리]


# [01장 텍스트 처리 서비스]

# [01-01 문자열 말줄임 - textwrap.shorten]
# textwrap.shorten은 문자열을 특정길이에 맞게 말줄임(...)을 할 수 있도록 도와주는 파이썬 표준 라이브러리이다.
# 문제
# 다음 문자열을 길이 15자리가 넘지 않도록 말줄임하여 표시하시오. (단, 길이가 15자리가 넘지 않을 경우에는 그대로 표시)
# Life is too short, you need python
# 풀이
# import textwrap
# result = textwrap.shorten("Life is too short, you need python", width=15)
# print(result)
# 결과는 다음과 같다.
# Life is [...]
# 이 때 문자열에 포함된 모든 연속된 공백 문자열은 단일 공백 문자열로 축약된다. 그리고 매개변수 width에 전달된 길이만큼 문자열이 표시된다. 이 때 축약된 문자열을 의미하는 [...] 문자 역시 길이에 포함되며 줄여지는 문자열은 단어단위로 길이에 맞게 생략된다.
# 한글 문자열인 경우도 다음처럼 동일하게 수행된다. 단, 한글 1문자도 역시 길이 1로 계산된다는 점에 유의하자.
# import textwrap
# result = textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15)
# print(result)
# 결과는 다음과 같다.
# 인생은 짧으니 [...]
# 활용예
# 코딩도장의 문제 요약중 내용이 많을 경우 다음처럼 말줄임으로 표시한다. textwrap.shorten 을 사용하면 이런 화면을 쉽게 만들수 있다.
''' import textwrap
result = textwrap.shorten("Life is too short, you need python", width=15)
print(result)
import textwrap
result = textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15)
print(result) '''

# [01-02 문자열 줄바꿈 - textwrap.wrap]
# textwrap.wrap은 문자열을 특정길이에 맞게 줄바꿈(wrapping)할 수 있게 해주는 파이썬 표준 라이브러리이다. 
# 문자열 래핑은 문자열이 너무 길어질 경우 특정 길이에서 줄바꿈을 하려고 할때 필요하다.
# 문제
# 다음과 같이 긴 문자열 long_text가 있다.
# >>> long_text = 'Life is too short, you need python. ' * 10
# >>> long_text
# 'Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. '
# long_text를 70바이트 길이로 줄바꿈 하시오.
# 풀이
# import textwrap
# long_text = 'Life is too short, you need python. ' * 10
# result = textwrap.wrap(long_text, width=70)
# print(result)
# 출력결과는 다음과 같다.
# ['Life is too short, you need python. Life is too short, you need', 'python. Life is too short, you need python. Life is too short, you', 'need python. Life is too short, you need python. Life is too short,', 'you need python. Life is too short, you need python. Life is too', 'short, you need python. Life is too short, you need python. Life is', 'too short, you need python.']
# textwrap.wrap 함수는 긴 문자열을 매개변수 width로 전달한 70바이트 길이만큼 잘라서 리스트로 리턴해 준다. 이것을 고정폭 문자열로 표시하려면 다음과 같이 하면 된다.
# '\n'.join(result)
# 하지만 textwrap.fill 함수를 사용하면 다음처럼 이 과정을 축약할 수 있다.
# import textwrap
# long_text = 'Life is too short, you need python. ' * 10
# result = textwrap.fill(long_text, width=70)
# print(result)
# 출력결과는 다음과 같다.
# Life is too short, you need python. Life is too short, you need
# python. Life is too short, you need python. Life is too short, you
# need python. Life is too short, you need python. Life is too short,
# you need python. Life is too short, you need python. Life is too
# short, you need python. Life is too short, you need python. Life is
# too short, you need python.
''' import textwrap
long_text = 'Life is too short, you need python. ' * 10
result = textwrap.wrap(long_text, width=70)
print(result)
import textwrap
long_text = 'Life is too short, you need python. ' * 10
result = textwrap.fill(long_text, width=70)
print(result) '''

# [01-03 문자열의 차이 - diff_match_patch]
# diff_match_patch는 두 개의 파일 또는 두 개의 문자열 사이의 차이점을 보여주는 라이브러리이다.
# 설치
# pip install diff_match_patch
# 문제
# 다음과 같은 문자열이 있다.
# Life is too short, you need python.
# 위 문자열이 다음처럼 바뀌었다.
# Life is short, you need python language.
# 이 때 어떤 부분이 추가되었고 어떤 부분이 삭제되었는지를 알려주는 코드를 작성하시오.
# 풀이
# 다음은 diff_match_patch를 사용한 해법이다.
# from diff_match_patch import diff_match_patch
# before = "Life is too short, you need python."
# after = "Life is short, you need python language."
# dmp = diff_match_patch()
# diff = dmp.diff_main(before, after)
# dmp.diff_cleanupSemantic(diff)
# for d in diff:
#     print(d)
# diff_match_patch() 로 dmp객체 생성후 dmp.diff_main(before, after) 로 변경전 내용과 변경후 내용을 입력으로 diff 객체를 생성하였다.
# 이렇게 diff 객체를 생성하면 이후 dmp.diff_cleanupSemantic(diff) 와 같은 함수를 사용할 수 있게 된다.
# 출력 결과는 다음과 같다.
# (0, 'Life is ')
# (-1, 'too ')
# (0, 'short, you need python')
# (1, ' language')
# (0, '.')
# diff_cleanupSemantic은 변경단위를 튜플로 묶어서 리턴한다. 튜플의 첫번째 숫자는 다음과 같은 의미를 같는다.
# 숫자	의미
# 0	동일한 문자열
# 1	추가된 문자열
# -1	삭제된 문자열
# 따라서 출력 결과 중 (0, 'Life is ') 의 의미는 Life is 는 이전 내용과 이후 내용이 동일하다는 의미이고 (-1, 'too ')는 이전 내용에서
# too 라는 문자열이 삭제되었음을 의미한다.
''' from diff_match_patch import diff_match_patch
before = "Life is too short, you need python."
after = "Life is short, you need python language."
dmp = diff_match_patch()
diff = dmp.diff_main(before, after)
dmp.diff_cleanupSemantic(diff)
for d in diff:
    print(d) '''


# [02장 바이너리 데이터 서비스]

# [02-01 C 구조체 다루기 - struct]
# struct는 C 구조체로 만들어진 이진 데이터를 처리하기 위해 사용되는 파이썬 표준 라이브러리이다.
# C 구조체로 만들어진 파일을 읽거나 네트워크로 전달되는 C 구조체 이진 데이터를 파이썬에서 처리하기위해 주로 사용된다.
# 문제
# 다음과 같이 C로 작성되어진 프로그램이 있다. save_type이라는 구조체 데이터를 output이라는 파일에 저장하는 프로그램이다.
# save_type은 double형 1개, int형 1개, char형 1개로 이루어진 구조체이다.
# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
# typedef struct { 
#     double v; 
#     int t; 
#     char c;
# } save_type;
# int main() {
#     save_type s = {7.5f, 15, 'A'};
#     FILE *f = fopen("output", "w");
#     fwrite(&s, sizeof(save_type), 1, f);
#     fclose(f);
#     return 0;
# }
# 위 프로그램을 실행했을때 생성되는 output파일을 읽어서 저장된 값을 출력하는 파이썬 프로그램을 작성하시오.
# 풀이
# 다음처럼 struct의 unpack을 사용하면 C 구조체 데이터를 쉽게 읽을 수 있다.
# import struct
# with open('output', 'rb') as f:
#     chunk = f.read(16)
#     result = struct.unpack('dicccc', chunk)
#     print(result)
# unpack에 사용된 'dicccc'의 의미는 double형 1개, int형 1개, char형 4개를 의미한다. 
# 위 C코드의 save_type 구조체는 double형 1개, int형 1개, char형 1개를 사용했지만 unpack은 구조체의 전체길이인 16사이즈에 맞게 설정하여 unpack을 해야 한다.
# 위 구조체의 길이가 16이 된 이유는 C의 구조체의 특징 때문인데 가장 큰 double형의 길이가 8바이트이므로 8바이트의 배수로 구조체의 길이가 결정되기 때문이다.
# 따라서 위 구조체의 길이는 16바이트가 되어 실제 길이는 13바이트지만 나머지 3바이트는 널값으로 채워지게 된다.
# 다음은 위 구조체에서 사용된 멤버들의 타입과 파이썬 타입을 표로 표시한 것이다. double은 총 8바이트의 길이를 갖는다.
# Format	C Type	Python Type	Standard Size
# d	double	float	8
# i	int	integer	4
# c	char	bytes of length 1	1
# 위에 작성한 파이썬 프로그램을 실행하면 다음과 같은 결과값이 출력된다.
# (7.5, 15, 'A', 'V', '\x00', '\x00')
# 앞의 3개 항목을 보면 구조체에 저장된 7.5, 15, 'A' 데이터를 정상적으로 읽었음을 확인할 수 있다. 뒤에 3개의 값은 Null 또는 의미없는 값으로 채워진다.
# 파이썬에서 이진데이터를 읽을때는 struct.unpack을 사용하고 이진데이터를 생성할때는 다음처럼 struct.pack을 사용하면 된다.
# struct.pack('dicccc', 7.5, 15, b'A', b'\x00', b'\x00', b'\x00')
# C 구조체의 char형의 데이터를 생성하기 위해서는 위처럼 1자리수의 byte문자열로 생성해 주어야 한다.
''' import struct
with open('output', 'rb') as f:
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk)
    print(result)
    result = struct.pack('dicccc', 7.5, 15, b'A', b'\x00', b'\x00', b'\x00')
    print(result) '''


# [03장 데이터형]
# 이 장에서는 날짜와 시간, 힙큐, 데크, 열거형과 같은 특수 데이터형을 다루는 라이브러리에 대해서 알아본다.]

# [03-01 두 날짜의 차이 - datetime.date]
# datetime.date는 년, 월, 일로 날짜를 표현할 때 사용되는 파이썬 표준 라이브러리이다.
# 문제1
# 2020년 12월 14일(2020-12-14)과 1995년 6월 5일(1995-06-05)의 두 날짜의 차이 일자를 구하시오.
# 풀이1
# 년월일(year, month, day)을 알수 있다면 다음과 같이 datetime.date 객체를 만들 수 있다.
# >>> import datetime
# >>> day1 = datetime.date(2020, 12, 14)
# >>> day1
# datetime.date(2020, 12, 14)
# >>> day2 = datetime.date(1995, 6, 5)
# >>> day2
# datetime.date(1995, 6, 5)
# 위 코드와 같이 datetime.date 객체는 년, 월, 일을 인수로 전달하여 생성할 수 있다. 2020년 12월 14일에 해당되는 date객체는 day1, 
# 1995년 6월 5일에 해당되는 date객체는 day2로 생성하였다.
# 두 날짜의 차이는 다음과 같은 산술식으로 쉽게 구할 수 있다.
# >>> interval = day1 - day2
# >>> interval
# datetime.timedelta(days=9324)
# >>> interval.days
# 9324
# day1에서 day2를 빼면 datetime.timedelta 객체가 리턴되고 이 객체를 이용하면 위와 같이 두 날짜의 차이 일자를 구할 수 있다.
# datetime.timedelta 는 https://wikidocs.net/104836 문서를 참고하도록 하자.
# datetime.date는 년, 월, 일로만 구성된 날짜이다. 만약 시, 분, 초까지 포함한 날짜 데이터를 생성하려면 다음과 같이 datetime.datetime 을 사용해야 한다.
# >>> import datetime
# >>> day3 = datetime.datetime(2020, 12, 14, 14, 10, 50)
# >>> day3.hour
# 14
# >>> day3.minute
# 10
# >>> day3.second
# 50
# 또는 다음과 같이 datetime.date 객체와 datetime.time 객체를 combine 함수를 사용하여 합쳐서 만들수도 있다.
# >>> import datetime
# >>> day = datetime.date(2020, 12, 14)
# >>> time = datetime.time(10, 14, 50)
# >>> dt = datetime.datetime.combine(day, time)
# >>> dt
# datetime.datetime(2020, 12, 14, 10, 14, 50)
# 문제2
# 2020년 12월 14일은 무슨 요일인가?
# 풀이2
# 요일은 datetime.date 객체의 weekday 함수를 사용하면 쉽게 구할 수 있다.
# >>> import datetime
# >>> day = datetime.date(2020, 12, 14)
# >>> day.weekday()
# 0
# 0은 월요일을 의미한다. 차례대로 1은 화요일, 2는 수요일, 6은 일요일이 된다.
# 만약 월요일은 1, 화요일은 2, ..., 일요일은 7을 리턴하게 하려면 다음처럼 isoweekday 함수를 사용하면 된다.
# >>> day.isoweekday()
# 1
# 2020년 12월 14일은 월요일이므로 isoweekday를 사용할 경우 월요일을 의미하는 1이 리턴된다.
''' import datetime
day1 = datetime.date(2020, 12, 14)
day2 = datetime.date(1995, 6, 5)
interval = day1 - day2
print(day1,day2)
print(interval.days)
import datetime
day3 = datetime.datetime(2020, 12, 14, 14, 10, 50)
print(day3)
import datetime
day = datetime.date(2020, 12, 14)
time = datetime.time(10, 14, 50)
dt = datetime.datetime.combine(day, time)
daytime = datetime.datetime(2020, 12, 14, 10, 14, 50)
print(day)
print(time)
print(dt)
print(daytime)
import datetime
day = datetime.date(2020, 12, 14)
print(day.weekday())
print(day.isoweekday()) '''

# [03-02 날짜 더하기 - datetime.timedelta]
# datetime.timedelta 는 두 날짜나 시간의 차이인 기간을 나타낼 때 사용하는 파이썬 표준 라이브러리이다. 
# timedelta 객체에는 산술 연산자(+, -)를 사용할 수 있기 때문에 어떤 날짜에 특정 기간(일, 시, 분, 초)을 더하거나 뺄 수 있다.
# 문제
# 오늘로부터 50일 이후의 날짜를 구하는 코드를 작성하시오.
# 풀이
# 먼저 오늘 일자를 알기 위해 datetime.date.today() 로 오늘 일자를 얻는다.
# >>> import datetime
# >>> today = datetime.date.today()
# >>> today
# datetime.date(2020, 12, 14)
# today는 현재일자를 반환하므로 위의 경우 오늘 일자는 2020년 12월 14일임을 나타낸다.
# 오늘로부터 50일 이후의 일자를 얻기 위해서 datetime.timedelta(days=50) 로 50일을 뜻하는 datetime.timedelta 객체가 필요하다.
# >>> later = datetime.timedelta(days=50)
# >>> later
# datetime.timedelta(days=50)
# timedelta에는 days파라미터 외에도 다음과 같은 것들을 사용할 수 있다.
# 항목	설명
# days	일
# seconds	초
# microseconds	마이크로초
# milliseconds	밀리초 (1밀리초는 1000마이크로초)
# minutes	분
# hours	시간
# weeks	주 (7일을 의미함)
# 이제 오늘일자 + 50일 에 해당하는 다음의 산술식을 사용하면 50일 이후의 일자를 쉽게 얻을 수 있다.
# >>> today + later
# datetime.date(2021, 2, 2)
# 오늘(2020년 12월 14일)로부터 50일 이후의 일자는 2021년 2월 2일임을 알수 있다.
# 만약 50일 전의 일자를 알고 싶다면 today - later 산술식을 사용하면 된다.
''' import datetime
today = datetime.date.today()
later = datetime.timedelta(days=50)
print(today + later) '''

# [03-03 윤년확인 - calendar.isleap]
# calendar는 달력과 관련된 유용한 함수들을 제공하는 파이썬 표준 라이브러리이다.
# 문제
# 다음 년도들이 윤년이면 True 아니면 False를 출력하시오.
# 0 년
# 1 년
# 4 년
# 1200 년
# 700 년
# 2020 년
# 풀이
# 윤년의 정의
# 서력 기원 연수가 4로 나누어 떨어지는 해는 우선 윤년으로 하고,
# 그 중에서 100으로 나누어 떨어지는 해는 평년으로 하며,
# 400으로 나누어 떨어지는 해는 다시 윤년으로 정하였다.
# 윤년의 경우 2월달의 일수는 28일이 아닌 29일이 된다.
# 윤년의 정의에 맞게 작성된 파이썬 함수는 다음과 같다.
# def is_leap_year(year):
#     if year % 400 == 0: 
#         return True
#     if year % 100 == 0: 
#         return False
#     if year % 4 == 0: 
#         return True
#     return False
# 하지만 다음처럼 calendar의 isleap 함수를 사용하는 것이 간편하다.
# >>> import calendar
# >>> calendar.isleap(0)
# True
# >>> calendar.isleap(1)
# False
# >>> calendar.isleap(4)
# True
# >>> calendar.isleap(1200)
# True
# >>> calendar.isleap(700)
# False
# >>> calendar.isleap(2020)
# True
''' import calendar
print(calendar.isleap(0))
print(calendar.isleap(1))
print(calendar.isleap(4))
print(calendar.isleap(1200))
print(calendar.isleap(700))
print(calendar.isleap(2020))
print(calendar.calendar(2020)) '''

# [03-04 데크 - collections.deque]
# deque는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료구조이다. 양방향이기 때문에 스택(Stack)처럼 써도 되고 큐(Queue)처럼 써도 된다.
# deque는 "데크"라고 읽는다.
# 문제
# 다음과 같은 리스트가 있다.
# a = [1, 2, 3, 4, 5]
# 위 리스트를 2만큼 오른쪽으로 회전하여 다음과 같은 리스트를 만드시오.
# [4, 5, 1, 2, 3]
# 풀이
# 리스트에서 n만큼 회전하는 문제는 알고리즘 퀴즈 중에서도 자주 등장한다. collections.deque를 사용하면 아주 간단하게 이 문제를 해결할 수 있다.
# from collections import deque
# a = [1, 2, 3, 4, 5]
# q = deque(a)
# q.rotate(2)
# result = list(q)
# print(result)
# deque(a) 로 deque객체를 만든 후 rotate함수를 사용하여 2만큼 우측으로 회전하였다. (만약 좌측으로 2만큼 회전한다면 2대신 -2를 입력하면 된다.)
# list와 비슷한 deque
# deque의 사용법을 잠시 살펴보자.
# >>> from collections import deque
# >>> d = deque([1,2,3,4,5])
# >>> d.append(6)
# >>> d
# deque([1, 2, 3, 4, 5, 6])
# >>> d.appendleft(0)
# >>> d
# deque([0, 1, 2, 3, 4, 5, 6])
# >>> d.pop()
# 6
# >>> d
# deque([0, 1, 2, 3, 4, 5])
# >>> d.popleft()
# 0
# >>> d
# deque([1, 2, 3, 4, 5])
# >>>
# 위의 예제를 보면 알겠지만 deque는 list와 거의 흡사하다. 스택과 큐로 사용할 수 있는 메써드들도 대부분 일치한다.
# 다만 deque에는 다음과 같은 메써드들이 추가로 존재한다.
# appendleft
# popleft
# 예를 들어 리스트의 경우 첫번째 요소를 삭제할 경우 pop(0) 를 사용하지만 deque는 popleft를 사용한다. 
# 리스트를 사용하면 deque를 쓰는 것과 동일한 효과를 낼 수 있지만 deque를 사용하면 스택, 큐 작업시 다음과 같은 장점들이 있으니 참고하자.
# deque는 list보다 속도가 빠르다. pop(0)와 같은 메서드를 수행할 때 리스트의 경우 O(N)연산을 수행하지만 deque는 O(1) 연산을 수행하기 때문이다.
# 쓰레드 환경에서 안전하다.
''' from collections import deque
a = [1, 2, 3, 4, 5]
q = deque(a)
q.rotate(2)
result = list(q)
print(result) '''

# [03-05 키값이 있는 튜플 - collections.namedtuple]
# 튜플(tuple)은 인덱스를 통해서만 데이터에 접근이 가능하지만 네임드튜플(namedtuple)은 인덱스뿐만 아니라 키(Key) 값으로도 데이터 접근이 가능한 자료형이다.
# 문제
# 다음과 같은 데이터베이스 테이블이 있다.
# 테이블명: employees
# 컬럼	설명
# name	이름
# age	나이
# cellphone	휴대전화
# 이 테이블의 전체 데이터를 조회하는 코드는 다음과 같다.
# import sqlite3
# conn = sqlite3.connect('/companydata')
# cursor = conn.cursor()
# cursor.execute('SELECT name, age, cellphone FROM employees')
# data = cursor.fetchall()
# print(data)
# conn.close()
# 출력결과는 다음과 같다.
# [('홍길동', 23, '01099990001'), ('김철수', 31, '01099991002'), ('이영희', 29, '01099992003'), ... ]
# 하지만 결과 리스트의 요소가 튜플이어서 데이터에 접근하기가 쉽지 않다. 왜냐하면 데이터를 확인하기 위해서는 튜플 데이터의
# 인덱스 순서가 무엇을 의미하는지 알고 있어야 하기 때문이다.
# 다음처럼 튜플 데이터를 각 컬럼의 이름으로 접근할 수 있도록 코드를 재구성 하시오.
# employee = data[0]  # 첫번째 직원
# print(employee.name)  # "홍길동" 출력
# print(employee.age)  # 23 출력
# print(employee.cellphone)  # 01099990001 출력
# 풀이
# 튜플 데이터를 이름으로 접근하기 위해서는 여러가지 방법이 있을 수 있다. 일반적으로 클래스를 이용한 해법이 있지만 여기서는 이 문제를
# 가장 간단하게 해결할 수 있는 namedtuple을 사용해 보자.
# from collections import namedtuple
# data = [
#     ('홍길동', 23, '01099990001'),
#     ('김철수', 31, '01099991002'),
#     ('이영희', 29, '01099992003'),
# ]
# Employee = namedtuple('Employee', 'name, age, cellphone')  # namedtuple 자료형 생성
# data = [Employee(row[0], row[1], row[2]) for row in data]  # data의 row를 튜플에서 namedtuple로 변환
# employee = data[0]  # 첫번째 직원
# print(employee.name)  # "홍길동" 출력
# print(employee.age)  # 23 출력
# print(employee.cellphone)  # 01099990001 출력
# namedtuple 함수의 첫번째 입력항목은 namedtuple의 자료형의 명칭(type name)이다. 보통 namedtuple로 생성되는 객체명과 동일하게 한다. 
# 여기서는 Employee로 명명하였다. 뒤에 따라오는 콤마로 구성된 문자열은 Employee의 속성이 된다.
# 그리고 리스트 내포를 이용하여 data의 각 튜플들을 모두 Employee 자료형으로 교체하였다.
# namedtuple로 생성한 Employee의 _make 함수를 사용하면 다음처럼 보다 깔끔한 코드를 작성할 수 있다.
# from collections import namedtuple
# data = [
#     ('홍길동', 23, '01099990001'),
#     ('김철수', 31, '01099991002'),
#     ('이영희', 29, '01099992003'),
# ]
# Employee = namedtuple('Employee', 'name, age, cellphone')  # namedtuple 자료형 생성
# data = [Employee._make(row) for row in data]  # data의 row를 튜플에서 namedtuple로 변환
# employee = data[0]  # 첫번째 직원
# print(employee.name)  # "홍길동" 출력
# print(employee.age)  # 23 출력
# print(employee.cellphone)  # 01099990001 출력
# namedtuple 자료형은 다음처럼 _asdict()를 사용하면 딕셔너리로 쉽게 변환할 수 있다.
# employee = data[0]  # 첫번째 직원
# print(employee._asdict())
# 출력결과는 다음과 같다.
# {'name': '홍길동', 'age': 23, 'cellphone': '01099990001'}
# 또한 네임드튜플은 다음처럼 인덱스 접근도 가능하다.
# employee = data[0]  # 첫번째 직원
# print(employee[0])  # "홍길동" 출력
# print(employee[1])  # 23 출력
# print(employee[2])  # 01099990001 출력
# 그리고 네임드튜플은 튜플의 값을 변경할 수 없는(immutable) 특징을 그대로 가지고 있기 때문에 속성 값을 변경하려고 하면 오류가 발생한다.
# employee = data[0]  # 첫번째 직원
# employee.name = "박길동"
# 위와 같이 값을 변경하려고 하면 다음과 같은 오류가 발생한다.
# Traceback (most recent call last):
#   File ...
#     employee.name = "박길동"
# AttributeError: can't set attribute
# 값을 변경하려면 다음처럼 _replace 함수를 통해서만 가능하다. 하지만 _replace 함수는 해당 객체를 직접 변경하는 것은 아니고 
# 변경된 새로운 객체를 만들어서 리턴해 준다는 점에 유의하도록 하자.
# employee = data[0]  # 첫번째 직원
# new_employee = employee._replace(name="박길동")
''' from collections import namedtuple
data = [
    ('홍길동', 23, '01099990001'),
    ('김철수', 31, '01099991002'),
    ('이영희', 29, '01099992003'),
]
Employee = namedtuple('Employee', 'name, age, cellphone')  # namedtuple 자료형 생성
data = [Employee._make(row) for row in data]  # data의 row를 튜플에서 namedtuple로 변환
print(data)
employee = data[0]  # 첫번째 직원
print(employee.name)  # "홍길동" 출력
print(employee.age)  # 23 출력
print(employee.cellphone)  # 01099990001 출력
for i in range(0,len(data)):
    employee = data[i]  # 첫번째 직원
    print(employee._asdict()) '''

# [03-06 동일한 요소의 갯수 - collections.Counter]
# collections.Count는 리스트나 문자열과 같은 자료형의 요소 중 동일한 값의 요소가 몇개인지를 파악하는데 사용되는 파이썬 표준 라이브러리이다.
# 문제
# 다음은 김소월의 시 "산유화" 이다.
# 산에는 꽃 피네.
# 꽃이 피네.
# 갈 봄 여름없이
# 꽃이 피네.
# 산에
# 산에
# 피는 꽃은
# 저만치 혼자서 피어있네.
# 산에서 우는 새여
# 꽃이 좋아
# 산에서
# 사노라네.
# 산에는 꽃지네
# 꽃이 지네.
# 갈 봄 여름 없이
# 꽃이 지네.
# 위 시에서 사용된 단어중 가장 많이 사용된 단어와 그 단어의 사용횟수를 구하시오.
# 풀이
# 이 문제를 해결하려면 산유화 시를 단어별로 나누고 딕셔너리를 사용하여 단어별로 값을 0으로 초기화 한 후 해당 단어가 반복될 때마다
# 1씩 증가시켜 빈도수를 알아내는 방법을 써야 한다.하지만 여기서는 보다 쉬운 방법으로 이 문제를 해결해 보자.
# from collections import Counter
# import re
# data = """
# 산에는 꽃 피네.
# 꽃이 피네.
# 갈 봄 여름없이
# 꽃이 피네.
# 산에
# 산에
# 피는 꽃은
# 저만치 혼자서 피어있네.
# 산에서 우는 새여
# 꽃이 좋아
# 산에서
# 사노라네.
# 산에는 꽃지네
# 꽃이 지네.
# 갈 봄 여름 없이
# 꽃이 지네.
# """
# words = re.findall(r'\w+', data)
# counter = Counter(words)
# print(counter.most_common(1))
# 우선 문장을 단어별로 나누기 위해 다음처럼 re 모듈을 사용했다.
# words = re.findall(r'\w+', data)
# \w+ 는 단어를 의미하므로 re.findall에 의해서 산유화 시의 모든 단어가 리스트로 리턴된다. counter = Counter(words) 는 단어 리스트를 입력으로
# counter 객체를 생성하였다.
# 만약 생성된 counter객체를 print(counter)로 출력해 본다면 다음과 같이 출력될 것이다.
# Counter({'꽃이': 5, '피네': 3, '산에는': 2, '갈': 2, '봄': 2, '산에': 2, '산에서': 2, '지네': 2, '꽃': 1, '여름없이': 1, '피는': 1, '꽃은': 1, '저만치': 1, '혼자서': 1, '피어있네': 1, '우는': 1, '새여': 1, '좋아': 1, '사노라네': 1, '꽃지네': 1, '여름': 1, '없이': 1})
# 모든 단어가 빈도수가 큰 것부터 차례로 출력된 모습이다.
# 하지만 우리가 원하는 것은 가장 빈도수가 높은 1개의 단어이므로 Counter객체의 most_common 메서드를 이용하여 다음과 같이 출력하였다.
# print(counter.most_common(1))
# 출력 결과는 다음과 같다.
# [('꽃이', 5)]
# most_common 메서드는 빈도수가 높은 것부터 입력으로 받은 갯수만큼 튜플로 리턴한다. 만약 빈도수가 높은 2개의 단어를 보고 싶다면 다음과 같이 출력하면 된다.
# print(counter.most_common(2))
# 출력 결과는 다음과 같을 것이다.
# [('꽃이', 5), ('피네', 3)]
''' from collections import Counter
import re
data = """
산에는 꽃 피네.
꽃이 피네.
갈 봄 여름없이
꽃이 피네.
산에
산에
피는 꽃은
저만치 혼자서 피어있네.
산에서 우는 새여
꽃이 좋아
산에서
사노라네.
산에는 꽃지네
꽃이 지네.
갈 봄 여름 없이
꽃이 지네.
"""
words = re.findall(r'\w+', data)
counter = Counter(words)
print(counter)
print(counter.most_common(1))
print(counter.most_common(2)) '''

# [03-07 딕셔너리의 초깃값 - collections.defaultdict]
# collections.defaultdict는 딕셔너리의 value에 초기값을 지정하여 사용할 수 있게 해주는 파이썬 표준 라이브러리이다.
# 문제
# 다음과 같은 문자열이 있다.
# Life is too short, You need python.
# 위 문자열을 이용하여 다음처럼 사용된 문자와 그 사용횟수로 구성된 딕셔너리를 만드시오.
# {'L': 1, 'i': 2, 'f': 1, 'e': 3, ' ': 6, 's': 2, 't': 3, 'o': 5, 'h': 2, 'r': 1, ',': 1, 'Y': 1, 'u': 1, 'n': 2, 'd': 1, 'p': 1, 'y': 1, '.': 1}
# 풀이
# 다음은 일반적인 풀이방법이다.
# text = "Life is too short, You need python."
# d = dict()
# for c in text:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1
# print(d)
# 딕셔너리 d의 키에 해당 문자가 없을 경우 그 문자를 키로 등록하고 값은 0으로 초기화 해주는 방어적인 코드를 삽입했다. 
# 만약 방어적인 코드없이 다음처럼 작성한다면 오류가 발생할 것이다.
# text = "Life is too short, You need python."
# d = dict()
# for c in text:
#     d[c] += 1
# print(d)
# 위와 같이 작성하면 다음과 같은 KeyError 오류가 발생한다.
# Traceback (most recent call last):
#   File "...", line 5, in <module>
#     d[c] += 1
# KeyError: 'L'
# 딕셔너리로 위와 같이 집계를 위한 코드를 작성할 경우에 초기 값은 항상 신경써야 하는 부분이다.
# 하지만 collections의 defaultdict를 사용하면 이러한 불편함을 없앨수 있다.
# 다음은 collections의 defaultdict를 이용한 방법이다.
# from collections import defaultdict
# text = "Life is too short, You need python."
# d = defaultdict(int)
# for c in text:
#     d[c] += 1
# print(d)
# defaultdict의 인수로 int를 전달하여 딕셔너리 d의 value를 int로 초기화 해 주었다. 따라서 이제 방어적인 코드없이도 코드를 간결하게 작성할 수 있게 되었다.
# defaultdict의 인수에는 int외에도 list등 여러 자료형을 사용할 수 있으니 자세한 내용은 "참고"의 URL에서 확인해 보자.
''' from collections import defaultdict
text = "Life is too short, You need python."
d = defaultdict(int)
for c in text:
    d[c] += 1
print(d) '''

# [03-08 우선 순위 큐 - heapq]
# heapq는 우선 순위가 가장 높은 자료(data)를 가장 먼저 꺼낼 수 있는 우선 순위 큐이다. 리스트등을 사용하여 우선 순위 큐를 직접 구현하는 것이 어렵진
# 않지만 이런 작업에 최적화된 파이썬 표준 라이브러리인 heapq를 사용하는 것이 좋다.
# 문제
# 다음은 어떤 육상대회의 100m 달리기 기록이다.
# 강보람  12.23
# 김지원  12.31
# 박시우  11.98
# 장준혁  11.99
# 차정웅  11.67
# 박중수  12.02
# 차동현  11.57
# 고미숙  12.04
# 한시우  11.92
# 이민석  12.22
# 총 3명에게 금, 은, 동메달을 수여하려고 한다. 기록이 가장 좋은 순서로 3명을 뽑아내는 코드를 작성하시오.
# 풀이
# 다음은 heapq를 사용한 풀이이다.
# import heapq
# data = [
#     (12.23, "강보람"),
#     (12.31, "김지원"),
#     (11.98, "박시우"),
#     (11.99, "장준혁"),
#     (11.67, "차정웅"),
#     (12.02, "박중수"),
#     (11.57, "차동현"),
#     (12.04, "고미숙"),
#     (11.92, "한시우"),
#     (12.22, "이민석"),
# ]
# h = []  # 힙 생성
# for score in data:
#     heapq.heappush(h, score)  # 힙에 데이터 저장
# for i in range(3):
#     print(heapq.heappop(h))  # 우선 순위 순으로 힙 반환
# 힙으로 사용할 h변수를 빈리스트로 생성하고 heappush로 힙에 데이터들을 추가했다. 이 때 데이터는 기록(100m 달리기 성적)과 이름을 쌍으로 갖는 튜플이며
# 우선순위는 튜플의 첫번째 항목이어야 한다. 따라서 우선순위는 기록을 튜플의 첫번째 요소로 해야한다. 그리고 금, 은, 동 메달을 수여하기 위해 heappop으로 
# 성적이 가장 좋은(가장 작은 값) 데이터를 3개를 출력하였다.
# 출력결과는 다음과 같다.
# (11.57, '차동현')
# (11.67, '차정웅')
# (11.92, '한시우')
# 힙 데이터를 생성하는 부분은 다음과 같이 heapify 함수를 사용하여 간략화 할 수 있다.
# import heapq
# data = [
#     (12.23, "강보람"),
#     (12.31, "김지원"),
#     (11.98, "박시우"),
#     (11.99, "장준혁"),
#     (11.67, "차정웅"),
#     (12.02, "박중수"),
#     (11.57, "차동현"),
#     (12.04, "고미숙"),
#     (11.92, "한시우"),
#     (12.22, "이민석"),
# ]
# heapq.heapify(data)  # data를 힙으로 만든다.
# for i in range(3):
#     print(heapq.heappop(data))  # 최소값부터 힙 반환
# heapify 함수를 사용하여 data 리스트를 힙으로 만들었다. 이 때 data 리스트가 힙 자료형으로 변환된다는 점에 유의하자.
# nsmallest 함수를 사용하면 위 코드를 다음과 같이 더욱 간략화 할수 있다.
# import heapq
# data = [
#     (12.23, "강보람"),
#     (12.31, "김지원"),
#     (11.98, "박시우"),
#     (11.99, "장준혁"),
#     (11.67, "차정웅"),
#     (12.02, "박중수"),
#     (11.57, "차동현"),
#     (12.04, "고미숙"),
#     (11.92, "한시우"),
#     (12.22, "이민석"),
# ]
# print(heapq.nsmallest(3, data))
# heapq.nsmallest(n, iterable) 는 iterable 데이터 집합에서 n 개의 가장 작은 요소로 구성된 리스트를 반환한다.
# 만약 꼴찌부터 순위를 매긴다면 heapq.nlargest(3, data) 를 사용할 수 있다.
''' import heapq
data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]
print(heapq.nsmallest(3, data))
print(heapq.nlargest(3, data)) '''

# [03-09 예쁘게 출력하기 - pprint]
# pprint는 데이터를 예쁘게 출력할 수 있게 해주는 파이썬 표준 라이브러리이다.
# pprint는 네트워크 프로그램에서 복잡한 구조를 지닌 json 데이터를 출력하는 용도로 많이 사용된다.

# [03-10 이진 탐색 - bisect]
# bisect는 이진 탐색 알고리즘을 구현한 파이썬 표준 라이브러리이다. bisect.bisect 함수는 정렬된 리스트에 값을 삽입할 때 정렬을 유지할 수 있는 인덱스를 리턴한다.
# 문제
# A 학급의 학생수는 총 7명이다. 7명의 성적은 다음과 같다.
# [33, 99, 77, 70, 89, 90, 100]
# 그리고 성적에 대한 학점은 다음과 같은 기준으로 정해진다.
# 90점 이상 : A
# 80점 이상 : B
# 70점 이상 : C
# 60점 이상 : D
# 0~59점 : F
# A학급 학생들의 학점을 순서대로 구하시오.
# 풀이
# bisect.bisect 함수를 사용하면 이 문제를 쉽게 풀수 있다.
# import bisect
# result = []
# for score in [33, 99, 77, 70, 89, 90, 100]:
#     pos = bisect.bisect([60, 70, 80, 90], score)  # 점수가 정렬되어 삽입될 수 있는 포지션을 반환
#     grade = 'FDCBA'[pos]
#     result.append(grade)
# print(result)
# 출력결과는 다음과 같다.
# ['F', 'A', 'C', 'C', 'B', 'A', 'A']
# bisect.bisect([60, 70, 80, 90], score) 에서 bisect함수는 [60, 70, 80, 90] 에서 score가 정렬되어 삽입될 수 있는 인덱스를 리턴한다.
# 예를 들어 85점이라면 80과 90 사이인 3을 리턴한다.
# 70점과 90점과 같이 학점을 구분하는 점수와 동일한 경우 bisect 함수는 좌측이 아닌 우측으로 삽입되는 인덱스를 반환한다.
# 그런데 만약 학점의 기준이 다음과 같이 변경된다면 어떻게 해야 할까?
# 90점 초과 : A
# 80점 초과 : B
# 70점 초과 : C
# 60점 초과 : D
# 0~60점 : F
# 학점의 기준이 위와 같이 변경된다면 80점인 경우 B가 아닌 C가 되어야 한다. 이런 경우에는 다음처럼 bisect함수 대신 bisect_left 함수를 사용해야 한다.
# import bisect
# result = []
# for score in [33, 99, 77, 70, 89, 90, 100]:
#     pos = bisect.bisect_left([60, 70, 80, 90], score)
#     grade = 'FDCBA'[pos]
#     result.append(grade)
# print(result)
# 출력 결과는 다음과 같다.
# ['F', 'A', 'C', 'D', 'B', 'B', 'A']
# 성적이 70점인 경우 D학점, 90점인 경우 B학점으로 나왔다.
# bisect대신 bisect_left를 사용하면 점수가 학점을 구분하는 리스트([60, 70, 80, 90])의 요소 값과 동일할 경우(예:70점, 90점) 삽입되는 위치가 우측이
# 아닌 좌측이 된다. 즉, 점수가 70점인 경우 삽입 위치가 2가 아닌 1이 된다.
# bisect 함수는 bisect_right 함수와 동일하다. 즉, bisect 대신 bisect_right 함수를 사용해도 된다.
# bisect.insort
# bisect.insort 는 정렬될 수 있는 위치에 해당 항목을 삽입한다.
# >>> import bisect
# >>> a = [60, 70, 80, 90]
# >>> bisect.insort(a, 85)
# >>> a
# [60, 70, 80, 85, 90]
''' import bisect
result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect([60, 70, 80, 90], score)  # 점수가 정렬되어 삽입될 수 있는 포지션을 반환
    grade = 'FDCBA'[pos]
    result.append(grade)
print(result)
import bisect
result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect_left([60, 70, 80, 90], score)
    grade = 'FDCBA'[pos]
    result.append(grade)
print(result)
import bisect
a = [60, 70, 80, 90]
bisect.insort(a, 85)
print(a) '''

# [03-11 상수 집합 - enum]
# enum은 서로 관련이 있는 여러 개의 상수의 집합을 정의할 때 사용되는 파이썬 표준 라이브러리이다.
# enum 라이브러리는 파이썬 3.4 버전부터 사용이 가능하다.
# 문제
# 다음과 같이 날짜를 입력하면 그 날짜의 요일에 해당되는 메뉴를 리턴하는 get_menu 함수가 있다.
# from datetime import date
# def get_menu(input_date):
#     weekday = input_date.isoweekday()  # 1:월요일, 2:화요일, ... , 7: 일요일
#     if weekday == 1:
#         menu = "김치찌개"
#     elif weekday == 2:
#         menu = "비빔밥"
#     elif weekday == 3:
#         menu = "된장찌개"
#     elif weekday == 4:
#         menu = "불고기"
#     elif weekday == 5:
#         menu = "갈비탕"
#     elif weekday == 6:
#         menu = "라면"
#     elif weekday == 7:
#         menu = "건빵"
#     return menu
# print(get_menu(date(2020, 12, 6)))
# print(get_menu(date(2020, 12, 18)))
# 위 프로그램의 출력결과는 다음과 같다. (2020년 12월 6일은 일요일이므로 "건빵"을 출력하고 2020년 12월 18일은 금요일이므로 "갈비탕"을 출력한다. )
# 건빵
# 갈비탕
# 하지만 이 프로그램은 요일을 나타내는 숫자 1~7이라는 매직넘버를 사용하고 있다. 프로그램에서 사용된 매직넘버는 코드를 이해하기 어렵게 하고 가독성을 떨어뜨리기 때문에 좋은 방법이 아니다.
# 위 프로그램의 매직넘버를 제거하여 보다 우아한 코드로 바꾸어 보시오.
# 풀이
# 위 코드는 enum 라이브러리를 사용하여 다음과 같이 변경할 수 있다.
# from datetime import date
# from enum import IntEnum
# class Week(IntEnum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7
# def get_menu(input_date):
#     weekday = input_date.isoweekday()
#     if weekday == Week.MONDAY:
#         menu = "김치찌개"
#     elif weekday == Week.TUESDAY:
#         menu = "비빔밥"
#     elif weekday == Week.WEDNESDAY:
#         menu = "된장찌개"
#     elif weekday == Week.THURSDAY:
#         menu = "불고기"
#     elif weekday == Week.FRIDAY:
#         menu = "갈비탕"
#     elif weekday == Week.SATURDAY:
#         menu = "라면"
#     elif weekday == Week.SUNDAY:
#         menu = "건빵"
#     return menu
# print(get_menu(date(2020, 12, 6)))
# print(get_menu(date(2020, 12, 18)))
# Week클래스는 enum.IntEnum 을 상속하여 만든 Enum형 자료형이다. 이렇게 상수를 숫자값으로 직접 사용하지 않고 Enum형 자료형을 만들어 사용하면 유지보수에 유리하며 가독성도 좋아진다.
# enum.IntEnum은 enum.Enum을 상속하여 만든 클래스이다.
# enum.Enum을 상속하여 만든 Enum형 자료형은 다음처럼 name과 value 속성으로 접근할 수 있다.
# print(Week.MONDAY.name)
# print(Week.MONDAY.value)
# 출력결과는 다음과 같다.
# MONDAY
# 1
# 그리고 다음처럼 for문에서 사용할 수도 있다.
# for week in Week:
#     print("{}:{}".format(week.name, week.value))
# 출력결과는 다음과 같다.
# MONDAY:1
# TUESDAY:2
# WEDNESDAY:3
# THURSDAY:4
# FRIDAY:5
# SATURDAY:6
# SUNDAY:7
''' from datetime import date
from enum import IntEnum
class Week(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
def get_menu(input_date):
    weekday = input_date.isoweekday()
    if weekday == Week.MONDAY:
        menu = "김치찌개"
    elif weekday == Week.TUESDAY:
        menu = "비빔밥"
    elif weekday == Week.WEDNESDAY:
        menu = "된장찌개"
    elif weekday == Week.THURSDAY:
        menu = "불고기"
    elif weekday == Week.FRIDAY:
        menu = "갈비탕"
    elif weekday == Week.SATURDAY:
        menu = "라면"
    elif weekday == Week.SUNDAY:
        menu = "건빵"
    return menu
print(get_menu(date(2020, 12, 6)))
print(get_menu(date(2020, 12, 18))) '''

# [03-12 위상정렬 - graphlib.TopologicalSorter]
# graphlib의 TopologicalSorter는 위상정렬을 위한 파이썬 표준 라이브러리이다.
# 파이썬 3.9 버전이상부터 사용가능
# 위상정렬이란?
# 위상 정렬(topological sorting)은 유향 그래프의 꼭짓점들(vertex)을 변의 방향을 거스르지 않도록 나열하는 것을 의미한다.
# 위상정렬을 가장 잘 설명해 줄 수 있는 예로 대학의 선수과목(prerequisite) 구조를 예로 들 수 있다. 만약 특정 수강과목에 선수과목이 있다면 
# 그 선수 과목부터 수강해야 하므로, 특정 과목들을 수강해야 할 때 위상 정렬을 통해 올바른 수강 순서를 찾아낼 수 있다. 이와 같이 선후 관계가 
# 정의된 그래프 구조 상에서 선후 관계에 따라 정렬하기 위해 위상 정렬을 이용할 수 있다. 정렬의 순서는 유향 그래프의 구조에 따라 여러 개의 종류가 나올 수 있다.
# 위상 정렬이 성립하기 위해서는 반드시 그래프의 순환이 존재하지 않아야 한다. 즉, 그래프가 비순환 유향 그래프(directed acyclic graph)여야 한다.
# [출처: 위키백과]
# 문제
# A씨는 다음 5개의 영어 수업을 모두 수강할 예정이다.
# 영어초급, 영어중급, 영어고급, 영어문법, 영어회화
# 그런데 각각의 수업은 선수과목이 있어서 순서를 지켜서 수업을 들어야 한다고 한다. 선수과목의 규칙은 다음과 같다.
# 규칙1: 영어초급 --> 영어중급 --> 영어고급
# 규칙2: 영어중급 --> 영어문법 --> 영어고급
# 규칙3: 영어문법 --> 영어회화
# 즉, 영어고급을 들으려면 영어중급과 영어문법을 모두 들어야 하고 영어중급을 듣기 위해서는 영어초급을 먼저 들어야 한다.
# A씨가 5개의 수업을 어떤 순서로 수강해야 하는지 구하시오.
# 풀이
# 위 영어 수업의 선수과목을 나타낸 그림은 다음과 같다.
# 규칙1: 주황색 화살표
# 규칙2: 초록색 화살표
# 규칙3: 파란색 화살표
# 파이썬 graphlib의 TopologicalSorter를 사용하면 이 문제를 쉽게 풀수 있다.
# from graphlib import TopologicalSorter
# ts = TopologicalSorter()
# # 규칙1
# ts.add('영어중급', '영어초급')  # 영어중급의 선수과목은 영어초급
# ts.add('영어고급', '영어중급')  # 영어고급의 선수과목은 영어중급
# # 규칙2
# ts.add('영어문법', '영어중급')  # 영어문법의 선수과목은 영어중급
# ts.add('영어고급', '영어문법')  # 영어고급의 선수과목은 영어문법
# # 규칙3
# ts.add('영어회화', '영어문법')  # 영어회화의 선수과목은 영어문법
# print(list(ts.static_order()))  # 위상정렬한 결과를 출력
# 출력결과는 다음과 같다. A 씨는 다음 순서대로 수업을 수강하면 된다.
# ['영어초급', '영어중급', '영어문법', '영어고급', '영어회화']
# add(노드, *선행노드) 메서드는 어떤 노드의 선행노드를 추가할 때 사용하는 함수이다. 선행노드는 1개 이상도 가능하다.
# 위의 예에서 보면 "영어고급" 노드의 선행노드는 "영어중급", "영어문법" 2개이므로 다음과 같이 사용해도 된다.
# ts.add('영어고급', '영어중급', '영어문법')  # 영어고급의 선수과목은 영어중급과 영어문법
# 위상 정렬은 한가지 주의해야 할 점이 있다. 만약 규칙3이 "영어문법-->영어회화" 가 아니라 "영어문법-->영어회화-->영어중급" 순으로 변경된다면
# 다음과 같은 모습이 되어 [영어중급, 영어문법, 영어회화] 구간이 순환하게 된다.
# 이런 경우 다음과 같은 CycleError 오류가 발생하게 된다.
# graphlib.CycleError: ('nodes are in a cycle', ['영어중급', '영어문법', '영어회화', '영어중급'])
''' from graphlib import TopologicalSorter
ts = TopologicalSorter()
# 규칙1
ts.add('영어중급', '영어초급')  # 영어중급의 선수과목은 영어초급
ts.add('영어고급', '영어중급')  # 영어고급의 선수과목은 영어중급
# 규칙2
ts.add('영어문법', '영어중급')  # 영어문법의 선수과목은 영어중급
ts.add('영어고급', '영어문법')  # 영어고급의 선수과목은 영어문법
# 규칙3
ts.add('영어회화', '영어문법')  # 영어회화의 선수과목은 영어문법
print(list(ts.static_order()))  # 위상정렬한 결과를 출력 '''

# [03-13 가짜 데이터 생성기 - faker]
# faker는 가짜 데이터를 생성하는데 사용되는 파이썬 라이브러리이다.
# 설치
# pip install Faker
# 문제
# 다음과 같은 형식의 테스트 데이터 30건이 필요하다. 수동으로 테스트 데이터를 작성하지 말고 좀 더 멋진 방법으로 테스트 데이터를 만드시오.
# [(이름1, 주소1), (이름2, 주소2), ..., (이름30, 주소30)]
# 풀이
# 테스트 데이터는 Faker를 사용하면 아주 쉽게 만들 수 있다.
# 이름은 다음처럼 만들수 있다.
# >>> from faker import Faker
# >>> fake = Faker()
# >>> fake.name()
# 'Matthew Estrada'
# 만약 한글 이름을 만드려면 다음과 같이 한국을 의미하는 ko-KR을 전달하여 fake객체를 생성하면 된다.
# >>> fake = Faker('ko-KR')
# >>> fake.name()
# '김하은'
# 주소는 다음과 같이 만들 수 있다.
# >>> fake.address()
# '충청북도 수원시 잠실6길 (경자주이읍)'
# 따라서 이름과 주소를 쌍으로 갖는 30건의 테스트 데이터는 다음과 같이 만들면 된다.
# >>> test_data = [(fake.name(), fake.address()) for i in range(30)]
# 결과는 다음과 같다.
# >>> test_data
# Faker는 위에서 알아본 name, address 이외에 다른 항목들도 제공해 준다. 대표적인 것 몇 가지만 알아보자.
# 항목	설명
# fake.name()	이름
# fake.address()	주소
# fake.postcode()	우편번호
# fake.country()	국가명
# fake.company()	회사명
# fake.job()	직업명
# fake.phone_number()	휴대전화번호
# fake.email()	이메일주소
# fake.user_name()	사용자명
# fake.pyint(min_value=0, max_value=100)	0부터 100 사이의 임의의 숫자
# fake.ipv4_private()	IP 주소
# fake.text()	임의의 문장
# fake.color_name()	색상명
# 제공해 주는 항목이 무척 많으므로 자세한 내용은 참고 URL을 살펴보도록 하자.
''' from faker import Faker
fake = Faker('ko-KR')
test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data) '''


# [04장 숫자와 수학모듈]
# 이 장에서는 숫자와 수학에 관련된 라이브러리에 대해서 알아본다.

# [04-01 최대공약수 - math.gcd]
# math.gcd 는 최대공약수를 구하는 파이썬 표준 라이브러리이다. (gcd: greatest common divisor - 최대공약수)
# math.gcd는 파이썬 3.5 버전부터 사용이 가능하다.
# 최대공약수란?
# 공약수(common divisor)란 두 수 이상의 여러 수의 공통된 약수를 의미한다. 예를 들어 30과 15는 공통적으로 1, 3, 5, 15라는 약수를 가지고 있는데
# 이를 공약수라고 한다. 또 이런 공약수중에 가장 큰 공약수를 최대 공약수라고 한다.
# 문제
# 사탕 60개와 초콜릿 100개 그리고 젤리 80개를 각각 나누어 똑같이 봉지에 나누어 담으려고 한다. 최대한으로 만들수 있는 봉지의 개수를 구하시오. 
# (단, 사탕, 초콜릿, 젤리가 남으면 안된다.)
# 풀이
# 이 문제는 60, 100, 80의 최대 공약수를 구하면 바로 해결된다.
# >>> import math
# >>> math.gcd(60, 100, 80)
# 20
# math.gcd 함수를 사용하여 최대공약수 20을 구했다. 따라서 최대한 만들수 있는 봉지수는 20개이고 각 봉지당 사탕은 3개, 초콜릿은 5개, 젤리는 4개를 담으면 된다.
''' import math
print(math.gcd(60, 100, 80)) '''

# [04-02 최소공배수 - math.lcm]
# math.lcm 은 최소공배수를 구하는 파이썬 표준 라이브러리이다. (lcm: least common multiple - 최소공배수)
# math.lcm은 파이썬 3.9 버전부터 사용이 가능하다.
# 최소공배수란?
# 두 수의 최소공배수는 두 수에 서로 공통으로 존재하는 배수 중 가장 작은 수를 뜻한다. 예를들어 3과 5의 최소공배수는 15가 된다.
# 문제
# 어느 버스 정류장에 시내버스는 15분마다 도착하고 마을버스는 25분마다 도착한다고 한다. 그럼 오후 1시에 두 버스가 동시에 도착하였다고 했을 때, 
# 다음에 두 버스가 동시에 도착할 시간을 구하시오.
# 풀이
# 이 문제는 15와 25의 최소공배수를 구하면 바로 해결된다.
# >>> import math
# >>> math.lcm(15, 25)
# 75
# math.lcm 함수를 사용하여 최소공배수 75를 구했다. 따라서 다음 두 버스가 동시에 도착할 시간은 75분 후인 오후 2시 15분이다.
''' import math
print(math.lcm(15, 25)) '''

# [04-03 정확한 소숫점 연산 - decimal.Decimal]
# decimal.Decimal은 숫자를 10진수로 처리하여 정확한 소수점 자릿수를 표현하게 해 주는 파이썬 표준 라이브러리이다.
# 문제
# 다음은 파이썬의 이상한 연산 결과이다.
# >>> 0.1 * 3 == 0.3
# False
# >>> 1.2 - 0.1 == 1.1
# False
# >>> 0.1 * 0.1 == 0.01
# False
# 이렇게 되는 이유는 이진수 기반의 파이썬 float 연산은 경우에 따라 미세한 오차가 발생할 수 있기 때문이다.
# >>> 0.1 * 3
# 0.30000000000000004
# >>> 1.2 - 0.1
# 1.0999999999999999
# >>> 0.1 * 0.1
# 0.010000000000000002
# >>>
# 어떻게 하면 이런 연산 오류를 방지할 수 있을까?
# 풀이
# == 연산자 대신 math.isclose를 사용하는 방법이 있다.
# >>> import math
# >>> math.isclose(0.1*3, 0.3)
# True
# >>> math.isclose(1.2-0.1, 1.1)
# True
# >>> math.isclose(0.1*0.1, 0.01)
# True
# 하지만 math.isclose는 완전한 해결이 될 수 없다.
# 십진수 연산을 사용하는 decimal.Decimal을 사용하면 이 문제를 완벽하게 해결할 수 있다.
# >>> from decimal import Decimal
# >>> Decimal('0.1') * 3
# Decimal('0.3')
# >>> Decimal('1.2') - Decimal('0.1')
# Decimal('1.1')
# >>> Decimal('0.1') * Decimal('0.1')
# Decimal('0.01')
# Decimal을 사용시 주의해야 할 점
# 다음처럼 Decimal의 입력으로 문자열 대신 float를 입력하면 float연산에서 발생한 문제점이 그대로 나타나게 된다.
# >>> Decimal(1.1)
# Decimal('1.100000000000000088817841970012523233890533447265625')
# 그리고 Decimal 객체에는 다음처럼 정수 연산은 가능하지만 실수연산은 불가능하다.
# >>> Decimal('1.1') * 3
# Decimal('3.3')
# >>> Decimal('1.1') * 3.0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for *: 'decimal.Decimal' and 'float'
# Decimal은 어떤 경우에 사용하는 것이 유리할까?
# Decimal은 정확성을 향상시키기 위해 고정소수점을 사용하여 메모리를 많이 사용하기 때문에 모든 float연산을 Decimal로 바꾸는 것은 좋은 방법이 아니다.
# Decimal은 보통 한치의 오차도 허용하지 않는 금융권 또는 재무/회계 관련 프로그램을 작성할 때 사용하는 것이 유리하다.
''' from decimal import Decimal
print(Decimal('0.1') * 3)
print(Decimal('1.2') - Decimal('0.1'))
print(Decimal('0.1') * Decimal('0.1')) '''

# [04-04 유리수 - fractions]
# fractions는 유리수 산술을 지원하는 파이썬 표준 라이브러리이다.
# 유리수(rational number)는 두 정수의 비율 또는 분수의 형식으로 나타낼 수 있는 수이다.
# 문제
# 유리수 1/5 와 2/5를 더하면 3/5이다. 하지만 파이썬은 다음과 같은 계산결과를 보여준다.
# >>> 1/5 + 2/5
# 0.6000000000000001
# 1/5+2/5=3/5의 결과가 나올 수 있도록 파이썬에서 유리수 연산을 하시오.
# 풀이
# 파이썬에서 유리수 연산을 정확하게 하기 위해서는 fractions.Fraction을 사용하면 된다.
# >>> from fractions import Fraction
# 유리수는 다음처럼 Fraction(분자, 분모) 형태로 만들 수 있다.
# >>> a = Fraction(1, 5)
# >>> a
# Fraction(1, 5)
# 또는 Fraction('1/5') 처럼 문자열로 만들 수도 있다.
# 분자는 다음처럼 numerator로 알 수 있다.
# >>> a.numerator
# 1
# 분모는 다음처럼 denominator로 알 수 있다.
# >>> a.denominator
# 5
# 따라서 1/5+2/5=3/5 연산은 다음처럼 할 수 있다.
# >>> result = Fraction(1, 5)+Fraction(2, 5)
# >>> result
# Fraction(3, 5)
# 결과값은 다음처럼 실수로 바꿀 수 있다.
# >>> float(result)
# 0.6
''' from fractions import Fraction
result = Fraction(1, 5)+Fraction(2, 5)
print(result)
print(float(result)) '''

# [04-05 난수생성 - random]
# random은 난수를 생성하기 위한 모듈이다.
# 문제
# 6개의 숫자로 이루어진 로또 번호를 무작위로 생성해 주는 프로그램을 작성하시오.
# 로또는 1부터 45까지의 숫자 중 6개를 맞히면 1등에 당첨되는 복권이다. 단, 6개의 숫자는 중복될 수 없다.
# 풀이
# 무작위 숫자를 생성하려면 파이썬 random 모듈을 사용하면 된다.
# import random
# result = []
# while len(result) < 6:
#     num = random.randint(1, 45)  # 1~45 사이의 숫자중 임의의 숫자 생성
#     result.append(num)
# print(result)  # 무작위 생성된 6개의 숫자 출력
# random.randint(1, 45)는 1~45 사이의 숫자중 한 개를 무작위로 생성하는 함수이다.
# 리스트의 요소를 무작위로 섞고 싶을 때는 다음처럼 random.shuffle을 사용한다.
# >>> a = [1,2,3,4,5]
# >>> random.shuffle(a)
# >>> a
# [5, 3, 2, 4, 1] 
# 리스트의 요소중 무작위로 하나를 선택하려면 random.choice를 사용한다.
# >>> a = [1,2,3,4,5]
# >>> random.choice(a)
# 2
''' import random
num = random.randint(1, 45)
result=[]
for i in range(6):
    num = random.randint(1, 45)
    if num in result:
        num = random.randint(1, 45)
    result.append(num)
print(result) '''

# [04-06 평균값과 중앙값 - statistics]
# statistics는 평균값과 중앙값을 구할 수 있는 모듈이다.
# 중앙값이란 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미한다.
# 예를 들어 1, 2, 100의 세 값이 있을 때, 2가 가장 중앙에 있기 때문에 2가 중앙값이다. 값이 짝수개일 때에는 중앙값이 유일하지 않고 두 개가 될 수도 있다.
# 이 경우 그 두 값의 평균을 취한다. 예를 들어 1, 10, 90, 200 네 수의 중앙값은 10과 90의 평균인 50이 된다.
# 문제
# 다음은 A학급의 학생 10명의 수학 점수이다.
# marks = [78, 93, 99, 95, 51, 71, 52, 43, 81, 78]
# A학급의 수학 점수 평균과 중앙값을 구하시오.
# 풀이
# 평균값은 statistics.mean 함수를 사용하여 쉽게 구할 수 있다.
# >>> import statistics
# >>> marks = [78, 93, 99, 95, 51, 71, 52, 43, 81, 78]
# >>> statistics.mean(marks)
# 74.1
# 중앙값은 statistics.median 함수를 사용하여 구할 수 있다.
# >>> statistics.median(marks)
# 78.0
''' import statistics
marks = [78, 93, 99, 95, 51, 71, 52, 43, 81, 78]
print(statistics.mean(marks)) '''

# [04-07 기호 계산 - sympy]
# sympy는 기호(symbol) 계산을 위한 파이썬 라이브러리이다. sympy를 사용하면 방정식 풀이를 쉽게 할 수 있다.
# 설치
# pip install sympy
# 문제
# 시윤이는 가지고 있던 돈의 2/5로 학용품을 샀다. 학용품을 사는 데 쓴 돈이 1760원이라면 남은 돈은 얼마일까?
# 풀이
# 이 문제는 연습장과 연필만 있으면 쉽게 구할 수 있는 1차 방정식 문제이다. 하지만 파이썬으로도 방정식 풀이를 할 수 있다. 다음처럼 sympy를 사용해 보자.
# from fractions import Fraction
# import sympy
# # 가지고 있던 돈을 x라고 하자.
# x = sympy.symbols("x")
# # 가지고 있던 돈의 2/5가 1760원이므로 방정식은 x * (2/5) = 1760 이다.
# f = sympy.Eq(x*Fraction('2/5'), 1760)
# # 방정식을 만족하는 값(result)을 구한다.
# result = sympy.solve(f)  # 결괏값은 리스트
# # 남은 돈은 다음과 같이 가지고 있던 돈에서 1760원을 빼면 된다.
# remains = result[0] - 1760
# print('남은 돈은 {}원 입니다.'.format(remains))
# 출력결과는 다음과 같다.
# 남은 돈은 2640원 입니다.
# sympy.symbols는 x, y 처럼 방정식에 사용되는 기호를 생성할 때 사용한다. 만약 x, y 두개가 필요하면 다음처럼 할 수 있다.
# x, y = sympy.symbols('x y')
# sympy.Eq(a, b)는 a와 b가 같다는 방정식이다. 즉, x * (2/5) = 1760 라는 식에 대응되는 방정식은 sympy.Eq(x*Fraction('2/5'), 1760)이다. 이 때 사용한 Fraction은 유리수를 표현할 때 사용하는 파이썬 클래스로 2/5를 정확하게 계산하기 위해 사용하였다.
# Fraction은 이 책의 'fractions' 챕터를 참고하자.
# f 라는 방정식을 세웠으므로 sympy.solve(f)를 사용하여 x에 해당되는 값을 구할 수 있다. solve함수는 결괏값으로 리스트를 반환한다.
# sympy의 활용 예
# x2=1 과 같은 이차방정식의 해를 구해보자.
# >>> import sympy
# >>> f = sympy.Eq(x**2, 1)
# >>> sympy.solve(f)
# [-1, 1]
# 다음과 같은 방정식의 해를 구해보자.
# x + y = 10
# x - y = 4
# >>> import sympy
# >>> x, y = sympy.symbols('x y')
# >>> f1 = sympy.Eq(x+y, 10)
# >>> f2 = sympy.Eq(x-y, 4)
# >>> sympy.solve([f1, f2])  # 변수가 2개 이상인 경우 결괏값이 리스트가 아닌 딕셔너리임에 주의
# {x: 7, y: 3}
''' from fractions import Fraction
import sympy
# 가지고 있던 돈을 x라고 하자.
x = sympy.symbols("x")
# 가지고 있던 돈의 2/5가 1760원이므로 방정식은 x * (2/5) = 1760 이다.
f = sympy.Eq(x*Fraction('2/5'), 1760)
# 방정식을 만족하는 값(result)을 구한다.
result = sympy.solve(f)  # 결괏값은 리스트
# 남은 돈은 다음과 같이 가지고 있던 돈에서 1760원을 빼면 된다.
remains = result[0] - 1760
print('남은 돈은 {}원 입니다.'.format(remains))
import sympy
f = sympy.Eq(x**2, 1)
print(sympy.solve(f))
import sympy
x, y = sympy.symbols('x y')
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
print(sympy.solve([f1, f2]))  # 변수가 2개 이상인 경우 결괏값이 리스트가 아닌 딕셔너리임에 주의 '''


# [05장 함수형 프로그래명 모듈]
# 이 장에서는 함수형 프로그래밍을 지원하는 라이브러리들에 대해서 알아본다.

# [05-01 무한 반복자 - itertools.cycle]
# itertools.cycle(iterable)은 iterable을 순서대로 무한히 반복시키는 이터레이터를 리턴한다.
# 문제
# 여러분은 콜센터 프로그램을 만들고 있다. 전화가 올때마다 다음 3명의 상담원이 순서대로 전화연결이 될 수 있는 프로그램을 만들어야 한다.
# ['김은경', '이명자', '이성진']
# 요청할때마다 순서대로 상담원을 리턴하는 프로그램을 작성하시오.
# 풀이
# 다음처럼 itertools.cycle 로 무한히 반복되는 이터레이터를 만들고 next를 호출하여 값을 요청하면 된다.
# >>> emp_pool = itertools.cycle(['김은경', '이명자', '이성진'])
# >>> next(emp_pool)
# '김은경'
# >>> next(emp_pool)
# '이명자'
# >>> next(emp_pool)
# '이성진'
# >>> next(emp_pool)
# '김은경'
# >>> next(emp_pool)
# '이명자'
# ...
# next함수는 파이썬 빌트인 함수로 이터레이터의 다음 요소를 리턴하는 함수이다.
''' import itertools
emp_pool = itertools.cycle(['김은경', '이명자', '이성진'])
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool)) '''

# [05-02 누적합 계산 - itertools.accumulate]
# itertools.accumulate(iterable)은 iterable의 누적합을 계산하여 이터레이터로 리턴하는 함수이다.
# 문제
# 다음은 A회사의 1월부터 12월까지의 수입이다.
# [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
# 1월에는 1161만원, 2월에는 1814만원, ..., 12월에는 2134만원의 수입이 발생하였다. A회사의 사장님은 1년간 수입의 월별 누적치를 
# 알고 싶어한다. 즉, 1월에는 1161만원 2월에는 1161+1814=2975만원, 3월에는 2975+1270=4245만원, ... 식으로 월별 누적 합계금액을
# 알고 싶어한다.
# A회사의 월별 누적합계를 구해주는 프로그램을 작성하시오.
# 풀이
# 누적치를 알고 싶을 때는 itertools의 accumulate함수를 사용하는 것이 가장 편리하다. 다음은 itertools.accumulate함수를 사용하여 
# 1월부터 12월까지의 월별 누적합계를 구하는 프로그램이다.
# import itertools
# monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
# result = list(itertools.accumulate(monthly_income))
# print(result)
# 출력 결과는 다음과 같다.
# [1161, 2975, 4245, 6501, 7914, 9756, 11977, 14184, 16634, 19457, 21997, 24131]
# 만약 1월에서 12월 기간 동안 월 수입의 최댓값을 누적하여 보여주고 싶다면 다음처럼 itertools.accumulate 함수의 두번째 인수로
# max함수를 전달하여 구할 수 있다.
# import itertools
# monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
# result = list(itertools.accumulate(monthly_income, max))
# print(result)
# 출력결과는 다음과 같다.
# [1161, 1814, 1814, 2256, 2256, 2256, 2256, 2256, 2450, 2823, 2823, 2823]
# 3월까지는 월 최고 수입이 1814만원이었고 8월까지는 월 최고 수입이 2256만원임을 알수 있다.
''' import itertools
monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income))
print(result)
import itertools
monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income, max))
print(result) '''

# [05-03 키값으로 분류 - itertools.groupby]
# itertools.groupby(iterable, key=None) 은 iterable을 key값으로 분류한 결과를 리턴하는 함수이다.
# 문제
# 다음은 8명의 혈액형 데이터이다.
# data = [
#     {'name': '이민서', 'blood': 'O'},
#     {'name': '이영순', 'blood': 'B'},
#     {'name': '이상호', 'blood': 'AB'},
#     {'name': '김지민', 'blood': 'B'},
#     {'name': '최상현', 'blood': 'AB'},
#     {'name': '김지아', 'blood': 'A'},
#     {'name': '손우진', 'blood': 'A'},
#     {'name': '박은주', 'blood': 'A'}
# ]
# 위 혈액형 데이터를 다음처럼 혈액형별로 분류된 데이터로 바꾸시오.
# data = {
#     'A': [{'name': '김지아', 'blood': 'A'}, {'name': '손우진', 'blood': 'A'}, {'name': '박은주', 'blood': 'A'}], 
#     'AB': [{'name': '이상호', 'blood': 'AB'}, {'name': '최상현', 'blood': 'AB'}], 
#     'B': [{'name': '이영순', 'blood': 'B'}, {'name': '김지민', 'blood': 'B'}], 
#     'O': [{'name': '이민서', 'blood': 'O'}]
# }
# 풀이
# itertools.groupby를 사용하면 분류기준으로 묶어 데이터를 분류할 수 있다. 단, groupby전에 분류기준으로 먼저 소트를 진행해야 한다.
# import itertools
# import operator
# data = [
#     {'name': '이민서', 'blood': 'O'},
#     {'name': '이영순', 'blood': 'B'},
#     {'name': '이상호', 'blood': 'AB'},
#     {'name': '김지민', 'blood': 'B'},
#     {'name': '최상현', 'blood': 'AB'},
#     {'name': '김지아', 'blood': 'A'},
#     {'name': '손우진', 'blood': 'A'},
#     {'name': '박은주', 'blood': 'A'}
# ]
# data = sorted(data, key=operator.itemgetter('blood'))
# grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))
# result = {}
# for key, group_data in grouped_data:
#     result[key] = list(group_data)
# print(result)
# 출력결과는 다음과 같다.
# {'A': [{'name': '김지아', 'blood': 'A'}, {'name': '손우진', 'blood': 'A'}, {'name': '박은주', 'blood': 'A'}], 'AB': [{'name': '이상호', 'blood': 'AB'}, {'name': '최상현', 'blood': 'AB'}], 'B': [{'name': '이영순', 'blood': 'B'}, {'name': '김지민', 'blood': 'B'}], 'O': [{'name': '이민서', 'blood': 'O'}]}
# 데이터의 'blood' 항목으로 소트하고 분류하기 위해 operator.itemgetter('blood')를 사용하였다.
# 만약 위 문제를 소트없이 groupby만 진행할 경우 분류기준이 바뀔때마다 그룹이 생성되므로 원하는 결과를 얻을 수 없다.
# import itertools
# import operator
# data = [
#     {'name': '이민서', 'blood': 'O'},
#     {'name': '이영순', 'blood': 'B'},
#     {'name': '이상호', 'blood': 'AB'},
#     {'name': '김지민', 'blood': 'B'},
#     {'name': '최상현', 'blood': 'AB'},
#     {'name': '김지아', 'blood': 'A'},
#     {'name': '손우진', 'blood': 'A'},
#     {'name': '박은주', 'blood': 'A'}
# ]
# grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))
# result = {}
# for key, group_data in grouped_data:
#     print(key, list(group_data))
# 출력결과는 다음과 같다.
# O [{'name': '이민서', 'blood': 'O'}]
# B [{'name': '이영순', 'blood': 'B'}]
# AB [{'name': '이상호', 'blood': 'AB'}]
# B [{'name': '김지민', 'blood': 'B'}]
# AB [{'name': '최상현', 'blood': 'AB'}]
# A [{'name': '김지아', 'blood': 'A'}, {'name': '손우진', 'blood': 'A'}, {'name': '박은주', 'blood': 'A'}]
''' import itertools
import operator
data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이영순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'}
]
data = sorted(data, key=operator.itemgetter('blood'))
grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))
result = {}
for key, group_data in grouped_data:
    result[key] = list(group_data)
print(result)
import itertools
import operator
data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이영순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'}
]
grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))
result = {}
for key, group_data in grouped_data:
    print(key, list(group_data)) '''

# [05-04 사이즈가 큰 것을 기준으로 묶기 - itertools.zip_longest]
# itertools.zip_longest(*iterables, fillvalue=None) 는 파이썬 빌트인 함수인 zip과 동일하게 동작하지만 전달된 이터러블들의 길이가 
# 같지 않을 경우 긴 이터러블을 기준으로 누락된 값은 fillvalue로 채워진다.
# 문제
# 다음과 같은 파이썬 코드가 있다.
# students = ['한민서', '황지민', '이영철', '이광수', '김승민']
# rewards = ['사탕', '초컬릿', '젤리']
# result = zip(students, rewards)
# print(list(result))
# 이 파이썬 코드를 실행하면 다음과 같은 결과가 나온다.
# [('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리')]
# students와 rewards의 갯수가 일치하지 않기 때문에 갯수가 더 적은 rewards의 갯수 만큼만 zip으로 묶이게 된다. 
# 하지만 students의 갯수가 rewards의 갯수보다도 많더라도 다음처럼 부족한 rewards는 '새우깡'으로 함께 묶일수
# 있도록 해주는 코드를 작성하시오.
# [('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]
# 풀이
# itertools.zip_longest 를 사용하면 갯수가 긴 것을 기준으로 묶을 수 있다. 이 때 부족한 항목은 None으로 채워지는데 다음처럼
# fillvalue에 값을 전달하면 None대신 다른 값을 지정할 수 있다.
# import itertools
# students = ['한민서', '황지민', '이영철', '이광수', '김승민']
# rewards = ['사탕', '초컬릿', '젤리']
# result = itertools.zip_longest(students, rewards, fillvalue='새우깡')
# print(list(result))
# 출력결과는 다음과 같다.
# [('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]
''' import itertools
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
rewards = ['사탕', '초컬릿', '젤리']
result = itertools.zip_longest(students, rewards, fillvalue='새우깡')
print(list(result)) '''

# [05-05 순열 - itertools.permutations]
# itertools.permutations(iterable, r=None) 는 iterable 요소의 길이 r에 해당하는 순열을 리턴한다.
# 문제
# 1, 2, 3의 숫자가 적힌 카드가 있을 때, 이 중 두 장의 카드를 꺼내어 만들수 있는 2자리 숫자를 모두 구하시오.
# 풀이
# [1, 2, 3] 이라는 3장의 카드 중 2장을 뽑는 경우의 수는 총 3가지이다. (조합)
# 1, 2
# 2, 3
# 1, 3
# 하지만 이 문제는 위 3가지에 순서를 더해 다음처럼 6가지가 된다. (순열)
# 1, 2
# 2, 1
# 2, 3
# 3, 2
# 1, 3
# 3, 1
# 이 같은 순열은 itertools.permutations를 사용하여 간단히 구할 수 있다.
# >>> import itertools
# >>> list(itertools.permutations([1,2,3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
# 3장의 숫자 카드중 2개를 고르는 경우의 수는 다음처럼 itertools.combinations를 사용하면 된다.
# >>> import itertools
# >>> list(itertools.combinations([1,2,3], 2))
# [(1, 2), (1, 3), (2, 3)]
''' import itertools
print(list(itertools.permutations([1,2,3], 2)))
import itertools
print(list(itertools.combinations([1,2,3], 2))) '''

# [05-06 조합 - itertools.combinations]
# itertools.combinations(iterable, r)은 iterable중에서 r개를 선택할 수 있는 조합을 이터레이터로 리턴하는 함수이다.
# 문제
# 로또 번호 1~45 중 숫자 6개를 구하는 경우의 수를 모두 구하고 그 갯수를 출력하시오.
# 풀이
# itertools.combinations를 사용하면 45개의 숫자 줏 6개를 선택하는 경우의 수를 다음과 같이 구할 수 있다.
# >>> import itertools
# >>> it = itertools.combinations(range(1, 46), 6)
# itertools.combinations(range(1, 46), 6) 는 1~45의 숫자 중에서 6개를 뽑아내는 경우의 수를 이터레이터로 리턴한다.
# 반환된 이터레이터를 루프를 돌면서 출력하면 아마 끝도 없이 출력될 것이다. (궁금하다면 실행해 봐도 좋다.)
# >>> for num in it:
# ...     print(num)
# ...
# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 7)
# (1, 2, 3, 4, 5, 8)
# (1, 2, 3, 4, 5, 9)
# (1, 2, 3, 4, 5, 10)
# (1, 2, 3, 4, 5, 11)
# (1, 2, 3, 4, 5, 12)
# (1, 2, 3, 4, 5, 13)
# ...
# 하지만 이터레이터를 순환하여 출력하지 않고 갯수만 세려면 다음과 같이 하면 된다.
# >>> len(list(itertools.combinations(range(1, 46), 6)))
# 8145060
# 선택할 수 있는 로또 번호의 갯수는 8145060이다.
# 만약 로또 복권이 숫자의 중복을 허용하도록 규칙이 변경된다면 경우의 수는 몇개가 될까?
# 중복이 허용된다 함은 당첨 번호가 [1,2,3,4,5,5] 처럼 5가 2번 이상 나와도 되고 [1,1,1,1,1,1] 처럼 1이 6번 중복되도 된다는 의미이다.
# 중복을 허용하는 중복조합은 itertools.combinations_with_replacement를 사용하면 된다.
# >>> len(list(itertools.combinations_with_replacement(range(1, 46), 6)))
# 15890700
# 무시무시한 경우의 수가 나오는 것을 확인할 수 있다.
''' import itertools
it = itertools.combinations(range(1, 46), 6)
print(len(list(itertools.combinations(range(1, 46), 6)))) '''

# [05-07 함수로 정렬 - functools.cmp_to_key]
# functools.cmp_to_key(func) 는 sorted와 같은 정렬 함수의 key에 함수(func)를 전달할때 사용한다. 단, func는 두 개의 인수를 받아들이고, 
# 첫번째 인수를 기준으로 그들을 비교하여, 작으면 음수, 같으면 0, 크면 양수를 반환하는 비교 함수이어야 한다.
# 문제
# 2차원 평면 위의 점 N개가 다음과 같이 (x, y) 좌표의 리스트로 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 
# 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
# 즉, 정렬후에는 다음과 같은 결과가 나와야 한다.
# [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]
# 풀이
# 이 문제는 sorted함수의 key에 특별한 소트를 할 수 있는 함수를 전달하여 해결할 수 있다. key에 함수를 전달하기 위해서는 다음처럼 
# functools.cmp_to_key를 사용해야 한다.
# import functools
# def xy_compare(n1, n2):
#     if n1[1] > n2[1]:         # y 좌표가 크면
#         return 1
#     elif n1[1] == n2[1]:      # y 좌표가 같으면
#         if n1[0] > n2[0]:     # x 좌표가 크면
#             return 1
#         elif n1[0] == n2[0]:  # x 좌표가 같으면
#             return 0
#         else:                 # x 좌표가 작으면
#             return -1
#     else:                     # y 좌표가 작으면
#         return -1
# src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
# result = sorted(src, key=functools.cmp_to_key(xy_compare))
# print(result)
# 출력결과는 다음과 같다.
# [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]
# y좌표로 정렬되고 y좌표가 같은 경우 x좌표로 정렬되었다.
# xy_compare와 같이 정렬을 하기 위한 함수는 반드시 다음 3가지 중 하나를 리턴해야 한다. (단, 첫번째 인수를 기준으로 비교한다.)
# 크다 (양수 리턴)
# 작다 (음수 리턴)
# 같다 (0 리턴)
''' import functools
def xy_compare(n1, n2):
    if n1[1] > n2[1]:         # y 좌표가 크면
        return 1
    elif n1[1] == n2[1]:      # y 좌표가 같으면
        if n1[0] > n2[0]:     # x 좌표가 크면
            return 1
        elif n1[0] == n2[0]:  # x 좌표가 같으면
            return 0
        else:                 # x 좌표가 작으면
            return -1
    else:                     # y 좌표가 작으면
        return -1
src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key=functools.cmp_to_key(xy_compare))
print(result) '''

# [05-08 함수의 결과를 캐시 - functools.lru_cache]
# @functools.lru_cache(maxsize=128)는 함수의 리턴결과를 캐시해 주는 데코레이터이다. 최초 요청 이후에는 캐시된 결과를 리턴한다.
# maxsize는 캐시할 수 있는 최대 갯수를 의미하며 최대 갯수를 초과할 경우에는 호출빈도가 가장 작은것부터 캐시에서 사라진다.
# LRU는 'Least Recently Used'의 약자로 가장 최근에 참조되지 않은 데이터가 교체시점에 먼저 나가는 방식이다.
# 문제
# 다음은 위키독스의 특정 페이지의 리소스를 가져오는 프로그램이다. 이 프로그램의 성능 향상을 위해 동일한 페이지를 다시 요청할 
# 경우에는 캐시를 사용하도록 수정하시오.
# import urllib.request
# def get_wikidocs(page):
#     print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
#     resource = 'https://wikidocs.net/{}'.format(page)
#     try:
#         with urllib.request.urlopen(resource) as s:
#             return s.read()
#     except urllib.error.HTTPError:
#         return 'Not Found'
# 풀이
# 다음처럼 functools의 lru_cache를 데코레이터로 사용하면 쉽게 캐시함수를 만들 수 있다.
# import urllib.request
# from functools import lru_cache
# @lru_cache(maxsize=32)
# def get_wikidocs(page):
#     print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
#     resource = 'https://wikidocs.net/{}'.format(page)
#     try:
#         with urllib.request.urlopen(resource) as s:
#             return s.read()
#     except urllib.error.HTTPError:
#         return 'Not Found'
# first_6 = get_wikidocs(6)
# first_7 = get_wikidocs(7)
# second_6 = get_wikidocs(6)
# second_7 = get_wikidocs(7)
# assert first_6 == second_6  # 처음 요청한 6번 페이지의 내용과 두번째 요청한 6번 페이지의 내용이 같은지를 확인
# assert first_7 == second_7
# 출력결과는 다음과 같다.
# wikidocs page:6
# wikidocs page:7
# 처음 요청한 6페이지와 7페이지는 웹 요청이 발생하여 로그가 출력되었지만 이후 재 요청시에는 함수가 호출되는 대신 캐시에 
# 저장된 데이터가 리턴되는 것을 확인할 수 있다.
''' import urllib.request
from functools import lru_cache
@lru_cache(maxsize=32)
def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'
first_6 = get_wikidocs(6)
first_7 = get_wikidocs(7)
second_6 = get_wikidocs(6)
second_7 = get_wikidocs(7)
assert first_6 == second_6  # 처음 요청한 6번 페이지의 내용과 두번째 요청한 6번 페이지의 내용이 같은지를 확인
assert first_7 == second_7 '''

# [05-09 인수를 지정하여 함수 재정의 - functools.partial]
# functools.partial 은 하나 이상의 인수가 이미 채워진 함수의 새 버전을 만들기 위해 사용하는 도구이다.
# 문제
# 다음은 입력 인수의 합과 곱을 선택적으로 리턴하는 파이썬 함수 add_mul이다.
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
# add_mul('add', 1, 2, 3, 4, 5)를 호출하면 1~5의 합인 15를 리턴하고 add_mul('sum', 1, 2, 3 ,4 ,5)를 호출하면 1~5의 곱인 120을 
# 리턴한다.
# add_mul 함수를 활용하여 다음과 같이 동작하는 add, mul 함수를 작성하시오.
# add(1, 2, 3, 4, 5)  # 15 리턴
# mul(1, 2, 3, 4, 5)  # 120 리턴
# 풀이
# 이 문제의 가장 일반적인 풀이는 다음과 같다.
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
# def add(*args):
#     return add_mul('add', *args)
# def mul(*args):
#     return add_mul('mul', *args)    
# print(add(1,2,3,4,5))  # 15 출력
# print(mul(1,2,3,4,5))  # 120 출력
# 하지만 functools.partial을 사용하면 다음처럼 보다 우아한 코드를 작성할 수 있다.
# from functools import partial
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
# add = partial(add_mul, 'add')
# mul = partial(add_mul, 'mul')
# print(add(1,2,3,4,5))  # 15 출력
# print(mul(1,2,3,4,5))  # 120 출력
# partial은 이처럼 하나 이상의 인수가 이미 채워진 함수의 새 버전을 만드는데 유용하게 사용된다.
# 만약 add 함수는 항상 100을 기준으로 시작되어야 한다고 가정한다면 다음처럼 간단하게 정의할 수 있다.
# add = partial(add_mul, 'add', 100)
# 이와 같이 add 함수를 지정하고 add(1)을 호출하면 101이 리턴될 것이다.
# 마찬가지로 mul 함수도 다음과 같이 기준값을 1000으로 지정할 수 있다.
# add = partial(add_mul, 'mul', 1000)
# 이와 같이 mul 함수를 지정하고 mul(2, 3)을 호출하면 6000이 리턴될 것이다.
# 그리고 partial로 만든 함수는 다음과 같이 func와 args 속성을 갖는다.
# print(add.func)
# print(add.args)
# 출력 결과는 다음과 같다.
# <function add_mul at 0x7f3a483893a0>
# ('add', 100)
''' from functools import partial
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')
print(add(1,2,3,4,5))  # 15 출력
print(mul(1,2,3,4,5))  # 120 출력 '''

# [05-10 함수 적용하여 단일값으로 줄여나가기 - functools.reduce]
# functools.reduce(function, iterable)는 function을 iterable의 요소에 차례로(왼쪽에서 오른쪽으로) 누적적으로 적용하여 
# iterable을 단일 값으로 줄여나가는 함수이다.
# 문제
# 다음은 입력인수 data의 요소를 모두 더하여 리턴하는 add 함수이다.
# def add(data):
#     result = 0
#     for i in data:
#         result += i
#     return result
# data = [1, 2, 3, 4, 5]
# result = add(data)
# print(result)  # 15 출력
# functools.reduce를 사용하여 동일한 기능을 하는 코드를 작성하시오.
# 풀이
# functools.reduce 를 사용한 코드는 다음과 같다.
# import functools
# data = [1, 2, 3, 4, 5]
# result = functools.reduce(lambda x, y: x + y, data)
# print(result)  # 15 출력
# functools.reduce를 사용하면 reduce에 선언된 lambda 함수를 data의 요소들에 차례대로 누적 적용하여 다음과 같이 계산된다. 
# 따라서 add 함수와 동일한 역할을 하게 된다.
# ((((1+2)+3)+4)+5)
# functools.reduce로 최댓값 구하기
# num_list = [3, 2, 8, 1, 6, 7]
# max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
# print(max_num)  # 8 출력
# [3, 2, 8, 1, 6, 7]의 요소에 차례로 reduce의 함수에 전달되어 작은 값이 제거되어 최종적으로 남은 최댓값이 리턴되게 된다.
# 최소값은 functools.reduce(lambda x, y: x if x < y else y, num_list) 로 구할 수 있다.
''' import functools
data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)  # 15 출력 '''

# [05-11 래퍼함수의 속성 유지 - functools.wraps]
# functools.wraps(wrapped)는 래퍼 함수를 정의할 때 함수의 이름이나 설명문 같은 속성들을 유지할 수 있게 만들어 주는 편의 
# 함수이다.
# 문제
# 다음은 함수의 수행시간을 알려주는 elapsed 데코레이터를 사용하는 예제이다.
# import time
# def elapsed(original_func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         original_func(*args, **kwargs)
#         end = time.time()
#         print("함수 수행시간: %f 초" % (end - start))
#     return wrapper
# @elapsed
# def add(a, b):
#     """ 두 수 a, b를 더한값을 리턴하는 함수 """
#     return a + b
# result = add(3, 4)
# 위 예제처럼 add 함수에 elpased 데코레이터를 적용하여 실행하면 다음과 같이 add 함수의 수행시간이 출력된다.
# 함수 수행시간: 0.000002 초
# 하지만 다음처럼 add 함수를 출력해 보면
# print(add)
# 다음처럼 add 함수의 이름이 출력되지 않고 elapsed에 대한 정보만이 출력된다.
# <function elapsed.<locals>.wrapper at 0x7f65dc058af0>
# 마찬가지로 함수의 독스트링(함수의 설명문)을 출력하는 help명령을 실행해 보면
# help(add)
# 함수의 설명문인 '두 수 a, b를 더한값을 리턴하는 함수' 라는 설명문이 출력되지 않는다.
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)
# elapsed 데코레이터를 사용하더라도 함수명과 함수의 설명문을 유지할 수 있도록 코드를 수정하시오.
# 풀이
# 데코레이터를 사용하더라도 함수명과 함수의 설명문을 유지하기 위해서는 functools.wraps를 사용하면 된다.
# import functools
# import time
# def elapsed(original_func):
#     @functools.wraps(original_func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         original_func(*args, **kwargs)
#         end = time.time()
#         print("함수 수행시간: %f 초" % (end - start))
#     return wrapper
# @elapsed
# def add(a, b):
#     """ 두 수 a, b를 더한값을 리턴하는 함수 """
#     return a + b
# print(add)
# help(add)
# 실행결과는 다음과 같다.
# <function add at 0x7f44f004caf0>
# Help on function add in module __main__:
# add(a, b)
#     두 수 a, b를 더한값을 리턴하는 함수
# 함수명과 함수의 설명문이 정확하게 출력되는 것을 확인할 수 있다.
# 실행해야 하는 original_func을 인수로 functools.wraps 데코레이터를 적용하면 내부적으로 functools.update_wrapper 가 실행되어 
# 함수명 및 함수에 대한 설명들이 유지된다. 함수에는 여러 속성들이 있는데 이런 속성들을 보호하면서 데코레이터 함수를 만들려면
# functools의 wraps함수를 반드시 사용해야 한다.
''' import functools
import time
def elapsed(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
    return wrapper
@elapsed
def add(a, b):
    """ 두 수 a, b를 더한값을 리턴하는 함수 """
    return a + b
print(add)
help(add) '''

# [05-12 다중 수준 정렬 - operator.itemgetter]
# operator.itemgetter는 주로 sorted와 같은 함수의 key파라미터에 적용되어 다중 수준의 정렬을 가능하게 해 준다.
# 문제
# 다음과 같은 students 리스트가 있다.
# students = [
#     ("jane", 22, 'A'),
#     ("dave", 32, 'B'),
#     ("sally", 17, 'B'),
# ]
# students라는 리스트는 총 3개의 튜플을 가지고 있다. 각 튜플은 순서대로 "이름", "나이", "성적"에 해당되는 데이터를 갖는다. 
# 이 리스트를 나이 순으로 소트하시오.
# 풀이
# 이 문제는 다음처럼 sorted 함수의 key 매개변수에 operator.itemgetter를 적용하여 쉽게 해결할 수 있다.
# from operator import itemgetter
# students = [
#     ("jane", 22, 'A'),
#     ("dave", 32, 'B'),
#     ("sally", 17, 'B'),
# ]
# result = sorted(students, key=itemgetter(1))
# 출력결과는 다음과 같다.
# [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]
# 나이순서대로 소트된 것을 확인할 수 있다.
# itemgetter(1)과 같이 사용하면 students의 item인 튜플의 2번째 요소로 소트를 하겠다는 의미이다.
# operator.attrgetter
# 만약 students 리스트의 요소가 튜플이 아닌 Student클래스의 객체일 경우에는 다음처럼 attrgetter를 적용하여 소트해야 한다.
# from operator import attrgetter
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
# students = [
#     Student('jane', 22, 'A'),
#     Student('dave', 32, 'B'),
#     Student('sally', 17, 'B'),
# ]
# result = sorted(students, key=attrgetter('age'))
# attrgetter('age')와 같이 사용하면 Student 객체의 객체변수 age로 소트를 하겠다는 의미이다.
''' from operator import itemgetter
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]
result = sorted(students, key=itemgetter(1))
print(result)
from operator import attrgetter
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]
result = sorted(students, key=attrgetter('age'))
print(result) '''


# [06장 파일과 디렉터리 액세스]

# [06-01 파일 시스템 경로를 객체로 다루기 - pathlib]
# pathlib는 파일 시스템 경로를 단순한 문자열 대신 객체로 만들어 여러가지 일을 할 수 있게 해주는 라이브러리이다.
# pathlib는 파이썬 3.4 버전부터 사용할 수 있다.
# 문제
# 다음은 현재 디렉터리의 모든 txt 파일을 archive라는 디렉터리로 이동시키는 전통적인 파이썬 코드이다. (단, archive 디렉터리는 
# 이미 존재한다고 가정한다.)
# import glob
# import os
# import shutil
# for file_path in glob.glob('%s/*.txt' % os.getcwd()):
#     parent = os.path.dirname(file_path)
#     filename = os.path.basename(file_path)
#     new_path = os.path.join(parent, 'archive', filename)
#     shutil.move(file_path, new_path)
# 위 코드를 glob, os, shutil 대신 pathlib 만을 사용하도록 수정하시오.
# 풀이
# 파이썬 pathlib를 사용하면 glob, os.path, shutil에서 사용했던 모든 기능을 다음처럼 pathlib만을 사용하여 구현할 수 있다.
# import pathlib
# for p in pathlib.Path.cwd().glob('*.txt'):
#     new_p = p.parent.joinpath('archive', p.name)
#     p.replace(new_p)
# pathlib.Path.cwd()는 현재 디렉터리 객체(Path)를 리턴한다. 그리고 Path객체의 glob함수로 해당 디렉터리에 있는 txt 파일 리스트를
# 얻을 수 있다. Path 객체의 parent 는 os.path.dirname처럼 해당 파일의 상위 디렉터리를 리턴한다. 마찬가지로 Path 객체의 
# joinpath는 os.path.join처럼 파일 경로와 파일명등을 합쳐서 새로운 경로를 만들어 낸다. 그리고 파일을 옮기기 위해서 Path 
# 객체의 replace 함수를 사용하였다.
# 하위 디렉터리까지 검색하고 싶은 경우에는 glob대신 rglob을 사용하면 된다.
# pathlib를 사용하지 않은 코드와 사용한 코드를 비교한 표는 다음과 같다.
# 전통적인 방식	pathlib 방식 (p는 pathlib로 생성된 Path객체를 의미한다.)
# os.getcwd	p.cwd
# glob.glob	p.glob
# os.path.dirname	p.parent
# os.path.basename	p.name
# os.path.join	p.joinpath
# shutil.move	p.replace
# 현재 디렉터리의 모든 파일을 조사하여 확장자별 건수 구하기
# >>> import collections, pathlib
# >>> collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())
# Counter({'.md': 2, '.txt': 4, '.pdf': 2, '.py': 1})
# iterdir은 해당 디렉터리의 모든 파일을 이터레이터로 리턴한다. Path객체의 suffix는 파일의 확장자명(.을 포함한 확장자명)을 
# 의미한다.

# [06-02 파일 시스템 경로 - os.path]
# os.path는 경로명(파일명)에 대한 유용한 함수를 제공하는 라이브러리이다.
# 문제
# 입력으로 받은 디렉터리의 파이썬 파일을 모두 출력하는 search(dirname) 함수를 작성하시오. (단, 하위 디렉터리의 파이썬 파일도 
# 모두 출력할것)
# 풀이
# 디렉터리 경로를 입력으로 받아 파이썬 파일을 출력하는 search함수는 다음과 같다.
# import os
# def search(dirname):
#     filenames = os.listdir(dirname)
#     for filename in filenames:
#         filepath = os.path.join(dirname, filename)
#         if os.path.isdir(filepath):
#             search(filepath)
#         elif os.path.isfile(filepath):
#             name, ext = os.path.splitext(filepath)
#             if ext == '.py': 
#                 print(filepath)
# 입력으로 받은 디렉터리의 모든 파일을 os.listdir로 얻고 그 파일들 중에서 확장자가 .py이면 파일명을 출력한다. 만약 os.listdir로 얻은 경로가 파일이 아닌 디렉터리인 경우에는 다시 그 경로를 입력으로 하여 search함수를 재귀호출한다.
# 여기서 사용된 os모듈과 os.path모듈을 정리한 표는 다음과 같다.
# 사용모듈	설명
# os.listdir(path)	path 하위의 파일(디렉터리 포함)을 리스트로 리턴한다.
# os.path.join(path, *paths)	path와 paths에 해당되는 모든 경로를 더하여 전체 경로를 리턴한다. 이때 경로를 구분하는 구분자는
# 실행 OS시스템에 맞게 변경된다. (경로 구분자의 예: 유닉스는 /, 윈도우는 \\)
# os.path.isdir(path)	path의 디렉터리여부를 리턴한다.
# os.path.isfile(path)	path의 파일여부를 리턴한다.
# os.path.splitext(path)	path를 파일명과 확장자로 구분한다. (이때 확장자에는 .이 포함된다.)
# pathlib를 사용한 풀이는 다음과 같다.
# import pathlib
# def search(dirname):
#     for p in pathlib.Path(dirname).rglob('*.py'):
#         print(p)

# [06-03 여러파일을 한꺼번에 처리하기 - fileinput]
# fileinput은 여러 파일을 한꺼번에 처리할 수 있게 해주는 라이브러리이다.
# 문제
# 현재 디렉터리에 많은 수의 txt 파일이 있다. 현재 디렉터리의 모든 txt 파일을 읽어 그 내용을 한 줄씩 출력하는 코드를 작성하시오.
# 풀이
# 여러개의 파일을 한꺼번에 처리할 경우에는 다음처럼 fileinput을 사용하는 것이 가장 편리하다.
# import fileinput
# import glob
# with fileinput.input(glob.glob("*.txt")) as f:
#     for line in f:
#         print(line)

# [06-04 디렉터리와 파일비교 - filecmp]
# filecmp는 두 파일 또는 두 디렉터리를 비교할 때 사용하는 라이브러리이다.
# 문제
# 두 디렉토리(a, b)의 차이점을 알 수 있는 다음과 같은 프로그램을 작성하시오.
# a에만 있고 b에는 없는 파일은 다음과 같이 출력
# a: 파일명
# b에만 있고 a에는 없는 파일은 다음과 같이 출력
# b: 파일명
# a와 b에 모두 존재하지만 내용이 서로 다른 경우는 다음과 같이 출력
# x: 파일명
# 풀이
# filecmp.dircmp를 사용하면 다음처럼 이 문제를 쉽게 해결할 수 있다.
# import filecmp
# fd = filecmp.dircmp('a', 'b')
# for a in fd.left_only:
#     print("a: %s" % a)
# for b in fd.right_only:
#     print("b: %s" % b)
# for x in fd.diff_files:
#     print("x: %s" % x)
# 먼저 fd = filecmp.dircmp('a', 'b') 처럼 a, b디렉터리 비교를 위한 fd객체를 생성한다. 그리고 a 디렉터리에만 있는 파일은
# left_only, b 디렉터리에만 있는 파일은 right_only, 동일하게 있지만 내용이 다른 파일은 diff_files로 구할 수 있다.

# [06-05 임시파일 - tempfile]
# tempfile은 임시파일을 만들때 사용하는 모듈이다.
# 문제
# 다음은 파일 객체를 입력으로 받아 파일의 숫자를 모두 더하여 리턴하는 sumfile 함수이다.
# def sumfile(f):
#     result = 0
#     for line in f.readlines():
#         num = int(line)
#         result += num
#     return result
# 임의로 1~100 사이의 10개의 숫자를 생성하여 파일에 기록한 후 sumfile 함수를 실행하여 그 합을 출력하는 코드를 작성하시오. 
# (단, 생성한 파일은 함수 실행후 삭제해야 한다.)
# 풀이
# 임의로 숫자를 생성할 때는 random.randint 함수를 사용하고 파일을 임시로 생성할 때는 tempfile을 사용하면 된다.
# import random
# import tempfile
# def sumfile(f):
#     result = 0
#     for line in f.readlines():
#         num = int(line)
#         result += num
#     return result
# tf = tempfile.TemporaryFile(mode='w+')
# for i in range(10):
#     num = random.randint(1, 100)
#     tf.write(str(num))
#     tf.write("\n")
# tf.seek(0)
# result = sumfile(tf)
# tf.close()
# print(result)
# tf = tempfile.TemporaryFile(mode='w+') 처럼 tempfile 모듈을 사용하면 임시파일을 쉽게 만들 수 있다. mode='w+'의 의미는 쓰기와
# 읽기를 위해 파일을 생성한다는 의미이다. 여기서는 파일에 임의로 생성된 10개의 숫자를 써야하고 또 sumfile함수에서는 파일을 
# 읽어야 하므로 mode='w+'를 사용하였다. 파일 쓰기가 끝나면 파일의 위치(offset)가 파일의 끝을 가리키므로 tf.seek(0)를 수행하여
# 파일을 다시 처음부터 읽을 수 있도록 하였다. 임시파일은 tf.close()가 수행되거나 파이썬 프로세스가 종료되면 자동으로 삭제된다.
# TemporaryFile대신 NamedTemporaryFile을 사용하면 생성되는 임시파일이 파일 시스템에서 보이는 이름을 갖게 된다. 예를 들어 
# 유닉스의 경우 위 코드의 tf.close()가 실행되기 전에 input()과 같은 사용자 입력 대기 명령줄을 추가하면 사용자 입력이 되어 
# 프로그램이 종료되기 전에 /tmp 디렉터리에 생성되는 임시파일을 눈으로 확인해 볼 수 있다. NamedTemporaryFile은 이점만 제외하면 
# TemporaryFile과 동일한 기능을 수행한다.
''' import random
import tempfile
def sumfile(f):
    result = 0
    for line in f.readlines():
        num = int(line)
        result += num
    return result
tf = tempfile.TemporaryFile(mode='w+')
for i in range(10):
    num = random.randint(1, 100)
    tf.write(str(num))
    tf.write("\n")
tf.seek(0)
result = sumfile(tf)
tf.close()
print(result) '''

# [06-06 파일 검색 - glob]
# glob은 패턴(유닉스 셸이 사용하는 규칙)을 사용하여 파일을 검색하는 모듈이다.
# 문제
# 현재 디렉터리와 하위 디렉터리의 모든 텍스트파일(*.txt)을 찾아서 출력하는 코드를 작성하시오.
# 풀이
# 다음은 glob 모듈을 사용한 풀이이다.
# import glob
# for filename in glob.glob("**/*.txt"):
#     print(filename)
# 패턴으로 사용된 **/*.txt 는 하위 경로를 포함한 모든 텍스트파일을 의미한다. 만약 현재 디렉터리의 텍스트 파일만을 
# 검색하려면 *.txt를 사용하면 된다.
# **/*.txt 와 같은 재귀적 패턴은 파이썬 3.5버전부터 가능

# [06-07 파일 매치- fnmatch]
# fnmatch는 파일 중에서 특정 패턴(유닉스 셸 스타일)과 일치하는 파일을 찾는데 사용하는 모듈이다.
# 문제
# 현재 디렉터리의 모든 파일중에서 다음과 같은 규칙을 가진 파일명을 모두 출력하시오.
# 파일명은 a로 시작한다.
# 확장자는 파이썬 파일을 의미하는 .py 이다.
# 확장자를 제외한 파일명의 길이는 5이다.
# 파일명의 마지막 5번째 문자는 숫자이다.
# 풀이
# 다음은 fnmatch를 사용한 풀이이다.
# import fnmatch
# import os
# for file in os.listdir('.'):
#     if fnmatch.fnmatch(file, 'a???[0-9].py'):
#         print(file)
# fnmatch에 사용할 수 있는 패턴에는 다음과 같은 것들이 있다.
# 패턴	의미
# *	모든 것과 일치
# ?	모든 단일 문자와 일치
# [seq]	seq의 모든 문자와 일치
# [!seq]	seq에 없는 모든 문자와 일치

# [06-08 파일에서 임의의 줄 가져오기 - linecache]
# linecache 모듈은 파일에서 임의의 줄을 가져올때 사용한다.
# 문제
# 다음은 속담 100개가 있는 saying.txt 파일이다.
# saying.txt
# 가는 날이 장날이다
# 가는 말이 고와야 오는 말이 곱다
# 가랑비에 옷 젖는 줄 모른다
# 가랑잎이 솔잎더러 바스락거린다고 한다
# 가재는 게 편이라
# 가지 많은 나무에 바람 잘 날 없다
# 간에 가 붙고 쓸개에 가 붙는다
# 간에 기별도 안 간다
# 간이 콩알만해지다
# 갈수록 태산
# 값싼 것이 비지떡
# 같은 값이면 다홍치마
# 개구리 올챙이 적 생각을 못한다
# 개밥에 도토리
# 개천에서 용 난다
# 고기는 씹어야 맛이요, 말은 해야 맛이라
# 고래 싸움에 새우 등 터진다
# 고양이 목에 방울 달기
# 공든 탑이 무너지랴
# 구더기 무서워 장 못 담글까
# 구슬이 서 말이라도 꿰어야 보배라
# 귀에 걸면 귀걸이, 코에 걸면 코걸이
# 그림의 떡
# 금강산도 식후경
# 뛰는 놈 위에 나는 놈 있다
# 까마귀 날자 배 떨어진다
# 꿩 대신 닭
# 꿩 먹고 알 먹기
# 남의 잔치에 감 놓아라 배 놓아라 한다
# 낫 놓고 기역자도 모른다
# 낮말은 새가 듣고 밤말은 쥐가 듣는다
# 내 코가 석 자
# 누워서 침 뱉기
# 늦게 배운 도둑이 날 새는 줄 모른다
# 다 된 죽에 코 풀기
# 달면 삼키고 쓰면 뱉는다
# 닭 잡아 먹고 오리발 내민다
# 도둑이 제 발 저리다
# 돌다리도 두들겨 보고 건너라
# 되로 주고 말로 받는다
# 등잔 밑이 어둡다
# 땅 짚고 헤엄치기
# 똥 묻은 개가 겨 묻은 개 나무란다
# 마른 하늘에 날벼락
# 말 한마디에 천 냥 빚도 갚는다
# 목구멍이 포도청
# 못된 송아지 엉덩이에 뿔 난다
# 믿는 도끼에 발등 찍힌다
# 밑 빠진 독에 물 붓기
# 바늘 도둑이 소 도둑 된다
# 배보다 배꼽이 더 크다
# 백지장도 맞들면 낫다
# 벼룩의 간 빼먹기
# 병 주고 약 준다
# 보기 좋은 떡이 먹기도 좋다
# 빛 좋은 개살구
# 사공이 많으면 배가 산으로 올라간다
# 새발의 피
# 서당 개 삼 년에 풍월을 읊는다
# 세 살 버릇 여든까지 간다
# 소문난 잔치에 먹을 것 없다
# 소 잃고 외양간 고친다
# 쇠뿔도 단김에 빼랬다
# 수박 겉 핥기
# 식은 죽 먹기
# 십 년이면 강산도 변한다
# 아는 길도 물어 가라
# 아니 땐 굴뚝에 연기 나랴
# 아닌 밤중에 홍두깨
# 약방에 감초
# 어물전 망신은 꼴뚜기가 시킨다
# 열 길 물 속은 알아도 한 길 사람 속은 모른다
# 열 번 찍어 아니 넘어가는 나무 없다
# 오뉴월 감기는 개도 아니 앓는다
# 오르지 못할 나무는 쳐다보지도 말아라
# 옥의 티
# 우물에 가서 숭늉 찾는다
# 울며 겨자 먹기
# 원수는 외나무 다리에서 만난다
# 원숭이도 나무에서 떨어진다
# 윗물이 맑아야 아랫물도 맑다
# 자라 보고 놀란 가슴 솥뚜껑 보고 놀란다
# 자랄 나무는 떡잎부터 알아본다
# 작은 고추가 더 맵다
# 종로에서 뺨 맞고 한강 가서 눈 흘긴다
# 좋은 약은 입에 쓰다
# 쥐구멍에도 볕 들 날이 있다
# 지렁이도 밟으면 꿈틀한다
# 천 리 길도 한 걸음부터
# 칼로 물 베기
# 콩 심은 데 콩 나고 팥 심은 데 팥 난다
# 티끌 모아 태산
# 핑계 없는 무덤 없다
# 하늘의 별 따기
# 하늘이 무너져도 솟아날 구멍이 있다
# 하룻강아지 범 무서운 줄 모른다
# 한 귀로 듣고 한 귀로 흘린다
# 한 술 밥에 배 부르랴
# 함흥차사라
# 호랑이도 제 말 하면 온다
# 이 파일의 속담 중 한개를 임의로 선택해서 출력하는 코드를 작성하시오.
# 풀이
# 다음은 linecache를 사용한 풀이이다.
# import linecache
# import random
# no = random.randint(1, 100)
# print(linecache.getline('saying.txt', no))
# linecache.getline(filename, lineno)는 파일의 특정라인을 가져올때 사용한다. 이때 메모리 캐시가 사용되므로 linecache.getline을 
# 여러번 호출을 할 경우 캐시에 저장된 값을 리턴하므로 매우 빠르다.
''' import linecache
import random
no = random.randint(1, 100)
print(linecache.getline('saying.txt', no)) '''

# [06-09 파일 카피 - shutil]
# shutil은 파일을 카피(Copy)하거나 이동(Move)할때 사용하는 모듈이다.
# 문제
# c:/doit/a.txt 파일을 c:/temp/a.txt.bak 이라는 파일로 카피하는 코드를 작성하시오.
# 풀이
# 다음은 shutil을 사용한 풀이이다.
# import shutil
# shutil.copy("c:/doit/a.txt", "c:/temp/a.txt.bak")
# c:/doit/a.txt 파일을 c:/temp/a.txt로 이동(Move)하는 코드는 다음과 같다.
# import shutil
# shutil.move("c:/doit/a.txt", "c:/temp/a.txt")


# [07장 데이터 지속성]

# [07-01 객체 저장하고 불러오기 - pickle]
# pickle모듈을 사용하면 파이썬에서 사용하는 자료형(예: 딕셔너리)을 변환없이 그대로 파일에 저장하고 불러올 수 있다.
# 문제
# 다음처럼 '번호', '제목', '내용'에 해당되는 3개의 인수를 받아 파일에 저장하는 함수 add_data를 만드시오.
# add_data(no, subject, content)  # no:번호, subject:제목, content:내용
# 그리고 다음처럼 번호로 데이터를 조회할 수 있는 함수 get_data를 만드시오.
# data = get_data(no)
# print(data['no'])  # 번호 출력
# print(data['subject'])  # 제목 출력
# print(data['content'])  # 내용 출력
# 단, 한번 저장된 데이터는 영구적으로 사용할 수 있어야 하고 중복된 번호는 저장할 수 없다.
# 풀이
# 단순한 텍스트를 저장하는 것이 아니라 이렇게 규칙이 있는 데이터를 파일에 저장할 경우에는 데이터의 형식을 유지할 수 있도록 
# 저장해야 한다. 파이썬에서 데이터의 형식을 유지하면서 저장하는 가장 쉬운 방법은 pickle 모듈을 사용하는 것이다. 다음은 
# pickle을 사용한 풀이이다.
# import pickle
# def get_all_data():
#     try:
#         with open("data.p", 'rb') as f: 
#             return pickle.load(f)
#     except FileNotFoundError:
#         return {}
# def add_data(no, subject, content):
#     data = get_all_data()
#     assert no not in data
#     data[no] = {'no': no, 'subject': subject, 'content': content}
#     with open('data.p', 'wb') as f:
#         pickle.dump(data, f)
# def get_data(no):
#     data = get_all_data()
#     return data[no]
# # 데이터저장
# add_data(1, '안녕 피클', '피클은 매우 간단합니다.')
# # 데이터조회
# data = get_data(1)
# print(data['no'])
# print(data['subject'])
# print(data['content'])
# 출력결과는 다음과 같다.
# 1
# 안녕 피클
# 피클은 매우 간단합니다.
# add_data 함수에서 데이터를 저장하기 전에 이미 저장되어 있던 데이터를 먼저 읽어야 하므로 get_all_data 함수가 필요하다. 
# get_all_data 함수는 pickle로 저장된 파일을 읽는 역할을 한다. 만약 아직 파일이 없다면 사용할 데이터 형식인 빈 딕셔너리를 
# 리턴한다.
# pickle로 저장된 파일을 읽기 위해서 pickle.load를 사용하였다. pickle은 바이너리 데이터이므로 파일을 'rb' 모드로 읽어야 한다.
# add_data함수는 번호(no)가 기존 데이터에 있는지를 assert로 체크하여 중복을 방지한다. 중복이 아니라면 get_all_data로 얻은 
# 딕셔너리에 1건을 추가하여 data.p라는 파일에 저장한다.
# 딕셔너리를 파일에 저장하기 위해서 pickle.dump를 사용하였다. pickle은 바이너리 데이터이므로 파일을 'wb' 모드로 써야 한다.
# get_data함수는 전체 데이터를 읽은 후 해당 번호에 해당되는 딕셔너리 1건만 리턴한다.
''' import pickle
def get_all_data():
    try:
        with open("data.p", 'rb') as f: 
            return pickle.load(f)
    except FileNotFoundError:
        return {}
def add_data(no, subject, content):
    data = get_all_data()
    assert no not in data
    data[no] = {'no': no, 'subject': subject, 'content': content}
    with open('data.p', 'wb') as f:
        pickle.dump(data, f)
def get_data(no):
    data = get_all_data()
    return data[no]
# 데이터저장
add_data(1, '안녕 피클', '피클은 매우 간단합니다.')
# 데이터조회
data = get_data(1)
print(data['no'])
print(data['subject'])
print(data['content']) '''

# [07-02 안전하게 pickle 사용하기 - copyreg]
# copyreg 모듈은 특정 객체를 pickle로 로드할 때 객체를 생성하는 함수를 실행할 수 있게 해준다.
# [먼저 공부해야 할 모듈]
# pickle
# 문제
# 다음은 pickle을 이용하여 Student 객체를 파일에 저장하는 예제이다.
# import pickle
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# a = Student('임철희', 27)
# with open('student.p', 'wb') as f:
#     pickle.dump(a, f)
# 이렇게 저장한 데이터는 다음처럼 pickle.load로 불러와 사용할 수 있다.
# with open('student.p', 'rb') as f:
#     student = pickle.load(f)
# print(student.name)  # '임철희' 출력
# 하지만 이렇게 한번 저장한 Student객체의 클래스가 다음처럼 변경된다고 가정해 보자.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.dummy = 'dummy'
# __init__ 메서드에 dummy 속성이 신규로 추가되었다. 이렇게 Student 클래스가 변경되면 dummy 속성이 추가된 이후에 저장된 
# Student 객체는 상관이 없지만 dummy속성이 추가되기 이전에 저장된 데이터에는 dummy 속성이 없어 다음과 같은 오류를 발생시킨다.
# with open('student.p', 'rb') as f:
#     student = pickle.load(f)  # dummy 속성이 생성되기 전에 저장된 pickle데이터를 읽으면
# print(student.dummy)  # dummy 속성을 찾을 수 없다는 오류가 발생한다.
# pickle 사용시 이런 오류는 매우 조심해야 한다. 이러한 오류를 방지하고 안전하게 pickle을 사용할 수 있도록 코드를 수정하시오.
# 풀이
# copyreg 모듈을 사용하면 pickle 로드시에 객체 생성자를 재호출하여 이러한 오류를 방지할 수 있다.
# import pickle
# import copyreg
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.dummy = 'dummy'
# def pickle_student(student):
#     kwargs = student.__dict__
#     return unpickle_student, (kwargs, )
# def unpickle_student(kwargs):
#     return Student(**kwargs)
# copyreg.pickle(Student, pickle_student)
# pickle_student와 unpickle_student라는 함수를 생성하고 copyreg.pickle을 사용하여 Student 클래스의 객체가 pickle로 처리될 때 
# 이 함수들을 호출하도록 등록해 주었다. copyreg 모듈을 사용하여 이렇게 pickle_student 함수를 등록해 놓으면 pickle.load 호출시
# unpickle_student함수가 호출된다. 그리고 unpickle_student 함수는 Student 객체 생성시 사용한 입력인수 kwargs를 사용하여 다시
# Student 객체를 생성하여 리턴한다.
# 이제 dummy속성 없이 저장했던 객체라도 unpickle_student함수에 의해 생성자가 다시 호출되어 리턴되므로 오류가 발생하지 않는다.
# with open("student.p", 'rb') as f:
#     s = pickle.load(f)  # dummy 속성이 생성되기 전에 저장된 pickle데이터를 읽더라도
# print(s.dummy)  # 'dummy' 출력
# copyreg 모듈은 객체가 생성되는 시점에 미리 사용되어야 한다. 만약 copyreg없이 객체가 저장되었다면 이후에 copyreg로 함수를 
# 등록하더라도 객체 로드시 등록한 함수가 실행되지 않을 것이다.

# [07-03 딕셔너리를 영구적으로 저장 - shelve]
# shelve는 딕셔너리를 영구적으로 사용하기 위한 모듈이다. key에 해당되는 value를 저장할 수 있고 이때 저장되는 value에는 파이썬의
# 모든 객체를 저장할 수 있다.
# 문제
# 프로그램에서 사용되는 딕셔너리 데이터는 프로그램이 종료되면 사라진다. 딕셔너리 데이터를 파일에 저장하고 불러올 수 있는 
# 다음과 같은 형식의 save, get 함수를 작성하시오.
# def save(key, value):
#     """ key에 대응되는 value를 저장한다. """
#     pass
# def get(key):
#    """ key에 저장된 value를 리턴한다. """
#    pass
# 풀이
# 다음은 shelve 모듈을 이용한 풀이이다.
# import shelve
# def save(key, value):
#     with shelve.open('shelve.dat') as savedict:
#         savedict[key] = value
# def get(key):
#     with shelve.open('shelve.dat') as savedict:
#         return savedict[key]
# save('number', [1, 2, 3, 4, 5])
# print(get('number'))  # [1, 2, 3, ,4, 5] 출력
# shelve 모듈을 사용하여 key, value를 딕셔너리 형태로 파일에 저장하고 불러오는 함수를 작성하였다. 이제 한번 저장한 데이터는 
# 프로그램이 종료되더라도 다시 불러올수 있다.
# pickle과 shelve의 차이
# shelve는 pickle을 이용하여 작성된 모듈로 pickle의 작은 개념이라고 보면 된다. pickle은 파이썬의 모든 객체를 처리할 수 있지만
# shelve는 딕셔너리만 처리하는 모듈이다. shelve는 key, value로 이루어진 데이터만을 처리한다.
''' import shelve
def save(key, value):
    with shelve.open('shelve.dat') as savedict:
        savedict[key] = value
def get(key):
    with shelve.open('shelve.dat') as savedict:
        return savedict[key]
save('number', [1, 2, 3, 4, 5])
print(get('number'))  # [1, 2, 3, ,4, 5] 출력 '''

# [07-04 SQLite 데이터베이스 - sqlite3]
# sqlite3 모듈은 SQLite 데이터베이스를 사용하기 위한 인터페이스 모듈이다.
# 문제
# 풀이
# SQLite
# 데이터베이스 접속하기
# 테이블 생성하기
# 데이터 입력하기
# 데이터 조회하기
# 데이터 수정과 삭제
# 데이터 저장과 취소
# 데이터베이스 접속 종료
# SQLite 도구
# 블로그 데이터 모델
# 참고
# 문제
# 여러분은 블로그 사이트를 제작하려고 한다. 하지만 그 전에 블로그 데이터를 저장하는 모듈을 먼저 작성하려고 한다.
# 블로그의 데이터 형식은 다음과 같다.
# 항목	데이터 타입	설명
# id	숫자	고유번호
# subject	문자열	제목
# content	문자열	내용
# date	문자열	작성일자
# 위 블로그 데이터의 형식을 참고하여 블로그 데이터를 저장, 조회, 수정, 삭제하는 함수를 작성하시오.
# 풀이
# 이 문제는 pickle로 해결할 수도 있다. 하지만 pickle 기반의 데이터 모델은 편리하지만 몇가지 단점이 있다. 대표적인 단점으로는
# 저장한 객체의 구조가 변경되면 저장된 객체를 불러올 수 없다는 점이다. 한번 데이터 구조가 결정되면 바꿀 수 없다는 것은 치명적인
# 단점이라고 할 수 있다. 그리고 데이터가 개별적으로 저장되는 것이 아니라 한꺼번에 저장되기 때문에 효율성이 떨어진다. 만약 
# 1000건 이상의 블로그 데이터가 저장되어 있다면 1건 추가할 때마다 1000건의 기존 데이터도 항상 함께 저장해야 한다.
# 이러한 단점을 해결하려면 결국 데이터베이스를 사용해야 한다.
# SQLite
# 여기서는 데이터베이스를 이용하여 이 문제를 해결해 보자. 파이썬으로 사용할 수 있는 데이터베이스 중 가장 간단한 SQLite를 사
# 용할 것이다.
# SQLite는 "에스큐엘라이트" 또는 "시퀄라이트"라고 읽는다.
# SQLite는 주로 개발용이나 소규모 프로젝트에서 사용되는 아주아주 가벼운 파일기반의 데이터베이스이다. 개발시에는 SQLite를 
# 사용하여 빠르게 개발하고 실제 운영시스템은 좀 더 규모있는 DB를 사용하는 것이 일반적인 개발 패턴이다. (참고. 파이썬은 DB를 
# 핸들링하는 범용적인 API를 제공해 주기 때문에 이렇게 개발시와 운영시에 다른 DB를 사용하여 개발하는것이 가능하다.)
# 자, 이제 SQLite를 사용해 보자. 한가지 기쁜 사실은 파이썬 설치시 이미 SQLite도 함께 설치된다는 점이다. SQLite를 사용하기 
# 위해 추가적으로 진행해야 할 일은 없다.
# 데이터베이스 접속하기
# 먼저 다음과 같은 명령을 수행해 보자.
# >>> import sqlite3
# >>> conn = sqlite3.connect('blog.db')
# sqlite3 모듈의 connect 메서드를 이용하면 데이터베이스를 핸들링할 수 있는 conn객체(Connection object)를 얻을 수 있다. 이 때
# 입력으로 사용한 "blog.db"는 데이터를 저장할 데이터베이스 파일이 된다.
# 테이블 생성하기
# 이곳에서 DB의 기초적인 내용인 테이블, 쿼리등에 대해서 자세한 설명을 하지는 않는다. 만약 DB에 대한 기초적인 지식이 없다면
# 다음을 이해하기 어려울 수도 있다.
# 이번에는 DB 데이터를 저장하는 공간인 테이블을 생성해 보자.
# >>> c = conn.cursor()  # 커서 생성
# >>> c.execute('''CREATE TABLE blog (id integer PRIMARY KEY, subject text, content text, date text)''')
# DB 테이블을 생성하기 위해서는 위 처럼 CREATE TABLE 테이블명 (...) 과 같은 DB 질의문(쿼리문)을 실행해야 한다. 이런 쿼리문을 
# 실행하기 위해서는 커서 객체(Cursor object)가 먼저 필요하다. 커서 객체는 conn객체를 통해 생성할 수 있다.
# 쿼리문은 커서 객체의 execute 함수를 호출하여 실행한다.
# 위 쿼리문을 실행하면 다음과 같은 구조의 blog 테이블이 생성 된다.
# 컬럼명	컬럼타입	설명
# id	integer	고유번호 (PRIMARY KEY)
# subject	text	제목
# content	text	내용
# date	text	작성일자
# 컬럼타입은 데이터베이스별로 서로 다르다. 예를 들어 오라클의 문자열은 text가 아닌 varchar형식의 컬럼타입을 사용한다. 그리고 
# sqlite는 간편하게 컬럼의 길이를 따로 지정하지 않는데 대부분의 데이터베이스들은 컬럼의 길이도 함께 지정해 주어야 한다.
# blog테이블에는 위처럼 총 4개의 컬럼이 생성되었다. 컬럼타입은 컬럼에 저장되는 데이터의 성격을 의미한다. text는 문자열
# integer는 숫자형 자료가 저장될 것이다. 특별하게 id 컬럼에는 PRIMARY KEY("프라이머리 키"라고 읽는다.)라고 지정이 되었는데 
# 이 컬럼에는 동일한 값이 입력될 수 없다는 의미이다. 예를들어 id에 1이라는 값이 이미 저장되어 있다면 id가 1인 데이터를 중복으로
# 저장할 수 없다는 말이다. 만약 동일한 값을 입력하려고 시도한다면 sqlite는 다음과 같은 오류를 발생시킬 것이다.
# sqlite3.IntegrityError: UNIQUE constraint failed: blog.id
# 데이터 입력하기
# 이제 테이블을 만들었으니 테이블에 데이터를 입력 해 보자.
# >>> c.execute("INSERT INTO blog VALUES (1, '첫번째 블로그', '첫번째 블로그입니다.', '20190827')")
# 데이터 입력 역시 커서 객체의 execute 함수를 사용한다. 데이터 입력시에는 위처럼 INSERT INTO 테이블명 VALUES (...) 쿼리문을
# 이용한다. 위와 같이 입력하면 테이블에는 다음과 같이 데이터 1건이 입력된다.
# id	subject	content	date
# 1	첫번째 블로그	첫번째 블로그입니다.	20190827
# 다음과 같이 한건을 더 입력 해 보자.
# >>> c.execute("INSERT INTO blog VALUES (2, '두번째 블로그', '두번째 블로그입니다.', '20190827')")
# 위 처럼 한건을 더 입력하면 테이블에는 다음과 같이 총 2건의 데이터가 입력된다.
# id	subject	content	date
# 1	첫번째 블로그	첫번째 블로그입니다.	20190827
# 2	두번째 블로그	두번째 블로그입니다.	20190827
# 이렇게 한건 한건 데이터가 등록될 때마다 테이블에는 새로운 행(Row)이 추가된다.
# 데이터 입력시 다음과 같이 변수를 이용하여 값을 전달하여 입력할 수도 있다.
# >>> _id = 3
# >>> subject = "세번째 블로그"
# >>> content = "세번째 블로그입니다."
# >>> date = "20190827"
# >>> c.execute("INSERT INTO blog VALUES (%d, '%s', '%s', %s)" % (_id, subject, content, date))
# 하지만 위처럼 쿼리문을 구성하는 것은 보안상 매우 취약하다. 사용자로부터 입력 받은 값이 쿼리문에 그대로 들어가기 때문에 
# 악의적인 입력값으로 인해 데이터베이스에 위험한 쿼리가 실행될 수 있기 때문이다.
# 이런것을 SQL Injection 공격이라고 부른다.
# 따라서 위와 같은 쿼리보다는 아래와 같은 물음표 스타일의 쿼리문을 작성해야 한다.
# >>> _id = 4
# >>> subject = "네번째 블로그"
# >>> content = "네번째 블로그입니다."
# >>> date = "20190827"
# >>> c.execute("INSERT INTO blog VALUES (?, ?, ?, ?)",  (_id, subject, content, date))
# 입력해야 할 부분을 '%s' 대신 물음표(?)로 바꾸어 주고 %연산자로 데이터를 입력하는 대신 튜플 형태의 데이터를 두번째 파라미터로
# 넘겨야 한다.
# 또는 다음과 같은 딕셔너리를 이용한 이름 기반 스타일의 쿼리를 사용해도 된다.
# >>> c.execute("INSERT INTO blog VALUES (:id, :subject, :content, :date)", {"id": 5, "subject": "다섯번째 블로그", "content": "다섯번째 블로그입니다.", "date": "20190827"})
# 데이터 조회하기
# 이제 데이터를 입력했으니 데이터가 정상적으로 입력이 잘 되었는지 확인해 보자.
# >>> c.execute('SELECT * FROM blog')
# >>> all = c.fetchall()
# >>> print(all)
# 데이터 조회는 위처럼 SELECT ... FROM 테이블명 ... 형식의 쿼리문을 이용한다. 커서 객체의 fetchall 메서드를 호출하면 조회 
# 결과를 모두 리스트로 리턴해 준다.
# 지금까지 입력했던 데이터들이 다음처럼 출력될 것이다.
# [(1, '첫번째 블로그', '첫번째 블로그입니다.', '20190827'), (2, '두번째 블로그', '두번째 블로그입니다.', '20190827'),
#  (3, '세번째 블로그', '세번째 블로그입니다.', '20190827'), (4, '네번째 블로그', '네번째 블로그입니다.', '20190827'), 
#  (5, '다섯번째 블로그', '다섯번째 블로그입니다.', '20190827')]
# fetchall은 한번 수행하면 끝이다. 다시 한번 수행한다면 동일한 결과가 리턴되는것이 아니라 빈 리스트가 출력된다.
# fetchall 대신 fetchone 을 사용하면 모든 데이터를 가져오는 것이 아니라 한개의 Row를 가져온다.
# >>> c.execute('SELECT * FROM blog')
# >>> one = c.fetchone()
# >>> print(one)
# 한개의 Row가 다음처럼 튜플형태로 출력될 것이다.
# (1, '첫번째 블로그', '첫번째 블로그입니다.', '20190827')
# fetchone을 다시한번 수행하면 그 다음 Row가 차례로 리턴된다.
# 데이터 수정과 삭제
# 이번에는 블로그 데이터를 수정해 보자.
# 우리가 입력한 데이터 중 제목이 "첫번째 블로그"를 "최초의 블로그"라는 제목으로 변경해 보자. 데이터 변경을 위해서는 
# 다음처럼 UPDATE 테이블명 SET ... 쿼리문을 사용해야 한다.
# >>> c.execute("UPDATE blog SET subject='최초의 블로그' WHERE id=1")
# "첫번째 블로그"에 해당되는 블로그 데이터의 PK인 id값은 1이므로 WHERE구문에 id=1을 입력하여 데이터를 수정한다.
# 다음과 같이 조회하여 데이터가 변경되었는지 확인해 보자.
# >>> c.execute('SELECT * FROM blog WHERE id=1')
# >>> one = c.fetchone()
# >>> print(one)
# (1, '최초의 블로그', '첫번째 블로그입니다.', '20190827')
# 이번에는 블로그 데이터를 삭제해 보자. 마지막으로 입력한 5번째 데이터를 삭제하도록 하자. 데이터를 삭제하려면 다음과 같이
# DELETE FROM 테이블명 ... 쿼리문을 사용해야 한다.
# >>> c.execute('DELETE FROM blog WHERE id=5')
# 수정할 때와 마찬가지로 삭제하려는 데이터의 id값을 이용하여 데이터를 삭제한다. 만약 WHERE문을 생략하게 되면 테이블 내의 
# 모든 데이터가 삭제되므로 주의하도록 하자.
# 만약 실수로 지워졌다고 하더라도 너무 걱정할 필요는 없다. 데이터를 추가, 수정, 삭제하더라도 이전 상태로 되돌릴 수 있는 
# 기능이 있다. 바로 이어지는 설명에서 확인하도록 하자.
# 데이터 저장과 취소
# 지금까지 INSERT 쿼리문으로 데이터를 입력했는데 커밋(commit)을 하지 않고 파이썬 프로그램을 종료하게 되면 데이터는 사라지게 된다.
# 데이터를 완전하게 저장하기 위해서는 다음과 같이 컨넥션 객체(Connection object)의 commit 메서드를 호출해야 한다.
# commit메서드는 데이터 저장을 위한 마지막 결정사인과 같은 역할을 한다.
# >>> conn.commit()
# 만약 데이터 입력을 했는데도 불구하고 데이터가 유실되었다면 프로그램에서 commit 메서드가 정상적으로 호출되었는지 확인해 
# 봐야 한다.
# 이번에는 데이터의 입력을 취소하는 방법에 대해서 알아보자. 취소를 위해서는 다음처럼 컨넥션 객체의 rollback 메서드를
# 호출해야 한다.
# >>> conn.rollback()
# rollback 메서드가 호출되면 commit 되기전의 데이터의 변경사항들이 모두 취소된다. 이미 commit된 데이터들은 rollback을 
# 하더라도 취소되지 않는다.
# INSERT외에 DELETE, UPDATE 등으로 변경된 데이터들도 commit, rollback이 동일하게 동작한다.
# 데이터베이스 접속 종료
# 데이터베이스 접속을 종료하기 위해서는 다음의 명령을 수행한다.
# >>> conn.close()
# 단, close는 자동으로 commit을 수행하지 않기 때문에 commit 없이 close 될 경우 변경된 내용들이 모두 사라지게 된다는 점에 주
# 의해야 한다.
# SQLite 도구
# 지금까지 파이썬을 사용하여 sqlite 데이터베이스 파일을 생성하고 테이블을 만들고 쿼리를 실행하였다. 이번에는 sqlite의
# 데이터를 보다 쉽게 관리할 수 있는 도구인 "DB Browser for SQLite"에 대해서 알아보자. "DB Browser for SQLite"를 사용하면 
# GUI 환경에서 테이블 생성, 수정, 삭제, 쿼리문 수행등을 보다 편리하게 할 수 있다.
# 먼저 다음 URL에서 "DB Broswer for SQLite"를 다운로드 받도록 하자.
# https://sqlitebrowser.org/dl/
# 설치 후 실행하면 다음과 같은 GUI 도구를 만나게 된다.
# [데이터베이스 열기 -> 저장한 blog.db파일 선택] 을 하면 파이썬으로 작성한 테이블과 데이터들을 볼 수 있을 것이다. 테이블을 
# 수정하거나 데이터를 수정할 경우에는 파이썬을 사용해도 되지만 이 도구를 사용하는 것이 훨씬 편리하다.
# 이제 이 도구를 이용하여 blog 테이블을 조금 수정해 보도록 하자.
# 우리가 만든 테이블 구조에는 불편한 점이 한가지 있기 때문이다. 그것은 새로운 데이터를 추가할 때 저장된 고유번호(id)의 
# 중복 저장 방지를 위해 max값을 구한 후 더하기 1을 하여 고유번호(id)를 생성해야만 한다는 점이다. 하지만 데이터베이스를 
# 사용하는 경우에는 SQLite의 자동증가(auto increment) 기능을 사용할 수 있다. 다음처럼 자동증가 기능을 사용해 보자.
# 위 그림처럼 먼저 테이블 blog를 선택하고 [편집 -> 테이블 수정하기]를 클릭한다.
# 그리고 다음과 같이 수정하고 '확인' 버튼을 누르자.
# 테이블 생성 쿼리문을 보면 알겠지만 "id" 컬럼에 AUTOINCREMENT가 적용됨을 알 수 있다. 이렇게 자동증가가 적용되면 다음처럼 
# INSERT문에 id 값을 전달하지 않더라도 id가 자동증가되게 데이터를 입력할 수 있다.
# INSERT INTO blog (subject, content, date) VALUES ('자동증가', 'id값이 자동증가되어 입력됩니다.', '20190831')
# id를 명시적으로 쿼리문에 추가하지 않아도 id는 자동증가되면서 저장된다.
# 위 문장은 이전 INSERT 구문과 차이가 있는데 VALUES 앞에 인서트 대상이 되는 컬럼명 (subject, content, date) 를 모두 명시해 
# 준 점이다. 만약 컬럼명을 명시적으로 표기하지 않으면 테이블 컬럼 순서대로 VALUES 뒤의 값들이 차례대로 입력되게 된다. 이전에는
# 이런 방법을 사용할 수 있었지만 지금처럼 자동증가 기능 추가로 id에 해당되는 값을 입력하지 않기 때문에 위처럼 대상이 되는
# 컬럼명을 명시적으로 표기해 주어야 한다.
# INSERT 문에 대상이 되는 컬럼명은 항상 명시적으로 표기하는 것이 좋다.
# 블로그 데이터 모델
# 이제 문제에서 제시한 블로그 데이터를 저장, 조회, 수정, 삭제할 수 있는 함수들을 만들어 보자.
# 가장 먼저 블로그 목록을 조회하는 함수를 작성해 보자.
# import sqlite3
# def get_blog_list():
#     conn = sqlite3.connect('blog.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM blog")
#     result = c.fetchall()
#     conn.close()
#     return result
# 그리고 get_blog_list 함수를 수행하면 다음과 같은 결과를 보게된다.
# [(1, '최초의 블로그', '첫번째 블로그입니다.', '20190827'), (2, '두번째 블로그', '두번째 블로그입니다.', '20190827'), 
#  (3, '세번째 블로그', '세번째 블로그입니다.', '20190827'), (4, '네번째 블로그', '네번째 블로그입니다.', '20190827'),
#  (5, '자동증가', 'id값이 자동증가되어 입력됩니다.', '20190831')]
# 조회 결과로 리스트 안에 튜플이 포함된 형태의 데이터가 리턴되었다. 튜플 대신 딕셔너리를 사용할 수 있도록 다음과 같이 
# get_blog_list 함수를 변경하자.
# def get_blog_list():
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     c.execute("SELECT * FROM blog")
#     result = c.fetchall()
#     conn.close()
#     return result
# conn.row_factory = sqlite3.Row 를 사용하면 튜플대신 딕셔너리로 응답을 얻을 수 있다. 다음과 같이 확인해 보자.
# for blog in get_blog_list():
#     print(blog)
#     print(blog["subject"])
# 실제 응답되는 객체는 sqlite3.Row 객체이지만 딕셔너리처럼 사용할 수 있다.
# 이번에는 블로그를 생성하는 add_blog 함수를 작성하자.
# def add_blog(subject, content):
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     today = time.strftime('%Y%m%d')
#     c.execute("INSERT INTO blog (subject, content, date) VALUES (?, ?, ?)", 
#         (subject, content, today))
#     conn.commit()
#     conn.close()
# 위처럼 데이터의 변경이 발생하는 경우에는 변경된 사항을 저장하기 위해 conn.commit() 을 수행해야 한다.
# 이번에는 블로그를 읽는 read_blog 함수를 작성하자.
# def read_blog(_id):
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     c.execute("SELECT * FROM blog WHERE id=?", (_id,))
#     result = c.fetchone()
#     conn.close()
#     retrun result
# 이번에는 블로그를 수정하는 modify_blog 함수를 작성하자.
# def modify_blog(_id, subject, content):
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     c.execute("UPDATE blog SET subject=?, content=? WHERE id=?", 
#         (subject, content, _id))
#     conn.commit()
#     conn.close()
# 이번에는 블로그를 삭제하는 remove_blog 함수를 작성하자.
# def remove_blog(_id):
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     c.execute("DELETE FROM blog WHERE id=?", (_id,))
#     conn.commit()
#     conn.close()
# 지금까지 작성한 함수를 보면 데이터베이스를 connect하고 close하는 부분이 반복적으로 수행된다는 것을 알 수 있다. 이러한 
# 부분들은 모든 함수에서 사용되기 때문에 공통으로 사용할 수 있도록 변경하는 것이 좋다.
# 실제 수행하는 문장은 중간쯤에 위치하고 함수 시작과 끝에 공통적인 부분이 있기 때문에 이런 상황에서는 데코레이터를 
# 사용할 수 있다.
# 다음과 같은 데코레이터 함수를 작성하자.
# def with_cursor(original_func):
#     def wrapper(*args, **kwargs):
#         conn = sqlite3.connect('blog.db')
#         conn.row_factory = sqlite3.Row
#         c = conn.cursor()
#         rv = original_func(c, *args, **kwargs)
#         conn.commit()
#         conn.close()            
#         return rv
#     return wrapper
# with_cursor 데코레이터는 데이터베이스 연결을 하고 커서 객체를 원본함수에 전달하여 수행한 후 데이터베이스 리소스를 
# clear하는 역할을 수행한다.
# 최종적으로 with_cursor 데코레이터를 사용하여 만들어진 함수들은 다음과 같다.
''' import sqlite3
import time
def with_cursor(original_func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        rv = original_func(c, *args, **kwargs)
        conn.commit()
        conn.close()            
        return rv
    return wrapper
@with_cursor
def get_blog_list(c):
    c.execute("SELECT * FROM blog")
    return c.fetchall()
@with_cursor
def add_blog(c, subject, content):
    c.execute("INSERT INTO blog (subject, content, date) VALUES (?, ?, ?)", 
        (subject, content, time.strftime('%Y%m%d')))
@with_cursor
def read_blog(c, _id):
    c.execute("SELECT * FROM blog WHERE id=?", (_id,))
    return c.fetchone()
@with_cursor
def modify_blog(c, _id, subject, content):
    c.execute("UPDATE blog SET subject=?, content=? WHERE id=?", 
        (subject, content, _id))
@with_cursor
def remove_blog(c, _id):
    c.execute("DELETE FROM blog WHERE id=?", (_id,)) '''


# [08장 데이터 압축 및 보관]

# [08-01 데이터 압축하기1 - zlib]
# zlib는 데이터를 압축하거나 해제할 때 사용하는 도구이다.
# 문제
# 다음처럼 350,000 바이트의 문자열이 있다.
# data = "Life is too short, You need python." * 10000
# print(len(data))  # 350000 출력
# 이 문자열을 네트워크를 이용하여 전송해야 한다. 하지만 네트워크를 사용하여 데이터 전송시 허용가능한 트래픽 용량은 2,000 
# 바이트까지라고 한다. 문자열의 손실없이 데이터를 전송할 수 있도록 데이터를 압축하고 해제하는 프로그램을 작성하시오.
# 풀이
# zlib의 compress와 decompress를 사용하면 문자열의 압축과 해제를 할 수 있다.
# import zlib
# data = "Life is too short, You need python." * 10000
# compress_data = zlib.compress(data.encode(encoding='utf-8'))
# print(len(compress_data))  # 1077 출력
# org_data = zlib.decompress(compress_data).decode('utf-8')
# print(len(org_data))  # 350000 출력
# data는 유니코드 문자열이므로 data.encode(encoding='utf-8') 와 같이 utf-8 형식으로 인코딩한 바이트문자열을 만든후
# zlib.compress 를 사용하여 바이트 문자열을 압축하였다. 압축한 바이트 문자열의 길이를 출력해 보았더니 1077이라는 값이 
# 출력된다. 350000바이트가 1077바이트가 되었으니 압축률이 상당히 좋다.
# 압축된 바이트 문자열을 원래 문자열로 복구하기 위해 zlib.decompress(compress_data) 로 먼저 압축이 해제된 바이트 문자열을
# 얻고 다시 .decode('utf-8')로 utf-8 형식으로 인코딩된 바이트를 유니코드 문자열로 바꾸어 주었다.
# 최종적으로 org_data의 길이를 출력해 보면 원래의 문자열 길이인 350000을 출력하는 것을 확인할 수 있다.
''' import zlib
data = "Life is too short, You need python." * 10000
compress_data = zlib.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 1077 출력
org_data = zlib.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력 '''

# [08-02 압축하여 파일로 저장하기 - gzip]
# gzip은 파일을 압축하거나 해제할때 사용되는 도구이다.
# ※ gzip은 내부적으로 zlib를 사용한다.
# 문제
# 다음처럼 350,000 바이트의 문자열이 있다.
# data = "Life is too short, You need python." * 10000
# print(len(data))  # 350000 출력
# 이 문자열을 파일에 저장해야 한다. 하지만 파일을 저장할 수 있는 여유공간은 2,000 바이트라고 한다. 문자열의 손실없이 데이터를
# 저장할 수 있도록 데이터를 압축하여 파일에 저장하고 해제하여 읽을 수 있는 프로그램을 작성하시오.
# 풀이
# gzip의 open을 사용하면 쉽게 데이터를 압축하여 파일로 저장하고 또 해제하여 읽을 수 있다.
# import gzip
# data = "Life is too short, you need python." * 10000
# with gzip.open('data.txt.gz', 'wb') as f:
#     f.write(data.encode('utf-8'))
# # 저장된 파일을 확인해 보았더니 파일사이즈가 1097 바이트로 표시된다.
# with gzip.open('data.txt.gz', 'rb') as f:
#     read_data = f.read().decode('utf-8')
# assert data == read_data
# data는 유니코드 문자열이므로 data.encode('utf-8') 와 같이 utf-8 형식으로 인코딩한 바이트문자열을 저장하였다. 저장된 파일 
# data.txt.gz 파일의 길이를 확인해 보았더니 1097 바이트이다. 350000바이트가 1097바이트가 되었으니 압축률이 상당히 좋다.
# 압축된 파일은 마찬가지 방법으로 gzip.open을 사용하여 'rb' 모드로 읽으면 된다.
# 최종적으로 원래의 350000바이트의 문자열과 압축하여 저장하고 다시 읽어들인 문자열이 동일한지를 assert를 사용하여 검사해 
# 보았다. 만약 동일하지 않다면 오류가 발생할 것이다.

# [08-03 데이터 압축하기2 - bz2]
# bz2는 데이터를 압축하거나 해제할 때 사용하는 도구이다.
# ※ zlib 와 사용법이 동일하다. bz2는 스레드환경에서 안전한 특징이 있다.
# 문제
# 다음처럼 350,000 바이트의 문자열이 있다.
# data = "Life is too short, You need python." * 10000
# print(len(data))  # 350000 출력
# 이 문자열을 네트워크를 이용하여 전송해야 한다. 하지만 네트워크를 사용하여 데이터 전송시 허용가능한 트래픽 용량은
# 1,000 바이트까지라고 한다. 문자열의 손실없이 데이터를 전송할 수 있도록 데이터를 압축하고 해제하는 프로그램을 작성하시오.
# 풀이
# bz2의 compress와 decompress를 사용하면 문자열의 압축과 해제를 할 수 있다.
# import bz2
# data = "Life is too short, You need python." * 10000
# compress_data = bz2.compress(data.encode(encoding='utf-8'))
# print(len(compress_data))  # 163 출력
# org_data = bz2.decompress(compress_data).decode('utf-8')
# print(len(org_data))  # 350000 출력
# assert data == org_data
# data는 유니코드 문자열이므로 data.encode(encoding='utf-8') 와 같이 utf-8 형식으로 인코딩한 바이트문자열을 만든후
# bz2.compress 를 사용하여 바이트 문자열을 압축하였다. 압축한 바이트 문자열의 길이를 출력해 보았더니 163이라는 값이
# 출력된다. 350000바이트가 163바이트가 되었으니 압축률이 상당히 좋다.
# ※ zlib를 사용할 경우 1077바이트였다.
# 압축된 바이트 문자열을 원래 문자열로 복구하기 위해 bz2.decompress(compress_data) 로 먼저 압축이 해제된 바이트 문자열을 
# 얻고 다시 .decode('utf-8')로 utf-8 형식으로 인코딩된 바이트를 유니코드 문자열로 바꾸어 주었다.
# 최종적으로 org_data의 길이를 출력해 보면 원래의 문자열 길이인 350000을 출력하는 것을 확인할 수 있고 data를 압축하고
# 해제한 org_data가 동일함을 assert로 확인할 수 있다.
# bz2는 다음과 같이 파일 압축 해제도 지원된다.
# ※ gzip과 사용법이 동일하다.
# import bz2
# data = "Life is too short, you need python." * 10000
# with bz2.open('data.txt.bz2', 'wb') as f:
#     f.write(data.encode('utf-8'))
# with bz2.open('data.txt.bz2', 'rb') as f:
#     read_data = f.read().decode('utf-8')
# assert data == read_data
# 압축파일의 사이즈는 157바이트로 압축률도 뛰어나다.
''' import bz2
data = "Life is too short, you need python." * 10000
with bz2.open('data.txt.bz2', 'wb') as f:
    f.write(data.encode('utf-8'))
with bz2.open('data.txt.bz2', 'rb') as f:
    read_data = f.read().decode('utf-8')
assert data == read_data '''

# [08-04 데이터 압축하기3 - lzma]
# lzma는 LZMA 압축 알고리즘을 사용하여 데이터를 압축하거나 해제할 때 사용하는 도구이다.
# ※ zlib, bz2 와 사용법이 동일하다. lzma는 bz2와 달리 스레드 환경에서 안전하지 않다.
# 문제
# 다음처럼 350,000 바이트의 문자열이 있다.
# data = "Life is too short, You need python." * 10000
# print(len(data))  # 350000 출력
# 이 문자열을 네트워크를 이용하여 전송해야 한다. 하지만 네트워크를 사용하여 데이터 전송시 허용가능한 트래픽 용량은
# 1,000 바이트까지라고 한다. 문자열의 손실없이 데이터를 전송할 수 있도록 데이터를 압축하고 해제하는 프로그램을 작성하시오.
# 풀이
# lzma의 compress와 decompress를 사용하면 문자열의 압축과 해제를 할 수 있다.
# import lzma
# data = "Life is too short, You need python." * 10000
# compress_data = lzma.compress(data.encode(encoding='utf-8'))
# print(len(compress_data))  # 220 출력
# org_data = lzma.decompress(compress_data).decode('utf-8')
# print(len(org_data))  # 350000 출력
# assert data == org_data
# data는 유니코드 문자열이므로 data.encode(encoding='utf-8') 와 같이 utf-8 형식으로 인코딩한 바이트문자열을 만든후 
# lzma.compress 를 사용하여 바이트 문자열을 압축하였다. 압축한 바이트 문자열의 길이를 출력해 보았더니 220이라는 값이
# 출력된다. 350000바이트가 220바이트가 되었으니 압축률이 상당히 좋다.
# ※ zlib를 사용할 경우 1077바이트였다.
# 압축된 바이트 문자열을 원래 문자열로 복구하기 위해 lzma.decompress(compress_data) 로 먼저 압축이 해제된 바이트 문자열을 
# 얻고 다시 .decode('utf-8')로 utf-8 형식으로 인코딩된 바이트를 유니코드 문자열로 바꾸어 주었다.
# 최종적으로 org_data의 길이를 출력해 보면 원래의 문자열 길이인 350000을 출력하는 것을 확인할 수 있고 data를 압축하고 
# 해제한 org_data가 동일함을 assert로 확인할 수 있다.
# lzma는 다음과 같이 파일 압축 해제도 지원된다.
# ※ gzip과 사용법이 동일하다.
# import lzma
# data = "Life is too short, you need python." * 10000
# with lzma.open('data.txt.xz', 'wb') as f:
#     f.write(data.encode('utf-8'))
# with lzma.open('data.txt.xz', 'rb') as f:
#     read_data = f.read().decode('utf-8')
# assert data == read_data
# 압축파일의 사이즈는 220바이트로 압축률도 뛰어나다.

# [08-05 파일 합치기1 - zipfile]
# zipfile은 여러개의 파일을 하나로 합치거나 해제할때 사용하는 도구이다.
# 문제
# 다음처럼 총 3개의 텍스트 파일이 있다.
# a.txt
# b.txt
# c.txt
# 이 3개의 텍스트 파일을 하나로 합쳐 mytext.zip 이라는 파일을 만들고, 또 만들어진 mytext.zip 파일을 원래의 3개의 텍스트
# 파일로 해제하는 코드를 작성하시오.
# 풀이
# zipfile.ZipFile을 사용한 풀이는 다음과 같다.
# import zipfile
# # 파일 합치기
# with zipfile.ZipFile('mytext.zip', 'w') as myzip:
#     myzip.write('a.txt')
#     myzip.write('b.txt')
#     myzip.write('c.txt')
# # 해제하기
# with zipfile.ZipFile('mytext.zip') as myzip:
#     myzip.extractall()
# ZipFile 객체의 write 함수로 개별 파일을 추가할 수 있고 extreactall 함수를 사용하면 모든 파일을 해제할 수 있다.
# 만약 합쳐진 파일에서 특정 파일만 해제하고 싶다면 다음과 같이 extract 함수를 사용하면 된다.
# with zipfile.ZipFile('mytext.zip') as myzip:
#     myzip.extract('a.txt')

# [08-06 파일 합치기2 - tarfile]
# tarfile은 여러개의 파일을 하나로 합치거나 해제할때 사용하는 도구이다.
# ※ 파일을 합칠 때 gzip, bz2 및 lzma 압축을 사용할 수 있다.
# 문제
# 다음처럼 총 3개의 텍스트 파일이 있다.
# a.txt
# b.txt
# c.txt
# 이 3개의 텍스트 파일을 하나로 합쳐 mytext.tar 라는 파일을 만들고, 또 만들어진 mytext.tar 파일을 원래의 3개의 텍스트
# 파일로 해제하는 코드를 작성하시오.
# 풀이
# tarfile을 사용한 풀이는 다음과 같다.
# import tarfile
# # 여러파일 합치기
# with tarfile.open('mytext.tar', 'w') as mytar:
#     mytar.add('a.txt')
#     mytar.add('b.txt')
#     mytar.add('c.txt')
# # 여러파일 해제하기
# with tarfile.open('mytext.tar') as mytar:
#     mytar.extractall()
# tarfile.open으로 생성한 객체의 add 함수로 여러 파일을 추가할 수 있고 extreactall 함수를 사용하면 여러 파일을 해제할 수 있다.
# 만약 합쳐진 파일에서 특정 파일만 해제하고 싶다면 다음과 같이 extract 함수를 사용하면 된다.
# with tarfile.open('mytext.tar') as mytar:
#     mytar.extract('a.txt')
# 만약 tar파일을 작성할 때 파일도 압축하여 합치고 싶다면 다음처럼 압축방법에 대한 문자열(:gz)을 추가로 전달해 주면 된다.
# import tarfile
# # 여러파일 합치기
# with tarfile.open('mytext.tar.gz', 'w:gz') as mytar:
#     mytar.add('a.txt')
#     mytar.add('b.txt')
#     mytar.add('c.txt')
# # 여러파일 해제하기
# with tarfile.open('mytext.tar.gz') as mytar:
#     mytar.extractall()
# w:gz 처럼 gzip 압축을 사용할 경우 관례적으로 *.tar.gz와 같은 확장자를 가지도록 파일이름을 짓는다.
# 만약 w:bz2 (bzip2 압축)를 사용할 경우에는 *.tar.bz2라고 명명하며 w:xz (lzma 압축)을 사용할 경우에는 *.tar.xz 라고 명명한다.


# [09장 파일 형식]

# [09-01 CSV 파일 읽고 쓰기 - csv]
# csv 모듈은 csv 파일을 읽고 쓰기위해 사용되는 파이썬 표준 라이브러리이다.
# 문제
# 다음처럼 엑셀로 작성되어진 score.csv 파일이 있다. 두번째 열(B열)은 총 2번의 시험 점수를 의미한다.
# 이 파일을 읽어 2번의 시험 점수의 평균점수를 4번째 열(D열)에 기록한 score_result.csv 파일을 작성하시오.
# score_result.csv 파일을 엑셀로 읽으면 다음처럼 4번째 열이 추가되어 보여야 한다.
# 풀이
# score.csv 파일은 80,55 처럼 데이터 내에 콤마가 포함되어 있기 때문에 콤마로 split하여 데이터를 추출하는 방법은 피해야 한다.
# csv파일을 처리할 때는 다음처럼 csv 모듈을 사용하는 것이 가장 좋다.
# import csv
# result = []
# with open('score.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for line in reader:
#         average = sum(map(int, line[1].split(','))) / 2
#         line.append(average)
#         result.append(line)
# with open('score_result.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(result)
# csv 파일을 읽을때는 csv.reader를 사용한다. 점수는 콤마로 나누어진 문자열이므로 
# average = sum(map(int, line[1].split(','))) / 2 처럼 콤마로 나누고 정수로 바꾼후에 평균값을 계산하였다.
# reader로 읽어들인 line은 리스트 자료형이므로 평균값(average)을 4번째 항목에 추가했다.
# 마찬가지로 csv파일을 작성하기 위해서는 csv.writer를 사용한다. csv.writer로 만든 writer객체에 writerows 함수를 사용하면 
# 전체 데이터를 파일에 저장할 수 있다.
# 여시서 사용된 newline=''은 윈도우즈에서는 데이터를 쓸 때 각 라인의 뒤에 빈 라인이 추가되는 문제가 있는데 이를 방지하기 
# 위함이다.

# [09-02 ini 파일 처리하기 - configparser]
# ini 파일은 프로그램 정보를 저장하는 텍스트 문서로 섹션과 그 섹션에 해당되는 키=값 들로 구성된다. configparser 모듈은 
# 이러한 ini 파일을 처리할때 사용하는 파이썬 모듈이다.
# 참고 : INI 파일
# 문제
# 다음 ftp.ini 파일에서 FTP2 섹션의 PORT정보를 읽어서 출력하시오.
# [파일명: ftp.ini]
# [FTP1]
# SERVER_IP = 111.23.56.78
# PORT = 21
# USERNAME = foo
# PASSWORD = bar
# [FTP2]
# SERVER_IP = 111.23.56.79
# PORT = 22221
# USERNAME = admin
# PASSWORD = hello
# 풀이
# ini 파일의 정보를 얻기 위해서는 다음처럼 configparser를 사용해야 한다.
# import configparser
# config = configparser.ConfigParser()
# config.read('ftp.ini')
# ftp2_port = config['FTP2']['PORT']
# print(ftp2_port)  # 22221 출력
# 먼저 configparser.ConfigParser()로 만든 config객체의 read함수로 ini 파일을 읽어들인다.
# config.read('ftp.ini')
# 그리고 다음과 같은 방법으로 ini 해당 섹션의 키에 해당하는 값을 얻을 수 있다.
# config[섹션명][키]
# FTP2 섹션의 PORT키에 해당되는 값을 얻기 위해 다음처럼 사용하였다.
# config['FTP2']['PORT']


# [10장 암호화 서비스]
# [10-01 문자열 해싱 - hashlib]
# hashlib 모듈은 md5, sha256등의 알고리즘으로 문자열을 해싱(Hashing)할때 사용하는 파이썬 표준 라이브러리이다.
# 해싱이란 원본 문자열을 알아볼 수 없는 난해한 문자열로 정의하는 방법으로 해시값을 조사하여 데이터 변조의 유무를 확인하는
# 것이 주 목적이다.
# 문제
# 입력한 비밀번호를 파일(passwd.txt)에 저장하는 프로그램을 작성하시오. (단, 비밀번호는 유추 및 복호화가 불가능한 
# sha256방식으로 해싱하여 저장할 것) 그리고 이미 비밀번호 파일이 있을 경우에는 기존 비밀번호를 입력받아 비밀번호가 
# 일치할 경우에만 새로운 비밀번호를 저장할 수 있도록 코딩하시오.
# 풀이
# 다음은 hashlib 모듈을 사용한 풀이이다.
# import hashlib
# import os
# def check_passwd():
#     if os.path.exists('passwd.txt'):
#         before_passwd = input('기존 비밀번호를 입력하세요:')
#         m = hashlib.sha256()
#         m.update(before_passwd.encode('utf-8'))
#         with open('passwd.txt', 'r') as f:
#             return m.hexdigest() == f.read()
#     else:
#         return True
# if check_passwd():
#     passwd = input('새로운 비밀번호를 입력하세요:')
#     with open('passwd.txt', 'w') as f:
#         m = hashlib.sha256()
#         m.update(passwd.encode('utf-8'))
#         f.write(m.hexdigest())
# else:
#     print("비밀번호가 일치하지 않습니다.")
# check_passwd 함수는 이미 작성된 비밀번호 파일이 없거나 기존 비밀번호와 일치하는 경우에 True를 리턴한다. check_passwd 함수가
# True를 리턴할 경우에만 새로운 비밀번호를 생성하여 파일에 저장할 수 있다.
# sha256방식으로 해싱 할 수 있는 객체는 hashlib.sha256()로 만들 수 있다. 문자열을 해싱하기 위해서는 update함수를 사용한다. 
# 이때 해싱할 문자열은 바이트 문자열로 바꾸어 주어야 하므로 utf-8 인코딩 방식의 바이트 문자열로 먼저 바꾸어 사용해야 한다. 
# 그리고 해싱된 문자열은 hexdigest 함수를 사용하여 16진수 형태로 변환하여 사용하였다.

# [10-02 메시지 인증을 위한 키 해싱 - hmac]
# hmac은 해싱기술을 사용하여 송수신자 간의 메시지 변조를 확인할 수 있는 모듈이다.
# 문제
# A씨는 B씨에게 인터넷으로 파일을 전달하여 중요한 메시지를 전달하려고 한다. 하지만 어떤 해커가 A씨가 보낸 파일을 중간에서
# 가로채어 내용을 바꾼 후에 B씨에게 전달할 가능성이 있다고 한다.
# A씨가 보낸 파일이 해커에 의해 변조되었는지 변조되지 않았는지 확인할 수 있는 프로그램을 작성하시오. 단, 해커가 파일의
# 내용을 보는 것은 상관이 없고 파일이 변조었는지만 확인할 수 있으면 된다.
# 풀이
# hmac 모듈을 사용하면 이 문제를 쉽게 해결할 수 있다. hmac은 서로 약속된 비밀키가 필요하다. 이 비밀키는 해커가 알 수 없게 
# 비밀스럽게(전화통화 또는 구두로 전달) 공유된 값이어야 한다.
# A씨와 B씨가 서로 공유할 비밀키는 다음과 같다고 한다.
# PYTHON
# 이제 A씨는 보내야 할 원본 파일과 비밀키를 이용하여 해싱한 해싱 파일 2개를 B씨에게 인터넷으로 전달하면 된다. 그리고 B씨는 
# 전달받은 원본 파일의 내용을 PYTHON 이라는 공유 키로 해싱한 결과가 전달받은 해싱 파일의 내용과 동일한지를 비교하여 메시지가 
# 변조되었는지를 확인하면 된다.
# 물론 해커는 원본 파일과 해싱 파일을 변조할 수 있겠지만 PYTHON이라는 비밀키 값을 알수 없으므로 파일을 변조했다면 금방 
# 들통나게 될 것이다.
# 다음은 A씨가 B씨에게 전달할 원본파일(message.txt)과 해싱파일(message_digest.txt)을 작성하는 코드이다.
# import hmac
# import hashlib
# SECRET_KEY = 'PYTHON'
# important_message = '나의 생각은 내가 아니다.'
# with open('message.txt', 'w') as f:
#     f.write(important_message)
# with open('message_digest.txt', 'w') as f:
#     m = hmac.new(SECRET_KEY.encode('utf-8'), important_message.encode('utf-8'),
#                  hashlib.sha256)
#     f.write(m.hexdigest())
# 비밀키는 다음처럼 설정하였다.
# SECRET_KEY = 'PYTHON'
# 보내야할 메시지를 message.txt 원본파일에 저장하고 hmac.new(비밀키, 메시지, 암호화방식) 을 사용하여 메시지를 해싱한 값을
# message_digest.txt 파일에 저장하였다. 이 때 비밀키와 메시지는 바이트 문자열을 사용해야 하므로 utf-8로 문자열을 인코딩해야
# 한다. 암호화 방식은 sha256을 사용하였다.
# 이제 A씨는 원본파일(message.txt)과 해싱파일(message_digest.txt)을 B씨에게 인터넷(메일, FTP, 기타등등)으로 전달하면 된다.
# 그리고 B씨는 전달받은 2개의 파일을 다음과 같이 검증해야 한다.
# import hmac
# import hashlib
# SECRET_KEY = 'PYTHON'
# with open('message_digest.txt') as f:
#     message_digest = f.read()
# with open('message.txt') as f:
#     message = f.read()
#     m = hmac.new(SECRET_KEY.encode('utf-8'), message.encode('utf-8'),
#                  hashlib.sha256)
#     if m.hexdigest() == message_digest:
#         print("메시지가 변조되지 않았습니다. 안전합니다.")
# 전달받은 해싱파일의 내용과 원본파일의 내용을 'PYTHON' 이라는 비밀키로 해싱했을때의 값이 동일한지를 체크하여 원본파일의 내용이
# 손상되었는지를 확인할 수 있다.

# [10-03 편리한 난수 생성기 - secrets]
# secrets 모듈은 난수를 생성하는 파이썬 라이브러리이다.
# 문제
# 16진수 문자로 구성된 32자리의 난수 문자열을 생성하시오.
# 16진수 문자는 숫자 0~9, 문자 a~f 사이의 문자를 의미한다.
# 풀이
# 다음은 secrets 모듈을 사용한 해법이다.
# import secrets
# key = secrets.token_hex(16)
# print(key)
# 출력결과는 다음과 같다. (난수이므로 실행할때마다 값이 변한다.)
# 3f9c82af943b6e5b6279f4fb5985f1d2
# secrets.token_hex(nbytes) 에서 nbytes는 바이트수이다. 1바이트는 2개의 16진수 문자열로 변환되므로 secrets.token_hex(16) 
# 처럼하면 32자리로 구성된 난수 문자열을 얻을 수 있다.
# 만약 16자리의 난수 문자열을 얻고 싶다면 다음처럼 사용하면 된다.
# key = secrets.token_hex(8)
''' import secrets
key = secrets.token_hex(16)
print(key) '''


# [11장 일반 운영체제 서비스]

# [11-01 문자열을 파일처럼 사용하기 - io.StringIO]
# io.StringIO 는 문자열을 파일객체처럼 사용할 수 있게 도와주는 모듈이다.
# 문제
# 다음은 csv 파일을 읽어 첫번째 행과 두번째 행의 숫자를 더해 세번째 행에 추가한 전체 결과를 리턴하는 프로그램이다.
# 참고 : CSV 파일 읽고 쓰기 - https://wikidocs.net/121964
# import csv
# def execute(f):
#     result = []
#     reader = csv.reader(f)
#     for line in reader:
#         one = int(line[0])
#         two = int(line[1])
#         three = one+two
#         line.append(three)
#         result.append(line)
#     return result
# with open('src.csv', 'r', encoding='utf-8') as f:
#     result = execute(f)  # 함수실행
#     print(result)
# execute 함수를 구동하기 위한 src.csv 파일의 내용은 다음과 같다.
# 20,40
# 50,90
# 77,22
# 그리고 이 프로그램을 실행하면 다음과 같은 결과가 출력된다.
# [['20', '40', 60], ['50', '90', 140], ['77', '22', 99]]
# src.csv 파일 대신 src.csv와 동일한 내용의 문자열을 전달하여 execute 함수를 실행할 수 있도록 프로그램을 변경하시오.
# 단, execute 함수의 내용은 변경할 수 없다.
# 풀이
# execute 함수는 인수로 파일객체를 필요로 하기 때문에 문자열을 전달할 수 없다. 하지만 다음처럼 문자열을 파일 객체처럼 
# 만들어 주는 io.StringIO 를 사용하면 파일생성 없이 문자열을 전달하는 것이 가능하다.
# import csv
# def execute(f):
#     result = []
#     reader = csv.reader(f)
#     for line in reader:
#         one = int(line[0])
#         two = int(line[1])
#         three = one+two
#         line.append(three)
#         result.append(line)
#     return result
# src = """
# 20,40
# 50,90
# 77,22
# """
# import io
# with io.StringIO(src) as f:  # 문자열을 파일객체럼 만든다.
#     result = execute(f)
#     print(result)
# src라는 문자열을 io.StringIO(src)를 사용하여 파일과 동일한 역할을 하는 객체를 만들었다. 따라서 execute함수는 수정할 필요가
# 없어진다.
# 출력결과는 다음과 같이 동일하다.
# [['20', '40', 60], ['50', '90', 140], ['77', '22', 99]]
''' import csv
def execute(f):
    result = []
    reader = csv.reader(f)
    for line in reader:
        one = int(line[0])
        two = int(line[1])
        three = one+two
        line.append(three)
        result.append(line)
    return result
src = """
20,40
50,90
77,22
"""
import io
with io.StringIO(src) as f:  # 문자열을 파일객체럼 만든다.
    result = execute(f)
    print(result) '''

[11-02 명령행 파서 - argparse]
argparse는 파이썬 스크립트의 명령행 옵션을 파싱할때 사용하는 모듈이다.

문제
다음과 같이 동작하는 add_mul.py를 작성하시오.

$ python add_mul.py -a 1 2 3 4 5
합은 15입니다.
$ python add_mul.py --add 1 2 3 4 5
합은 15입니다.
$ python add_mul.py -m 1 2 3 4 5
곱은 120입니다.
$ python add_mul.py --mul 1 2 3 4 5
곱은 120입니다.
$ python add_mul.py -a 1 2 3 4 5 -m 1 2 3 4 5
합은 15입니다.
곱은 120입니다.
-a 또는 --add 옵션을 주었을 경우에는 뒤따라오는 정수들의 합을 출력하고 -m 또는 --mul 옵션을 주었을 경우에는 뒤따라오는 정수들의 곱을 출력해야 한다. 그리고 두 개의 옵션을 함께 사용할 수도 있어야 한다.

풀이
이 문제는 sys.argv 모듈을 사용하여 해결할 수도 있지만 다음처럼 argparse 모듈을 사용하는 것이 편리하고 안전하다.

[add_mul.py]

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자')
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')

args = parser.parse_args()

if args.add:
    print("합은 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("곱은 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))
parser = argparse.ArgumentParser() 로 만든 parser객체에 add_argument함수를 사용하여 명령행을 파싱하는 규칙을 만들면 된다. -a, --add 는 명령행 옵션을 의미하고 type은 뒤따라오는 숫자의 자료형을 의미한다. nargs는 뒤따라오는 숫자의 갯수를 의미하는데 +를 사용하면 1개 이상의 값이 필요함을 의미한다.

metavar나 help는 다음처럼 -h 옵션으로 도움말을 출력할때 도움말을 잘 표현하기 위해 사용된다.

$ python add_mul.py -h
usage: add_mul.py [-h] [-a N [N ...]] [-m N [N ...]]

optional arguments:
  -h, --help            show this help message and exit
  -a N [N ...], --add N [N ...]
                        더할 숫자
  -m N [N ...], --mul N [N ...]
                        곱할 숫자
metavar에 사용된 N이라는 문자가 설명문에 어떻게 표시되고 help 문자열이 어떻게 보이는지 확인할 수 있다.

[11-03 로그파일 생성하기 - logging]
logging은 로그를 파일에 출력하기 위해 사용하는 모듈이다.

로그는 파일뿐만 아니라 소켓, 이메일, 콘솔등 다양한 방법으로 출력이 가능하다.

문제
다음 myfunc 함수에서 "함수가 시작되었습니다." 라는 문자열을 print로 출력하는 대신 debug.log 라는 로그파일에 저장할 수 있도록 변경하시오.

def myfunc():
    print("함수가 시작되었습니다.")

myfunc()
단, 출력되는 문자열은 다음과 같이 시간 + 메시지 형식이어야 함

[2021-04-06 00:35:32,089] 함수가 시작되었습니다.
풀이
로그 파일에 로그를 작성하기 위해서는 파이썬 logging 모듈을 사용해야 한다. 다음처럼 dictConfig로 표시할 로그를 설정하고 logging.debug로 로그를 출력하면 된다.

from logging.config import dictConfig
import logging

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})


def myfunc():
    logging.debug("함수가 시작되었습니다.")


myfunc()
이와 같이 프로그램을 수정한 후 실행해 보면 debug.log 파일에 다음과 같은 로그가 출력되는 것을 확인할 수 있다.

[debug.log]

[2021-04-06 00:35:32,089] 함수가 시작되었습니다.
dictConfig에 설정한 내용을 자세히 알아보자.

version을 고정값 "1"로 지정했다

version은 고정값 “1”을 사용해야 한다. 만약 다른 값을 입력하면 ValueError가 발생한다. 이 값은 의미 없어 보일 수도 있지만, logging 모듈이 미래에 업그레이드 될때 현재 설정을 보장해 주는 안전장치이다.

formatters에 로그를 출력할 형식을 정의했다

formatters에는 ‘로그를 출력할 형식’을 정의한다. 여기서는 default 포맷터를 등록했다. default 포맷터에 사용한 항목은 다음과 같다.

asctime: 현재 시간
message: 출력 내용
다음과 같은 항목도 추가로 사용가능하다.

levelname: 로그의 레벨(debug, info, warning, error, critical)
module: 로그를 호출한 모듈명
handlers에 로그를 출력할 방법을 정의했다

handlers에는 ‘로그를 출력하는 방법’을 정의한다. 여기서는 file이라는 핸들러를 등록했다. file 핸들러에 사용한 항목은 다음과 같다.

level: 출력 로그 레벨, 여기서는 DEBUG를 사용
class: 로그 핸들러 클래스, FileHandler를 사용.
filename: 로그 파일명
formatter: 포맷터, default 설정
root에 DEBUG 로그를 출력하도록 설정하고 이를 위해 file 핸들러를 추가했다

root는 ‘최상위 로거’를 의미한다. 로그 레벨은 DEBUG로 설정하고, 로그를 출력할 핸들러로 file 핸들러를 추가했다.

level: 로그 레벨, DEBUG로 설정
handler: 로그 핸들러, 위에서 정의한 file로 설정
참고로 로그 레벨은 다음과 같이 5단계로 구성된다.

1단계 DEBUG: 디버깅 목적으로 사용
2단계 INFO: 일반 정보를 출력할 목적으로 사용
3단계 WARNING: 경고 정보를 출력할 목적으로(작은 문제) 사용
4단계 ERROR: 오류 정보를 출력할 목적으로(큰 문제) 사용
5단계 CRITICAL: 아주 심각한 문제를 출력할 목적으로 사용
설명에서 짐작할 수 있듯이 로그 레벨의 순서는 다음과 같다. 그리고 설정한 레벨 이상의 로그만 출력될 것이다.

DEBUG < INFO < WARNING < ERROR < CRITICAL
예를 들어 핸들러나 로거에서 로그 레벨을 INFO로 설정하면 DEBUG 로그는 출력되지 않고 INFO 이상의 로그, 즉 INFO, WARNING, ERROR, CRITICAL만 출력된다.

만약 ERROR로 설정하면 ERROR, CRITICAL 로그만 출력된다.

[11-04 에코없이 암호 입력하기 - getpass]
getpass는 비밀번호 입력시 비밀번호가 화면에 노출되지 않게 해 주는 모듈이다.

문제
다음은 사용자의 비밀번호를 묻는 프로그램이다.

passwd = input("Password:")
하지만 위 프로그램을 실행하면 다음처럼 입력하는 비밀번호가 화면에 노출된다.

Password:abcde1234
입력받는 비밀번호가 화면에 노출(에코)되지 않도록 프로그램을 변경하시오.

풀이
다음은 getpass 모듈을 이용한 풀이이다.

import getpass

passwd = getpass.getpass("Password:")
input 대신에 getpass.getpass를 사용하면 화면에 입력하는 비밀번호가 노출되지 않는다.

[11-05 터미널 그래픽 애플리케이션 - curses]
curses는 터미널 그래픽 애플리케이션을 만들 수 있는 모듈이다.

문제
사용자에게 1~100 사이의 숫자 두개를 더하는 문제를 3회 반복하여 풀게하시오. 단 하나의 문제를 풀고 다음 문제를 풀때는 화면을 모두 클리어 하여 이전 문제가 보이지 않게 해야 하고 덧셈에 사용되는 숫자는 잘 보일수 있도록 강조된 색상으로 표현하시오. 그리고 3개의 문제를 모두 풀면 최종결과(맞은갯수와 틀린갯수)를 표시하시오.

[출력 형식의 예]



풀이
터미널을 제어하기 위해서는 curses 모듈을 사용해야 한다. curses 모듈을 사용하면 화면을 clear하거나 원하는 위치에 문자열을 삽입할 수 있고 또 문자에 색을 입힐수 있다.

다음은 curses 모듈을 사용한 풀이이다.

import curses
import random

try:
    stdscr = curses.initscr()

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    success = 0
    failure = 0

    for i in range(3):
        stdscr.clear()  # 문제가 변경되면 화면을 클리어한다.
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        result = a + b

        stdscr.addstr(0, 0, str(a), curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(" + ")
        stdscr.addstr(str(b), curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(" = ?")

        answer = stdscr.getstr(1, 0, 3)

        if result == int(answer):
            success += 1
        else:
            failure += 1

    stdscr.addstr(3, 0, "맞은갯수:%d, 틀린갯수:%d" % (success, failure))
    stdscr.addstr(5, 0, "Press enter key...")
    stdscr.getkey()

finally:
    curses.endwin()

curses로 터미널을 제어하기 위해서는 가장먼저 initscr()을 호출하여 터미널 객체 stdscr을 생성해야 한다.

stdscr = curses.initscr()
그리고 프로그램이 종료된 후에는 다시 터미널을 원상태로 복구하기 위해 curses.endwin()을 반드시 호출해야 한다. 여기서는 curses.endwin()이 프로그램 정상수행 여부에 상관없이 항상 호출되도록 하기 위해 try .. finally 절에 사용하였다.

curses.endwin()
글씨에 색을 표시하기 위해서는 다음과 같은 과정이 필요하다.

curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
start_color와 use_default_color를 호출하여 색상을 초기화하고 검은색 배경의 하늘색 글씨를 사용하기 위해 init_pair로 글색상을 생성하였다.

숫자를 화면에 표시할 때 만든 색상을 사용하였다.

stdscr.addstr는 화면에 문자열을 출력할 때 사용한다. stdscr.addstr(0, 0, "abc") 와 같이 사용되면 0번째 줄 0번째 열부터 "abc"라는 문자열을 출력하라는 의미이다. 만약 줄과 열에 대한 값을 생략하면 현재 커서의 위치에서 문자열을 출력한다.

사용자의 입력을 얻기 위해서는 다음과 같이 stdscr.getstr 을 사용하였다.

answer = stdscr.getstr(1, 0, 3)
stdscr.getstr(1, 0, 3)의 의미는 1번째 줄 0번째 열에서 3개의 문자만 입력 받겠다는 의미이다. 입력받아야 할 숫자는 1~100 사이의 숫자 두개의 합에 대한 결과이므로 3개의 문자로 충분하다.

그리고 마지막으로 화면이 종료되기 전에 최종결과를 표시해 주기 위해 stdscr.getkey()로 사용자의 아무 키나 입력받도록 해 주었다. 이 과정이 없다면 최종결과를 볼 틈도 없이 프로그램이 종료될 것이다.


[11-06 시스템 환경 확인하기 - platform]
platform 모듈을 사용하면 시스템 환경을 확인할 수 있다.

문제
현재 시스템의 CPU 및 OS정보를 출력하시오.

풀이
platform 모듈을 사용하면 CPU 및 OS정보를 쉽게 취득할 수 있다.

>>> import platform
>>>
>>> info = platform.uname()
>>> print(info)
uname_result(system='Windows', node='DESKTOP-8R43RU6', release='10', version='10.0.18362', machine='AMD64', processor='AMD64 Family 23 Model 17 Stepping 0, AuthenticAMD')
platform의 uname함수를 사용하면 namedtuple 형태의 시스템 정보를 얻을 수 있다.

CPU정보는 다음과 같다.

>>> print(info.processor)
AMD64 Family 23 Model 17 Stepping 0, AuthenticAMD
OS정보는 다음과 같다.

>>> print(info.system)
Windows
다음은 processor와 system 이외의 것들에 대한 간략한 설명이다.

node - 네트워크 이름
release - 시스템의 릴리즈 번호
version - 시스템의 릴리즈 버전
machine - 시스템의 유형

[11-07 C 라이브러리 사용하기 - ctypes]
ctypes 모듈을 사용하면 C로 작성된 라이브러리를 파이썬에서 쉽게 사용할 수 있다.

문제
다음과 같이 작성되어진 C 프로그램이 있다.

[파일명:mylib.c]

int add(int a, int b)
{
    return a + b;
}
두 개의 정수를 입력받아 더하여 리턴하는 간단한 add 함수이다. 이 add함수를 파이썬에서 불러서 사용하시오.

풀이
mylib.c에 작성된 add함수를 파이썬에서 사용하기 위해서는 먼저 다음처럼 mylib.so(shared library)파일을 만들어야 한다.

$ gcc -c mylib.c 
$ gcc -shared mylib.o -o mylib.so
mylib.so가 만들어지면 파이썬 ctypes 모듈을 사용하여 다음과 같이 사용할 수 있다.

>>> import ctypes
>>> mylib = ctypes.cdll.LoadLibrary('./mylib.so')
>>> mylib.add(3, 4)
7
ctypes.cdll의 LoadLibrary로 현재 디렉터리에 만들어진 mylib.so를 읽어 사용하면 된다.


[12장 동시실행]

[12-01 스레드 기반의 병렬처리 - threading]
threading모듈은 한 프로세스에서 2가지 또는 그 이상의 일을 동시에 수행하도록 한다.

문제
다음 프로그램은 페이지번호를 입력받아 위키독스의 페이지 리소스를 wikidocs_페이지번호.html 파일로 저장하는 프로그램이다.

import urllib.request


def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'
A씨는 다음처럼 10개의 위키독스 페이지가 필요하다고 한다.

[12, 13, 14, 15, 17, 18, 20, 21, 22, 24]
위 프로그램을 사용하면 페이지수 만큼 실행하여 원하는 결과를 얻을 수 있다. 하지만 A씨는 10개의 요청을 하나씩 보내기 보다는 동시에 요청하여 보다 빠른 속도로 리소스를 얻기 원한다. 동시요청이 가능하도록 프로그램을 수정하시오.

풀이
동시요청을 위해서는 threading 모듈을 사용하면 된다. 먼저 threading 없이 10개의 페이지를 요청할 경우 얼마의 시간이 소요되는지 측정해 보자.

import urllib.request


def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'


import time

start = time.time()

pages = [12, 13, 14, 15, 17, 18, 20, 21, 22, 24]
for page in pages:
    get_wikidocs(page)

end = time.time()

print("수행시간: %f 초" % (end - start))
출력결과는 다음과 같다.

wikidocs page:12
wikidocs page:13
wikidocs page:14
wikidocs page:15
wikidocs page:17
wikidocs page:18
wikidocs page:20
wikidocs page:21
wikidocs page:22
wikidocs page:24
수행시간: 10.096202 초
10개의 페이지 리소스를 저장하는데 10초 정도의 시간이 소요되었다.

이번에는 threading 모듈을 사용하여 페이지 리소스를 동시에 저장하도록 변경해 보자.

import urllib.request


def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'


import time
import threading

start = time.time()

pages = [12, 13, 14, 15, 17, 18, 20, 21, 22, 24]
threads = []
for page in pages:
    t = threading.Thread(target=get_wikidocs, args=(page, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()  # 스레드가 모두 종료될 때까지 기다린다.

end = time.time()

print("수행시간: %f 초" % (end - start))
threading.Thread로 get_wikidocs함수를 실행하는 스레드 t를 생성해 주었다. target은 실행할 함수 그리고 args는 함수에 전달해야할 파라미터를 의미한다. 이렇게 스레드를 생성한 후 t.start()를 실행하면 스레드가 독립적으로 실행된다. (각각의 스레드는 이전 스레드의 종료를 기다리지 않고 곧바로 실행된다.) 그리고 만들어진 각각의 스레드 t는 threads라는 리스트 변수에 담아 주었다. 이렇게 하는 이유는 생성된 스레드가 모두 종료된 후에 수행시간을 출력하기 위해서이다. 생성된 스레드를 모두 종료하기 위해서는 생성된 각 스레드마다 join() 함수를 호출해 주어야만 한다. 만약 join 없이 위 프로그램을 실행하면 아직 스레드가 종료되지 않은 상태에서 수행시간이 출력되어 버리기 때문에 정확한 수행시간을 출력할 수 없게 된다.

출력결과는 다음과 같다.

wikidocs page:12
wikidocs page:13
wikidocs page:14
wikidocs page:15
wikidocs page:17
wikidocs page:18
wikidocs page:20
wikidocs page:21
wikidocs page:22
wikidocs page:24
수행시간: 2.453772 초
10초 정도 걸리던 작업이 2.4초 가량으로 상당히 단축된 것을 확인할 수 있다.

[12-02 프로세스 기반의 병렬처리 - multiprocessing]
multiprocessing 모듈을 사용하면 멀티 프로세스를 활용하여 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.

문제
다음은 CPU 연산이 많은 heavy_work 함수를 4번 수행하고 총 소요된 시간을 측정하는 예제이다.

import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


start = time.time()

for i in range(4):
    heavy_work(i)

end = time.time()

print("수행시간: %f 초" % (end - start))
실행 결과는 다음과 같다.

0 done
1 done
2 done
3 done
수행시간: 2.027041 초
heavy_work 함수를 동시에 실행하여 수행시간을 단축하시오.

풀이
다음은 threading 모듈을 사용한 풀이이다.

import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import threading

    start = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target=heavy_work, args=(i, ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # 스레드가 모두 종료될 때까지 기다린다.

    end = time.time()

    print("수행시간: %f 초" % (end - start))
실행 결과는 다음과 같다.

2 done
0 done
1 done
3 done
수행시간: 2.005648 초
스레드는 이처럼 CPU연산만 수행하는 경우에 수행시간에 전혀 이득이 없음을 확인할 수 있다.

※ 파이썬 스레드는 메모리 관리를 위해 하나의 thread만이 Python object에 접근할 수 있도록 제한하는데 이것을 GIL(Global Interpreter Lock)이라고 한다. 이러한 이유로 스레드는 GIL에 영향을 받지 않는 I/O가 주로 발생하는 작업(네트워크 통신, 파일 읽고 쓰기등)에 유리하다.

이번에는 threading대신 multiprocessing 모듈을 사용해 보자.

※ multiprocessing 모듈은 멀티 프로세스와 별개의 메모리를 사용하여 완전히 독립적인 병렬 프로그래밍이 가능하다. 단, 여러개의 CPU를 가지고 있는 멀티코어 환경에서만 가능하다.

import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import multiprocessing

    start = time.time()
    procs = []
    for i in range(4):
        p = multiprocessing.Process(target=heavy_work, args=(i, ))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()  # 프로세스가 모두 종료될 때까지 기다린다.

    end = time.time()

    print("수행시간: %f 초" % (end - start))
사용방법은 threading 모듈을 사용하는 것과 거의 동일하다. multiprocessing.Process 클래스로 프로세스를 생성한다. target에는 실행할 함수명을 지정하고 args에는 그 함수에 전달할 파라미터를 설정한다. 스레드와 마찬가지로 start함수로 프로세스를 실행하고 join함수로 프로세스가 종료될때까지 기다린다.

multiprocessing.Process를 사용한 결과는 다음과 같다.

0 done
3 done
1 done
2 done
수행시간: 0.663679 초
멀티코어 환경에서 무려 3배 이상의 속도향상이 있음을 확인할 수 있다.

multiprocessing.Process 과 비슷하게 multiprocessing.Pool 을 사용할 수도 있다. 사용방법은 다음과 같다.

import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import multiprocessing

    start = time.time()
    pool = multiprocessing.Pool(processes=4)
    pool.map(heavy_work, range(4))
    pool.close()
    pool.join()

    end = time.time()

    print("수행시간: %f 초" % (end - start))
multiprocessing.Pool(processes=4) 과 같이 pool 객체를 만든후 실행할 함수와 파라미터를 인자로 하여 map함수를 호출하여 프로세스를 실행할 수 있다. multiprocessing.Pool은 포크할 프로세스의 갯수를 지정할 수 있는 특징이 있다. 위 예에서는 4개의 프로세스를 실행하도록 설정하였다.

[12-03 병렬작업 실행하기 - concurrent.futures]
스레드를 구현하기 위해서는 threading 모듈을 사용하고 멀티 프로세스 프로그램을 구현하기 위해서는 multiprocessing 모듈을 사용해야 한다. 하지만 일반적인 경우에 concurrent.futures를 사용하면 동일한 규칙으로 스레드와 멀티 프로세스 코드를 쉽게 작성할 수 있다.

문제
다음은 multiprocessing 챕터에서 다루었던 풀이이다.

※ 참고 : https://wikidocs.net/124290

import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import multiprocessing

    start = time.time()
    procs = []
    for i in range(4):
        p = multiprocessing.Process(target=heavy_work, args=(i, ))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()  # 프로세스가 모두 종료될 때까지 기다린다.

    end = time.time()

    print("수행시간: %f 초" % (end - start))
heavy_work 함수를 여러 프로세스가 동시에 호출하는 코드이다. 현재 heavy_work함수는 result를 계산만 하고 그 값을 리턴하지 않고 있다. heavy_work함수가 계산된 result를 리턴하도록 수정하고 메인 프로세스에서는 호출된 heavy_work 함수의 리턴값을 모두 더해서 출력하도록 수정하시오.

풀이
multiprocess 모듈로 포크한 프로세스의 수행 결과를 메인 프로세스에서 취합하는 방법에는 여러가지가 있겠지만 가장 일반적으로 사용되는 concurrent.futures 모듈로 이 문제를 풀어보자.

import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)
    return result  # 결과를 리턴하도록 변경


if __name__ == '__main__':
    import concurrent.futures

    start = time.time()

    total_result = 0
    pool = concurrent.futures.ProcessPoolExecutor(max_workers=4)

    procs = []
    for i in range(4):
        procs.append(pool.submit(heavy_work, i))

    for p in concurrent.futures.as_completed(procs):
        total_result += p.result()

    end = time.time()

    print("수행시간: %f 초" % (end - start))
    print("총결괏값: %s" % total_result)
우선 heavy_work함수가 계산된 result를 리턴하도록 변경했다. 그리고 multiprocessing.Process를 사용하는 대신 concurrent.futures.ProcessPoolExecutor로 변경하였다. 두 개의 모듈이 하는 역할은 여러개의 프로세스를 동시에 실행하는 것으로 동일하다. 단, concurrent.futures.ProcessPoolExecutor 는 max_workers를 지정하여 포크할 프로세스의 최대 갯수를 지정하는 것이 가능하다.

pool.submit(heavy_work, i)는 프로세스를 포크하여 heavy_work함수를 호출한다. i 는 heavy_work 함수에 전달되는 파라미터이다.

concurrent.futures.as_completed(procs)는 수행된 프로세스들이 모두 종료될 때까지 대기하게 하고 p.result()로 수행된 프로세스의 결과를 얻을 수 있게 해 준다.

수행 결과는 다음과 같다.

2 done
0 done
1 done
3 done
수행시간: 0.926396 초
총결괏값: 31999992000000
이전에 살펴보았던 위키독스의 여러 페이지 리소스를 스레드를 이용하여 가져오는 예제도 concurrent.futures.ThreadPoolExecutor 를 사용하여 다음과 같이 변경할 수 있다.

※ 참고 : https://wikidocs.net/124143

import urllib.request


def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'


if __name__ == '__main__':
    import time
    import concurrent.futures

    start = time.time()

    pages = [12, 13, 14, 15, 17, 18, 20, 21, 22, 24]
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    threads = []
    for page in pages:
        threads.append(pool.submit(get_wikidocs, page))

    concurrent.futures.wait(threads)  # 스레드가 모두 종료되기를 기다린다.

    end = time.time()

    print("수행시간: %f 초" % (end - start))
위 예제에서는 리턴값이 필요없으므로 concurrent.futures.as_completed 대신 concurrent.futures.wait 를 사용했다.

[12-04 시스템 명령어 실행 - subprocess]
subprocess는 시스템 명령을 다양한 방법으로 실행할 수 있는 모듈이다.

문제
다음은 유닉스(리눅스) 시스템에서 현재 디렉터리의 파일목록을 자세하게 출력하고 싶을때 사용하는 명령어이다.

ls -l
위 명령을 실행하여 그 결과를 out.txt 라는 파일에 저장하는 코드를 작성하시오.

풀이
시스템 명령어를 실행하는 방법에는 os.system, os.spawn 등이 있지만 사용방법이 다양하고 유연한 subprocess를 사용하는 것이 가장 일반적인 방법이다. 실제로 파이썬 os.system 문서를 보면 os.system 대신 subprocess를 사용하라고 권고하고 있다.

다음은 subprocess를 사용한 풀이이다.

import subprocess

with open('out.txt', 'wb') as f:
    out = subprocess.run(['ls', '-l'], capture_output=True)
    f.write(out.stdout)
※ 만약 윈도우 시스템이라면 ['ls', '-l'] 대신 ['dir']을 사용하면 된다.

ls -l 이라는 명령어는 ['ls', '-l'] 처럼 공백을 기준으로 split된 문자열을 리스트로 전달해야 한다.

다음처럼 shlex를 사용하면 보다 쉽게 명령어를 구분할 수 있다. 명령어가 복잡할 경우 shlex를 사용하면 편리하다.

import shlex

command = shlex.split('ls -l')
print(command)  # ['ls', '-l'] 출력
capture_output은 명령을 실행한 결과를 저장할 수 있다. capture_output을 True로 설정하면 위와 같이 CompletedProcess의 객체(out)를 리턴받아 표준출력에 해당되는 out.stdout 또는 표준에러에 해당되는 out.stderr를 구할 수 있다.

out.stdout은 바이트 데이터이므로 파일 작성시 'wb' 모드를 주어야 한다. 만약 출력 결과로 바이트 대신 문자열을 얻고 싶다면 다음처럼 text=True 옵션을 추가하면 된다.

out = subprocess.run(['ls', '-l'], capture_output=True, text=True)
만약 text=True 옵션을 추가했다면 출력결과는 바이트가 아닌 문자열이 되므로 파일쓰기 모드도 'wb' 대신 'w'로 바꾸어야 한다.

만약 다음처럼 복잡한 형태의 명령어를 실행하는 경우에는 shell=True 옵션을 사용하는 것이 유리하다.

import subprocess

subprocess.run('find ./ -name "*.html"|xargs grep "python"', shell=True)
※ 위에서 사용한 복잡한 find 명령어는 현재 디렉터리의 하위 디렉터리를 포함한 모든 html 파일에서 "python"이라는 문자열이 포함되어 있는 부분을 전부 찾으라는 명령어이다.

shell=True 옵션을 주면 명령어를 공백으로 구분할 필요없이 전체 명령어를 한 개의 문자열로 전달하면 된다.

[12-05 이벤트 스케줄러 - sched]
sched 모듈은 프로그램 수행 후 지정된 시간에 원하는 이벤트를 실행하도록 해 준다.

문제
다음과 같은 프로그램이 있다.

def print_a(a):
    print(a)


def print_b(b):
    print(b)


def print_c(c):
    print(c)


print_a("A")
print_b("B")
print_c("C")
print_a, print_b, print_c 함수를 한번씩 호출하는 프로그램이다. 이 프로그램을 다음과 같이 동작하도록 수정하시오.

프로그램 실행 후 5초 후에 print_a를 호출
프로그램 실행 후 3초 후에 print_b를 호출
프로그램 실행 후 7초 후에 print_c를 호출
풀이
time.sleep을 사용해서 이 문제를 풀 수도 있지만 프로그램 실행시간을 기준으로 스케줄을 작성해야 할 경우에는 sched 모듈을 사용하는 것이 가장 편리하다. 다음은 sched를 사용한 풀이이다.

def print_a(a):
    print(a)


def print_b(b):
    print(b)


def print_c(c):
    print(c)


import sched

s = sched.scheduler()
s.enter(5, 1, print_a, ('A',))  # 5초 후에 실행
s.enter(3, 1, print_b, ('B',))  # 3초 후에 실행
s.enter(7, 1, print_c, ('C',))  # 7초 후에 실행
s.run()
sched.scheduler() 로 스케줄러 객체 s를 생성한 후 s.enter 로 실행할 이벤트를 등록하면 된다. enter함수의 첫번째 파라미터는 delay시간(초)을 의미한다. 두번째 파라미터는 우선순위(priority)로 만약 동일한 delay시간에 1개 이상의 이벤트가 등록될 경우 우선순위가 높은 것(낮은 숫자가 우선순위가 높다)부터 시작된다. 세번째 파라미터는 실행할 함수이고 네번째 파라미터는 실행할 함수에 전달해야 하는 파라미터 값이다.

s.enter로 이벤트를 등록한 후 s.run으로 스케줄을 시작한다.

실행 결과는 다음과 같다.

B
A
C
프로그램 실행 후 3초 후에 B가 실행되고 그리고 2초 뒤(총 5초 경과 후)에 A 그리고 또 2초 뒤(총 7초 경과후)에 C가 출력된다.