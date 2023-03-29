import sys
def input():
    return sys.stdin.readline().rstrip()

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

n,m,k=map(int,input().split())
arr=[]
smell_num=[[0]*n for _ in range(n)]
sharks={}
sharks_dir=[[0]*5 for _ in range(m+1)]
sharks_d=[0]*(m+1)
shark_cnt=m

for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j]>0:
            sharks[(i,j)]=arr[i][j]
            smell_num[i][j]=arr[i][j]
            arr[i][j]=k
lst=list(map(int,input().split()))
for i in range(len(lst)):
    sharks_d[i+1]=lst[i]
for i in range(m*4):
    num,dir=i//4+1,i%4+1
    lst=list(map(int,input().split()))
    sharks_dir[num][dir]=lst

ans=0
notFound=False
while shark_cnt!=1:
    ans+=1
    if ans>1000:
        notFound=True
        break
    tmp_sharks={}
    for sx,sy in sharks:
        s_num=sharks[(sx,sy)]
        s_d=sharks_d[s_num]
        s_dir=sharks_dir[s_num][s_d]
        mx,my,m_d=-1,-1,s_d
        for d in s_dir:
           nx,ny=sx+dx[d],sy+dy[d] 
           if 0<=nx<n and 0<=ny<n:
               if arr[nx][ny]==0:
                   mx,my=nx,ny
                   m_d=d
                   break
               elif arr[nx][ny]>0 and mx==-1 and my==-1:
                   num=smell_num[nx][ny]
                   if num==s_num:
                       m_d=d
                       mx,my=nx,ny
        if (mx,my) in tmp_sharks:
            origin=tmp_sharks[(mx,my)]
            if origin>s_num:
                tmp_sharks[(mx,my)]=s_num
            shark_cnt-=1
        else:
            tmp_sharks[(mx,my)]=s_num
        sharks_d[s_num]=m_d
    sharks=tmp_sharks
    for i in range(n):
        for j in range(n):
            if arr[i][j]>0:
                arr[i][j]-=1
                if arr[i][j]==0:
                    smell_num[i][j]=0
    for sx,sy in sharks:
        arr[sx][sy]=k
        smell_num[sx][sy]=sharks[(sx,sy)]
                         
if notFound:
    print(-1)
else:
    print(ans)