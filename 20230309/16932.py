import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(N) :
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

zeros = []
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 0 :
            zeros.append((i, j))

answer = 0
dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

ones = {}
visited = [[0] * M for _ in range(N)]

def bfs(row, col, cnt) :
    visited[row][col] = cnt
    queue = deque([(row, col)])
    while queue :
        x, y = queue.popleft()
        for dx, dy in dirs : 
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and visited[nx][ny] == 0 and board[nx][ny] == 1 : 
                visited[nx][ny] = cnt
                queue.append((nx, ny))

cnt = 0
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 and visited[i][j] == 0 :
            cnt += 1
            visited[i][j] = cnt
            bfs(i, j, cnt)
            
ones = {}
for i in range(N) :
    for j in range(M) :
        if visited[i][j] not in ones :
            ones[visited[i][j]] = 1
        else :
            ones[visited[i][j]] += 1

answer = 0
for x, y in zeros :
    tmp = 1
    visited_2 = []
    for dx, dy in dirs :
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < M and (nx, ny) not in visited_2 and visited[nx][ny] > 0 :
            visited_2.append(visited[nx][ny])
    for v in set(visited_2) :
        tmp += ones[v]
    answer = max(answer, tmp)

print(answer)