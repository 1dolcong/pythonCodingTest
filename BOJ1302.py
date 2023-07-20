import sys

N = int(input())
book_dic = {}
for i in range(N):
    title = str(sys.stdin.readline()).rstrip()
    if not title in book_dic.keys():
        book_dic[title] = 1
    else:
        book_dic[title] += 1
book_dic_title = sorted(book_dic, reverse=True)
most_book = book_dic_title[0]
for i in range(1,len(book_dic_title)):
    if book_dic[book_dic_title[i]] >= book_dic[most_book]:
        most_book = book_dic_title[i]

print(most_book)