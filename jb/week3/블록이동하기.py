from collections import deque

def solution(board):
    n = len(board)
    time = 0
    visited = []
    dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
    
    def get_next_moves(nodes) :
        moves = []
        nodes = list(nodes)
        sx, sy, ex, ey = nodes[0][0], nodes[0][1], nodes[1][0], nodes[1][1]
        
        for dx, dy in dirs :
            nsx, nsy, nex, ney = sx + dx, sy + dy, ex + dx, ey + dy
            if -1 < nsx < n and -1 < nsy < n and -1 < nex < n and -1 < ney < n and board[nsx][nsy] == 0 and board[nex][ney] == 0 :
                
                moves.append({(nsx, nsy), (nex, ney)})
                
        if sx == ex :
            for i in [-1, 1] :
                if -1 < sx + i < n and -1 < ex + i < n and board[sx+i][sy] == 0 and board[ex+i][ey] == 0 :
                    moves.append({(sx, sy), (sx + i, sy)})
                    moves.append({(ex, ey), (ex + i, ey)})
        
        if sy == ey :
              for i in [-1, 1] :
                if -1 < sy + i < n and -1 < ey + i < n and board[sx][sy+i] == 0 and board[ex][ey+i] == 0 :
                    moves.append({(sx, sy), (sx, sy + i)})
                    moves.append({(ex, ey), (ex, ey + i)})
        return moves 
    
    queue = deque([({(0, 0), (0, 1)}, time)])
    while queue :
        nodes, time = queue.popleft()

        if (n-1, n-1) in nodes :
            return time
        visited.append(nodes)
        moves = get_next_moves(nodes)
        
        for move in moves :
            if move not in visited :
                visited.append(move)
                queue.append((move, time + 1))