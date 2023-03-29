import sys

def input():
    return sys.stdin.readline().rstrip()

ans=0

n=int(input())

arr=[0]*n

for i in range(n):
    a,b=map(int,input().split())
    arr[i]=(a,b)
    
def dfs(idx):
    global ans
    if idx==len(arr):
        value=0
        for a in arr:
            if a[0]<=0:
                value+=1
        ans=max(ans,value)
        return
    
    for i in range(len(arr)):
        hp,weight=arr[idx]
        if hp<=0:
            dfs(idx+1)
        elif i!=idx:
            nhp,nweight=arr[i]
            if nhp<=0:
                dfs(idx+1)
            else:
                arr[idx]=(hp-nweight,weight)
                arr[i]=(nhp-weight,nweight)
                if nhp-weight<=0:
                    dfs(idx+1)
                else:
                    dfs(idx+1)
                arr[idx]=(hp,weight)
                arr[i]=(nhp,nweight)
    
    
if n==1:
    print(0)
else:
    dfs(0)
    print(ans)