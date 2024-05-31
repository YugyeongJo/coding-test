def solution(s):
    p, y = 0, 0
    s = s.upper()
    for c in s:
        if c == 'P':
            p = p+1
        elif c == 'Y':
            y = y+1
    return True if p == y else False