
## 题目描述

```
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

```

// LeetCode, Subsets
// 增量构造法，深搜，时间复杂度O(2^n)，空间复杂度O(n)
class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin(), S.end());  // 输出要求有序
        vector<vector<int> > result;
        vector<int> path;
        subsets(S, path, 0, result);
        return result;
    }

private:
    static void subsets(const vector<int> &S, vector<int> &path, int step,
            vector<vector<int> > &result) {
        if (step == S.size()) {
            result.push_back(path);
            return;
        }
        // 不选S[step]
        subsets(S, path, step + 1, result);
        // 选S[step]
        path.push_back(S[step]);
        subsets(S, path, step + 1, result);
        path.pop_back();
    }
};






// LeetCode, Subsets
// 位向量法，深搜，时间复杂度O(2^n)，空间复杂度O(n)
class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin(), S.end());  // 输出要求有序

        vector<vector<int> > result;
        vector<bool> selected(S.size(), false);
        subsets(S, selected, 0, result);
        return result;
    }

private:
    static void subsets(const vector<int> &S, vector<bool> &selected, int step,
            vector<vector<int> > &result) {
        if (step == S.size()) {
            vector<int> subset;
            for (int i = 0; i < S.size(); i++) {
                if (selected[i]) subset.push_back(S[i]);
            }
            result.push_back(subset);
            return;
        }
        // 不选S[step]
        selected[step] = false;
        subsets(S, selected, step + 1, result);
        // 选S[step]
        selected[step] = true;
        subsets(S, selected, step + 1, result);
    }
};






// LeetCode, Subsets
// 迭代版，时间复杂度O(2^n)，空间复杂度O(1)
class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin(), S.end()); // 输出要求有序
        vector<vector<int> > result(1);
        for (auto elem : S) {
            result.reserve(result.size() * 2);
            auto half = result.begin() + result.size();
            copy(result.begin(), half, back_inserter(result));
            for_each(half, result.end(), [&elem](decltype(result[0]) &e){
                e.push_back(elem);
            });
        }
        return result;
    }
};






// LeetCode, Subsets
// 二进制法，时间复杂度O(2^n)，空间复杂度O(1)
class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin(), S.end()); // 输出要求有序
        vector<vector<int> > result;
        const size_t n = S.size();
        vector<int> v;

        for (size_t i = 0; i < 1 << n; i++) {
            for (size_t j = 0; j < n; j++) {
                if (i & 1 << j) v.push_back(S[j]);
            }
            result.push_back(v);
            v.clear();
        }
        return result;
    }
};



//AZL
```C++
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        auto ret = vector<vector<int>>();
        auto tmp = vector<int>();
        backtrack(ret, tmp, nums, 0);
        return ret;
    }

    void backtrack(vector<vector<int>>& list, vector<int>& tempList, vector<int>& nums, int start) {
        list.push_back(tempList);
        for (auto i = start; i < nums.size(); ++i) {
            tempList.push_back(nums[i]);
            backtrack(list, tempList, nums, i + 1);
            tempList.pop_back();
        }
    }
};