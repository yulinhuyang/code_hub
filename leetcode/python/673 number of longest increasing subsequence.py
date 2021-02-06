## 题目描述

```
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

```

## 前置知识

- 动态规划

## 关键点解析

- [最长上升子序列问题](https://lucifer.ren/blog/2020/06/20/LIS/)
- dp[j][1] = dp[i][1] 容易忘记

## 代码

代码支持: Python

```py
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0] ->  LIS
        # dp[i][1] -> NumberOfLIS
        dp = [[1, 1] for i in range(n)]
        ans = [1, 1]
        longest = 1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if dp[i][0] + 1 > dp[j][0]:
                        dp[j][0] = dp[i][0] + 1
                        # 下面这行代码容易忘记，导致出错
                        dp[j][1] = dp[i][1]
                        longest = max(longest, dp[j][0])
                    elif dp[i][0] + 1 == dp[j][0]:
                        dp[j][1] += dp[i][1]
        return sum(dp[i][1] for i in range(n) if dp[i][0] == longest)