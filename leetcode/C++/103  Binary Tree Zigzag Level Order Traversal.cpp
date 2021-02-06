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



// LeetCode, Binary Tree Zigzag Level Order Traversal
// 递归版，时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
        vector<vector<int>> result;
        traverse(root, 1, result, true);
        return result;
    }

    void traverse(TreeNode *root, size_t level, vector<vector<int>> &result,
            bool left_to_right) {
        if (!root) return;

        if (level > result.size())
            result.push_back(vector<int>());

        if (left_to_right)
            result[level-1].push_back(root->val);
        else
            result[level-1].insert(result[level-1].begin(), root->val);

        traverse(root->left, level+1, result, !left_to_right);
        traverse(root->right, level+1, result, !left_to_right);
    }
};




// LeetCode, Binary Tree Zigzag Level Order Traversal
// 广度优先遍历，用一个bool记录是从左到右还是从右到左，每一层结束就翻转一下。
// 迭代版，时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
        vector<vector<int> > result;
        queue<TreeNode*> current, next;
        bool left_to_right = true;
        
        if(root == nullptr) {
            return result;
        } else {
            current.push(root);
        }

        while (!current.empty()) {
            vector<int> level; // elments in one level
            while (!current.empty()) {
                TreeNode* node = current.front();
                current.pop();
                level.push_back(node->val);
                if (node->left != nullptr) next.push(node->left);
                if (node->right != nullptr) next.push(node->right);
            }
            if (!left_to_right) reverse(level.begin(), level.end());
            result.push_back(level);
            left_to_right = !left_to_right;
            swap(next, current);
        }
        return result;
    }
};



//azl
## 关键点解析

- 队列

- 队列中用Null(一个特殊元素)来划分每层

- 树的基本操作- 遍历 - 层次遍历（BFS）


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
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        auto ret = vector<vector<int>>();
        if (root == nullptr) return ret;
        auto queue = vector<const TreeNode*>{root};
        auto isOdd = true;
        while (!queue.empty()) {
            auto sz = queue.size();
            auto level = vector<int>();
            for (auto i = 0; i < sz; ++i) {
                auto n = queue.front();
                queue.erase(queue.begin());
                if (isOdd) level.push_back(n->val);
                else level.insert(level.begin(), n->val);
                if (n->left != nullptr) queue.push_back(n->left);
                if (n->right != nullptr) queue.push_back(n->right);
            }
            isOdd = !isOdd;
            ret.push_back(level);
        }
        return ret;
    }
};



## 拓展

由于二叉树是递归结构，因此，可以采用递归的方式来处理。在递归时需要保留当前的层次信息（从0开始），作为参数传递给下一次递归调用。

### 描述

1. 当前层次为偶数时，将当前节点放到当前层的结果数组尾部
2. 当前层次为奇数时，将当前节点放到当前层的结果数组头部
3. 递归对左子树进行之字形遍历，层数参数为当前层数+1
4. 递归对右子树进行之字形遍历，层数参数为当前层数+1

### C++实现

```C++
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        auto ret = vector<vector<int>>();
        zigzagLevelOrder(root, 0, ret);
        return ret;
    }
private:
    void zigzagLevelOrder(const TreeNode* root, int level, vector<vector<int>>& ret) {
        if (root == nullptr || level < 0) return;
        if (ret.size() <= level) {
            ret.push_back(vector<int>());
        }
        if (level % 2 == 0) ret[level].push_back(root->val);
        else ret[level].insert(ret[level].begin(), root->val);
        zigzagLevelOrder(root->left, level + 1, ret);
        zigzagLevelOrder(root->right, level + 1, ret);
    }
};
```