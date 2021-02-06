## 题目描述

```
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

```

## 前置知识

- 二叉树
- 递归


// LeetCode, Binary Tree Inorder Traversal
// 使用栈，时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> result;
        stack<const TreeNode *> s;
        const TreeNode *p = root;

        while (!s.empty() || p != nullptr) {
            if (p != nullptr) {
                s.push(p);
                p = p->left;
            } else {
                p = s.top();
                s.pop();
                result.push_back(p->val);
                p = p->right;
            }
        }
        return result;
    }
};




// LeetCode, Binary Tree Inorder Traversal
// Morris中序遍历，时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> result;
        TreeNode *cur = root, *prev = nullptr;

        while (cur != nullptr) {
            if (cur->left == nullptr) {
                result.push_back(cur->val);
                prev = cur;
                cur = cur->right;
            } else {
                /* 查找前驱 */
                TreeNode *node = cur->left;
                while (node->right != nullptr && node->right != cur)
                    node = node->right;

                if (node->right == nullptr) { /* 还没线索化，则建立线索 */
                    node->right = cur;
                    /* prev = cur; 不能有这句，cur还没有被访问 */
                    cur = cur->left;
                } else {    /* 已经线索化，则访问节点，并删除线索  */
                    result.push_back(cur->val);
                    node->right = nullptr;
                    prev = cur;
                    cur = cur->right;
                }
            }
        }
        return result;
    }
};



//azl

## 关键点解析

- 二叉树的基本操作（遍历）
  > 不同的遍历算法差异还是蛮大的
- 如果非递归的话利用栈来简化操作

- 如果数据规模不大的话，建议使用递归

- 递归的问题需要注意两点，一个是终止条件，一个如何缩小规模

1. 终止条件，自然是当前这个元素是 null（链表也是一样）

2. 由于二叉树本身就是一个递归结构， 每次处理一个子树其实就是缩小了规模，
   难点在于如何合并结果，这里的合并结果其实就是`left.concat(mid).concat(right)`,
   mid 是一个具体的节点，left 和 right`递归求出即可`




C++ Code：

```c++
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<TreeNode*> s;
        vector<int> v;
        while (root != NULL || !s.empty()) {
            for (; root != NULL; root = root->left)
                s.push_back(root);
            v.push_back(s.back()->val);
            root = s.back()->right;
            s.pop_back();
        }
        return v;
    }
};