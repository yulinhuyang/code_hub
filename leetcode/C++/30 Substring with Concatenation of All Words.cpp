## 题目描述

```
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]


```

// LeetCode, Substring with Concatenation of All Words
// 时间复杂度O(n*m)，空间复杂度O(m)
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& dict) {
        size_t wordLength = dict.front().length();
        size_t catLength = wordLength * dict.size();
        vector<int> result;

        if (s.length() < catLength) return result;

        unordered_map<string, int> wordCount;

        for (auto const& word : dict) ++wordCount[word];

        for (auto i = begin(s); i <= prev(end(s), catLength); ++i) {
            unordered_map<string, int> unused(wordCount);

            for (auto j = i; j != next(i, catLength); j += wordLength) {
                auto pos = unused.find(string(j, next(j, wordLength)));

                if (pos == unused.end() || pos->second == 0) break;

                if (--pos->second == 0) unused.erase(pos);
            }

            if (unused.size() == 0) result.push_back(distance(begin(s), i));
        }

        return result;
    }
};



//AZL
CPP Code:

```cpp

class Solution {
private:
    int len, n;
    string s;
    bool rec(int i, unordered_map<string, int> &m, int cnt) {
        if (cnt == n) return true;
        int &v = m[s.substr(i, len)];
        if (v) {
            v--;
            bool ret = rec(i + len, m, cnt + 1);
            v++;
            return ret;
        }
        return false;
    }
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (words.empty()) return {};
        this->s = s;
        len = words[0].size();
        n = words.size();
        unordered_map<string, int> m;
        for (string word : words) ++m[word];
        int end = s.size() - n * len;
        vector<int> v;
        for (int i = 0; i <= end; ++i) {
            if (rec(i, m, 0)) v.push_back(i);
        }
        return v;
    }
};