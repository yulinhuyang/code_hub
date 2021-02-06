## 题目描述

```

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

```

## 前置知识

- 数组


# Method 1: Binary Search on each row, if the first element of the row is already bigger than target, then skip
# Time Complexity: O(mlogn)
def searchMatrix1(self, matrix, target):
    def helper(low, high, row):
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] < target: low = mid + 1
            elif matrix[row][mid] > target: high = mid - 1
            else: return True
        return False
    
    if not matrix or not matrix[0]: return False
    for i in range(len(matrix)):
        if matrix[i][0] > target: return False
        elif matrix[i][0] == target: return True
        if helper(0, len(matrix[i]) - 1, i): return True
    return False

# Method 2: compare the element with top-right corner, and reduce the search range
# Time complexity: O(m + n)
def searchMatrix2(self, matrix, target):
    if not matrix or not matrix[0]: return False
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target: col -= 1
        elif matrix[row][col] < target: row += 1
        else: return True
    return False


//azl

Python Code:

```python
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        i = m - 1
        j = 0

        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
```