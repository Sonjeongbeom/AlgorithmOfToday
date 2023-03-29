import sys
def input():
    return sys.stdin.readline().rstrip()
n=int(input())
arr=[[0]*n for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
likes={}

for _ in range(n*n):
    a,b,c,d,e=map(int,input().split())
    hash={b:True,c:True,d:True,e:True}
    likes[a]={b:True,c:True,d:True,e:True}
    cnt=-1
    empty_cnt=-1
    tx,ty=-1,-1
    for x in range(n):
        for y in range(n):
            if arr[x][y]!=0:
                continue
            now=0
            empty=0
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx>=0 and ny>=0 and nx<n and ny<n:
                    if arr[nx][ny] in hash:
                        now+=1
                    if arr[nx][ny]==0:
                        empty+=1
            if now>cnt:
                cnt=now
                empty_cnt=empty
                tx,ty=x,y
            elif now==cnt and empty_cnt<empty:
                empty_cnt=empty
                tx,ty=x,y
    arr[tx][ty]=a

ans=0
for x in range(n):
    for y in range(n):
        cnt=0
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if arr[nx][ny] in likes[arr[x][y]]:
                    cnt+=1
        if cnt==0:
            ans+=0
        elif cnt==1:
            ans+=1
        elif cnt==2:
            ans+=10
        elif cnt==3:
            ans+=100
        else:
            ans+=1000                  
print(ans)  