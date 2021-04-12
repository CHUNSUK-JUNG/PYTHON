import turtle as t

n=int(t.textinput("반복 회수","반복 회수를 입력하세요."))
s=t.textinput("마우스 모양", "모양을 입력하세요.(arrow, turtle, circle, square, triangle, classic)") #마우스 모양을 입력하여, 변수 s에 문자로 할당
w=int(t.textinput("선의 두깨", "선의 두께를 입력하세요.(0-10)")) #선의 두께를 입력하여, 변수 w에 정수로 할당
c=t.textinput("선의 색상", "선의 색상을 입력하세요.(black, white, red, purple, blue, green, yellow, orange 등)") #선의 색상을 입력하여, 변수 c에 문자로 할당
sp=int(t.textinput("그리기 속도", "그리는 속도를 입력하세요.(0-10)")) #그리는 속도를 입력하여, 변수 sp에 정수로 할당 
t.shape(s) #터틀의 모양을 s에 입력한 값으로 설정 
t.width(w) #선의 두께를 ()안의 숫자 크기로 설정
t.color(c) #선의 색상을 ()안의 영문으로 설정 
t.speed(sp) #그리기 속도를 ()안의 숫자 크기로 설정

for i in range(n):
    t.fd(i)
    t.rt(91)

t.mainloop()