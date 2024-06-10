basket, count = map(int, input().split())
result=[]

for y in range(basket):
    result.append(int("0"))

for i in range(count):
    a, b, c = map(int, input().split())
    for x in range(a-1,b):
        result[x]=c
          
print(*result) 