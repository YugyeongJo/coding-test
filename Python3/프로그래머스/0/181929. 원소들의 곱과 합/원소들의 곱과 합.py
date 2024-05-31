def solution(num_list):
    multiple = 1
    add = 0
    for i in range(len(num_list)):
        multiple = multiple*num_list[i]
        add = add+num_list[i]
    if multiple < add**2:
        answer = 1
    else: 
        answer = 0
    return answer