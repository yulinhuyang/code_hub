
```
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```

## 前置知识

- 栈


#AZL
简单来说就是，一元操作符绑定一个操作数。而二元操作符绑定两个操作数。

算法：

- 从左到右遍历 s
- 如果是数字，则更新数字
- 如果是空格，则跳过
- 如果是运算符，则按照运算符规则计算，并将计算结果重新入栈，具体见代码。最后更新 pre_flag 即可。

为了简化判断， 我使用了两个哨兵。一个是 s 末尾的 $，另一个是最开始的 pre_flag。

## 关键点解析

- 记录 pre_flag，即上一次出现的操作符
- 使用哨兵简化操作。一个是 s 的 $ ，另一个是 pre_flag 的 +



Python Code：

```py
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s += '$'
        pre_flag = '+'
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ': continue
            else:
                if pre_flag == '+':
                    stack.append(num)
                elif pre_flag == '-':
                    stack.append(-num)
                elif pre_flag == '*':
                    stack.append(stack.pop() * num)
                elif pre_flag == '/':
                    stack.append(int(stack.pop() / num))
                pre_flag = c
                num = 0
        return sum(stack)

```


## 扩展

224. 基本计算器 和这道题差不多，官方难度困难。就是多了个括号而已。所以基本上可以看做是这道题的扩展。题目描述：

```
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。


因此我们可以使用递归，每次遇到 `(` 则开启一轮新的递归，遇到 `)`则退出一层递归即可。

Python 代码：

```py
class Solution:
    def calculate(self, s: str) -> int:
        def dfs(s, start):
            stack = []
            pre_flag = '+'
            num = 0
            i = start
            while i < len(s):
                c = s[i]
                if  c == ' ':
                    i += 1
                    continue
                elif c == '(':
                    i, num = dfs(s, i+1)
                elif c.isdigit():
                    num = num * 10 + int(c)
                else:
                    if pre_flag == '+':
                        stack.append(num)
                    elif pre_flag == '-':
                        stack.append(-num)
                    if c == ')': break
                    pre_flag = c
                    num = 0
                i += 1
            return i, sum(stack)
        s += '$'
        return dfs(s, 0)[1]

```