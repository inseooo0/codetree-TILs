n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
result = []

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if n_x >= 0 and n_y >= 0 and n_x < n and n_y < n and not visited[n_x][n_y] and arr[n_x][n_y]:
            dfs(n_x, n_y)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            global cnt
            cnt = 0
            dfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for res in result:
    print(res)