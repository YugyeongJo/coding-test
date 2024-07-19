def solution(numbers, n):
    answer = 0
    for x in numbers:
        if answer <= n:
            answer += x
        else:
            return answer
    return answer