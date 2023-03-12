import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()
first, second = nums[-1], nums[-2]

cnt = ((M // (K+1)) * K) + (M % (K+1))

answer = cnt * first + (M - cnt) * second
print(answer)