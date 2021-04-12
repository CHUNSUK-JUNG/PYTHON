#배수구하기
x, y = map(int,input('숫자 2개를 입력하세요.').split())
if x%y==0 :
    print('%d은 %d의 배수입니다.' % (x,y))
else:
    print('%d은 %d의 배수가 아닙니다.' % (x,y))

a=int(input('숫자 1개를 입력하세요.'))
for i in range(1, a+1) :
    if a % i ==0:
        print('%d는 %d의 약수입니다.' % (i, a))