import sys

def input():
    return sys.stdin.readline().rstrip()

dir=[(0,0),(0,1),(0,-1),(-1,0),(1,0)]

n,m,x,y,k=map(int,input().split())

dice=[0,0,0,0,0,0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))
    
cmd_list=list(map(int,input().split()))

nx, ny = x, y
for i in cmd_list:
    dx,dy=dir[i]
    nx += dx
    ny += dy

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx
        ny -= dy
        continue
    turn(i)
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[-1]
    else:
        dice[-1] = arr[nx][ny]
        arr[nx][ny] = 0

    print(dice[0])
        
