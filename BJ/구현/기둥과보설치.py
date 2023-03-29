def solution(n, build_frame):
    answer = []
    a_arr=[[0]*(n+1) for _ in range(n+1)]
    b_arr=[[0]*(n+1) for _ in range(n+1)]
    
    def check_a(x,y):
        return y==0 or (a_arr[x][y-1]==1 or (x>0 and b_arr[x-1][y]==1) or b_arr[x][y]==1)

    def check_b(x,y):
        return x<n and y>0 and (a_arr[x][y-1]==1 or a_arr[x+1][y-1]==1 or (x>0 and b_arr[x-1][y]==1 and b_arr[x+1][y]==1))
        
    
    def check(x,y):
        for i in range(len(a_arr)):
            for j in range(len(b_arr)):
                if a_arr[i][j]==1 and not check_a(i,j):
                    return False
                if b_arr[i][j]==1 and not check_b(i,j):
                    return False
        return True
    
    for build in build_frame:
        x,y,a,b=build
        if a==0:
            if b==1:
                if check_a(x,y):
                    a_arr[x][y]=1
            else:
                a_arr[x][y]=0
                if not check(x,y):
                    a_arr[x][y]=1
                    
        else:
            if b==1:
                if check_b(x,y):
                    b_arr[x][y]=1
            else:
                b_arr[x][y]=0
                if not check(x,y):
                    b_arr[x][y]=1
                    
    for i in range(len(a_arr)):
        for j in range(len(a_arr)):
            if a_arr[i][j]:
                answer.append([i,j,0])
            if b_arr[i][j]:
                answer.append([i,j,1])

    return answer