
## 题目描述

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

![image.png](https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png)

```

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

```

## 前置知识

- 回溯
- 笛卡尔积

// LeetCode, Letter Combinations of a Phone Number
// 时间复杂度O(3^n)，空间复杂度O(n)
class Solution {
public:
    const vector<string> keyboard { " ", "", "abc", "def", // '0','1','2',...
            "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };

    vector<string> letterCombinations (const string &digits) {
        vector<string> result;
        if (digits.empty()) return result;
        dfs(digits, 0, "", result);
        return result;
    }

    void dfs(const string &digits, size_t cur, string path,
            vector<string> &result) {
        if (cur == digits.size()) {
            result.push_back(path);
            return;
        }
        for (auto c : keyboard[digits[cur] - '0']) {
            dfs(digits, cur + 1, path + c, result);
        }
    }
};




// LeetCode, Letter Combinations of a Phone Number
// 时间复杂度O(3^n)，空间复杂度O(1)
class Solution {
public:
    const vector<string> keyboard { " ", "", "abc", "def", // '0','1','2',...
            "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };

    vector<string> letterCombinations (const string &digits) {
        if (digits.empty()) return vector<string>();
        vector<string> result(1, "");
        for (auto d : digits) {
            const size_t n = result.size();
            const size_t m = keyboard[d - '0'].size();

            result.resize(n * m);
            for (size_t i = 0; i < m; ++i)
                copy(result.begin(), result.begin() + n, result.begin() + n * i);

            for (size_t i = 0; i < m; ++i) {
                auto begin = result.begin();
                for_each(begin + n * i, begin + n * (i+1), [&](string &s) {
                    s += keyboard[d - '0'][i];
                });
            }
        }
        return result;
    }
};



//azl
```c++
class Solution {
public:
    string letterMap[10] = {" "," ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    vector<string> res;
    vector<string> letterCombinations(string digits) {
        if(digits == "")
        {
            return res;
        }
        dfs(digits, 0, "");
        return res;
    }

    void dfs(string digits, int index, string s)
    {
        if(index == digits.length())
        {
            res.push_back(s);
            return;
        }
        // 获取当前数字
        char c = digits[index];
        // 获取数字对应字母
        string letters = letterMap[c-'0'];
        for(int i = 0 ; i < letters.length() ; i ++)
        {
            dfs(digits, index+1, s+letters[i]);
        }
    }
}
```