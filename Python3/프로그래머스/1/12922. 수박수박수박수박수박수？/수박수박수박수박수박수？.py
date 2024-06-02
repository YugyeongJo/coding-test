def solution(n):
    answer = ''
    watermelon = "수박"
    i = n//2
    if n%2 == 0:
        answer = watermelon*i
    else:
        answer = watermelon*i + "수"
        
    return answer