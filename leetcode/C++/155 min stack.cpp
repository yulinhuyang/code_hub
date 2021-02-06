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


//azl

## 两个栈

### 思路

我们使用两个栈：

- 一个栈存放全部的元素，push，pop都是正常操作这个正常栈。
- 另一个存放最小栈。 每次push，如果比最小栈的栈顶还小，我们就push进最小栈，否则不操作
- 每次pop的时候，我们都判断其是否和最小栈栈顶元素相同，如果相同，那么我们pop掉最小栈的栈顶元素即可

### 关键点

- 往minstack中 push的判断条件。 应该是stack为空或者x小于等于minstack栈顶元素


C++ Code:
```c++
class MinStack {
    stack<int> data;
    stack<int> helper;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        data.push(x);
        if(helper.empty() || helper.top() >= x)
        {
            helper.push(x);
        }
        
    }
    
    void pop() {
        int top = data.top();
        data.pop();
        if(top == helper.top())
        {
            helper.pop();
        }
        
    }
    
    int top() {
        return data.top();
    }
    
    int getMin() {
        return helper.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```


#一个栈

C++ Code:

```c++
class MinStack {
    stack<long> data;
    long min = INT_MAX;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        data.push(x - min);
        if(x < min)
        {
            min = x;
        }
        
    }
    
    void pop() {
        long top = data.top();
        data.pop();
        // 更新最小值
        if(top < 0)
        {
            min -= top;
        }
        
    }
    
    int top() {
        long top = data.top();
        // 最小值为 min
        if (top < 0)
        {
            return min;
        }
        else{
            return min+top;
        }
    }
    
    int getMin() {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```