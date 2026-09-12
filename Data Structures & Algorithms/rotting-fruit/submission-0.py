class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)] 
        # right, left, up, down
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
        mins = -1
        # BFS
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dh, dv  in directions:
                    nr, nc = r + dh, c + dv
                    # if out of bounds or visited SKIP
                    if (
                        nr >= rows or nr < 0 or
                        nc >= cols or nc < 0 or 
                        grid[nr][nc] != 1
                    ):
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr,nc))
            mins += 1
         # Check if any fresh oranges remain
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        # for the case like if all fruits are rotten at start
        return max(mins, 0)
