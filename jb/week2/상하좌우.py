import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(str, sys.stdin.readline().rstrip().split()))

dirs = {
    'L' : (0, -1),
    'R' : (0, +1),
    'U' : (-1, 0),
    'D' : (+1, 0)
}

cx, cy = 1 ,1 
for a in A :
    dx, dy = dirs[a][0], dirs[a][1]
    if 0 < cx + dx < N+1 and 0 < cy + dy < N+1 :
        cx += dx
        cy += dy

print(cx, cy)