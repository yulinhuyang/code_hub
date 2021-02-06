## 题目描述

```
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

```

## 前置知识

- 回溯法


// LeetCode, Combination Sum II
// 时间复杂度O(n!)，空间复杂度O(n)
class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int> &nums, int target) {
        sort(nums.begin(), nums.end()); // 跟第 50 行配合，
                                        // 确保每个元素最多只用一次
        vector<vector<int> > result;
        vector<int> path;
        dfs(nums, path, result, target, 0);
        return result;
    }
private:
    // 使用nums[start, nums.size())之间的元素，能找到的所有可行解
    static void dfs(const vector<int> &nums, vector<int> &path, 
            vector<vector<int> > &result, int gap, int start) {
        if (gap == 0) {  //  找到一个合法解
            result.push_back(path);
            return;
        }

        int previous = -1;
        for (size_t i = start; i < nums.size(); i++) {
            // 如果上一轮循环已经使用了nums[i]，则本次循环就不能再选nums[i]，
            // 确保nums[i]最多只用一次
            if (previous == nums[i]) continue;

            if (gap < nums[i]) return;  // 剪枝

            previous = nums[i];

            path.push_back(nums[i]);
            dfs(nums, path, result, gap - nums[i], i + 1);
            path.pop_back();  // 恢复环境
        }
    }
};



//AZL
CPP Code:

```cpp
class Solution {
    vector<vector<int>> ans;
    void backtrack(vector<int> &A, int target, int start, vector<int> &path) {
        if (!target) {
            ans.push_back(path);
            return;
        }
        for (int i = start; i < A.size() && target >= A[i]; ++i) {
            if (i != start && A[i] == A[i - 1]) continue;
            path.push_back(A[i]);
            dfs(A, target - A[i], i + 1, path);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& A, int target) {
        sort(A.begin(), A.end());
        vector<int> path;
        backtrack(A, target, 0, path);
        return ans;
    }
};