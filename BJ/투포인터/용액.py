import sys

def input():
    return sys.stdin.readline().rstrip()

n=int(input())
arr=sorted(list(map(int,input().split())))

min_sum=1000000000
ans=[]

l,r=0,n-1

while l<r:
    cur_sum=abs(arr[l]+arr[r])
    if min_sum>cur_sum:
        min_sum=cur_sum
        ans=[arr[l],arr[r]]
    if arr[l]+arr[r]<0:
        l+=1
    elif arr[l]+arr[r]>0:
        r-=1
    else:
        ans=[arr[l],arr[r]]
        break
print(*ans)