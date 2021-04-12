import turtle #모듈 불러오기
t=turtle.Turtle() #터틀 윈도우 생성

s=turtle.textinput("마우스 모양", "모양을 입력하세요.(arrow, turtle, circle, square, triangle, classic)") #마우스 모양을 입력하여, 변수 s에 문자로 할당
w=int(turtle.textinput("선의 두깨", "선의 두께를 입력하세요.(0 이상)")) #선의 두께를 입력하여, 변수 w에 정수로 할당
c=turtle.textinput("선의 색상", "선의 색상을 입력하세요.(black, white, red, purple, blue, green, yellow, orange 등)") #선의 색상을 입력하여, 변수 c에 문자로 할당
sp=int(turtle.textinput("그리기 속도", "그리는 속도를 입력하세요.(0 이상)")) #그리는 속도를 입력하여, 변수 sp에 정수로 할당
t.shape(s) #터틀의 모양을 s에 입력한 값으로 설정 
t.width(w) #선의 두께를 ()안의 숫자 크기로 설정
t.color(c) #선의 색상을 ()안의 영문으로 설정 
t.speed(sp) #그리기 속도를 ()안의 숫자 크기로 설정

color_list=["yellow","red","blue","green"] #색상을 color_list 변수에 list로 저장
r=int(turtle.textinput("원의 반지름","원의 반지름을 입력하세요.")) #원의 반지름을 입력하여, 변수 r에 정수로 할당
m=int(turtle.textinput("원의 이동","원의 이동 거리를 입력하세요.")) #원의 이동 거리를 입력하여, 변수 m에 정수로 할당

for i in range(len(color_list)): #color_list의 list 길이 만큼 반복
    t.fillcolor(color_list[i]) #면 색을 color_list의 i번째로 선택
    t.begin_fill() #면 채우기 시작
    t.circle(r) #입력받은 r을 반지름으로 하는 원 그리기
    t.end_fill() #면 채우기 종료
    t.up() #펜 들기
    t.fd(m) #입력받은 변수 m만큼 앞쪽으로 이동
    t.down() #펜 내리기
