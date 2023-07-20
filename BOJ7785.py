import sys

N = int(input())

people = set()
for i in range(N):
    name, behave = str(sys.stdin.readline()).rstrip().split()
    if behave == "enter":
        people.add(name)
    else:
        people.remove(name)

for person in sorted(people, reverse=True):
    print(person)

