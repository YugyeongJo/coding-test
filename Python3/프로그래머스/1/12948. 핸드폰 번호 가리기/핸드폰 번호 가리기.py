def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        if i == len(phone_number)-4:
            answer = answer+phone_number[i]
        elif i == len(phone_number)-3:
            answer = answer+phone_number[i]
        elif i == len(phone_number)-2:
            answer = answer+phone_number[i]
        elif i == len(phone_number)-1:
            answer = answer+phone_number[i]
        else:
            answer = answer+"*"
    return answer