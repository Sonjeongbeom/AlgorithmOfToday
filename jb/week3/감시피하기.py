import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())
board = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(N)]

teachers, empties, students = [], [], []
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 'S' :
            students.append((i, j))
        elif board[i][j] == 'T' :
            teachers.append((i, j))
        else :
            empties.append((i, j))

dirs = [1, 2, 3, 4] # 동서남북
cases = list(combinations(empties, 3))

def watch(tx, ty, dir) :
    if dir == 1 :
        while ty < N :
            if board[tx][ty] == 'S' :
                return 1
            elif board[tx][ty] == 'O' :
                return 0
            ty += 1
        return 0
    if dir == 2 :
        while ty > -1 :
            if board[tx][ty] == 'S' :
                return 1
            elif board[tx][ty] == 'O' :
                return 0
            ty -= 1
        return 0
    if dir == 3 :
        while tx < N :
            if board[tx][ty] == 'S' :
                return 1
            elif board[tx][ty] == 'O' :
                return 0
            tx += 1
        return 0
    if dir == 4 :
        while tx > -1 :
            if board[tx][ty] == 'S' :
                return 1
            elif board[tx][ty] == 'O' :
                return 0
            tx -= 1
        return 0

def search() :
    for tx, ty in teachers :
        for dir in dirs :
            if watch(tx, ty, dir):
                return 1
    return 0

canHide = 0
for case in cases :
    for cx, cy in case :
        board[cx][cy] = 'O'

    if not search() :
        canHide = 1
        break
    
    for cx, cy in case :
        board[cx][cy] = 'X'

if canHide :
    print('YES')
else :
    print('NO')