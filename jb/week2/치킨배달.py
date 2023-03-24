import sys
from itertools import combinations

# 0 : 빈칸 / 1 : 집 / 2 : 치킨집
N, M = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(N) :
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

homes, chickens = [], []

for i in range(N) :
    for j in range(N) :
        if board[i][j] == 1 :
            homes.append((i,j))
        elif board[i][j] == 2 :
            chickens.append((i, j))

answers = []
cases = list(combinations(chickens, M))

for case in cases :
    total = 0
    for hx, hy in homes :
        tmp = float('Inf')
        for cx, cy in case :
            tmp = min(tmp, abs(cx - hx) + abs(cy - hy))
        total += tmp
    answers.append(total)

print(min(answers))