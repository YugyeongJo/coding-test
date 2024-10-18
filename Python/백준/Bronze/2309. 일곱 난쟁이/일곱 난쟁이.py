from itertools import combinations

people = [int(input()) for _ in range(9)]

for this_case in combinations(people, 7):
    if sum(this_case) == 100:
        for person in sorted(this_case):
            print(person)
        break