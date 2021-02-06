## 题目描述

```
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

```

## 前置知识

- 中序遍历

# method 1: using recursion

def isValidBST1(self, root, lower = float('-inf'), upper = float('inf')):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root: return True
    if root.val <= lower or root.val >= upper: return False
    return self.isValidBST(root.left, lower, min(upper, root.val)) \
        and self.isValidBST(root.right, max(lower, root.val), upper)


# method 2: a proper BST should have this porperty: inorder traversal is increasing
def isValidBST2(self, root):
    inorder = []
    def helper(root):
        if root:
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
            
    helper(root)
    for i in range(len(inorder) - 1):
        if inorder[i + 1] <= inorder[i]: return False
    return True



##azl

定义法

Python Code:

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, area: tuple=(-float('inf'), float('inf'))) -> bool:
        """思路如上面的分析，用Python表达会非常直白
        :param root TreeNode 节点
        :param area tuple 取值区间
        """
        if root is None:
            return True

        is_valid_left = root.left is None or\
                   (root.left.val < root.val and area[0] < root.left.val < area[1])
        is_valid_right = root.right is None or\
                   (root.right.val > root.val and area[0] < root.right.val < area[1])

        # 左右节点都符合，说明本节点符合要求
        is_valid = is_valid_left and is_valid_right

        # 递归下去
        return is_valid\
            and self.isValidBST(root.left, (area[0], root.val))\
            and self.isValidBST(root.right, (root.val, area[1]))
 