232.用栈实现队列

225.用队列实现栈


用栈实现队列


class MyQueue {
    private Stack<Integer> s1, s2;
    
    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }
    
    /** 添加元素到队尾 */
    public void push(int x) {
      s1.push(x);
}
    /** 返回队头元素 */
    public int peek() {
        if (s2.isEmpty())
            // 把 s1 元素压入 s2
            while (!s1.isEmpty())
                s2.push(s1.pop());
        return s2.peek();
    }

    /** 删除队头的元素并返回 */
    public int pop() {
        // 先调用 peek 保证 s2 非空
        peek();
        return s2.pop();
    }


    /** 判断队列是否为空 */
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
}



二、用队列实现栈


class MyStack {
    Queue<Integer> q = new LinkedList<>();
    int top_elem = 0;

    /** 添加元素到栈顶 */
    public void push(int x) {
        // x 是队列的队尾，是栈的栈顶
        q.offer(x);
        top_elem = x;
    }
    
    /** 返回栈顶元素 */
    public int top() {
        return top_elem;
    }
    
    /** 删除栈顶的元素并返回 */
    public int pop() {
        int size = q.size();
        // 留下队尾 2 个元素
        while (size > 2) {
            q.offer(q.poll());
            size--;
        }
        // 记录新的队尾元素
        top_elem = q.peek();
        q.offer(q.poll());
        // 删除之前的队尾元素
        return q.poll();
    }
    
    /** 判断栈是否为空 */
    public boolean empty() {
        return q.isEmpty();
    }
    
}

