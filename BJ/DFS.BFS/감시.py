import sys
from collections import deque
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()

dir=[
     [],
     [[(-1,0)],[(0,1)],[(1,0)],[(0,-1)]],
     [[(0,1),(0,-1)],[(1,0),(-1,0)]],
     [[(-1,0),(0,1)],[(1,0),(0,1)],[(1,0),(0,-1)],[(-1,0),(0,-1)]],
     [[(-1,0),(0,1),(0,-1)],[(1,0),(-1,0),(0,1)],[(1,0),(0,1),(0,-1)],[(1,0),(-1,0),(0,-1)]],
     [[(-1,0),(0,1),(0,-1),(1,0)]]
    ]

ans = 987654321

n,m=map(int,input().split())

arr=[]
cctvs=[]
for _ in range(n):
    arr.append((list(map(int,input().split()))))

for i in range(n):
    for j in range(m):
        if 1<=arr[i][j]<=5:
            cctvs.append((i,j))
            
def dfs(depth):
    global ans
    if depth==len(cctvs):
        cnt=0
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    cnt+=1
        ans=min(ans,cnt)
        return
    
    cctv=cctvs[depth]
    x,y=cctv
    for d in dir[arr[x][y]]:
        tmp=[]
        for dx,dy in d:
            nx,ny=x,y
            while nx>=0 and ny>=0 and nx<n and ny<m:
                if arr[nx][ny]==0:
                    arr[nx][ny]=7
                    tmp.append((nx,ny))
                elif arr[nx][ny]==6:
                    break
                nx+=dx
                ny+=dy
                              
        dfs(depth+1)
        for a,b in tmp:
            arr[a][b]=0

dfs(0)

print(ans)
        