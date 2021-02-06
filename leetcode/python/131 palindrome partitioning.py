## 题目描述

```
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

```

## 前置知识

- 回溯法




```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """回溯法"""

        res = []

        def helper(s, tmp):
            """
            如果是空字符串，说明已经处理完毕
            否则逐个字符往前测试，判断是否是回文
            如果是，则处理剩余字符串，并将已经得到的列表作为参数
            """
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res
```