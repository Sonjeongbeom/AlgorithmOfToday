import sys
from collections import defaultdict
input = sys.stdin.readline

A,B,C,D=[],[],[],[]
n=int(input())

for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

y=[]

dict=defaultdict(int)

for a in A:
    for b in  B:
        dict[a+b]+=1
           
ans=0
for c in C:
    for d in D:
        value=-(c+d)
        if value in dict:
            ans+=dict[value]
print(ans)
