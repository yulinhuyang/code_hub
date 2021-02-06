## 题目描述

```
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？




//AZL
Python3 Code:

直接修改第一行和第一列为 0 的解法：

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setRowZeros(matrix: List[List[int]], i:int) -> None:
            C = len(matrix[0])
            matrix[i] = [0] * C

        def setColZeros(matrix: List[List[int]], j:int) -> None:
            R = len(matrix)
            for i in range(R):
                matrix[i][j] = 0

        isCol = False
        R = len(matrix)
        C = len(matrix[0])

        for i in range(R):
            if matrix[i][0] == 0:
                isCol = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for j in range(1, C):
            if matrix[0][j] == 0:
                setColZeros(matrix, j)

        for i in range(R):
            if matrix[i][0] == 0:
                setRowZeros(matrix, i)

        if isCol:
            setColZeros(matrix, 0)

```

另一种方法是用一个特殊符合标记需要改变的结果，只要这个特殊标记不在我们的题目数据范围（0 和 1）即可，这里用 None。

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        这题要解决的问题是，必须有个地方记录判断结果，但又不能影响下一步的判断条件；
        直接改为0的话，会影响下一步的判断条件；
        因此，有一种思路是先改为None，最后再将None改为0；
        从条件上看，如果可以将第一行、第二行作为记录空间，那么，用None应该也不算违背题目条件；
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # 遍历矩阵，用None记录要改的地方，注意如果是0则要保留，否则会影响下一步判断
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] is not None and matrix[r][c] == 0:
                    # 改值
                    for i in range(rows):
                        matrix[i][c] = None if matrix[i][c] != 0 else 0
                    for j in range(cols):
                        matrix[r][j] = None if matrix[r][j] != 0 else 0
        # 再次遍历，将None改为0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] is None:
                    matrix[r][c] = 0
```