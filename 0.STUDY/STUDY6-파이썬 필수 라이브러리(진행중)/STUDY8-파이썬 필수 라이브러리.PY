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
























