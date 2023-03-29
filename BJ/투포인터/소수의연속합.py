import sys
from collections import defaultdict

input=sys.stdin.readline
n=int(input())
hash=defaultdict(int)
a = [True] * (n + 1)
m = int(n**0.5)

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, n + 1, i):
            a[j] = False
        
arr=[i for i in range(2, n+1) if a[i] == True]

l,cur=0,0
ans=0
for r in range(len(arr)):
    cur+=arr[r]
    while cur>=n and l<len(arr):
        if cur==n:
            ans+=1
            break
        cur-=arr[l]
        l+=1
print(ans)