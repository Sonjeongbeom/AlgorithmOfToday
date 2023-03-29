import sys
def input():
    return sys.stdin.readline().rstrip()

str1=input()
str2=input()

dp=[[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
if dp[-1][-1]==0:
    print(0)
else:
    res=[]
    print(dp[-1][-1])
    i,j=len(str1),len(str2)
    while True:
        if dp[i][j]==0:
            break
        if dp[i][j]==dp[i-1][j]:
            i,j=i-1,j
        elif dp[i][j]==dp[i][j-1]:
            i,j=i,j-1
        else:
            res.append(str1[i-1])
            i,j=i-1,j-1
    res=res[::-1]
    for r in res:
        print(r,end='')