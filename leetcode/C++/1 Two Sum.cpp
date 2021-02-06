## 题目描述

```
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```




//LeetCode, Two Sum
// 方法2：hash。用一个哈希表，存储每个数对应的下标
// 时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> mapping;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            mapping[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++) {
            const int gap = target - nums[i];
            if (mapping.find(gap) != mapping.end() && mapping[gap] > i) {
                result.push_back(i + 1);
                result.push_back(mapping[gap] + 1);
                break;
            }
        }
        return result;
    }
};



//azl
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& A, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < A.size(); ++i) {
            int t = target - A[i];
            if (m.count(t)) return { m[t], i };
            m[A[i]] = i;
        }
        return {};
    }
};
```