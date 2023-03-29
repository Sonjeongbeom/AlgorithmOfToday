import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

ans=[]

check={'a':True, 'e':True, 'i':True, 'o':True, 'u':True}

n,m=map(int,input().split())
arr=list(input().split())
arr.sort()
    
res=list(combinations(arr,n))

for r in res:
    cnt=0
    for ch in r:
        if ch in check:
            cnt+=1
    
    if cnt>0 and n-cnt>=2:
        ans.append(r)

for value in ans:
    print(''.join(value))
    