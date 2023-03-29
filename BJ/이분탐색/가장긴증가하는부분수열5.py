import sys
import bisect
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
lis=[arr[0]]
record=[0 for _ in range(n)]
record[0]=1

for i in range(1,n):
    if lis[-1]>arr[i]:
        idx=bisect.bisect_left(lis,arr[i])
        lis[idx]=arr[i]
        record[i]=idx+1
    elif lis[-1]<arr[i]:
        lis.append(arr[i])
        record[i]=len(lis)
ans=len(lis)
res=[]
max_idx=ans
for i in range(n-1,-1,-1):
    if record[i]==max_idx:
        res.append(arr[i])
        max_idx-=1
    if max_idx<1:
        break
print(ans)
print(*res[::-1])

        