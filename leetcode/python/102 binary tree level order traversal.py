## 题目描述
```
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
```

## 前置知识

- 队列



## 关键点解析

- 队列

- 队列中用Null(一个特殊元素)来划分每层

- 树的基本操作- 遍历 - 层次遍历（BFS）

- 注意塞入null的时候，判断一下当前队列是否为空，不然会无限循环


Python Code：
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """递归法"""
        if root is None:
            return []
        
        result = []
        
        def add_to_result(level, node):
            """递归函数
            :param level int 当前在二叉树的层次
            :param node TreeNode 当前节点
            """
            if level > len(result) - 1:
                result.append([])
                
            result[level].append(node.val)
            if node.left:
                add_to_result(level+1, node.left)
            if node.right:
                add_to_result(level+1, node.right)
        
        add_to_result(0, root)
        return result