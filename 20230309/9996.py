import sys
from collections import deque
import copy

N = int(sys.stdin.readline().rstrip())
left, right = map(str, sys.stdin.readline().rstrip().split("*"))

for _ in range(N) :
    name = sys.stdin.readline().rstrip()
    if len(left) + len(right) > len(name) :
        print('NE')
    else :
        if name[:len(left)] == left and name[-len(right):] == right :
            print('DA')
        else :
            print('NE')