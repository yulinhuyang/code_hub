
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

//azL

```py
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        # 0-9
        self.d = [" "," ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.res = []
        self.dfs(digits, 0, "")
        return self.res

    def dfs(self, digits, index, s):
        # 递归的终止条件,用index记录每次遍历到字符串的位置
        if index == len(digits):
            self.res.append(s)
            return
        # 获取当前数字
        c = digits[index]
        # print(c, int(c))
        # 获取数字对应字母
        letters = self.d[int(c)]
        # 遍历字符串
        for l in letters:
            # 调用下一层
            self.dfs(digits, index+1, s+l)



//  azL
## 笛卡尔积解法
### 关键点

- 笛卡尔积
- 记忆化递归

### 代码

代码支持：Python3

```py

# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = [" ", " ", "abc", "def", "ghi",
                  "jkl", "mno", "pqrs", "tuv", "wxyz"]
		    @lru_cache(None)
        def backtrack(digits, start):
            if start >= len(digits):
                return ['']
            ans = []
            for i in range(start, len(digits)):
                for c in mapper[int(digits[i])]:
                    # 笛卡尔积
                    for p in backtrack(digits, i + 1):
                        # 需要过滤诸如  "d", "e", "f" 等长度不符合的数据
                        if start == 0:
                            if len(c + p) == len(digits):
                                ans.append(c + p)
                        else:
                            ans.append(c + p)
            return ans
        if not digits:
            return []
        return backtrack(digits, 0)

```