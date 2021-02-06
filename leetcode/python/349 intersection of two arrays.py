## 题目描述

```
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
 

说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

```

## 前置知识

- hashtable

Python Code:

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited, result = {}, []
        for num in nums1:
            visited[num] = num
        for num in nums2:
            if num in visited:
                result.append(num)
                visited.pop(num)
        return result

    # 另一种解法：利用 Python 中的集合进行计算
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
```