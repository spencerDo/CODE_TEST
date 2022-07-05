def solution(n, computers):
    def dfs(x,y):
        if x < 0 or y < 0 or x >= n or y >= n:
            return False
        if computers[x][y] == 1:
            computers[x][y] = 0
            dfs(x,y-1)
            dfs(x,y+1)
            dfs(x+1,y)
            dfs(x-1,y)
            return True
        return False
    answer = 0
    for i in range(n):
        for j in range(n):
            if dfs(i,j) == True:
                answer += 1
    return answer
