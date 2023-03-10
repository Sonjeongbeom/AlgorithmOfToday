import sys

def input():
    return sys.stdin.readline().rstrip()

# 걍 n^2으로 풀기 쌉가능
# 하지만 hash를 활용하면 좀 더 잘 풀 수 있음.

n,m=map(int,input().split())

arr=list(map(int,input().split()))

hash={}

for item in arr:
    if item not in hash:
        hash[item]=1
    else:
        hash[item]+=1

ans=0

for i in range(1,m+1):
    n-=hash[i]
    ans+=hash[i]*n
    
print(ans)