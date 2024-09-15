def making_matrix():
    matrix = []

    for i in range(9):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def find_max(matrix):
    max_number = 0
    for idx_row, row in enumerate(matrix):
        for idx_col, col in enumerate(row):
            if col >= max_number:
                max_number_row = idx_row + 1
                max_number_col = idx_col + 1
                max_number = col
    return max_number, max_number_row, max_number_col
    
max_num, row, col = find_max(making_matrix())
print(max_num)
print(row, col)