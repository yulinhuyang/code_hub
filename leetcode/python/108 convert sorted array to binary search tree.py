## 题目描述

```
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

```

## 关键点

- 找中点

Python Code:

 
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
 



##不开辟新空间

Python Code:
 
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.reBuild(nums, 0, len(nums)-1)
    
    def reBuild(self, nums, left, right):
         # 终止条件：
        if left > right:
            return
        # 建立当前子树的根节点
        mid = (left + right)//2
        root = TreeNode(nums[mid])
        # 左右子树的下层递归
        root.left = self.reBuild(nums, left, mid-1)
        root.right = self.reBuild(nums, mid+1, right)
        
        return root
```
