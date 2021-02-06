## 题目描述

```
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

```

## 前置知识

- 哈希表
- [滑动窗口]



// LeetCode, Longest Substring Without Repeating Characters
// 时间复杂度O(n)，空间复杂度O(1)
// 考虑非字母的情况


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        const int ASCII_MAX = 255;
        int last[ASCII_MAX]; // 记录字符上次出现过的位置
        int start = 0; // 记录当前子串的起始位置

        fill(last, last + ASCII_MAX, -1); // 0也是有效位置，因此初始化为-1
        int max_len = 0;
        for (int i = 0; i < s.size(); i++) {
            if (last[s[i]] >= start) {
                max_len = max(i - start, max_len);
                start = last[s[i]] + 1;
            }
            last[s[i]] = i;
        }
        return max((int)s.size() - start, max_len);  // 别忘了最后一次，例如"abcd"
    }
};



//azL

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int ans = 0, start = 0;
        int n = s.length();
        // 
        map<char, int> mp;

        for(int i=0;i<n;i++)
        {
            char alpha = s[i];
            if(mp.count(alpha))
            {
                start = max(start, mp[alpha]+1);
            }
            ans = max(ans, i-start+1);
            // 字符位置
            mp[alpha] = i;
        }

        return ans;
    }
};
```
//
