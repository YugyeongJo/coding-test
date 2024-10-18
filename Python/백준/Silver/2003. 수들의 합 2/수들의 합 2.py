import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = list(map(int, input().split()))

s = e = 0
tmp = ans = 0

while True:
    if tmp < M:
        if e == N:
            break
        tmp += score[e]
        e += 1
    elif tmp > M:
        tmp -= score[s]
        s += 1
    else:
        ans += 1
        tmp -= score[s]
        s += 1

print(ans)