## 题目描述

```
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

```

## 前置知识

- DFS
- 回溯法


Python Code:

```py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(l, r, s):
            if l > n or r > n: return
            if (l == r == n): res.append(s)
            if l < r: return
            # 加一个左括号
            dfs(l + 1, r, s + '(')
            # 加一个右括号
            dfs(l, r + 1, s + ')')
        dfs(0, 0, '')
        return res
```