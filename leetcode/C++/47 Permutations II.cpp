
## 题目描述

```
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]




## 关键点解析

- 回溯法
- backtrack 解题公式


// LeetCode, Permutations II
// 深搜，时间复杂度O(n!)，空间复杂度O(n)
class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int>& num) {
        sort(num.begin(), num.end());

        unordered_map<int, int> count_map; // 记录每个元素的出现次数
        for_each(num.begin(), num.end(), [&count_map](int e) {
            if (count_map.find(e) != count_map.end())
                count_map[e]++;
            else
                count_map[e] = 1;
        });

        // 将map里的pair拷贝到一个vector里
        vector<pair<int, int> > elems;
        for_each(count_map.begin(), count_map.end(),
                [&elems](const pair<int, int> &e) {
                    elems.push_back(e);
                });

        vector<vector<int>> result; // 最终结果
        vector<int> p;  // 中间结果

        n = num.size();
        permute(elems.begin(), elems.end(), p, result);
        return result;
    }

private:
    size_t n;
    typedef vector<pair<int, int> >::const_iterator Iter;

    void permute(Iter first, Iter last, vector<int> &p,
            vector<vector<int> > &result) {
        if (n == p.size()) {  // 收敛条件
            result.push_back(p);
        }

        // 扩展状态
        for (auto i = first; i != last; i++) {
            int count = 0; // 统计 *i 在p中出现过多少次
            for (auto j = p.begin(); j != p.end(); j++) {
                if (i->first == *j) {
                    count ++;
                }
            }
            if (count < i->second) {
                p.push_back(i->first);
                permute(first, last, p, result);
                p.pop_back(); // 撤销动作，返回上一层
            }
        }
    }
};



//AZL

CPP Code:

```cpp
class Solution {
private:
  vector<vector<int>> ans;
  void permute(vector<int> nums, int start) {
    if (start == nums.size() - 1) {
      ans.push_back(nums);
      return;
    }
    for (int i = start; i < nums.size(); ++i) {
      if (i != start && nums[i] == nums[start]) continue;
      swap(nums[i], nums[start]);
      permute(nums, start + 1);
    }
  }
public:
  vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    permute(nums, 0);
    return ans;
  }
};
 