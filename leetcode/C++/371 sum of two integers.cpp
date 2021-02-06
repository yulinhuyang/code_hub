## 题目描述

```
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1

```

## 前置知识

- [位运算]

C++ Code:
```c++
class Solution {
public:
    int getSum(int a, int b) {
        if(a==0) return b;
        if(b==0) return a;

        while(b!=0)
        {
            // 防止 AddressSanitizer 对有符号左移的溢出保护处理
            auto carry = ((unsigned int ) (a & b))<<1;
            // 计算无进位的结果
            a = a^b;
            //将存在进位的位置置1
            b =carry;
        }
        return a;
    }
};
```