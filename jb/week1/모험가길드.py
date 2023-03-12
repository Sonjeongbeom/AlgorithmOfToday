import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

answer, tmp = 0, 0

nums.sort()
for num in nums :
    tmp += 1
    if tmp >= num :
        answer += 1
        tmp = 0

print(answer)
