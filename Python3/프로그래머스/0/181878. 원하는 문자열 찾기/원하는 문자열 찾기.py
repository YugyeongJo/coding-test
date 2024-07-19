def solution(myString, pat):
    up_myString = myString.upper()
    up_pat = pat.upper()
    
    if up_pat in up_myString:
        return 1
    else:
        return 0