def solution(numbers):
    
    numbers.sort(reverse=True)
    minus_mul = numbers[0]*numbers[1]
    plus_mul = numbers[-1]*numbers[-2]
    
    if minus_mul > plus_mul:
        answer = minus_mul
    else:
        answer = plus_mul        

    return answer