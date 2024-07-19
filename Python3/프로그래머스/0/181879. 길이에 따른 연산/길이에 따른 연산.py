def solution(num_list):
    from functools import reduce
    from operator import mul
    
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return reduce(mul, num_list)