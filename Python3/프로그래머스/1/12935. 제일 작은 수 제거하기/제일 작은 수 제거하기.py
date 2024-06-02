def solution(arr):
    answer = []
    min_num = min(arr)
    for x in arr:
        if x == min_num:
            pass
        else: 
            answer.append(x)
    if answer == []:
        answer = [-1]
        
    return answer