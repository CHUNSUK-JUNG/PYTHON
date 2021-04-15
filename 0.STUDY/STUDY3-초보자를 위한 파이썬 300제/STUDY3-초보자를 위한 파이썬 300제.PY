# 출처 [https://wikidocs.net/book/922, 초보자를 위한 파이썬 300제]


''' # [291-300]
# 291 파일 쓰기
# 바탕화면에 '매수종목1.txt' 파일을 생성한 후 다음과 같이 종목코드를 파일에 써보세요.
# 005930
# 005380
# 035420
f = open("매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()

# 292 파일 쓰기
# 바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER
f = open("매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()

# 293 CSV 파일 쓰기
# 바탕화면에 '매수종목.csv' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요. 
# 인코딩은 'cp949'를 사용해야합니다.
import csv
f = open("매수종목.csv", mode="wt", encoding="cp949", newline='')
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()

# 294 파일 읽기
# 바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.
# 005930
# 005380
# 035420
f = open("매수종목1.txt", encoding="utf-8")
lines = f.readlines()   # python list
codes = []
for line in lines:
    code = line.strip()  #'\n'
    codes.append(code)
print(codes)
f.close()

# 295 파일 읽기
# 바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. 종목명을 key로 종목명을 value로 저장합니다.
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER
f = open("매수종목2.txt", encoding="utf-8")
lines = f.readlines()
data = {}
for line in lines:
    line = line.strip()     # '\n' 제거
    k, v = line.split()
    #print(k, v)
    data[k] = v
print(data)
f.close()

# 296 예외처리
# 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. 예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.
# per = ["10.31", "", "8.00"]
# for i in per:
#     print(float(i))
per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))
    except:
        print(0)

# 297 예외처리 및 리스트에 저장
# 문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.
# per = ["10.31", "", "8.00"]
# for i in per:
#     print(float(per))
per = ["10.31", "", "8.00"]
new_per = []
for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)
print(new_per)

# 298 특정 예외만 처리하기
# 어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다. try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.
try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")

# 299 예외의 메시지 출력하기
# 다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.
# try:
#     실행코드
# except 예외 as 변수:
#     예외처리코드 
# 리스트의 인덱싱에 대해 에러를 출력해보세요.
# data = [1, 2, 3]
# for i in range(5)
#     print(data[i])
data = [1, 2, 3]
for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

# 300 try, except, else, finally 구조 사용해보기
# 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.
# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드
# 아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally에 적당한 코드를 작성해봅시다. else와 finally는 적당한 문구를 print하시면 됩니다.
# per = ["10.31", "", "8.00"]
# for i in per:
#     print(float(per))
per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료") '''



''' # [281-290]
# 281 클래스 정의
# 다음 코드가 동작하도록 차 클래스를 정의하세요.
# >> car = 차(2, 1000)
# >> car.바퀴
# 2
# >> car.가격
# 1000
class 차:
    def __init__ (self,바퀴,가격):
        self.바퀴=바퀴
        self.가격=가격
car=차(2,100)
print(car.바퀴)
print(car.가격)

# 282 클래스 상속
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
class 자전차(차):
    pass

# 283 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
# >> bicycle = 자전차(2, 100)
# >> bicycle.가격
# 100
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
bicycle = 자전차(2, 100)
print(bicycle.가격)

# 284 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.구동계
# 시마노
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        #차.__init__(self, 바퀴, 가격)
        self.구동계 = 구동계
bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)
print(bicycle.바퀴)

# 285 클래스 상속
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
# >> car = 자동차(4, 1000)
# >> car.정보()
# 바퀴수 4
# 가격 1000
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)
    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)
car = 자동차(4, 1000)
car.정보()

# 286 부모 클래스 생성자 호출
# 다음 코드가 동작하도록 자전차 클래스를 수정하세요.
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)
class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계
bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 287 부모 클래스 메서드 호출
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
# 구동계 시마노
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)
class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계
    def 정보(self):
        super().정보()
        print("구동계 ", self.구동계)
bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 288 메서드 오버라이딩
# 다음 코드의 실행 결과를 예상해보세요.
# class 부모:
#   def 호출(self):
#     print("부모호출")
# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
# 나 = 자식()
# 나.호출()
class 부모:
    def 호출(self):
        print("부모호출")
class 자식(부모):
    def 호출(self):
        print("자식호출")
나 = 자식()
나.호출()

# 289 생성자
# 다음 코드의 실행 결과를 예상해보세요.
# class 부모:
#   def __init__(self):
#     print("부모생성")
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
# 나 = 자식()
class 부모:
    def __init__(self):
        print("부모생성")
class 자식(부모):
    def __init__(self):
        print("자식생성")
나 = 자식()

# 290 부모클래스 생성자 호출
# 다음 코드의 실행 결과를 예상해보세요.
# class 부모:
#   def __init__(self):
#     print("부모생성")
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()
# 나 = 자식()

class 부모:
    def __init__(self):
        print("부모생성")
class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()
나 = 자식() '''



''' # [271-280]
# 271 Account 클래스
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. 
# Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다.
# 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
# 은행이름: SC은행
# 계좌번호: 111-11-111111
import random
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
kim = Account("김민수", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)

# 272 클래스 변수
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)

# 273 클래스 변수 출력
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count +=1
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)     # Account.account_count
kim = Account("김민수", 100)
lee = Account("이민수", 100)
kim.get_account_num()

# 274 입금 메서드
# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count +=1
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)     # Account.account_count
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

# 275 출금 메서드
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print(k.balance)

# 276 정보 출력 메서드
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10,000원
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
p = Account("파이썬", 10000)
p.display_info()

# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)

# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)
data.append(k)
data.append(l)
data.append(p)
print(data)

# 279 객체 순회
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)
data.append(k)
data.append(l)
data.append(p)
for c in data:
    if c.balance >= 1000000:
        c.display_info()

# 280 입출금 내역
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는
# deposit_history와 withdraw_history 메서드를 추가하세요.
import random
class Account:
    # class variable
    account_count = 0
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count
    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)
    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print('출금 내역 : ', amount)
    def deposit_history(self):
        for amount in self.deposit_log:
            print('입금 내역 : ', amount)
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()
k.withdraw(100)
k.withdraw(200)
k.withdraw_history() '''



''' # [261-270]
# 261 Stock 클래스 생성
# 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. 클래스는 속성과 메서드를 갖고 있지 않습니다.
class Stock:
    pass

# 262 생성자
# Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.
# 삼성 = Stock("삼성전자", "005930")
class Stock:
    def __init__ (self,name,code):
        self.name=name
        self.code=code
삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)

# 263 메서드
# 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
# a = Stock(None, None)
# a.set_name("삼성전자")
class Stock:
    def __init__ (self,name,code):
        self.name=name
        self.code=code
    def set_name (self,name):
        self.name=name
a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

# 264 메서드
# 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.
# a = Stock(None, None)
# a.set_code("005930")
class Stock:
    def __init__ (self,name,code):
        self.name=name
        self.code=code
    def set_code(self,code):
        self.code=code
a = Stock(None, None)
a.set_code("005930")
print(a.code)

# 265 메서드
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고
# 이를 출력해보세요.
# 삼성 = Stock("삼성전자", "005930")
class Stock:
    def __init__ (self,name,code):
        self.name=name
        self.code=code
    def set_name (self,name):
        self.name=name
    def set_code (self,code):
        self.code=code
    def get_name (self):
        return self.name
    def get_code (self):
        return self.code
삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)
print(삼성.get_name())
print(삼성.get_code())

# 266 객체의 속성값 업데이트
# 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR,
# 배당수익률은 float 타입입니다.
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code

# 267 객체 생성
# 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.
# 항목	정보
# 종목명	삼성전자
# 종목코드	005930
# PER	15.79
# PBR	1.33
# 배당수익률	2.83
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.배당수익률)

# 268 객체의 속성 수정
# PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def set_per(self, per):
        self.per = per
    def set_pbr(self, pbr):
        self.pbr = pbr
    def set_dividend(self, dividend):
        self.dividend = dividend

# 269 객체의 속성 수정
# 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def set_per(self, per):
        self.per = per
    def set_pbr(self, pbr):
        self.pbr = pbr
    def set_dividend(self, dividend):
        self.dividend = dividend
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)
print(삼성.per)

# 270 여러 종목의 객체 생성
# 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.
# 종목명	종목코드	PER	PBR	배당수익률
# 삼성전자	005930	15.79	1.33	2.83
# 현대차	005380	8.70	0.35	4.27
# LG전자	066570	317.34	0.69	1.37
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def set_per(self, per):
        self.per = per
    def set_pbr(self, pbr):
        self.pbr = pbr
    def set_dividend(self, dividend):
        self.dividend = dividend
종목 = []
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)
for i in 종목:
    print(i.code, i.per) '''



''' # [251-260]
# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.
# 클래스=도면, 객체=실물, 인스턴스=객체를 클래스의 인스턴르라 함

# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
class Human:
    pass

# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
class Human:
    pass
areum = Human()

# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
# >>> areum = Human()
# 응애응애
class Human:
    def __init__(self) :
        print('응애응애')
areum = Human()

# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
# >>> areum = Human("아름", 25, "여자")
class Human:
    def __init__(self,name,age,sex) :
        print(name,age,sex)
areum = Human("아름", 25, "여자")

# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예
# >>> areum.age
# 25
class Human:
    def __init__(self,name,age,sex) :
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("조아름", 25, "여자")
print('이름 : {}, 나이 : {}, 성별 : {}'.format(areum.name, areum.age, areum.sex))

# 257 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.sex))
areum = Human("조아름", 25, "여자")
areum.who()   

# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.sex))
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("불명", "미상", "모름")
areum.who()     
areum.setInfo("아름", 25, "여자")
areum.who()

# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __del__(self):
        print("나의 죽음을 알리지마라")
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("아름", 25, "여자")
del(areum)

# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
# class OMG : 
#     def print() :
#         print("Oh my god")
# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()
# TypeError: print() takes 0 positional arguments but 1 was given '''



''' # [241-250]
# 241 현재시간
# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
import datetime
print(datetime.datetime.now())

# 242 현재시간의 타입
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
import datetime
print(type(datetime.datetime.now()))

# 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
import datetime
now = datetime.datetime.now()
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(delta)
    print(date)

# 244 strftime
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# 18:35:01
import datetime
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

# 245 strptime
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. 
# "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
import datetime
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

# 246 sleep 함수 - 무한 루프
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
# import time
# import datetime
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
# 1) from datetime import datetime
# 2) from datetime import *
# 3) import datetime
# 4) import datetime as t

# 248 os 모듈
# os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
import os
ret = os.getcwd()
print(ret, type(ret))

# 249 rename 함수
# 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.
# import os
# os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

# 250 numpy
# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
import numpy
for i in numpy.arange(0, 5.1, 0.1):
    print(i) '''

''' # [231-240]
# 231 함수
# 아래 코드를 실행한 결과를 예상하라.
# def n_plus_1 (n) :
#     result = n + 1
# n_plus_1(3)
# print (result)
# 에러발생 지역함수 사용

# 232 함수
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com
def make_url(문자열):
    print('www.{}.com'.format(문자열))
make_url("naver")

# 233 함수
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']
a=[]
def make_list(문자열):
    for i in 문자열:
        a.append(i)
make_list("abcd")
print(a)

# 234 함수
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]
result = []
def pickup_even(리스트):
    for i in 리스트:
        if i % 2==0:
            result.append(i)
pickup_even([3, 4, 5, 6, 7, 8])
print(result)

# 235 함수
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# convert_int("1,234,567")
# 1234567
def convert_int(문자열):
    a=int(문자열.replace(',',''))
    print(a, type(a))
convert_int("1,234,567")

# 236 함수
# 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)
# 22

# 237 함수
# 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4
# c = 함수(함수(함수(10)))
# print(c)
# 22

# 238 함수
# 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     return num * 10
# a = 함수1(10)
# c = 함수2(a)
# print(c)
# 140

# 239 함수
# 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
# c = 함수2(10)
# print(c)
# 16

# 240 함수
# 아래 코드의 실행 결과를 예측하라.
# def 함수0(num) :
#     return num * 2
# def 함수1(num) :
#     return 함수0(num + 2)
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
# c = 함수2(2)
# print(c)
# 28 '''



''' # [221-230]
# 221
# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# print_reverse("python")
# nohtyp
def print_reverse(i):
    print(i[::-1])
print_reverse("python")

# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# print_score ([1, 2, 3])
# 2.0
def print_score(i):
    print(sum(i)/len(i))
print_score ([1, 2, 3])

# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12
def print_even(i):
    for j in i:
        if j % 2 ==0:
            print(j)
print_even ([1, 3, 2, 10, 12, 11, 15])

# 224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별
def print_keys(i):
    print(i.keys())
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# my_dict = {"10/26" : [100, 130, 100, 100],"10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]
my_dict = {"10/26" : [100, 130, 100, 100],"10/27" : [10, 12, 10, 11]}
def print_value_by_key (i, j):
    if j in i.keys():
        print(i[j])
print_value_by_key  (my_dict, "10/26")

# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸
def print_5xn(string):
    chunk_num = int(len(string) / 5)
    for x in range(chunk_num + 1) :
        print(string[x * 5: x * 5 + 5])
print_5xn("아이엠어보이유알어걸")

# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# print_mxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸
def print_mxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num])
print_mxn("아이엠어보이유알어걸", 3)

# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 
# 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# 1000000
def calc_monthly_salary(annual_salary):
    print(int(annual_salary/12))
calc_monthly_salary(12000000)

# 229
# 아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
# my_print(a=100, b=200)
# 왼쪽: 100, 오른쪽: 200

# 230
# 아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
# my_print(b=100, a=200)
# 왼쪽:200, 오른쪽:100 '''



''' # [211-220]
# 211 함수
# 함수의 호출 결과를 예측하라.
# def 함수(문자열) :
#     print(문자열)
# 함수("안녕")
# 함수("Hi")
# 안녕, Hi

# 212 함수
# 함수의 호출 결과를 예측하라.
# def 함수(a, b) :
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)
# 7, 15

# 213 함수
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'
# 함수에 매개변수가 한개 정의되어 있으나, 함수 호출 시 인수를 기재하지 않았다.

# 214 함수
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
# TypeError: must be str, not int
# 인수 두개를 매개변수로 넘겨줄 때, 문자열과 정수를 넘겨주었는데, + 연산을 실시하였다. 

# 215 함수
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def print_with_smile(i):
    print(i+':D')
a=input('문자열을 입력하세요 : ')
print_with_smile(a)

# 216 함수
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
def print_with_smile(i):
    print(i+':D')
print_with_smile('안녕하세요')

# 217 함수
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
def print_upper_price(a):
    print(a*1.3)
print_upper_price(100)

# 218 함수
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
a=int(input('첫번째 숫자를 입력하세요 : '))
b=int(input('두번째 숫자를 입력하세요 : '))
def print_sum(i,j):
    c=i+j
    print(c)
print_sum(a,b)

# 219 함수
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75
a=int(input('첫번째 숫자를 입력하세요 : '))
b=int(input('두번째 숫자를 입력하세요 : '))
def print_arithmetic_operation(i,j):
    print('{} + {} = {}'.format(i,j,i+j))
    print('{} - {} = {}'.format(i,j,i-j))
    print('{} * {} = {}'.format(i,j,i*j))
    print('{} / {} = {}'.format(i,j,i/j)) 
print_arithmetic_operation(a, b)

# 220 함수
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
a=int(input('첫번째 숫자를 입력하세요 : '))
b=int(input('두번째 숫자를 입력하세요 : '))
c=int(input('세번째 숫자를 입력하세요 : '))
d=a,b,c
def print_max(i):
    print(max(i))
print_max(d) '''



''' # [201-210]
# 201 함수
# "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print("비트코인")

# 202 함수
# 201번에서 정의한 함수를 호출하라.
def print_coin():
    print("비트코인")
print_coin()

# 203 함수
# 201번에서 정의한 print_coin 함수를 100번호출하라.
def print_coin():
    print("비트코인")
for i in range(100):
    print_coin()

# 204 함수
# "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coin():
    for i in range(100):
        print("비트코인")

# 205 함수
# 아래의 에러가 발생하는 이유에 대해 설명하라.
# hello()
# def hello():
#     print("Hi")
# 실행 예
# NameError: name 'hello' is not defined
# 함수 정의 전 함수를 호출하였음

# 206 함수
# 아래 코드의 실행 결과를 예측하라.
# def message() :
#     print("A")
#     print("B")
# message()
# print("C")
# message()
# A B C A B

# 207 함수
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message() :
#     print("B")
# print("C")
# message()
# A C B

# 208 함수
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()
# A C B E D

# 209 함수
# 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")
# def message2():
#     print("B")
#     message1()
# message2()
# B A

# 210 함수
# 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
# message3()
# B C B C B C A '''



''' # [191-200]
# 191 반복문
# data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.
# data = [[ 2000,  3050,  2050,  1980],[ 7500,  2050,  2050,  1980],[15450, 15050, 15550, 14900]]
# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
# 2000.28
# 3050.427
# 2050.2870000000003
# ...
data = [[ 2000,  3050,  2050,  1980],[ 7500,  2050,  2050,  1980],[15450, 15050, 15550, 14900]]
for row in data:
    for col in row:
        print(col*1.00014)

# 192 반복문
# 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.
# 2000.28
# 3050.427
# 2050.2870000000003
# 1980.2772
# ----
# 7501.05
# 2050.2870000000003
# 2050.2870000000003
# 1980.2772
# ----
# 15452.163
# 15052.107
# 15552.177
# 14902.086000000001
# ----
data = [[ 2000,  3050,  2050,  1980],[ 7500,  2050,  2050,  1980],[15450, 15050, 15550, 14900]]
for row in data:
    for col in row:
        print(col*1.00014)
    print('----')

# 193 반복문
# 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.
# >> print(result)
# [2000.28, 3050.427, 2050.2870000000003, 1980.2772, 7501.05, 2050.2870000000003, 2050.2870000000003, ...]
data = [[ 2000,  3050,  2050,  1980],[ 7500,  2050,  2050,  1980],[15450, 15050, 15550, 14900]]
result = []
for row in data:
    for col in row:
        result.append(col*1.00014)
print(result)

# 194 반복문
# 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.
# >> print(result)
# [
#  [2000.28, 3050.427, 2050.2870000000003, 1980.2772],
#  [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772],
#  [15452.163, 15052.107, 15552.177, 14902.086000000001]
# ]
data = [[ 2000,  3050,  2050,  1980],[ 7500,  2050,  2050,  1980],[15450, 15050, 15550, 14900]]
result = []
for row in data:
    sub = []
    for col in row:
        sub.append(col*1.00014)
    result.append(sub)
print(result)

# 195 반복문
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.
# ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
# 100
# 190
# 310
ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
for row in ohlc[1:]:
    print(row[3])

# 196 반복문
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.
# ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
# 190
# 310
ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
for row in ohlc[1:]:
    if row[3] > 150:
        print(row[3])

# 197 반복문
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
# ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
# 100
# 310
ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
for row in ohlc[1:]:
    if row[3] >= row[0]:
        print(row[3])

# 198 반복문
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 
# 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
# ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
# >> print(volatility)
# [40, 30, 10]
ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1]-row[2])
print(volatility)

# 199 반복문
# 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.
# ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
# 종가가 시가보다 높은 거래일의 OHLC는 [300, 310, 300, 310] 이다. 따라서 이 거래일의 변동성은 10 (310 - 300)이다.
# 10
ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
for row in ohlc[1:]:
    if row[3]-row[0] > 0:
        print(row[3]-row[0])

# 200 반복문
# 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
# ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
# 1일차 수익 0원 (100 - 100), 2일차 수익 -10원 (190 - 200), 3일차 수익 10원 (310 - 300) 이다.
# 0
ohlc = [["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]]
hab =0
for row in ohlc[1:]:
    hab=hab+(row[3]-row[0])
print(hab) '''



''' # [181-190]
# 181 반복문
# 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
# 101호	102호
# 201호	202호
# 301호	302호
리스트 = [['101호', '102호'],['201호', '202호'],['301호', '302호']]
print(리스트)

# 182 반복문
# 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
# 시가	종가
# 100	80
# 200	210
# 300	330
리스트 = [[100, 80], [200, 210], [300, 330]]
print(리스트)

# 183 반복문
# 아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
# 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
# 시가	종가
# 100	80
# 200	210
# 300	330
딕셔너리 = {'100':80, '200':210, '300':330}
print(딕셔너리)

# 184 반복문
# 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다.
# 첫 열이 날짜이다.
# 10/10	80	110	70	90
# 10/11	210	230	190	200
딕셔너리 = {'10/10':[80,110,70,90], '10/11':[210,230,190,200]}
print(딕셔너리)

# 185 반복문
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")

# 186 반복문
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 301 호
# 302 호
# 201 호
# 202 호
# 101 호
# 102 호
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    for col in row:
        print(col, "호")

# 187 반복문
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 302 호
# 301 호
# 202 호
# 201 호
# 102 호
# 101 호
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    for col in row[::-1]:
        print(col, "호")

# 188 반복문
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# -----
# 102 호
# -----
# 201 호
# -----
# 202 호
# -----
# 301 호
# -----
# 302 호
# -----
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
        print('-----')

# 189 반복문
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# -----
# 201 호
# 202 호
# -----
# 301 호
# 302 호
# -----
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
    print('-----')

# 190 반복문
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# -----
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
print('-----') '''



''' # [171-180]
# 171 반복문
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 32100
# 32150
# 32000
# 32500
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

# 172 반복문
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])

# 173 반복문
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])

# 174 반복문
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500
price_list = [32100, 32150, 32000, 32500]
for i in range(3):
    print(100+i*10, price_list[i])

# 175 반복문
# my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1])

# 176 반복문
# 리스트를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라", "마"]
# 가 나 다
# 나 다 라
# 다 라 마
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2):
    print(my_list[i], my_list[i+1], my_list[i+2])

# 177 반복문
# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가
my_list = ["가", "나", "다", "라"]
for i in range(3,0,-1):
    print(my_list[i], my_list[i-1])

# 178 반복문
# 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
# my_list = [100, 200, 400, 800]
# 예를들어 100을 기준으로 우측에 위치한 200과의 차분 값를 화면에 출력하고, 
# 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다.
# 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.
# 100
# 200
# 400
my_list = [100, 200, 400, 800]
for i in range(3):
    print(my_list[i+1]-my_list[i])

# 179 반복문
# 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
# my_list = [100, 200, 400, 800, 1000, 1300]
# 첫 번째 줄에는 100, 200, 400의 평균값이 출력된다. 두 번째 줄에는 200, 400, 800의 평균값이 출력된다. 같은 방식으로 나머지 데이터의 평균을 출력한다.
# 233.33333333333334
# 466.6666666666667
# 733.3333333333334
# 1033.3333333333333
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(4):
    a=my_list[i:i+3]
    print(sum(a)/3.0)

# 180 반복문
# 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을
# volatility 리스트에 저장하라.
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    a=high_prices[i]-low_prices[i]
    volatility.append(a)
print(volatility) '''



'''# [161-170]
# 161 반복문
# for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
for i in range(0,100):
    print(i)

# 162 반복문
# 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
for i in range(2002,2051):
    if i % 4 == 0:
        print(i)

# 163 반복문
# 1부터 30까지의 숫자 중 3의 배수를 출력하라.
for i in range(1,31):
    if i % 3 == 0:
        print(i)

# 164 반복문
# 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for i in range(99,-1,-1):
    print(i)

# 166 반복문
# 구구단 3단을 출력하라.
for i in range(1,10):
    print('3 x {} = {}'.format(i,i*3))

# 167 반복문
# 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
for i in range(1,10):
    if i % 2 == 1:
        print('3 x {} = {}'.format(i,i*3))

# 168 반복문
# 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
hab = 0
for i in range(1, 11):
    hab += i
print("합 :", hab)

# 169 반복문
# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
hab = 0
for i in range(1, 11, 2):
    hab += i
print("합 :", hab)

# 170 반복문
# 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
gob = 1
for i in range(1,11):
    gob *= i
print('곱 :',gob) '''



''' # [151-160]
# 151 반복문
# 리스트에는 네 개의 정수가 저장돼 있다.
# 리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0:
        print('음수 =',i)

# 152 반복문
# for문을 사용해서 3의 배수만을 출력하라.
# 리스트 = [3, 100, 23, 44]
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i % 3 == 0:
        print('3의 배수 =',i)

# 153 반복문
# 리스트에서 20 보다 작은 3의 배수를 출력하라
# 리스트 = [13, 21, 12, 14, 30, 18]
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if (i <= 20) and (i % 3 == 0) :
        print('20보다 작은 3의 배수 =',i)

# 154 반복문
# 리스트에서 세 글자 이상의 문자를 화면에 출력하라
# 리스트 = ["I", "study", "python", "language", "!"]
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)

# 155 반복문
# 리스트에서 대문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# (참고) isupper() 메서드는 대문자 여부를 판별합니다.
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():
        print(i)

# 156 반복문
# 리스트에서 소문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.islower():
        print(i)

# 157 반복문
# 이름의 첫 글자를 대문자로 변경해서 출력하라.
# 리스트 = ['dog', 'cat', 'parrot']
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    if i[0:1].islower:
        print(i[0:1].upper()+i[1:])

# 158 반복문
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
a=''
b=''
for i in 리스트:
    a, b = i.split('.')
    print(a, type(a))

# 159 반복문
# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
a=''
b=''
for i in 리스트:
    a, b = i.split('.')
    if b[0:1]=='h':
        print(i)

# 160 반복문
# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
a=''
b=''
for i in 리스트:
    a, b = i.split('.')
    if b[0:1]=='h' or b[0:1]=='c':
        print(i) '''



'''# [141-150]
# 141 반복문
# 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 
# 단 부가세는 10원으로 가정한다.
# 리스트 = [100, 200, 300]
# 110
# 210
# 310
리스트 = [100, 200, 300]
for i in 리스트:
    print(i+10)

# 142 반복문
# for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
# 리스트 = ["김밥", "라면", "튀김"]
# 오늘의 메뉴: 김밥
# 오늘의 메뉴: 라면
# 오늘의 메뉴: 튀김
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print('오늘의 메뉴 : ',i)

# 143 반복문
# 리스트에 주식 종목이름이 저장돼 있다.
# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# 저장된 문자열의 길이를 다음과 같이 출력하라.
# 6
# 4
# 4
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

# 144 반복문
# 리스트에는 동물이름이 문자열로 저장돼 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# 동물 이름과 글자수를 다음과 같이 출력하라.
# dog 3
# cat 3
# parrot 6
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

# 145 반복문
# 리스트에 동물 이름 저장돼 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# for문을 사용해서 동물 이름의 첫 글자만 출력하라.
# d
# c
# p
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[:1])

# 146 반복문
# 리스트에는 세 개의 숫자가 바인딩돼 있다.
# 리스트 = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하라.
# 3 x 1
# 3 x 2
# 3 x 3
리스트 = [1, 2, 3]
for i in 리스트:
    print('3 x', i)

# 147 반복문
# 리스트에는 세 개의 숫자가 바인딩돼 있다.
# 리스트 = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하라.
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
리스트 = [1, 2, 3]
for i in 리스트:
    print('3 x', i*3)

# 148 반복문
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 나
# 다
# 라
리스트 = ["가", "나", "다", "라"]
뉴리스트 = 리스트[1:]
for i in 뉴리스트:
    print(i)

# 149 반복문
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 가
# 다
리스트 = ["가", "나", "다", "라"]
뉴리스트 = 리스트[:2]
for i in 뉴리스트:
    print(i)

# 150 반복문
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 라
# 다
# 나
# 가
리스트 = ["가", "나", "다", "라"]
뉴리스트 = 리스트[::-1]
for i in 뉴리스트:
    print(i) '''



''' # [131-140]
# 131 반복문
# for문의 실행결과를 예측하라.
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

# 132 반복문
# for문의 실행결과를 예측하라.
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print("#####")

# 133 반복문
# 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
# for 변수 in ["A", "B", "C"]:
#   print(변수)
for 변수 in ["A", "B", "C"]:
    print(변수)

# 134 반복문
# for문을 풀어서 동일한 동작을하는 코드를 작성하라.
# for 변수 in ["A", "B", "C"]:
#   print("출력:", 변수)
for 변수 in ["A", "B", "C"]:
    print("출력:", 변수)

# 135 반복문
# for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
for 변수 in ["A", "B", "C"]:
    b = 변수.lower()
    print("변환:", b)

# 136 반복문
# 다음 코드를 for문으로 작성하라.
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
for 변수 in [10,20,30]:
    print('변수 = ',변수)

# 137 반복문
# 다음 코드를 for문으로 작성하라.
# print(10)
# print(20)
# print(30)
for 변수 in [10,20,30]:
    print('print(%d)'%변수)

# 138 반복문
# 다음 코드를 for문으로 작성하라.
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
for 변수 in [10,20,30]:
    print('print(%d)'%변수)
    print('print("------")')

# 139 반복문
# 다음 코드를 for문으로 작성하라.
# print("++++")
# print(10)
# print(20)
# print(30)
print('print("++++")')
for 변수 in [10,20,30]:
    print('print(%d)'%변수)

# 140 반복문
# 다음 코드를 for문으로 작성하라.
# print("-------")
# print("-------")
# print("-------")
# print("-------")
for 변수 in range(1,5):
    print('print("-------")') '''



''' # [121-130]
# 121 분기문
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
a=input('영문자 한개를 입력하세요 : ')
if a.islower():
    print(a.upper())
else:
    print(a)

# 122 분기문
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
score=int(input('점수를 입력하세요.(0-100 사이의 정수) : '))
if score > 80:
    print('A')
elif score > 60:
    print('B')
elif score > 40:
    print('C')
elif score > 20:
    print('D')
else:
    print('E')

# 123 분기문
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171
환율 = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
user = input("입력(금액과 통화명 사이에 공백을 두세요.) : ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

# 124 분기문
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
a=int(input('한개의 정수를 입력하세요.(첫번째 숫자) : '))
b=int(input('한개의 정수를 입력하세요.(두번째 숫자) : '))
c=int(input('한개의 정수를 입력하세요.(세번째 숫자) : '))
d=a,b,c
print(max(d))

# 125 분기문
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 
# 통신사를 출력하는 프로그램을 작성하라.
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
통신사 = {'011':'SKT', '016':'KT', '019':'LGU', '010':'알수없음'}
number = input("휴대전화 번호 입력 (입력예 '000-0000-0000') : ")
num = number[0:3]
if num in 통신사.keys():
    if num == '011':
        print(통신사[num])
    elif num == '016':
        print(통신사[num])
    elif num == '019':
        print(통신사[num])
    elif num == '010':
        print(통신사[num])

# 126 분기문
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
# -	  0	      1	      2	      3	      4	      5	       6	  7	      8	     9 
# 01 강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")

# 127 분기문
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
주민번호 = input("주민등록번호: ")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0] == "1" or 주민번호[0] == "3":
    print("남자")
else:
    print("여자")

# 128 분기문
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
주민번호 = input("주민등록번호 (입력예 : 000000-0000000) : ")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

# 129 분기문
# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5 
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다.
#  즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.
# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)
if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

# 130 분기문
# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 
# 그렇지 않은 경우 "하락장" 문자열을 출력하라.
# Key Name	Description
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price	최근 24시간 내 최저 거래금액
# max_price	최근 24시간 내 최고 거래금액
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장") '''



''' # [111-120]
# 111 분기문
# 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
print('안녕하세요'*2)

# 112 분기문
# 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
a=input("하나의 숫자를 입력하세요 : ")
b=int(a)
c=b+10
print(c)

# 113 분기문
# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
a=int(input("하나의 숫자를 입력하세요 : "))
if a%2==0:
    print('입력하신 숫자 {}는 짝수입니다.'.format(a))
else:
    print('입력하신 숫자 {}는 홀수입니다.'.format(a))

# 114 분기문
# 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
a=int(input("하나의 숫자를 입력하세요 : "))
b=a+20
if b>255:
    print("결과값이 255를 초과하였습니다.")
else:
    print("결과값은 {}입니다.".format(b))

# 115 분기문
# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 
# 단 출력 값의 범위는 0~255이다. 
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
a=int(input("하나의 숫자를 입력하세요 : "))
b=a-20
if b<0:
    print("결과값이 0 미만입니다.")
elif b>255:
    print("결과값이 255 초과입니다.")
else:
    print("결과값이 {}입니다".format(b))

# 116 분기문
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.
time = input("현재시간을 입력하세요 : (입력형태->시간:분 형태('00:00')) ")
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

# 117 분기문
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = ["사과", "포도", "홍시"]
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은? ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

# 118 분기문
# 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면
# '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user=input('종목명을 입력하세요. : ')
if user in warn_investment_list:
    print('투자 경고 종목입니다')
else:
    print("투자 경고 종목이 아닙니다.")

# 119 분기문
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user=input('key값을 입력하세요 : ')
if user in fruit.keys():
    print("정답입니다.")
else:
    print("오답입니다.")

# 120 분기문
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user=input('value값을 입력하세요 : ')
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.") '''



''' # [101-110]
# 101 분기문
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# bool

# 102 분기문
# 아래 코드의 출력 결과를 예상하라
# print(3 == 5)
print(3 == 5)

# 103 분기문
# 아래 코드의 출력 결과를 예상하라
# print(3 < 5)
print(3 < 5)

# 104 분기문
# 아래 코드의 결과를 예상하라.
# x = 4
# print(1 < x < 5)
x = 4
print(1 < x < 5)

# 105 분기문
# 아래 코드의 결과를 예상하라.
# print ((3 == 3) and (4 != 3))
print ((3 == 3) and (4 != 3))

# 106 분기문
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3 => 4)
# 부등호가 먼저 와야함.

# 107 분기문
# 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#     print("Hello World")
if 4 < 3:
    print("Hello World")

# 108 분기문
# 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

# 109 분기문
# 아래 코드의 출력 결과를 예상하라
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")

# 110 분기문
# 아래 코드의 출력 결과를 예상하라
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5") '''



''' # [091-100]
# 091 딕셔너리 생성
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
# 이름	가격	재고
# 메로나	300	20
# 비비빅	400	3
# 죠스바	250	100
inventory={'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}
print(inventory)

# 092 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
# inventory = {"메로나": [300, 20],"비비빅": [400, 3],"죠스바": [250, 100]}
inventory = {"메로나": [300, 20],"비비빅": [400, 3],"죠스바": [250, 100]}
print(inventory['메로나'][0])

# 093 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
# inventory = {"메로나": [300, 20],"비비빅": [400, 3],"죠스바": [250, 100]}
inventory = {"메로나": [300, 20],"비비빅": [400, 3],"죠스바": [250, 100]}
print(inventory['메로나'][1])

# 094 딕셔너리 추가
# inventory 딕셔너리에 아래 데이터를 추가하라.
# 이름	가격	재고
# 월드콘	500	7
# inventory = {"메로나": [300, 20],"비비빅": [400, 3],"죠스바": [250, 100]}
inventory = {"메로나": [300, 20],"비비빅": [400, 3],"죠스바": [250, 100]}
inventory['월드콘']=[500,7]
print(inventory)

# 095 딕셔너리 keys() 메서드
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
a=icecream.keys()
b=list(a)
print(a,type(a))
print(b,type(b))

# 096 딕셔너리 values() 메서드
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
a=icecream.values()
b=list(a)
print(a,type(a))
print(b,type(b))

# 097 딕셔너리 values() 메서드
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
a=icecream.values()
b=list(a)
c=sum(a)
print(c)

# 098 딕셔너리 update 메서드
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 099 zip과 dict
# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 100 zip과 dict
# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table=dict(zip(date,close_price)) '''



'''# [081-090]
# 081 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)

# 082 별 표현식
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score=scores
print(valid_score)

# 083 별 표현식
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores
print(valid_score)

# 084 비어있는 딕셔너리
# temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}
print(temp,type(temp))

# 085 딕셔너리 생성
# 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
# 이름	희망 가격
# 메로나	1000
# 폴라포	1200
# 빵빠레	1800
ice = {'메로나':1000,'폴라포':1200,'빵바레':1800}
print(ice, type(ice))

# 086 딕셔너리 추가
# 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
# 이름	희망 가격
# 죠스바	1200
# 월드콘	1500
ice = {'메로나':1000,'폴라포':1200,'빵바레':1800}
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)

# 087 딕셔너리 출력
# 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
# ice = {'메로나': 1000,'폴로포': 1200,'빵빠레': 1800,'죠스바': 1200,'월드콘': 1500}
ice = {'메로나': 1000,'폴로포': 1200,'빵빠레': 1800,'죠스바': 1200,'월드콘': 1500}
print('메로나 가격 :',ice['메로나'])

# 088 딕셔너리 수정
# 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
# ice = {'메로나': 1000,'폴로포': 1200,'빵빠레': 1800,'죠스바': 1200,'월드콘': 1500}
ice = {'메로나': 1000,'폴로포': 1200,'빵빠레': 1800,'죠스바': 1200,'월드콘': 1500}
ice['메로나']=1300
print(ice)

# 089 딕셔너리 삭제
# 다음 딕셔너리에서 메로나를 삭제하라.
# ice = {'메로나': 1000,'폴로포': 1200,'빵빠레': 1800,'죠스바': 1200,'월드콘': 1500}
ice = {'메로나': 1000,'폴로포': 1200,'빵빠레': 1800,'죠스바': 1200,'월드콘': 1500}
del ice["메로나"]
print(ice)

# 090 딕셔너리
# 다음 코드에서 에러가 발생한 원인을 설명하라.
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# 딕셔너리의 없는 키 값을 조회하였음 '''



''' # [071-080]
# 071 튜플 만들기
# my_variable 이름의 비어있는 튜플을 만들라.
my_variable = 1,2
print(my_variable, type(my_variable))
my_variable = (1,2)
print(my_variable, type(my_variable))
my_variable = (1,)
print(my_variable, type(my_variable))
my_variable = (1)
print(my_variable, type(my_variable))

# 072 튜플 만들기
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank = '닥터 스트레인지', '스플릿', '럭키'
print(movie_rank, type(movie_rank))

# 073 튜플 만들기
# 숫자 1 이 저장된 튜플을 생성하라.
my_variable = (1,)
print(my_variable, type(my_variable))

# 074 튜플 수정
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# 튜플은 index 변경이 불가하다.

# 075 튜플 입력법
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
t = 1, 2, 3, 4
print(type(t))

# 076 튜플 수정
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# t = ('a', 'b', 'c')
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

# 077 튜플 변환
# 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
a=list(interest)
print(a, type(a))

# 078 리스트 변환
# 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = ['삼성전자', 'LG전자', 'SK Hynix']
a=tuple(interest)
print(a, type(a))

# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# (2, 4, 6, 8 ... 98)
a=tuple(range(1,100,2))
print(a,type(a)) '''



''' # [061-070]
# 061 리스트 슬라이싱
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# price = ['20180728', 100, 130, 140, 150, 160, 170]
price = ['20180728', 100, 130, 140, 150, 160, 170]
a=price[1:]
print(a)

# 062 리스트 슬라이싱
# 슬라이싱을 사용해서 홀수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=nums[::2]
print(a)

# 063 리스트 슬라이싱
# 슬라이싱을 사용해서 짝수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=nums[1::2]
print(a)

# 064 리스트 슬라이싱
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5]
a=nums[::-1]
print(a)

# 065 리스트 인덱싱
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver
interest = ['삼성전자', 'LG전자', 'Naver']
a=interest[0]
b=interest[2]
print(f'{a}, {b}')

# 066 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# 067 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))

# 068 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

# 069 문자열 split 메서드
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)

# 070 리스트 정렬
# 리스트에 있는 값을 오름차순으로 정렬하세요.
# data = [2, 4, 3, 1, 5, 10, 9]
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
data.reverse()
print(data) '''



''' # [051-060]
# 051 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank=['닥터 스트레인지','스플릿','럭키']
print(movie_rank)

# 052 리스트에 원소 추가
# 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank=['닥터 스트레인지','스플릿','럭키']
movie_rank.append('배트맨')
print(movie_rank)

# 053 리스트에 원소 추가
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054 리스트 원소 삭제
# movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 056 리스트 합치기
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
# >> lang1 = ["C", "C++", "JAVA"]
# >> lang2 = ["Python", "Go", "C#"]
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
print(langs)

# 057 리스트 최댓값과 최솟값 구하기
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
# nums = [1, 2, 3, 4, 5, 6, 7]
nums = [1, 2, 3, 4, 5, 6, 7]
a=min(nums)
b=max(nums)
print(a,b)

# 058 리스트의 합 구하기
# 다음 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5]
a=sum(nums)
print(a)

# 059 리스트의 개수 구하기
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
a=len(cook)
print(a)

# 060 리스트의 평균 구하기
# 다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5]
a=sum(nums)/len(nums)
print(a) '''



''' # [041-050]
# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
# ticker = "btc_krw"
ticker = "btc_krw"
a=ticker.upper()
print(a)

# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
# ticker = "BTC_KRW"
ticker = "BTC_KRW"
a=ticker.lower()
print(a)

# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
a='hello'
b=a.capitalize()
print(b)

# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"
file_name = "보고서.xlsx"
b=file_name.endswith('xlsx')
print(b)

# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"
file_name = "보고서.xlsx"
b=file_name.endswith('xlsx' or 'xls')
print(b)

# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
# file_name = "2020_보고서.xlsx"
file_name = "2020_보고서.xlsx"
b=file_name.startswith('2020')
print(b)

# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# a = "hello world"
a = "hello world"
b=a.split(' ')
print(b,type(b))

# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"
ticker = "btc_krw"
b=ticker.split('_')
print(b,type(b))

# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# date = "2020-05-01"
date = "2020-05-01"
b=date.split('-')
print(b,type(b))

# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# data = "039490     "
data = "039490     "
b=data.rstrip()
print(b,type(b)) '''



''' # [031-040]
# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.
# >> a = "3"
# >> b = "4"
# >> print(a + b)
a = "3"
b = "4"
print(a + b)

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
# >> print("Hi" * 3)
print("Hi" * 3)

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.
print('-'*80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# >>> t1 = 'python'
# >>> t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예:
# python java python java python java python java
t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ')*4)

# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1,age1))
print("이름: %s 나이: %d" % (name2,age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: {} 나이: {}'.format(name1,age1))
print('이름: {} 나이: {}'.format(name2,age2))

# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"
상장주식수 = "5,969,782,550"
a=상장주식수.replace(',','')
b=int(a)
print(f'b={b}, type(b)={type(b)}')

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"
분기 = "2020/03(E) (IFRS연결)"
a=분기[0:7]
print(a)

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
# data = "   삼성전자    "
data = "   삼성전자    "
a=data.replace(' ','')
print(a) '''



''' # [021-030]
# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
letters='python'
a=letters[0:1]+letters[2:3]
print(a)

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
a=license_plate[-4:]
print(a)

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
string = "홀짝홀짝홀짝"
for i in string:
    if i=="홀":
        print(i,end="")
print()

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
string = "PYTHON"
a=string[::-1]
print(a)

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
phone_number = "010-1111-2222"
a=phone_number.replace('-',' ')
print(a)

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number = "010-1111-2222"
a=phone_number.replace('-',' ')
b=a.replace(' ','')
print(b)

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
url = "http://sharebook.kr"
a=url[-2:]
print(a)

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# >> lang = 'python'
# >> lang[0] = 'P' #에러 발생함. 문자열은 변경 불가함. 
# >> print(lang)

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# >> string = 'abcdfe2a354a32a'
string = 'abcdfe2a354a32a'
a=string.replace('a','A')
print(a)

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
string = 'abcd'; string.replace('b', 'B'); print(string) '''



''' # [011-020]
# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자=50000
주식수=10
총평가금액=삼성전자*주식수
print('{0:+,}'.format(총평가금액))

# 012 변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
# 항목	값
# 시가총액	298조
# 현재가	50,000원
# PER	15.79
시가총액 = "298조"
현재가 = "50,000원"
PER = 15.79

# 013 문자열 출력
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
# s = "hello"
# t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# 실행 예 : hello! python
s='hello'
t='python'
print('{}! {}'.format(s,t))

# 014 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보세요.
# >> 2 + 2 * 3 
print(2+2*3)

# 015 type 함수
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
# >> a = "132"
a=128
print('a={}, type(a)={}'.format(a,type(a)))
a="132"
print('a={}, type(a)={}'.format(a,type(a)))

# 016 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환해보세요.
# >> num_str = "720"
num_str='720'
b=int(num_str)
print('type(num_str)={}, type(b)={}'.format(type(num_str),type(b)))

# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
b=str(num)
print('type(num)={}, type(b)={}'.format(type(num),type(b)))

# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
a="15.79"
b=float(a)
print('type(a)={}, type(b)={}'.format(type(a),type(b)))

# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year='2019'
year_int=int(year)
print('올해={}년, 내년={}년, 내후년={}년'.format(year_int, year_int+1, year_int+2))

# 020 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
month_payment=42548
total_month=36
total_amount=month_payment*total_month
print('총금액은={:+,}입니다.'.format(total_amount)) '''



''' # [001-010]
# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.
print('Hello World')

# 002 print 기초
# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")

# 003 print 기초
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)(신씨가 소리질렀다. "도둑이야".)
print('신씨가 소리질렀다. "도둑이야".')

# 004 print 기초
# 화면에 "C:\aWindows"를 출력하세요.
print('"c:\\aWindows"')

# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t\t반갑습니다.")

# 006 print 여러 데이터 출력
# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print ("오늘은", "일요일")

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print('naver','kakao','sk','samsung',sep=';')

# 008 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung
print('naver','kakao','sk','samsung',sep='/')

# 009 print 줄바꿈
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 
# 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# print("first");print("second")
print("first", end=""); print("second")

# 010 연산 결과 출력
# 5/3의 결과를 화면에 출력하세요.
print(5/3) '''