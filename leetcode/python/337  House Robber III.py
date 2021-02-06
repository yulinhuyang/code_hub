## 题目描述

```
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.


```

## 前置知识

- 二叉树
- 动态规划

"""
Answe inspired by the post from here: 
https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
"""
# Method 1: dynamic programming solution:
def rob1(self, root):
        lookup = {}
        def helper(root):
            if not root: return 0
            if root in lookup: return lookup[root]
            val = 0
        
            if root.left:
                val += helper(root.left.left) + helper(root.left.right)
            if root.right:
                val += helper(root.right.left) + helper(root.right.right)
            val = max(val + root.val, helper(root.left) + helper(root.right))
            lookup[root] = val
            return val
        return helper(root)

# Method 2: Greedy approach:
def rob2(self, root):
    def helper(root):
        if not root: return [0, 0]
        left, right = helper(root.left), helper(root.right)
        not_robbed = max(left) + max(right)
        robbed = root.val + left[0] + right[0]
        return [not_robbed, robbed]
    return max(helper(root))


##
Python Code:

```python

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            [l_rob, l_not_rob] = dfs(node.left)
            [r_rob, r_not_rob] = dfs(node.right)
            return [node.val + l_not_rob + r_not_rob, max([l_rob, l_not_rob]) +  max([r_rob, r_not_rob])]
        return max(dfs(root))


# @lc code=end
