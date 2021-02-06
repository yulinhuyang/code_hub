## 题目描述

```
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

 

示例 1：

输入：[3,2,3]
输出：[3]
示例 2：

输入：nums = [1]
输出：[1]
示例 3：

输入：[1,1,1,3,3,2,2,2]
输出：[1,2]
 

提示：

1 <= nums.length <= 5 * 104
-10^9 <= nums[i] <= 10^9

```

## 前置知识

- 摩尔投票法


## 关键点解析

- 摩尔投票法
- 两个 counter
- 最后得到的只是出现次数最多的两个数字，有可能不满足出现次数大于 1/3

## 代码

代码支持：CPP，JS

CPP Code:

```cpp
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int c1 = 0, c2 = 0, v1 = 0, v2 = 1;
        for (int n : nums) {
            if (v1 == n) ++c1;
            else if (v2 == n) ++c2;
            else if (!c1) v1 = n, ++c1;
            else if (!c2) v2 = n, ++c2;
            else --c1, --c2;
        }
        c1 = c2 = 0;
        for (int n : nums) {
            if (v1 == n) ++c1;
            if (v2 == n) ++c2;
        }
        vector<int> v;
        if (c1 > nums.size() / 3) v.push_back(v1);
        if (c2 > nums.size() / 3) v.push_back(v2);
        return v;
    }
};