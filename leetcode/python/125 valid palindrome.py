## 题目描述

```
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

```

## 前置知识

- 回文
- 双指针



#AZL

Python Code:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                break
        return right <= left

    def isPalindrome2(self, s: str) -> bool:
        """
        使用语言特性进行求解
        """
        s = ''.join(i for i in s if i.isalnum()).lower()
        return s == s[::-1]
```
