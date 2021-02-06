## 题目描述

```
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

```

## 前置知识

- [前缀树](../thinkings/trie.md)
- [深度优先遍历](../thinkings/DFS.md)
- [小岛专题](../thinkings/island.md)
- 剪枝

Python3 Code：

关于 Trie 的代码:

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        curr = self.Trie
        for w in prefix:
            if w not in curr:
                return False
            curr = curr[w]
        return True
```

主逻辑代码：

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        trie = Trie()
        seen = None
        res = set()
        for word in words:
            trie.insert(word)

        def dfs(s, i, j):
            if (i, j) in seen or i < 0 or i >= m or j < 0 or j >= n or not trie.startsWith(s):
                return
            s += board[i][j]
            seen[(i, j)] = True

            if s in words:
                res.add(s)
            dfs(s, i + 1, j)
            dfs(s, i - 1, j)
            dfs(s, i, j + 1)
            dfs(s, i, j - 1)

            del seen[(i, j)]

        for i in range(m):
            for j in range(n):
                seen = dict()
                dfs("", i, j)
        return list(res)
```