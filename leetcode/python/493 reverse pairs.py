## 题目描述

```
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。

```

## 前置知识

- 归并排序
- 逆序数
- 分治

## 分治法
Python3 Code:

```python
class Solution(object):
    def reversePairs(self, nums):
        self.cnt = 0

        def mergeSort(lst):
            L = len(lst)
            if L <= 1:
                return lst
            return mergeTwo(mergeSort(lst[:L//2]), mergeSort(lst[L//2:]))

        def mergeTwo(left, right):
            l = r = 0
            while l < len(left) and r < len(right):
                if left[l] <= 2 * right[r]:
                    l += 1
                else:
                    self.cnt += len(left) - l
                    r += 1
            return sorted(left+right)

        mergeSort(nums)
        return self.cnt

```
