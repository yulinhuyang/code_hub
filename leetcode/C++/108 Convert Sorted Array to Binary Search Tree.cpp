
## 题目描述

```
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

```


// LeetCode, Convert Sorted Array to Binary Search Tree
// 分治法，时间复杂度O(n)，空间复杂度O(logn)
class Solution {
public:
    TreeNode* sortedArrayToBST (vector<int>& num) {
        return sortedArrayToBST(num.begin(), num.end());
    }

    template<typename RandomAccessIterator>
    TreeNode* sortedArrayToBST (RandomAccessIterator first,
            RandomAccessIterator last) {
        const auto length = distance(first, last);

        if (length <= 0) return nullptr;  // 终止条件

        // 三方合并
        auto mid = first + length / 2;
        TreeNode* root = new TreeNode (*mid);
        root->left = sortedArrayToBST(first, mid);
        root->right = sortedArrayToBST(mid + 1, last);

        return root;
    }
};


//azl
C++ Code:

```c++
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return reBuild(nums, 0, nums.size()-1);
    }

    TreeNode* reBuild(vector<int>& nums, int left, int right) 
    {
        // 终止条件：中序遍历为空
        if(left > right)
        {
            return NULL;
        }
        // 建立当前子树的根节点
        int mid = (left+right)/2;
        TreeNode * root = new TreeNode(nums[mid]);
       
        // 左子树的下层递归
        root->left = reBuild(nums, left, mid-1);
        // 右子树的下层递归
        root->right = reBuild(nums, mid+1, right);
        // 返回根节点
        return root;
    }
};
```