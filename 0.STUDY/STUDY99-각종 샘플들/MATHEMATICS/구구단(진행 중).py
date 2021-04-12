dan=int(input("계산할 단을 입력하세요.(2-9 입력)")

i=1

for i in range(9):
    print("%s * %s = %s" % (dan, i, dan*i))
    i +=i