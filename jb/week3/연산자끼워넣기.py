import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
ops = list(map(int, sys.stdin.readline().rstrip().split()))
# +, - *, /

add, minus, mul, div = ops
answers = []
totalCnt = sum(ops)

def dfs(curVal, cnt) :
    global add, minus, mul, div
    if cnt == totalCnt :
        answers.append(curVal)
        return
    else :
        if add > 0 :
            add -= 1
            dfs(curVal + A[cnt+1], cnt + 1)
            add += 1

        if minus > 0 :
            minus -= 1
            dfs(curVal - A[cnt+1], cnt + 1)
            minus += 1

        if mul > 0 :
            mul -= 1
            dfs(curVal * A[cnt+1], cnt + 1)
            mul += 1

        if div > 0 :
            div -= 1
            dfs(int(curVal / A[cnt+1]), cnt + 1)
            div += 1
        
dfs(A[0], 0)
print(max(answers))
print(min(answers))