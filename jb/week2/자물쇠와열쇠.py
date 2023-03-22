def solution(key, lock):
    n, m = len(lock), len(key)
    # 0 홈 / 1 돌기
    board = [[1] * (n + 2 * (m-1)) for _ in range((n + 2 * (m-1)))]
    for i in range(n) :
        for j in range(n) :
            board[i + (m-1)][j + (m-1)] = lock[i][j]

    def rotateRight90(key) :
        tmpKey = [[0] * m for _ in range(m)]
        for i in range(m) :
            for j in range(m) :
                tmpKey[i][j] = key[m-j-1][i]
        return tmpKey
    
    def put(key, cx, cy) :
        for i in range(m) :
            for j in range(m) :
                board[cx + i][cy + j] += key[i][j]
    
    def back(key, cx, cy) :
        for i in range(m) :
            for j in range(m) :
                board[cx + i][cy + j] -= key[i][j]
    
    def check() :
        for i in range(m - 1 , m - 1 + n) :
            for j in range(m - 1 , m - 1 + n) :
                if board[i][j] != 1 :
                    return False
        return True
    
    for i in range(len(board) - m + 1) :
        for j in range(len(board) - m + 1) :
            for r in range(4) :
                key = rotateRight90(key)
                put(key, i, j)
                if check() :
                    return True
                back(key, i, j)
    
    return False