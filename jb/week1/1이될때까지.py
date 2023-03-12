import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

while True :
    if N < K :
        break

    while N % K != 0 :
        N -= 1
        cnt += 1

    N //= K
    cnt += 1

cnt += (N - 1)
print(cnt)