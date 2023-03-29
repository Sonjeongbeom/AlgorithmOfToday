import sys

input=sys.stdin.readline

ans=0
n=int(input())
arr=list(map(int,input().split()))
lis=[arr[0]]

for i in range(1,n):
    if lis[-1]>arr[i]:
        left,right=0,len(lis)
        while left<right:
            mid=(left+right)//2
            if lis[mid]<arr[i]:
                left=mid+1
            else:
                right=mid
        lis[right]=arr[i]
    elif lis[-1]<arr[i]:
        lis.append(arr[i])
print(len(lis))