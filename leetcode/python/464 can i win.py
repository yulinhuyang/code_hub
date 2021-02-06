## 题目描述

```
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？

你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

示例：

输入：
maxChoosableInteger = 10
desiredTotal = 11

输出：
false

解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

```

## 前置知识

- [动态规划](https://github.com/azl397985856/leetcode/blob/master/thinkings/dynamic-programming.md "动态规划")
- [回溯](https://github.com/azl397985856/leetcode/blob/master/thinkings/backtrack.md)


### 代码

代码支持：Python3

Python3 Code:

```py
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False
        # picked 用于保存当前已经选择过的数。
        # acc 表示当前累计的数字和
        def backtrack(picked, acc):
            if acc >= desiredTotal:
                return False
            if len(picked) == maxChoosableInteger:
                # 说明全部都被选了，没得选了，返回 False， 代表输了。
                return False
            for n in range(1, maxChoosableInteger + 1):
                if n not in picked:
                    picked.add(n)
                    # 对方有一种情况赢不了，我就选这个数字就能赢了，返回 true，代表可以赢。
                    if not backtrack(picked, acc + n):
                        picked.remove(n)
                        return True
                    picked.remove(n)
            return False

        # 初始化集合，用于保存当前已经选择过的数。
        return backtrack(set(), 0)
```
## 状态压缩 + 回溯
Python3 Code:

```python

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        @lru_cache(None)
        def dp(picked, acc):
            if acc >= desiredTotal:
                return False
            if picked == (1 << (maxChoosableInteger + 1)) - 1:
                return False
            for n in range(1, maxChoosableInteger + 1):
                if picked & 1 << n == 0:
                    if not dp(picked | 1 << n, acc + n):
                        return True
            return False

        return dp(0, 0)
```