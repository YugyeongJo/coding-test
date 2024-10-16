T = int(input())
enter_people = set()

for i in range(T):
    name, status = input().split()
    
    if status == "enter":
        enter_people.add(name)
    else:
        enter_people.remove(name)
    
for people in sorted(enter_people, reverse=True):
    print(people)