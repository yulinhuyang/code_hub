## 题目描述

```
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

进阶：

你能在线性时间复杂度内解决此题吗？

 

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

```

## 前置知识

- 队列
- 滑动窗口



因此思路就是用一个双端队列来保存`接下来的滑动窗口可能成为最大值的数`。

具体做法：

- 入队列
- 移除失效元素，失效元素有两种

## 关键点解析

- 双端队列简化时间复杂度

- 滑动窗口

Python3:

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # 本质就是单调队列
        ans = []
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]: q.pop() # 维持单调性
            while q and i - q[0] >= k: q.popleft() # 移除失效元素
            q.append(i)
            if i >= k - 1: ans.append(nums[q[0]])
        return ans