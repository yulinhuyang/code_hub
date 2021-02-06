
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


## 前置知识

- 中序遍历


// Validate Binary Search Tree
// 时间复杂度O(n)，空间复杂度O(\logn)
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValidBST(root, LONG_MIN, LONG_MAX);
    }

    bool isValidBST(TreeNode* root, long long lower, long long upper) {
        if (root == nullptr) return true;

        return root->val > lower && root->val < upper
                && isValidBST(root->left, lower, root->val)
                && isValidBST(root->right, root->val, upper);
    }
};



//azl
## 关键点解析

- 二叉树的基本操作（遍历）
- 中序遍历一个二叉查找树（BST）的结果是一个有序数组
- 如果一个树遍历的结果是有序数组，那么他也是一个二叉查找树(BST)


### 中序遍历

C++ Code：

```c++
// 递归
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        TreeNode* prev = nullptr;
        return validateBstInorder(root, prev);
    }

private:
    bool validateBstInorder(TreeNode* root, TreeNode*& prev) {
        if (root == nullptr) return true;
        if (!validateBstInorder(root->left, prev)) return false;
        if (prev != nullptr && prev->val >= root->val) return false;
        prev = root;
        return validateBstInorder(root->right, prev);
    }
};

// 迭代
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        auto s = vector<TreeNode*>();
        TreeNode* prev = nullptr;
        while (root != nullptr || !s.empty()) {
            while (root != nullptr) {
                s.push_back(root);
                root = root->left;
            }
            root = s.back();
            s.pop_back();
            if (prev != nullptr && prev->val >= root->val) return false;
            prev = root;
            root = root->right;
        }
        return true;
    }
};
```
### 定义法
C++ Code：

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
// 递归
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return helper(root, LONG_MIN, LONG_MAX);
    }
private:
    bool helper(const TreeNode* root, long min, long max) {
        if (root == nullptr) return true;
        if (root->val >= max || root->val <= min) return false;
        return helper(root->left, min, root->val) && helper(root->right, root->val, max);
    }
};

// 循环
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) return true;
        auto ranges = queue<pair<long, long>>();
        ranges.push(make_pair(LONG_MIN, LONG_MAX));
        auto nodes = queue<const TreeNode*>();
        nodes.push(root);
        while (!nodes.empty()) {
            auto sz = nodes.size();
            for (auto i = 0; i < sz; ++i) {
                auto range = ranges.front();
                ranges.pop();
                auto n = nodes.front();
                nodes.pop();
                if (n->val >= range.second || n->val <= range.first) {
                    return false;
                }
                if (n->left != nullptr) {
                    ranges.push(make_pair(range.first, n->val));
                    nodes.push(n->left);
                }
                if (n->right != nullptr) {
                    ranges.push(make_pair(n->val, range.second));
                    nodes.push(n->right);
                }
            }
        }
        return true;
    }
};
```