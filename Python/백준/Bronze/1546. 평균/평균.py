N = int(input())

score = [int(x) for x in input().split()]
pass
max = max(score)
for i in range(N):
    score[i] = score[i]/max*100

average = sum(score)/N
    
print(average)