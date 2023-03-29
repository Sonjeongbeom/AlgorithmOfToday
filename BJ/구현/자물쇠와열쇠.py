def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret
    


def solution(key, lock):
    answer = False
    lengthLock=len(lock)
    lengthKey=len(key)
    arr=[[0]*lengthLock*3 for _ in range(lengthLock*3)]
    
    for i in range(lengthLock):
        for j in range(lengthLock):
            arr[i+lengthLock][j+lengthLock]=lock[i][j]
            
    for i in range(3*lengthLock-lengthKey):
        for j in range(3*lengthLock-lengthKey):
            for _ in range(4):
                key=rotate_90(key)
                for x in range(lengthKey):
                    for y in range(lengthKey):
                        arr[i+x][j+y]+=key[x][y]
                check=True
                for x in range(lengthLock):
                    for y in range(lengthLock):
                        if arr[x+lengthLock][y+lengthLock]!=1:
                            check=False
                            break
                    if not check:
                        break
                if check:
                    return True
                for x in range(lengthKey):
                    for y in range(lengthKey):
                        arr[i+x][j+y]-=key[x][y]
    return answer