def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        try:
            if arr[i] == arr[i-1]:
                pass
            else: 
                answer.append(arr[i])
        except:
            pass
    return answer