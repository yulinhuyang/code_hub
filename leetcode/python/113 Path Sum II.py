## 题目描述

```
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

```

## 前置知识

- 回溯法

"""
Method 1
"""
def pathSum(self, root, sum):
    if not root: return []
    res = []

    def dfs(root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            dfs(root.left, sum - root.val, ls + [root.val], res)
        if root.right:
            dfs(root.right, sum - root.val, ls + [root.val], res)

    dfs(root, sum, [], res)
    return res

"""
Method 2
"""
def pathSum(self, root, sum):
    if not root: return []
    if not root.left and not root.right and root.val == sum: return [[root.val]]
    temp = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
    return [[root.val] + i for i in temp]



#azl

## 关键点解析

- 回溯法
- backtrack 解题公式


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        result = []

        def trace_node(pre_list, left_sum, node):
            new_list = pre_list.copy()
            new_list.append(node.val)
            if not node.left and not node.right:
                # 这个判断可以和上面的合并，但分开写会快几毫秒，可以省去一些不必要的判断
                if left_sum == node.val:
                    result.append(new_list)
            else:
                if node.left:
                    trace_node(new_list, left_sum-node.val, node.left)
                if node.right:
                    trace_node(new_list, left_sum-node.val, node.right)

        trace_node([], sum, root)
        return result
```


