count = int(input())

# num = input().split()
# num_int = map(int, num)
a = list(map(int, input().split()))

same = int(input())

result = 0
for i in range(count):
    if a[i] == same:
        result += 1

print(result)