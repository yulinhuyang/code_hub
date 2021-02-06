## 题目描述

```
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

```

## 前置知识

- hashmap


Python Code:

```py
class Solution:
    def longestConsecutive(self, A: List[int]) -> int:
        seen = set(A)
        ans = 0
        for a in A:
            t = a
            #  if 的作用是剪枝
            if t + 1 not in seen:
                while t - 1 in seen:
                    t -= 1
            ans = max(ans, a - t + 1)
        return ans
```