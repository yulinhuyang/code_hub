
## 题目描述

给定一个仅包含  0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例：

输入：

```
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```

输出：6

## 前置知识

- 单调栈



//AZL


Python Code:

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, heights, st, ans = len(heights), [0] + heights + [0], [], 0
        for i in range(n + 2):
            while st and heights[st[-1]] > heights[i]:
                ans = max(ans, heights[st.pop(-1)] * (i - st[-1] - 1))
            st.append(i)

        return ans
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            ans = max(ans, self.largestRectangleArea(heights))
        return ans

```