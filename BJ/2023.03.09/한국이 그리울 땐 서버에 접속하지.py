import sys

def input():
    return sys.stdin.readline().rstrip()

n=int(input())
pattern=input()
left,right=pattern.split('*')

length=len(left)+len(right)

ans=[]

for _ in range(n):
    target=input()
    if length>len(target):
        ans.append("NE")
        continue
    
    target_left=target[:len(left)]
    target_right=target[::-1][:len(right)][::-1]
    
    if target_left==left and target_right==right:
        ans.append('DA')
    else:
        ans.append("NE")
    
for a in ans:
    print(a)
                
    