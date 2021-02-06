## 题目描述

```
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

```

## 前置知识

#### 解法二 - 前缀和 + 暴力

_Python3 code_ `(TLE)`

```python
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = -sys.maxsize
        sum = 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                maxSum = max(maxSum, sum)

        return maxSum


#### 解法三 - 优化前缀和
_Python3 code_

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        minSum = sum = 0
        for i in range(n):
            sum += nums[i]
            maxSum = max(maxSum, sum - minSum)
            minSum = min(minSum, sum)

        return maxSum


#### 解法四 - 分治法
```python
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)
    def helper(self, nums, l, r):
        if l > r:
            return -sys.maxsize
        mid = (l + r) // 2
        left = self.helper(nums, l, mid - 1)
        right = self.helper(nums, mid + 1, r)
        left_suffix_max_sum = right_prefix_max_sum = 0
        sum = 0
        for i in reversed(range(l, mid)):
            sum += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum, sum)
        sum = 0
        for i in range(mid + 1, r + 1):
            sum += nums[i]
            right_prefix_max_sum = max(right_prefix_max_sum, sum)
        cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
        return max(cross_max_sum, left, right)
```


#### 解法五 - 动态规划

_Python3 code_

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum_ending_curr_index = max_sum = nums[0]
        for i in range(1, n):
            max_sum_ending_curr_index = max(max_sum_ending_curr_index + nums[i], nums[i])
            max_sum = max(max_sum_ending_curr_index, max_sum)

        return max_sum
```
