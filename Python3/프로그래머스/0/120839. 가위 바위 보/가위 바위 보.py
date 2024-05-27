def solution(rsp):
    answer = []
    for i in range(len(rsp)):
        rsp[i]
        if rsp[i] == "2":
            result = "0"
        elif rsp[i] == "0":
            result = "5"
        else:
            result = "2"
        answer.append(result)
    answer = "".join(answer)
    return answer