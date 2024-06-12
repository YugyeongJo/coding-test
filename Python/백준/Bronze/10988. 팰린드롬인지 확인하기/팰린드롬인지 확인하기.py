A = list(input())
B = list(reversed(A))


def solution(A, B):
    score = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            score += 1
            
    if score == len(A):
        print("1")
    else : 
        print("0")
    return 0

solution(A, B)