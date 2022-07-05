def dfs(x, y, graph):
    graph[x][y] = 0
    for i in range(len(graph)):
        if graph[y][i] == 1:
            dfs(y, i, graph)

def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                answer += 1
                dfs(i, j, computers)
    return answer
