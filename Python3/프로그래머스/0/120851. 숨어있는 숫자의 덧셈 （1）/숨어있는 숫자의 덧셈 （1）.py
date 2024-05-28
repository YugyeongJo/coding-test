def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i].isnumeric() == True:
            answer = answer + int(my_string[i])
        else:
            answer = answer
    return answer