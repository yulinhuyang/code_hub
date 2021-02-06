
## 题目描述

```
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

```

## 前置知识

- 回溯法

//AZL

Python3 Code:

```python
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        :param list nums
        """
        # 第一步，从后往前，找到下降点
        down_index = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                down_index = i
                break
        # 如果没有下降点，重新排列
        if down_index is None:
            nums.reverse()
        # 如果有下降点
        else:
            # 第二步，从后往前，找到比下降点大的数，对换位置
            for i in range(len(nums)-1, i, -1):
                if nums[down_index] < nums[i]:
                    nums[down_index], nums[i] = nums[i], nums[down_index]
                    break
            # 第三部，重新排列下降点之后的数
            i, j = down_index+1, len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
```