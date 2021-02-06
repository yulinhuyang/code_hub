
## 题目描述

给定一个正整数  n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例  2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设  n  不小于 2 且不大于 58。

## 前置知识

- 递归
- 动态规划


## 考虑优化

如上，我们可以考虑使用记忆化递归的方式来解决。只是用一个 hashtable 存储计算过的值即可。

```python
class Solution:
    @lru_cache()
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        res = 0
        for i in range(1, n):
            res = max(res, max(i * self.integerBreak(n - i),i * (n - i)))
        return res
```


```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])
        return dp[n]
```
