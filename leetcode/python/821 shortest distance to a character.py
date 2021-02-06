## 题目描述

```
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:

- 字符串 S 的长度范围为 [1, 10000]。
- C 是一个单字符，且保证是字符串 S 里的字符。
- S 和 C 中的所有字母均为小写字母。

```

## 前置知识

- 数组的遍历(正向遍历和反向遍历)


```py
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = [10000] * len(S)
        stack = []
        for i in range(len(S)):
            while stack and S[i] == C:
                ans[stack.pop()] = i - stack[-1]
            if S[i] != C:stack.append(i)
            else: ans[i] = 0
        for i in range(len(S) - 1, -1, -1):
            while stack and S[i] == C:
                ans[stack.pop()] = min(ans[stack[-1]], stack[-1] - i)
            if S[i] != C:stack.append(i)
            else: ans[i] = 0

        return ans



优化
Python3 Code：

```py
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        pre = -10000
        ans = []

        for i in range(len(S)):
            if S[i] == C: pre = i
            ans.append(i - pre)
        pre = 20000
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: pre = i
            ans[i] = min(ans[i], pre - i)
        return ans
```