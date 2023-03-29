import sys
def input():
    return sys.stdin.readline().rstrip()

def lower_bound(lis,x):
    left,right=0,len(lis)
    while left<right:
        mid=(left+right)//2
        if lis[mid][1]<x:
            left=mid+1
        else:
            right=mid
    return right

n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))
arr.sort()
lis=[arr[0]]
dp=[0 for _ in range(n)]
dp[0]=0
ans=n

for i in range(1,n):
    if lis[-1][1]>arr[i][1]:
        idx=lower_bound(lis,arr[i][1])
        dp[i]=idx
        lis[idx]=arr[i]
    elif lis[-1][1]<arr[i][1]:
        lis.append(arr[i])
        dp[i]=len(lis)-1
ans-=len(lis)
res=[]
max_idx=len(lis)-1
for i in range(n-1,-1,-1):
    if dp[i]!=max_idx:
        res.append(arr[i][0])
    else:
        max_idx-=1
res.reverse()
print(ans)
for r in res:
    print(r)
