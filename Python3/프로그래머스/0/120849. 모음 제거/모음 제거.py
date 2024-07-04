def solution(my_string):
    
    vowels = 'aeiou'
    answer = ''
    
    for my_str in my_string:
        if my_str not in vowels:
            answer += my_str
                
    return answer