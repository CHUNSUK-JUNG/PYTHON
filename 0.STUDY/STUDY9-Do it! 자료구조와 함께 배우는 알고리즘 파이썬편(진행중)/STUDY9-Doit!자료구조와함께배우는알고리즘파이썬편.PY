# 출처 [Do it! 자료구조와 함께 배우는 알고리즘 파이썬편]


# [CHAP01]

# [Do it! 실습 1-1] 세 정수를 입력받아 최댓값 구하기
# print('세 정수의 최댓값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.: '))
# b = int(input('정수 b의 값을 입력하세요.: '))
# c = int(input('정수 c의 값을 입력하세요.: '))
# maximum = a
# if b > maximum: maximum = b
# if c > maximum: maximum = c
# print(f'최댓값은 {maximum}입니다.')

# [Do it! 실습 1-2] # 세 정수의 최댓값을 구하기
# def max3(a, b, c):
#     """a, b, c의 최댓값을 구하여 반환"""
#     maximum = a
#     if b > maximum: maximum = b
#     if c > maximum: maximum = c
#     return maximum  # 최댓값 반환
# print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')   # [A] a > b > c
# print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')   # [B] a > b = c
# print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')   # [C] a > c > b
# print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')   # [D] a = c > b
# print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')   # [E] c > a > b
# print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')   # [F] a = b > c
# print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')   # [G] a = b = c
# print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')   # [H] c > a = b
# print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')   # [I] b > a > c
# print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')   # [J] b > a = c
# print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')   # [K] b > c > a
# print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')   # [L] b = c > a
# print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')   # [M] c > b > a

# [Do it! 실습 1-3] 입력받은 정숫값의 부호(양수, 음수, 0) 출력하기
# n = int(input('정수를 입력하세요.: '))
# if n > 0:
#     print('이 수는 양수입니다.')
# elif n < 0:
#     print('이 수는 음수입니다.')
# else:
#     print('이 수는 0입니다.')

# [Do it! 실습 1-4] 3개로 분기하는 조건문
# n = int(input('정수를 입력하세요.: '))
# if n == 1:
#     print('A')
# elif n == 2:
#     print('B')
# else:
#     print('C')

# [Do it! 실습 1-5] 4개로 분기하는 조건문
# n = int(input('정수를 입력하세요.: '))
# if n == 1:
#     print('A')
# elif n == 2:
#     print('B')
# elif n == 3:
#     print('C')

# [Do it! 실습 1-6] 실습 1-5의 원래 모습
# n = int(input('정수를 입력하세요.: '))
# if n == 1:
#     print('A')
# elif n == 2:
#     print('B')
# elif n == 3:
#     print('C')
# else :
#     pass

# [Do it! 실습 1-7] 1부터 n까지 정수의 합 구하기 1(while 문)
# print('1부터 n까지 정수의 합을 구합니다.')
# n = int(input('n값을 입력하세요.: '))
# sum = 0
# i = 1
# while i <= n:  # i가 n보다 작거나 같은 동안 반복
#     sum += i   # sum에 i를 더함
#     i += 1     # i에 1을 더함
# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
# print(f'i값은 {i}입니다.')

# [Do it! 실습 1-8] 1부터 n까지의 합 구하기 2(for 문)
# print('1부터 n까지의 합을 구합니다.')
# n = int(input('n값을 입력하세요.: '))
# sum = 0
# for i in range(1, n + 1):
#     sum += i  # sum에 i를 더함
# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# [Do it! 실습 1-9] a부터 b까지 정수의 합 구하기(for 문)
# print('a부터 b까지의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요.: '))
# b = int(input('정수 b를 입력하세요.: '))
# if a > b:
#     a, b = b, a  # a와 b를 오름차순으로 정렬
# sum = 0
# for i in range(a, b + 1):
#     sum += i  # sum에 i를 더함
# print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')

# [Do it! 실습 1-10] a부터 b까지 정수의 합 구하기 1
# print('a부터 b까지의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요.: '))
# b = int(input('정수 b를 입력하세요.: '))
# if a > b:
#     a, b = b, a
# sum = 0
# for i in range(a, b + 1):  # b - a번 반복
#     if i < b:              # i가 b보다 작으면 합을 구하는 과정을 출력
#         print(f'{i} + ', end='')
#     else:                  # i가 b보다 크거나 같으면 최종값 출력을 위해 i =를 출력
#         print(f'{i} = ', end='')
#     sum += i               # sum에 i를 더함
# print(sum)

# [Do it! 실습 1-10] 1부터 n까지의 합 구하기 3(가우스 덧셈 방법)
# print('1부터 n까지의 합을 구합니다.')
# n = int(input('n값을 입력하세요.: '))
# sum = n * (n + 1) // 2
# print(f'1부터 {n}까지의 합은 {sum}입니다.')

# [Do it! 실습 1-11] a부터 b까지 정수의 합 구하기 2
# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요.: '))
# b = int(input('정수 b를 입력하세요.: '))
# if a > b :
#     a, b = b, a
# sum = 0
# for i in range(a, b):
#     print(f'{i} + ', end='')
#     sum += i  # sum에 i를 더함
# print(f'{b} = ', end ='')
# sum += b      # sum에 b를 더함
# print(sum)

# [Do it! 실습 1-12] +와 -를 번갈아 출력하기 1
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))
# for i in range(n):          # 반복 n번
#     if i % 2:                 
#         print('-', end='')  # 홀수인 경우 - 출력
#     else:
#         print('+', end='')  # 짝수인 경우 + 출력
# print()

# [Do it! 실습 1-12] +와 -를 번갈아 출력하기 1(for 문 수정)
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))
# for i in range(1, n + 1):  
#     if i % 2:              # 홀수
#         print('+', end='')
#     else:                  # 짝수
#         print('-', end='')
# print()

# [Do it! 실습 1-13] +와 -를 번갈아 출력하기 2(range()함수 수정)
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))
# for _ in range(1, n // 2 + 1):
#     print('+-', end='')  # n // 2개의 +-를 출력
# if n % 2:
#     print('+', end='')  # n이 홀수일 때만 +를 출력

# [Do it! 실습 1-14] *를 n개 출력하되 w개마다 줄바꿈하기 1
# print('*를 출력합니다.')
# n = int(input('몇 개를 출력할까요? : '))
# w = int(input('몇 개마다 줄바꿈할까요? : '))
# for i in range(n):      # n번 반복
#     print('*', end='')
#     if i % w == w - 1:  # n번 판단
#         print()         # 줄바꿈
# if n % w:
#     print()             # 줄바꿈

# [Do it! 실습 1-14] *를 n개 출력하되 w개마다 줄바꿈하기 2
# print('*를 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))
# w = int(input('몇 개마다 줄바꿈할까요?: '))
# for _ in range(n // w):  # 반복 n // w번 반복
#     print('*' * w)
# rest = n % w
# if rest:
#     print('*' * rest)  # if 문 1번 판단

# [Do it! 실습 1-16] 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)
# print('1부터 n까지 정수의 합을 구합니다.')
# while True:
#     n = int(input('n값을 입력하세요.: '))
#     if n > 0:
#         break  # n이 0보다 커질 때까지 반복
# sum = 0
# i = 1
# for i in range(1, n + 1):
#     sum += i  # sum에 i를 더함
#     i += 1    # i에 1을 더함
# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# [Do it! 실습 1-17] 가로 세로가 정수이고 넓이가 area인 직사각형에서 변의 길이를 나열하기
# area = int(input('직사각형의 넓이를 입력하세요.: '))
# for i in range(1, area + 1):  # 1부터 사각형의 넓이 계산
#     if i * i > area: break
#     if area % i: continue
#     print(f'{i} × {area // i}')

# [Do it! 실습 1-18] 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)
# import random
# n = int(input('난수의 개수를 입력하세요.: '))
# for _ in range(n):
#     r = random.randint(10, 99)
#     print(r, end=' ')
#     if r == 13:
#         print('\n프로그램을 중단합니다.')
#         break
# else :
#     print('\n난수 생성을 종료합니다.')

# [Do it! 실습 1-19] 1~12까지 8을 건너뛰고 출력하기 1
# for i in range(1, 13):
#     if i == 8:
#         continue
#     print(i, end=' ')
# print()

# [Do it! 실습 1-20] 1부터 12까지 8을 건너 뛰고 출력하기 2
# for i in list(range(1, 8)) + list(range(9, 13)):
#     print(i, end=' ')
# print()

# [Do it! 실습 1-21] 구구단 곱셈표 출력하기
# print('-' * 27)
# for i in range(1, 10):      # 행 루프
#     for j in range(1, 10):  # 열 루프
#         print(f'{i * j : 3}', end='')
#     print()                 # 행 변경
# print('-' * 27)

# [Do it! 실습 1-22] 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기
# print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변의 길이를 입력하세요.: '))
# for i in range(n):          # 행 루프
#     for j in range(i + 1):  # 열 루프
#         print('*', end='')
#     print()

# [Do it! 실습 1-22] 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기(언더스코어 사용)
# print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변의 길이를 입력하세요.: '))
# for i in range(n):          # 행 루프
#     for _ in range(i + 1):  # 열 루프
#         print('*', end='')
#     print()

 # [Do it! 실습 1-23] 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기
# print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변 길이를 입력하세요.: '))
# for i in range(n):              # 행 루프
#     for _ in range(n - i - 1):  # 열 루프(공백을 출력)
#         print(' ', end='')
#     for _ in range(i + 1):
#         print('*', end='')      # 열 루프(*을 출력)
#     print()

# [Do it! 실습 1C-1] 이름을 입력받아 인사하기
# print('이름을 입력하세요.: ', end = '')
# name = input()
# print(f'안녕하세요? {name} 님.')

# [Do it! 실습 1C-1] 이름을 입력 받아 인사합니다(실습 1C-1 수정).
# name = input( '이름을 입력하세요.: ')
# print(f'안녕하세요? {name} 님.')

# [Do it! 실습 1C-2] 세 정숫값을 입력받아 중앙값을 구하기 1
# def med3(a, b, c):
#     """a, b, c의 중앙값을 구하여 반환"""
#     if a >= b: 
#         if b >= c: 
#             return b
#         elif a <= c: 
#             return a
#         else:
#             return c
#     elif a > c: 
#         return a
#     elif b > c: 
#         return c
#     else:
#         return b
# print('세 정수의 중앙값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.: '))
# b = int(input('정수 b의 값을 입력하세요.: '))
# c = int(input('정수 c의 값을 입력하세요.: '))
# print(f'중앙값은 {med3(a, b, c)}입니다.')

# [Do it! 실습 1C-2] 세 정숫값을 입력받아 중앙값을 구하기 2
# def med3(a, b, c):
#     """a, b, c의 중앙값을 구하여 반환(다른 방법)"""
#     if (b >= a and c <= a) or (b <= a and c >= a):
#         return a
#     elif (a > b and c < b) or (a < b and c > b):
#         return b
#     return c
# print('세 정수의 중앙값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.: '))
# b = int(input('정수 b의 값을 입력하세요.: '))
# c = int(input('정수 c의 값을 입력하세요.: '))
# print(f'중앙값은 {med3(a, b, c)}입니다.')

# [Do it! 실습 1C-3] 2자리 양수(10 ~ 99) 입력받기
# print('2자리 양수를 입력하세요.')
# while True:
#     no = int(input('값을 입력하세요.: '))
#     if no >= 10 and no <= 99:
#         break
# print(f'입력받은 양수는 {no}입니다.')

# [Do it! 실습 1C-3] 2자리 양수(10 ~ 99) 입력받기 2
# print('2자리 양수를 입력하세요.')
# while True:
#     no = int(input('값을 입력하세요.: '))
#     if 10 <= no <= 99:
#         break
# print(f'입력받은 양수는 {no}입니다.')

# [Do it! 실습 1C-3] 2자리 양수(10~99) 입력받기 3
# print('2자리 양수를 입력하세요.')
# while True:
#     no = int(input('값을 입력하세요.: '))
#     if not(no < 10 or no > 99):
#         break
# print(f'입력받은 양수는 {no}입니다.')

# [Do it! 실습 1C-4] 함수의 내부·외부에서 정의한 변수와 객체의 식별 번호를 출력
# n = 1      # 전역 변수(함수 내부·외부에서 사용)
# def put_id():
#     x = 1  # 지역 변수(함수 내부에서만 사용)
#     print(f'id(x) = {id(x)}')
# print(f'id(1) = {id(1)}')
# print(f'id(n) = {id(n)}')
# put_id()

# [Do it! 실습 1C-5] 1부터 100까지 반복하여 출력
# for i in range(1, 101):
#     print(f'i = {i:3}   id({i}) = {id(i)}')


# [CHAP02]

# [리스트와 튜플 생성]
# list01 = []                 # [] 빈 리스트 생성
# list02 = [1, 2, 3]          # [1, 2, 3]
# list03 = ['A', 'B', 'C', ]  # ['A', 'B', 'C'] 맨 마지막 원소에 쉼표를 써도 됨
# list04 = list()           # [] 빈 리스트 생성
# list05 = list('ABC')      # ['A', 'B', 'C'] 각각의 문자로부터 원소 생성
# list06 = list([1, 2, 3])  # [1, 2, 3] 리스트로부터 원소 생성
# list07 = list((1, 2, 3))  # [1, 2, 3] 튜플로부터 원소 생성
# list08 = list({1, 2, 3})  # [1, 2, 3] 집합으로부터 원소 생성
# list09 = list(range(7))         # [0, 1, 2, 3, 4, 5, 6]
# list10 = list(range(3, 8))      # [3, 4, 5, 6, 7]
# list11 = list(range(3, 13, 2))  # [3, 5, 7, 9, 11]
# # 원소 수가 5이고 모든 원소값이 없는 리스트를 생성
# list12 = [None] * 5  # [None, None, None, None, None]
# tuple01 = ()              # ()
# tuple02 = 1,              # (1,)
# tuple03 = (1,)            # (1,)
# tuple04 = 1, 2, 3         # (1, 2, 3)
# tuple05 = 1, 2, 3,        # (1, 2, 3)
# tuple06 = (1, 2, 3)       # (1, 2, 3)
# tuple07 = (1, 2, 3, )     # (1, 2, 3)
# tuple08 = 'A', 'B', 'C',  # ('A', 'B', 'C')
# tuple09 = tuple()           # () 빈 튜플 생성
# tuple10 = tuple('ABC')      # ('A', 'B', 'C') 문자열의 각 문자로부터 원소를 생성
# tuple11 = tuple([1, 2, 3])  # (1, 2, 3) 리스트로부터 원소 생성
# tuple12 = tuple({1, 2, 3})  # (1, 2, 3) 집합으로부터 원소 생성
# tuple13 = tuple(range(7))         # (0, 1, 2, 3, 4, 5, 6)
# tuple14 = tuple(range(3, 8))      # (3, 4, 5, 6, 7)
# tuple15 = tuple(range(3, 13, 2))  # (3, 5, 7, 9, 11)
# print('list01 =', list01)
# print('list02 =', list02)
# print('list03 =', list03)
# print('list04 =', list04)
# print('list05 =', list05)
# print('list06 =', list06)
# print('list07 =', list07)
# print('list08 =', list08)
# print('list09 =', list09)
# print('list10 =', list10)
# print('list11 =', list11)
# print('list12 =', list12)
# print('tupe01 =', tuple01)
# print('tupe02 =', tuple02)
# print('tupe03 =', tuple03)
# print('tupe04 =', tuple04)
# print('tupe05 =', tuple05)
# print('tupe06 =', tuple06)
# print('tupe07 =', tuple07)
# print('tupe08 =', tuple08)
# print('tupe09 =', tuple09)
# print('tupe10 =', tuple10)
# print('tupe11 =', tuple11)
# print('tupe12 =', tuple12)
# print('tupe13 =', tuple13)
# print('tupe14 =', tuple14)
# print('tupe15 =', tuple15)

# 튜플의 모든 원소를 ​​스캔하기(원소 수를 미리 파악)
# x = ('John', 'George', 'Paul', 'Ringo')
# for i in range(len(x)):
#     print(f'x[{i}] = {x[i]}')

# 튜플의 모든 원소를 ​​enumerate 함수로 스캔하기
# x = ('John', 'George', 'Paul', 'Ringo')
# for i, name in enumerate(x):
#     print(f'x[{i}] = {name}')

# 튜플의 모든 원소를 ​​enumerate 함수로 스캔하기(1부터 카운트)
# x = ('John', 'George', 'Paul', 'Ringo')
# for i, name in enumerate(x, 1):
#     print(f'{i} 번째 = {name}')

# 튜플의 모든 원소를 ​​스캔하기(인덱스 값을 사용하지 않음)
# x = ('John', 'George', 'Paul', 'Ringo')
# for i in x:
#     print(i)

# [Do it! 실습 2-1] 학생 5명의 점수를 입력받아 합계와 평균을 출력하기
# print('학생 그룹 점수의 합계와 평균을 구합니다.')
# score1 = int(input('1번 학생의 점수를 입력하세요.: '))
# score2 = int(input('2번 학생의 점수를 입력하세요.: '))
# score3 = int(input('3번 학생의 점수를 입력하세요.: '))
# score4 = int(input('4번 학생의 점수를 입력하세요.: '))
# score5 = int(input('5번 학생의 점수를 입력하세요.: '))
# total = 0
# total += score1
# total += score2
# total += score3
# total += score4
# total += score5
# print(f'합계는 {total}점입니다.')
# print(f'평균은 {total / 5}점입니다.')

# [Do it! 실습 2-2] 시퀀스 원소의 최댓값 출력하기
# from typing import Any, Sequence
# def max_of(a: Sequence) -> Any:
#     """시퀀스형 a 요소의 최댓값을 반환"""
#     maximum = a[0]
#     for i in range(1, len(a)):
#          if a[i] > maximum: 
#             maximum = a[i]
#     return maximum
# if __name__ == '__main__':
#     print('배열의 최댓값을 구합니다.')
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num    # 원소 수가 num인 리스트를 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]를 입력하세요.: '))
#     print(f'최댓값은 {max_of(x)}입니다.')

# [Do it! 실습 2-3] 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)
# from max import max_of
# print('배열의 최댓값을 구합니다.')
# print('주의: "End"를 입력하면 종료합니다.')
# number = 0
# x = []                  # 빈 리스트
# while True:
#     s = input(f'x[{number}]를 입력하세요.: ')
#     if s == 'End':
#         break
#     x.append(int(s))    # 배열의 끝에 추가
#     number += 1
# print(f'{number}개를 입력했습니다.')
# print(f'최댓값은 {max_of(x)}입니다.')

# [Do it! 실습 2-4] 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)
# import random
# from max import max_of
# print('난수의 최댓값을 구합니다.')
# num = int(input('난수의 개수를 입력하세요.: '))
# lo = int(input('난수의 최솟값을 입력하세요.: '))
# hi = int(input('난수의 최댓값을 입력하세요.: '))
# x = [None] * num        # 원소 수 num인 리스트를 생성
# for i in range(num):
#     x[i] = random.randint(lo, hi)
# print(f'{(x)}')
# print(f'이 가운데 최댓값은 {max_of(x)}입니다.')

# [Do it! 실습 2-5] 배열 요소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)
# from max import max_of
# t = (4, 7, 5.6, 2, 3.14, 1)
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']
# print(f'{t}의 최댓값은 {max_of(t)}입니다.')
# print(f'{s}의 최댓값은 {max_of(s)}입니다.')
# print(f'{a}의 최댓값은 {max_of(a)}입니다.')

# [Do it! 실습 2-6] 뮤터블 시퀀스 원소를 역순으로 정렬
# from typing import Any, MutableSequence
# def reverse_array(a: MutableSequence) -> None:
#     """뮤터블 시퀀스형 a의 원소를 역순으로 정렬"""
#     n = len(a)
#     for i in range(n // 2):
#          a[i], a[n - i - 1] = a[n - i - 1], a[i]
# if __name__ == '__main__':
#     print('배열 원소를 역순으로 정렬합니다.')
#     nx = int(input('원소 수를 입력하세요.: '))
#     x = [None] * nx   # 원소 수가 nx인 리스트를 생성
#     for i in range(nx):
#         x[i] = int(input(f'x[{i}] : '))
#     reverse_array(x)  # x를 역순으로 정렬
#     print('배열 원소를 역순으로 정렬했습니다.')
#     for i in range(nx):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 2-6] 뮤터블 시퀀스 원소를 역순으로 정렬(n을 사용하지 않음)
# from typing import Any, MutableSequence
# def reverse_array(a: MutableSequence) -> None:
#     """뮤터블 시퀀스형 a의 원소를 역순으로 정렬"""
#     for i in range(len(a) // 2):
#          a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
# if __name__ == '__main__':
#     print('배열 원소를 역순으로 정렬합니다.')
#     nx = int(input('원소 수를 입력하세요.: '))
#     x = [None] * nx   # 원소 수가 nx인 리스트를 생성
#     for i in range(nx):
#         x[i] = int(input(f'x[{i}]：'))
#     reverse_array(x)  # x를 역순으로 정렬
#     print('배열 원소를 역순으로 정렬했습니다.')
#     for i in range(nx):
#         print(f'x[{i}]＝{x[i]}')

# Do it! 실습 2-7 [A] 10진수 정수값을 입력받아 2~36진수로 변환하여 출력하기
# def card_conv(x: int, r: int) -> str:
#     """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
#     d =  ''  # 변환 뒤 문자열
#     dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     n = len(str(x))  # 변환하기 전의 자릿수
#     print(f'{r:2} | {x:{n}d}')
#     while x > 0:
#         print('   +' + (n + 2) * '-')
#         if x // r:
#             print(f'{r:2} | {x // r:{n}d} … {x % r}')
#         else:
#             print(f'     {x // r:{n}d} … {x % r}')
#         d += dchar [x % r]  # 해당하는 문자를 꺼내 결합
#         x //= r
#     return d[::-1]  # 역순으로 반환

# Do it! 실습 2-7 [B]
# if __name__ == '__main__':
#     print('10진수를 n진수로 변환합니다.')
#     while True:
#         while True :  # 음이 아닌 정수를 입력받음
#             no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
#             if no > 0:
#                 break
#         while True :  # 2~36진수의 정수값을 입력받음
#             cd = int(input('어떤 진수로 변환할까요?(2-36의 정수 입력): '))
#             if 2 <=  cd <=  36:
#                 break
#         print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')
#         retry = input( "한 번 더 변환할까요?(Y ... 예/N ... 아니오): ")
#         if retry in {'N', 'n'}:
#            break

# [Do it! 실습 2-8] 1,000 이하의 소수를 나열하기
# counter = 0  # 나눗셈 횟수
# for n in range(2, 1001):
#     for i in range(2, n):
#         counter += 1
#         if n % i == 0 :     # 나누어 떨어지면 소수가 아님
#             break           # 반복은 더 이상 불필요하여 중단
#     else:                   # 끝까지 나누어 떨어지지 않으면 다음을 수행
#         print(n)
# print(f'나눗셈을 실행한 횟수: {counter}')

# [Do it! 실습 2-9] 1,000 이하의 소수를 나열하기(알고리즘 개선 1)
# counter = 0           # 나눗셈 횟수
# ptr = 0               # 이미 찾은 소수의 개수
# prime = [None] * 500  # 소수를 저장하는 배열
# prime[ptr] = 2        # 2는 소수이므로 초깃값으로 지정
# ptr += 1
# for n in range(3, 1001, 2):  # 홀수만을 대상으로 설정
#     for i in range(1, ptr):  # 이미 찾은 소수로 나눔
#         counter += 1
#         if n % prime[i] == 0:  # 나누어 떨어지면 소수가 아님
#             break              # 반복 중단
#     else:                      # 끝까지 나누어 떨어지지 않았다면
#         prime[ptr] = n         # 소수로 배열에 등록
#         ptr += 1
# for i in range(ptr):  # ptr의 소수를 출력
#     print(prime[i])
# print(f'나눗셈을 실행한 횟수: {counter}')

# [Do it! 실습 2-10] 1,000 이하의 소수를 나열하기(알고리즘 개선 2) - 배열의 원솟수를 미리 결정하지 않음
# counter = 0             # 곱셈과 나눗셈을 합한 횟수
# prime = [2, 3]          # 소수를 저장하는 배열
# for n in range(5, 1001, 2):     # 홀수만을 대상으로 설정
#     i = 1
#     while prime[i] * prime[i] <= n:
#         counter += 2
#         if n % prime[i] == 0:   # 나누어 떨어지므로 소수가 아님
#             break               # 반복 중단
#         i += 1
#     else:                       # 끝까지 나누어 떨어지지 않았다면
#         prime += [n]            # 소수로 배열에 등록
#         counter += 1
# for i in prime:                 # 소수를 출력
#     print(i)
# print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')

# [Do it! 실습 2C-1] 리스트의 모든 원소를 ​​스캔하기(원소 수를 미리 파악)
# x = ['John', 'George', 'Paul', 'Ringo']
# for i in range(len(x)):
#     print(f'x[{i}] = {x[i]}')

# [Do it! 실습 2C-2] 리스트의 모든 원소를 ​​enumerate 함수로 스캔하기
# x = ['John', 'George', 'Paul', 'Ringo']
# for i, name in enumerate(x):
#     print(f'x[{i}] = {name}')

# [Do it! 실습 2C-3] 리스트의 모든 요소를 ​​enumerate 함수로 스캔(1부터 카운트)
# x = ['John', 'George', 'Paul', 'Ringo']
# for i, name in enumerate(x, 1):
#     print(f'{i}번째 = {name}')

# [Do it! 실습 2C-4] 리스트의 모든 원소를 ​​스캔하기(인덱스 값을 사용하지 않음)
# x = ['John', 'George', 'Paul', 'Ringo']
# for i in x:
#     print(i)

# [Do it! 실습 2C-5] 1부터 n까지 정수의 합 구하기
# def sum_1ton(n):
#     """1부터 n까지 정수의 합"""
#     s = 0
#     while n > 0:
#         s += n
#         n -= 1
#     return s
# x = int(input('x의 값을 입력하세요.: '))
# print(f'1부터 {x}까지 합은 {sum_1ton(x)}입니다.')

# [Do it! 실습 2C-6] 리스트의 모든 원솟값을 업데이트하기
# def change(lst, idx, val):
#     """lst[idx]의 값을 val로 업데이트"""
#     lst [idx] = val
# x = [11, 22, 33, 44, 55]
# print('x =', x)
# index = int(input('업데이트할 인덱스를 선택하세요.: '))
# value = int(input('새로운 값을 입력하세요.: '))
# change(x, index, value)
# print(f'x = {x}')

# [Do it! 실습 2C-7] 자료형을 정하지 않은 리스트 원소 확인하기
# x = [15, 64, 7, 3.14, [32, 55], 'ABC']
# for i in range(len(x)):
#     print(f'x[{i}] = {x[i]}')


# [CHAP03]

# 선형 검색 알고리즘(검색에 실패하면 ValueError를 보냄)
# from typing import Any, Sequence
# def seq_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 값이 같은 요소를 선형 검색(for 문)"""
#     for i in range(len(a)):
#         if a[i] == key:
#             return i        # 검색 성공(첨자를 반환)
#     raise ValueError        # 검색 실패
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     ky = int(input('검색할 값을 입력하세요.: '))  # 키 ky를 입력받음
#     try:
#         idx = seq_search(x, ky)  # ky와 값이 같은 요소를 x에서 검색
#     except ValueError:
#         print('검색 값을 갖는 요소가 존재하지 않습니다.')
#     else:
#         print(f'검색 값은 x[{idx}]에 있습니다.')

# 이진 검색 알고리즘(검색에 실패할 때 ValueError를 내보냄）
# from typing import Any, Sequence
# def bin_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 일치하는 요소를 이진 검색"""
#     pl = 0           # 검색 범위 맨 앞 요소의 인덱스
#     pr = len(a) - 1  # 검색 범위 맨 끝 요소의 인덱스
#     while True:
#         pc = (pl + pr) // 2  # 중앙 요소의 인덱스
#         if a[pc] == key:
#             return pc  # 검색 성공
#         elif a[pc] < key:
#             pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
#         else:
#             pr = pc - 1  # 검색 범위를 앞쪽 절반으로 좁힘
#         if pl > pr:
#             break
#     raise ValueError  # 검색 실패
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수 num인 배열을 생성
#     print('오름차순으로 입력하세요.')
#     x[0] = int(input('x[0] : '))
#     for i in range(1, num):
#         while True:
#             x[i] = int(input(f'x[{i}] : '))
#             if x[i] >= x[i - 1]:
#                  break
#     ky = int(input('검색할 값을 입력하세요.: '))  # 키 ky를 입력받음
#     try:
#         idx = bin_search(x, ky)                 # ky와 같은 값의 요소를 x에서 검색
#     except ValueError:
#         print('검색값을 갖는 요소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')

# [Do it! 실습 3-1] while 문으로 작성한 선형 검색 알고리즘
# from typing import Any, Sequence
# def seq_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key값이 같은 원소를 선형 검색(while 문)"""
#     i = 0
#     while True:
#         if i == len(a):
#             return -1  # 검색에 실패하여 -1을 반환
#         if a[i] == key:
#             return i   # 검색에 성공하여 현재 조사한 배열의 인덱스를 반환
#         i += 1
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
#     x = [None] * num                           # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받기
#     idx = seq_search(x, ky)                     # ky와 같은 원소를 x에서 검색
#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')

# [Do it! 실습 3-2] for 문으로 작성한 선형 검색 알고리즘
# from typing import Any, Sequence
# def seq_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key값이 같은 요소를 선형 검색(for 문)"""
#     for i in range(len(a)):
#         if a[i] == key:
#             return i  # 검색 성공(인덱스를 반환)
#     return -1         # 검색 실패(-1을 반환)
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
#     x = [None] * num                           # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받음
#     idx = seq_search(x, ky)                     # ky와 값이 같은 요소를 x에서 검색
#     if idx == -1:
#         print('검색 값을 갖는 요소가 존재하지 않습니다.')
#     else:
#         print(f'검색 값은 x[{idx}]에 있습니다.')

# [Do it! 실습 3-3] 선형 검색 알고리즘(실습 3-1)을 보초법으로 수정
# from typing import Any, Sequence
# import copy
# def seq_search(seq: Sequence, key: Any) -> int:
#     """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
#     a = copy.deepcopy(seq)  # seq를 복사
#     a.append(key)           # 보초 key를 추가
#     i = 0
#     while True:
#         if a[i] == key: 
#             break  # 검색에 성공하면 while 문을 종료
#         i += 1
#     return -1 if i == len(seq) else i
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
#     x = [None] * num                           # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받기
#     idx = seq_search(x, ky)                     # ky값과 같은 원소를 x에서 검색
#     if idx == -1:
#          print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')

# [Do it! 실습 3-3] 이진 검색 알고리즘
# from typing import Any, Sequence
# def bin_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
#     pl = 0           # 검색 범위 맨 앞 원소의 인덱스
#     pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스
#     while True:
#         pc = (pl + pr) // 2  # 중앙 원소의 인덱스
#         if a[pc] == key:
#             return pc    # 검색 성공
#         elif a[pc] < key:
#             pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
#         else:
#             pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
#         if pl > pr:
#             break
#     return -1            # 검색 실패
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     print('배열 데이터를 오름차순으로 입력하세요.')
#     x[0] = int(input('x[0]: '))
#     for i in range(1, num):
#         while True:
#             x[i] = int(input(f'x[{i}]: '))
#             if x[i] >= x[i - 1]:
#                  break
#     ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 ky를 입력
#     idx = bin_search(x, ky)                     # ky와 같은 값의 원소를 x에서 검색
#     if idx < 0:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')

# 체인법으로 해시 함수 구현하기
# Do it! 실습 3-5 [A]
# from __future__ import annotations
# from typing import Any, Type
# import hashlib
# class Node:
#     """해시를 구성하는 노드"""
#     def __init__(self, key: Any, value: Any, next: Node) -> None:
#         """초기화"""
#         self.key   = key    # 키
#         self.value = value  # 값
#         self.next  = next   # 뒤쪽 노드를 참조

# Do it! 실습 3-5 [B]
# class ChainedHash:
#     """체인법을 해시 클래스 구현"""
#     def __init__(self, capacity: int) -> None:
#         """초기화"""
#         self.capacity = capacity             # 해시 테이블의 크기를 지정
#         self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언
#     def hash_value(self, key: Any) -> int:
#         """해시값을 구함"""
#         if isinstance(key, int):
#             return key % self.capacity
#         return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

# Do it! 실습 3-5[C]
#     def search(self, key: Any) -> Any:
#         """키가 key인 원소를 검색하여 값을 반환"""
#         hash = self.hash_value(key)  # 검색하는 키의 해시값
#         p = self.table[hash]         # 노드를 노드
#         while p is not None:
#             if p.key == key:
#                  return p.value  # 검색 성공
#             p = p.next           # 뒤쪽 노드를 주목
#         return None              # 검색 실패
#     def add(self, key: Any, value: Any) -> bool:
#         """키가 key이고 값이 value인 원소를 삽입"""
#         hash = self.hash_value(key)  # 삽입하는 키의 해시값
#         p = self.table[hash]         # 주목하는 노드
#         while p is not None:
#             if p.key == key:
#                 return False         # 삽입 실패
#             p = p.next               # 뒤쪽 노드에 주목
#         temp = Node(key, value, self.table[hash])
#         self.table[hash] = temp      # 노드를 삽입
#         return True                  # 삽입 성공

# Do it! 실습 3-5[D]
#     def remove(self, key: Any) -> bool:
#         """키가 key인 원소를 삭제"""
#         hash = self.hash_value(key)  # 삭제할 키의 해시값
#         p = self.table[hash]         # 주목하고 있는 노드
#         pp = None                    # 바로 앞 주목 노드
#         while p is not None:
#             if p.key == key:  # key를 발견하면 아래를 실행
#                 if pp is None:
#                     self.table[hash] = p.next
#                 else:
#                     pp.next = p.next
#                 return True  # key 삭제 성공
#             pp = p
#             p = p.next       # 뒤쪽 노드에 주목
#         return False         # 삭제 실패(key가 존재하지 않음)
#     def dump(self) -> None:
#         """해시 테이블을 덤프"""
#         for i in range(self.capacity):
#             p = self.table[i]
#             print(i, end='')
#             while p is not None:
#                 print(f'  → {p.key} ({p.value})', end='')  # 해시 테이블에 있는 키와 값을 출력
#                 p = p.next
#             print()

# [Do it! 실습 3-6] 체인법을 구현하는 해시 클래스 ChainedHash의 사용
# from enum import Enum
# from chained_hash import ChainedHash
# Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])  # 메뉴를 선언
# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '   ', end='')
#         n = int(input(': '))
#         if 1 <=  n <=  len(Menu):
#             return Menu(n)
# hash = ChainedHash(13)     # 크기가 13인 해시 테이블을 생성
# while True:
#     menu = select_menu()   # 메뉴 선택
#     if menu == Menu.추가:  # 추가
#         key = int(input('추가할 키를 입력하세요.: '))
#         val = input('추가할 값을 입력하세요.: ')
#         if not hash.add(key, val):
#             print('추가를 실패했습니다!')
#     elif menu == Menu.삭제:  # 삭제
#         key = int(input('삭제할 키를 입력하세요.: '))
#         if not hash.remove(key):
#             print('삭제를 실패했습니다!')
#     elif menu == Menu.검색:  # 검색
#         key = int(input('검색할 키를 입력하세요.: '))
#         t = hash.search(key)
#         if t is not None:
#             print(f'검색한 키를 갖는 값은 {t}입니다.')
#         else:
#             print('검색할 데이터가 없습니다.')
#     elif menu == Menu.덤프:  # 덤프
#         hash.dump()
#     else:  # 종료
#         break

# [Do it! 실습 3-7] 오픈 주소법으로 해시함수 구현하기
# from __future__ import annotations
# from typing import Any, Type
# from enum import Enum
# import hashlib
# # 버킷의 속성
# class Status(Enum):
#     OCCUPIED = 0  # 데이터를 저장
#     EMPTY = 1     # 비어 있음
#     DELETED = 2   # 삭제 완료
# class Bucket:
#     """해시를 구성하는 버킷"""
#     def __init__(self, key: Any = None, value: Any = None,
#                        stat: Status = Status.EMPTY) -> None:
#         """초기화"""
#         self.key = key      # 키
#         self.value = value  # 값
#         self.stat = stat    # 속성
#     def set(self, key: Any, value: Any, stat: Status) -> None:
#         """모든 필드에 값을 설정"""
#         self.key = key      # 키
#         self.value = value  # 값
#         self.stat = stat    # 속성
#     def set_status(self, stat: Status) -> None:
#         """속성을 설정"""
#         self.stat = stat
# class OpenHash:
#     """오픈 주소법을 구현하는 해시 클래스"""
#     def __init__(self, capacity: int) -> None:
#         """초기화"""
#         self.capacity = capacity                 # 해시 테이블의 크기를 지정
#         self.table = [Bucket()] * self.capacity  # 해시 테이블
#     def hash_value(self, key: Any) -> int:
#         """해시값을 구함"""
#         if isinstance(key, int):
#             return key % self.capacity
#         return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
#                 % self.capacity)
#     def rehash_value(self, key: Any) -> int:
#         """재해시값을 구함"""
#         return(self.hash_value(key) + 1) % self.capacity
#     def search_node(self, key: Any) -> Any:
#         """키가 key인 버킷을 검색"""
#         hash = self.hash_value(key)  # 검색하는 키의 해시값
#         p = self.table[hash]         # 버킷을 주목
#         for i in range(self.capacity):
#             if p.stat == Status.EMPTY:
#                 break
#             elif p.stat == Status.OCCUPIED and p.key == key:
#                 return p
#             hash = self.rehash_value(hash)  # 재해시
#             p = self.table[hash]
#         return None
#     def search(self, key: Any) -> Any:
#         """키가 key인 갖는 원소를 검색하여 값을 반환"""
#         p = self.search_node(key)
#         if p is not None:
#             return p.value  # 검색 성공
#         else:
#             return None     # 검색 실패
#     def add(self, key: Any, value: Any) -> bool:
#         """키가 key이고 값이 value인 요소를 추가"""
#         if self.search(key) is not None:
#             return False             # 이미 등록된 키
#         hash = self.hash_value(key)  # 추가하는 키의 해시값
#         p = self.table[hash]         # 버킷을 주목
#         for i in range(self.capacity):
#             if p.stat == Status.EMPTY or p.stat == Status.DELETED:
#                 self.table[hash] = Bucket(key, value, Status.OCCUPIED)
#                 return True
#             hash = self.rehash_value(hash)  # 재해시
#             p = self.table[hash]
#         return False                        # 해시 테이블이 가득 참
#     def remove(self, key: Any) -> int:
#         """키가 key인 갖는 요소를 삭제"""
#         p = self.search_node(key)  # 버킷을 주목
#         if p is None:
#             return False           # 이 키는 등록되어 있지 않음
#         p.set_status(Status.DELETED)
#         return True
#     def dump(self) -> None:
#         """해시 테이블을 덤프"""
#         for i in range(self.capacity):
#             print(f'{i:2} ', end='')
#             if self.table[i].stat == Status.OCCUPIED:
#                 print(f'{self.table[i].key} ({self.table[i].value})')
#             elif self.table[i].stat == Status.EMPTY:
#                 print('-- 미등록 --')
#             elif self.table[i] .stat == Status.DELETED:
#                 print('-- 삭제 완료 --')

# [Do it! 실습 3-8] 오픈 주소법을 구현하는 해시 클래스 OpenHash 사용
# from enum import Enum
# from open_hash import OpenHash
# Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])
# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '  ', end='')
#         n = int(input(': '))
#         if 1 <=  n <= len(Menu):
#             return Menu(n)
# hash = OpenHash(13)  # 크기가 13인 해시 테이블 생성
# while True:
#     menu = select_menu()  # 메뉴 선택
#     if menu == Menu.추가:  # 추가
#         key = int(input('추가할 키를 입력하세요.: '))
#         val = input('추가할 값을 입력하세요.: ')
#         if not hash.add(key, val):
#             print('추가를 실패했습니다!')
#     elif menu == Menu.삭제:  # 삭제
#         key = int(input('삭제할 키를 입력하세요.: '))
#         if not hash.remove(key):
#             print('삭제를 실패했습니다!')
#     elif menu == Menu.검색:  # 검색
#         key = int(input('검색할 키를 입력하세요.: '))
#         t = hash.search(key)
#         if t is not None:
#             print(f'검색한 키를 갖는 값은 {t}입니다.')
#         else:
#             print('검색할 데이터가 없습니다.')
#     elif menu == Menu.덤프:  # 덤프
#         hash.dump()
#     else:  # 종료
#         break

# [Do it! 실습 3C-1] seq_search() 함수를 사용하여 실수 검색하기
# from ssearch_while import seq_search
# print('실수를 검색합니다.')
# print('주의: "End"를 입력하면 종료합니다.')
# number = 0
# x = []  # 빈 리스트 x를 생성
# while True:
#     s = input(f'x[{number}]: ')
#     if s == 'End':
#         break
#     x.append(float(s))  # 배열 마지막에 원소를 추가
#     number += 1
# ky = float(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력
# idx = seq_search(x, ky)  # ky와 같은 값의 원소를 x에서 검색
# if idx == -1:
#     print('검색값을 갖는 원소가 존재하지 않습니다.')
# else:
#     print(f'검색값은 x[{idx}]에 있습니다.')

# [Do it! 실습 3C-2] seq_search() 함수를 사용하여 특정 인덱스 검색하기
# from ssearch_while import seq_search
# t = (4, 7, 5.6, 2, 3.14, 1)
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']
# print(f'{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}입니다.')
# print(f'{s}에서 "n"의 인덱스는 {seq_search(s, "n")}입니다.')
# print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a, "DTS")}입니다.')

# [Do it! 실습 3C-3] 이진 검색 알고리즘의 실행 과정을 출력
# from typing import Any, Sequence
# def bin_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 일치하는 원소를 이진 검색(실행 과정을 출력)"""
#     pl = 0           # 검색 범위 맨 앞 원소의 인덱스
#     pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스
#     print('   |', end='')
#     for i in range(len(a)):
#         print(f'{i : 4}', end='')
#     print()
#     print('---+' + (4 * len(a) + 2) * '-')
#     while True:
#         pc = (pl + pr) // 2  # 중앙 원소의 인덱스
#         print('   |', end='')
#         if pl != pc:         # pl 원소 위에 <-를 출력
#             print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
#         else: 
#             print((pc * 4 + 1) * ' ' + '<+', end='')
#         if pc != pr:         # pr 원소 위에 ->를 출력
#             print(((pr - pc) * 4 - 2) * ' ' + '->')
#         else:
#             print('->')
#         print(f'{pc:3}|', end='')
#         for i in range(len(a)):
#             print(f'{a[i]:4}', end='') 
#         print('\n   |')
#         if a[pc] == key:
#             return pc    # 검색 성공
#         elif a[pc] < key:
#             pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
#         else:
#             pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
#         if pl > pr:  
#             break
#     return -1            # 검색 실패
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     print('배열 데이터를 오름차순으로 입력하세요.')
#     x[0] = int(input('x[0]: '))
#     for i in range(1, num):
#         while True:
#             x[i] = int(input(f'x[{i}]: '))
#             if x[i] >= x[i - 1]:
#                  break
#     ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 ky를 입력
#     idx = bin_search(x, ky)                     # ky와 같은 값의 원소를 x에서 검색
#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')


# [CHAP04]

# 고정 길이 스택 클래스 FixedStack 구현하기
# [Do it! 실습 4-1 [A]]
# from typing import Any
# class FixedStack:
#     """고정 길이 스택 클래스"""
#     class Empty(Exception):
#         """비어 있는 FixedStack에 pop 또는 peek를 호출할 때 내보내는 예외 처리"""
#         pass
#     class Full(Exception):
#         """가득 찬 FixedStack에 push를 호출할 때 내보내는 예외 처리"""
#         pass
#     def __init__(self, capacity: int = 256) -> None:
#         """초기화"""
#         self.stk = [None] * capacity  # 스택 본체
#         self.capacity = capacity      # 스택의 크기
#         self.ptr = 0                  # 스택 포인터
#     def __len__(self) -> int:
#         """스택에 쌓여있는 데이터 개수를 반환"""
#         return self.ptr
#     def is_empty(self) -> bool:
#         """스택이 비어 있는가?"""
#         return self.ptr <= 0
#     def is_full(self) -> bool:
#         """스택은 가득 찼는가?"""
#         return self.ptr >= self.capacity

# [Do it! 실습 4-1 [B]]
#     def push(self, value: Any) -> None:
#         """스택에 value를 푸시"""
#         if self.is_full():              # 스택이 가득 참
#             raise FixedStack.Full
#         self.stk[self.ptr] = value
#         self.ptr += 1
#     def pop(self) -> Any:
#         """스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)"""
#         if self.is_empty():             # 스택이 비어 있음
#              raise FixedStack.Empty
#         self.ptr -= 1
#         return self.stk[self.ptr]
#     def peek(self) -> Any:
#         """스택에서 데이터를 피크(꼭대기 데이터를 들여다 봄)"""
#         if self.is_empty():             # 스택이 비어 있음
#             raise FixedStack.Empty
#         return self.stk[self.ptr - 1]
#     def clear(self) -> None:
#         """스택을 비움(모든 데이터를 삭제)"""
#         self.ptr = 0

# [Do it! 실습 4-1 [C]]
#     def find(self, value: Any) -> Any:
#         """스택에서 value를 찾아 첨자(없으면 -1)를 반환"""
#         for i in range(self.ptr - 1, -1, -1):  # 꼭대기 쪽부터 선형 검색
#             if self.stk[i] == value:
#                 return i  # 검색 성공
#         return -1         # 검색 실패
#     def count(self, value: Any) -> bool:
#         """스택에 포함되어있는 value의 개수를 반환"""
#         c = 0
#         for i in range(self.ptr):  # 바닥 쪽부터 선형 검색
#             if self.stk[i] == value:
#                 c += 1             # 들어 있음
#         return c
#     def __contains__(self, value: Any) -> bool:
#         """스택에 value가 있는가?"""
#         return self.count(value)
#     def dump(self) -> None:
#         """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
#         if self.is_empty():  # 스택이 비어 있음
#             print('스택이 비어 있습니다.')
#         else:
#             print(self.stk[:self.ptr])

# [Do it! 실습 4-2] 고정 길이 스택 FixedStack의 사용하기
# from enum import Enum
# from fixed_stack import FixedStack
# Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])
# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '   ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
# s = FixedStack(64)  # 최대 64개를 푸시할 수 있는 스택
# while True:
#     print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
#     menu = select_menu()  # 메뉴 선택 
#     if menu == Menu.푸시:  # 푸시
#         x = int(input('데이터를 입력하세요.: '))
#         try:
#             s.push(x)
#         except FixedStack.Full:
#             print('스택이 가득 차 있습니다.')
#     elif menu == Menu.팝:  # 팝
#         try:
#             x = s.pop()
#             print(f'팝한 데이터는 {x}입니다.')
#         except FixedStack.Empty:
#             print('스택이 비어 있습니다.')
#     elif menu == Menu.피크:  # 피크
#         try:
#             x = s.peek()
#             print(f'피크한 데이터는 {x}입니다.')
#         except FixedStack.Empty:
#             print('스택이 비어 있습니다.')
#     elif menu == Menu.검색:  # 검색
#         x = int(input('검색할 값을 입력하세요.: '))
#         if x in s:
#             print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
#         else:
#             print('검색값을 찾을 수 없습니다.')
#     elif menu == Menu.덤프:  # 덤프
#         s.dump()
#     else:
#         break

# 고정 길이 큐 클래스 FixedQueue 구현하기
# [Do it! 실습 4-3 [A]]
# from typing import Any
# class FixedQueue:
#     class Empty(Exception):
#         """비어 있는 FixedQueue에 대해 deque 또는 peek를 호출할 때 내보내는 예외처리"""
#         pass
#     class Full(Exception):
#         """가득 찬 FixedQueue에 enque를 호출할 때 내보내는 예외처리"""
#         pass
#     def __init__(self, capacity: int) -> None:
#         """초기화 선언"""
#         self.no = 0     # 현재 데이터 개수
#         self.front = 0  # 맨앞 원소 커서
#         self.rear = 0   # 맨끝 원소  커서
#         self.capacity = capacity      # 큐의 크기
#         self.que = [None] * capacity  # 큐의 본체
#     def __len__(self) -> int:
#         """큐에 있는 모든 데이터 개수를 반환"""
#         return self.no
#     def is_empty(self) -> bool:
#         """큐가 비어 있는지 판단"""
#         return self.no <= 0
#     def is_full(self) -> bool:
#         """큐가 가득 찼는지 판단"""
#         return self.no >= self.capacity

# [Do it! 실습 4-3 [B]]
#     def enque(self, x: Any) -> None:
#         """데이터 x를 인큐"""
#         if self.is_full():
#             raise FixedQueue.Full  # 큐가 가득 찬 경우 예외처리를 발생
#         self.que[self.rear] = x
#         self.rear += 1
#         self.no += 1
#         if self.rear == self.capacity:
#             self.rear = 0

# [Do it! 실습 4-3 [C]]
#     def deque(self) -> Any:
#         """데이터를 디큐합니다"""
#         if self.is_empty():
#             raise FixedQueue.Empty  # 큐가 비어 있는 경우 예외처리를 발생
#         x = self.que[self.front]
#         self.front += 1
#         self.no -= 1
#         if self.front == self.capacity:
#             self.front = 0
#         return x

# [Do it! 실습 4-3 [D]]
#     def peek(self) -> Any:
#         """데이터를 피크합니다(맨 앞 데이터를 들여다 봄)"""
#         if self.is_empty():
#             raise FixedQueue.Empty  # 큐가 비어 있으면 예외처리를 발생
#         return self.que[self.front]
#     def find(self, value: Any) -> Any:
#         """큐에서 value를 찾아 인덱스를 반환하고 없으면 -1을 반환합니다"""
#         for i in range(self.no):
#             idx = (i + self.front) % self.capacity
#             if self.que[idx] == value:  # 검색 성공
#                 return idx
#         return -1  # 검색 실패
#     def count(self, value: Any) -> bool:
#         """큐에 포함되어 있는 value의 개수를 반환합니다"""
#         c = 0
#         for i in range(self.no):  # 큐 데이터를 선형 검색
#             idx = (i + self.front) % self.capacity
#             if self.que[idx] == value:  # 검색 성공
#                 c += 1  # 들어있음
#         return c
#     def __contains__(self, value: Any) -> bool:
#         """큐에 value가 포함되어 있는지 판단합니다"""
#         return self.count(value)
#     def clear(self) -> None:
#         """큐의 모든 데이터를 비웁니다"""
#         self.no = self.front = self.rear = 0
#     def dump(self) -> None:
#         """모든 데이터를 맨 앞에서 맨 끝 순서로 출력합니다"""
#         if self.is_empty():  # 큐가 비어 있으면 예외처리를 발생
#             print('큐가 비어 있습니다.')
#         else:
#             for i in range(self.no):
#                 print(self.que[(i + self.front) % self.capacity], end=' ')
#             print()

# [Do it! 실습 4-4] 고정 길이 큐 클래스(FixedQueue)를 사용하기
# from enum import Enum
# from fixed_queue import FixedQueue
# Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])
# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='   ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
# q = FixedQueue(64)  # 최대 64개를 인큐할 수 있는 큐 생성(고정 길이)
# while True:
#     print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
#     menu = select_menu()   # 메뉴 선택
#     if menu == Menu.인큐:  # 인큐
#         x = int(input('인큐할 데이터를 입력하세요.: '))
#         try:
#             q.enque(x)
#         except FixedQueue.Full:
#             print('큐가 가득 찼습니다.')
#     elif menu == Menu.디큐:  # 디큐
#         try:
#             x = q.deque()
#             print(f'디큐한 데이터는 {x}입니다.')
#         except FixedQueue.Empty:
#             print('큐가 비어 있습니다.')
#     elif menu == Menu.피크:  # 피크
#         try:
#             x = q.peek()
#             print(f'피크한 데이터는 {x}입니다.')
#         except FixedQueue.Empty:
#             print('큐가 비었습니다.')
#     elif menu == Menu.검색:  # 검색
#         x = int(input('검색할 값을 입력하세요.: '))
#         if x in q:
#             print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
#         else:
#             print('검색값을 찾을 수 없습니다.')
#     elif menu == Menu.덤프:  # 덤프
#         q.dump()
#     else:
#         break

# [Do it! 4C-1] 고정 길이 스택 클래스 구현하기(collections.deque를 사용)
# from typing import Any
# from collections import deque
# class Stack:
#     """고정 길이 스택 클래스(collections.deque를 사용)"""
#     def __init__(self, maxlen: int = 256) -> None:
#         """초기화 선언"""
#         self.capacity = maxlen
#         self.__stk = deque([], maxlen)
#     def __len__(self) -> int:
#         """스택에 쌓여있는 데이터 개수를 반환"""
#         return len(self.__stk)
#     def is_empty(self) -> bool:
#         """스택이 비어 있는지 판단"""
#         return not self.__stk
#     def is_full(self) -> bool:
#         """스택이 가득 찼는지 판단"""
#         return len(self.__stk) == self.__stk.maxlen
#     def push(self, value: Any) -> None:
#         """스택에 value를 푸시"""
#         self.__stk.append(value)
#     def pop(self) -> Any:
#         """스택에서 데이터를 팝"""
#         return self.__stk.pop()
#     def peek(self) -> Any:
#         """스택에서 데이터를 피크"""
#         return self.__stk[-1]
#     def clear(self) -> None:
#         """스택을 비웁니다"""
#         self.__stk.clear()
#     def find(self, value: Any) -> Any:
#         """스택에서 value를 찾아 인덱스(없으면 -1)를 반환"""
#         try:
#             return self.__stk.index(value)
#         except ValueError:
#             return -1
#     def count(self, value: Any) -> int:
#         """스택에 포함된 value의 개수를 반환"""
#         return self.__stk.count(value)
#     def __contains__(self, value: Any) -> bool:
#         """스택에 value가 포함되어 있는지 판단"""
#         return self.count(value)
#     def dump(self) -> int:
#         """스택 안에 있는 모든 데이터를 나열"""
#         print(list(self.__stk))

# [Do it! 4C-1] 고정 길이 스택 클래스(collections.deque)를 사용하기
# from enum import Enum
# from stack import Stack
# Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])
# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='  ', end='')
#         n = int(input('：'))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
# s = Stack(64)  # 최대 64 개를 푸시할 수 있는 스택
# while True:
#     print(f'현재 데이터 개수：{len(s)} / {s.capacity}')
#     menu = select_menu()  # 메뉴 선택
#     if menu == Menu.푸시:  # 푸시
#         x = int(input('데이터：'))
#         try:
#             s.push(x)
#         except IndexError:
#             print('스택이 가득 찼습니다.')
#     elif menu == Menu.팝:  # 팝
#         try:
#             x = s.pop()
#             print(f'팝한 데이터는 {x}입니다.')
#         except IndexError:
#            print('스택이 비어 있습니다.')
#     elif menu == Menu.피크:  # 피크
#         try:
#             x = s.peek()
#             print(f'피크한 데이터는 {x}입니다.')
#         except IndexError:
#            print('스택이 비어 있습니다.')
#     elif menu == Menu.검색:  # 검색
#         x = int(input('검색 값을 입력하세요：'))
#         if x in s:
#             print(f'{s.count(x)} 개를 포함하고, 맨 앞쪽의 위치는 {s.find(x)}입니다.')
#         else:
#             print('검색 값은 포함되어 있지 않습니다.')       
#     elif menu == Menu.덤프:  # 덤프
#         s.dump()
#     else:
#         break

# [Do it! 실습 4C-2] 원하는 개수(n)만큼 값을 입력받아 마지막 n개를 저장
# n = int(input('정수를 몇 개 저장할까요? : '))
# a = [None] * n  # 입력 받은 값을 저장하는 배열
# cnt = 0         # 입력 받은 개수
# while True:
#     a[cnt % n] = int(input((f'{cnt + 1} 번째 정수를 입력하세요.: ')))
#     cnt += 1
#     retry = input(f'계속 할까요?(Y ... Yes / N ... No) : ')
#     if retry in {'N', 'n'}:
#         break
# i = cnt - n
# if i < 0: i = 0
# while i < cnt:
#     print(f'{i + 1}번째 = {a[i % n]}')
#     i += 1


# [CHAP05]

# [Do it! 실습 5-1] 양의 정수인 팩토리얼 구하기
# def factorial(n: int) -> int:
#     """양의 정수 n의 팩토리얼을 구하는 과정"""
#     if n > 0:
#         return n * factorial(n - 1)
#     else:
#         return 1
# if __name__ == '__main__':
#     n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
#     print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')

# [보충수업 5-1] 양의 정수인 팩토리얼 구하기(n이 음수면 ValueError 예외 처리 발생)
# def factorial(n : int) -> int:
#     """양의 정수 n의 팩토리얼값을 재귀적으로 구함(n이 음수면 ValueError 예외 처리 발생)"""
#     if n > 0:
#         return n * factorial(n - 1)
#     elif n == 0:
#         return 1
#     else:
#         raise ValueError
# if __name__ == '__main__':
#     n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
#     try:
#         print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
#     except ValueError:
#         print(f'{n}의 팩토리얼은 구할 수 없습니다.')

# [Do it! 실습 5-2] 유클리드 호제법으로 최대 공약수 구하기
# def gcd(x: int, y: int) -> int:
#     """정숫값 x와 y의 최대 공약수를 반환"""
#     if y == 0:
#         return x
#     else:
#         return gcd(y, x % y)
# if __name__ == '__main__':
#     print('두 정숫값의 최대 공약수를 구합니다.')
#     x = int(input('첫 번째 정숫값을 입력하세요.: '))
#     y = int(input('두 번째 정숫값을 입력하세요.: '))
#     print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}입니다.')

# [Do it! 실습 5-3] 순수한 재귀 함수 구현하기
# def recur(n: int) -> int:
#     """순수한 재귀 함수 recur의 구현"""
#     if n > 0:
#         recur(n - 1)
#         print(n)
#         recur(n - 2)
# x = int(input('정숫값을 입력하세요.: '))
# recur(x)

# recur 함수를 거꾸로 출력(Do it! 실습 5-3 수정)
# def recur(n: int) -> int:
#     """순수한 재귀 함수 recur의 구현(거꾸로 출력)"""
#     if n > 0:
#         recur(n - 2)
#         print(n)
#         recur(n - 1)
# x = int(input('정숫값을 입력하세요.: '))
# recur(x)

# [Do it! 실습 5-4] 재귀 함수의 구현(꼬리 재귀를 제거)
# def recur(n: int) -> int:
#     """꼬리 재귀를 제거한 함수 recur"""
#     while n > 0:
#         recur(n - 1)
#         print(n)
#         n = n - 2
# x = int(input('정수값을 입력하세요.: '))
# recur(x)

# [Do it! 실습 5-5] 스택으로 재귀 함수 구현하기(재귀를 제거)
# from stack import Stack  # stack.py의 Stack 클래스를 임포트
# def recur(n: int) -> int:
#     """재귀를 제거한 함수 recur"""
#     s = Stack(n)
#     while True:
#         if n > 0:
#             s.push(n)         # n 값을 푸시
#             n = n - 1
#             continue
#         if not s.is_empty():  # 스택이 비어 있지 않으면
#             n = s.pop()       # 저장하고 있는 값을 n에 팝
#             print(n)
#             n = n - 2
#             continue
#         break
# x = int(input('정수값을 입력하세요.: '))
# recur(x)

# [Do it! 실습 5-6] 하노이의 탑 구현하기
# def move(no: int, x: int, y: int) -> None:
#     """원반을 no개를 x 기둥에서 y 기둥으로 옮김"""
#     if no > 1:
#         move(no - 1, x, 6 - x - y)
#     print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')
#     if no > 1:
#         move(no - 1, 6 - x - y, y)
# print('하노이의 탑을 구현하는 프로그램입니다.')
# n = int(input('원반의 개수를 입력하세요.: '))
# move(n, 1, 3)

# [Do it! 실습 5-7] 각 열에 1개 퀸을 배치한 조합을 재귀적으로 나열하기
# pos = [0] * 8  # 각 열에서 퀸의 위치를 출력
# def put() -> None:
#     """각 열에 배치한 퀸의 위치를 출력"""
#     for i in range(8):
#         print(f'{pos[i]:2}', end='')
#     print()
# def set(i: int) -> None:
#     """i 열에 퀸을 배치"""
#     for j in range(8):
#         pos[i] = j   # 퀸을 j행에 배치
#         if i == 7 :  # 모든 열에 배치를 종료
#             put()
#         else:
#             set(i + 1)  # 다음 열에 퀸을 배치
# set(0)  # 0 열에 퀸을 배치

# [Do it! 실습 5-8] 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기
# pos = [0] * 8       # 각 열에서 퀸의 위치
# flag = [False] * 8  # 각 행에 퀸을 배치했는지 체크
# def put() -> None:
#     """각 열에 놓은 퀸의 위치를 출력"""
#     for i in range(8):
#         print(f'{pos[i]:2}', end='')
#     print()
# def set(i: int) -> None:
#     """i 열의 알맞은 위치에 퀸을 배치"""
#     for j in range(8):
#         if not flag[j]:  # j 행에 퀸을 배치하지 않았으면
#             pos[i] = j   # 퀸을 j 행에 배치
#             if i == 7:   # 모든 열에 퀸을 배치를 완료
#                 put()
#             else:
#                 flag[j] = True
#                 set(i + 1)  # 다음 열에 퀸을 배치
#                 flag[j] = False
# set(0)  # 0열에 퀸을 배치

# [Do it! 실습 5-9] 8퀸 문제 알고리즘 구현하기
# pos = [0] * 8          # 각 열에 배치한 퀸의 위치
# flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
# flag_b = [False] * 15  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
# flag_c = [False] * 15  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크
# def put() -> None:
#     """각 열에 배치한 퀸의 위치를 출력"""
#     for i in range(8):
#         print(f'{pos[i]:2}', end='')
#     print()
# def set(i: int) -> None:
#     """i 열의 알맞은 위치에 퀸을 배치"""
#     for j in range(8):
#         if(     not flag_a[j]            # j행에 퀸이 배치 되지 않았다면
#             and not flag_b[i + j]        # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
#             and not flag_c[i - j + 7]):  # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
#             pos[i] = j  # 퀸을 j행에 배치
#             if i == 7:  # 모든 열에 퀸을 배치하는 것을 완료
#                 put()
#             else:
#                 flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
#                 set(i + 1)  # 다음 열에 퀸을 배치
#                 flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False
# set(0)  # 0열에 퀸을 배치

# [Do it! 실습 5-9] 8퀸 문제 알고리즘 구현하기(퀸을 놓는 상황을 네모로 표시)
# pos = [0] * 8          # 각 열에 배치한 퀸의 위치
# flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
# flag_b = [False] * 15  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
# flag_c = [False] * 15  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크
# def put() -> None:
#     """퀸을 놓는 상황을 □와 ■로 출력"""
#     for j in range(8):
#         for i in range(8):
#             print('■' if pos[i] == j else '□', end='')
#         print()
#     print()
# def set(i: int) -> None:
#     """i 열의 알맞은 위치에 퀸을 놓기"""
#     for j in range(8):
#         if(     not flag_a[j]           # j 행에 아직 퀸을 놓지 않았으면
#             and not flag_b[i + j]       # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
#             and not flag_c[i - j + 7]): # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
#             pos[i] = j          # 퀸을 j 행에 놓기
#             if i == 7:          # 모든 열에 퀸을 배치하는 것을 완료
#                 put()
#             else:
#                 flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
#                 set(i + 1)      # 다음 열에 퀸을 놓기
#                 flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False
# set(0)          # 0 열에 퀸을 놓기


# [CHAP06]

# 병합 정렬 알고리즘 구현하기(heapq.merge를 사용)
# from typing import MutableSequence
# import heapq
# def merge_sort(a: MutableSequence) -> None:
#     """병합 정렬(heapq.merge를 사용)"""
#     atype = type(a)
#     def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
#         """a[left]～a[right]를 재귀적으로 병합 정렬"""
#         if left < right:
#             center = (left + right) // 2
#             _merge_sort(a, left, center)            # 앞부분 배열의 병합 정렬
#             _merge_sort(a, center + 1, right)       # 뒷부분 배열의 병합 정렬
#             buff = atype(heapq.merge(a[left: center+1], a[center + 1: right+1]))
#             for i in range(len(buff)):
#                 a[left + i] = buff[i]
#     _merge_sort(a, 0, len(a))       # 배열 전체를 병합 정렬
# if __name__ == '__main__':
#     print('병합 정렬을 수행합니다(heapq.merge를 사용).')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     merge_sort(x)       # 배열 x를 병합 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# 고정 길이 스택 클래스(collections.deque을 사용) 구현 예제
# from typing import Any
# from collections import deque
# class Stack:
#     """고정 길이 스택 클래스(collections.deque을 사용)"""
#     def __init__(self, maxlen: int = 256) -> None:
#         """초기화 선언"""
#         self.capacity = maxlen
#         self.__stk = deque([], maxlen)
#     def __len__(self) -> int:
#         """스택에 쌓여있는 데이터 개수를 반환"""
#         return len(self.__stk)
#     def is_empty(self) -> bool:
#         """스택이 비어 있는지 판단"""
#         return not self.__stk
#     def is_full(self) -> bool:
#         """스택이 가득 찼는지 판단"""
#         return len(self.__stk) == self.__stk.maxlen
#     def push(self, value: Any) -> None:
#         """스택에 value를 푸시"""
#         self.__stk.append(value)
#     def pop(self) -> Any:
#         """스택에서 데이터를 팝"""
#         return self.__stk.pop()
#     def peek(self) -> Any:
#         """스택에서 데이터를 피크"""
#         return self.__stk[-1]
#     def clear(self) -> None:
#         """스택을 비웁니다"""
#         self.__stk.clear()
#     def find(self, value: Any) -> Any:
#         """스택에서 value를 찾아 인덱스(없으면 -1)를 반환"""
#         try:
#             return self.__stk.index(value)
#         except ValueError:
#             return -1
#     def count(self, value: Any) -> int:
#         """스택에 포함된 value의 개수를 반환"""
#         return self.__stk.count(value)
#     def __contains__(self, value: Any) -> bool:
#         """스택에 value가 포함되어 있는지 판단"""
#         return self.count(value)
#     def dump(self) -> int:
#         """스택 안에 있는 모든 데이터를 나열"""
#         print(list(self.__stk))

# 정렬을 마친 두 배열의 병합 (heapq.merege 사용）
# import heapq
# a = [2, 1, 6, 8, 11, 13]
# b = [1, 2, 3, 4, 9, 16, 21]
# c = list(heapq.merge(a, b))  # 배열 a와 b를 병합하여 c에 저장
# print('배열 a와 b를 병합하여 배열 c에 저장하였습니다.')
# print(f'배열 a: {a}')
# print(f'배열 b: {b}')
# print(f'배열 c: {c}')

# [Do it! 실습 6-1] 버블 정렬 알고리즘 구현하기
# from typing import MutableSequence
# def bubble_sort(a: MutableSequence) -> None:
#     """버블 정렬"""
#     n = len(a)
#     for i in range(n - 1):
#         for j in range(n - 1, i, -1):
#             if a[j - 1] > a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     bubble_sort(x)  # 배열 x를 버블 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-2] 버블 정렬 알고리즘 구현(정렬 과정을 출력)
# from typing import MutableSequence
# def bubble_sort_verbose(a: MutableSequence) -> None:
#     """버블 정렬(정렬 과정을 출력)"""
#     ccnt = 0  # 비교 횟수
#     scnt = 0  # 교환 횟수
#     n = len(a)
#     for i in range(n - 1):
#         print(f'패스 {i + 1}')
#         for j in range(n - 1, i, -1):
#             for m in range(0, n - 1):
#                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
#                                     ' +' if a[j - 1] > a[j] else ' -'), 
#                                     end='')
#             print(f'{a[n - 1]:2}')
#             ccnt += 1
#             if a[j - 1] > a[j]:
#                 scnt += 1
#                 a[j - 1], a[j] = a[j], a[j - 1]
#         for m in range(0, n - 1):
#            print(f'{a[m]:2}', end='  ')
#         print(f'{a[n - 1]:2}')
#     print(f'비교를 {ccnt}번 했습니다.')
#     print(f'교환을 {scnt}번 했습니다.')
# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     bubble_sort_verbose(x)  # 배열 x를 버블 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-3] 버블 정렬 알고리즘 구현하기(알고리즘의 개선 1) - 정렬 과정을 출력
# from typing import MutableSequence
# def bubble_sort2_verbose(a: MutableSequence) -> None:
#     """버블 정렬(교환 횟수에 따른 중단)"""
#     ccnt = 0  # 비교 횟수
#     scnt = 0  # 교환 횟수
#     n = len(a)
#     for i in range(n - 1):
#         print(f"패스 {i + 1}")
#         exchng = 0  # 패스에서의 교환 횟수
#         for j in range(n - 1, i, -1):
#             for m in range(0, n - 1):
#                 print(
#                     f"{a[m]:2}"
#                     + ("  " if m != j - 1 else " +" if a[j - 1] > a[j] else " -"),
#                     end="",
#                 )
#             print(f"{a[n - 1]:2}")
#             ccnt += 1
#             if a[j - 1] > a[j]:
#                 scnt += 1
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 exchng += 1
#         for m in range(0, n - 1):
#             print(f"{a[m]:2}", end="  ")
#         print(f"{a[n - 1]:2}")
#         if exchng == 0:  # 교환이 수행되지 않았으면 작업을 중단
#             break
#     print(f"비교를 {ccnt}번 했습니다.")
#     print(f"교환을 {scnt}번 했습니다.")
# if __name__ == "__main__":
#     print("버블 정렬을 수행합니다")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num        # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#     bubble_sort2_verbose(x)  # 배열 x를 버블 정렬
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# [Do it! 실습 6-3]버블 정렬 알고리즘 구현하기(알고리즘의 개선 1)
# from typing import MutableSequence
# def bubble_sort(a: MutableSequence) -> None:
#     """버블 정렬(교환 횟수에 따른 중단)"""
#     n = len(a)
#     for i in range(n - 1):
#         exchng = 0  # 패스에서 교환 횟수
#         for j in range(n - 1, i, -1):
#             if a[j - 1] > a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 exchng += 1
#         if exchng == 0:
#             break
# if __name__ == '__main__':
#     print('버블 정렬을 합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num    # 원소 수 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     bubble_sort(x)      # 배열 x를 버블 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-4] 버블 정렬 알고리즘 구현하기(알고리즘의 개선 2) - 정렬 과정을 출력
# from typing import MutableSequence
# def bubble_sort3_verbose(a: MutableSequence) -> None:
#     """버블 정렬(스캔 범위를 제한)"""
#     ccnt = 0  # 비교 횟수
#     scnt = 0  # 교환 횟수
#     n = len(a)
#     k = 0
#     i = 0
#     while k < n - 1:
#         print(f'패스 {i + 1}')
#         i += 1
#         last = n - 1
#         for j in range(n - 1, k, -1):
#             for m in range(0, n - 1):
#                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
#                                     ' +' if a[j - 1] > a[j] else ' -'),
#                      end='')
#             print(f'{a[n - 1]:2}')
#             ccnt += 1
#             if a[j - 1] > a[j]:
#                 scnt += 1
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 last = j
#         k = last
#         for m in range(0, n - 1):
#            print(f'{a[m]:2}', end='  ')
#         print(f'{a[n - 1]:2}')
#     print(f'비교를 {ccnt}번 했습니다.')
#     print(f'교환을 {scnt}번 했습니다.')
# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     bubble_sort3_verbose(x)  # 배열 x를 버블
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-4] 버블 정렬 알고리즘 구현하기(알고리즘의 개선 2)
# from typing import MutableSequence
# def bubble_sort(a: MutableSequence) -> None:
#     """버블 정렬(스캔 범위를 제한)"""
#     n = len(a)
#     k = 0
#     while k < n - 1:
#         last = n - 1
#         for j in range(n - 1, k, -1):
#             if a[j - 1] > a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 last = j
#         k = last
# if __name__ == '__main__':
#     print('버블 정렬을 합니다.')
#     num = int(input('원솟수를 입력하세요.: '))
#     x = [None] * num    # 원솟수 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     bubble_sort(x)      # 배열 x를 버블 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-5] 셰이커 정렬 알고리즘 구현하기(정렬 과정을 출력)
# from typing import MutableSequence
# def shaker_sort_verbose(a: MutableSequence) -> None:
#     """"셰이커 정렬(정렬 과정을 출력)"""
#     ccnt = 0  # 비교 횟수
#     scnt = 0  # 교환 횟수
#     left = 0
#     n = len(a)
#     right = len(a) - 1
#     last = right
#     i = 0
#     while left < right:
#         print(f'패스{i + 1}')
#         i += 1
#         for j in range(right, left, -1):
#             for m in range(0, n - 1):
#                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
#                                     ' +' if a[j - 1] > a[j] else ' -'),
#                      end='')
#             print(f'{a[n - 1]:2}')
#             ccnt += 1
#             if a[j - 1] > a[j]:
#                 scnt += 1
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 last = j
#         left = last
#         for m in range(0, n - 1):
#            print(f'{a[m]:2}', end='  ')
#         print(f'{a[n - 1]:2}')
#         if (left == right):
#              break
#         print(f'패스 {i + 1}')
#         i += 1
#         for j in range(left, right):
#             for m in range(0, n - 1):
#                print(f'{a[m]:2}' + ('  ' if m != j else
#                                     ' +' if a[j] > a[j + 1] else ' -'),
#                      end='')
#             print(f'{a[n - 1]:2}')
#             if a[j] > a[j + 1]:
#                 scnt += 1
#                 a[j], a[j + 1] = a[j + 1], a[j]
#                 last = j
#         right = last
#         for m in range(0, n - 1):
#            print(f'{a[m]:2}', end='  ')
#         print(f'{a[n - 1]:2}')
#     print(f'비교를 {ccnt}번 했습니다.')
#     print(f'교환을 {scnt}번 했습니다.')
# if __name__ == '__main__':
#     print('셰이커 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     shaker_sort_verbose(x)  # 배열 x를 단순 교환 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-5] 셰이커 정렬 알고리즘 구현하기
# from typing import MutableSequence
# def shaker_sort(a: MutableSequence) -> None:
#     """셰이커 정렬"""
#     left = 0
#     right = len(a) - 1
#     last = right
#     while left < right:
#         for j in range(right, left, -1):
#             if a[j - 1] > a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 last = j
#         left = last
#         for j in range(left, right):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#                 last = j
#         right = last
# if __name__ == '__main__':
#     print('셰이커 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     shaker_sort(x)      # 배열 x를 단순 교환 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-6] 단순 선택 정렬 알고리즘 구현
# from typing import MutableSequence
# def selection_sort(a: MutableSequence) -> None:
#     """단순 선택 정렬"""
#     n = len(a)
#     for i in range(n - 1):
#         min = i  # 정렬 할 부분에서 가장 작은 원소의 인덱스
#         for j in range(i + 1, n):
#             if a[j] < a[min]:
#                 min = j
#         a[i], a[min] = a[min], a[i]  # 정렬 할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환 
# if __name__ == '__main__':
#     print('단순 선택 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     selection_sort(x)  # 배열 x를 단순 선택 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-7] 단순 삽입 정렬 알고리즘 구현하기
# from typing import MutableSequence
# def insertion_sort(a: MutableSequence) -> None:
#     """단순 삽입 정렬"""
#     n = len(a)
#     for i in range(1, n):
#         j = i
#         tmp = a[i]
#         while j > 0 and a[j - 1] > tmp:
#             a[j] = a[j - 1]
#             j -= 1
#         a[j] = tmp
# if __name__ == '__main__':
#     print('단순 삽입 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     insertion_sort(x)  # 배열 x를 단순 삽입 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-8] 셸 정렬 알고리즘 구현하기
# from typing import MutableSequence
# def shell_sort(a: MutableSequence) -> None:
#     """셸 정렬"""
#     n = len(a)
#     h = n // 2
#     while h > 0:
#         for i in range(h, n):
#             j = i - h
#             tmp = a[i]
#             while j >= 0 and a[j] > tmp:
#                 a[j + h] = a[j]
#                 j -= h
#             a[j + h] = tmp
#         h //= 2
# if __name__ == '__main__':
#     print('셸 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     shell_sort(x)  # 배열 x를 셸 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-9] 셸 정렬 알고리즘 구현하기(h * 3 + 1의 수열 사용)
# from typing import MutableSequence
# def shell_sort(a: MutableSequence) -> None:
#     """셸 정렬(h * 3 + 1의 수열 사용)"""
#     n = len(a)
#     h = 1
#     while h < n // 9:
#         h = h * 3 + 1
#     while h > 0:
#         for i in range(h, n):
#             j = i - h
#             tmp = a[i]
#             while j >= 0 and a[j] > tmp:
#                 a[j + h] = a[j]
#                 j -= h
#             a[j + h] = tmp
#         h //= 3
# if __name__ == '__main__':
#     print('셸 정렬을 수행합니다(h * 3 + 1의 수열 사용).')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     shell_sort(x)  # 배열 x를 셸 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-10] 배열을 두 그룹으로 나누기
# from typing import MutableSequence
# def partition(a: MutableSequence) -> None:
#     """배열을 분할하여 출력"""
#     n = len(a)
#     pl = 0         # 왼쪽 커서
#     pr = n - 1     # 오른쪽 커서
#     x = a[n // 2]  # 피벗(가운데 원소)
#     while pl <= pr:
#         while a[pl] < x: pl += 1
#         while a[pr] > x: pr -= 1
#         if pl <= pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
#     print(f'피벗은 {x}입니다.')
#     print('피벗 이하인 그룹입니다.')
#     print(*a[0 : pl])           # a[0] ~ a[pl - 1]
#     if pl > pr + 1:
#         print('피벗과 일치하는 그룹입니다.')
#         print(*a[pr + 1 : pl])  # a[pr + 1] ~ a[pl - 1]
#     print('피벗 이상인 그룹입니다.')
#     print(*a[pr + 1 : n])       # a[pr + 1] ~ a[n - 1]
# if __name__ == '__main__':
#     print('배열을 나눕니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     partition(x)         # 배열 x를 나누어서 출력

# [Do it! 실습 6-10] 퀵 정렬 알고리즘 구현
# from typing import MutableSequence
# def qsort(a: MutableSequence, left: int, right: int) -> None:
#     """a[left] ~ a[right]를 퀵 정렬"""
#     pl = left                   # 왼쪽 커서
#     pr = right                  # 오른쪽 커서
#     x = a[(left + right) // 2]  # 피벗(가운데 요소)
#     while pl <= pr:    # 실습 6-10과 같은 while 문
#         while a[pl] < x: pl += 1
#         while a[pr] > x: pr -= 1
#         if pl <= pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
#     if left < pr: qsort(a, left, pr)
#     if pl < right: qsort(a, pl, right)
# def quick_sort(a: MutableSequence) -> None:
#     """퀵 정렬"""
#     qsort(a, 0, len(a) - 1)
# if __name__ == '__main__':
#     print('퀵 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num   # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     quick_sort(x)      # 배열 x를 퀵 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-12] 퀵 정렬 알고리즘 구현(비재귀적인 퀵 정렬)
# from stack import Stack  # 실습 4C-1의 파일 import
# from typing import MutableSequence
# def qsort(a: MutableSequence, left: int, right: int) -> None:
#     """a[left] ~ a [right]를 퀵 정렬(비재귀 버전)"""
#     range = Stack(right - left + 1)  # 스택 생성
#     range.push((left, right))
#     while not range.is_empty():
#         pl, pr = left, right = range.pop()  # 왼쪽, 오른쪽 커서를 꺼냄
#         x = a[(left + right) // 2]          # 피벗(중앙 요소)
#         while pl <= pr:
#             while a[pl] < x: pl += 1
#             while a[pr] > x: pr -= 1
#             if pl <= pr:                        # 실습 6-10, 실습 6-11과 같음
#                 a[pl], a[pr] = a[pr], a[pl]
#                 pl += 1
#                 pr -= 1
#         if left < pr: range.push((left, pr))    # 왼쪽 그룹의 커서를 저장
#         if pl < right: range.push((pl, right))  # 오른쪽 그룹의 커서를 저장
# def quick_sort(a: MutableSequence) -> None:
#     """퀵 정렬"""
#     qsort(a, 0, len(a) - 1)
# if __name__ == '__main__':
#     print('비재귀적인 퀵 정렬')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     quick_sort(x)       # 배열 x를 퀵 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-13] 퀵 정렬 알고리즘 구현하기(원소 수가 9개 미만인 경우 단순 삽입 정렬)
# from typing import MutableSequence
# def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
#     """a[idx1], a[idx2], a[idx3]을 오름차순으로 정렬하고 가운데 값의 인덱스를 반환"""
#     if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
#     if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
#     if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
#     return idx2
# def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
#     """a[left] ~ a[right]를 단순 삽입 정렬"""
#     for i in range(left + 1, right + 1):
#         j = i
#         tmp = a[i]
#         while j > 0 and a[j - 1] > tmp:
#             a[j] = a[j - 1]
#             j -= 1
#         a[j] = tmp
# def qsort(a: MutableSequence, left: int, right: int) -> None:
#     """a[left] ~ a[right]를 퀵 정렬"""
#     if right - left < 9:            # 원소 수가 9개 미만이면 단순 삽입 정렬을 호출
#         insertion_sort(a, left, right)
#     else:                           # 원소 수가 9개 이상이면 퀵 정렬을 수행
#         pl = left                   # 왼쪽 커서
#         pr = right                  # 오른쪽 커서
#         m = sort3(a, pl, (pl + pr) // 2, pr)
#         x = a[m]

#         a[m], a[pr - 1] = a[pr - 1], a[m]
#         pl += 1
#         pr -= 2
#         while pl <= pr:
#             while a[pl] < x: pl += 1
#             while a[pr] > x: pr -= 1
#             if pl <= pr:
#                 a[pl], a[pr] = a[pr], a[pl]
#                 pl += 1
#                 pr -= 1
#         if left < pr: qsort(a, left, pr)
#         if pl < right: qsort(a, pl, right)
# def quick_sort(a: MutableSequence) -> None:
#     """퀵 정렬"""
#     qsort(a, 0, len(a) - 1)
# if __name__ == '__main__':
#     print('퀵 정렬을 합니다(원소 수가 9개 미만이면 단순 삽입 정렬).')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     quick_sort(x)       # 배열 x를 퀵 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-14] 정렬을 마친 두 배열을 병합하기
# from typing import Sequence, MutableSequence
# def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
#     """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
#     pa, pb, pc = 0, 0, 0                 # 각 배열의 커서
#     na, nb, nc = len(a), len(b), len(c)  # 각 배열의 원소수 
#     while pa < na and pb < nb:  # pa와 pb를 비교하여 작은 값을 pc에 저장
#         if a[pa] <= b[pb]:
#             c[pc] = a[pa]
#             pa += 1
#         else:
#             c[pc] = b[pb]
#             pb += 1
#         pc += 1
#     while pa < na:              # a에 남은 원소를 복사
#         c[pc] = a[pa]
#         pa += 1
#         pc += 1
#     while pb < nb:              # b에 남은 원소를 복사
#         c[pc] = b[pb]
#         pb += 1
#         pc += 1
# if __name__ == '__main__':
#     a = [2, 4, 6, 8, 11, 13]
#     b = [1, 2, 3, 4, 9, 16, 21]
#     c = [None] * (len(a) + len(b))
#     print('정렬을 마친 두 배열의 병합을 수행합니다.')
#     merge_sorted_list(a, b, c)  # 배열 a와 b를 병합하여 c에 저장
#     print('배열 a와 b를 병합하여 배열 c에 저장하였습니다.')
#     print(f'배열 a: {a}')
#     print(f'배열 b: {b}')
#     print(f'배열 c: {c}')

# [Do it! 실습 6-15] 병합 정렬 알고리즘 구현하기
# from typing import MutableSequence
# def merge_sort(a: MutableSequence) -> None:
#     """병합 정렬"""
#     def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
#         """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
#         if left < right:
#             center = (left + right) // 2
#             _merge_sort(a, left, center)            # 배열 앞부분을 병합 정렬
#             _merge_sort(a, center + 1, right)       # 배열 뒷부분을 병합 정렬
#             p = j = 0
#             i = k = left
#             while i <= center:
#                  buff[p] = a[i]
#                  p += 1
#                  i += 1
#             while i <= right and j < p:
#                  if buff[j] <= a[i]:
#                      a[k] = buff[j]
#                      j += 1
#                  else:
#                      a[k] = a[i]
#                      i += 1
#                  k += 1
#             while j < p:
#                 a[k] = buff[j]
#                 k += 1
#                 j += 1
#     n = len(a)
#     buff = [None] * n           # 작업용 배열을 생성
#     _merge_sort(a, 0, n - 1)    # 배열 전체를 병합 정렬
#     del buff                    # 작업용 배열을 소멸
# if __name__ == '__main__':
#     print('병합 정렬을 수행합니다')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     merge_sort(x)       # 배열 x를 병합 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-16] 힙 정렬 알고리즘 구현하기
# from typing import MutableSequence
# def heap_sort(a: MutableSequence) -> None:
#     """힙 정렬"""
#     def down_heap(a: MutableSequence, left: int, right: int) -> None:
#         """a[left] ~ a[right]를 힙으로 만들기"""
#         temp = a[left]      # 루트
#         parent = left
#         while parent < (right + 1) // 2:
#             cl = parent * 2 + 1     # 왼쪽 자식
#             cr = cl + 1             # 오른쪽 자식
#             child = cr if cr <= right and a[cr] > a[cl] else cl  # 큰 값을 선택합니다.
#             if temp >= a[child]:
#                 break
#             a[parent] = a[child]
#             parent = child
#         a[parent] = temp
#     n = len(a)
#     for i in range((n - 1) // 2, -1, -1):   # a[i] ~ a[n-1]을 힙으로 만들기
#         down_heap(a, i, n - 1)
#     for i in range(n - 1, 0, -1):
#         a[0], a[i] = a[i], a[0]     # 최댓값인 a[0]과 마지막 원소 a[i]를 교환
#         down_heap(a, 0, i - 1)      # a[0] ~ a[i-1]을 힙으로 만들기
# if __name__ == '__main__':
#     print('힙 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요. : '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     heap_sort(x)        # 배열 x를 힙 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-17] 도수 정렬 알고리즘 구현하기
# from typing import MutableSequence
# def fsort(a: MutableSequence, max: int) -> None:
#     """도수 정렬(배열 원솟값은 0 이상 max 이하)"""
#     n = len(a)           # 정렬할 배열 a
#     f = [0] * (max + 1)  # 누적 도수 분포표 배열 f
#     b = [0] * n          # 작업용 배열 b
#     for i in range(n):              f[a[i]] += 1                     # [1단계]
#     for i in range(1, max + 1):     f[i] += f[i - 1]                 # [2단계]
#     for i in range(n - 1, -1, -1):  f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [3단계]
#     for i in range(n):              a[i] = b[i]                      # [4단계]
# def counting_sort(a: MutableSequence) -> None:
#     """도수 정렬"""
#     fsort(a, max(a))
# if __name__ == '__main__':
#     print('도수 정렬을 합니다.')
#     num = int(input('원소 수를 입력하세요. : '))
#     x = [None] * num  # 원소 수가 num인 배열을 생성
#     for i in range(num):  # 양수만 입력받음
#         while True:
#             x[i] = int(input(f'x[{i}] : '))
#             if x[i] >= 0: break
#     counting_sort(x)  # 배열 x를 도수 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6C-1] 이진 삽입 정렬 알고리즘 구현하기
# from typing import MutableSequence
# def binary_insertion_sort(a: MutableSequence) -> None:
#     """이진 삽입 정렬"""
#     n = len(a)
#     for i in range(1, n):
#         key = a[i]
#         pl = 0      # 검색 범위의 맨 앞 원소 인덱스
#         pr = i - 1  # 검색 범위의 맨 끝 원소 인덱스
#         while True:
#             pc = (pl + pr) // 2  # 검색 범위의 중앙 원소 인덱스
#             if a[pc] == key:     # 검색 성공
#                 break
#             elif a[pc] < key:
#                 pl = pc + 1
#             else:
#                 pr = pc - 1
#             if pl > pr:
#                 break
#         pd = pc + 1 if pl <= pr else pr + 1  # 삽입할 위치의 인덱스
#         for j in range(i, pd, -1):
#             a[j] = a[j - 1]
#         a[pd] = key
# if __name__ == "__main__":
#     print("이진 삽입 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num          # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#     binary_insertion_sort(x)  # 배열 x를 이진 삽입 정렬
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# [Do it! 실습 6C-2] 이진 삽입 정렬 알고리즘의 구현(bisect.insort 사용)
# from typing import MutableSequence
# import bisect
# def binary_insertion_sort(a: MutableSequence) -> None:
#     """이진 삽입 정렬(bisect.insort을 사용)"""
#     for i in range(1, len(a)):
#         bisect.insort(a, a.pop(i), 0, i)
# if __name__ == '__main__':
#     print('이진 삽입 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num            # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     binary_insertion_sort(x)    # 배열 x를 이진 삽입 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6C-3] 퀵 정렬 알고리즘 구현(배열을 나누는 과정 출력)
# from typing import MutableSequence
# def qsort(a: MutableSequence, left: int, right: int) -> None:
#     """a[left] ~ a[right]를 퀵 정렬(배열을 나누는 과정 출력)"""
#     pl = left                   # 왼쪽 커서
#     pr = right                  # 오른쪽 커서
#     x = a[(left + right) // 2]  # 피벗(가운데 원소)
#     print(f'a[{left}] ~ a[{right}]: ', *a[left : right + 1])  # 새로 추가된 부분
#     while pl <= pr:                     
#         while a[pl] < x: pl += 1
#         while a[pr] > x: pr -= 1
#         if pl <= pr:                    
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
#     if left < pr: qsort(a, left, pr)   
#     if pl < right: qsort(a, pl, right)
# def quick_sort(a: MutableSequence) -> None:
#     """퀵 정렬"""
#     qsort(a, 0, len(a) - 1)
# if __name__ == '__main__':
#     print('퀵 정렬을 수행합니다(배열을 나누는 과정 출력).')
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#     quick_sort(x)       # 배열 x를 퀵 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6C-4] sorted() 함수를 사용하여 정렬하기
# print('sorted() 함수를 사용하여 정렬합니다.')
# num = int(input('원소 수를 입력하세요.: '))
# x = [None] * num    # 원소 수가 num인 배열을 생성
# for i in range(num):
#     x[i] = int(input(f'x[{i}]: '))
# # 배열 x를 오름차순으로 정렬
# x = sorted(x)
# print('오름차순으로 정렬했습니다.')
# for i in range(num):
#     print(f'x[{i}] = {x[i]}')
# # 배열 x를 내림차순으로 정렬
# x = sorted(x, reverse = True)
# print('내림차순으로 정렬했습니다.')
# for i in range(num):
#     print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6C-5] 힙 정렬 알고리즘 구현하기(heapq.push와 heapq.pop를 사용）
# import heapq
# from typing import MutableSequence
# def heap_sort(a: MutableSequence) -> None:
#     """힙 정렬(heapq.push와 heapq.pop를 사용)"""
#     heap = []
#     for i in a:
#         heapq.heappush(heap, i)
#     for i in range(len(a)):
#         a[i] = heapq.heappop(heap)
# if __name__ == '__main__':
#     print('힙 정렬을 수행합니다(heapq.push와 heapq.pop를 사용).')
#     num = int(input('원소 수를 입력하세요. : '))
#     x = [None] * num    # 원소 수가 num인 배열을 생성
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#     heap_sort(x)        # 배열 x를 힙 정렬
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')


# [CHAP07]

# 문자열에 포함되어 있는 문자열을 검색(find 계열 함수）
# txt = input('문자열 txt: ')  # 문자열 나열
# ptn = input('문자열 ptn: ')  # 검색할 문자
# c = txt.count(ptn)
# if c == 0:                                                  # 포함된 문자가 없음
#     print('ptn은 txt에 포함되어 있지 않습니다.')
# elif c == 1:                                                # 포함된 문자가 １개만 있는 경우
#     print('ptn이 txt에 포함되어 있는 인덱스: ', txt.find(ptn))
# else:                                                       # 포함된 문자가 2개 이상 있는 경우
#     print('ptn이 txt에 포함되어 있는 맨 앞 인덱스: ', txt.find(ptn))
#     print('ptn이 txt에 포함되어 있는 맨 끝 인덱스: ', txt.rfind(ptn))

# 문자열에 포함되어 있는 문자열을 검색(index 계열 함수)
# txt = input('문자열 txt: ')
# ptn = input('문자열 ptn: ')
# c = txt.count(ptn)
# if c == 0:                                                  # 포함된 문자가 없음
#     print('ptn은 txt에 포함되어 있지 않습니다.')
# elif c == 1:                                                # 포함된 문자가 １개만 있는 경우
#     print('ptn이 txt에 포함되어 있는 인덱스: ', txt.index(ptn))
# else:                                                       # 포함된 문자가 2개 이상 있는 경우
#     print('ptn이 txt에 포함되어 있는 맨 앞 인덱스: ', txt.index(ptn))
#     print('ptn이 txt에 포함되어 있는 맨 끝 인덱스: ', txt.rindex(ptn))

# [Do it! 실습 7-1] 브루트 포스법으로 문자열 검색하기
# def bf_match(txt: str, pat: str) -> int:
#     """브루트 포스법으로 문자열 검색"""
#     pt = 0  # txt(텍스트)를 따라가는 커서
#     pp = 0  # pat(패턴)를 따라가는 커서
#     while pt != len(txt) and pp != len(pat):
#         if txt[pt] == pat[pp]:
#             pt += 1
#             pp += 1
#         else:
#             pt = pt - pp + 1
#             pp = 0
#     return pt - pp if pp == len(pat) else -1
# if __name__ == '__main__':
#     s1 = input('텍스트를 입력하세요.: ')  # 텍스트용 문자열
#     s2 = input('패턴을 입력하세요.: ')    # 패턴용 문자열
#     idx = bf_match(s1, s2)  # 문자열 s1~s2를 브루트 포스법으로 검색
#     if idx == -1:
#         print('텍스트 안에 패턴이 존재하지 않습니다.')
#     else:
#         print(f'{(idx + 1)}번째 문자에서 일치합니다.')

# [Do it! 실습 7-2] KMP법으로 문자열 검색하기
# def kmp_match(txt: str, pat: str) -> int:
#     """KMP법에 의한 문자열 검색"""
#     pt = 1  # txt를 따라가는 커서
#     pp = 0  # pat를 따라가는 커서
#     skip = [0] * (len(pat) + 1)  # 건너뛰기 표
#     # 건너뛰기 표 만들기
#     skip[pt] = 0
#     while pt != len(pat):
#         if pat[pt] == pat[pp]:
#             pt += 1
#             pp += 1
#             skip[pt] = pp
#         elif pp == 0:
#             pt += 1
#             skip[pt] = pp
#         else:
#             pp = skip[pp]
#     # 검색하기
#     pt = pp = 0
#     while pt != len(txt) and pp != len(pat):
#         if txt[pt] == pat[pp]:
#             pt += 1
#             pp += 1
#         elif pp == 0:
#             pt += 1
#         else:
#             pp = skip[pp]
#     return pt - pp if pp == len(pat) else -1
# if __name__ == '__main__':
#     s1 = input('텍스트를 입력하세요.: ')  # 텍스트용 문자열
#     s2 = input('패턴을 입력하세요.: ')    # 패턴용 문자열
#     idx = kmp_match(s1, s2)  # 문자열 s1~s2를 KMP법으로 검색
#     if idx == -1:
#         print('텍스트 안에 패턴이 존재하지 않습니다.')
#     else:
#         print(f'{(idx + 1)}번째 문자에서 일치합니다.')

# [Do it! 실습 7-3] 보이어 무어법으로 문자열 검색하기(0~255 문자)
# def bm_match(txt: str, pat: str) -> int:
#     """보이어 무어법에 의한 문자열 검색"""
#     skip = [None] * 256  # 건너뛰기 표
#     # 건너뛰기 표 만들기
#     for pt in range(256):
#         skip[pt] = len(pat)
#     for pt in range(len(pat)):
#         skip[ord(pat[pt])] = len(pat) - pt - 1
#     # 검색하기
#     while pt < len(txt):
#         pp = len(pat) - 1
#         while txt[pt] == pat[pp]:
#             if pp == 0:
#                 return pt
#             pt -= 1
#             pp -= 1
#         pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
#               else len(pat) - pp
#     return -1
# if __name__ == '__main__':
#     s1 = input('텍스트를 입력하세요.: ')  # 텍스트 문자열
#     s2 = input('패턴을 입력하세요.: ')    # 패턴 문자열
#     idx = bm_match(s1, s2)  # 문자열 s1~s2를 KMP법으로 검색
#     if idx == -1:
#         print('텍스트 안에 패턴이 존재하지 않습니다.')
#     else:
#         print(f'{(idx + 1)}번째 문자에서 일치합니다.')


# [CHAP08]

# [Do it! 실습 8-1] 포인터로 연결 리스트 만들기
# from __future__ import annotations
# from typing import Any, Type
# class Node:
#     """연결 리스트용 노드 클래스"""
#     def __init__(self, data: Any = None, next: Node = None):
#         """초기화"""
#         self.data = data  # 데이터
#         self.next = next  # 뒤쪽 포인터

# Do it! 실습 8-1 [B]
# class LinkedList:
#     """연결 리스트 클래스"""
#     def __init__(self) -> None:
#         """초기화"""
#         self.no = 0          # 노드의 개수
#         self.head = None     # 머리 노드
#         self.current = None  # 주목 노드
#     def __len__(self) -> int:
#         """연결 리스트의 노드 개수를 반환"""
#         return self.no

# Do it! 실습 8-1 [C]
    # def search(self, data: Any) -> int:
    #     """data와 값이 같은 노드를 검색"""
    #     cnt = 0
    #     ptr = self.head
    #     while ptr is not None:
    #         if ptr.data == data:
    #             self.current = ptr
    #             return cnt
    #         cnt += 1
    #         ptr = ptr.next
    #     return -1
    # def __contains__(self, data: Any) -> bool:
    #     """연결 리스트에 data가 포함되어 있는가?"""
    #     return self.search(data) >= 0

# Do it! 실습 8-1 [D]
#     def add_first(self, data: Any) -> None:
#         """맨 앞에 노드를 삽입"""
#         ptr = self.head  # 삽입 전의 머리 노드
#         self.head = self.current = Node(data, ptr)
#         self.no += 1

# Do it! 실습 8-1 [E]
#     def add_last(self, data: Any):
#         """맨 끝에 노드를 삽입"""
#         if self.head is None :    # 리스트가 비어 있으면
#             self.add_first(data)  # 맨앞에 노드 삽입
#         else:
#             ptr = self.head
#             while ptr.next is not None:
#                 ptr = ptr.next  # while문을 종료할 때 ptr은 꼬리 노드를 참조
#             ptr.next = self.current = Node(data, None)
#             self.no += 1

# Do it! 실습 8-1 [F]
#     def remove_first(self) -> None:
#         """머리 노드를 삭제"""
#         if self.head is not None:  # 리스트가 비어 있으면
#             self.head = self.current = self.head.next
#         self.no -= 1

# Do it! 실습 8-1 [G]
#     def remove_last(self):
#         """꼬리 노드 삭제"""
#         if self.head is not None:
#             if self.head.next is None :  # 노드가 1개 뿐이라면
#                 self.remove_first()      # 머리 노드를 삭제
#             else:
#                 ptr = self.head  # 스캔 중인 노드
#                 pre = self.head  # 스캔 중인 노드의 앞쪽 노드
#                 while ptr.next is not None:
#                     pre = ptr
#                     ptr = ptr.next # while문 종료시 ptr은 꼬리 노드를 참조하고 pre는 맨끝에서 두 번째 노드를 참조
#                 pre.next = None  # pre는 삭제 뒤 꼬리 노드
#                 self.current = pre
#                 self.no -= 1

# Do it! 실습 8-1 [H]
#     def remove(self, p: Node) -> None:
#         """노드 p를 삭제"""
#         if self.head is not None:
#             if p is self.head:       # p가 머리 ​​노드이면
#                 self.remove_first()  # 머리 노드를 삭제
#             else:
#                 ptr = self.head
#                 while ptr.next is not p:
#                     ptr = ptr.next
#                     if ptr is None:
#                         return  # ptr은 리스트에 존재하지 않음
#                 ptr.next = p.next
#                 self.current = ptr
#                 self.no -= 1
#     def remove_current_node(self) -> None:
#         """주목 노드를 삭제"""
#         self.remove(self.current)
#     def clear(self) -> None:
#         """전체 노드를 삭제"""
#         while self.head is not None:  # 전체가 비어 있게 될 때까지
#             self.remove_first()       # 머리 노드를 삭제
#         self.current = None
#         self.no = 0
#     def next(self) -> bool:
#         """주목 노드를 한 칸 뒤로 진행"""
#         if self.current is None or self.current.next is None:
#             return False  # 진행할 수 없음
#         self.current = self.current.next
#         return True

# Do it! 실습 8-1 [I]
#     def print_current_node(self) -> None:
#         """주목 노드를 출력"""
#         if self.current is None:
#             print('주목 노드가 존재하지 않습니다.')
#         else:
#             print(self.current.data)
#     def print(self) -> None:
#         """모든 노드를 출력"""
#         ptr = self.head
#         while ptr is not None:
#             print(ptr.data)
#             ptr = ptr.next

# Do it! 실습 8-1 [J]
#     def __iter__(self) -> LinkedListIterator:
#         """이터레이터(반복자)를 반환"""
#         return LinkedListIterator(self.head)
# class LinkedListIterator:
#     """클래스 LinkedList의 이터레이터(반복자)용 클래스"""
#     def __init__(self, head: Node):
#         self.current = head
#     def __iter__(self) -> LinkedListIterator:
#         return self
#     def __next__(self) -> Any:
#         if self.current is None:
#             raise StopIteration
#         else:
#             data = self.current.data
#             self.current = self.current.next
#             return data

# [Do it! 실습 8-2] 포인터로 이용한 연결 리스트 클래스 LinkedList 사용하기
# from enum import Enum
# from linked_list import LinkedList
# Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
#                      '꼬리노드삭제', '주목노드출력', '주목노드이동',
#                      '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
#                      '모든노드출력', '스캔', '종료',])
# def select_Menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='  ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
# lst = LinkedList()  # 연결 리스트를 생성
# while True:
#     menu = select_Menu()  # 메뉴 선택
#     if menu == Menu.머리에노드삽입:  # 맨 앞에 노드 삽입
#         lst.add_first(int(input('머리에 넣을 값을 입력하세요.: ')))
#     elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드 삽입
#         lst.add_last(int(input('꼬리에 넣을 값을 입력하세요.: ')))
#     elif menu == Menu.머리노드삭제:  # 맨 앞 노드 삭제
#         lst.remove_first()
#     elif menu == Menu.꼬리노드삭제:  # 맨 끝 노드 삭제
#         lst.remove_last()
#     elif menu == Menu.주목노드출력:  # 주목 노드 출력
#         lst.print_current_node()
#     elif menu == Menu.주목노드이동:  # 주목 노드를 한 칸 뒤로 이동
#         lst.next()
#     elif menu == Menu.주목노드삭제:  # 주목 노드 삭제
#         lst.remove_current_node()
#     elif menu == Menu.모든노드삭제:  # 모든 노드를 삭제
#         lst.clear()
#     elif menu == Menu.검색:  # 노드를 검색
#         pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
#         if pos >= 0:
#             print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
#         else:
#             print('해당 데이터가 없습니다.')
#     elif menu == Menu.멤버십판단:  # 멤버십 판단
#         print('그 값의 데이터는 포함되어' + (' 있습니다.' if int(input('멤버십 판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))
#     elif menu == Menu.모든노드출력:  # 모든 노드 출력
#         lst.print()
#     elif menu == Menu.스캔:  # 모든 노드 스캔
#         for e in lst:
#             print(e)
#     else:  # 종료
#         break

# [Do it! 실습 8-3] 커서를 이용한 선형 리스트 클래스 ArrayLinkedList 사용하기
# from enum import Enum
# from array_list import ArrayLinkedList
# Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
#                      '꼬리노드삭제', '주목노드출력', '주목노드이동',
#                      '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
#                      '모든노드출력', '스캔', '종료'])
# def select_Menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '  ', end='')
#         n = int(input(' : '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
# lst = ArrayLinkedList(100)  # 선형 리스트를 생성
# while True:
#     menu = select_Menu()  # 메뉴 선택
#     if menu == Menu.머리에노드삽입:               # 맨 앞에 노드 삽입
#         lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))                                  
#     elif menu == Menu.꼬리에노드삽입:             # 맨 끝에 노드 삽입
#         lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))
#     elif menu == Menu.머리노드삭제:             # 맨 앞 노드를 삭제
#         lst.remove_first()
#     elif menu == Menu.꼬리노드삭제:             # 맨 끝 노드를 삭제
#         lst.remove_last()
#     elif menu == Menu.주목노드출력:             # 주목 노드를 출력
#         lst.print_current_node()
#     elif menu == Menu.주목노드이동:             # 주목 노드를 한 칸 뒤로 이동
#         lst.next()
#     elif menu == Menu.주목노드삭제:             # 주목 노드를 삭제
#         lst.remove_current_node()
#     elif menu == Menu.모든노드삭제:             # 모두 삭제
#         lst.clear()
#     elif menu == Menu.검색:                     # 검색
#         pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
#         if pos >= 0:
#             print(f'이 키를 갖는 데이터는 {pos + 1}번째에 있습니다.')
#         else:
#             print('해당 데이터가 없습니다.')
#     elif menu == Menu.멤버십판단:               # 멤버십을 판단
#         print('그 값의 데이터는 포함되어'
#               +('있습니다.' if int(input('판단할 값을 입력하세요.')) in lst else ' 있지 않습니다.'))
#     elif menu == Menu.모든노드출력:             # 모든 노드를 출력
#         lst.print()
#     elif menu == Menu.스캔:                     # 모든 노드 스캔
#         for e in lst:
#              print(e)
#     else:                                       # 종료
#         break

# [Do it! 실습 8-3] 커서로 선형 리스트 만들기
# from __future__ import annotations
# from typing import Any, Type
# Null = -1
# class Node:
#     """선형 리스트용 노드 클래스(배열 커서 버전)"""
#     def __init__(self, data = Null, next = Null, dnext = Null):
#         """초기화"""
#         self.data  = data   # 데이터
#         self.next  = next   # 리스트의 뒤쪽 포인터
#         self.dnext = dnext  # 프리 리스트의 뒤쪽 포인터
# class ArrayLinkedList:
#     """선형 리스트 클래스(배열 커서 버전)"""
#     def __init__(self, capacity: int):
#         """초기화"""
#         self.head = Null                   # 머리 노드
#         self.current = Null                # 주목 노드
#         self.max = Null                    # 사용 중인 맨끝 레코드
#         self.deleted = Null                # 프리 리스트의 머리 노드
#         self.capacity = capacity           # 리스트의 크기
#         self.n = [Node()] * self.capacity  # 리스트 본체
#         self.no = 0
#     def __len__(self) -> int:
#         """선형 리스트의 노드 수를 반환"""
#         return self.no
#     def get_insert_index(self):
#         """다음에 삽입할 레코드의 첨자를 구합니다"""
#         if self.deleted == Null:  # 삭제 레코드는 존재하지 않습니다
#             if self.max+1 < self.capacity:
#                 self.max += 1
#                 return self.max   # 새 레코드를 사용
#             else:
#                 return Null       # 크기 초과
#         else:
#             rec = self.deleted                # 프리 리스트에서
#             self.deleted = self.n[rec].dnext  # 맨 앞 rec를 꺼내기
#             return rec
#     def delete_index(self, idx: int) -> None:
#         """레코드 idx를 프리 리스트에 등록"""
#         if self.deleted == Null:      # 삭제 레코드는 존재하지 않습니다
#             self.deleted = idx        # idx를 프리 리스트의
#             self.n[idx].dnext = Null  # 맨 앞에 등록
#         else:
#             rec = self.deleted        # idx를 프리 리스트의
#             self.deleted = idx        # 맨 앞에 삽입
#             self.n[idx].dnext = rec
#     def search(self, data: Any) -> int:
#         """data와 값이 같은 노드를 검색"""
#         cnt = 0
#         ptr = self.head             # 현재 스캔 중인 노드
#         while ptr != Null:
#             if self.n[ptr].data == data:
#                 self.current = ptr
#                 return cnt          # 검색 성공
#             cnt += 1
#             ptr = self.n[ptr].next  # 뒤쪽 노드에 주목
#         return Null                 # 검색 실패
#     def __contains__(self, data: Any) -> bool:
#         """선형 리스트에 data가 포함되어 있는지 확인"""
#         return self.search(data) >= 0
#     def add_first(self, data: Any):
#         """머리 노드에 삽입"""
#         ptr = self.head                     # 삽입하기 전의 머리 노드
#         rec = self.get_insert_index()
#         if rec != Null:
#             self.head = self.current = rec  # rec번째 레코드에 삽입
#             self.n[self.head] = Node(data, ptr)
#             self.no += 1
#     def add_last(self, data: Any) -> None:
#         """꼬리 노드에 삽입"""
#         if self.head == Null:     # 리스트가 비어 있으면
#             self.add_first(data)  # 맨 앞에 노드 삽입
#         else:
#             ptr = self.head
#             while self.n[ptr].next != Null:
#                 ptr = self.n[ptr].next
#             rec = self.get_insert_index()
#             if rec != Null:       # rec번째 레코드에 삽입
#                 self.n[ptr].next = self.current = rec
#                 self.n[rec] = Node(data)
#                 self.no += 1
#     def remove_first(self) -> None:
#         """머리 노드를 삭제"""
#         if self.head != Null:  # 리스트가 비어 있으면
#             ptr = self.n[self.head].next
#             self.delete_index(self.head)
#             self.head = self.current = ptr
#             self.no -= 1
#     def remove_last(self) -> None:
#         """꼬리 노드를 삭제"""
#         if self.head != Null:
#             if self.n[self.head].next == Null:  # 노드가 1개 뿐이면
#                 self.remove_first()             # 머리 노드를 삭제
#             else:
#                 ptr = self.head                 # 스캔 중인 노드
#                 pre = self.head                 # 스캔 중인 노드의 앞쪽 노드
#                 while self.n[ptr].next != Null:
#                     pre = ptr
#                     ptr = self.n[ptr].next
#                 self.n[pre].next = Null  # pre는 삭제한 뒤의 꼬리 노드
#                 self.delete_index(ptr)
#                 self.current = pre
#                 self.no -= 1
#     def remove(self, p: int) -> None:
#         """레코드 p를 삭제"""
#         if self.head != Null:
#             if p == self.head:       # p가 머리 노드면
#                 self.remove_first()  # 머리 노드를 삭제
#             else:
#                 ptr = self.head
#                 while self.n[ptr].next != p:
#                     ptr = self.n[ptr].next
#                     if ptr == Null:
#                         return  # p는 리스트에 존재하지 않음
#                 #self.n[ptr].next = Null
#                 self.delete_index(p)
#                 self.n[ptr].next = self.n[p].next
#                 self.current = ptr
#                 self.no -= 1
#     def remove_current_node(self) -> None:
#         """주목 노드를 삭제"""
#         self.remove(self.current)
#     def clear(self) -> None:
#         """모든 노드를 삭제"""
#         while self.head != Null:  # 리스트 전체가 빌 때까지
#             self.remove_first()   # 머리 노드를 삭제
#         self.current = Null
#     def next(self) -> bool:
#         """주목 노드를 한 칸 뒤로 진행"""
#         if self.current == Null or self.n[self.current].next == Null:
#             return False  # 진행할 수 없음
#         self.current = self.n[self.current].next
#         return True
#     def print_current_node(self) -> None:
#         """주목 노드를 출력"""
#         if self.current == Null:
#             print('주목 노드가 없습니다.')
#         else:
#             print(self.n[self.current].data)
#     def print(self) -> None:
#         """모든 노드를 출력"""
#         ptr = self.head
#         while ptr != Null:
#             print(self.n[ptr].data)
#             ptr = self.n[ptr].next
#     def dump(self) -> None:
#         """배열을 덤프"""
#         for i in self.n:
#             print(f'[{i}]  {i.data} {i.next} {i.dnext}')
#     def __iter__(self) -> ArrayLinkedListIterator:
#         """이터레이터를 반환"""
#         return ArrayLinkedListIterator(self.n, self.head)
# class ArrayLinkedListIterator:
#     """클래스 ArrayLinkedList의 이터레이터용 클래스"""
#     def __init__(self, n: int, head: int):
#         self.n = n
#         self.current = head
#     def __iter__(self) -> ArrayLinkedListIterator:
#         return self
#     def __next__(self) -> Any:
#         if self.current == Null:
#             raise StopIteration
#         else:
#             data = self.n[self.current].data
#             self.current = self.n[self.current].next
#             return data

# 원형 이중 연결 리스트 구현하기
# Do it! 실습 8-5 [A] 
# from __future__ import annotations
# from typing import Any, Type
# class Node:
#     """원형 이중 연결 리스트용 노드 클래스"""
#     def __init__(self, data: Any = None, prev: Node = None,
#                        next: Node = None) -> None:
#         """초기화"""
#         self.data = data          # 데이터
#         self.prev = prev or self  # 앞쪽 포인터
#         self.next = next or self  # 뒤쪽 포인터
# class DoubleLinkedList:
#     """원형 이중 연결 리스트 클래스"""
#     def __init__(self) -> None:
#         """초기화"""
#         self.head = self.current = Node()  # 더미 노드를 생성
#         self.no = 0
#     def __len__(self) -> int:
#         """선형 리스트의 노드 수를 반환"""
#         return self.no
#     def is_empty(self) -> bool:
#         """리스트가 비어 있는가?"""
#         return self.head.next is self.head  

# Do it! 실습 8-5 [B]
#     def search(self, data: Any) -> Any:
#         """data와 값이 같은 노드를 검색"""
#         cnt = 0
#         ptr = self.head.next  # 현재 스캔 중인 노드
#         while ptr is not self.head:
#             if data == ptr.data:
#                 self.current = ptr
#                 return cnt  # 검색 성공
#             cnt += 1
#             ptr = ptr.next  # 뒤쪽 노드에 주목
#         return -1           # 검색 실패
#     def __contains__(self, data: Any) -> bool:
#         """연결 리스트에 data가 포함되어 있는가?"""
#         return self.search(data) >= 0

# Do it! 실습 8-5 [C]
#     def print_current_node(self) -> None:
#         """주목 노드를 출력"""
#         if self.is_empty():
#             print('주목 노드는 없습니다.')
#         else:
#             print(self.current.data)
#     def print(self) -> None:
#         """모든 노드를 출력"""
#         ptr = self.head.next  # 더미 노드의 뒤쪽 노드
#         while ptr is not self.head:
#             print(ptr.data)
#             ptr = ptr.next
#     def print_reverse(self) -> None:
#         """모든 노드를 역순으로 출력"""
#         ptr = self.head.prev  # 더미 노드의 앞쪽 노드
#         while ptr is not self.head:
#             print(ptr.data)
#             ptr = ptr.prev
#     def next(self) -> bool:
#         """주목 노드를 한 칸 뒤로 이동"""
#         if self.is_empty() or self.current.next is self.head:
#             return False  # 이동할 수 없음
#         self.current = self.current.next
#         return True
#     def prev(self) -> bool:
#         """주목 노드를 한 칸 앞으로 이동"""
#         if self.is_empty() or self.current.prev is self.head:
#             return False  # 이동할 수 없음
#         self.current = self.current.prev
#         return True

# Do it! 실습 8-5[D]
#     def add(self, data: Any) -> None:
#         """주목 노드의 바로 뒤에 노드를 삽입"""
#         node = Node(data, self.current, self.current.next)
#         self.current.next.prev = node
#         self.current.next = node
#         self.current = node
#         self.no += 1
#     def add_first(self, data: Any) -> None:
#         """맨 앞에 노드를 삽입"""
#         self.current = self.head  # 더미 노드 head의 바로 뒤에 삽입
#         self.add(data)
#     def add_last(self, data: Any) -> None:
#         """맨 뒤에 노드를 삽입"""
#         self.current = self.head.prev  # 꼬리 노드 head.prev의 바로 뒤에 삽입
#         self.add(data)

# Do it! 실습 8-5[E]
#     def remove_current_node(self) -> None:
#         """주목 노드 삭제"""
#         if not self.is_empty():
#             self.current.prev.next = self.current.next
#             self.current.next.prev = self.current.prev
#             self.current = self.current.prev
#             self.no -= 1
#             if self.current is self.head:
#                 self.current = self.head.next
#     def remove(self, p: Node) -> None:
#         """노드 p를 삭제"""
#         ptr = self.head.next
#         while ptr is not self.head:
#             if ptr is p:  # p를 발견
#                 self.current = p
#                 self.remove_current_node()
#                 break
#             ptr = ptr.next
#     def remove_first(self) -> None:
#         """머리 노드 삭제"""
#         self.current = self.head.next  # 머리 노드 head.next를 삭제
#         self.remove_current_node()
#     def remove_last(self) -> None:
#         """꼬리 노드 삭제"""
#         self.current = self.head.prev  # 꼬리 노드 head.prev를 삭제
#         self.remove_current_node()
#     def clear(self) -> None:
#         """모든 노드를 삭제"""
#         while not self.is_empty():  # 리스트 전체가 빌 때까지
#             self.remove_first()  # 머리 노드를 삭제
#         self.no = 0

# Do it! 실습 8-5[F]
#     def __iter__(self) -> DoubleLinkedListIterator:
#         """반복자를 반환"""
#         return DoubleLinkedListIterator(self.head)
#     def __reversed__(self) -> DoubleLinkedListReverseIterator:
#         """내림차순 반복자를 반환"""
#         return DoubleLinkedListReverseIterator(self.head)
# class DoubleLinkedListIterator:
#     """DoubleLinkedList의 반복자용 클래스"""
#     def __init__(self, head: Node):
#         self.head = head
#         self.current = head.next
#     def __iter__(self) -> DoubleLinkedListIterator:
#         return self
#     def __next__(self) -> Any:
#         if self.current is self.head:
#             raise StopIteration
#         else:
#             data = self.current.data
#             self.current = self.current.next
#             return data
# class DoubleLinkedListReverseIterator:
#     """DoubleLinkedList의 내림차순 반복자용 클래스"""
#     def __init__(self, head: Node):
#         self.head = head
#         self.current = head.prev
#     def __iter__(self) -> DoubleLinkedListReverseIterator:
#         return self
#     def __next__(self) -> Any:
#         if self.current is self.head:
#             raise StopIteration
#         else:
#             data = self.current.data
#             self.current = self.current.prev
#             return data

# [Do it! 실습 8-6] 원형 이중 연결 리스트 클래스 DoubleLinkedList 구현하기
# from enum import Enum
# from double_list import DoubleLinkedList
# Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입',
#                      '머리노드삭제', '꼬리노드삭제', '주목노드출력',
#                      '주목노드이동', '주목노드역순이동', '주목노드삭제',
#                      '모든노드삭제', '검색', '멤버십판단', '모든노드출력',
#                      '모든노드역순출력', '모든노드스캔', '모든노드역순스캔', '종료'])
# def select_Menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '  ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
# lst = DoubleLinkedList()  # 원형・이중 연결 리스트 생성
# while True:
#     menu = select_Menu()  # 메뉴 선택
#     if menu == Menu.머리에노드삽입:  # 맨 앞에 노드 삽입
#         lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))
#     elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드 삽입
#         lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))
#     elif menu == Menu.주목노드바로뒤삽입:  # 주목 노드 바로 뒤에 삽입
#         lst.add(int(input('주목 노드 바로 뒤에 넣을 값을 입력하세요 : ')))
#     elif menu == Menu.머리노드삭제:  # 맨 앞 노드 삭제
#         lst.remove_first()
#     elif menu == Menu.꼬리노드삭제:  # 맨 끝 노드 삭제
#         lst.remove_last()
#     elif menu == Menu.주목노드출력:  # 주목 노드 출력
#         lst.print_current_node()
#     elif menu == Menu.주목노드이동:  # 주목 노드를 한 칸 뒤로 이동
#         lst.next()
#     elif menu == Menu.주목노드역순이동:  # 주목 노드를 한 칸 앞으로 이동
#         lst.prev()
#     elif menu == Menu.주목노드삭제:  # 주목 노드 삭제
#         lst.remove_current_node()
#     elif menu == Menu.모든노드삭제:  # 모두 삭제
#         lst.clear()
#     elif menu == Menu.검색:  # 검색
#         pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
#         if pos >= 0:
#             print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
#         else:
#             print('해당 데이터가 없습니다.')
#     elif menu == Menu.멤버십판단:  # 멤버십 판단
#         print('그 값의 데이터는 포함되어'
#               +(' 있습니다.' if int(input('판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))
#     elif menu == Menu.모든노드출력:  # 모든 노드를 출력
#         lst.print()
#     elif menu == Menu.모든노드역순출력:  # 모든 노드 역순 출력
#         lst.print_reverse()
#     elif menu == Menu.모든노드스캔:  # 모든 노드 스캔
#         for e in lst:
#              print(e)
#     elif menu == Menu.모든노드역순스캔:  # 모든 노드 역순 스캔
#         for e in reversed(lst):
#              print(e)
#     else:  # 종료
#         break


# [CHAP01]

# [Do it! 실습 9-1] 이진 검색 트리의 구현
# from __future__ import annotations
# from typing import Any, Type
# class Node:
#     """이진 검색 트리의 노드"""
#     def __init__(self, key: Any, value: Any, left: Node = None,
#                  right: Node = None):
#         """생성자"""
#         self.key = key      # 키
#         self.value = value  # 값
#         self.left = left    # 왼쪽 포인터(왼쪽 자식 참조)
#         self.right = right  # 오른쪽 포인터(오른쪽 자식 참조)
# class BinarySearchTree:
#     """이진 검색 트리"""
#     def __init__(self):
#         """초기화"""
#         self.root = None  # 루트

# Do it! 실습 9-1[B]
#     def search(self, key: Any) -> Any:
#         """키 key를 갖는 노드를 검색"""
#         p = self.root           # 루트에 주목
#         while True:
#             if p is None:       # 더 이상 진행할 수 없으면
#                 return None     # 검색 실패
#             if key == p.key:    # key와 노드 p의 키가 같으면
#                 return p.value  # 검색 성공
#             elif key < p.key:   # key 쪽이 작으면
#                 p = p.left      # 왼쪽 서브 트리에서 검색
#             else:               # key 쪽이 크면
#                 p = p.right     # 오른쪽 서브 트리에서 검색

# Do it! 실습 9-1[C]
#     def add(self, key: Any, value: Any) -> bool:
#         """키가 key이고, 값이 value인 노드를 삽입"""
#         def add_node(node: Node, key: Any, value: Any) -> None:
#             """node를 루트로 하는 서브 트리에 키가 key이고, 값이 value인 노드를 삽입"""
#             if key == node.key:
#                 return False  # key가 이진검색트리에 이미 존재
#             elif key < node.key:
#                 if node.left is None:
#                     node.left = Node(key, value, None, None)
#                 else:
#                     add_node(node.left, key, value)
#             else:
#                 if node.right is None:
#                     node.right = Node(key, value, None, None)
#                 else:
#                     add_node(node.right, key, value)
#             return True
#         if self.root is None:
#             self.root = Node(key, value, None, None)
#             return True
#         else:
#             return add_node(self.root, key, value)

# Do it! 실습 9-1[D]
#     def remove(self, key: Any) -> bool:
#         """키가 key인 노드를 삭제"""
#         p = self.root           # 스캔 중인 노드
#         parent = None           # 스캔 중인 노드의 부모 노드
#         is_left_child = True    # p는 parent의 왼쪽 자식 노드인지 확인
#         while True:
#             if p is None:       # 더 이상 진행할 수 없으면
#                 return False    # 그 키는 존재하지 않음
#             if key == p.key:    # key와 노드 p의 키가 같으면
#                 break           # 검색 성공
#             else:
#                 parent = p                  # 가지를 내려가기 전에 부모를 설정
#                 if key < p.key:             # key 쪽이 작으면
#                     is_left_child = True    # 여기서 내려가는 것은 왼쪽 자식
#                     p = p.left              # 왼쪽 서브 트리에서 검색
#                 else:                       # key 쪽이 크면
#                     is_left_child = False   # 여기서 내려가는 것은 오른쪽 자식
#                     p = p.right             # 오른쪽 서브 트리에서 검색
#         if p.left is None:                  # p에 왼쪽 자식이 없으면
#             if p is self.root:
#                 self.root = p.right
#             elif is_left_child:
#                 parent.left = p.right       # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
#             else:
#                 parent.right = p.right      # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
#         elif p.right is None:               # p에 오른쪽 자식이 없으면
#             if p is self.root:
#                 self.root = p.left
#             elif is_left_child:
#                 parent.left = p.left        # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
#             else:
#                 parent.right = p.left       # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
#         else:
#             parent = p
#             left = p.left                   # 서브 트리 안에서 가장 큰 노드
#             is_left_child = True
#             while left.right is not None:   # 가장 큰 노드 left를 검색
#                 parent = left
#                 left = left.right
#                 is_left_child = False
#             p.key = left.key                # left의 키를 p로 이동
#             p.value = left.value            # left의 데이터를 p로 이동
#             if is_left_child:
#                 parent.left = left.left     # left를 삭제
#             else:
#                 parent.right = left.left    # left를 삭제
#         return True

# Do it! 실습 9-1[E]
#     def dump(self) -> None:
#         """덤프(모든 노드를 키의 오름차순으로 출력)"""
#         def print_subtree(node: Node):
#             """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
#             if node is not None:
#                 print_subtree(node.left)            # 왼쪽 서브 트리를 오름차순으로 출력
#                 print(f'{node.key}  {node.value}')  # node를 출력
#                 print_subtree(node.right)           # 오른쪽 서브 트리를 오름차순으로 출력
#         print_subtree(self.root)

# Do it! 실습 9-1[F]
#     def min_key(self) -> Any:
#         """가장 작은 키"""
#         if self.root is None:
#             return None
#         p = self.root
#         while p.left is not None:
#             p = p.left
#         return p.key
#     def max_key(self) -> Any:
#         """가장 큰 키"""
#         if self.root is None:
#             return None
#         p = self.root
#         while p.right is not None:
#             p = p.right
#         return p.key

# [Do it! 실습 9-2] 이진 검색 트리 클래스 BinarySearchTree 사용하기
# from enum import Enum
# from bst import BinarySearchTree
# Menu = Enum('Menu', ['삽입', '삭제', '검색', '덤프', '키의범위', '종료'])
# def select_Menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '  ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
# tree = BinarySearchTree()  # 이진 검색 트리를 생성
# while True:
#     menu = select_Menu()  # 메뉴 선택
#     if menu == Menu.삽입:  # 삽입
#         key = int(input('삽입할 키를 입력하세요.: '))
#         val = input('삽입할 값을 입력하세요.: ')
#         if not tree.add(key, val):
#             print('삽입에 실패했습니다!')
#     elif menu == Menu.삭제:  # 삭제
#         key = int(input('삭제할 키를 입력하세요.: '))
#         tree.remove(key)
#     elif menu == Menu.검색:  # 검색
#         key = int(input('검색할 키를 입력하세요.: '))
#         t = tree.search(key)
#         if t is not None:
#             print(f'이 키를 갖는 값은 {t}입니다.')
#         else:
#             print('해당 데이터가 없습니다.')
#     elif menu == Menu.덤프:  # 덤프(모두 출력)
#         tree.dump()
#     elif menu == Menu.키의범위 :  # 키의 범위(최솟값과 최댓값)
#         print(f'키의 최솟값은 {tree.min_key()}입니다.')
#         print(f'키의 최댓값은 {tree.max_key()}입니다.')
#     else:  # 종료
#         break

# [Do it! 실습 9C-1] 이진 검색 트리의 구현(키를 내림차순으로 덤프)
# from __future__ import annotations
# from typing import Any, Type
# class Node:
#     """이진검색트리의 노드"""
#     def __init__(self, key: Any, value: Any, left: Node = None,
#                  right: Node = None):
#         """생성자"""
#         self.key = key          # 키
#         self.value = value      # 값
#         self.left = left        # 왼쪽 포인터(왼쪽 자식에 대한 참조)
#         self.right = right      # 오른쪽 포인터(오른쪽 자식에 대한 참조)
# class BinarySearchTree:
#     """이진검색트리"""
#     def __init__(self):
#         """초기화"""
#         self.root = None        # 루트
#     def search(self, key: Any) -> Any:
#         """키 key를 갖는 노드를 검색"""
#         p = self.root # 루트에 주목
#         while True:
#             if p is None:                       # 더 이상 진행할 수 없으면
#                 return None                     # ... 검색 실패
#             if key == p.key:                    # key와 노드 p의 키가 같으면
#                 return p.value                  # ... 검색 성공
#             elif key < p.key:                   # key 쪽이 작으면
#                 p = p.left                      # ... 왼쪽 서브 트리에서 검색
#             else:                               # key 쪽이 크면
#                 p = p.right                     # ... 오른쪽 서브 트리에서 검색
#     def add(self, key: Any, value: Any) -> bool:
#         """키가 key이고, 값이 value인 노드를 삽입"""
#         def add_node(node: Node, key: Any, value: Any) -> None:
#             """node를 루트로 하는 서브 트리에 키가 key이고, 값이 value인 노드를 삽입"""
#             if key == node.key:
#                 return False # key가 이진검색트리에 이미 존재
#             elif key < node.key:
#                 if node.left is None:
#                     node.left = Node(key, value, None, None)
#                 else:
#                     add_node(node.left, key, value)
#             else:
#                 if node.right is None:
#                     node.right = Node(key, value, None, None)
#                 else:
#                     add_node(node.right, key, value)
#             return True
#         if self.root is None:
#             self.root = Node(key, value, None, None)
#             return True
#         else:
#             return add_node(self.root, key, value)
#     def remove(self, key: Any) -> bool:
#         """키가 key인 노드를 삭제"""
#         p = self.root           # 스캔 중인 노드
#         parent = None           # 스캔 중인 노드의 부모 노드
#         is_left_child = True    # p는 parent의 왼쪽 자식 노드입니까?
#         while True:
#             if p is None:                       # 더 이상 진행할 수 없으면
#                 return False                    # ... 그 키는 존재하지 않음
#             if key == p.key:                    # key와 노드 p의 키가 같으면
#                 break                           # ... 검색 성공
#             else:
#                 parent = p                      # 가지를 내려가기 전에 부모를 설정
#                 if key < p.key:                 # key 쪽이 작으면
#                     is_left_child = True        # ... 여기서 내려가는 것은 왼쪽 자식
#                     p = p.left                  #... 왼쪽 서브 트리에서 검색
#                 else:                           # key 쪽이 크면
#                     is_left_child = False       # ... 여기서 내려가는 것은 오른쪽 자식
#                     p = p.right                 # ... 오른쪽 서브 트리에서 검색
#         if p.left is None:                      # p에 왼쪽 자식이 없으면 ...
#             if p is self.root:
#                 self.root = p.right
#             elif is_left_child:
#                 parent.left = p.right           # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킵니다.
#             else:
#                 parent.right = p.right          # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킵니다.
#         elif p.right is None:                   # p에 오른쪽 자식이 없으면 ...
#             if p is self.root:
#                 self.root = p.left
#             elif is_left_child:
#                 parent.left = p.left            # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킵니다.
#             else:
#                 parent.right = p.left           # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킵니다.
#         else:
#             parent = p
#             left = p.left                       # 서브 트리 안에서 가장 큰 노드
#             is_left_child = True
#             while left.right is not None:       # 가장 큰 노드 left를 검색
#                 parent = left
#                 left = left.right
#                 is_left_child = False
#             p.key = left.key                    # left의 키를 p로 이동
#             p.value = left.value                # left의 데이터를 p로 이동
#             if is_left_child:
#                 parent.left = left.left         # left를 삭제
#             else:
#                 parent.right = left.left        # left를 삭제
#         return True
#     def dump(self, reverse = False) -> None:
#         """덤프(모든 노드를 키의 오름차순/내림차순으로 출력)"""
#         def print_subtree(node: Node):
#             """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
#             if node is not None:
#                 print_subtree(node.left)                # 왼쪽 서브 트리를 오름차순으로 출력
#                 print(f'{node.key}  {node.value}')      # node를 출력
#                 print_subtree(node.right)               # 오른쪽 서브 트리를 오름차순으로 출력
#         def print_subtree_rev(node: Node):
#             """node를 루트로 하는 서브 트리의 노드를 키의 내림차순으로 출력"""
#             if node is not None:
#                 print_subtree_rev(node.right)           # 오른쪽 서브 트리를 내림차순으로 출력
#                 print(f'{node.key}  {node.value}')      # node를 출력
#                 print_subtree_rev(node.left)            # 왼쪽 서브 트리를 내림차순으로 출력
#         print_subtree_rev(self.root) if reverse else print_subtree(self.root)
#     def min_key(self) -> Any:
#         """가장 작은 키"""
#         if self.root is None:
#             return None
#         p = self.root
#         while p.left is not None:
#             p = p.left
#         return p.key
#     def max_key(self) -> Any:
#         """가장 큰 키"""
#         if self.root is None:
#             return None
#         p = self.root
#         while p.right is not None:
#             p = p.right
#         return p.key

# [Do it! 실습 9C-1] 이진 검색 트리 클래스 BinarySearchTree 사용하기(오름차순, 내림차순으로 덤프)
# from enum import Enum
# from bst2 import BinarySearchTree
# Menu = Enum('Menu', ['삽입', '삭제', '검색', '오름차순덤프', '내림차순덤프', '키의범위', '종료'])
# def select_Menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep = '  ', end='')
#         n = int(input(' : '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
# tree = BinarySearchTree()  # 이진 검색 트리를 생성
# while True:
#     menu = select_Menu()  # 메뉴 선택
#     if menu == Menu.삽입:  # 삽입
#         key = int(input('삽입할 키를 입력하세요.: '))
#         val = input('삽입할 값을 입력하세요.: ')
#         if not tree.add(key, val):
#             print('삽입에 실패했습니다!')
#     elif menu == Menu.삭제:  # 삭제
#         key = int(input('삭제할 키를 입력하세요.: '))
#         tree.remove(key)
#     elif menu == Menu.검색:  # 검색
#         key = int(input('검색할 키를 입력하세요.: '))
#         t = tree.search(key)
#         if t is not None:
#             print(f'이 키를 갖는 값은 {t}입니다.')
#         else:
#             print('해당 데이터가 없습니다.')
#     elif menu == Menu.오름차순덤프:  # 오름차순 덤프
#         tree.dump()
#     elif menu == Menu.내림차순덤프:  # 내림차순 덤프
#         tree.dump(reverse = True)
#     elif menu == Menu.키의범위 :  # 키의 범위(최솟값과 최댓값)
#         print(f'키의 최솟값은 {tree.min_key()}입니다.')
#         print(f'키의 최댓값은 {tree.max_key()}입니다.')      
#     else:# 종료
#         break