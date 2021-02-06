# 题目描述

```
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
 

提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。

```

## 前置知识

- [栈]


### 思路

我们使用两个栈：

- 一个栈存放全部的元素，push，pop都是正常操作这个正常栈。
- 另一个存放最小栈。 每次push，如果比最小栈的栈顶还小，我们就push进最小栈，否则不操作
- 每次pop的时候，我们都判断其是否和最小栈栈顶元素相同，如果相同，那么我们pop掉最小栈的栈顶元素即可

### 关键点

- 往minstack中 push的判断条件。 应该是stack为空或者x小于等于minstack栈顶元素



Python3 Code:

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if tmp == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()


## 一个栈

Python Code:

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minV = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x - self.minV)
        if x < self.minV:
            self.minV = x

    def pop(self) -> None:
        if not self.stack:
            return
        tmp = self.stack.pop()
        if tmp < 0:
            self.minV -= tmp

    def top(self) -> int:
        if not self.stack:
            return
        tmp = self.stack[-1]
        if tmp < 0:
            return self.minV
        else:
            return self.minV + tmp

    def min(self) -> int:
        return self.minV