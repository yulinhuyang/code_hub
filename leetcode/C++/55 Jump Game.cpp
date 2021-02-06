## 题目描述

```
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

```


// LeetCode, Jump Game
// 思路1，时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    bool canJump(const vector<int>& nums) {
        int reach = 1; // 最右能跳到哪里
        for (int i = 0; i < reach && reach < nums.size(); ++i)
            reach = max(reach,  i + 1 + nums[i]);
        return reach >= nums.size();
    }
};




// LeetCode, Jump Game
// 思路2，时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    bool canJump (const vector<int>& nums) {
        if (nums.empty()) return true;
        // 逆向下楼梯，最左能下降到第几层
        int left_most = nums.size() - 1;

        for (int i = nums.size() - 2; i >= 0; --i)
            if (i + nums[i] >= left_most)
                left_most = i;

        return left_most == 0;
    }
};




// LeetCode, Jump Game
// 思路三，动规，时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    bool canJump(const vector<int>& nums) {
        vector<int> f(nums.size(), 0);
        f[0] = 0;
        for (int i = 1; i < nums.size(); i++) {
            f[i] = max(f[i - 1], nums[i - 1]) - 1;
            if (f[i] < 0) return false;;
        }
        return f[nums.size() - 1] >= 0;
    }
};


//AZL
C++ Code:

```c++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n=nums.size();
        int k=0;
        for(int i=0;i<n;i++)
        {
            if(i>k){
                return false;
            }
            // 能跳到最后一个位置
            if(k>=n-1){
                return true;
            }
            // 从当前位置能跳的最远的位置
            k = max(k, i+nums[i]);
        }
        return k >= n-1;
    }
};