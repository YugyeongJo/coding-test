def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        start = parts[i][0]
        end = parts[i][-1]
        answer += my_strings[i][start:end+1]
    return answer
