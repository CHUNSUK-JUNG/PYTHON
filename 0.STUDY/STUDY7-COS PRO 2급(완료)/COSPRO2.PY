# [2진수, 8진수, 16진수의 출력]
# print(0b10)
# print(0o10)
# print(0xF)

# [복소수 만들기]
# print(complex(1.2, 1.3))

# [비어있는 변수 만들기]
# x=None
# print(x)

# [여러개의 변수 만들기]
# x, y, z = 10, 20, 30
# print(x, y, z)
# x = y = z = 10
# print(x, y, z)

# [변수에 변수 할당하기]
# x, y = 10, 20
# print(x, y)
# x, y = y, x
# print(x, y)

# [변수의 삭제]
# x, y = 10, 20
# print(x, y)
# del x
# print(y)

# [변수에 값이 저장되는 방식]
# import sys
# print(sys.getrefcount(1000)) # 처음 레퍼런스 카운트는 2
# x = 1000
# print(sys.getrefcount(1000))
# y = 1000
# print(sys.getrefcount(1000))
# print(id(x), id(y))
# print( x is y)

# [문자열 저장]
# x = ''' 여러줄
#     문자열
#     저장 '''
# print(x)
# y = '안녕하세요.'
# print(len(y), len(y.encode('utf-8')))

# [문자열 연산]
# x = 'hello'
# y = 'world'
# z = 10
# print(x+y)
# print(x*3)
# print(x+str(z))

# [입력]
# a = input('첫번째 문자열을 입력하세요. : ')
# b = input('두번째 문자열을 입력하세요. : ')
# print(a+b)
# c = int(input('첫번째 정수를 입력하세요. : '))
# d = int(input('두번째 정수를 입력하세요. : '))
# print(a+b)

# [동시에 여러개의 입력]
# a, b, c = map(int, input('정수 3개를 입력하세요. : ').split())
# print(a+b+c)
# d, e, f = input('문자 또는 문자열 3개를 입력하세요. : ').split()
# print(d+e+f)

# [몫과 나머지 구하기 및 부호]
# x, y = divmod(5, 2)
# print(x, y)
# z = -10
# print(+z, -z)

# [객체 참조]
# x = 10
# y = 10
# print(x == y, x != y, x is y)
# print(id(x), id(y))

# [조건부 표현식]
# x = 5
# y = 10 if x == 5 else 0
# print(y)

# [if 문의 실행]
# if None : # None은 거짓을 의미한다.
#     print('참')
# else:
#     print('거짓')
# if 0x1 :
#     print('참')
# else:
#     print('거짓')
# if '' :
#     print('참')
# else:
#     print('거짓')
# if not None :
#     print('참')
# else:
#     print('거짓')

# [조건식 여러개 지정]
# x = 10
# if x > 0 and x < 20:
#     print('0과 20 사이의 숫자입니다.')
# else:
#     print('0과 20 사이의 숫자가 아닙니다.')
# x = -1
# if 0 < x < 20:
#         print('0과 20 사이의 숫자입니다.')
# else:
#     print('0과 20 사이의 숫자가 아닙니다.')

# [for와 range]
# for i in range(10):
#     print(i, end='')
# print()
# for i in reversed(range(10)):
#     print(i, end='')
# print()
# x = range(10)
# print(x, type(x))
# n = 5
# factoral = 1
# for i in range(1, n+1):
#     factoral *=i
# print(factoral)

# [while]
# import random
# a = []
# b = 0
# i = 0
# while i < 6 :
#     b = random.randint(0, 45)
#     a.append(b)
#     i += 1
# print(a)
# cnt = 1
# while cnt < 11 :
#     print('hellow %d ' %cnt, end='')
#     cnt += 1

# [FizzBuzz]
# for i in range(1, 101):
#     if i % 3 == 0 :
#         print('%d Pizz' %i, end=' ')
#     if i % 5 == 0 :
#         print('%d Buzz' %i, end=' ')
#     if i % 3 == 0 and i % 5 == 0 :
#         print('%d FizzBuzz' %i, end=' ')

# [리스트]
# a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(a[1:1])
# print(a[:])
# print(a[:7])
# print(a[7:])
# print(a[7:-1])

# [튜플]
# a = tuple([1,2,3])
# print(a)
# b = tuple(range(10))
# print(b)
# c = list((1,2,3))
# print(c)
# d = list(tuple(range(5)))
# print(d)

# [리스트 조작하기]
# a = []
# a.append(10)
# a.append(20)
# a.append(30)
# a.append([40,50])
# print(a)
# a.clear()
# print(a)
# a.extend([10])
# a.extend([20, 30])
# print(a)

# [리스트의 할당과 복사]
# a = list(range(10))
# b = a
# print(a, b, a is b, id(a), id(b))
# b = a.copy()
# print(a, b, a is b, id(a), id(b))

# [리스트의 인덱스와 값 출력하기]
# a = [10, 20, 30]
# b = ()
# c = {}
# for b in enumerate(a):
#     print(b)
# for key, value in enumerate(a):
#     c[key] = value
# print(c)

# [리스트 표현식]
# a = [i for i in range(10)]
# print(a)
# b = [i for i in range(10)
#             if i % 2 == 0]
# print(b)
# c = [i*j for i in range(2, 10)
#             for j in range(1, 10)]
# print(c)

# [map 함수]
# a = list(range(10))
# print(a)
# a = list(map(str, a))
# print(a)
# a = list(map(float, a))
# print(a)
# a = input('문자 2개를 입력하세요. : ').split()
# print(a)
# b = list(map(int, input('정수 2개를 입력하세요. : ').split()))
# print(b)

# [2차원 리스트]
# a = [[10, 20], [30, 40], [50, 60]]
# for i, j in a:
#     print(i, j)
# b = []
# b = [[0 for i in range(2)] for j in range(3)]
# print(b)
# c = [[0]*2 for i in range(3)]
# print(c)

# [함수 doc 스트링]
# def add(a, b):
#     ''' a와 b를 더하는
#     함수 '''
#     return a+b
# a = add(10, 20)
# print(a)
# print(add.__doc__)
# help(add)

# [시프트 연산자]
# a = 0b1100
# b = 0b0011
# c = a & b
# d = a | b
# print(bin(c), bin(d))