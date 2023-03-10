import sys

def input():
    return sys.stdin.readline().rstrip()

string=input()

one_str=0
zero_str=0

series=int(string[0])
prev=series

for i in range(1,len(string)):
    num=int(string[i])
    if prev!=num:
        if series==0:
            zero_str+=1
        else:
            one_str+=1
        series=num
    prev=num

if series==1:
    one_str+=1
else:
    zero_str+=1
    
print(min(one_str,zero_str))