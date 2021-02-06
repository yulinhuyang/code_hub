
## 题目描述
```
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

```

```python
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        candidates = [str(i) for i in range(1, n + 1)]

        while n != 0:
            facto = math.factorial(n - 1)
            # i 表示前面被我们排除的组数，也就是k所在的组的下标
            # k // facto 是不行的， 比如在 k % facto == 0的情况下就会有问题
            i = math.ceil(k / facto) - 1
            # 我们把candidates[i]加入到结果集，然后将其弹出candidates（不能重复使用元素）
            res += candidates[i]
            candidates.pop(i)
            # k 缩小了 facto *  i
            k -= facto * i
            # 每次迭代我们实际上就处理了一个元素，n 减去 1，当n == 0 说明全部处理完成，我们退出循环
            n -= 1
        return res
```