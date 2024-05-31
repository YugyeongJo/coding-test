def solution(n):
    answer = []
    n = str(n)
    for x in n:
        answer.append(x)
    answer.sort(reverse=True)
    answer = "".join(answer)
    return int(answer)