import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

# 0 빈칸 / 1 벽 / 2 바이러스
N, M = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(N) :
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
viruses = []

for i in range(N) :
    for j in range(N) :
        if board[i][j] == 2 :
            board[i][j] = '*'
            viruses.append((i, j))
        elif board[i][j] == 0 :
            board[i][j] = -1
        else :
            board[i][j] = '-'

cases = list(combinations(viruses, M))

def check(tmp) :
    for i in range(N) :
        for j in range(N) :
            if tmp[i][j] == -1 :
                return False
    return True

answer = float('Inf')
for case in cases :
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    time = 0
    tmp = deepcopy(board)
    for c in case :
        x, y = c
        queue.append((x, y, 0))
        visited[x][y] = 1
        tmp[x][y] = 0

    while queue :
        cx, cy, ctime = queue.popleft()
        for dx, dy in dirs :
            nx, ny = cx + dx, cy + dy
            if -1 < nx < N and -1 < ny < N and visited[nx][ny] == 0 and tmp[nx][ny] != '-' :
                if tmp[nx][ny] == -1 :
                    visited[nx][ny] = 1
                    tmp[nx][ny] = 1
                    queue.append((nx, ny, ctime + 1))
                    time = max(time, ctime+1)

                elif tmp[nx][ny] == '*' :
                    visited[nx][ny] = 1
                    tmp[nx][ny] = 1
                    queue.append((nx, ny, ctime + 1))


    if not check(tmp) :
        time = float('Inf')
    answer = min(answer, time)

if answer == float('Inf') :
    print(-1)
else :
    print(answer)