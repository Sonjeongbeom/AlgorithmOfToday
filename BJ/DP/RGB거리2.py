import sys
def input():
    return sys.stdin.readline().rstrip()

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
INF=int(1e9)

dp_r=[[INF]*3 for _ in range(n)]
dp_g=[[INF]*3 for _ in range(n)]
dp_b=[[INF]*3 for _ in range(n)]
r,g,b=arr[0]

dp_r[1]=[INF,arr[1][1]+r,arr[1][2]+r]
dp_g[1]=[arr[1][0]+g,INF,arr[1][2]+g]
dp_b[1]=[arr[1][0]+b,arr[1][1]+b,INF]

def solve(dp,color):
    global n
    for i in range(2,n):
        r,g,b=arr[i]
        dp[i][0]=min(dp[i-1][1]+r,dp[i-1][2]+r)
        dp[i][1]=min(dp[i-1][0]+g,dp[i-1][2]+g)
        dp[i][2]=min(dp[i-1][1]+b,dp[i-1][0]+b)
    dp[-1][color]=INF
    return min(dp[-1])

print(min([solve(dp_r,0),solve(dp_g,1),solve(dp_b,2)]))