def solution(n, numlist):
    answer = []
    for i in range(len(numlist)):
        if numlist[i]%n == 0:
            answer.append(numlist[i])
        else:
            pass
    
    return answer