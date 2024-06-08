a, b = map(int, input().split())
c = int(input())

if b+c < 60:
    a=a
    b=b+c
    pass
else :
    a = a+((b+c)//60)
    if a >= 24:
        a = a-24
    else : 
        a=a
    b = (b+c)%60

print("{} {}".format(a,b))