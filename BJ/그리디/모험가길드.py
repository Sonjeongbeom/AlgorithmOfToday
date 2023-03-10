import sys

def input():
    return sys.stdin.readline().rstrip()

# 10만까지가 범위, 따라서 n^2으로 풀 수 없다.

n=int(input())
arr=list(map(int,input().split()))

ans=0
arr.sort()

cnt=0

for x in arr:
    cnt+=1
    if x<=cnt:
        cnt=0
        ans+=1
        
print(ans)
        
    
    
