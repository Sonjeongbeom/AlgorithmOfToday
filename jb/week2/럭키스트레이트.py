import sys

N = list(map(int, sys.stdin.readline().rstrip()))

if sum(N[:len(N)//2]) == sum(N[len(N)//2:]) :
    print('LUCKY')
else :
    print('READY')