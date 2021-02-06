## 题目描述

```
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

```

## 前置知识

- 队列


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
    vector<int> rightSideView(TreeNode* root) {
        auto ret = vector<int>();
        if (root == nullptr) return ret;
        auto q = queue<const TreeNode*>();
        q.push(root);
        while (!q.empty()) {
            auto sz = q.size();
            for (auto i = 0; i < sz; ++i) {
                auto n = q.front();
                q.pop();
                if (n->left != nullptr ) q.push(n->left);
                if (n->right != nullptr ) q.push(n->right);
                if (i == sz - 1) ret.push_back(n->val);
            }
        }
        return ret;
    }
};