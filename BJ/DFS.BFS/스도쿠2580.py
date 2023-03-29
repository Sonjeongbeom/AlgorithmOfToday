import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

col=defaultdict(set)
row=defaultdict(set)
squares=defaultdict(set)

arr=[]

def check(r,c,item):
    if item not in col[c] and item not in row[r] and item not in squares[(r//3,c//3)]:
        return True
    return False

for _ in range(9):
    arr.append(list(map(int,input().split())))
empty=[]
for r in range(9):
    for c in range(9):
        value=arr[r][c]
        if value>0:
            row[r].add(value)
            col[c].add(value)
            squares[(r//3,c//3)].add(value)
        else:
            empty.append((r,c))
            
def dfs(idx):
    if idx==len(empty):
        for r in range(9):
            for c in range(9):
                print(arr[r][c],end=' ')
            print()
        exit(0)
    for num in range(1,10):
        r,c=empty[idx]
        if check(r,c,num):
            arr[r][c]=num
            row[r].add(num)
            col[c].add(num)
            squares[(r//3,c//3)].add(num)
            dfs(idx+1)
            arr[r][c]=0
            row[r].remove(num)
            col[c].remove(num)
            squares[(r//3,c//3)].remove(num)
            
dfs(0)
