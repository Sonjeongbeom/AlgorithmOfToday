import sys

def input():
    return sys.stdin.readline().rstrip()

# 문제가 상당히 DP 혹은 BFS스러움. BOJ 1463번은 DP
# 나누는 선택지가 하나밖에 없기에, 나누는것이 항상 더 우선이다.
# 10만까지이므로 단순 반복문으로 해결가능

n,k=map(int,input().split())
ans=0
value=n

while True:
    if value==1:
        break
    if value%k==0:
        value//=k
    else:
        value-=1
    ans+=1
    
# while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
 #   target = (n // k) * k
 #   result += (n - target)
 #   n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  #  if n < k:
  #    break
    # K로 나누기
   # result += 1
    #n //= k

    
print(ans)
