def solution(n):
    answer = 0
    x = n**(1/2)
    if int(x) == x:
        return (x+1)**2
    else:
        return -1