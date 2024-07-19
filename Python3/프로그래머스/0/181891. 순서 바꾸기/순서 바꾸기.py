def solution(num_list, n):
    answer01 = []
    answer02 = []
    for i in range(len(num_list)):
        if i < n:
            answer01.append(num_list[i])
        else:
            answer02.append(num_list[i])
    answer = answer02+answer01
    return answer