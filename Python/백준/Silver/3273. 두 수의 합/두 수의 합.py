N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())

start = 0
end = N-1
count = 0

while start < end:
    add = nums[start] + nums[end]
    
    if add == M:
        count += 1
        start += 1
        end -= 1
    elif add < M:
        start += 1
    else:
        end -= 1
        
print(count)