## 题目描述

```
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

```

## 前置知识

- 哈希表
- 排序


// LeetCode, Anagrams
// 时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    vector<string> anagrams(vector<string> &strs) {
        unordered_map<string, vector<string> > group;
        for (const auto &s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            group[key].push_back(s);
        }

        vector<string> result;
        for (auto it = group.cbegin(); it != group.cend(); it++) {
            if (it->second.size() > 1)
                result.insert(result.end(), it->second.begin(), it->second.end());
        }
        return result;
    }
};



#桶排序

下面我们介绍另外一种方法，我们建立一个 26 长度的 counts 数组（如果区分大小写，我们可以建立 52 个，如果支持其他字符依次类推）。
然后我们给每一个字符一个固定的数组下标，然后我们只需要更新每个字符出现的次数。 最后形成的 counts 数组如果一致，则说明他们可以通过
交换顺序得到。这种算法空间复杂度 O(n), 时间复杂度 O(n \* k), n 为数组长度，k 为字符串的平均长度.
//AZL
CPP Code:

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& A) {
        unordered_map<string, int> m;
        vector<vector<string>> ans;
        for (auto &s : A) {
            auto p = s;
            sort(p.begin(), p.end());
            if (!m.count(p)) {
                m[p] = ans.size();
                ans.push_back({});
            }
            ans[m[p]].push_back(s);
        }
        return ans;
    }
};
