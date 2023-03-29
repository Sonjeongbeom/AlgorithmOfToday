import sys

def input():
    return sys.stdin.readline().rstrip()

n=int(input())

ans=10000000

arr=[]

check=[False]*21

for _ in range(n):
    arr.append(list(map(int,input().split())))

def dfs(x,idx):
    global ans
    if x==n//2:
        start,link=0,0
        for i in range(n):
            for j in range(n):
                if check[i] and check[j]:
                    start+=arr[i][j]
                if not check[i] and not check[j]:
                    link+=arr[i][j]
        ans=min(ans,abs(start-link))
        return
    
    for i in range(idx,n):
        check[i]=True
        dfs(x+1,i+1)
        check[i]=False
        
dfs(0,0)
    
print(ans)
    