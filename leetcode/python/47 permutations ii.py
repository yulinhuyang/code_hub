## 题目描述

```
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

```

## 前置知识

- 回溯法


#AZL

Python3 code:

```Python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """与46题一样，当然也可以直接调用itertools的函数，然后去重"""
        return list(set(itertools.permutations(nums)))

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """自己写回溯法，与46题相比，需要去重"""
        # 排序是为了方便去重
        nums.sort()
        res = []
        def backtrack(nums, pre_list):
            if len(nums) <= 0:
                res.append(pre_list)
            else:
                for i in range(len(nums)):
                    # 同样值的数字只能使用一次
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    p_list = pre_list.copy()
                    p_list.append(nums[i])
                    left_nums = nums.copy()
                    left_nums.pop(i)
                    backtrack(left_nums, p_list)
        backtrack(nums, [])
        return res
```