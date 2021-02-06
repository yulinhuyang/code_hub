## 题目描述

```
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

```


// LeetCode, Combination Sum
// 时间复杂度O(n!)，空间复杂度O(n)
class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int> > result; // 最终结果
        vector<int> path; // 中间结果
        dfs(nums, path, result, target, 0);
        return result;
    }

private:
    void dfs(vector<int>& nums, vector<int>& path, vector<vector<int> > &result,
            int gap, int start) {
        if (gap == 0) {  // 找到一个合法解
            result.push_back(path);
            return;
        }
        for (size_t i = start; i < nums.size(); i++) { // 扩展状态
            if (gap < nums[i]) return; // 剪枝

            path.push_back(nums[i]); // 执行扩展动作
            dfs(nums, path, result, gap - nums[i], i);
            path.pop_back();  // 撤销动作
        }
    }
};




//AZL
CPP Code:

```cpp
class Solution {
private:
    vector<vector<int>> res;
    void dfs(vector<int> &c, int t, int start, vector<int> &v) {
        if (!t) {
            res.push_back(v);
            return;
        }
        for (int i = start; i < c.size() && t >= c[i]; ++i) {
            v.push_back(c[i]);
            dfs(c, t - c[i], i, v);
            v.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> v;
        dfs(candidates, target, 0, v);
        return res;
    }
};
```
