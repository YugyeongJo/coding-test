chess = [1, 1, 2, 2, 2, 8]
mine = input().split()
new_mine = []

def chess_func(chess, mine, new_mine):
    for i in range(6):
        result = chess[i] - int(mine[i])
        new_mine.append(result)
    return new_mine

answer = chess_func(chess, mine, new_mine)
print(*answer)