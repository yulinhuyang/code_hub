## 题目描述
和leetcode 102 基本是一样的，思路是完全一样的。

```
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

```

## 前置知识

- 队列


"""
simple bfs
"""

def zigzagLevelOrder(self, root):
    if not root: return []
    stack = [[root]]
    res = [[root.val]]
    level = 0
    while True:
        level += 1
        children = [child for node in stack[-1] for child in (node.left, node.right) if child]
        if not children: break
        temp = [node.val for node in children]
        if level % 2 == 1: temp.reverse()
        res.append(temp)
        stack.append(children)
    return res


//azl
