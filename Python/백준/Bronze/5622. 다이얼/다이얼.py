A = list(input())
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num = 0

def dial(A, alphabet, num):
    for i in range(len(A)):
        for j in alphabet:
            if A[i] in j:
                num += alphabet.index(j)+3
    return num

answer = dial(A, alphabet, num)
print(answer)
pass