import sys
from collections import defaultdict, deque

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
graph = defaultdict(list)
for _ in range(M) :
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)

queue = deque([X])
visited = [-1] * (N+1)
visited[X] = 0

while queue :
    node = queue.popleft()
    for i in graph[node] :
        if visited[i] == -1 :
            visited[i] = visited[node] + 1
            queue.append(i)

if K not in visited :
    print(-1)
else :
    for i, v in enumerate(visited) :
        if v == K :
            print(i)