## 题目描述

```
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


```

![42.trapping-rain-water-1](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu8i4s97j30bg04hmx3.jpg)

```
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

```

## 前置知识

- 空间换时间
- 双指针
- 单调栈


#AZL

## 双数组
Python Code:

```python
class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = [0] * (n + 1), [0] * (n + 1)
        ans = 0
        for i in range(1, len(heights) + 1):
            l[i] = max(l[i - 1], heights[i - 1])
        for i in range(len(heights) - 1, 0, -1):
            r[i] = max(r[i + 1], heights[i])
        for i in range(len(heights)):
            ans += max(0, min(l[i + 1], r[i]) - heights[i])
        return ans
```


#AZL 双指针
### 思路

上面代码比较好理解，但是需要额外的 N 的空间。从上面解法可以看出，我们实际上只关心左右两侧较小的那一个，并不需要两者都计算出来。具体来说：

- 如果 l[i + 1] < r[i] 那么 最终积水的高度由 i 的左侧最大值决定。
- 如果 l[i + 1] >= r[i] 那么 最终积水的高度由 i 的右侧最大值决定。

因此我们不必维护完整的两个数组，而是可以只进行一次遍历，同时维护左侧最大值和右侧最大值，使用常数变量完成即可。这是一个典型的双指针问题，



Python Code:

```python
class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        l_max = r_max = 0
        l, r = 0, n - 1
        ans = 0
        while l < r:
            if heights[l] < heights[r]:
                if heights[l] < l_max:
                    ans += l_max - heights[l]
                else:
                    l_max = heights[l]
                l += 1
            else:
                if heights[r] < r_max:
                    ans += r_max - heights[r]
                else:
                    r_max = heights[r]
                r -= 1
        return ans
```