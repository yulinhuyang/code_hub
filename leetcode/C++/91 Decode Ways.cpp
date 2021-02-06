## 题目描述

```
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

题目数据保证答案肯定是一个 32 位的整数。

 

示例 1：

输入："12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2：

输入："226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
示例 3：

输入：s = "0"
输出：0
示例 4：

输入：s = "1"
输出：1
示例 5：

输入：s = "2"
输出：1
 

提示：

1 <= s.length <= 100
s 只包含数字，并且可以包含前导零。



// LeetCode, Decode Ways
// 时间复杂度O(n)，空间复杂度O(logn)
class Solution {
public:
    int sumNumbers(TreeNode *root) {
        return dfs(root, 0);
    }
private:
    int dfs(TreeNode *root, int sum) {
        if (root == nullptr) return 0;
        if (root->left == nullptr && root->right == nullptr)
            return sum * 10 + root->val;

        return dfs(root->left, sum * 10 + root->val) +
                dfs(root->right, sum * 10 + root->val);
    }
};


//azl
使用滚动数组优化。

CPP code:

```cpp
class Solution {
public:
  int numDecodings(string s) {
    int pre2 = 0, pre1 = 1;
    for (int i = 0; i < s.size() && pre1; ++i) {
      int cur = 0;
      if (s[i] != '0') cur += pre1;
      if (i != 0 && s[i - 1] != '0' && (s[i - 1] - '0') * 10 + s[i] - '0' <= 26)
        cur += pre2;
      pre2 = pre1;
      pre1 = cur;
    }
    return pre1;
  }
};
```