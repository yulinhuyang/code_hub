## 题目描述

```

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

```

## 前置知识

- 递归
- 动态规划


## 关键点解析

- 如果用递归 + 缓存， 缓存的设计很重要
  我的做法是 key 就是 n，value 是以 n 为起点，到达底端的深度。
  下次取出缓存的时候用当前的 level + 存的深度 就是我们想要的 level.

- 使用动态规划的核心点还是选和不选的问题

CPP Code:

```cpp
class Solution {
public:
    int numSquares(int n) {
        static vector<int> dp{0};
        while (dp.size() <= n) {
            int m = dp.size(), minVal = INT_MAX;
            for (int i = 1; i * i <= m; ++i) minVal = min(minVal, 1 + dp[m - i * i]);
            dp.push_back(minVal);
        }
        return dp[n];
    }
};
```