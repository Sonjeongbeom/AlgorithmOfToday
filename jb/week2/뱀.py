import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
apples, moves = [], deque()

for _ in range(K) :
    x, y = map(int, sys.stdin.readline().rstrip().split())
    apples.append((x, y))

L = int(sys.stdin.readline().rstrip())
for _ in range(L) :
    sec, dir = map(str, sys.stdin.readline().rstrip().split())
    moves.append((int(sec), dir))

board = [[0] * N for _ in range(N)]

# 0 : 빈칸, 1 : 사과, 2: 뱀
for x, y in apples :
    board[x-1][y-1] = 1

# 북 / 동 / 남 / 서
dirs = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

def turn90(cdir) :
    sec, dir = moves.popleft()
    if dir == 'L' :
        return (cdir - 1) % 4
    else :
        return (cdir + 1) % 4
    
cx, cy, cdir, time = 0, 0, 1, 0
queue = deque([(cx, cy)])
board[cx][cy] = 2
    
while True :
    dx, dy = dirs[cdir]
    nx, ny = cx + dx, cy + dy
    time += 1

    if -1 < nx < N and -1 < ny < N and board[nx][ny] != 2 :
        if board[nx][ny] == 1 :
            board[nx][ny] = 2
            queue.append((nx, ny))
        elif board[nx][ny] == 0 :
            board[nx][ny] = 2
            queue.append((nx, ny))
            px, py = queue.popleft()
            board[px][py] = 0

        if moves and moves[0][0] == time :
            cdir = turn90(cdir)
        
        cx, cy = nx, ny

    else :
        break

print(time)