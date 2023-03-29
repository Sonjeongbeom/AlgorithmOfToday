import sys
from collections import deque

def input():
    return sys.stdin.readline()
r,c,m=map(int,input().split())
dx=[0,-1,1,0,0]
dy=[0,0,0,1,-1]
NO=(0,0,0)
ans=0

arr=[[NO]*(c) for _ in range(r)]
sharks=[]


for _ in range(m):
    sr,sc,s,d,z=map(int,input().split())
    arr[sr-1][sc-1]=(s,d,z)

for fish_y in range(c):
    for fish_x in range(r):
        if arr[fish_x][fish_y]!=NO:
            ans+=arr[fish_x][fish_y][2]
            arr[fish_x][fish_y]=NO
            break
    tmp_sharks={}
    for sx in range(r):
        for sy in range(c):
            if arr[sx][sy]!=NO:
                s,d,z=arr[sx][sy]
                nx,ny=sx+dx[d]*s,sy+dy[d]*s
                arr[sx][sy]=NO
                if nx>=0 and ny>=0 and nx<r and ny<c:
                    if (nx,ny) in tmp_sharks:
                        if tmp_sharks[(nx,ny)][2]<z:
                            tmp_sharks[(nx,ny)]=(s,d,z)
                    else:
                        tmp_sharks[(nx,ny)]=(s,d,z)
                else: 
                    if d==1:
                        tmp_value=s-sx
                        tmp_x=0
                        change=abs(nx//r)
                        while tmp_value!=0:
                            if d==1:
                                d=2
                            else:
                                d=1
                            value=min(r-1,tmp_value)
                            tmp_value-=value
                            tmp_x+=dx[d]*value
                        if (tmp_x,ny) in tmp_sharks:
                            if tmp_sharks[(tmp_x,ny)][2]<z:
                                tmp_sharks[(tmp_x,ny)]=(s,d,z)
                        else:
                            tmp_sharks[(tmp_x,ny)]=(s,d,z)
                    elif d==2:
                        tmp_value=s-(r-1-sx)
                        tmp_x=r-1
                        change=abs(nx//r)
                        while tmp_value!=0:
                            if d==1:
                                d=2
                            else:
                                d=1
                            value=min(r-1,tmp_value)
                            tmp_value-=value
                            tmp_x+=dx[d]*value
                        if (tmp_x,ny) in tmp_sharks:
                            if tmp_sharks[(tmp_x,ny)][2]<z:
                                tmp_sharks[(tmp_x,ny)]=(s,d,z)
                        else:
                            tmp_sharks[(tmp_x,ny)]=(s,d,z)
                    elif d==3:
                        tmp_value=s-(c-1-sy)
                        tmp_y=c-1
                        change=abs(ny//c)
                        while tmp_value!=0:
                            if d==3:
                                d=4
                            else:
                                d=3
                            value=min(c-1,tmp_value)
                            tmp_value-=value
                            tmp_y+=dy[d]*value
                        if (nx,tmp_y) in tmp_sharks:
                            if tmp_sharks[(nx,tmp_y)][2]<z:
                                tmp_sharks[(nx,tmp_y)]=(s,d,z)
                        else:
                            tmp_sharks[(nx,tmp_y)]=(s,d,z)
                    else:
                        tmp_value=s-sy
                        tmp_y=0
                        change=abs(ny//c)
                        while tmp_value!=0:
                            if d==3:
                                d=4
                            else:
                                d=3
                            value=min(c-1,tmp_value)
                            tmp_value-=value
                            tmp_y+=dy[d]*value
                        if (nx,tmp_y) in tmp_sharks:
                            if tmp_sharks[(nx,tmp_y)][2]<z:
                                tmp_sharks[(nx,tmp_y)]=(s,d,z)
                        else:
                            tmp_sharks[(nx,tmp_y)]=(s,d,z)

    for key,value in tmp_sharks.items():
        nx,ny=key
        arr[nx][ny]=value

print(ans)