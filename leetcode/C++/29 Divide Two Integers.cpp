
## 题目描述

```
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

 

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
 

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

```



// LeetCode, Divide Two Integers
// 时间复杂度O(logn)，空间复杂度O(1)
class Solution {
public:
    int divide(int dividend, int divisor) {
        // 当 dividend = INT_MIN时，-dividend会溢出，所以用 long long
        long long a = dividend >= 0 ? dividend : -(long long)dividend;
        long long b = divisor >= 0 ? divisor : -(long long)divisor;

        // 当 dividend = INT_MIN时，divisor = -1时，结果会溢出，所以用 long long
        long long result = 0;
        while (a >= b) {
            long long c = b;
            for (int i = 0; a >= c; ++i, c <<= 1) {
                a -= c;
                result += 1 << i;
            }
        }

        return ((dividend^divisor) >> 31) ? (-result) : (result);
    }
};






// LeetCode, Divide Two Integers
// 时间复杂度O(logn)，空间复杂度O(1)
class Solution {
public:
    int divide(int dividend, int divisor) {
        int result = 0; // 当 dividend = INT_MIN时，divisor = -1时，结果会溢出
        const bool sign = (dividend > 0 && divisor < 0) ||
                (dividend < 0 && divisor > 0); // 异号

        // 当 dividend = INT_MIN时，-dividend会溢出，所以用 unsigned int
        unsigned int a = dividend >= 0 ? dividend : -dividend;
        unsigned int b = divisor >= 0 ? divisor : -divisor;

        while (a >= b) {
            int multi = 1;
            unsigned int bb = b;
            while (a >= bb) {
                a -= bb;
                result += multi;

                if (bb < INT_MAX >> 1) { // 防止溢出
                    bb += bb;
                    multi += multi;
                }
            }
        }
        if (sign) return -result;
        else return result;
    }
};


//AZL
CPP Code:

```cpp
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (!divisor) return 0;  // divide-by-zero error
        bool pos1 = dividend > 0, pos2 = divisor > 0, pos = !(pos1^pos2);
        if (pos1) dividend = -dividend;
        if (pos2) divisor = -divisor;
        int q = 0, d = divisor, t = 1;
        while (t > 0 && dividend < 0) {
            if (dividend - d <= 0) {
                dividend -= d;
                q -= t;
                if ((INT_MIN >> 1) < d) {
                    t <<= 1;
                    d <<= 1;
                }
            } else {
                d >>= 1;
                t >>= 1;
            }
        }
        return pos? -q : q;
    }
};