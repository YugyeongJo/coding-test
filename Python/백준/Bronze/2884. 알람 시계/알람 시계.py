a, b= map(int, input().split())

if b >= 45:
    a = a
    b = b-45
else :
    a = a-1
    if a < 0 :
        a = 24-1
    b = 60-(45-b)

print("{} {}".format(a, b))