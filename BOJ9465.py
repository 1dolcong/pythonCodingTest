import sys
for _ in range(int(input())):
    n = int(input())
    sticker = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n > 1:
        dp[0][1] = sticker[1][0] + sticker[0][1]
        dp[1][1] = sticker[0][0] + sticker[1][1]
    for i in range(2,n):
        for j in range(2):
            dp[j][i] = max(dp[j^1][i-2],dp[j^1][i-1]) + sticker[j][i]
    print(max(dp[0][n-1],dp[1][n-1]))
