# 출처 [https://nadocoding.tistory.com, 나도코딩]


# [목차]

# [기본편]
# 1.소개 & 환경설정
# 2.자료형
# 3.연산자
# 4.문자열 처리
# 5.자료구조
# 6.제어문
# 7.함수
# 8.입출력
# 9.클래스
# 10.예외처리
# 11.모듈과 패키지


# [파이썬 기본편] 1-3.파이썬 실행하기
''' print("hello world") '''

# [파이썬 기본편] 2-1~2-3.숫자, 문자열, boolean 자료형
''' print(-10) # -10 출력
print(3.14) # 3.14 출력
print(1000) # 1000 출력
print(5+3) # 8 출력
print(2*8) # 16 출력 (주의 : x 가 아닌 * 예요)
print(3*(3+1)) # 12 출력
print('풍선') # 작은 따옴표로 감싼 문자열 
print("나비") # 큰 따옴표로 감싼 문자열 
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ") # 긴 문자열 
print("ㅋ"*9) # ㅋ 을 9번 출력
print(5 > 10) # False 출력 
print(5 < 10) # True 출력
print(True) # True 
print(False) # False
print(not True) # False 출력 
print(not False) # True 출력 
print(not (5 > 10)) # True 출력 '''

# [파이썬 기본편] 2-4.변수
''' animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3
print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며, " + hobby + "(을)를 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult)) '''

# [파이썬 기본편] 3-1.연산자
''' print(1 + 1) # 2
print(3 - 2) # 1
print(5 * 2) # 10
print(6 / 3) # 2.0
print(2 ** 3) # 2의 3제곱 = 2^3 = 8
print(5 % 3) # 5를 3으로 나눈 나머지 = 2
print(10 % 3) # 10을 3으로 나눈 나머지 = 1
print(5 // 3) # 5를 3으로 나눈 몫 = 1
print(10 // 3) # 10을 3으로 나눈 몫 = 3
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True
# 좌항과 우항이 같은지 비교
print(3 == 3) # 같으므로 True
print(4 == 2) # 다르므로 False
print(3 + 4 == 7) # 같으므로 True
# 좌항과 우항이 다른지 비교
print(1 != 3) # 다르므로 True
# 좌항과 우항이 모두 참인가?
print((3 > 0) and (3 > 5)) # 좌항(3 > 0) 은 참이지만 우항(3 > 5) 는 거짓이므로 False 
# 좌항 또는 우항 중 하나라도 참인가?
print((3 > 0) or (3 > 5)) # 좌항(3 > 0) 이 참이므로 우항(3 > 5) 이 거짓이라도 True
# 좌항과 우항이 다른지 비교한 결과의 반대
print(not(1 != 3)) # 1과 3은 다르므로 True 인데, True 의 반대이므로 False
print(5 > 4 > 3) # (5 > 4) 도 참이며 (4 > 3) 도 참이므로 True
print(5 > 4 > 7) # (5 > 4) 는 참이지만 (4 > 7) 은 거짓이므로 False '''

# [파이썬 기본편] 3-2.간단한수식
''' number = 16
number *= 2 # number = number * 2 와 동일
print(number) # 36
number /= 2 # number = number / 2 와 동일
print(number) # 18
number -= 2 # number = number - 2 와 동일
print(number) # 16
number %= 2 # number = number % 2 와 동일
print(number) # 0 '''

# [파이썬 기본편] 3-3.숫자처리함수
''' from math import *
print(abs(-5)) # -5 의 절대값 = 5
print(pow(4, 2)) # 4의 2제곱 = 4 * 4 = 16
print(max(5, 12)) # 5 와 12 중 큰 값 = 12
print(min(5, 12)) # 5 와 12 중 작은 값 = 5
print(round(3.14)) # 3.14 의 반올림 = 3
print(round(4.99)) # 4.99 의 반올림 = 5
print(floor(4.99)) # 4.99 의 내림 = 4
print(ceil(3.14)) # 3.14 의 올림 = 4
print(sqrt(16)) # 16 의 제곱근 = 4
import math # math 모듈을 가져다 쓰겠다는 의미
print(math.floor(4.99)) # math. 과 함께 사용
print(math.ceil(3.14))
print(math.sqrt(16)) '''

# [파이썬 기본편] 3-4.랜덤함수
''' from random import * # random 모듈에서 모든 것들을 가져다 쓰겠다는 의미
print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 이상 10 미만의 임의의 정수 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하 (11 미만) 의 임의의 정수 값 생성
print(int(random() * 45) + 1) # 1 이상 46 미만의 임의의 정수 값 생성
print(randrange(1, 46)) # 1 이상 46 미만의 임의의 정수 값 생성
print(randint(1, 45)) # 1 이상 45 이하(45를 포함해요!!)의 임의의 정수 값 생성 '''

# [파이썬 기본편] 4-1.문자열
''' sentence1 = '나는 소년입니다'
print(sentence1) # 나는 소년입니다
sentence2 = "파이썬은 쉬워요"
print(sentence2) # 파이썬은 쉬워요
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3) # 큰 따옴표 대신 작은 따옴표 3개씩으로 감싸도 돼요 '''

# [파이썬 기본편] 4-2.슬라이싱
''' jumin = "990120-1234567"
print("성별 : " + jumin[7]) # 성별 : 1
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1) : 99 년
print("월 : " + jumin[2:4]) # 2 부터 4 직전까지 (2, 3) : 01 월
print("일 : " + jumin[4:6]) # 4 부터 6 직전까지 (4, 5) : 20 일
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 -> jumin[0:6] 과 동일
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지 -> jumin[7:14] 와 동일
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째 위치로부터 끝까지 '''

# [파이썬 기본편] 4-3.문자열처리함수
''' python = "Python is Amazing"
print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True : 0 번째 인덱스의 값이 대문자인지 확인
print(len(python)) # 17 : 띄어쓰기를 포함한 문자열의 전체 길이 (length)
print(python.replace("Python", "Java")) # Java is Amazing
index = python.index("n") # 처음으로 발견된 n 의 인덱스
print(index) # 5 : Python 의 n
index = python.index("n", index + 1) # 6 번째 인덱스 이후에 처음으로 발견된 n 의 인덱스 
print(index) # 15 : Amazing 의 n
find = python.find("n") # 처음으로 발견된 n 의 인덱스
print(find) # 5 : Python 의 n
find = python.find("n", find + 1) # 6 번째 인덱스 이후에 처음으로 발견된 n 의 인덱스 
print(find) # 15 : Amazing 의 n
# print(python.index("Java")) # Java 가 없기 때문에 에러가 발생하며 프로그램 종료
print(python.find("Java")) # Java 가 없으면 -1 을 반환(출력)하며 프로그램 계속 수행
print(python.count("n")) # 2 : 문자열 내에서 n 이 나온 횟수 '''

# [파이썬 기본편] 4-4.문자열포맷
''' print("a" + "b") # ab
print("a", "b") # a b
# 방법 1
print("나는 %d살입니다." % 20) # 나는 20살입니다
print("나는 %s을 좋아합니다." % "파이썬") # 나는 파이썬을 좋아합니다.
print("Apple 은 %c로 시작해요." % "A") # Apple 은 A로 시작해요.
print("나는 %s살입니다." % 20) # 나는 20살입니다 (%s 로도 정수값 표현 가능)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요
# 방법 2
print("나는 {}살입니다.".format(20)) # 나는 20살입니다.
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 나는 빨간색과 파란색을 좋아해요
# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
# 나는 20살이며, 빨간색을 좋아해요
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))
# 나는 20살이며, 빨간색을 좋아해요 (.format 뒤에 순서를 변경해도 괜찮아요)
# 방법 4 (파이썬 버전 3.6 부터 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # 나는 20살이며, 빨간색을 좋아해요. '''

# [파이썬 기본편] 5-1.리스트
''' subway = [10, 20, 30]
print(subway) # [10, 20, 30]
subway = ["유재석", "조세호", "박명수"]
print(subway) # ['유재석', '조세호', '박명수']
# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호")) # 1 (인덱스는 0부터 시작한다는 것, 기억나시죠?)
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']
# 정형돈씨를 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈") # 인덱스 1 위치에 삽입
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # 하하 내림
print(subway) # ['유재석', '정형돈', '조세호', '박명수']
print(subway.pop()) # 박명수 내림
print(subway) # ['유재석', '정형돈', '조세호']
print(subway.pop()) # 조세호 내림
print(subway) # ['유재석', '정형돈']
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석") # 설명을 위해 유재석씨를 맨 뒤에 태울게요
print(subway) # ['유재석', '정형돈', '유재석']
print(subway.count("유재석")) # 유재석씨가 2명이 있네요!
num_list = [5, 2, 4, 3, 1]
num_list.sort() # 정렬
print(num_list) # [1, 2, 3, 4, 5]
num_list.reverse() # 순서 뒤집기
print(num_list) # [5, 4, 3, 2, 1]
# 모두 지우기
num_list.clear()
print(num_list) # []
mix_list = ["조세호", 20, True] # 다양한 자료형을 함께 사용할 수 있어요
print(mix_list) # ['조세호', 20, True]
num_list = [5, 2, 4, 3, 1] # num_list 값 다시 정의
num_list.extend(mix_list) # 리스트 확장
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True] '''

# [파이썬 기본편] 5-2.사전
''' cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3]) # 유재석 -> key 3 에 해당하는 value
print(cabinet[100]) # 김태호 -> key 100 에 해당하는 value
print(cabinet.get(3)) # 유재석 -> key 3 에 해당하는 value
print("hi")
print(cabinet.get(5)) # key 가 5 인 값이 없을 땐 None 반환 후 계속 진행 (hi 출력됨)
print("hi")
print(cabinet.get(5, "사용 가능")) # key 에 해당하는 값이 없는 경우 기본 값을 사용
# 사전 자료형에 값이 있는지 여부 확인
print(3 in cabinet)  # True
print(5 in cabinet)  # False
# key 는 정수형이 아닌 문자열도 가능
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호
# 업데이트 또는 추가
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국" # key 에 해당하는 값이 있는 경우 업데이트
cabinet["C-20"] = "조세호" # key 에 해당하는 값이 없는 경우 신규 추가
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}
# 삭제
del cabinet["A-3"] # key "A-3" 에 해당하는 데이터 삭제
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}
# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])
# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])
# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])
# 전체 삭제
cabinet.clear()
print(cabinet) # {} '''

# [파이썬 기본편] 5-3.튜플
''' menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) # 김종국 20 코딩
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) # 김종국 20 코딩 '''

# [파이썬 기본편] 5-4.세트
''' my_set = {1, 2, 3, 3, 3} # 중복을 허용하지 않으므로 3은 1번만 들어감
print(my_set) # {1, 2, 3}
java = {"유재석", "김태호", "양세형"} # 자바 개발자 집합
python = set(["유재석", "박명수"]) # 파이썬 개발자 집합
# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}
# 합집합 (java 또는 python 을 할 수 있는 개발자)
print(java | python) # {'박명수', '유재석', '김태호', '양세형'}
print(java.union(python)) # {'박명수', '유재석', '김태호', '양세형'}
# 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}
# python 개발자 추가 (기존 개발자 : 박명수, 유재석)
python.add("김태호")
print(python) # {'박명수', '유재석', '김태호'}
# java 개발자 삭제 (기존 개발자 : 유재석, 김태호, 양세형)
java.remove("김태호")
print(java) # {'유재석', '양세형'} '''

# [파이썬 기본편] 5-5.자료구조의 변경
''' menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # menu 의 type 정보 : set
menu = list(menu) # 리스트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : list
menu = tuple(menu) # 튜플 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : tuple
menu = set(menu) # 세트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : set '''

# [파이썬 기본편] 6-1.if
''' weather = input("오늘 날씨는 어때요? ")
temp = int(input("기온은 어때요? "))
# print(weather) # 사용자가 입력한 값 출력 # 주석 처리
if weather == "비" or weather == "눈": # 조건 변경
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")
if 30 <= temp: # 30 도 이상이면
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # 10도 이상 30도 미만이면
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
# 위 비교 문장은 이렇게도 작성 가능합니다.
# elif 0 <= temp < 10:
    print("외투를 챙기세요")
else: # 그 외의 모든 경우 (0도 미만이면)
    print("너무 추워요. 나가지 마세요") '''

# [파이썬 기본편] 6-2.for
''' for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no)) # {0} 위치에는 waiting_no 의 값이 들어가요
for waiting_no in range(5): # 0부터 5직전까지 (0~4)
    print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(1, 6): # 1부터 6직전까지 (1~5)
    print("대기번호 : {0}".format(waiting_no))
starbucks = ["아이언맨", "토르", "아이엠 그루트"] # 손님 리스트
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer)) '''

# [파이썬 기본편] 6-3.while
''' customer = "토르" # 손님
index = 5 # 부르는 횟수, 총 5회
while index >= 1: # 부르는 횟수가 1 이상인 경우에만 반복 실행
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))    
    index -= 1 # 부르는 횟수 감소
    if index == 0: # 5번 모두 불렀다면
        print("커피는 폐기처분되었습니다.") '''

# [파이썬 기본편] 6-4.continue 와 break
''' absent = [2, 5] # 결석한 학생 출석번호
for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
        continue
    print("{0}, 책을 읽어봐".format(student))
absent = [2, 5] # 결석한 학생 출석번호
no_book = [7] # 책을 가져오지 않은 학생 출석번호
for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
        continue
    elif student in no_book: # 책을 가져오지 않았으면 바로 수업 종료 (반복문 탈출)
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student)) '''

# [파이썬 기본편] 6-5.한 줄 for
''' students = [1, 2, 3, 4, 5]
print(students) # [1, 2, 3, 4, 5]
# 한 줄 for 를 이용하여 각 항목에 100 을 더함
students = [i + 100 for i in students]
print(students) # [101, 102, 103, 104, 105]
students = ["Iron man", "Thor", "I am groot"]
print(students) # ["Iron man", "Thor", "I am groot"]
# 한 줄 for 를 이용하여 각 이름의 길이 정보로 변환
students = [len(i) for i in students]
print(students) # [8, 4, 10]
students = ["Iron man", "Thor", "I am groot"]
print(students) # ["Iron man", "Thor", "I am groot"]
# 한 줄 for 를 이용하여 각 이름을 대문자로 변경
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT'] '''

# [파이썬 기본편] 7-1.함수
''' def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account() # 앞에서 정의된 open_account() 함수 호출 '''

# [파이썬 기본편] 7-2.전달값과 반환값
''' def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money # 입금 후 잔액 정보 반환 
balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금
print(balance) # 현재 잔액
def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money # 출금 후 잔액 반환
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance # 기존 잔액 반환       
balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금
# 출금 시도
balance = withdraw(balance, 2000) # 2000원 출금 시도 시 잔액이 부족하므로 실패
balance = withdraw(balance, 500) # 500원 출금 시도 시 성공
print(balance) # 현재 잔액
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 출금 수수료 100원
    return commission, balance - money - commission # 튜플 형식으로 반환
balance = 0 # 최초 잔액
balance = deposit(balance, 1000) # 1000원 입금
# 저녁에 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance)) '''

# [파이썬 기본편] 7-3.기본값
''' def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profile("유재석", 20, "파이썬") # 유재석씨(20세)의 주 사용 언어는 파이썬
profile("김태호", 25, "자바") # 김태호씨(25세)의 주 사용 언어는 자바
def profile(name, age=17, main_lang="파이썬"): # 전달값을 따로 받지 않을때 기본으로 사용할 값
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profile("유재석")
profile("김태호") '''

# [파이썬 기본편] 7-4.키워드 인자
''' def profile(name, age, main_lang): # 키워드 인자 : name, age, main_lang
    print(name, age, main_lang)
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호") '''

# [파이썬 기본편] 7-5.가변인자
''' def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 문장 출력 후 줄바꿈 대신 띄어쓰기
    print(lang1, lang2, lang3, lang4, lang5)
profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
def profile(name, age, *language): # 언어 정보를 전달하고 싶은 갯수 만큼 전달 가능    
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # print(type(language)) # tuple
    for lang in language:
        print(lang, end=" ") # 언어들을 모두 한 줄에 표시
    print() # 줄바꿈 목적
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript") # JavaScript 추가
profile("김태호", 25, "Kotlin", "Swift") '''

# [파이썬 기본편] 7-6.지역변수와 전역변수
''' gun = 10
def checkpoint(soldiers):
    global gun # 전역공간에 있는 gun 이라는 변수를 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))
gun = 10
def checkpoint_ret(gun, soldiers): # 전체 총 수와 군인 수를 전달받음
    gun = gun - soldiers # 전달받은 gun 을 사용
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2) # gun 값을 함수에 전달
print("남은 총 : {0}".format(gun)) '''

# [파이썬 기본편] 8-1.표준입출력
''' print("Python", "Java")
print("Python" + "Java")
print("Python", "Java", sep=",") # 값들을 콤마(,) 로 구분
print("Python", "Java", "JavaScript", sep=" vs ") # 값들을 " vs " 로 구분
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")
import sys # sys 모듈을 가져와서 사용하겠다는 의미
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # key, value
    print(subject, score)
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
for num in range(1, 21): # 1~20 까지의 숫자
    print("대기번호 : " + str(num))
for num in range(1, 21): # 1~20 까지의 숫자
    print("대기번호 : " + str(num).zfill(3)) '''

# [파이썬 기본편] 8-2.다양한 출력포맷
''' print("{0}".format(500)) # {0} 위치에 500 값 출력
print("{0: >10}".format(500)) # 빈 자리는 비워두기, 우측 정렬, 10 칸의 공간 확보
print("{0: >+10}".format(500)) # 빈 자리는 비워두기, 우측 정렬, + 기호, 10 칸의 공간 확보
print("{0: >+10}".format(-500))
print("{0:_<10}".format(500)) # 빈 자리는 _ 로, 좌측 정렬, 10 칸의 공간 확보
print("{0:,}".format(100000000000)) # 3자리 마다 콤마 찍어주기
print("{0:+,}".format(100000000000)) # + 기호, 3자리 마다 콤마 찍어주기
print("{0:+,}".format(-100000000000))
# 빈 자리는 ^ 로, 좌측 정렬, + 기호, 30 칸의 공간 확보, 3자리 마다 콤마 찍어주기
print("{0:^<+30,}".format(100000000000))
print("{0:f}".format(5/3)) # 실수 값 출력
print("{0:.2f}".format(5/3)) # 소수점 둘째자리까지 출력 '''

# [파이썬 기본편] 8-3.파일입출력
''' score_file = open("score.txt", "w", encoding="utf8") # score.txt 파일을 쓰기("w") 모드로 열기
print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
score_file.close() # score.txt 파일 닫기
score_file = open("score.txt", "a", encoding="utf8") # score.txt 파일을 쓰기("a") 모드로 열기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # write 는 줄바꿈 안해주기 때문에 탈출문자(\n)로 줄바꿈 추가
score_file.close()
score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기("r") 모드로 열기
print(score_file.read()) # 파일 전체 읽어오기
score_file.close()
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄바꿈 중복을 방지하기 위해 end="" 처리
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 더 이상 읽어올 내용이 없으면?
        break # 반복문 탈출
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리   
score_file.close()
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리    
score_file.close() '''

# [파이썬 기본편] 8-4.pickle
''' import pickle # pickle 모듈 가져다 쓰기
profile_file = open("profile.pickle", "wb") # 바이너리(binary) 형태로 저장
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 데이터를 file 에 저장
profile_file.close()
profile_file = open("profile.pickle", "rb") # 읽을 때에도 바이너리(binary) 명시
profile = pickle.load(profile_file) # file 에 있는 정보를 불러와서 profile 에 저장
print(profile)
profile_file.close() '''

# [파이썬 기본편] 8-5.with
''' import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read()) '''

# [파이썬 기본편] 9-1.클래스
''' class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35) '''

# [파이썬 기본편] 9-2.__init__
''' class Unit:
    def __init__(self, name, hp, damage): # 3개의 전달값
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35) '''
    
# [파이썬 기본편] 9-3.멤버변수
''' class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5) # 체력 80, 공격력 5
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 멤버변수 접근
# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.cloaking = True # 빼앗은 레이스만을 위한 특별한 멤버변수 정의
if wraith2.cloaking == True: # 클로킹 상태라면?
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
# 에러 발생
# if wraith1.cloaking == True: # 우리가 만든 레이스 클로킹 여부
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name)) '''

# [파이썬 기본편] 9-4.메소드
''' class AttackUnit: # 공격 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, location): # 공격 방향
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
    def damaged(self, damage): # damage 만큼 유닛 피해
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
        self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
        if self.hp <= 0: # 남은 체력이 0 이하이면?
            print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
# 파이어뱃 : 공격 유닛, 화염방사기. 
firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
firebat1.attack("5시") # 5시 방향으로 공격 명령
# 공격 2번 받는다고 가정
firebat1.damaged(25) # 남은 체력 25
firebat1.damaged(25) # 남은 채력 0 '''

# [파이썬 기본편] 9-5.상속
# 일반 유닛
''' class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name)) '''

# [파이썬 기본편] 9-6.다중상속
''' # 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):  # 공중 이동 속도
        self.flying_speed = flying_speed
    def fly(self, name, location):  # 유닛 이름, 이동 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):  # 이름, 체력, 공격력, 공중 이동 속도
        AttackUnit.__init__(self, name, hp, damage)  # 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed)  # 공중 이동 속도
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)  # 이름, 체력, 공격력, 공중 이동 속도
valkyrie.fly(valkyrie.name, "3시")  # 3시 방향으로 발키리를 이동 '''

# [파이썬 기본편] 9-7.메소드 오버라이딩
# 일반 유닛
''' class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20) # 지상 speed 10
# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") # 오버라이딩된 move() 호출 '''

# [파이썬 기본편] 9-8.pass
# 일반 유닛
''' class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 체력 500, 생성 위치 7시
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass
game_start()
game_over() '''

# [파이썬 기본편] 9-9.super
''' class Unit:
    def __init__(self):
        print("Unit 생성자")
class Flyable:
    def __init__(self):
        print("Flyable 생성자")       
# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit): # 순서 변경
    def __init__(self):
        # super().__init__()
        Unit.__init__(self) # Unit 클래스 생성자 호출
        Flyable.__init__(self) # Flyable 클래스 생성자 호출
# 드랍쉽
dropship = FlyableUnit() '''

# [파이썬 기본편] 9-10.스타크래프트 프로젝트 전반전
# 일반 유닛
''' class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) # 출력문 추가
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
    def damaged(self, damage): # AttackUnit 에서 Unit 으로 이동
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    siege_developed = False # 시즈모드 개발여부 (클래스 변수)
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
        self.siege_mode = False # 시즈모드 (해제 상태)
    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return
        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배로 증가
            self.siege_mode = True # 시즈 모드 설정
        # 현재 시즈모드일 때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시즈 모드 해제
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        self.fly(self.name, location)
# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
        self.cloaked = False # 클로킹 모드 (해제 상태)
    # 클로킹 모드
    def cloaking(self):
        # 현재 클로킹 모드일 때
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 클로킹 모드가 아닐 때
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.cloaked = True '''

# [파이썬 기본편] 9-11.스타크래프트 프로젝트 후반전
# 일반 유닛
''' class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    siege_developed = False # 시즈모드 개발여부 (클래스 변수)
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
        self.siege_mode = False # 시즈모드 (해제 상태)
    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return
        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배로 증가
            self.siege_mode = True # 시즈 모드 설정
        # 현재 시즈모드일 때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시즈 모드 해제
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        self.fly(self.name, location)
# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
        self.cloaked = False # 클로킹 모드 (해제 상태)
    # 클로킹 모드
    def cloaking(self):
        # 현재 클로킹 모드일 때
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 클로킹 모드가 아닐 때
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.cloaked = True
# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
# 게임 종료
def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
# 실제 게임 진행
game_start()
# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
# 탱크 2기 생성
t1 = Tank()
t2 = Tank()
# 레이스 1기 생성
w1 = Wraith()
# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t1)
attack_units.append(w1)
# 전군 이동
for unit in attack_units:
    unit.move("1시")
# 탱크 시즈모드 개발
Tank.siege_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # Marine 의 인스턴스이면 스팀팩
        unit.stimpack()
    elif isinstance(unit, Tank): # Tank 의 인스턴스이면 시즈모드
        unit.set_siege_mode()
    elif isinstance(unit, Wraith): # Wraith 의 인스턴스이면 클로킹
        unit.cloaking()
# 전군 공격
for unit in attack_units:
    unit.attack("1시")
# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)
# 게임 종료
game_over() '''

# [파이썬 기본편] 10-1.예외처리
''' try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err) '''

# [파이썬 기본편] 10-2.에러 발생시키기
''' try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.") '''

# [파이썬 기본편] 10-3.사용자 정의 예외처리
''' class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return "[에러코드 001] " + self.msg # 에러 메시지 가공
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 자세한 에러 메시지
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err) # 에러 메시지 출력 '''

# [파이썬 기본편] 10-4.finally
''' class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: # 에러 발생 여부 상관 없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.") '''

# [파이썬 기본편] 11-1.모듈
''' from STUDY2_MODULE import *
price(3)
price_morning(4)
price_soldier(5) '''

# [파이썬 기본편] 11-2.패키지
''' from STUDY2_PACKAGE import vietnam # travel 패키지에서 vietnam 모듈 가져오기
from STUDY2_PACKAGE import Thailand # travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
trip_to = vietnam.VietnamPackage() # travel. 은 생략
trip_to.detail()
trip_to = Thailand.ThailandPackage() # travel.thailand. 는 생략
trip_to.detail() '''

# [파이썬 기본편] 11-3.__all__
''' from STUDY2_PACKAGE import *
# trip_to = vietnam.VietnamPackage()
trip_to = vietnam.VietnamPackage() # travel. 은 생략
trip_to.detail()
trip_to = Thailand.ThailandPackage() # 태국
trip_to.detail() '''

# [파이썬 기본편] 11-5.패키지, 모듈 위치
''' import inspect
import random
from STUDY2.PACKAGE import *
print(inspect.getfile(random)) # random 모듈의 위치
print(inspect.getfile(Thailand)) # thailand 모듈의 위치 '''

# [파이썬 기본편] 11-6.pip install
''' from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify()) '''

# [파이썬 기본편] 11-7.내장함수
''' import random # random 모듈 가져다 쓰기
import pickle # pickle 모듈 가져다 쓰기
print(dir())
print(dir())
print(dir())
print(dir(random))
lst = [1, 2, 3]
print(dir(lst))
name = "Jim"
print(dir(name)) '''

# [파이썬 기본편] 11-8.외장함수
''' import glob
import os
import time
import datetime
print(glob.glob("*.py")) # 확장자가 py 인 모든 파일
print(os.getcwd()) # 현재 디렉토리
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후 '''