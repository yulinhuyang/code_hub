## 题目描述

```
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

// LeetCode, Maximum Depth of Binary Tree
// 时间复杂度O(n)，空间复杂度O(logn)
class Solution {
public:
    int maxDepth(TreeNode *root) {
        if (root == nullptr) return 0;

        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};



//azl
## 关键点解析

- 队列
- 队列中用 Null(一个特殊元素)来划分每层，或者在对每层进行迭代之前保存当前队列元素的个数（即当前层所含元素个数）
- 树的基本操作- 遍历 - 层次遍历（BFS）


//azl

C++ Code:

```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        auto q = vector<TreeNode*>();
        auto d = 0;
        q.push_back(root);
        while (!q.empty())
        {
            ++d;
            auto sz = q.size();
            for (auto i = 0; i < sz; ++i)
            {
                auto t = q.front();
                q.erase(q.begin());
                if (t->left != nullptr) q.push_back(t->left);
                if (t->right != nullptr) q.push_back(t->right);
            }
        }
        return d;
    }
};
```