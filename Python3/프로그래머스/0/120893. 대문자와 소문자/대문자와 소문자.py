def solution(my_string):
    list_variable = []
    for i in range(len(my_string)):
        string = my_string[i]
        if string.isupper() == True:
            result = string.lower()
            list_variable.append(result)
        else:
            result = string.upper()
            list_variable.append(result)
        answer = "".join(list_variable)
    return answer