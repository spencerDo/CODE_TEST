from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
city = [[] for _ in range(n + 1)]

for _ in range(m):
    n1, n2 = map(int, stdin.readline().split())
    city[n1].append(n2)

visited = [-1 for _ in range(n + 1)]
visited[x] = 0

def bfs(graph, v, visited):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)

bfs(city, x, visited)

check = 1
for i in range(n+1):
    if visited[i] == k:
        print(i)
        check = 0

if check:
  print(-1)
