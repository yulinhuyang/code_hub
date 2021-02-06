## 题目描述

```
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


```

## 前置知识

- 二叉搜索树
- 分治


def generateTrees(self, n):
    if n == 0: return []
    
    def helper(start, end):
        ls = []
        if start > end:
            ls.append(None)
            return ls
        if start == end:
            ls.append(TreeNode(start))
            return ls
        
        for i in range(start, end + 1):
            left = helper(start, i - 1)
            right = helper(i + 1, end)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    ls.append(root)
        return ls
    
    return helper(1, n)




//azl
Python3 Code:

```Python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []

        def generateTree(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                ls = generateTree(start, i - 1)
                rs = generateTree(i + 1, end)
                for l in ls:
                    for r in rs:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)

            return res

        return generateTree(1, n)
```
