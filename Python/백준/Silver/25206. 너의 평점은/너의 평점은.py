rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total_score = 0 # 학점 총합
total_lecture_score = 0 # (학점 * 과목평점) 총합

for i in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        total_score += b * grade[rating.index(c)]
        total_lecture_score += b
        
print(total_score/total_lecture_score)