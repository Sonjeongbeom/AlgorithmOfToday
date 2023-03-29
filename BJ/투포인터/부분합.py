import sys

input=sys.stdin.readline

n,s=map(int,input().split())
arr=[0]

arr.extend(list(map(int,input().split())))

ans=100000001

for i in range(1,n+1):
    arr[i]+=arr[i-1]

l=1
check=False
for r in range(1,n+1):
    cur_sum=arr[r]-arr[l-1]
    if cur_sum>=s:
        check=True
        while True:
            cur_sum=arr[r]-arr[l-1]
            if l>r:
                l-=1
                break
            if cur_sum<s:
                break
            ans=min(ans,r-l+1)
            l+=1
if not check:
    print(0)
else:
    print(ans)

