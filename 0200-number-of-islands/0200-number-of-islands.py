class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        n, m = len(grid), len(grid[0])

        visited = [[False for _ in range(m)] for _ in range(n)]

        def dfs(x, y):
            stack = []
            stack.append((x, y))

            while stack:
                cur_x, cur_y = stack.pop()

                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = cur_x+dx, cur_y+dy

                    if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and grid[nx][ny] == "1":
                        stack.append((nx, ny))
                        visited[nx][ny] = True


        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = True
                    answer += 1
                    dfs(i, j)

        return answer

        