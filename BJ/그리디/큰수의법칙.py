import sys

def input():
    return sys.stdin.readline().rstrip()

# 2<=N<=1000, 1<=M<=10000, 1<=K<=10000
# N의 범위를 봤을때, 정렬을 통해 가장 큰 수를 찾아낸다.

n,m,k=map(int,input().split())

arr=list(map(int,input().split()))

arr.sort(reverse=True)

repeat=0
ans=0

for _ in range(m):
    if repeat==k:
        repeat=0
        ans+=arr[1]
    else:
        ans+=arr[0]
        repeat+=1
    
print(ans)
