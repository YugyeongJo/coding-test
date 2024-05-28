def solution(cipher, code):
    list_variable = []
    num = int(len(cipher)/code)
    for i in range(1, num+1):
        result = cipher[(code*i)-1]
        list_variable.append(result)
        answer = "".join(list_variable)
    return answer