def solution(s):
    s = s.split(" ")
    answer = []

    for x in s:
        non_answer = ''
        for i in range(len(x)):
            if (i+1)%2 != 0:
                upper_str = x[i].upper()
                non_answer = non_answer + upper_str
            else: 
                non_answer = non_answer + x[i].lower()
        answer.append(non_answer)
            
    answer = " ".join(answer)
    return answer