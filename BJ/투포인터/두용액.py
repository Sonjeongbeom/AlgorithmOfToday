import sys

def input():
    return sys.stdin.readline().rstrip()

ans=20000000001
ans_left=-1
ans_right=-1

n=int(input())

arr=list(map(int,input().split()))
arr.sort()

left=0
right=len(arr)-1

while left<right:
    value=abs(arr[left]+arr[right])
    if ans>value:
        ans=value
        ans_left=arr[left]
        ans_right=arr[right]
    if arr[left]+arr[right]<0:
        left+=1
    elif arr[left]+arr[right]==0:
        ans_left=arr[left]
        ans_right=arr[right]
        break
    else:
        right-=1

print(ans_left,ans_right)