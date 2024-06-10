list_num = []

for i in range(9):
    a = int(input())
    list_num.append(a)
    pass

for i in range(9):
    if max(list_num) == list_num[i]:
        a = i

print(max(list_num))
print(a+1)