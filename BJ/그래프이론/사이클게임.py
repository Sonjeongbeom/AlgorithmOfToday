import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()


n,m=map(int,input().split())
parents=[i for i in range(n+1)]

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
        return parents[x]
    return x

def union(a,b):
    a=find(a)
    b=find(b)
    
    if a==b:
        return False
    if a>b:
        parents[b]=a
    else:
        parents[a]=b  
    return True
cycle=False
for i in range(m):
    a,b=map(int,input().split())
    if cycle:continue
    if not union(a,b):
        print(i+1)
        cycle=True
if not cycle:
    print(0)
