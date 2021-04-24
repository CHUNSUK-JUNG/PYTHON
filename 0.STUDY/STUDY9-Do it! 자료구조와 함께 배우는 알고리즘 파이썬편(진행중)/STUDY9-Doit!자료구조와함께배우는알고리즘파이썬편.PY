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

# [Do it! 실습 2C-6] 리스트의 모든 원솟값을 업데이트하기
def change(lst, idx, val):
    """lst[idx]의 값을 val로 업데이트"""
    lst [idx] = val
x = [11, 22, 33, 44, 55]
print('x =', x)
index = int(input('업데이트할 인덱스를 선택하세요.: '))
value = int(input('새로운 값을 입력하세요.: '))
change(x, index, value)
print(f'x = {x}')

# [Do it! 실습 2C-7] 자료형을 정하지 않은 리스트 원소 확인하기
# x = [15, 64, 7, 3.14, [32, 55], 'ABC']
# for i in range(len(x)):
#     print(f'x[{i}] = {x[i]}')

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