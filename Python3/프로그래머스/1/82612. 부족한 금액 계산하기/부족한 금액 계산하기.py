def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer = answer + price*i
    if money - answer < 0:
        answer = abs(money - answer)
    else: 
        answer = 0

    return answer