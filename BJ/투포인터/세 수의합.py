import sys
from collections import defaultdict

input=sys.stdin.readline

n=int(input())
nums=[]
hash=defaultdict(int)
for _ in range(n):
    num=int(input())
    nums.append(num)

for num1 in nums:
    for num2 in nums:
        hash[num1+num2]=True
ans=0
for num1 in nums:
    for num2 in nums:
        if num2-num1 in hash:
            ans=max(ans,num2)
print(ans)