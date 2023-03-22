import sys

loc = sys.stdin.readline().rstrip()
row, col = int(loc[1]) - 1, ord(loc[0]) - 97

dirs = [(-1, -2), (-1, +2), (+1, -2), (+1, +2), (-2, -1), (-2, +1), (+2, -1), (+2, +1)]

cnt = 0

for dx, dy in dirs :
    nx, ny = row + dx, col + dy
    if -1 < nx < 8 and -1 < ny < 8 :
        cnt += 1

print(cnt)