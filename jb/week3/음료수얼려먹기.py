import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

answer = 0
visited = [[0] * M for _ in range(N)]

dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def dfs(x, y) :
    if x <= -1 or x >= N or y <= -1 or y >= M :
        return False
    
    if board[x][y] == 0 :
        board[x][y] = 1
        dfs(x-1, y)
        dfs(x+1 ,y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(N) : 
    for j in range(M) :
        if dfs(i, j) :
            answer += 1

print(answer)

    