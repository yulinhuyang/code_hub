## 题目描述

```
国际象棋中的骑士可以按下图所示进行移动：

```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu303ibcj305305p744.jpg)

```         

这一次，我们将 “骑士” 放在电话拨号盘的任意数字键（如上图所示）上，接下来，骑士将会跳 N-1 步。每一步必须是从一个数字键跳到另一个数字键。

每当它落在一个键上（包括骑士的初始位置），都会拨出键所对应的数字，总共按下 N 位数字。

你能用这种方式拨出多少个不同的号码？

因为答案可能很大，所以输出答案模 10^9 + 7。

 

示例 1：

输入：1
输出：10
示例 2：

输入：2
输出：20
示例 3：

输入：3
输出：46
 

提示：

1 <= N <= 5000

```

## 前置知识

- DFS
- 记忆化搜索



### 代码

```python
class Solution:
    def knightDialer(self, N: int) -> int:
        cnt = 0
        jump = [[4, 6], [6, 8], [7, 9], [4, 8], [
            0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        visited = dict()

        def helper(i, n):
            if (i, n) in visited: return visited[(i, n)]
            if n == 1:
                return 1
            cnt = 0
            for j in jump[i]:
                cnt += helper(j, n - 1)
            visited[(i, n)] = cnt
            return cnt
        for i in range(10):
            cnt += helper(i, N)
        return cnt % (10**9 + 7)
```
