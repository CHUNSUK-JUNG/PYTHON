# switch = {
#     '+': lambda x, y: x + y,    # 람다 표현식으로 실행할 코드를 작성
#     '*': lambda x, y: x * y
#     }
# x = '%'
# try:
#     print(switch[x](10, 20))    # 딕셔너리에 키를 지정하는 방식
# except KeyError:
#     print('default')

# class Person:
#     pass
# person = Person()
# a = 0
# print(isinstance(a, Person))

# class Person():
#     ''' 사람 클래스 '''
#     def __init__(self) -> None:
#         pass
#     def add(self, a, b):
#         ''' 더하는 함수 '''
#         pass
# a = 10
# print(globals())
# print(__name__)
# print(__file__)
# print(Person.__doc__)
# print(Person.add.__doc__)

# class A:
#     def greeting(self):
#         print('안녕하세요. A입니다.')
# class B(A):
#     def greeting(self):
#         print('안녕하세요. B입니다.')
# class C(A):
#     def greeting(self):
#         print('안녕하세요. C입니다.')
# class D(B, C):
#     pass
# x = D()
# print(D.__mro__)
# x.greeting()    # 안녕하세요. B입니다.

# from abc import *
# class Student(metaclass=ABCMeta):
#     @abstractmethod
#     def go_school(self):
#         pass
# class MiddleSchool(Student):
#     def go_school(self):
#         print('중학생입니다.')
# james = MiddleSchool()
# james.go_school()

# import math
# class Point2D:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
# p1 = Point2D(2, 3)
# p2 = Point2D(1, 5)
# d = math.sqrt(pow(p1.x-p2.x, 2)+pow(p1.y-p2.y, 2))
# print('p1과 p2 두 점 사이의 거리는 %10.8f 입니다.' %d)

# import math, collections
# Point2D = collections.namedtuple('Point2D', ['x', 'y'])
# p1 = Point2D(2, 3)
# p2 = Point2D(1, 5)
# d = math.sqrt(pow(p1.x-p2.x, 2)+pow(p1.y- p2.y, 2))
# print(d)

# y = [10, 20, 30]
# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)
# except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
#     print('숫자를 0으로 나눌 수 없습니다.')
# except IndexError:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
#     print('잘못된 인덱스입니다.')

# y = [10, 20, 30]
# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)
# except ZeroDivisionError as e:                    # as 뒤에 변수를 지정하면 에러를 받아옴
#     print('숫자를 0으로 나눌 수 없습니다.', e)    # e에 저장된 에러 메시지 출력
# except IndexError as c:
#     print('잘못된 인덱스입니다.', c)

# print(dir([1, 2, 3]))
# a = [1, 2, 3].__iter__()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# class Counter:
#     def __init__(self, stop):
#         self.stop = stop
 
#     def __getitem__(self, index):
#         if index < self.stop:
#             return index
#         else:
#             raise IndexError
# for i in Counter(3):
#     print(i, end=' ')

# def number_coroutine():
#     while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
#         x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
#         print(x)
# co = number_coroutine()
# next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)
# co.send(1)    # 코루틴에 숫자 1을 보냄
# co.send(2)    # 코루틴에 숫자 2을 보냄
# co.send(3)    # 코루틴에 숫자 3을 보냄

# def sum_coroutine():
#     total = 0
#     while True:
#         x = (yield total)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
#         total += x
# co = sum_coroutine()
# print(next(co))      # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력
# print(co.send(1))    # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
# print(co.send(2))    # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
# print(co.send(3))    # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력

# def number_coroutine():
#     while True:
#         x = (yield)
#         print(x, end=' ')
# co = number_coroutine()
# next(co)
# for i in range(20):
#     co.send(i)
# co.close()    # 코루틴 종료

# def number_coroutine():
#     try:
#         while True:
#             x = (yield)
#             print(x, end=' ')
#     except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
#         print()
#         print('코루틴 종료')
# co = number_coroutine()
# next(co)
# for i in range(20):
#     co.send(i)
# co.close()

# def sum_coroutine():
#     try:
#         total = 0
#         while True:
#             x = (yield)
#             total += x
#     except RuntimeError as e:
#         print(e)
#         yield total    # 코루틴 바깥으로 값 전달
# co = sum_coroutine()
# next(co)
# for i in range(20):
#     co.send(i)
# print(co.throw(RuntimeError, '예외로 코루틴 끝내기')) # 190

# def decorator1(func):
#     def wrapper():
#         print('decorator1')
#         func()
#     return wrapper
# def decorator2(func):
#     def wrapper():
#         print('decorator2')
#         func()
#     return wrapper
# # 데코레이터를 여러 개 지정
# @decorator1
# @decorator2
# def hello():
#     print('hello')
# hello()

# def trace(func):          # 호출할 함수를 매개변수로 받음
#     def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
#         r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
#         print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
#         return r          # func의 반환값을 반환
#     return wrapper        # wrapper 함수 반환
# @trace              # @데코레이터
# def add(a, b):      # 매개변수는 두 개
#     return a + b    # 매개변수 두 개를 더해서 반환
# print(add(10, 20))