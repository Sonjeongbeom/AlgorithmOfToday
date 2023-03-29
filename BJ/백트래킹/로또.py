import sys

def input():
    return sys.stdin.readline().rstrip()

def lottery(origin,arr,idx):
    if 6==len(arr):
        print(*arr)
        return
    
    for i in range(idx,len(origin)):
        if origin[i] not in arr:
            lottery(origin,arr+[origin[i]],i)
    

while True:
    arr=list(map(int,input().split()))[1:]
    arr.sort()
    if len(arr)==0:
        break
    lottery(arr,[],0)
    print()

