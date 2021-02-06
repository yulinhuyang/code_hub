## 题目描述

```
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

```

## 前置知识

- DFS
- 回溯法


// LeetCode, Generate Parentheses
// 时间复杂度O(TODO)，空间复杂度O(n)
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string path;
        if (n > 0) generate(n, path, result, 0, 0);
        return result;
    }
    // l 表示 ( 出现的次数, r 表示 ) 出现的次数
    void generate(int n, string& path, vector<string> &result, int l, int r) {
        if (l == n) {
            string s(path);
            result.push_back(s.append(n - r, ')'));
            return;
        }
        
        path.push_back('(');
        generate(n, path, result, l + 1, r);
        path.pop_back();

        if (l > r) {
            path.push_back(')');
            generate(n, path, result, l, r + 1);
            path.pop_back();
        }
    }
};







// LeetCode, Generate Parentheses
// @author 连城 (http://weibo.com/lianchengzju)
class Solution {
public:
    vector<string> generateParenthesis (int n) {
        if (n == 0) return vector<string>(1, "");
        if (n == 1) return vector<string> (1, "()");
        vector<string> result;

        for (int i = 0; i < n; ++i)
            for (auto inner : generateParenthesis (i))
                for (auto outer : generateParenthesis (n - 1 - i))
                    result.push_back ("(" + inner + ")" + outer);

        return result;
    }
};


//azl
```cpp
class Solution {
private:
    vector<string> ans;
    void generate(int leftCnt, int rightCnt, string &s) {
        if (!leftCnt && !rightCnt) {
            ans.push_back(s);
            return;
        }
        if (leftCnt) {
            s.push_back('(');
            generate(leftCnt - 1, rightCnt, s);
            s.pop_back();
        }
        if (rightCnt > leftCnt) {
            s.push_back(')');
            generate(leftCnt, rightCnt - 1, s);
            s.pop_back();
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        string s;
        generate(n, n, s);
        return ans;
    }
};
```