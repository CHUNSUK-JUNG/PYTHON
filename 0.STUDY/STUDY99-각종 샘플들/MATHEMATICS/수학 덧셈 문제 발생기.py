import random #모듈 불러오기

r=int(input("문제 풀 갯수를 선택하세요."))
a=b=0

for i in range(r):
    x=random.randint(1,100)
    y=random.randint(1,100)
    print(x,"+",y,"=",end=" ")
    answer=int(input())
    if answer == x+y:
        a +=1
        print("정답입니다.")
    else:
        b +=1
        print("정답이 아닙니다.")

print("총 %s문제 중 정답 개수는 %s개, 오답 개수는 %s개 입니다." % (r, a, b) )
