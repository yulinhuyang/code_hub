## 题目描述

```
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

```

## 前置知识



// LeetCode, Valid Parentheses
// 时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    bool isValid (string const& s) {
        string left = "([{";
        string right = ")]}";
        stack<char> stk;

        for (auto c : s) {
            if (left.find(c) != string::npos) {
                stk.push (c);
            } else {
                if (stk.empty () || stk.top () != left[right.find (c)])
                    return false;
                else
                    stk.pop ();
            }
        }
        return stk.empty();
    }
};


//azl
基本思路是修改参数，将参数作为我们的栈。 随着我们不断遍历， s 慢慢变成了一个栈。
C++:

```c++
class Solution {
public:
    bool isValid(string s) {
        int top = -1;
        for(int i =0;i<s.length();++i){
            if(top<0 || !isMatch(s[top], s[i])){
                ++top;
                s[top] = s[i];
            }else{
                --top;
            }
        }
        return top == -1;
    }
    bool isMatch(char c1, char c2){
        if(c1 == '(' && c2 == ')') return true;
        if(c1 == '[' && c2 == ']') return true;
        if(c1 == '{' && c2 == '}') return true;
        return false;
    }
};
```