## 题目描述

```
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

 

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

```

## 前置知识

- [滑动窗口]

C++ Code：

```C++
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int num_len= nums.size();
        int left=0, right=0, total=0, min_len= num_len+1;
        while (right < num_len) {
            do {
                total += nums[right++];
            } while (right < num_len && total < s);
            while (left < right && total - nums[left] >= s) total -= nums[left++];
            if (total >=s && min_len > right - left)
                min_len = right- left;
        }
        return min_len <= num_len ? min_len: 0;
    }
};