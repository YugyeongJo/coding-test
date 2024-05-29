def solution(array):
    answer = []
    A = max(array)
    answer.append(A)
    for i in range(len(array)):
        if array[i] == A:
            num = i
            answer.append(num)
        else:
            pass
    return answer