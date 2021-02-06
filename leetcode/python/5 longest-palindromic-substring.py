
## 题目描述

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设  s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

## 前置知识

- 回文





//azl

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        res = s[0]
        def extend(i, j, s):
            while(i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            return s[i + 1:j]

        for i in range(n - 1):
            e1 = extend(i, i, s)
            e2 = extend(i, i + 1, s)
            if max(len(e1), len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2
        return res
```