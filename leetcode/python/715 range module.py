## 题目描述

```
Range 模块是跟踪数字范围的模块。你的任务是以一种有效的方式设计和实现以下接口。

addRange(int left, int right) 添加半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true。
removeRange(int left, int right) 停止跟踪区间 [left, right) 中当前正在跟踪的每个实数。
 

示例：

addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true （区间 [10, 14) 中的每个数都正在被跟踪）
queryRange(13, 15): false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
queryRange(16, 17): true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
 

提示：

半开区间 [left, right) 表示所有满足 left <= x < right 的实数。
对 addRange, queryRange, removeRange 的所有调用中 0 < left < right < 10^9。
在单个测试用例中，对 addRange 的调用总数不超过 1000 次。
在单个测试用例中，对  queryRange 的调用总数不超过 5000 次。
在单个测试用例中，对 removeRange 的调用总数不超过 1000 次。

```

## 前置知识

- 区间查找问题
- [二分查找]


## 关键点解析

- 二分查找的灵活使用（最左插入和最右插入）
- 将区间一维化处理

## 代码

为了明白 Python 代码的含义，你需要明白 bisect_left 和 bisect_right

Python3 Code:

```py
class RangeModule(object):
    def __init__(self):
        # [1,2,3,5,8,12]
        self.ranges = []

    def overlap(self, left, right, is_odd):
        i = bisect_left(self.ranges, left)
        j = bisect_right(self.ranges, right)
        merge = []
        if i & 1 == int(is_odd):
            merge.append(left)
        if j & 1 == int(is_odd):
            merge.append(right)
        # 修改 ranges 的 [i:j-1] 部分
        self.ranges[i:j] = merge

    def addRange(self, left, right):
        # [1,2,3,5,8,12]， 代入 left = 3, right = 5，此时需要保持不变， 就不难知道应该用 bisect_left 还是 bisect_right
        return self.overlap(left, right, False)

    def removeRange(self, left, right):
        # [1,2,3,5,8,12]， 代入 left = 3, right = 5，此时需要为 [1,2,8,12]， 就不难知道应该用 bisect_left 还是 bisect_right
        return self.overlap(left, right, True)

    def queryRange(self, left, right):
        # [1,2,3,5,8,12]， 代入 left = 3, right = 5，此时需要返回 true， 就不难知道应该用 bisect_left 还是 bisect_right
        i = bisect_right(self.ranges, left)
        j = bisect_left(self.ranges, right)
        return i & 1 == 1 and i == j  # 都在一个区间内

```

addRange 和 removeRange 中使用 bisect_left 找到左端点 l，使用 bisect_right 找到右端点，这样将 [left, right) 更新到区间 [l, r - 1] 即可。
