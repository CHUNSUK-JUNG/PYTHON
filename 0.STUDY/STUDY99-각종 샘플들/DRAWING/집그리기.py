import turtle as t #모듈 불러오기

l=int(t.textinput("변의 길이","한변의 길이를 입력하시오.")) #한변의 길이를 입력하여, 변수 l에 정수로 할당
s=t.textinput("마우스 모양", "모양을 입력하세요.(arrow, turtle, circle, square, triangle, classic)") #마우스 모양을 입력하여, 변수 s에 문자로 할당
w=int(t.textinput("선의 두깨", "선의 두께를 입력하세요.(0-10)")) #선의 두께를 입력하여, 변수 w에 정수로 할당
c=t.textinput("선의 색상", "선의 색상을 입력하세요.(black, white, red, purple, blue, green, yellow, orange 등)") #선의 색상을 입력하여, 변수 c에 문자로 할당
sp=int(t.textinput("그리기 속도", "그리는 속도를 입력하세요.(0-10)")) #그리는 속도를 입력하여, 변수 sp에 정수로 할당
t.shape(s) #터틀의 모양을 s에 입력한 값으로 설정 
t.width(w) #선의 두께를 ()안의 숫자 크기로 설정
t.color(c) #선의 색상을 ()안의 영문으로 설정 
t.speed(sp) #그리기 속도를 ()안의 숫자 크기로 설정

for i in range(4): #정사각형을 그리기 위해 4회 반복
    t.fd(l) #입력받은 변수 l길이의 한변 그리기 (forward=fd,backward=bk,left=lt,right=rt)
    t.rt(360/4) #360/4만큼의 각도 회전

t.rt(-60)
for i in range(2): #정삼각형을 그리기 위해 2회 반복 (한 변은 사각형 그리기에서 이미 그렸음)
    t.fd(l) #입력받은 변수 l길이의 한변 그리기
    t.rt(360/3) #360/3만큼의 각도 회전

t.mainloop()