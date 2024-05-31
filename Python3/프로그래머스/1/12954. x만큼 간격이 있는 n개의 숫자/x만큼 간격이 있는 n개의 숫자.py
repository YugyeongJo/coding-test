def solution(x, n):
    answer = []
    answer.append(x)
    input_x = x
    for i in range(n-1):
        input_x = input_x+x
        answer.append(input_x)
    return answer