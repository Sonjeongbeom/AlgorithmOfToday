import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
cx, cy, cdir = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range(N) :
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dirs = [(-1, 0), (0, +1), (+1, 0), (+1, 0)]
visited = [[0] * M for _ in range(N)]
answer = 1
turnCnt = 0

def turnLeft(cdir) :
    return (cdir - 1) % 4

while True :
    cdir = turnLeft(cdir)
    dx, dy = dirs[cdir]
    nx, ny = cx + dx, cy + dy

    if -1 < nx < N and -1 < ny < N and board[nx][ny] == 0 and visited[nx][ny] == 0 :
        visited[nx][ny] = 1
        answer += 1
        turnCnt = 0
        cx, cy = nx, ny
        continue

    else :
        turnCnt += 1
    
    if turnCnt == 4 :
        nx -= dx
        ny -= dy
        if -1 < nx < N and -1 < ny < N and visited[nx][ny] == 0 :
            cx, cy = nx, ny
            turnCnt = 0
        else :
            break

print(answer)
    




