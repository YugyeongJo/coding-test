N, M = map(int, input().split())
nums = list(map(int, input().split()))

cur_sum = sum(nums[:M])
max_sum = cur_sum
    
for i in range(1, N-M+1):
    cur_sum = cur_sum - nums[i-1] + nums[i+M-1]
    max_sum = max(max_sum, cur_sum)
    
print(max_sum)