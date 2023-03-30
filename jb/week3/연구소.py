import sys
from collections import deque
from itertools import combinations
import copy

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 0 빈칸 / 1 벽 / 2 바이러스

emptys, viruses = [], []
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 0 :
            emptys.append((i, j))
        elif board[i][j] == 2 :
            viruses.append((i, j))

cases = list(combinations(emptys, 3))
dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

def makeWall(case, tmp) :
    for x, y in case :
        tmp[x][y] = 1
    return tmp

def bfs(tmp) :
    visited = [[0] * M for _ in range(N)]
    queue = deque(viruses)
    while queue :
        cx, cy = queue.popleft()
        visited[cx][cy] = 1
        for dx, dy in dirs :
            nx, ny = cx + dx, cy + dy
            if -1 < nx < N and -1 < ny < M and visited[nx][ny] == 0 and tmp[nx][ny] == 0 :
                visited[nx][ny] = 1
                tmp[nx][ny] = 2
                queue.append((nx, ny))
    return tmp

def countSafeArea(tmp) :
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if tmp[i][j] == 0 :
                cnt += 1

    return cnt

answer = 0

for case in cases :
    tmp = copy.deepcopy(board)
    tmp = makeWall(case, tmp)
    tmp = bfs(tmp)
    cnt = countSafeArea(tmp)
    answer = max(answer, cnt)

print(answer)


