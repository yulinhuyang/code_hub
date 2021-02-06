## 题目描述

```
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

```

## 前置知识

- 排序
- 双指针
- 二分法
- 三角形边的关系



### 关键点解析

- 三角形边的关系
- 三层循环确定三个线段

### 代码

代码支持: Python

```py
class Solution:
    def is_triangle(self, a, b, c):
        if a == 0 or b == 0 or c == 0: return False
        if a + b > c and a + c > b and b + c > a: return True
        return False
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if self.is_triangle(nums[i], nums[j], nums[k]): ans += 1

        return ans


### 关键点分析

- 排序

### 代码

```py
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        for i in range(n - 2):
            if nums[i] == 0: continue
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k - j - 1
        return ans
```
