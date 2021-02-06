## 题目描述

```
在一根无限长的数轴上，你站在0的位置。终点在target的位置。

每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。

返回到达终点需要的最小移动次数。

示例 1:

输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。
示例 2:

输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。
注意:

target是在[-10^9, 10^9]范围中的非零整数。


```

## 关键点解析

- 对元素进行分组，分组的依据是符号， 是`+` 或者 `-`
- 通过数学公式推导可以简化我们的求解过程，这需要一点`数学知识和数学意识`

## 代码(Python)

Python Code:

```py
class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        steps = 0
        while target > 0:
            steps += 1
            target -= steps
        if target & 1 == 0: return steps
        steps += 1
        if (target - steps) & 1 == 0: return steps
        return steps + 1


```