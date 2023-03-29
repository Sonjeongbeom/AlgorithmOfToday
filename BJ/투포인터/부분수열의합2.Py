import sys
from collections import defaultdict

def input():
    return sys.stdin.readline()

n,s=map(int,input().split())
arr=list(map(int,input().split()))
hash=defaultdict(int)
hash2=defaultdict(int)
ans=0

def calc(depth,cur):
    if depth==n//2:
        hash[cur]+=1
        return
    calc(depth+1,cur+arr[depth])
    calc(depth+1,cur)

def calc_rest(depth,cur):
    global ans
    global s
    if depth==n:
        ans+=hash[s-cur]
        return
    calc_rest(depth+1,cur+arr[depth])
    calc_rest(depth+1,cur)
calc(0,0)
calc_rest(n//2,0)
if s==0:
    print(ans-1)
else:
    print(ans)