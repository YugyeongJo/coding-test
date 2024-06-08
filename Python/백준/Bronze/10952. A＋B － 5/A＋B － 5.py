while True : 
    a,b = map(int, input().split())
    if (a and b) != 0:
        result = a + b
        print(result)
    elif (a and b) == 0:
        break
