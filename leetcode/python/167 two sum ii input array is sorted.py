## 题目描述

这是leetcode头号题目`two sum`的第二个版本，难度简单。

```
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

```

## 前置知识

- 双指针

## 思路

由于题目没有对空间复杂度有求，用一个hashmap  存储已经访问过的数字即可。

假如题目空间复杂度有要求，由于数组是有序的，只需要双指针即可。一个left指针，一个right指针，
如果left + right 值 大于target 则 right左移动， 否则left右移，代码见下方python code。

> 如果数组无序，需要先排序（从这里也可以看出排序是多么重要的操作）


## 关键点解析

- 由于是有序的，因此双指针更好



#azl
Python Code:

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for index, number in enumerate(numbers):
            if target - number in visited:
                return [visited[target-number], index+1]
            else:
                visited[number] = index + 1

# 双指针思路实现
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
 