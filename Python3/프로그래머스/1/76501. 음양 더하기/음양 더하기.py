
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            result = absolutes[i]
            answer = answer+result
        else : 
            result = -absolutes[i]
            answer = answer+result
    return answer