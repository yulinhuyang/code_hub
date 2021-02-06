## 题目描述

```
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

```

## 前置知识

- 递归
- 位运算



//LeetCode, Pow(x, n)
// 二分法，$x^n = x^{n/2} * x^{n/2} * x^{n\%2}$
// 时间复杂度O(logn)，空间复杂度O(1)
class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0) return 1.0 / power(x, -n);
        else return power(x, n);
    }
private:
    double power(double x, int n) {
        if (n == 0) return 1;
        double v = power(x, n / 2);
        if (n % 2 == 0) return v * v;
        else return v * v * x;
    }
};


//AZL
我们的思路就是：

- 如果 n 是偶数，我们将 n 折半，底数变为 x^2
- 如果 n 是奇数， 我们将 n 减去 1 ，底数不变，得到的结果再乘上底数 x

这样终于可以 AC。


## 解法二 - 优化递归
CPP Code:

```cpp
class Solution {
    double myPow(double x, long n) {
        if (n < 0) return 1 / myPow(x, -n);
        if (n == 0) return 1;
        if (n == 1) return x;
        if (n == 2) return x * x;
        return myPow(myPow(x, n / 2), 2) * (n % 2 ? x : 1);
    }
public:
    double myPow(double x, int n) {
        return myPow(x, (long)n);
    }
};
```