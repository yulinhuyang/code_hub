## 题目描述

```

给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1：

输入：[1,2,3]

       1
      / \
     2   3

输出：6
示例 2：

输入：[-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出：42

```

## 前置知识

- 递归

##基本算法就是不断调用递归函数，然后在调用过程中不断计算和更新 MaxPath，最后在主函数中将 MaxPath 返回即可。
- Python

```py

class Solution:
    ans = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            self.ans = max(self.ans, max(l,0) + max(r, 0) + node.val)
            return max(l, r, 0) + node.val
        helper(root)
        return self.ans