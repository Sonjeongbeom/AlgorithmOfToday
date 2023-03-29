import sys
def input():
    return sys.stdin.readline().rstrip()
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
stack=[]
ans=0

for i,h in enumerate(arr+[-1]):
    start=i
    while stack and stack[-1][1]>=h:
        idx,height=stack.pop()
        ans=max(ans,height*(i-idx))
        start=idx
    stack.append((start,h))

    
print(ans)