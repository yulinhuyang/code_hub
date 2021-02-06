## 题目描述

```
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

```

## 前置知识

- 排序
- 双指针
- 分治

// LeetCode, 3Sum
// 先排序，然后左右夹逼，注意跳过重复的数，时间复杂度O(n^2)，空间复杂度O(1)
class Solution {
    public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.size() < 3) return result;
        sort(nums.begin(), nums.end());
        const int target = 0;
		
        auto last = nums.end();
        for (auto i = nums.begin(); i < last-2; ++i) {
            auto j = i+1;
            if (i > nums.begin() && *i == *(i-1)) continue;
            auto k = last-1;
            while (j < k) {
                if (*i + *j + *k < target) {
                    ++j;
                    while(*j == *(j - 1) && j < k) ++j;
                } else if (*i + *j + *k > target) {
                    --k;
                    while(*k == *(k + 1) && j < k) --k;
                } else {
                    result.push_back({ *i, *j, *k });
                    ++j;
                    --k;
                    while(*j == *(j - 1) && *k == *(k + 1) && j < k) ++j;
                }
            }
        }
        return result;
    }
};




//azl

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& A) {
        sort(begin(A), end(A));
        vector<vector<int>> ans;
        int N = A.size();
        for (int i = 0; i < N - 2; ++i) {
            if (i && A[i] == A[i - 1]) continue;
            int L = i + 1, R = N - 1;
            while (L < R) {
                int sum = A[i] + A[L] + A[R];
                if (sum == 0) ans.push_back({ A[i], A[L], A[R] });
                if (sum >= 0) {
                    --R;
                    while (L < R && A[R] == A[R + 1]) --R;
                }
                if (sum <= 0) {
                    ++L;
                    while (L < R && A[L] == A[L - 1]) ++L;
                }
            }
        }
        return ans;
    }
}
```