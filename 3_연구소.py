m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

def dfs(x,y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    elif graph[x][y] == 2:
        count = 0
        graph[x][y] = 2
        count += 1
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        print(count)
    else:
        return False
dfs(m,n)
