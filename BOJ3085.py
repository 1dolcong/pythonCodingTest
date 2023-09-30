import sys

input = sys.stdin.readline
N = int(input())
board = [ list(input().rstrip()) for _ in range(N)]
result = 1

def up_down_check(board, j):
    global result
    cnt = 1
    pre = board[0][j]
    for i in range(1, N):
        if pre == board[i][j]:
            cnt += 1
            if cnt > result:
                result = cnt
        else:
            cnt = 1
        pre = board[i][j]

def left_right_check(board, i):
    global result
    cnt = 1
    pre = board[i][0]
    for j in range(1,N):
        if pre == board[i][j]:
            cnt += 1
            if cnt > result:
                result = cnt
        else:
            cnt = 1
        pre = board[i][j]

def left_right_rotate(board):
    for i in range(N):
        for j in range(N-1):
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            left_right_check(board, i)
            up_down_check(board, j)
            up_down_check(board, j+1)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]


def up_down_rotate(board):
    for j in range(N):
        for i in range(N-1):
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            up_down_check(board, j)
            left_right_check(board, i)
            left_right_check(board, i+1)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]


left_right_rotate(board)
up_down_rotate(board)
print(result)