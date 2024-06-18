def croatia_len():
    a = input()
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for i in croatia:
        a = a.replace(i, '*')
    
    answer = len(a)
    return answer

print(croatia_len())