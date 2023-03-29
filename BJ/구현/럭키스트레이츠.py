import sys

def input():
    return sys.stdin.readline().rstrip()

data=input()

left=sum(list(map(int,data[:len(data)//2])))
right=sum(list(map(int,data[len(data)//2:])))

if left==right:
    print("LUCKY")
else:
    print("READY")
