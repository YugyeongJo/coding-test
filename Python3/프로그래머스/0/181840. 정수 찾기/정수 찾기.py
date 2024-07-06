def solution(num_list, n):
    answer = 0
    for x in num_list:
        if n == x:
            answer = 1
            break
        else: 
            answer = 0
    return answer