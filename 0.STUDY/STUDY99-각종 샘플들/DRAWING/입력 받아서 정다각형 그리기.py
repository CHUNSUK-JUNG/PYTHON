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

n=int(turtle.textinput("정다각형 그리기","몇 각형을 원하시나요?(숫자 3-12입력)")) #n각형 입력하여, 변수 n에 정수로 할당
l=int(turtle.textinput("변의 길이","한변의 길이를 입력하시오.")) #한변의 길이 입력하여, 변수 l에 정수로 할당

for i in range(n): #입력받은 변수 n만큼 반복
    t.fd(l) #입력받은 변수 l길이의 한변 그리기
    t.lt(360/n) #입력받은 변수 n만큼의 각도 회전