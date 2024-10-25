T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
    
for tc in range(T):
    R, C = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(R)]

    score = 0

    for r in range(R):
        for c in range(C):
            cur_score = matrix[r][c]
            
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    cur_score += matrix[nr][nc]
            
            if cur_score > score:
                score = cur_score
                
    print(f"#{tc+1} {score}")