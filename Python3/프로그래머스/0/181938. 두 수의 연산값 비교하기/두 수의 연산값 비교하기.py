def solution(a, b):
    add = int(str(a) + str(b))
    calculator = 2 * a * b
    if add >= calculator:
        return add
    else:
        return calculator