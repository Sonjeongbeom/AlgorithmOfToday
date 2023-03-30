import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().rstrip().split())

dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

queue = []
visited = [[0] * N for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        if board[i][j] != 0 :
            queue.append((i, j, board[i][j], 0))

queue = deque(sorted(queue, key = lambda x : x[2]))

time = 0
while queue :
    cx, cy, virus, time = queue.popleft()
    if time == S :
        break

    visited[cx][cy] = virus
    for dx, dy in dirs :
        nx, ny = cx + dx , cy + dy
        if -1 < nx < N and -1 < ny < N and visited[nx][ny] == 0 and board[nx][ny] == 0 :
            visited[nx][ny] = 1
            board[nx][ny] = virus
            queue.append((nx, ny, virus, time+1))

print(board[X-1][Y-1])