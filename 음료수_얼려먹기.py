m,n = map(int,input().split())
graph=[]
for i in range(m):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    elif graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    else:
        return False

icecream = 0 
for i in range(m):
    for j in range(n):
        if dfs(i,j) == True:
            icecream += 1
print(icecream)
