def solution(d, budget):
    answer = 0
    d.sort()
    for x in d:
        if budget >= x:
            budget = budget - x
            answer = answer + 1
        else:
            pass
    return answer