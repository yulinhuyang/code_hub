## 题目描述

```
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

```

## 前置知识

- 堆
- 队列



## 关键点解析

- 用两个堆（一个大顶堆，一个小顶堆）来简化时间复杂度
- 用优先级队列简化操作


CPP Code：

```cpp
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {

    }

    void addNum(int num) {
        if (big_queue.empty()) {
            big_queue.push(num);
            return;
        }
        if (big_queue.size() == small_queue.size()) {
            if (num <= big_queue.top()) {
                big_queue.push(num);
            } else {
                small_queue.push(num);
            }
        } else if (big_queue.size() > small_queue.size()) {
            if (big_queue.top() > num) {
                small_queue.push(big_queue.top());
                big_queue.pop();
                big_queue.push(num);
            } else {
                small_queue.push(num);
            }
        } else if (big_queue.size() < small_queue.size()) {
            if (small_queue.top() > num) {
                big_queue.push(num);
            } else {
                big_queue.push(small_queue.top());
                small_queue.pop();
                small_queue.push(num);
            }
        }
    }

    double findMedian() {
        if (big_queue.size() == small_queue.size()) {
            return (big_queue.top() + small_queue.top()) * 0.5;
        }
        if (big_queue.size() < small_queue.size()) {
            return small_queue.top();
        }
        return big_queue.top();
    }

private:
    std::priority_queue<int, std::vector<int>, std::greater<int>> small_queue;  // 最小堆
    std::priority_queue<int> big_queue; // 最大堆
};
```
