M, N = map(int, input().split())
basket = []

for i in range(1, M+1):
    basket.append(i)
# print(basket)

for count in range(N):
    i, j = map(int, input().split())
    pass
    basket[i-1:j] = basket[i-1:j][::-1]
    pass
print(*basket)