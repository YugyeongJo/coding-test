A = input()
B = input()

def divide(B):
    B = list(B)
    return B

list_B = divide(B)
def multiply(a, b):
        a = int(a)
        b = int(b)
        result = a * b
        print(result)
        return 0 
    
multiply(A, list_B[2])
multiply(A, list_B[1])
multiply(A, list_B[0])
multiply(A, B)