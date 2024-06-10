def input_error(str):
    while True:
        try:
            str = input()
            print(str)
        except EOFError:
            break
    return 0

input_error(str)