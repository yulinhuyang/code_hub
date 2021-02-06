## 题目描述

```
我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。

原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。

最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。

 

示例 1:
输入: "(123)"
输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
示例 2:
输入: "(00011)"
输出:  ["(0.001, 1)", "(0, 0.011)"]
解释:
0.0, 00, 0001 或 00.01 是不被允许的。
示例 3:
输入: "(0123)"
输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
示例 4:
输入: "(100)"
输出: [(10, 0)]
解释:
1.0 是不被允许的。
 

提示:

4 <= S.length <= 12.
S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。

```

## 前置知识

- 回溯
- 笛卡尔积


先将题目简化一下，不考虑题目给的那些限制， 只要将其分割成逗号分割的两部分即可，不用考虑是否是有效的（比如不能是 001 等）。

那么代码大概是：

Python3 Code:

```python
class Solution:

    def subset(self, s: str):
        ans = []
        for i in range(1, len(s)):
            ans.append(s[:i] + "." + s[i:])
        ans.append(s)
        return ans

    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        s = s[1:-1]
        for i in range(1, len(s)):
            x = self.subset(s[:i])
            y = self.subset(s[i:])
            for i in x:
                for j in y:
                    ans.append('(' + i + ', ' + j + ')')
        return ans


## 关键点

- 笛卡尔积优化

## 代码

代码支持：Python3

```python
class Solution:
    # "123" => ["1.23", "12.3", "123"]
    def subset(self, s: str):
        ans = []

        #  带小数点的
        for i in range(1, len(s)):
            # 不允许 00.111， 0.0，01.1，1.0
            if s[0] == '0' and i > 1:
                continue
            if s[-1] == '0':
                continue
            ans.append(s[:i] + "." + s[i:])
        # 不带小数点的（不允许 001）
        if s == '0' or not s.startswith('0'):
            ans.append(s)
        return ans

    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        s = s[1:-1]
        for i in range(1, len(s)):
            x = self.subset(s[:i])
            y = self.subset(s[i:])
            for i in x:
                for j in y:
                    ans.append('(' + i + ', ' + j + ')')
        return ans

 