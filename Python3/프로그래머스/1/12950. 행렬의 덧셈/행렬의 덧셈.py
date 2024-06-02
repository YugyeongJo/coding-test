def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr1[i])):
            add = arr1[i][j] + arr2[i][j]
            result.append(add)
        answer.append(list(result))

    return answer