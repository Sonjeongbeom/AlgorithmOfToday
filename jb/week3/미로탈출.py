import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

queue = deque([(0, 0)])
dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
visited = [[0] * M for _ in range(N)]


while queue :
    x, y = queue.popleft()

    visited[x][y] = 1
    for dx, dy in dirs :
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < M and visited[nx][ny] == 0 and board[nx][ny] == 1 :
            visited[nx][ny] = 1
            queue.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

print(board[N-1][M-1])
