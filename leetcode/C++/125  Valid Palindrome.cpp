## 题目描述

```
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

```

## 前置知识

- 回文
- 双指针



// Leet Code, Valid Palindrome
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        auto left = s.begin(), right = prev(s.end());
        while (left < right) {
            if (!::isalnum(*left))  ++left;
            else if (!::isalnum(*right)) --right;
            else if (*left != *right) return false;
            else { left++, right--; }
        }
        return true;
    }
};



//AZL

C++ Code:

```C++
class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty())
            return true;
        const char* s1 = s.c_str();
        const char* e = s1 + s.length() - 1;
        while (e > s1) {
            if (!isalnum(*s1)) {++s1; continue;}
            if (!isalnum(*e)) {--e; continue;}
            if (tolower(*s1) != tolower(*e)) return false;
            else {--e; ++s1;}
        }
        return true;
    }
};
```
