def solution(hp):
    a = hp//5
    remain = hp%5
    b = remain//3
    remain = remain%3
    c = remain
    answer = a+b+c
    return answer