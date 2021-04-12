# 출처 [http://pythonstudy.xyz/ 예제로 배우는 파이썬 프로그래밍]


# [PYTHON 기초]
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

# [Iterator]
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

# [Python Comprehension}
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

# [문자열]
# 문자열
# 파이썬에서 문자열은 단일인용부호(') 혹은 이중인용부호(") 를 사용하여 표현한다.
# 만약 여러 라인에 걸쳐 있는 문자열을 표현하고 싶다면, ''' '''또는 """ """처럼 3개의 인용부호를 사용한다.
# 복수 라인 문자열을 한 라인으로 표현하고 싶다면, Escape Sequence (\n)를 사용하면 된다. 즉, 다음 표현은 위와 동일한 표현이다.
# 물론 문자열에서 사용되는 Escape Sequence에는 타 언어와 비슷하게 여러 가지를 사용할 수 있다. 예를 들어 탭은 \t, 이중따옴표는 \", 백슬래쉬는 \\ 등과 같이 표현한다.
# 문자열 포맷팅
# 일정한 포맷에 맞춰 문자열을 조합하는 것을 문자열 포맷팅이라하는데, 문자열 포맷 템플릿 안에 대입값이 들어갈 자리를 지정해 두고 나중에 그 값을 채워 넣는 방식이다. 
# 예를 들어, "답: %s" % "A" 와 같은 표현에서 % 앞 부분은 포맷 템플릿이고, % 뒤는 실제 대입할 값이다. 이때 % 를 포맷팅 연산자 (Formatting Operator)라 부른다.
# % 앞뒤로 각각 하나의 값만을 받아들이므로 만약 % 뒤의 값이 복수 개이면 튜플로 묶어주어야 한다.
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
# Conversion Specifier는 % 와 Conversion 문자(예: s, d, f) 사이에 전체 자릿수와 소숫점 뒤자리수를 지정할 수 있다. 예를 들어 %10.2f 는 
# 전체 10자리이고 값이 적으면 앞에 빈칸을 채우게 되고, .2 는 소수점 2째 자리까지만 표시한다는 것을 의미한다. 만약 %-10.2f 처럼 
# 마이너스로 표현하면 전체 10자리인데 왼쪽으로 정렬한다는 의미이다.
# str (문자열 클래스)
# 문자열은 내부적으로 str 이라는 클래스 타입인데, 파이썬의 문자열은 기본적으로 유니코드이고, 한번 설정되면 다시 변경시킬 수 없는 Immutable 타입이다.
# 문자열은 인덱스를 사용하여 문자열 중 특정위치의 문자를 표현할 수 있다. 인덱스는 0로부터 시작하는데, 
# 문자열 s 에 대하여 첫번째 문자는 s[0], 두번째 문자는 s[1] 과 같이 표현된다.
# 파이썬에는 C 등에서 존재하는 문자(char) 타입이 존재하지 않는다. 따라서, 위의 예에서 s[1]의 타입이 char가 아닌 문자열 str 타입이 된다.
# 참고로 type(변수명)은 해당 변수의 타입을 리턴한다.
# 문자열을 표현할 때, r'문자열' 과 같이 사용하면, 이는 Escape Sequence를 표현하지 않고 Raw String을 직접 사용한다는 것을 의미한다. 
# 예를 들어, 윈도우즈에서 파일경로를 간략히 표현하기 위해 아래와 같이 Raw String 표현을 사용할 수 있다.\
# 자주 사용되는 str 메서드
# 문자열 str 클래스에는 여러 유용한 메서드들이 제공되고 있는데, 이 중 흔히 사용되는 몇가지만 소개한다.
# str.join()
# 우선 여러 개의 문자열을 하나로 결합하는 join() 메서드가 있는데, join() 메서드는 문자열을 결합하는데 사용되는 Separator를 join 메서드 
# 앞에 사용한다. 아래 예제에 보듯이, 콤마를 사용하여 문자열 리스트 요소들을 결합할 수도 있으며, 또한 빈 문자열을 사용하여 문자열들을
# 결합하는 방법도 자주 사용된다.
# str.split()
# split() 메서드는 join() 메서드의 반대로서 특정 separator를 기준으로 문자열을 분리하여 리스트를 리턴한다.
# 아래 예제에서 split() 메서드는 하나의 문자열을 콤마로 분리해서 3개의 요소를 갖는 리스트를 리턴한다.
# str.partition()
# partition() 메서드는 문자열을 partition() 메서드의 첫번째 파라미터로 분리하여 그 앞부분(prefix), partition 분리자(separator),
# 뒷부분 (suffix) 등 3개의 값을 Tuple로 리턴한다. 
# 아래 예제는 Dash (-) 로 문자열을 분리하여 3개의 값을 리턴하는 코드이다. 일반적으로 separator는 사용하지 않아서 _ 를 사용하였다.
# str.format()
# 마지막으로 str 클래스에서 가장 많이 사용되는 메서드 중의 하나로 format() 메소드를 들 수 있다. format() 메서드는 다양한 방식의 문자열 포맷팅을 지원하는데, 
# 아래는 흔히 사용되는 3가지 방식을 예시하고 있다. 먼저 위치를 기준으로한 포맷팅은 {0},{1},... 등의 필드들을 format() 파라미터들의 순서대로 치환하게 된다. 
# 두번째 필드명을 기준으로 한 포맷팅은 {name}, {age}와 같이 임의의 필드명을 지정하고 format() 파라미터에 이들 필드명을 사용하여 값을 지정하는 것이다. 
# 그리고 세번째 인덱스 및 키 사용 방식은 Python 오브젝트가 format()의 파라미터로 지정되고, 포맷에서 이 오브젝트의 인덱스(컬렉션의 경우) 혹은 속성, 키 등을 이용하는 것이다.
# bytes (바이트 클래스)
# bytes 클래스는 일련의 바이트들을 표현하는 클래스로서 bytes는 한번 설정되면 다시 변경할 수 없는 Immutable 타입이다. bytes 클래스와 비슷한 클래스로 bytearray 클래스가 있는데,
# 차이점은 bytearray는 바이트 객체의 요소를 변경할 수 있는 Mutable 타입이라는 점이다.
# 문자들을 바이트들로 표현하기 위해 b'문자들'과 같이 접두어 b를 앞에 붙인다. 이렇게 접두어 b를 붙여 바이트 리터럴을 만들때, 각 문자는 ASCII 코드를 갖는 문자로 처리된다.
# str 타입의 문자열을 bytes 타입의 바이트들로 변경하기 위해 str 클래스의 인코딩 메서드 encode()를 사용한다. 반대로 bytes 타입의 바이트 객체을 str 타입의 문자열로 변경하기 
# 위해 bytes 클래스의 디코딩 메서드 decode()를 사용한다. encode(), decode() 를 사용하여 문자열과 바이트들 간의 인코딩/디코딩을 할 때, 특별히 파라미터를 지정하지 않으면 디폴트 인코딩을 사용하지만, 
# 필요시 어떤 인코딩 방식을 사용할 지를 지정할 수 있다. 예를 들어, encode("UTF-8")과 같이 UTF8 인코딩 방식을 사용하도록 지정할 수 있다.
# 문자열 안에서 유니코드값을 사용하려면, \u 에 이어 유니코드값을 적으면 된다. 아래 예제는 문자열 s1을 UTF-8 인코딩을 사용하여 바이트들로 변경하고,
# 이를 다시 문자열로 디코딩하는 예제이다.
''' p = "이름: %s 나이: %d" % ("김유신", 65)
print(p)
# 출력: 이름: 김유신 나이: 65
p = "X = %0.3f, Y = %10.2f" % (3.141592, 3.141592)
print(p)
# 출력: X = 3.142, Y =       3.14
path = r'C:\Temp\test.csv'
print(path)
s = ','.join(['가나','다라','마바'])
print(s)
# 출력: 가나,다라,마바
s = ''.join(['가나','다라','마바'])
print(s)
# 출력 : 가나다라마바
items = '가나,다라,마바'.split(',')
print(items)
# 출력 : ['가나', '다라', '마바']
departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)
# 출력 : Seattle
# 위치를 기준으로 한 포맷팅
s = "Name: {0}, Age: {1}".format("강정수", 30)
print(s)  #출력: Name: 강정수, Age: 30
# 필드명을 기준으로 한 포맷팅
s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
print(s) #출력: Name: 강정수, Age: 30
# object의 인덱스 혹은 키를 사용하여 포맷팅
area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s) #출력: width: 10, height: 20
s = "Hello"
b = s.encode()
print(b)    # b'Hello'
s2 = b.decode()  
print(s2)   # 'Hello'
# 특정 인코딩 방식을 지정한 경우
x = "안녕".encode("UTF-8")
y= x.decode("UTF-8") '''

# [연산자}
# 파이썬은 산술연산자, 비교연산자, 할당연산자, 논리연산자, Bitwise 연산자, 멤버쉽연산자, Identity연산자를 지원한다.
# 1.산술연산자에는 (1) 사칙연산자 +, -, *, / 와 (2) 제곱을 나타내는 **, (3) 나머지를 산출하는 % (Modulus),
#   그리고 (4) 나누기에 소숫점 이하를 버리는 // 연산자(Floor Division) 등이 있다.
# 2.비교연산자는 관계연산자로도 불리우는데, 여기에는 등호(==), 같지 않음(!=), 부등호(<, >, <=, >=) 등이 있다.
# 3.할당연산자는 변수에 값을 할당하기 위하여 사용되는데, 기본적으로 = (Equal Sign)을 사용한다. 산술연산자와 함께 사용되어
#   할당을 보다 간결히 하기 위해 사용되는 +=, -=, *=, /=, %=, //= 등과 같은 연산자도 할당연산자에 해당된다.
# 4.논리연산자에는 and, or, not 이 있는데, and 는 양쪽의 값이 모두 참인 경우만 참이 되고, or 는 어느 한쪽만 참이면 참이된다. 
#   not 은 참이면 거짓으로 거짓이면 참이 된다. 아래 예제는 No가 출력된다.
# 5.Bitwise연산자에는 & (AND), | (OR), ^ (XOR), ~ (Complement), <<, >> (Shift)가 있는데, 이 연산자는 비트단위의 연산을 하는데 사용된다.
# 6.멤버쉽연산자에는 in, not in 이 있는데, 이는 좌측 Operand가 우측 컬렉션에 속해 있는지 아닌지를 체크한다.
# 7.Identity연산자에는 is, is not 이 있는데, 이는 양쪽 Operand가 동일한 Object를 가리키는지 아닌지를 체크한다.
''' a = 2
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

# [기본 데이타 타입]
# 파이썬에 사용되는 기본 데이타 타입(Scalar Data Type)에는 아래와 같은 타입들이 있다.
# 타입	설명	                 표현 예
# int	    정수형 데이타	100, 0xFF (16진수), 0o56 (8진수)
# float	소숫점을 포함한 실수	a = 10.25
# bool	참, 거짓을 표현하는 부울린	a = True
# None	Null과 같은 표현	a = None
# 리터럴 데이타를 특정 타입으로 변경하기 위하여 int(), float(), bool() 등과 같은 타입 생성자를 사용할 수 있다.
# 예를 들어, int(3.5)는 float 데이타를 정수형으로 변경하여 정수값 3 을 리턴한다. float("1.6")은 float형 1.6을 리턴한다.
# 파이썬은 복소수 타입을 지원하는데, 복소수는 a+bj 와 같이 표현된다 (수학에서 복소수를 표현할 때 i 를 사용하지만 파이썬에서는 j 를 사용한다). 
# 실수부의 값을 얻기 위해서는 복소수 변수명.real을, 허수부의 값을 얻기 위해선 변수명.imag 를 사용한다.
''' print(int(3.5))      # 3
print(2e3)           # 2000.0
print(float("1.6"))  # 1.6
print(float("inf"))  # 무한대
print(float("-inf")) # -무한대
print(bool(0))       # False. 숫자에서 0만 False임,
print(bool(-1))      # True
print(bool("False")) # True
a = None             # a는 None
print(a is None)     # a가 None 이므로 True
v = 2 + 3j
print(v.real)  # 2
print(v.imag)  # 3 '''

# [PEP]
# PEP 이란 Python Enhancement Proposals 의 약자로서 파이썬을 개선하기 위한 제안서를 의미한다.
# 이러한 PEP은 다음과 같이 크게 3 종류로 구분할 수 있으며, Python Software Foundation의 공식 웹사이트인 python.org 에서 관리한다.
# 1.파이썬에 새로운 기능(Feature)을 추가하거나 구현 방식을 제안하는 Standard Track PEP
# 2.파이썬 디자인 이슈를 설명하거나 일반적인 가이드라인 혹은 정보를 커뮤니티에 제공하는 Informational PEP
# 3.파이썬을 둘러싼 프로세스를 설명하거나 프로세스 개선을 제안하는 Process PEP. 예를 들어, 프로세스 절차, 가이드라인, 의사결정 방식의 개선, 파이썬 개발 도구 및 환경의 변경 등등.
# PEP은 파이썬 언어 자체 뿐만 아니라 코딩 표준, 커뮤니티 이슈 등을 담고 있는 유용한 자료이므로 파이썬을 배우면서 자주 참고하면 좋다. PEP은 각 문서마다 번호가 지정되어 있는데, 
# PEP 번호별 내용은 https://www.python.org/dev/peps/ 에서 찾아 볼 수 있다.
# 특히, 파인썬 코딩과 관련한 코딩 표준(Coding Convention)에 관한 문서는 PEP 8 (https://www.python.org/dev/peps/pep-0008) 에 정의되어 있는데, 파이썬의 기초를 익힌 후 참조하면 파이썬 코딩 스타일을 익히는데 도움이 된다.

# [PEP 8 파이썬 코딩 스타일]
# Python Enhancement Proposal 8 (PEP 8)은 파이썬 코딩 스타일에 대한 가이드를 제시하고 있다. 
# PEP 8은 2001년 귀도 반 로썸에 의해 처음 제안되었으며, python.org 의 PEP 링크에 자세히 소개되어 있다.
# 파이썬 프로그래머들은 일반적으로 이러한 PEP 8 코딩 스타일에 따라 프로그래밍을 하고 있는데, 이러한 일관된 
# 코딩 스타일을 적용하는 것은 자신의 코드를 명료하게 할 뿐만 아니라 특히 다른 개발자 혹은 커뮤니티간 코딩을 공유할 때 매우 효율적이다.

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
#     모듈 import시 절대 경로를 사용할 것을 권장한다. 예를 들어, sibling 모듈이 현재 모듈과 같은 폴더에 있더라도 패키지명부터 절대 경로를 사용함.
#     단, 복잡한 패키지 경로를 갖는 경우 상대경로(.)를 사용할 수 있다.

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