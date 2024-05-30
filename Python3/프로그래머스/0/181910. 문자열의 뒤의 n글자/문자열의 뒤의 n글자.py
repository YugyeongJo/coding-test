def solution(my_string, n):
    answer = ''
    for i in range(1, n+1):
        answer = answer+my_string[-i]
    answer = answer[::-1]
    return answer