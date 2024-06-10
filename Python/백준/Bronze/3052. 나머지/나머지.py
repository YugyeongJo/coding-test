list_b = []
for count in range(10):
    a = int(input())
    b = a%42
    list_b.append(b)
# print(list_b)

list_b = list(set(list_b))

print(len(list_b))