count = int(input())

def pop(count):        
    for i in range(count):
            str = list(input())
            first_str = str.pop(0)
            try:
                last_str = str.pop(-1)
            except:
                last_str = first_str
            str = first_str+last_str
            print(str)
    return 0

pop(count)