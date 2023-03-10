import sys

def input():
    return sys.stdin.readline().rstrip()

# 문제를 보면.. 이분탐색부터 생각이나는데
# 이거 참고했음, 모두 더하면 결국 그 값보다 큰건 못만들겠네?

n=int(input())
arr=list(map(int,input().split()))
arr.sort()

target=1
for x in arr:
    if target<x:
        break
    target+=x
    
print(target)

