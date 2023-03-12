import sys

N = int(sys.stdin.readline().rstrip())
coins = list(map(int, sys.stdin.readline().rstrip().split()))

coins.sort()
target = 1

for coin in coins :
    if coin > target :
        break

    target += coin

print(target)