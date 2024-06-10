num, standard = map(int, input().split())

a = list(map(int, input().split()))
b = []
for i in range(num):
    if standard > a[i]:
        b.append(a[i])
print(*b)