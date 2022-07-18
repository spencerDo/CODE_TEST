n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus = [[] for _ in range(k+1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
  for j in range(n):
    check_virus = arr[i][j]
    if check_virus != 0:
      virus[check_virus].append((i, j))
