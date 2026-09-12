class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxArea = 0
        rows, cols = len(grid),len(grid[0])
        seen = set()
        def dfs(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r,c))
            return 1 + dfs(r,c+1) + dfs(r,c-1) + dfs(r+1,c) + dfs(r-1,c) 


        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r,c))
        return maxArea