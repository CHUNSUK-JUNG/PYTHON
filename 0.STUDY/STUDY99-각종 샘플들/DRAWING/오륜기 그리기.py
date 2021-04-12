import turtle #모듈 불러오기
t=turtle.Turtle() #터틀 윈도우 생성

s=turtle.textinput("마우스 모양", "모양을 입력하세요.(arrow, turtle, circle, square, triangle, classic)") #마우스 모양을 입력하여, 변수 s에 문자로 할당
w=int(turtle.textinput("선의 두깨", "선의 두께를 입력하세요.(0 이상)")) #선의 두께를 입력하여, 변수 w에 정수로 할당
sp=int(turtle.textinput("그리기 속도", "그리는 속도를 입력하세요.(0 이상)")) #그리는 속도를 입력하여, 변수 sp에 정수로 할당
t.shape(s) #터틀의 모양을 s에 입력한 값으로 설정 
t.width(w) #선의 두께를 ()안의 숫자 크기로 설정
t.speed(sp) #그리기 속도를 ()안의 숫자 크기로 설정

color_list1=["blue","black","red"] #색상을 color_list1 변수에 list로 저장
color_list2=["yellow","green"] #색상을 color_list2 변수에 list로 저장
r=int(turtle.textinput("원의 반지름","원의 반지름을 입력하세요.")) #원의 반지름을 입력하여, 변수 r에 정수로 할당

x=0
y=0 #위치 좌표값 x, y 초기화

for i in range(3): #3회 반복
    t.color(color_list1[i]) #면 색을 color_list1의 i번째로 선택
    t.up() #이동하는 동안 선이 그려지지 않도록 펜을 든다.
    t.goto(x,y) # (x,y) 좌표만큼 이동
    t.down() #이동 후, 선이 그려지도록 펜을 내린다.
    t.circle(r) #입력받은 반지름 r길이의 원 그리기
    x +=70 #x 좌표를 50만큼 이동

x=50
y=-50 #위치 좌표값 x, y 초기화
for j in range(2): #2회 반복
    t.color(color_list2[j]) #면 색을 color_list1의 j번째로 선택
    t.up() #이동하는 동안 선이 그려지지 않도록 펜을 든다.
    t.goto(x,y) # (x,y) 좌표만큼 이동
    t.down() #이동 후, 선이 그려지도록 펜을 내린다.
    t.circle(r) #입력받은 반지름 r길이의 원 그리기
    x +=70 #x 좌표를 50만큼 이동
