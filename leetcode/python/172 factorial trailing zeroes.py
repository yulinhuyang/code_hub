## 题目描述

```
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

```

## 前置知识

- [递归]


Python Code:

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n = n // 5
            count += n
        return count


# 递归
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        return n // 5 + self.trailingZeroes(n // 5)
```