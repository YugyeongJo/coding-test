def solution(my_string, is_suffix):
    for i in range(len(is_suffix), 0, -1):
        try :
            if my_string[-i] == is_suffix[-i]:
                answer = 1
            else :
                answer = 0
                break
        except :
            answer = 0
            break

    return answer