times = int(input())

for x in range(times):
    count, str = input().split()
    count = int(count)
    str = list(str)
    result = []
    for z in str:
        for i in range(count):
            result.append(z)
            pass
    print(''.join(result))  