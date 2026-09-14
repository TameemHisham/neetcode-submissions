class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0]) # bounds for oceans 
        pacific = set()
        atlantic = set()
        res = []
        directions = [
            (1,0), 
            (-1,0), 
            (0,1), 
            (0,-1) 
        ]


        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, visited)

        for r in range(rows):
            dfs(r, 0, pacific)          # left
            dfs(r, cols - 1, atlantic)  # right

        for c in range(cols):
            dfs(0, c, pacific)          # top
            dfs(rows - 1, c, atlantic)  # bottom

        return list(pacific & atlantic)