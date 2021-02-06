## 题目描述

```
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

```

## 前置知识

- 回溯法


#AZL
Python3 Code:

```Python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """itertools库内置了这个函数"""
        import itertools
        return itertools.permutations(nums)

    def permute2(self, nums: List[int]) -> List[List[int]]:
        """自己写回溯法"""
        res = []
        def backtrack(nums, pre_list):
            if len(nums) <= 0:
                res.append(pre_list)
            else:
                for i in nums:
                    # 注意copy一份新的调用，否则无法正常循环
                    p_list = pre_list.copy()
                    p_list.append(i)
                    left_nums = nums.copy()
                    left_nums.remove(i)
                    backtrack(left_nums, p_list)
        backtrack(nums, [])
        return res

    def permute3(self, nums: List[int]) -> List[List[int]]:
        """回溯的另一种写法"""
        res = []
        length = len(nums)
        def backtrack(start=0):
            if start == length:
                # nums[:] 返回 nums 的一个副本，指向新的引用，这样后续的操作不会影响已经已知解
                res.append(nums[:])
            for i in range(start, length):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack()
        return res
