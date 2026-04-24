class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_size =0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.explore(grid, r, c,visited)
                max_size = max(max_size, size)
        return max_size

    def explore(self, grid, r, c, visited):
        row_inbound = 0 <= r < len(grid)
        col_inbound = 0 <= c < len(grid[0])

        if not row_inbound or not col_inbound:
            return 0
        if grid[r][c] == 0:
            return 0
        pos = (r,c)
        if pos in visited:
            return 0
        visited.add(pos)
        size = 1
        size+=self.explore(grid, r-1, c, visited)
        size+=self.explore(grid, r+1, c, visited)
        size+=self.explore(grid, r, c-1, visited)
        size+=self.explore(grid, r, c+1, visited)
        return size

    

        