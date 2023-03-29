import sys

def input():
    return sys.stdin.readline().rstrip()

r,c,t=map(int,input().split())

dir_x=[1,0,-1,0]
dir_y=[0,1,0,-1]

dusts=[]
up_clean=0
down_clean=0
arr=[]

for _ in range(r):
    arr.append(list(map(int,input().split())))
    
for i in range(r):
    for j in range(c):
        if arr[i][j]>0:
            dusts.append((i,j))
        elif arr[i][j]<0:
            if not up_clean:
                up_clean=(i,j)
            else:
                down_clean=(i,j)
            
for _ in range(t):
    tmp_dusts=[]
    tmp=[]
    for x,y in dusts:
        candidates=[]
        for i in range(4):
            nx,ny=x+dir_x[i],y+dir_y[i]
            if nx>=0 and ny>=0 and nx<r and ny<c and (nx,ny)!=up_clean and (nx,ny)!=down_clean:
                candidates.append((nx,ny))
        if len(candidates)>0:
            dust=arr[x][y]//5
            for cx,cy in candidates:
                tmp.append((cx,cy,dust))
            tmp.append((x,y,-dust*len(candidates)))
        tmp_dusts.append((x,y))
        tmp_dusts.extend(candidates)
    for x,y,value in tmp:
        arr[x][y]+=value
    dusts=tmp_dusts
    
    ux,uy=up_clean
    dx,dy=down_clean
    tmp=[]
    for i in range(ux-1,0,-1):
        arr[i][0]=arr[i-1][0]
    for i in range(c-1):
        arr[0][i]=arr[0][i+1]
    for i in range(ux):
        arr[i][c-1]=arr[i+1][c-1]
    for i in range(c-1,0,-1):
        arr[ux][i]=arr[ux][i-1]
    arr[ux][1]=0
    for i in range(dx+1,r-1):
        arr[i][0]=arr[i+1][0]
    for i in range(c-1):
        arr[r-1][i]=arr[r-1][i+1]
    for i in range(r-1,dx,-1):
        arr[i][c-1]=arr[i-1][c-1]
    for i in range(c-1,1,-1):
        arr[dx][i]=arr[dx][i-1]
    arr[dx][1]=0
                
    dusts=[]
    for i in range(r):
        for j in range(c):
            if arr[i][j]>0:
                dusts.append((i,j))

ans=0
for i in range(r):
    for j in range(c):
        if arr[i][j]>0:
            ans+=arr[i][j]
            
print(ans)
        
                
        
        
    
    