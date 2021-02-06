## 题目描述

```
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
 

注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。


## 排序

```py


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda a: a[0])

        def intersected(a, b):
            if a[0] > b[1] or a[1] < b[0]:
                return False
            return True

        def mergeTwo(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        i = 0
        while i < len(intervals) - 1:
            cur = intervals[i]
            next = intervals[i + 1]
            if intersected(cur, next):
                intervals[i] = None
                intervals[i + 1] = mergeTwo(cur, next)
            i += 1

        return list(filter(lambda x: x, intervals))


## 一次扫描
算法描述：

- 从左往右遍历，对于遍历到的每一项姑且称之为 interval。

  - 如果 interval 在 newInterval 左侧不相交，那么不断 push interval 到 ans。
  - 否则不断合并 interval 和 newInterval，直到合并之后的新区间和 interval 不重合，将合并后的**大区间** push 到 ans。融合的方法参考上方 56 题。
  - 后面不可能发生重合了（题目保证了），因此直接将后面的 interval 全部添加到 ans 即可

- 最终返回 ans



```py
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n = 0, len(intervals)
        ans = []

        def intersected(a, b):
            if a[0] > b[1] or a[1] < b[0]:
                return False
            return True
        # 前
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        # 中
        while i < n and intersected(intervals[i], newInterval):
            newInterval = [min(intervals[i][0], newInterval[0]),
                           max(intervals[i][1], newInterval[1])]
            i += 1
        ans.append(newInterval)
        # 后
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans
