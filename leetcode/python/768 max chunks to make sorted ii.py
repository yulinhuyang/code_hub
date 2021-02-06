## 题目描述

```
这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。

arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

示例 1:

输入: arr = [5,4,3,2,1]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。
示例 2:

输入: arr = [2,1,3,4,4]
输出: 4
解释:
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。
注意:

arr的长度在[1, 2000]之间。
arr[i]的大小在[0, 10**8]之间。

```

## 前置知识

- 栈
- 队列

### 关键点

- 计数

### 代码

- 语言支持：Python

Python Code:

```py
class Solution(object):
    def maxChunksToSorted(self, arr):
        count_a = collections.defaultdict(int)
        count_b = collections.defaultdict(int)
        ans = 0

        for a, b in zip(arr, sorted(arr)):
            count_a[a] += 1
            count_b[b] += 1
            if count_a == count_b: ans += 1

        return ans


### 关键点

- 计数
- count 的边界条件

### 代码

- 语言支持：Python

Python Code:

```py
class Solution(object):
    class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.defaultdict(int)
        non_zero_cnt = 0
        ans = 0

        for a, b in zip(arr, sorted(arr)):
            if count[a] == -1: non_zero_cnt -= 1
            if count[a] == 0: non_zero_cnt += 1
            count[a] += 1
            if count[b] == 1: non_zero_cnt -= 1
            if count[b] == 0: non_zero_cnt += 1
            count[b] -= 1
            if non_zero_cnt == 0: ans += 1

        return ans


## 单调栈

Python Code:

```py
class Solution:
    def maxChunksToSorted(self, A: [int]) -> int:
        stack = []
        for a in A:
            # 遇到一个比栈顶小的元素，而前面的块不应该有比 a 小的
            # 而栈中每一个元素都是一个块，并且栈的存的是块的最大值，因此栈中比 a 小的值都需要 pop 出来
            if stack and stack[-1] > a:
                # 我们需要将融合后的区块的最大值重新放回栈
                # 而 stack 是递增的，因此 stack[-1] 是最大的
                cur = stack[-1]
                # 维持栈的单调递增
                while stack and stack[-1] > a: stack.pop()
                stack.append(cur)
            else:
                stack.append(a)
        # 栈存的是块信息，因此栈的大小就是块的数量
        return len(stack)
