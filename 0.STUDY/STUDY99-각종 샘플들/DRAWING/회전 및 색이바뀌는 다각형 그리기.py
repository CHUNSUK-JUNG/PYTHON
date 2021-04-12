import turtle
t=turtle.Turtle()

s=turtle.textinput("마우스 모양", "모양을 입력하세요.(arrow, turtle, circle, square, triangle, classic)") #마우스 모양을 입력하여, 변수 s에 문자로 할당
w=int(turtle.textinput("선의 두깨", "선의 두께를 입력하세요.(0 이상)")) #선의 두께를 입력하여, 변수 w에 정수로 할당
bc=turtle.textinput("면의 색상", "면의 색상을 입력하세요.(black, white, red, purple, blue, green, yellow, orange 등)") #선의 색상을 입력하여, 변수 bc에 문자로 할당
sp=int(turtle.textinput("그리기 속도", "그리는 속도를 입력하세요.(0 이상)")) #그리는 속도를 입력하여, 변수 sp에 정수로 할당
t.shape(s) #터틀의 모양을 s에 입력한 값으로 설정 
t.width(w) #선의 두께를 ()안의 숫자 크기로 설정
t.speed(sp) #그리기 속도를 ()안의 숫자 크기로 설정
turtle.bgcolor(bc) #면의 색상을 ()안의 영문으로 설정

colors=["red","purple","blue","green","yellow","orange"]
length=10

while length < 500:
    t.fd(length)
    t.pencolor(colors[length%6])
    t.rt(89)
    length +=5
