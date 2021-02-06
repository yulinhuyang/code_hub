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




## 关键点解析

- 桶排序

#AZL


Python3 Code:

```Python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        思路同上，在Python中，这里涉及到3个知识点：
        1. 使用内置的 defaultdict 字典设置默认值；
        2. 内置的 ord 函数，计算ASCII值（等于chr）或Unicode值(等于unichr)；
        3. 列表不可哈希，不能作为字典的键，因此这里转为元组；
        """
        str_dict = collections.defaultdict(list)
        for s in strs:
          s_key = [0] * 26
          for c in s:
            s_key[ord(c)-ord('a')] += 1
          str_dict[tuple(s_key)].append(s)
        return list(str_dict.values())
```
