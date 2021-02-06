## 题目描述

```
给定一个无向图 graph，当这个图为二分图时返回 true。

如果我们能将一个图的节点集合分割成两个独立的子集 A 和 B，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，我们就将这个图称为二分图。

graph 将会以邻接表方式给出，graph[i]表示图中与节点 i 相连的所有节点。每个节点都是一个在 0 到 graph.length-1 之间的整数。这图中没有自环和平行边： graph[i]  中不存在 i，并且 graph[i]中没有重复的值。

示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释:
无向图如下:
0----1
| |
| |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释:
无向图如下:
0----1
| \ |
| \ |
3----2
我们不能将节点分割成两个独立的子集。
注意:

graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果 j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
```

## 前置知识

- 图的遍历
- DFS


## 关键点

- 图的建立和遍历
- colors 数组

## 代码

```py
class Solution:
    def dfs(self, grid, colors, i, color, N):
        colors[i] = color
        for j in range(N):
            if grid[i][j] == 1:
                if colors[j] == color:
                    return False
                if colors[j] == 0 and not self.dfs(grid, colors, j, -1 * color, N):
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        grid = [[0] * N for _ in range(N)]
        colors = [0] * N
        for i in range(N):
            for j in graph[i]:
                grid[i][j] = 1
        for i in range(N):
            if colors[i] == 0 and not self.dfs(grid, colors, i, 1, N):
                return False
        return True
```