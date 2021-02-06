## 题目描述

```
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

```

## 前置知识

- DFS



def numIslands(self, grid):
    if not grid or not grid[0]: return 0
    row, col = len(grid), len(grid[0])
    self.visited = [[False for _ in range(col)] for _ in range(row)]
    
    def floodfill(i, j):
        if grid[i][j] == '1' and self.visited[i][j] == False:
            self.visited[i][j] = True
            if i > 0:
                floodfill(i - 1, j)
            if i < row - 1:
                floodfill(i + 1, j)
            if j > 0:
                floodfill(i, j - 1)
            if j < col - 1:
                floodfill(i, j + 1)
    
    res = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1' and self.visited[i][j] == False:
                res += 1
                floodfill(i, j)
    return res


##azl
python code:

``` python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
                    
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
