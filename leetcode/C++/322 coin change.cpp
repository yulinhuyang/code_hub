## 题目描述

```
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

```

## 前置知识

- 贪心算法
- [动态规划]



C++ Code：

> C++中采用 INT_MAX，因此判断时需要加上`dp[a - coin] < INT_MAX`以防止溢出

```C++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        auto dp = vector<int>(amount + 1, INT_MAX);
        dp[0] = 0;
        for (auto a = 1; a <= amount; ++a) {
            for (const auto & coin : coins) {
                if (a >= coin && dp[a - coin] < INT_MAX) {
                    dp[a] = min(dp[a], dp[a-coin] + 1);
                }
            }
        }
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};
```