## 题目描述

```
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

```

## 前置知识

- 二叉搜索树
- 分治


def numTrees(self, n):
    if n == 1: return 1
    res = [1, 1]
    for i in range(2, n + 1):
        val = 0
        for j in range(i):
            val += res[j] * res[i - j - 1]
        res.append(val)
    return res[n]


//azl

Python3 Code:

```Python
class Solution:
    visited = dict()

    def numTrees(self, n: int) -> int:
        if n in self.visited:
            return self.visited.get(n)
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        self.visited[n] = res
        return res
```