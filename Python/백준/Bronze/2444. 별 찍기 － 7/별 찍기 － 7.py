A = int(input())

blank = " "
star = "*"



def starprint(A, blank, star):
    for i in range(A):
        n = (A-1)-i
        m = 2*(i+1)-1
        printing = (blank*n) + (star*m)
        print(printing)
    for x in range(A):
        l = (2*A-1)-(2*(x+1))
        printing = (blank*(x+1)) + (star*l)
        print(printing)
    return 0 

answer = starprint(A, blank, star)