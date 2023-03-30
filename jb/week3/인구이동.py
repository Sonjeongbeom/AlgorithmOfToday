import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dirs = [(-1, 0), (+1, 0), (0, -1), (0, + 1)]

def move(x, y, group, visited) :
    united = []
    united.append((x, y))

    queue = deque([(x, y)])
    while queue :
        x, y = queue.popleft()
        visited[x][y] = group
        for dx, dy in dirs :
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and visited[nx][ny] == 0 :
                diff = abs(board[x][y] - board[nx][ny])
                if L <= diff <= R :
                    visited[nx][ny] = group
                    united.append((nx, ny))
                    queue.append((nx, ny))
    
    population = 0
    for ux, uy in united :
        population += board[ux][uy]
    
    for ux, uy in united : 
        board[ux][uy] = population // len(united)

answer = 0
while True :
    visited = [[0] * N for _ in range(N)]
    group = 1

    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == 0 :
                move(i, j, group, visited)
                group += 1
    
    if group > N ** 2 :
        break
    answer += 1

print(answer)