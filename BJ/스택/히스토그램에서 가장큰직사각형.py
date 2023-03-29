import sys

def input():
    return sys.stdin.readline()

ans_arr=[]

while True:
    arr=list(map(int,input().split()))
    if len(arr)==1 and arr[0]==0:
        break
    arr=arr[1:]
    stack=[]
    ans=0
    for i,h in enumerate(arr+[-1]):
        start=i
        while stack and stack[-1][1]>h:
            idx,height=stack.pop()
            ans=max(ans,height*(i-idx))
            start=idx
        stack.append((start,h))
    ans_arr.append(ans)
        
for a in ans_arr:
    print(a)