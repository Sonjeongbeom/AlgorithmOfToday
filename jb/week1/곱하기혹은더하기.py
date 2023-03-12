import sys

S = sys.stdin.readline().rstrip()

answer = int(S[0])
for i in range(1, len(S)) :
    if answer <= 1 or int(S[i]) <= 1 :
        answer += int(S[i])
    else :
        answer *= int(S[i])

print(answer)