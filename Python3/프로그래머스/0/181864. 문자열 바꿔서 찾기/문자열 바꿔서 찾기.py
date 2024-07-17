def solution(myString, pat):
    answer = ''
    for x in myString:
        if x == "A":
            answer += 'B'
        else :
            answer += "A"
    
    if pat in answer :
        return 1
    else: 
        return 0