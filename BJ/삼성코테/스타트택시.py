import sys
def input():
    return sys.stdin.readline().rstrip()

n,m,k=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))