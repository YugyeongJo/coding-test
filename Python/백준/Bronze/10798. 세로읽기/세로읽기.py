def making_matrix():
    results = []
    length = []
    for i in range(5):
        word = input()
        results.append(word)
        length.append(len(word))
    return results, length

def matrix_print(results, length):
    answer = ''
    for i in range(max(length)):
        for j in range(5):
            if i < length[j]:
                answer += results[j][i]
    return answer
                
results, length = making_matrix()
print(matrix_print(results, length))