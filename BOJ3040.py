from itertools import combinations

dwarf = []
ans = []
for _ in range(9):
    dwarf.append(int(input()))

for i in combinations(dwarf, 7):
    if sum(i) == 100:
        ans = list(i)
        break

for i in sorted(ans):
    print(i)