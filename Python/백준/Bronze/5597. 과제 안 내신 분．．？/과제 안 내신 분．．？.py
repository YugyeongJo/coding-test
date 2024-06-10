number = []
for i in range(1, 31):
    number.append(int(i))

student_number = []
for x in range(28):
    submit_student = int(input())
    student_number.append(submit_student)

trash = []
for y in range(30):
    pass
    for z in range(28):
        if number[y] == student_number[z]:
           trash.append(student_number[z]) 

for a in trash:
    number.remove(a)

number.sort()

print(number[0])
print(number[1])