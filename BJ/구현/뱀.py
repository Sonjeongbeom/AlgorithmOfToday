import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n=int(input())
k=int(input())
dx=[0,-1,0,1]
dy=[1,0,-1,0]

dir=0

# L : +1
# R : -1
ans=0
arr=[[0]*n for _ in range(n)]
for _ in range(k):
    x,y=map(int,input().split())
    arr[x-1][y-1]=1
    
l=int(input())
change_dir={}

for _ in range(l):
    time,d=input().split()
    change_dir[int(time)]=d

q=deque([(0,0)])

while q:
    x,y=q.popleft()
    ans+=1
    
    nx,ny=x+dx[dir],y+dy[dir]
    if nx>=0 and ny>=0 and nx<n and ny<n:
        q.appendleft((x,y))
        if (nx,ny) in q:
            break
        q.appendleft((nx,ny))
        if arr[nx][ny]==1:
            arr[nx][ny]=0
        else:
            tmp=deque()
            length=len(q)
            for _ in range(length-1):
                x,y=q.popleft()
                tmp.append((x,y))
            q=deque()
            while tmp:
                x,y=tmp.popleft()
                q.append((x,y))
    else:
        break
    if ans in change_dir:
        d=change_dir[ans]
        if d=='L':
            if dir==3:
                dir=0
            else:
                dir+=1
        else:
            if dir==0:
                dir=3
            else:
                dir-=1
print(ans)