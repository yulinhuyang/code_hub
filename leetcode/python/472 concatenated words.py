## 题目描述

```
给定一个不含重复单词的列表，编写一个程序，返回给定单词列表中所有的连接词。

连接词的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。

示例:

输入: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

输出: ["catsdogcats","dogcatsdog","ratcatdogcat"]

解释: "catsdogcats"由"cats", "dog" 和 "cats"组成;
     "dogcatsdog"由"dog", "cats"和"dog"组成;
     "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
说明:

给定数组的元素总数不超过 10000。
给定数组中元素的长度总和不超过 600000。
所有输入字符串只包含小写字母。
不需要考虑答案输出的顺序。
```

## 前置知识

- [前缀树](../thinkings/trie.md)



## 关键点分析

- 前缀树

## 代码

代码支持：Python3

Python3 Code:

```python
class Trie:

    def __init__(self):
        self.Trie = {}
        self.visited = {}

    def insert(self, word):
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1

    def cntWords(self, word):
        if not word:
            return 0
        if word in self.visited:
            return self.visited[word]
        curr = self.Trie
        res = float('-inf')

        for i, w in enumerate(word):
            if w not in curr:
                return res
            curr = curr[w]
            if '#' in curr:
                res = max(res, 1 + self.cntWords(word[i + 1:]))
        self.visited[word] = res
        return res


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.trie = Trie()
        res = []

        for word in words:
            self.trie.insert(word)
        for word in words:
            if self.trie.cntWords(word) >= 2:
                res.append(word)
        return res