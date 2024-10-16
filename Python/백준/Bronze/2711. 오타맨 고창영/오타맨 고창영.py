T = int(input())

for _ in range(T):
    idx, text = input().split()
    idx = int(idx)

    print(text[:idx-1], text[idx:], sep='')