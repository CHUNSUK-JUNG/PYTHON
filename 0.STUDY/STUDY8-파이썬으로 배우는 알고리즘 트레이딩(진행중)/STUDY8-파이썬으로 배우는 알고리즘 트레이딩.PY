# 출처 [https://wikidocs.net/book/110, 파이썬으로 배우는 알고리즘 트레이딩 (개정판-2쇄)]


# [00. 들어가기 전에]
# 본 도서는 파이썬 이라는 프로그래밍 언어를 사용하여 효율적으로 주식 데이터를 분석하는 방법에 대해서 다룹니다. 이를 바탕으로 
# 여러분만의 투자 기법을 평가하고 더 나아가 자동화된 트레이딩 시스템으로 구축하는 최종 목표로 합니다.


# [08. 실전 프로젝트]

# [8.2 주소록 프로젝트]
# 아이폰이나 안드로이드폰을 보면 이름, 전화번호, 이메일 등을 저장하고 관리할 수 있는 주소록이 기본으로 제공됩니다.
# 이번 절에서는 파이썬을 이용해 주소록을 관리하는 프로그램을 직접 개발해 보겠습니다.
# PyCharm을 실행한 후 그림 8.21과 같이 ‘Contact’라는 이름의 프로젝트를 생성합니다.
# Contact 프로젝트에 contact.py 파일을 추가한 후 다음과 같이 기본 코드를 작성합니다. 그리고 Ctrl + F9 키를 눌러 화면에 'Contact'라는
# 문자열이 정상적으로 출력되는지 확인합니다.
# def run():
#     print("Contact")
# if __name__ == "__main__":
#     run()
''' def run():
    print("Contact")
if __name__ == "__main__":
    run() '''

# [1) Contact 클래스 만들기]
# 아이폰이나 안드로이드폰의 연락처 프로그램을 살펴보면 연락처에는 이름, 전화번호, 이메일, 주소 등을 입력할 수 있습니다. 이를 파이썬에서 제공하는
# 기본 자료형으로 표현하기보다 하나의 클래스로 정의하는 것이 좋습니다.
# 6장에서 배운 클래스를 이용해 다음과 같이 'Contact'라는 이름의 클래스를 정의하겠습니다. 클래스 인스턴스를 생성할 때 이름, 전화번호, 이메일, 주소를
# 입력받을 수 있게 생성자를 선언하고 인스턴스 변수에 저장된 정보를 화면에 출력하기 위해 print_info라는 메서드도 정의했습니다.
# class Contact:
#     def __init__(self, name, phone_number, e_mail, addr):
#         self.name = name
#         self.phone_number = phone_number
#         self.e_mail = e_mail
#         self.addr = addr
#     def print_info(self):
#         print("Name: ", self.name)
#         print("Phone Number: ", self.phone_number)
#         print("E-mail: ", self.e_mail)
#         print("Address: ", self.addr)
# 정의한 Contact 클래스가 제대로 동작하는지 확인하기 위해 앞서 작성한 run 함수를 수정해 연락처를 입력하고 입력된 정보를 화면에 출력해 보겠습니다.
# 이를 위해 다음과 같이 Contact 클래스에 대한 인스턴스를 생성합니다.
# def run():
#     kim = Contact('김일구', '010-8812-1193', 'ilgu.kim@python.com', 'Seoul')
#     kim.print_info()
# 지금까지 작성한 전체 코드는 다음과 같습니다.
''' class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)
def run():
    kim = Contact('김일구', '010-8812-1193', 'ilgu.kim@python.com', 'Seoul')
    kim.print_info()
if __name__ == "__main__":
    run() '''

# [2) 사용자로부터 데이터 입력받기]
# 이번 절에서는 사용자로부터 데이터를 입력받아 보겠습니다. 파이썬에서 사용자로부터 데이터를 입력 받을 때는 input 함수를 사용합니다.
# 사용자로부터 데이터를 입력받는 함수인 set_contact 함수를 새로 정의하고 run 함수에서 set_contact 함수를 호출하도록 코드를 변경해 봅시다.
''' class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    print(name, phone_number, e_mail, addr)
def run():
    set_contact()
if __name__ == "__main__":
    run() '''

# [3) 메인 메뉴 구성하기]
# 여러분이 작성할 연락처 프로그램은 기본적으로 연락처 입력, 연락처 출력, 연락처 삭제, 종료 기능을 제공합니다. 작성된 연락처 프로그램은 계속 실행 
# 상태를 유지하다가 사용자로부터 종료 명령을 받으면 프로그램이 종료해야 합니다. 이번 절에서는 이러한 기본 실행 구조를 파이썬 코드로 작성해 
# 보겠습니다.
# 작성한 프로그램이 한 번 실행됐을 때 종료하지 않은 상태로 계속 실행되게 하려면 무한 루프를 사용해야 합니다. 파이썬에서는 'while 1'이라는 구문을 
# 사용하면 프로그램이 계속 실행되도록 만들 수 있습니다. 하지만 사용자로부터 종료 명령을 받았을 때는 프로그램이 종료해야겠지요? 이를 위해서는 
# while 문 내부에서 if 문을 사용해 조건에 따라 while 문이 종료하도록 만들면 됩니다.
# 여기서 while 문은 결국 반복문이기 때문에 이를 종료하려면 반복문을 빠져나오면 됩니다. 이러한 용도로 사용하는 구문이 바로 break 문입니다. 지금까지
# 설명한 내용을 코드로 작성하면 다음과 같습니다. 참고로 지금부터는 지면상 새로 추가된 부분이나 수정된 코드만 표시하겠습니다.
''' def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)
def run():
    while 1:
        menu = print_menu()
        if menu == 4:
            break
if __name__ == "__main__":
    run() '''

# [4) 연락처 입력 동작 시키기]
# 이번에는 1번 메뉴인 ‘연락처 입력’ 기능이 정상적으로 동작하도록 프로그램을 변경해 보겠습니다. 먼저 사용자가 입력한 연락처 정보를 이용해 Contact
# 클래스 인스턴스를 생성하고 생성된 인스턴스를 반환하도록 set_contact 함수를 수정하겠습니다. set_contact 함수의 마지막 두 줄에서 Contact 클래스의
# 인스턴스를 생성하고 이를 반환하는 것을 확인할 수 있습니다.
# def set_contact():
#     name = input("Name: ")
#     phone_number = input("Phone Number: ")
#     e_mail = input("E-mail: ")
#     addr = input("Address: ")
#     contact = Contact(name, phone_number, e_mail, addr)
#     return contact
# 현재 set_contact 함수는 단순히 함수가 정의된 상태입니다. 이 함수가 정상적으로 동작하려면 어디선가 해당 함수를 호출해야 합니다. set_contact 함수는
# 사용자로부터 연락처를 입력받을 때 사용하는 함수이므로 사용자가 ‘1. 연락처 입력’ 메뉴를 선택했을 때 run 함수에서 set_contact 함수를 호출하면
# 됩니다.
# 다음과 같이 기존에 작성된 run 함수를 수정해 사용자가 1번 메뉴를 선택했을 때 set_contact 함수를 호출하도록 변경해 봅시다. 그리고 set_contact 
# 함수의 반환값인 Contact 인스턴스를 저장하기 위해 contact_list라는 이름의 리스트 자료구조를 생성하고 해당 리스트에 생성된 인스턴스를 추가해
# 봅시다.
# def run():
#     contact_list = []
#     while 1:
#         menu = print_menu()
#         if menu == 1:
#             contact = set_contact()
#             contact_list.append(contact)
#         elif menu == 4:
#             break
# 예제 8.1은 지금까지 작성한 코드입니다. 중간중간 코드를 수정하다가 흐름을 놓친 분들은 다음의 전체 코드를 살펴보시기 바랍니다.
''' class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)
def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 4:
            break
if __name__ == "__main__":
    run() '''

# [5) 연락처 출력하기]
# 이번에는 연락처를 출력하는 기능을 추가해 보겠습니다. 앞서 작성한 코드에서 연락처는 Contact라는 클래스의 인스턴스 형태로 저장되며, 인스턴스는
# contact_list라는 이름의 리스트를 통해 순서대로 저장됩니다. 즉, 입력된 연락처를 모두 출력하려면 contact_list에 있는 인스턴스에 저장된 정보를 
# 출력하면 되는 것입니다.
# 이미 여러분은 Contact 클래스를 정의할 때 인스턴스 변수의 데이터를 화면에 출력하는 메서드인 print_info 함수를 정의해 놓았습니다. 따라서 연락처를
# 출력하는 함수는 다음과 같이 간단히 구현할 수 있습니다.
# def print_contact(contact_list):
#     for contact in contact_list:
#         contact.print_info()
# print_contact 함수는 Contact 인스턴스를 저장하고 있는 리스트를 인자를 입력받은 후 for 문을 이용해 리스트에 저장된 인스턴스를 순회합니다.
# 이때 각 인스턴스에서 print_info 메서드를 호출합니다.
# 연락처 출력 기능은 메인 메뉴에서 ‘2. 연락처 출력’을 선택했을 때 수행돼야 합니다. 따라서 다음과 같이 run 함수도 수정합니다.
# def run():
#     contact_list = []
#     while 1:
#         menu = print_menu()
#         if menu == 1:
#             contact = set_contact()
#             contact_list.append(contact)
#         elif menu == 2:
#             print_contact(contact_list)
#         elif menu == 4:
#             break

# [6) 연락처 삭제하기]
# 이번에는 입력된 연락처를 삭제하는 기능을 추가해 보겠습니다. 연락처를 삭제하려면 삭제하고자 하는 연락처의 이름을 입력받은 후 연락처
# 리스트에서 해당 이름을 찾아서 지우면 됩니다.
# 연락처 리스트에서 연락처를 삭제하기 위해 다음과 같이 delete_contact 함수를 작성합니다. 이 함수는 연락처 리스트와 삭제할 이름을 인자로 
# 입력받습니다. delete_contact 함수는 연락처 리스트에 저장된 인스턴스 중 삭제하고자 하는 연락처 이름과 같은 연락처가 있는지 확인한 후 같은 
# 연락처가 있을 때 해당 연락처를 삭제합니다.
# def delete_contact(contact_list, name):
#     for i, contact in enumerate(contact_list):
#         if contact.name == name:
#             del contact_list[i]
# 연락처를 삭제하는 함수를 작성했다면 이번에는 run 함수를 수정하겠습니다. 연락처 삭제는 ‘3. 연락처 삭제’ 메뉴를 선택했을 때 동작하는데, 이때
# 삭제할 연락처의 이름(Name)을 한 번 더 입력받습니다.
# 삭제할 연락처의 이름을 입력받았다면 연락처 리스트와 삭제할 이름을 delete_contact 함수의 인자로 전달하면 해당 함수를 통해 연락처가 삭제됩니다.
# def run():
#     contact_list = []
#     while 1:
#         menu = print_menu()
#         if menu == 1:
#             contact = set_contact()
#             contact_list.append(contact)
#         elif menu == 2:
#             print_contact(contact_list)
#         elif menu == 3:
#             name = input("Name: ")
#             delete_contact(contact_list, name)
#         elif menu == 4:
#             break
# 지금까지 작성한 주소록 프로젝트의 전체 소스코드는 예제 8.2와 같습니다. 여러분이 입력한 코드와 틀린 부분이 없는 확인하고 틀린 부분이 없다면
# 작성한 프로그램을 실행해 보기 바랍니다.
# 프로그램이 정상적으로 동작하는지 확인하기 위해 여러 명의 연락처를 입력해 보기 바랍니다. 그리고 그중 일부 연락처를 삭제한 후 연락처도 
# 출력해 보기 바랍니다. 어떤가요? 지금까지 배운 파이썬의 기본 문법을 활용하고 프로그램을 단계별로 나눠서 작성하니 조금 복잡해 보이는 프로그램도
# 어렵지 않게 작성할 수 있지요?
''' class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)
def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            break
if __name__ == "__main__":
    run() '''

# [8.3 주소록 프로젝트의 기능 향상]
# 이번 절에서는 8.2절에서 작성한 연락처 관리 프로그램에 저장 기능을 추가해 보겠습니다. 지금까지 작성한 주소록 프로그램은 프로그램을 종료하면 
# 입력된 모든 연락처가 사라집니다. 이는 입력받은 연락처가 Contact 클래스의 인스턴스로서 메모리에 할당됐다가 프로그램이 종료되면 메모리에 있는 
# 모든 변수가 삭제되기 때문입니다.
# 이러한 문제를 해결하려면 어떻게 해야 할까요? 가장 간단한 방법은 프로그램이 종료되는 시점을 기준으로 유효한 연락처의 정보를 모두 파일로 저장하는
# 것입니다. 파일 입출력은 7장에서 살펴봤기 때문에 바로 해당 기능을 추가해 보겠습니다.
# 8.2절에서 구현한 메인 메뉴의 기능과 달리 파일 출력 기능은 메인 메뉴를 통해 제공되는 기능이 아닙니다. 단지 프로그램이 종료될 때 종료 시점에 
# 유효한 데이터를 파일로 출력하면 됩니다. 반대로 프로그램이 실행될 때는 기존에 저장된 연락처를 불러와야(Load) 합니다.

# [1) 연락처 저장 함수 작성하기]
# 맨 먼저 작성해볼 함수는 프로그램이 종료될 때 유효한 연락처 정보를 파일로 저장하는 store_contact라는 함수입니다. 이 함수는 contact_list라는 
# 리스트를 입력받은 후 해당 리스트에 있는 Contact 인스턴스를 순회하면서 데이터를 파일로 저장합니다.
# def store_contact(contact_list):
#     f = open("contact_db.txt", "wt")
#     for contact in contact_list:
#         f.write(contact.name + '\n')
#         f.write(contact.phone_number + '\n')
#         f.write(contact.e_mail + '\n')
#         f.write(contact.addr + '\n')
#     f.close()
# store_contact 함수는 함수가 호출될 때 먼저 'contact_db.txt'라는 이름의 텍스트 파일을 'wt' 모드로 엽니다. 그런 다음 contact_list를 순회하면서
# 각 인스턴스의 정보를 write 함수를 통해 출력합니다. 이때 출력되는 각 정보가 파일에서 각 라인 단위로 저장되도록 '\n'을 사용했습니다. 
# contact_list의 모든 데이터를 파일로 출력했다면 f.close()를 통해 파일을 닫습니다.
# 파일로 저장하는 기능은 프로그램이 종료될 때 호출하면 되므로 기존에 작성된 run 함수를 수정합니다.
# def run():
#     contact_list = []
#     while 1:
#         menu = print_menu()
#         if menu == 1:
#             contact = set_contact()
#             contact_list.append(contact)
#         elif menu == 2:
#             print_contact(contact_list)
#         elif menu == 3:
#             name = input("Name: ")
#             delete_contact(contact_list, name)
#         elif menu == 4:
#             store_contact(contact_list)
#             break
# 수정된 프로그램을 실행한 후 그림 8.28과 같이 연락처를 하나 입력하고 프로그램을 종료해 봅시다.

# [2) 연락처 불러들이기]
# 앞서 프로그램이 종료될 때 유효한 연락처를 파일로 저장하는 기능을 구현했습니다. 이번에는 이와 반대로 이전에 파일로 저장돼 있던 연락처 정보를
# 프로그램이 시작될 때 불러들이는 기능을 구현해 보겠습니다.
# 파일로부터 연락처를 로드하는 함수의 이름은 load_contact입니다. 이 함수 역시 contact_list를 인자로 받으며, 함수 내부에서 'contact_db.txt' 
# 파일을 열어서 해당 파일을 라인 단위로 저장된 이름, 전화번호, 이메일, 주소로 읽어 들여 Contact 클래스의 인스턴스를 생성합니다. 그런 다음 생성한
# 인스턴스를 contact_list에 추가합니다.
# def load_contact(contact_list):
#     f = open("contact_db.txt", "rt")
#     lines = f.readlines()
#     num = len(lines) / 4
#     num = int(num)
#     for i in range(num):
#         name = lines[4*i].rstrip('\n')
#         phone = lines[4*i+1].rstrip('\n')
#         email = lines[4*i+2].rstrip('\n')
#         addr = lines[4*i+3].rstrip('\n')
#         contact = Contact(name, phone, email, addr)
#         contact_list.append(contact)
#     f.close()
# load_contact 함수는 먼저 readlines 함수를 이용해 파일에 있는 모든 데이터를 읽습니다. 연락처 하나당 4줄의 데이터가 존재하므로 파일에서 읽어 들인
# 전체 라인 수를 4로 나누어 몇 개의 데이터가 존재하는지 확인합니다. 나눗셈 연산을 수행하면 num 값이 실수가 되는데, 이 값을 int 내장 함수를 사용해
# 정수형으로 형변환합니다.
# for 문에서는 num의 개수만큼 루프를 돌면서 lines 리스트에 저장된 데이터를 읽어 들여 Contact 클래스의 인스턴스를 생성하고 생성한 인스턴스를
# contact_list에 추가합니다.
# 앞서 설명한 것처럼 파일로 저장된 연락처를 불러오는 것은 연락처 관리 프로그램이 실행될 때 이뤄져야 합니다. 따라서 다음과 같이 run 함수가 시작하는
# 부분에서 load_contact 함수를 호출하면 됩니다.
# def run():
#     contact_list = []
#     load_contact(contact_list)
#     while 1:
#         menu = print_menu()
#         if menu == 1:
#             contact = set_contact()
#             contact_list.append(contact)
#         elif menu == 2:
#             print_contact(contact_list)
#         elif menu == 3:
#             name = input("Name: ")
#             delete_contact(contact_list, name)
#         elif menu == 4:
#             store_contact(contact_list)
#             break
''' class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    def print_info(self):
        print("Name : {}\t".format(self.name),end='')
        print("Phone Number : {}\t".format(self.phone_number),end='')
        print("E-mail : {}\t".format(self.e_mail),end='')
        print("Address : {}\t\n".format(self.addr),end='')
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]
def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)
    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()
def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = int(input("메뉴선택: "))
    return menu
def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
            store_contact(contact_list)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
            store_contact(contact_list)
        elif menu == 4:
            break
        else :
            continue
if __name__ == "__main__":
    run() '''


# [09. 파이썬과 COM (revision)]
# 1부 ‘파이썬 프로그래밍’을 통해 파이썬의 기본 문법을 배웠습니다. 특히 8장에서는 파이썬을 이용해 간단한 프로그램도 직접 만들어봤습니다. 그러나
# 지금까지 배운 내용은 궁극적으로 만들어야 할 알고리즘 트레이딩과는 다소 거리가 있었습니다.
# 2부 ‘증권사 API 기초’에서는 알고리즘 트레이딩 시스템의 기본이 되는 증권사 API(Application Programming Interface)를 배우겠습니다. 여기서 API란
# 파이썬의 함수나 메서드와 같은 것입니다. 증권사가 제공하는 API를 이용하면 시세 정보를 얻거나 프로그램을 통한 매매와 같은 기본 동작을 수행할 수 
# 있습니다.
# 그러나 여기에도 한 가지 문제가 있습니다. 국내 증권사에서 제공하는 API를 이용하면 프로그램을 쉽게 작성할 수 있는 것은 맞지만 국내 증권사의 API는
# 파이썬으로 구현돼 있지 않습니다. 파이썬으로 작성된 함수 또는 클래스라면 앞서 배운 내용을 바탕으로 어떻게 이용해볼 수는 있을 것 같은데, 다른 
# 프로그래밍 언어로 작성된 함수를 파이썬에서 어떻게 호출할 수 있을까요?
# 이 질문의 답이 될 수 있는 기술이 바로 이번 장에서 다룰 마이크로소프트의 COM(Component Object Model)입니다. 이번 장을 통해 COM에 대한 간단히 
# 알아보고 파이썬에서 COM을 사용하는 방법을 배워봅시다.

# [9.1 COM과 파이썬]
# COM이란 마이크로소프트에서 개발한 기술입니다. Component Object Model이라는 용어가 의미하듯이 여러 컴포넌트 객체를 이용해 프로그램을 개발하는 
# 모델을 의미합니다. 컨테이너를 이용해 집을 지으면 쉽고 빨리 집을 지을 수 있는 것처럼 프로그램을 개발할 때도 특정 기능을 위해 개발된 
# Component Object를 이용하면 프로그램을 더 쉽고 빠르게 개발할 수 있습니다.
# 참고로 컴포넌트 객체란 파이썬으로 치면 클래스로부터 만들어지는 객체와 같은 것이라 이해하면 됩니다. 여기까지만 본다면 COM이라는 기술의 개념은
# 기존의 객체지향 프로그래밍과 크게 다르지 않습니다. 그러나 COM은 여기서 더 나아가 프로그래밍 언어와 상관없이 개발된 객체를 사용할 수 있게
# 해줍니다. 예를 들어, COM을 이용하면 C++ 같은 프로그래밍 언어로 개발된 객체도 파이썬에서 사용할 수 있게 됩니다.
# 벌써 클래스, 객체, 인스턴스라는 용어가 기억이 나지 않는 분들을 위해 간단한 예를 통해 설명해 드리겠습니다. 대신증권은 C/C++로 구현된 CpStockCode
# 클래스를 제공하는데 이 클래스와 비슷한 기능을 제공하는 클래스를 파이썬으로 구현해 보겠습니다. 참고로 대신증권에서 실제로 제공하는 API는 10장에서
# 좀 더 자세히 다룰 예정입니다.
# class CpStockCode:
#     def __init__(self):
#         self.stocks = {'유한양행':'A000100'}
#     def GetCount(self):
#         return len(self.stocks)
#     def NameToCode(self, name):
#         return self.stocks[name]
# CpStockCode 클래스는 생성자(__init__)와 GetCount, NameToCode라는 메서드를 갖고 있습니다. 여기서 GetCount 메서드는 주식 종목수를 리턴하는
# 메서드이고, NameToCode 메서드는 종목명을 입력하면 해당 종목에 대한 종목 코드를 리턴하는 메서드입니다.
# 참고로 그림 9.1과 같이 KRX 웹페이지(www.krx.co.kr)에서 제공하는 주식 종목 검색기에서 종목명을 입력하면 종목코드를 확인할 수 있습니다. 
# 이와 비슷하게 증권사의 API에도 종목명을 입력하면 종목 코드를 반환하는 메서드가 있습니다. 여러분은 이러한 API를 프로그램 내에서 호출함으로써
# 종목 코드를 프로그램 내에서도 쉽게 얻을 수 있습니다.
# 6장에서 클래스를 정의하는 것은 붕어빵을 만드는 과정에서 붕어빵 틀을 만드는 것과 비슷하다고 설명했습니다. 붕어빵 틀에 반죽을 부은 후 붕어빵을 
# 굽는 것처럼 여러분은 클래스(붕어빵 틀)를 이용해 인스턴스(붕어빵)를 만들 수 있었습니다.
# instCpStockCode = CpStockCode()
# 위 코드는 CpStockCode 클래스를 이용해 instCpStockCode 객체를 생성한 예입니다. 즉, instCpStockCode 객체는 CpStockCode 클래스의 인스턴스입니다.
# 참고로 객체와 인스턴스라는 용어는 같은 의미이기 때문에 혼용하더라도 큰 무리는 없습니다. 다만, instCpStockCode와 같이 클래스를 통해 생성된 
# 인스턴스 자체를 지칭할 때는 ‘무슨 무슨 객체’라는 표 현을 주로 사용합니다. 이와 달리 ‘instCpStockCode 객체는 CpStockCode 클래스의 인스턴스’라는
# 표현에서처럼 객체가 어떤 클래스로부터 생성된 것인지를 의도할 때는 인스턴스라는 용어를 사용합니다.
# 객체와 인스턴스에 대한 차이는 이 정도로 설명하기로 하고 instCpStockCode 객체를 사용해 GetCount와 NameToCode 메서드를 호출해 보겠습니다.
# GetCount 메서드는 self 외에는 인자가 없으므로 호출할 때 인자를 전달하지 않아도 됩니다. NametoCode에는 종목 코드를 확인하고자 하는 종목의
# 종목명을 입력하면 됩니다. 참고로 NameToCode 메서드는 현재 ‘유한양행’이라는 종목에 대해서만 정상적으로 종목 코드를 리턴하도록 구현돼 있습니다.
# print(instCpStockCode.GetCount())
# print(instCpStockCode.NameToCode('유한양행'))
# 앞서 파이썬으로 구현된 CpStockCode 클래스에 대한 인스턴스를 생성할 때는 단순히 'instCpStockCode = CpStockCode()'와 같이 클래스 이름에 ()를
# 붙였습니다. 그러나 파이썬이 아닌 다른 프로그래밍 언어로 구현된 클래스에 대한 인스턴스는 파이썬에서 어떻게 생성할 수 있을까요?
# 파이썬에서 다른 프로그래밍 언어로 작성된 COM 객체를 생성하려면 win32com.client라는 모듈의 Dispatch 메서드를 사용하면 됩니다. 예를 들어, 
# 마이크로소프트의 인터넷 익스플로러에 대한 객체를 생성하려면 다음과 같이 구현하면 됩니다.
# import win32com.client
# explore = win32com.client.Dispatch("InternetExplorer.Application")
# explore.Visible = True
# 먼저 win32com.client라는 모듈을 사용하기 위해 모듈을 임포트(import)합니다. 그리고 win32com.client라는 모듈 내의 Dispatch 함수를 호출하는데,
# 이때 함수의 인자로 "InternetExplorer.Application"이라는 문자열을 사용했습니다. Dispatch 함수가 호출되면 객체가 생성되는데 explore라는 변수가
# 그림 9.2와 같이 생성된 COM 객체를 바인딩합니다. 
# COM 객체가 생성됐으니 COM 객체의 메서드를 호출하거나 속성을 변경할 수 있습니다. 'explore.Visible = True'는 Visible이라는 속성의 값을 True로
# 변경한 것입니다. 이 속성값을 True로 변경하면 그림 9.3과 같이 화면에 익스플로러가 나타납니다.
# 어떤가요? 마이크로소프트의 COM이라는 기술을 사용해 인터넷 익스플로러를 파이썬 코드에서도 실행할 수 있다니 신기하지 않습니까? 컴퓨터에 
# 마이크로소프트 워드가 설치된 분들은 다음 코드도 실행해보기 바랍니다.
# win32com은 pywin32 이라고도 하며, 윈도우 상에서 Python을 이용하여 ActiveX 함수를 호출할 수 있도록 도와주는 역할을 한다. 
# COM(Component Object Model)은 마이크로소프트에서 만들었으며, 다른 언어들을 python으로 변환해주는 것이라 생각하면 된다. 
# 파이썬에서 다른 프로그래밍 언어로 작성된 COM 객체를 생성하려면 win32com.client라는 모듈의 Dispatch 메소드를 사용하면 된다.
# 설치 : python -m pip install pywin32
''' import win32com.client
explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True
import win32com.client
word = win32com.client.Dispatch("Word.Application")
word.Visible = True '''

# [9.2 파이썬으로 엑셀 다루기]
# 9.1절에서는 파이썬에서 COM 객체를 생성하는 방법과 생성된 객체를 통해 메서드를 호출하거나 속성값을 변경하는 법을 배웠습니다. 이번 절에서는
# 알고리즘 트레이딩을 위한 도구로 많이 사용되는 마이크로소프트 엑셀을 파이썬에서 다뤄보겠습니다.
# 앞서 워드나 인터넷 익스플로러에 대한 COM 객체를 생성한 것과 마찬가지로 엑셀에 대한 COM 객체를 생성해보기 바랍니다. 물론 다음 코드가 정상적으로
# 실행되려면 PC에 마이크로소프트 엑셀이 미리 설치돼 있어야 합니다.
# import win32com.client
# excel = win32com.client.Dispatch("Excel.Application")
# 엑셀도 워드나 익스플로러와 마찬가지로 Visible이라는 이름의 속성이 있습니다. 다음과 같이 Visible 속성의 값을 True로 변경하면 화면에 엑셀이
# 나타납니다. 사실 Dispatch 함수를 호출해서 Excel.Application에 대한 인스턴스를 생성했을 때부터 엑셀은 이미 실행돼 있었습니다. 다만 화면에 
# 보이지는 않는 상태였을 뿐입니다.
# import win32com.client
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# 엑셀이 화면에 나타났으니 이제 엑셀에 글자를 출력해 봅시다. 아마도 엑셀을 사용할 때 항상 Worksheet에서부터 시작했을 것입니다. 
# 엑셀에는 여러 개의 Worksheet를 포함하는 상위 개념으로 Workbook이 있습니다. 즉, 엑셀 프로그램을 실행하면 Workbook이 자동으로 생성되고
# 'Sheet1'이라는 이름의 Worksheet가 자동으로 생성됩니다.
# COM을 사용해 파이썬 코드로 엑셀을 직접 컨트롤할 때도 Workbook과 Worksheet의 관계를 고려해야 합니다. 먼저 Workbook을 추가한 후 해당 Workbook에서
# 'Sheet1'이라는 Worksheet를 선택합니다.
# import win32com.client
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# 위 코드를 실행하면 그림 9.6과 같이 우리가 평상시에 사용하는 엑셀의 ‘새 통합 문서’ 상태가 됩니다.
# 엑셀의 Worksheet에는 셀(Cell)이 있는데, 각 셀은 행과 열의 인덱스 값을 통해 구분됩니다. Worksheet의 특정 셀에 값을 입력하려면 Cells 속성을 
# 사용하면 됩니다. Cells라는 키워드 다음에 행과 열에 대한 인덱스 값을 지정해 특정 셀에 접근할 수 있습니다.
# 예를 들어, 다음 코드에서 'Cells(1, 1)'이라는 표현은 첫 번째 행, 첫 번째 열에 해당하는 셀을 의미합니다. 즉, 그림 9.6의 Sheet1에서 A1 셀에 
# 해당합니다. 셀이 선택되면 셀의 Value 속성에 'hello world'를 입력합니다.
# import win32com.client
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# ws.Cells(1, 1).Value = "hello world"
# 위 코드를 실행하면 그림 9.7과 같이 'Sheet 1'의 A1 Cell에 'hello world'라는 문자열이 입력된 것을 확인할 수 있습니다.
# 엑셀에 정상적으로 데이터가 입력됐으니 해당 파일을 하드디스크에 저장하고 프로그램을 종료해 봅시다. 엑셀 프로그램 자체에도 
# [다른 이름으로 저장]이라는 저장 메뉴가 있듯이 엑셀 COM 객체에도 SaveAs라는 메서드가 있습니다. 다음과 같이 SaveAs 메서드에 파일을 저장할
# 경로를 인자로 전달하면 해당 경로에 엑셀 파일이 저장됩니다. SaveAs 메서드를 호출해 파일로 저장했다면 Quit 메서드를 호출해 엑셀을 종료합니다.
# import win32com.client
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# ws.Cells(1, 1).Value = "hello world"
# wb.SaveAs('c:\\Users\\Jason\\Desktop\\test.xlsx')
# excel.Quit()
# 위 코드를 실행하면 그림 9.8과 같이 윈도우의 바탕 화면에 엑셀 파일이 저장됩니다. 참고로 SaveAs 함수의 인자로 입력되는 저장 경로는 환경에 맞춰
# 적절히 변경해야 합니다.
# 이처럼 파이썬에서 COM 기술을 이용하면 엑셀 프로그램을 직접 실행할 필요 없이 엑셀 실행, 데이터 입력, 저장 및 종료를 모두 프로그램 내에서 처리할
# 수 있습니다. 평상시에도 엑셀로 작업을 많이 한다면 파이썬을 이용해 자동으로 엑셀 문서를 만드는 프로그램을 만들어 보기 바랍니다.

# [1) 엑셀 파일 읽기]
# 이번에는 하드디스크에 이미 존재하는 엑셀 파일로부터 데이터를 읽어 오는 파이썬 프로그램을 작성해보겠습니다. 프로그램에서 사용할 샘플 엑셀
# 파일을 만들기 위해 그림 9.9와 같이 엑셀을 실행한 후 A1 셀에 python을 입력합니다.
# 엑셀 메뉴에서 [파일] → [다른 이름으로 저장]을 선택해 윈도우의 바탕 화면에 input.xlsx라는 이름으로 파일을 저장합니다.
# 파이썬에서 하드디스크에 있는 엑셀 파일을 읽는 것도 앞서 엑셀 파일을 쓰는 것과 비슷합니다. 다만 Workbook과 Worksheet가 이미 존재하기 
# 때문에 기존에 있는 것 중 선택해서 사용해야 합니다. 먼저 다음 코드를 실행해 보기 바랍니다. Open 함수에 전달하는 인자는 윈도우 바탕 화면의
# 경로 및 저장한 파일의 이름에 맞춰 적절히 수정합니다.
# import win32com.client
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# wb = excel.Workbooks.Open('C:\\Users\\Jason\\Desktop\\input.xlsx')
# ws = wb.ActiveSheet
# print(ws.Cells(1,1).Value)
# excel.Quit()
# 위 코드에서 Open 함수가 호출되면 바로 Workbook 객체를 얻는 것을 확인할 수 있습니다. Workbook 객체를 통해 다시 Worksheet 객체를 얻을 수 있습니다.
# 이때 Worksheet 이름('Sheet1)을 사용해 여러 Worksheet 중 하나를 선택할 수도 있고, 위 코드와 현재 Active 상태인 Worksheet를 선택할 수도 있습니다.
# Worksheet를 얻었다면 Worksheet를 통해 해당 Worksheet에 있는 셀에 접근해서 저장된 데이터 값을 읽어올 수 있습니다.

# [2) 셀에 컬러 입히기]
# 이번에는 엑셀 Worksheet에서 특정 셀의 색상을 변경해 보겠습니다. 엑셀 COM 객체에는 엑셀 프로그램에서 우리가 사용했던 기능이 거의 그대로 메서드나
# 속성 형태로 제공됩니다. 먼저 앞에서 사용한 input.xlsx 파일을 COM 객체를 통해 읽어 봅시다.
# import win32com.client
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# wb = excel.Workbooks.Open('C:\\Users\\Jason\\Desktop\\input.xlsx')
# ws = wb.ActiveSheet
# B1 셀과 C1 셀에 'is'와 'good'이라는 문자열을 출력해 봅시다. 이를 위해 다음과 같이 Cells와 Range를 이용했습니다. 그리고 C1 셀의 색상을 
# 변경하기 위해 Interior 객체의 ColorIndex 속성값을 변경했습니다.
# ws.Cells(1,2).Value = "is"
# ws.Range("C1").Value = "good"
# ws.Range("C1").Interior.ColorIndex = 10
# 지금까지 작성한 코드를 실행하면 그림 9.10과 같이 B1과 C1 셀에 데이터가 입력되고 C1 셀의 색상이 변경된 것을 확인할 수 있습니다.
# 참고로 ColorIndex 속성은 0~56 범위의 값을 가질 수 있으며, 숫자별로 색상이 정해져 있습니다(자세한 색상 값은 마이크로소프트에서 제공하는
# MSDN1을 참고합니다). 저 또한 이러한 정보는 그림 9.11과 같이 그때그때 구글 검색을 통해 찾습니다.
# 앞서 Worksheet의 셀을 선택할 때 Cells와 Range라는 속성을 각각 이용했는데, 둘 다 셀을 선택하는데 사용됩니다. 다만 Range 속성은 이름 자체가 
# 의미하는 것처럼 여러 셀을 선택할 때 주로 사용합니다. 예를 들어, A2:C2 범위의 셀을 노란색으로 변경하려면 다음과 같이 작성하면 됩니다.
# ws.Range("A2:C2").Interior.ColorIndex = 27
# 지금까지 COM을 이용해 마이크로소프트 인터넷 익스플로러, 워드, 엑셀 등을 조작해 보았습니다. 이를 통해 COM을 이용하면 다른 프로그래밍 언어로 
# 작성된 객체도 쉽게 사용할 수 있음을 확인했습니다. 국내 증권사 API도 COM을 통해 지금까지 설명한 것과 유사한 방식으로 사용할 수 있습니다.