import sys

def input():
    return sys.stdin.readline().rstrip()

n,attack=map(int,input().split())
arr=[]
left,right=1,n*int(1e6)*int(1e6)
for _ in range(n):
    lst=list(map(int,input().split()))
    arr.append(lst)
    
while left<=right:
    mid=(left+right)//2
    cur_attack=attack
    cur=mid
    for t,a,h in arr:
        if t==1:
            v=h//cur_attack if not h%cur_attack else h//cur_attack+1
            cur-=a*(v-1)
        else:
            cur_attack+=a
            cur+=h
            if cur>mid:
                cur=mid
        if cur<=0:
            break
    if cur<=0:
        left=mid+1
    else:
        ans=mid
        right=mid-1
print(ans)
