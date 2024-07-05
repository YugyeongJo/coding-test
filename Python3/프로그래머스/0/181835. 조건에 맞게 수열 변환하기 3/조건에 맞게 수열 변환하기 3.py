def solution(arr, k):
    answer = []
    if k % 2 == 0:
        for x in arr:
            result = x+k
            answer.append(result)
    else:
        for x in arr:
            result = x*k
            answer.append(result)
    return answer