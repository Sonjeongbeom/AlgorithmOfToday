import sys

def input():
    return sys.stdin.readline().rstrip()

# 1<=N,M<=100
# O(n^2) 으로 풀어도 10000번 연산이라 브루트 포스(그리디)

n,m=map(int,input().split())
arr=[]
ans=0

for _ in range(n):
    arr.append(list(map(int,input().split())))
    
for i in range(n):
    min_val=10001
    for j in range(m):
        min_val=min(arr[i][j],min_val)
    ans=max(ans,min_val)
    
print(ans)