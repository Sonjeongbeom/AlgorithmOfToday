import sys

def input():
    return sys.stdin.readline()

arr=[]

n,m=map(int,input().split())

for _ in range(n):
    arr.append(int(input()))
    
left,right=min(arr),max(arr)*m
ans=right

while left<=right:
    mid=(left+right)//2
    value=0
    for t in arr:
        value+=(mid//t)

    if value>=m:
        ans=min(mid,ans)
        right=mid-1
    else:
        left=mid+1

print(ans)
    
    