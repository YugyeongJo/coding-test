N, M = map(int, input().split())

basket = list(range(1,N+1))
# print(basket)

for count in range(M):
    a, b = map(int, input().split())
    c = basket[a-1]
    d = basket[b-1]
    basket[a-1] = d
    basket[b-1] = c
    
print(*basket)