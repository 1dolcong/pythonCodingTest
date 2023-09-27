import itertools

tri_angle_num = []
s = 0
for i in range(1,45):
    s += i
    tri_angle_num.append(s)

method = list(itertools.combinations_with_replacement(tri_angle_num, 3))
for _ in range(int(input())):
    result = 0
    check_num = int(input())
    for i in range(len(method)):
        if sum(method[i]) == check_num:
            result = 1
            break
    print(result)
