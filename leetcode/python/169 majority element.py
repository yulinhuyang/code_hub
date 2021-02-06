## 题目描述

```
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2


## 思路

符合直觉的做法是利用额外的空间去记录每个元素出现的次数，并用一个单独的变量记录当前出现次数最多的元素。

但是这种做法空间复杂度较高，有没有可能进行优化呢？ 答案就是用"投票算法"。

投票算法的原理是通过不断消除不同元素直到没有不同元素，剩下的元素就是我们要找的元素。


Python Code:

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 1, nums[0]
        for num in nums[1:]:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority
```