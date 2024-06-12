A = list(input().upper())
B = list(set(A))
index_list = []

for i in range(len(B)):
    count_B = A.count(B[i])
    index_list.append(count_B)
index_list_count = index_list.count(max(index_list))

if index_list_count > 1:
    print("?")
else:
    index_list_index = index_list.index(max(index_list))
    print(B[index_list_index])