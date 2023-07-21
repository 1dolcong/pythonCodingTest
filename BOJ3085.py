import copy

N = int(input())
board = []
def check(board):
    best = 1
    for i in range(len(board)):
        present = 1
        for j in range(1,len(board)):
            if board[i][j-1] == board[i][j]:
                present += 1
                if best < present:
                    best = present
            else:
                present = 1
    for i in range(len(board)):
        present = 1
        for j in range(1, len(board)):
            if board[j-1][i] == board[j][i]:
                present += 1
                if best < present:
                    best = present
            else:
                present = 1
    return best

for i in range(N):
    board.append(list(input()))

max_val = 1

max_val = 1

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            # Swap elements horizontally
            board_temp = copy.deepcopy(board)
            board_temp[i][j], board_temp[i][j + 1] = board_temp[i][j + 1], board_temp[i][j]
            find = check(board_temp)
            if max_val < find:
                max_val = find

        if i + 1 < N:
            # Swap elements vertically
            board_temp = copy.deepcopy(board)
            board_temp[i][j], board_temp[i + 1][j] = board_temp[i + 1][j], board_temp[i][j]
            find = check(board_temp)
            if max_val < find:
                max_val = find

print(max_val)