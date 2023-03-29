import sys
from collections import deque
import math

def input():
    return sys.stdin.readline().rstrip()

dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

n,m,k=map(int,input().split())

arr=[[deque() for _ in range(n)] for _ in range(n)]

fires=deque()

for _ in range(m):
    r,c,m,s,d=map(int,input().split())
    arr[r-1][c-1].append((m,s,d))
    fires.append((r-1,c-1))
    
for i in range(k):
    length=len(fires)
    for _ in range(length):
        r,c=fires.popleft()
        m,s,d=arr[r][c].popleft()
        dr,dc=dir[d]
        nr,nc=(r+dr*s)%n,(c+dc*s)%n
        fires.append((nr,nc))
        arr[nr][nc].append((m,s,d))
    
    length=len(fires)
    hash={}
    for _ in range(length):
        r,c=fires.popleft()
        if (r,c) in hash:
            continue
        if len(arr[r][c])>1:
            hash[(r,c)]=True
            l=len(arr[r][c])
            sum_m,sum_s,even,odd=0,0,0,0
            while arr[r][c]:
                m,s,d=arr[r][c].popleft()
                sum_m+=m
                sum_s+=s
                if d%2==0:
                    even+=1
                elif d%2==1:
                    odd+=1
            sum_m=int(math.floor(sum_m//5))
            sum_s=int(math.floor(sum_s//l))
            if even>0 and odd>0:
                sum_d=False
            else:
                sum_d=True
            if sum_m>0:
                if sum_d:
                    for d in [0,2,4,6]:
                        arr[r][c].append((sum_m,sum_s,d))
                        fires.append((r,c))
                else:
                    for d in [1,3,5,7]:
                        arr[r][c].append((sum_m,sum_s,d))
                        fires.append((r,c))
        else:
            fires.append((r,c))

ans=0
while fires:
    r,c=fires.popleft()
    m,s,d=arr[r][c].popleft()
    ans+=m

print(ans)