import sys
from collections import deque
input = sys.stdin.readline
table = {chr(ord('A')+i): 0 for i in range(int(input()))}

s = input().rstrip()
for i in range(len(table)):
    table[chr(ord('A')+i)] = int(input())
def cal(opr, opd):
    if opr == '*':
        op2 = opd.pop()
        op1 = opd.pop()
        return op1 * op2
    elif opr == '/':
        op2 = opd.pop()
        op1 = opd.pop()
        return op1 / op2
    elif opr == '+':
        op2 = opd.pop()
        op1 = opd.pop()
        return op1 + op2
    else: # '-'
        op2 = opd.pop()
        op1 = opd.pop()
        return op1 - op2

opd = deque()
for c in s:
    if c == '*' or c == '/' or c == '+' or c == '-': # 연산자
        opd.append(cal(c,opd))
    else: #피연산자
        opd.append(table[c])
print("{:.2f}".format(opd[-1]))
