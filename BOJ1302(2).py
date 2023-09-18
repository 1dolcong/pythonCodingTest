import sys
input = sys.stdin.readline
books = {} # books = dict()
for _ in range(int(input())):
    title = input().rstrip()
    if title in books:
        books[title] += 1
    else:
        books[title] = 1

max_val = max(books.values())
arr = []
for k, v in books.items():
    if v == max_val:
        arr.append(k)

arr.sort()
print(arr[0])