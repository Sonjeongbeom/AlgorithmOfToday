import sys
from copy import deepcopy
sys.setrecursionlimit(10**9)


def input():
    return sys.stdin.readline().rstrip()

dir=[(0,0),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
ans=0

board=[[],[],[],[]]

for j in range(4):
    arr=list(map(int,input().split()))
    for i in range(0,8,2):
        board[j].append((arr[i],arr[i+1]))
        
            
def solve(x,y,board,cnt):
    global ans
    newBoard=deepcopy(board)
    cnt+=newBoard[x][y][0]
    ans=max(ans,cnt)
    newBoard[x][y]=(0,newBoard[x][y][1])
    d=newBoard[x][y][1]
    
    for idx in range(1,17):
        check=False
        for r in range(4):
            for c in range(4):
                if not check and newBoard[r][c][0]==idx:
                    a,b=newBoard[r][c]
                    for i in range(8):
                        nb=b+i
                        if nb>8:
                            nb-=8
                        dr,dc=dir[nb]
                        nr,nc=r+dr,c+dc
                        if nr==x and nc==y:
                            continue
                        if nr>=0 and nc>=0 and nr<4 and nc<4:
                            newBoard[r][c]=(a,nb)
                            newBoard[r][c],newBoard[nr][nc]=newBoard[nr][nc],newBoard[r][c]
                            check=True
                            break
    dx,dy=dir[d]
    for i in range(1,4):
        nx,ny=x+dx*i,y+dy*i
        if nx<0 or ny<0 or nx>=4 or ny>=4:
            break
        if newBoard[nx][ny][0]==-1:
            continue
        newBoard[x][y]=(-1,-1)
        solve(nx,ny,newBoard,cnt)

solve(0,0,board,0)
print(ans)