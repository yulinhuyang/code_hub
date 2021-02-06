## 题目描述

```
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
```

## BFS

CPP：

```cpp
class Solution {
public:
    int findBottomLeftValue_bfs(TreeNode* root) {
        queue<TreeNode*> q;
        TreeNode* ans = NULL;
        q.push(root);
        while (!q.empty()) {
            ans = q.front();
            int size = q.size();
            while (size--) {
                TreeNode* cur = q.front();
                q.pop();
                if (cur->left )
                    q.push(cur->left);
                if (cur->right)
                    q.push(cur->right);
            }
        }
        return ans->val;
    }
}