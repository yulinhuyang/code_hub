## 题目描述

```
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

```

## 前置知识

- 回溯法


// LeetCode, Path Sum II
// 时间复杂度O(n)，空间复杂度O(logn)
class Solution {
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<vector<int> > result;
        vector<int> cur; // 中间结果
        pathSum(root, sum, cur, result);
        return result;
    }
private:
    void pathSum(TreeNode *root, int gap, vector<int> &cur,
            vector<vector<int> > &result) {
        if (root == nullptr) return;

        cur.push_back(root->val);

        if (root->left == nullptr && root->right == nullptr) { // leaf
            if (gap == root->val)
                result.push_back(cur);
        }
        pathSum(root->left, gap - root->val, cur, result);
        pathSum(root->right, gap - root->val, cur, result);

        cur.pop_back();
    }
};


// LeetCode, Binary Tree Maximum Path Sum
// 时间复杂度O(n)，空间复杂度O(logn)
class Solution {
public:
    int maxPathSum(TreeNode *root) {
        max_sum = INT_MIN;
        dfs(root);
        return max_sum;
    }
private:
    int max_sum;
    int dfs(const TreeNode *root) {
        if (root == nullptr) return 0;
        int l = dfs(root->left);
        int r = dfs(root->right);
        int sum = root->val;
        if (l > 0) sum += l;
        if (r > 0) sum += r;
        max_sum = max(max_sum, sum);
        return max(r, l) > 0 ? max(r, l) + root->val : root->val;
    }
};


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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        auto ret = vector<vector<int>>();
        auto temp = vector<int>();
        backtrack(root, sum, ret, temp);
        return ret;
    }
private:
    void backtrack(const TreeNode* root, int sum, vector<vector<int>>& ret, vector<int>& tempList) {
        if (root == nullptr) return;
        tempList.push_back(root->val);
        if (root->val == sum && root->left == nullptr && root->right == nullptr) {
            ret.push_back(tempList);
        } else {
            backtrack(root->left, sum - root->val, ret, tempList);
            backtrack(root->right, sum - root->val, ret, tempList);
        }
        tempList.pop_back();
    }
};
```