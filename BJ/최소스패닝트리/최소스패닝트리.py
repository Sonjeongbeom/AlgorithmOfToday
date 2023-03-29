import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

v,e=map(int,input().split())
parent=[x for x in range(v+1)]
edges=[]
for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append([c,a,b])
edges.sort()

def find_parent(x):
    if parent[x]==x:
        return x
    parent[x]=find_parent(parent[x])
    
    return parent[x]

def union(a,b):
    a=find_parent(a)
    b=find_parent(b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

result=0
for edge in edges:
    c,a,b=edge
    if find_parent(a)!=find_parent(b):
        union(a,b)
        result+=c
print(result)