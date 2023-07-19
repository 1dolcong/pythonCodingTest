import sys
num = int(sys.stdin.readline().strip())
ps = [str(sys.stdin.readline().strip()) for _ in range(num)]
ans = ["YES"] * num
for i in range(len(ps)):
    stack = []
    for word in ps[i]:
        if word == '(':
            stack.append(word)
        else:#word == ')"
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    ans[i] = "NO"
                    break
            else: #stack = []일 때
                ans[i] = "NO"
                break
    if stack:
        ans[i] = "NO"

for i in ans:
    print(i)




