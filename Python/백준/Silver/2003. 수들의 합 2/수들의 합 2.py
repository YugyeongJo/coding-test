import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = list(map(int, input().split()))

start, end = 0, 0
current_sum = 0
ans = 0

while end < N:
    current_sum += score[end]
    end += 1
    
    while current_sum > M and start < end:
        current_sum -= score[start]
        start += 1
        
    if current_sum == M:
        ans += 1
    
print(ans)