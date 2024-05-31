def solution(arr):
    answer = 0
    for x in arr:
        answer = answer+x
    average = answer/len(arr)
    return average