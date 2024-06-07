def solution(sizes):
    answer = 0
    horizontal_size = []
    vertical_size = []
    for x in sizes:
        if x[0] > x[1]:
            horizontal_size.append(x[0])
            vertical_size.append(x[1])
        else: 
            horizontal_size.append(x[1])
            vertical_size.append(x[0])
        a = max(horizontal_size)
        b = max(vertical_size)
        answer = a*b
    return answer