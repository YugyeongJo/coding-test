N = int(input())

for star_print in range(1, N+1):
    star = "*"
    printing = star * star_print
    print(str(printing).rjust(N))