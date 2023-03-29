import sys

input=sys.stdin.readline

n,c=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
    
l,r=1,arr[-1]-arr[0]
ans=0

while l<=r:
    mid=(l+r)//2
    cnt=1
    idx=0
    for i in range(n):
        if arr[i]-arr[idx]>=mid:
            cnt+=1
            idx=i
    if cnt>=c:
        ans=mid
        l=mid+1
    else:
        r=mid-1
    
print(ans)