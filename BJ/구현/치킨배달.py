import sys

def input():
    return sys.stdin.readline().rstrip()

def calc(x,y,nx,ny):
    return abs(x-nx)+abs(y-ny)

n,m=map(int,input().split())

arr=[]
house=[]
chicken=[]
ans=100000000

for _ in range(n):
    arr.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chicken.append((i,j))
        if arr[i][j]==1:
            house.append((i,j))
            
def solve(arr,idx):
    global house
    global ans
    if len(arr)==m:
        sum_value=0
        for x,y in house:
            value=10000000
            for nx,ny in arr:
                value=min(value,calc(x,y,nx,ny))
            sum_value+=value
        ans=min(ans,sum_value)
        return
    
    for i in range(idx,len(chicken)):
        if chicken[i] not in arr:
            solve(arr+[chicken[i]],i)

solve([],0)
print(ans)