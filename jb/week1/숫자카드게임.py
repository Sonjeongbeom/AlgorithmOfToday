import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
cards = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

mins = []
for i in range(N) :
    mins.append(min(cards[i]))

print(max(mins))