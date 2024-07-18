def solution(myString):
    answer = ''
    for x in myString:
        if x == 'a' or x =='A':
            answer += x.upper()
        else:
            answer += x.lower()
    return answer