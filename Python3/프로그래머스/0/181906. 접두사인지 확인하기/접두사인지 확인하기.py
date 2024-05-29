def solution(my_string, is_prefix):
    for i in range(len(is_prefix)):
        try:
            if is_prefix[i] == my_string[i]:
                answer = 1
            else:
                answer = 0
                break
        except:
            answer = 0
            break
    return answer