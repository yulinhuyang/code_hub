## 题目描述

```
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

```

## 前置知识

- 栈
- 括号匹配


### 代码

代码支持：Python

Python：

```py
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                repeatStr = ''
                repeatCount = ''
                while stack and stack[-1] != '[':
                    repeatStr = stack.pop() + repeatStr
                # pop 掉 "["
                stack.pop()
                while stack and stack[-1].isnumeric():
                    repeatCount = stack.pop() + repeatCount
                stack.append(repeatStr * int(repeatCount))
            else:
                stack.append(c)
        return "".join(stack)
```



## 递归

### 代码

```py
class Solution:

    def decodeString(self, s: str) -> str:
        def dfs(start):
            repeat_str = repeat_count = ''
            while start < len(s):
                if s[start].isnumeric():
                    repeat_count += s[start]
                elif s[start] == '[':
                    # 更新指针
                    start, t_str = dfs(start + 1)
                    # repeat_count 仅作用于 t_str，而不作用于当前的 repeat_str
                    repeat_str = repeat_str + t_str * int(repeat_count)
                    repeat_count = ''
                elif s[start] == ']':
                    return start, repeat_str
                else:
                    repeat_str += s[start]
                start += 1
            return repeat_str
        return dfs(0)
```