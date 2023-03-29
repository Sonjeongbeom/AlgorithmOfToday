import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

board=[]
for _ in range(9):
    string=list(input())
    board.append(list(map(int,string)))

cols=defaultdict(set)
rows=defaultdict(set)
squares=defaultdict(set) #key=(r/3,c/3)
empty=[]

for r in range(9):
    for c in range(9):
        value=board[r][c]
        if value==0:
            empty.append((r,c))
        else:
            rows[r].add(value)
            cols[c].add(value)
            squares[(r//3,c//3)].add(value)

def solve(idx):
    if idx==len(empty):
        for r in range(9):
            for c in range(9):
                print(board[r][c],end='')
            print()
        exit(0)
    r,c=empty[idx]
    for num in range(1,10):
        if num not in rows[r] and num not in cols[c] and num not in squares[(r//3,c//3)]:
            rows[r].add(num)
            cols[c].add(num)
            squares[(r//3,c//3)].add(num)
            board[r][c]=num
            solve(idx+1)
            board[r][c]=0
            rows[r].remove(num)
            cols[c].remove(num)
            squares[(r//3,c//3)].remove(num)
            
solve(0)
            
            
        