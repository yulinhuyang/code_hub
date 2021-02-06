## 题目描述

```

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？


例如，上图是一个7 x 3 的网格。有多少可能的路径？

 

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9



// LeetCode, Unique Paths
// 深搜，小集合可以过，大集合会超时
// 时间复杂度O(n^4)，空间复杂度O(n)
class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m < 1 || n < 1) return 0; // 终止条件

        if (m == 1 && n == 1) return 1; // 收敛条件

        return uniquePaths(m - 1, n) + uniquePaths(m, n - 1);
    }
};





// LeetCode, Unique Paths
// 深搜 + 缓存，即备忘录法
// 时间复杂度O(n^2)，空间复杂度O(n^2)
class Solution {
public:
    int uniquePaths(int m, int n) {
        // f[x][y] 表示 从(0,0)到(x,y)的路径条数
        f = vector<vector<int> >(m, vector<int>(n, 0));
        f[0][0] = 1;
        return dfs(m - 1, n - 1);
    }
private:
    vector<vector<int> > f;  // 缓存

    int dfs(int x, int y) {
        if (x < 0 || y < 0) return 0; // 数据非法，终止条件

        if (x == 0 && y == 0) return f[0][0]; // 回到起点，收敛条件

        if (f[x][y] > 0) {
            return f[x][y];
        } else {
            return f[x][y] = dfs(x - 1, y) +  dfs(x, y - 1);
        }
    }
};




// LeetCode, Unique Paths
// 动规，滚动数组
// 时间复杂度O(n^2)，空间复杂度O(n)
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> f(n, 0);
        f[0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // 左边的f[j]，表示更新后的f[j]，与公式中的f[i][j]对应
                // 右边的f[j]，表示老的f[j]，与公式中的f[i-1][j]对应
                f[j] = f[j] + f[j - 1];
            }
        }
        return f[n - 1];
    }
};






// LeetCode, Unique Paths
// 数学公式
class Solution {
public:
    typedef long long int64_t;
    // 求阶乘, n!/(start-1)!，即 n*(n-1)...start，要求 n >= 1
    static int64_t factor(int n, int start = 1) {
        int64_t  ret = 1;
        for(int i = start; i <= n; ++i)
            ret *= i;
        return ret;
    }
    // 求组合数 C_n^k
    static int64_t combination(int n, int k) {
        // 常数优化
        if (k == 0) return 1;
        if (k == 1) return n;

        int64_t ret = factor(n, k+1);
        ret /= factor(n - k);
        return ret;
    }

    int uniquePaths(int m, int n) {
        // max 可以防止n和k差距过大，从而防止combination()溢出
        return combination(m+n-2, max(m-1, n-1));
    }
};




//AZL
CPP Code:

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n + 1, 0);
        dp[n - 1] = 1;
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) dp[j] += dp[j + 1];
        }
        return dp[0];
    }
};