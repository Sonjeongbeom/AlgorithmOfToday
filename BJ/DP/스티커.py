import sys

def input():
    return sys.stdin.readline().rstrip()

t=int(input())

for _ in range(t):
    dp=[]
    n=int(input())
    for _ in range(2):
        dp.append(list(map(int,input().split())))
    for i in range(1,n):
        for j in range(2):
            if j==0:
                dp[j][i]=max(dp[j][i]+dp[1][i-1],dp[j][i-1])
            else:
                dp[j][i]=max(dp[j][i]+dp[0][i-1],dp[j][i-1])

    print(max(dp[0][n-1],dp[1][n-1]))                