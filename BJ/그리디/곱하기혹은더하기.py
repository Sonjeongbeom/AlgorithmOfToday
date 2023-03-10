import sys

def input():
    return sys.stdin.readline().rstrip()

# 문제 딱 보면 브루트포스가 생각남 ..
# 잘 살펴보면 당연히 곱하기가 가능하면 곱하기만 하는게 이득이다. 0과 1만 +를 한다.

numbers=input()

ans=int(numbers[0])

for i in range(1,len(numbers)):
    num=int(numbers[i])
    if num==1 or ans==0:
        ans+=num
    else:
        ans*=num

print(ans)        