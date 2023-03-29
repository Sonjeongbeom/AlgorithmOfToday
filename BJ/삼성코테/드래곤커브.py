import sys

def input():
    return sys.stdin.readline().rstrip()

dy=[0,-1,0,1]
dx=[1,0,-1,0]
# -1씩 해주기

n=int(input())
arr=[[0]*(101) for _ in range(101)]

for _ in range(n):
    stack=[]
    x,y,d,g=map(int,input().split())
    arr[y][x]=1
    ny,nx=y+dy[d],x+dx[d]
    arr[ny][nx]=1
    stack.append(d)
    for _ in range(g):
        length=len(stack)
        for i in range(length-1,-1,-1):
            nd=(stack[i]+1)%4
            ny,nx=ny+dy[nd],nx+dx[nd]
            arr[ny][nx]=1
            stack.append(nd)

ans=0
for i in range(100):
    for j in range(100):
        if arr[i][j]==1:
            if arr[i+1][j+1] and arr[i+1][j] and arr[i][j+1]:
                ans+=1
print(ans)
        