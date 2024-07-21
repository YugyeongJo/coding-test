def solution(n):
    answer = 0
    if n % 2 != 0:
        for x in range(n+1):
            if x % 2 != 0:
                answer += x
            else:
                pass
    if n % 2 == 0:
        for x in range(n+1):
            if x % 2 ==0:
                answer += x**2
            else: 
                pass
    
    return answer