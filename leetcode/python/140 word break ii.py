## 题目描述

```
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]


## 前置知识

- 回溯
- 笛卡尔积


暴力回溯

Python3 Code:

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        n = len(s)

        def backtrack(temp, start):
            if start == n: ans.append(temp[1:])
            for i in range(start, n):
                if s[start:i + 1] in wordDict:
                    backtrack(temp + " " + s[start:i + 1], i + 1)
        backtrack('', 0)
        return ans
```

## 笛卡尔积优化


Python3 Code:

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        @lru_cache(None)
        def backtrack(start):
            ans = []
            if start == n:
                ans.append('')
            for i in range(start, n):
                if s[start:i + 1] in wordDict:
                    if start == 0: temp = s[start:i + 1]
                    else: temp = " " + s[start:i + 1]
                    ps = backtrack(i + 1)
                    for p in ps:
                        ans.append(temp + p)
            return ans
        return backtrack(0)
```