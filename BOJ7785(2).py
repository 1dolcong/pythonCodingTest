import sys

input = sys.stdin.readline
company = {}

for _ in range(int(input())):
    person, in_out = input().split()
    in_out = in_out.rstrip()
    if person in company:
        if in_out == "enter":
            company[person] = True
        else:
            company[person] = False
    else:
        company[person] = True

in_person = []
for person,is_in in company.items():
    if is_in:
        in_person.append(person)

for person in sorted(in_person, reverse = True):
    print(person)
