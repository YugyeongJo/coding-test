n = int(input())

def solution(n):
    for i in range(n):
        string = input()
        for j in range(len(string)-1):
            if string[j] == string[j+1]:
                pass
            elif string[j] in string[j+1:]:
                n -= 1
                break  
    return n

print(solution(n))