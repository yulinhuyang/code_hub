## 题目描述

```
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.

```

## 前置知识

- 递归



"""
Method 1: dfs
"""
def sumNumbers(self, root):
    if not root: return 0
    stack, res = [(root, root.val)], 0
    while stack:
        node, value = stack.pop()
        if not node.left and not node.right:
            res += value
        if node.right:
            stack.append((node.right, value * 10 + node.right.val))
        if node.left:
            stack.append((node.left, value * 10 + node.left.val))
    return res
    
    
    
"""
Method 2: recursive solution
"""
def sumNumbers(self, root):
    return self.helper(root, 0)

def helper(self, node, s):
    if not node: return 0
    if not node.left and not node.right: return s * 10 + node.val
    return self.helper(node.left, s * 10 + node.val) + \
            self.helper(node.right, s * 10 + node.val)



#AZL
Python Code:

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def helper(node, cur_val):
            if not node: return 0
            next_val = cur_val * 10 + node.val

            if not (node.left or node.right):
                return next_val

            left_val = helper(node.left, next_val)
            right_val = helper(node.right, next_val)

            return left_val + right_val

        return helper(root, 0)
```


### 描述

使用两个队列：
1. 当前和队列：保存上一层每个结点的当前和（比如49和40）
2. 结点队列：保存当前层所有的非空结点

每次循环按层处理结点队列。处理步骤：
1. 从结点队列取出一个结点
2. 从当前和队列将上一层对应的当前和取出来
3. 若左子树非空，则将该值乘以10加上左子树的值，并添加到当前和队列中
4. 若右子树非空，则将该值乘以10加上右子树的值，并添加到当前和队列中
5. 若左右子树均为空时，将该节点的当前和加到返回值中


Python Code:

```python
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        result = 0
        node_queue, sum_queue = [root], [root.val]
        while node_queue:
            for i in node_queue:
                cur_node = node_queue.pop(0)
                cur_val = sum_queue.pop(0)
                if cur_node.left:
                    node_queue.append(cur_node.left)
                    sum_queue.append(cur_val * 10 + cur_node.left.val)
                if cur_node.right:
                    node_queue.append(cur_node.right)
                    sum_queue.append(cur_val * 10 + cur_node.right.val)
                if not (cur_node.left or cur_node.right):
                    result += cur_val
        return result
```