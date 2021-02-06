## 题目描述

```
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


```

## 前置知识

- 二叉搜索树
- 分治


// LeetCode, Unique Binary Search Trees II
// 时间复杂度TODO，空间复杂度TODO
class Solution {
public:
    vector<TreeNode *> generateTrees(int n) {
        if (n == 0) return generate(1, 0);
        return generate(1, n);
    }
private:
    vector<TreeNode *> generate(int start, int end) {
        vector<TreeNode*> subTree;
        if (start > end) {
            subTree.push_back(nullptr);
            return subTree;
        }
        for (int k = start; k <= end; k++) {
            vector<TreeNode*> leftSubs = generate(start, k - 1);
            vector<TreeNode*> rightSubs = generate(k + 1, end);
            for (auto i : leftSubs) {
                for (auto j : rightSubs) {
                    TreeNode *node = new TreeNode(k);
                    node->left = i;
                    node->right = j;
                    subTree.push_back(node);
                }
            }
        }
        return subTree;
    }
};



//azl

CPP Code:

```cpp
class Solution {
private:
    vector<TreeNode*> generateTrees(int first, int last) {
        if (first > last) return { NULL };
        vector<TreeNode*> v;
        for (int i = first; i <= last; ++i) {
            auto lefts = generateTrees(first, i - 1);
            auto rights = generateTrees(i + 1, last);
            for (auto left : lefts) {
                for (auto right : rights) {
                    v.push_back(new TreeNode(i));
                    v.back()->left = left;
                    v.back()->right = right;
                }
            }
        }
        return v;
    }
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n <= 0) return {};
        return generateTrees(1, n);
    }
};
```