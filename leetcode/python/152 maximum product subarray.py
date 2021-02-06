## 题目描述
```
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```

## 前置知识

- 滑动窗口


//azl

Python3 Code:


```python


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max__dp = [1] * (n + 1)
        min_dp = [1] * (n + 1)
        ans = float('-inf')

        for i in range(1, n + 1):
            max__dp[i] = max(max__dp[i - 1] * nums[i - 1],
                             min_dp[i - 1] * nums[i - 1], nums[i - 1])
            min_dp[i] = min(max__dp[i - 1] * nums[i - 1],
                            min_dp[i - 1] * nums[i - 1], nums[i - 1])
            ans = max(ans, max__dp[i])
        return ans
  ```



##可以借助两个额外变量记录即可`。


Python3 Code:


```python

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = 1
        ans = float('-inf')

        for i in range(1, n + 1):
            temp = a
            a = max(a * nums[i - 1],
                    b * nums[i - 1], nums[i - 1])
            b = min(temp * nums[i - 1],
                    b * nums[i - 1], nums[i - 1])
            ans = max(ans, a)
        return ans
