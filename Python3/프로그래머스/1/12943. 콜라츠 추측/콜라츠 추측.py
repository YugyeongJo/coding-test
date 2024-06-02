def solution(num):
    answer = 0
    while True:
        if num%2 == 0:
            num = num/2
            answer = answer+1
            if num == 1:
                break
            elif answer == 500:
                answer = -1
                break
        else:
            if num ==1:
                break
            elif answer == 500:
                answer = -1
                break
            num = num*3+1
            answer = answer+1
    return answer