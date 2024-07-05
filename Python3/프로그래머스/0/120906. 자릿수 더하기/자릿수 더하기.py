def solution(n):
    n = str(n)
    answer = 0
    for i in range(len(n)):
        str_ = n[i]
        number = int(str_)
        answer = answer + number
    return answer