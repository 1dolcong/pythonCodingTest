import itertools
hat = []
for i in range(9):
    hat.append(int(input()))
# [int(input()) for _ in range(9)]

result = list(itertools.combinations(hat,7))
for i in range(len(result)):
    if sum(result[i]) == 100:
        for j in range(len(result[i])):
            print(result[i][j])
        break

