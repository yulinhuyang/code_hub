## 题目描述

```
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

```

## 前置知识

- 动态规划

//AZL

## 暴力（超时）

```py
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0

        def validCnt(start):
            # cnt 为 ) 的数量减去 ( 的数量
            cnt = 0
            ans = 0
            for i in range(start, n):
                if s[i] == '(':
                    cnt += 1
                if s[i] == ')':
                    cnt -= 1
                if cnt < 0:
                    return i - start
                if cnt == 0:
                    ans = max(ans, i - start + 1)
            return ans
        for i in range(n):
            ans = max(ans, validCnt(i))

        return ans
```

**复杂度分析**

- 时间复杂度：$$O(N^2)$$
- 空间复杂度：$$O(1)$$


## 栈
Python Code:

```py

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
```


## O(1) 空间

### 思路

我们可以采用解法一中的计数方法。

- 从左到右遍历一次，并分别记录左右括号的数量 left 和 right。
- 如果 right > left ，说明截止上次可以匹配的点到当前点这一段无法匹配，重置 left 和 right 为 0
- 如果 right == left, 此时可以匹配，此时有效括号长度为 left + right，我们获得一个局部最优解。如果其比全局最优解大，我们更新全局最优解

值得注意的是，对形如 `(((()` 这样的，更新全局最优解的逻辑永远无法执行。一种方式是再从右往左遍历一次即可，具体看代码。



Python3 Code:

```py
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = l = r = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, l + r)
            if r > l:
                l = r = 0
        l = r = 0
        for c in s[::-1]:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, l + r)
            if r < l:
                l = r = 0

        return ans




## 动态规划
Python3 Code:

该题需要我们找到最长的有效括号对, 我们首先想到的就是定义**dp[i]为前 i 个字符串的最长有效括号对长度**, 但是随后我们会发现, 这样的定义, 我们无法找到 dp[i]和 dp[i-1]的任何关系.
所以, 我们需要重新找一个新的定义: 定义**dp[i]为以第 i 个字符结尾的最长有效括号对长度**. 然后, 我们通过下面这个例子找一下 dp[i]和 dp[i-1]之间的关系.

```py
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mlen = 0
        slen = len(s)
        dp = [0] * (slen + 1)
        for i in range(1, len(s) + 1):
            # 有效的括号对不可能会以'('结尾的
            if s[i - 1] == '(':
                continue

            left_paren = i - 2 - dp[i - 1]
            if left_paren >= 0 and s[left_paren] == '(':
                dp[i] = dp[i - 1] + 2

                # 拼接有效括号对
                if dp[i - dp[i]]:
                    dp[i] += dp[i - dp[i]]

                # 更新最大有效扩对长度
                if dp[i] > mlen:
                    mlen = dp[i]

        return mlen
```


