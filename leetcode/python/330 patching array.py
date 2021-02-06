## 题目描述

```
给定一个已排序的正整数数组 nums，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。

示例 1:

输入: nums = [1,3], n = 6
输出: 1 
解释:
根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
所以我们最少需要添加一个数字。
示例 2:

输入: nums = [1,5,10], n = 20
输出: 2
解释: 我们需要添加 [2, 4]。
示例 3:

输入: nums = [1,2,2], n = 5
输出: 0

```

## 前置知识

- 贪心
- 前缀和


#azl


## 代码

代码变量说明：

- furthest 表示区间右端点
- i 表示当前遍历到的数组索引
- ans 是需要返回的答案

```py
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        furthest = i = ans = 0
        while furthest < n:
            # 可覆盖到，直接用前缀和更新区间
            if i < len(nums) and nums[i] <= furthest + 1:
                furthest += nums[i] #  [1, furthest] -> [1, furthest + nums[i]]
                i += 1
            else:
                # 不可覆盖到，增加一个数 furthest + 1，并用前缀和更新区间
                furthest = 2 * furthest + 1 # [1, furthest] -> [1, furthest + furthest + 1]
                ans += 1
        return ans

```

如果你的区间信息是左闭右开的，代码可以这么写：

```py
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        furthest, i, ans = 1, 0, 0
        # 结束条件也要相应改变
        while furthest <= n:
            if i < len(nums) and nums[i] <= furthest:
                furthest += nums[i] #  [1, furthest) -> [1, furthest + nums[i])
                i += 1
            else:
                furthest = 2 * furthest # [1, furthest) -> [1, furthest + furthest)
                ans += 1
        return ans
```