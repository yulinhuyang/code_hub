## 题目描述

```
给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。

返回 N 的长度。如果不存在这样的 N，就返回 -1。

 

示例 1：

输入：1
输出：1
解释：最小的答案是 N = 1，其长度为 1。
示例 2：

输入：2
输出：-1
解释：不存在可被 2 整除的正整数 N 。
示例 3：

输入：3
输出：3
解释：最小的答案是 N = 111，其长度为 3。
 

提示：

1 <= K <= 10^5

```

## 前置知识

- 循环节

## 代码

```python
#
# @lc app=leetcode.cn id=1015 lang=python3
#
# [1015] 可被 K 整除的最小整数
#

# @lc code=start


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 10 in [2, 4, 5, 6, 8]:
            return - 1
        seen = set()
        mod = 0
        for i in range(1, K + 1):
            mod = (mod * 10 + 1) % K
            if mod in seen:
                return -1
            if mod == 0:
                return ix
            seen.add(mod)
```