import sys
input = sys.stdin.readline

res = 4000000000
n=int(input())
arr=sorted(list(map(int,input().split())))
ans=[]

for i in range(n-2):
    pivot=arr[i]
    l,r=i+1,n-1
    while l<r:
        cur=pivot+arr[l]+arr[r]
        if abs(res)>=abs(cur):
            ans=[pivot,arr[l],arr[r]]
            res=cur
        if cur<0:
            l+=1
        elif cur>0:
            r-=1
        else:
            print(*ans)
            sys.exit()
            
print(*ans)
        
    