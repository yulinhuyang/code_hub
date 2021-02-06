## 题目描述

```
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

```


// LeetCode, Longest Valid Parenthese
// 时间复杂度O(n)，空间复杂度O(n)
// @author 一只杰森(http://weibo.com/wjson)
class Solution {
public:
    int longestValidParentheses(const string& s) {
        vector<int> f(s.size(), 0);
        int ret = 0;
        for (int i = s.size() - 2; i >= 0; --i) {
            int match = i + f[i + 1] + 1;
            // case: "((...))"
            if (s[i] == '(' && match < s.size() && s[match] == ')') {
                f[i] = f[i + 1] + 2;
                // if a valid sequence exist afterwards "((...))()"
                if (match + 1 < s.size()) f[i] += f[match + 1];
            }
            ret = max(ret, f[i]);
        }
        return ret;
    }
};




// LeetCode, Longest Valid Parenthese
// 两遍扫描，时间复杂度O(n)，空间复杂度O(1)
// @author 曹鹏(http://weibo.com/cpcs)
class Solution {
public:
    int longestValidParentheses(const string& s) {
        int answer = 0, depth = 0, start = -1;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                ++depth;
            } else {
                --depth;
                if (depth < 0) {
                    start = i;
                    depth = 0;
                } else if (depth == 0) {
                    answer = max(answer, i - start);
                }
            } 
        }

        depth = 0;
        start = s.size();
        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] == ')') {
                ++depth;
            } else {
                --depth;
                if (depth < 0) {
                    start = i;
                    depth = 0;
                } else if (depth == 0) {
                    answer = max(answer, start - i);
                }
            } 
        }
        return answer;
    }
};



//AZL

// 栈

CPP Code:

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        st.push(-1);
        int ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ')' && st.top() != -1 && s[st.top()] == '(') {
                st.pop();
                ans = max(ans, i - st.top());
            } else st.push(i);
        }
        return ans;
    }
};


//O(1) 空间
```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int left = 0, right = 0, ans = 0, N = s.size();
        for (int i = 0; i < N; ++i) {
            left += s[i] == '(';
            right += s[i] == ')';
            if (left == right) ans = max(ans, left + right);
            else if (right > left) left = right = 0;
        }
        left = 0, right = 0;
        for (int i = N - 1; i >= 0; --i) {
            left += s[i] == '(';
            right += s[i] == ')';
            if (left == right) ans = max(ans, left + right);
            else if (left > right) left = right = 0;
        }
        return ans;
    }
};


//动态规划
CPP Code:

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> dp(s.size() + 1, 0);
        int ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') continue;
            int start = i - dp[i] - 1;
            if (start >= 0 && s[start] == '(')
                dp[i + 1] = dp[i] + 2 + dp[start];
            ans = max(ans, dp[i + 1]);
        }
        return ans;
    }
};



