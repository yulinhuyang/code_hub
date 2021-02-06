## 题目描述

```
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.

```

## 前置知识

- 递归


//azl

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
    int sumNumbers(TreeNode* root) {
        return helper(root, 0);
    }
private:
    int helper(const TreeNode* root, int val) {
        if (root == nullptr) return 0;
        auto ret = root->val + val * 10;
        if (root->left == nullptr && root->right == nullptr)
            return ret;
        auto l = helper(root->left, ret);
        auto r = helper(root->right, ret);
        return l + r;
    }
};
```


### 描述

使用两个队列：
1. 当前和队列：保存上一层每个结点的当前和（比如49和40）
2. 结点队列：保存当前层所有的非空结点

每次循环按层处理结点队列。处理步骤：
1. 从结点队列取出一个结点
2. 从当前和队列将上一层对应的当前和取出来
3. 若左子树非空，则将该值乘以10加上左子树的值，并添加到当前和队列中
4. 若右子树非空，则将该值乘以10加上右子树的值，并添加到当前和队列中
5. 若左右子树均为空时，将该节点的当前和加到返回值中


C++ Code：

```C++
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if (root == nullptr) return 0;
        auto ret = 0;
        auto runningSum = vector<int>{root->val};
        auto queue = vector<const TreeNode*>{root};
        while (!queue.empty()) {
            auto sz = queue.size();
            for (auto i = 0; i < sz; ++i) {
                auto n = queue.front();
                queue.erase(queue.begin());
                auto tmp = runningSum.front();
                runningSum.erase(runningSum.begin());
                if (n->left != nullptr) {
                    runningSum.push_back(tmp * 10 + n->left->val);
                    queue.push_back(n->left);
                }
                if (n->right != nullptr) {
                    runningSum.push_back(tmp * 10 + n->right->val);
                    queue.push_back(n->right);
                }
                if (n->left == nullptr && n->right == nullptr) {
                    ret += tmp;
                }
            }
        }
        return ret;
    }
};
```