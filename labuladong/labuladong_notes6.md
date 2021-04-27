## 第四章、高频面试系列

### 1 如何实现LRU算法

计算机的缓存容量有限，如果缓存满了就要删除一些内容，给新内容腾位置。但问题是，删除哪些内容呢？我们肯定希望删掉哪些没什么用的缓存，而把有用的数据继续留在缓存里，方便之后继续使用。那么，什么样的数据，我们判定为「有用的」的数据呢？

LRU 缓存淘汰算法就是一种常用策略。LRU 的全称是 Least Recently Used，也就是说我们认为最近使用过的数据应该是是「有用的」，很久都没用过的数据应该是无用的，内存满了就优先删那些很久没用过的数据。

设计：

1、显然 `cache` 中的元素必须有时序，以区分最近使用的和久未使用的数据，当容量满了之后要删除最久未使用的那个元素腾位置。

2、我们要在 `cache` 中快速找某个 `key` 是否已存在并得到对应的 `val`；

3、每次访问 `cache` 中的某个 `key`，需要将这个元素变为最近使用的，也就是说 `cache` 要支持在任意位置快速插入和删除元素。


#### 1.1 实现

```java
class Node {
    public int key, val;
    public Node next, prev;
    public Node(int k, int v) {
        this.key = k;
        this.val = v;
    }
}
```

```java
class DoubleList {  
    // 头尾虚节点
    private Node head, tail;  
    // 链表元素数
    private int size;
    
    public DoubleList() {
        // 初始化双向链表的数据
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }

    // 在链表尾部添加节点 x，时间 O(1)
    public void addLast(Node x) {
        x.prev = tail.prev;
        x.next = tail;
        tail.prev.next = x;
        tail.prev = x;
        size++;
    }

    // 删除链表中的 x 节点（x 一定存在）
    // 由于是双链表且给的是目标 Node 节点，时间 O(1)
    public void remove(Node x) {
        x.prev.next = x.next;
        x.next.prev = x.prev;
        size--;
    }
    
    // 删除链表中第一个节点，并返回该节点，时间 O(1)
    public Node removeFirst() {
        if (head.next == tail)
            return null;
        Node first = head.next;
        remove(first);
        return first;
    }

    // 返回链表长度，时间 O(1)
    public int size() { return size; }

}
```
**注意我们实现的双链表 API 只能从尾部插入，也就是说靠尾部的数据是最近使用的，靠头部的数据是最久为使用的**。

```java
class LRUCache {
    // key -> Node(key, val)
    private HashMap<Integer, Node> map;
    // Node(k1, v1) <-> Node(k2, v2)...
    private DoubleList cache;
    // 最大容量
    private int cap;
    
    public LRUCache(int capacity) {
        this.cap = capacity;
        map = new HashMap<>();
        cache = new DoubleList();
    }
```

```java
/* 将某个 key 提升为最近使用的 */
private void makeRecently(int key) {
    Node x = map.get(key);
    // 先从链表中删除这个节点
    cache.remove(x);
    // 重新插到队尾
    cache.addLast(x);
}

/* 添加最近使用的元素 */
private void addRecently(int key, int val) {
    Node x = new Node(key, val);
    // 链表尾部就是最近使用的元素
    cache.addLast(x);
    // 别忘了在 map 中添加 key 的映射
    map.put(key, x);
}

/* 删除某一个 key */
private void deleteKey(int key) {
    Node x = map.get(key);
    // 从链表中删除
    cache.remove(x);
    // 从 map 中删除
    map.remove(key);
}

/* 删除最久未使用的元素 */
private void removeLeastRecently() {
    // 链表头部的第一个元素就是最久未使用的
    Node deletedNode = cache.removeFirst();
    // 同时别忘了从 map 中删除它的 key
    int deletedKey = deletedNode.key;
    map.remove(deletedKey);
}
```

```java
public int get(int key) {
    if (!map.containsKey(key)) {
        return -1;
    }
    // 将该数据提升为最近使用的
    makeRecently(key);
    return map.get(key).val;
}
```

```java
public void put(int key, int val) {
    if (map.containsKey(key)) {
        // 删除旧的数据
        deleteKey(key);
        // 新插入的数据为最近使用的数据
        addRecently(key, val);
        return;
    }
    
    if (cap == cache.size()) {
        // 删除最久未使用的元素
        removeLeastRecently();
    }
    // 添加为最近使用的元素
    addRecently(key, val);
}
```

#### 1.2 用 Java 的内置类型 `LinkedHashMap` 来实现 LRU 算法


```java
class LRUCache {
    int cap;
    LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>();
    public LRUCache(int capacity) { 
        this.cap = capacity;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        // 将 key 变为最近使用
        makeRecently(key);
        return cache.get(key);
    }
    
    public void put(int key, int val) {
        if (cache.containsKey(key)) {
            // 修改 key 的值
            cache.put(key, val);
            // 将 key 变为最近使用
            makeRecently(key);
            return;
        }
        
        if (cache.size() >= this.cap) {
            // 链表头部就是最久未使用的 key
            int oldestKey = cache.keySet().iterator().next();
            cache.remove(oldestKey);
        }
        // 将新的 key 添加链表尾部
        cache.put(key, val);
    }
    
    private void makeRecently(int key) {
        int val = cache.get(key);
        // 删除 key，重新插入到队尾
        cache.remove(key);
        cache.put(key, val);
    }
}
```

#### 1.3 其他语言实现

[146.LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)

**c++**

[gowufang](https://github.com/gowufang)提供第146题C++代码：
```cpp
class LRUCache {
        public:
        struct node {
            int val;
            int key;
            node* pre;//当前节点的前一个节点
            node* next;//当前节点的后一个节点
            node(){}
            node(int key, int val):key(key), val(val), pre(NULL), next(NULL){}
        };

        LRUCache(int size) {
            this->size = size;
            head = new node();
            tail = new node();
            head->next = tail;
            tail->pre = head;
        }


        void movetohead(node* cur)//相当于一个insert操作，在head 和 head的next之间插入一个节点
        {
            node* next = head->next;//head的next先保存起来
            head->next = cur;//将当前节点移动到head的后面
            cur->pre = head;//当前节点cur的pre指向head
            next->pre = cur;
            cur->next = next;
        }

        node* deletecurrentnode(node* cur)//移除当前节点
        {
            cur->pre->next = cur->next;
            cur->next->pre = cur->pre;
            return cur;
        }
        void makerecently(node* cur)
        {
            node* temp = deletecurrentnode(cur);// 删除 cur，要重新插入到对头
            movetohead(temp);//cur放到队头去
        }
        int get(int key)
        {
            int ret = -1;
            if ( map.count(key))
            {
                node* temp = map[key];
                makerecently(temp);// 将 key 变为最近使用
                ret = temp->val;
            }
            return ret;
        }

        void put(int key, int value) {
            if ( map.count(key))
            {
                // 修改 key 的值
                node* temp = map[key];
                temp->val = value;
                // 将 key 变为最近使用
                makerecently(temp);
            }
            else
            {
                node* cur = new node(key, value);
                if( map.size()== size )
                {
                    // 链表头部就是最久未使用的 key
                    node *temp = deletecurrentnode(tail->pre);
                    map.erase(temp->key);
                }
                movetohead(cur);
                map[key] = cur;

            }
        
        }

        unordered_map<int, node*> map;
        int size;
        node* head, *tail;

    };
```



**python**

```python
"""
所谓LRU缓存，根本的难点在于记录最久被使用的键值对，这就设计到排序的问题，
在python中，天生具备排序功能的字典就是OrderDict。
注意到，记录最久未被使用的键值对的充要条件是将每一次put/get的键值对都定义为
最近访问，那么最久未被使用的键值对自然就会排到最后。
如果你深入python OrderDict的底层实现，就会知道它的本质是个双向链表+字典。
它内置支持了
1. move_to_end来重排链表顺序，它可以让我们将最近访问的键值对放到最后面
2. popitem来弹出键值对，它既可以弹出最近的，也可以弹出最远的，弹出最远的就是我们要的操作。
"""
from collections import OrderedDict
class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity  # cache的容量
    self.visited = OrderedDict()  # python内置的OrderDict具备排序的功能
    
  def get(self, key: int) -> int:
    if key not in self.visited:
      return -1
    self.visited.move_to_end(key)  # 最近访问的放到链表最后，维护好顺序
    return self.visited[key]

  def put(self, key: int, value: int) -> None:
    if key not in self.visited and len(self.visited) == self.capacity:
      # last=False时，按照FIFO顺序弹出键值对
      # 因为我们将最近访问的放到最后，所以最远访问的就是最前的，也就是最first的，故要用FIFO顺序
      self.visited.popitem(last=False)
      self.visited[key]=value
      self.visited.move_to_end(key)    # 最近访问的放到链表最后，维护好顺序


```

### 2 如何高效寻找素数

#### 2.1 设计

```java
int countPrimes(int n) {
    boolean[] isPrim = new boolean[n];
    Arrays.fill(isPrim, true);
    for (int i = 2; i * i < n; i++) 
        if (isPrim[i]) 
            for (int j = i * i; j < n; j += i) 
                isPrim[j] = false;
    
    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim[i]) count++;
    
    return count;
}
```




#### 2.2 其他实现

**C++实现**

[204.计数质数](https://leetcode-cn.com/problems/count-primes)

统计所有小于非负整数 n 的质数的数量。

 

	示例 1：

	输入：n = 10
	输出：4
	解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。


	采用的算法是埃拉托斯特尼筛法
	埃拉托斯特尼筛法的具体内容就是：**要得到自然数n以内的全部素数，必须把不大于根号n的所有素数的倍数剔除，剩下的就是素数。**
	同时考虑到大于2的偶数都不是素数，所以可以进一步优化成：**要得到自然数n以内的全部素数，必须把不大于根号n的所有素数的奇数倍剔除，剩下的奇数就是素数。**
	此算法其实就是上面的Java解法所采用的。

这里提供C++的代码：
```C++
class Solution {
  public:
  int countPrimes(int n) {
    int res = 0;
    bool prime[n+1];
    for(int i = 0; i < n; ++i)
      prime[i] = true;

    for(int i = 2; i <= sqrt(n); ++i)   //计数过程 
    {                                   //外循环优化，因为判断一个数是否为质数只需要整除到sqrt(n)，反推亦然
      if(prime[i])
      {
        for(int j = i * i; j < n; j += i)   //内循环优化，i*i之前的比如i*2，i*3等，在之前的循环中已经验证了
        {
          prime[j] = false;
        }
      }      
    }
    for (int i = 2; i < n; ++i)
      if (prime[i])  res++;     //最后遍历统计一遍，存入res

    return res;    
  }
};
```

### 3 二分查找应用

[875.爱吃香蕉的珂珂](https://leetcode-cn.com/problems/koko-eating-bananas)

珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。


	示例 1：

	输入: piles = [3,6,7,11], H = 8
	输出: 4


[1011.在D天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days)

传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

 

#### 3.1  koko偷香蕉

珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

示例 1：

输入: piles = [3,6,7,11], H = 8

输出: 4

```java
int minEatingSpeed(int[] piles, int H) {
    // 套用搜索左侧边界的算法框架
    int left = 1, right = getMax(piles) + 1;
    while (left < right) {
        // 防止溢出
        int mid = left + (right - left) / 2;
        if (canFinish(piles, mid, H)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

```java
// 时间复杂度 O(N)
boolean canFinish(int[] piles, int speed, int H) {
    int time = 0;
    for (int n : piles) {
        time += timeOf(n, speed);
    }
    return time <= H;
}

int timeOf(int n, int speed) {
    return (n / speed) + ((n % speed > 0) ? 1 : 0);
}

int getMax(int[] piles) {
    int max = 0;
    for (int n : piles)
        max = Math.max(n, max);
    return max;
}
```


#### 3.2 运输问题：

要在 `D` 天内运输完所有货物，货物不可分割，如何确定运输的最小载重呢（下文称为 `cap`）？

其实本质上和 Koko 吃香蕉的问题一样的，首先确定 `cap` 的最小值和最大值分别为 `max(weights)` 和 `sum(weights)`。

我们要求**最小载重**，所以可以用搜索左侧边界的二分查找算法优化线性搜索：

```java
// 寻找左侧边界的二分查找
int shipWithinDays(int[] weights, int D) {
	// 载重可能的最小值
    int left = getMax(weights);
	// 载重可能的最大值 + 1
    int right = getSum(weights) + 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (canFinish(weights, D, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

// 如果载重为 cap，是否能在 D 天内运完货物？
boolean canFinish(int[] w, int D, int cap) {
    int i = 0;
    for (int day = 0; day < D; day++) {
        int maxCap = cap;
        while ((maxCap -= w[i]) >= 0) {
            i++;
            if (i == w.length)
                return true;
        }
    }
    return false;
}
```

#### 3.3 其他语言实现

**c++**

[cchroot](https://github.com/cchroot) 提供 C++ 代码：

```c++
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int H) {
        // 二分法查找最小速度
        // 初始化最小速度为 1，最大速度为题目设定的最大值 10^9
        // 这里也可以遍历 piles 数组，获取数组中的最大值，设置 right 为数组中的最大值即可(因为每堆香蕉1小时吃完是最快的)
        // log2(10^9) 约等于30，次数不多，所以这里暂时就不采取遍历获取最大值了
        int left = 1, right = pow(10, 9);
        while (left < right) { // 二分法基本的防止溢出
            int mid = left + (right - left) / 2;
            // 以 mid 的速度吃香蕉，是否能在 H 小时内吃完香蕉
            if (!canFinish(piles, mid, H))
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }

    // 以 speed 的速度是否能把香蕉吃完
    bool canFinish(vector<int>& piles, int speed, int H) {
        int time = 0;
        // 遍历累加时间 time
        for (int p: piles)
            time += (p - 1) / speed + 1;
        return time <= H; // time 小于等于 H 说明能在 H 小时吃完返回 true, 否则返回 false
    }
};
```

**python**

[tonytang731](https://https://github.com/tonytang731) 提供 Python3 代码：

```python
import math

class Solution:
    def minEatingSpeed(self, piles, H):
        # 初始化起点和终点， 最快的速度可以一次拿完最大的一堆
        start = 1
        end = max(piles)
        
        # while loop进行二分查找
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            # 如果中点所需时间大于H, 我们需要加速， 将起点设为中点
            if self.timeH(piles, mid) > H:
                start = mid
            # 如果中点所需时间小于H, 我们需要减速， 将终点设为中点
            else:
                end = mid
                
        # 提交前确认起点是否满足条件，我们要尽量慢拿
        if self.timeH(piles, start) <= H:
            return start
        
        # 若起点不符合， 则中点是答案
        return end
            
        
        
    def timeH(self, piles, K):
        # 初始化时间
        H = 0
        
        #求拿每一堆需要多长时间
        for pile in piles:
            H += math.ceil(pile / K)
            
        return H
```


### 4 如何高效解决接雨水问题

[42.接雨水](https://leetcode-cn.com/problems/trapping-rain-water)

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
 
#### 4.1 暴力

```cpp
int trap(vector<int>& height) {
    int n = height.size();
    int res = 0;
    for (int i = 1; i < n - 1; i++) {
        int l_max = 0, r_max = 0;
        // 找右边最高的柱子
        for (int j = i; j < n; j++)
            r_max = max(r_max, height[j]);
        // 找左边最高的柱子
        for (int j = i; j >= 0; j--)
            l_max = max(l_max, height[j]);
        // 如果自己就是最高的话，
        // l_max == r_max == height[i]
        res += min(l_max, r_max) - height[i];
    }
    return res;
}
```


#### 4.2 备忘录优化


```cpp
int trap(vector<int>& height) {
    if (height.empty()) return 0;
    int n = height.size();
    int res = 0;
    // 数组充当备忘录
    vector<int> l_max(n), r_max(n);
    // 初始化 base case
    l_max[0] = height[0];
    r_max[n - 1] = height[n - 1];
    // 从左向右计算 l_max
    for (int i = 1; i < n; i++)
        l_max[i] = max(height[i], l_max[i - 1]);
    // 从右向左计算 r_max
    for (int i = n - 2; i >= 0; i--) 
        r_max[i] = max(height[i], r_max[i + 1]);
    // 计算答案
    for (int i = 1; i < n - 1; i++) 
        res += min(l_max[i], r_max[i]) - height[i];
    return res;
}
```

#### 4.3 双指针解法

```cpp
int trap(vector<int>& height) {
    if (height.empty()) return 0;
    int n = height.size();
    int left = 0, right = n - 1;
    int res = 0;
    
    int l_max = height[0];
    int r_max = height[n - 1];
    
    while (left <= right) {
        l_max = max(l_max, height[left]);
        r_max = max(r_max, height[right]);
        
        // res += min(l_max, r_max) - height[i]
        if (l_max < r_max) {
            res += l_max - height[left];
            left++; 
        } else {
            res += r_max - height[right];
            right--;
        }
    }
    return res;
}
```

#### 4.4 其他语言


[Yifan Zhang](https://github.com/FanFan0919) 提供 java 代码

**双指针解法**：时间复杂度 O(N)，空间复杂度 O(1)

对cpp版本的解法有非常微小的优化。  
因为我们每次循环只会选 left 或者 right 处的柱子来计算，因此我们并不需要在每次循环中同时更新`maxLeft`和`maxRight`。  
我们可以先比较 `maxLeft` 和 `maxRight`，决定这次选择计算的柱子是 `height[left]` 或者 `height[right]` 后再更新对应的 `maxLeft` 或 `maxRight`。  
当然这并不会在时间上带来什么优化，只是提供一种思路。

```java
class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int left = 0, right = height.length - 1;
        int maxLeft = height[left], maxRight = height[right];
        int res = 0;
        
        while (left < right) {
            // 比较 maxLeft 和 maxRight，决定这次计算 left 还是 right 处的柱子
            if (maxLeft < maxRight) {
                left++;
                maxLeft = Math.max(maxLeft, height[left]);  // update maxLeft
                res += maxLeft - height[left];
            } else {
                right--;
                maxRight = Math.max(maxRight, height[right]);   // update maxRight
                res += maxRight - height[right];
            }
        }
        
        return res;
    }
}
```


### 5 如何去除有序数组的重复元素

#### 5.1 描述

**对于数组相关的算法问题，有一个通用的技巧：要尽量避免在中间删除元素，那我就先想办法把这个元素换到最后去**。这样的话，最终待删除的元素都拖在数组尾部，一个一个 pop 掉就行了，每次操作的时间复杂度也就降低到 O(1) 了。

**双指针**

我们让慢指针 `slow` 走左后面，快指针 `fast` 走在前面探路，找到一个不重复的元素就告诉 `slow` 并让 `slow` 前进一步。这样当 `fast` 指针遍历完整个数组 `nums` 后，**`nums[0..slow]` 就是不重复元素，之后的所有元素都是重复元素**。

```java
int removeDuplicates(int[] nums) {
    int n = nums.length;
    if (n == 0) return 0;
    int slow = 0, fast = 1;
    while (fast < n) {
        if (nums[fast] != nums[slow]) {
            slow++;
            // 维护 nums[0..slow] 无重复
            nums[slow] = nums[fast];
        }
        fast++;
    }
    // 长度为索引 + 1
    return slow + 1;
}
```

**一个有序链表去重**

```java
ListNode deleteDuplicates(ListNode head) {
    if (head == null) return null;
    ListNode slow = head, fast = head.next;
    while (fast != null) {
        if (fast.val != slow.val) {
            // nums[slow] = nums[fast];
            slow.next = fast;
            // slow++;
            slow = slow.next;
        }
        // fast++
        fast = fast.next;
    }
    // 断开与后面重复元素的连接
    slow.next = null;
    return head;
}
```


##### 5.2 python实现

[eric wang](https://www.github.com/eric496) 提供有序数组 Python3 代码 

```python
def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    
    if n == 0:
        return 0
    
    slow, fast = 0, 1
    
    while fast < n:
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            
        fast += 1
        
    return slow + 1
```

[eric wang](https://www.github.com/eric496) 提供有序链表 Python3 代码 

```python
def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return head
    
    slow, fast = head, head.next
    
    while fast:
        if fast.val != slow.val:
            slow.next = fast
            slow = slow.next
            
        fast = fast.next

    # 断开与后面重复元素的连接   
    slow.next = None
    return head
```

### 6 如何寻找最长回文子串

[5.最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring)

给你一个字符串 s，找到 s 中最长的回文子串。

	示例 1：

	输入：s = "babad"
	输出："bab"
	解释："aba" 同样是符合题意的答案。



下面，就来说一下正确的思路，如何使用双指针。

**寻找回文串的问题核心思想是：从中间开始向两边扩散来判断回文串**。对于最长回文子串，就是这个意思：

```python
for 0 <= i < len(s):
    找到以 s[i] 为中心的回文串
    更新答案
```

但是呢，我们刚才也说了，回文串的长度可能是奇数也可能是偶数，如果是 `abba`这种情况，没有一个中心字符，上面的算法就没辙了。所以我们可以修改一下：

```python
for 0 <= i < len(s):
    找到以 s[i] 为中心的回文串
    找到以 s[i] 和 s[i+1] 为中心的回文串
    更新答案
```

#### 6.1 实现

要传入两个指针 `l` 和 `r` 呢？**因为这样实现可以同时处理回文串长度为奇数和偶数的情况**：

```python
for 0 <= i < len(s):
    # 找到以 s[i] 为中心的回文串
    palindrome(s, i, i)
    # 找到以 s[i] 和 s[i+1] 为中心的回文串
    palindrome(s, i, i + 1)
    更新答案
```

下面看下 `longestPalindrome` 的完整代码：

```cpp
string longestPalindrome(string s) {
    string res;
    for (int i = 0; i < s.size(); i++) {
        // 以 s[i] 为中心的最长回文子串
        string s1 = palindrome(s, i, i);
        // 以 s[i] 和 s[i+1] 为中心的最长回文子串
        string s2 = palindrome(s, i, i + 1);
        // res = longest(res, s1, s2)
        res = res.size() > s1.size() ? res : s1;
        res = res.size() > s2.size() ? res : s2;
    }
    return res;
}
```

#### 6.2 其他语言实现

[5.最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring)

**java**

[cchromt](https://github.com/cchroot) 提供 Java 代码：

```java
// 中心扩展算法
class Solution {
    public String longestPalindrome(String s) {
        // 如果字符串长度小于2，则直接返回其本身
        if (s.length() < 2) {
            return s;
        }
        String res = "";
        for (int i = 0; i < s.length() - 1; i++) {
            // 以 s.charAt(i) 为中心的最长回文子串
            String s1 = palindrome(s, i, i);
            // 以 s.charAt(i) 和 s.charAt(i+1) 为中心的最长回文子串
            String s2 = palindrome(s, i, i + 1);
            res = res.length() > s1.length() ? res : s1;
            res = res.length() > s2.length() ? res : s2;
        }
        return res;
    }

    public String palindrome(String s, int left, int right) {
        // 索引未越界的情况下，s.charAt(left) == s.charAt(right) 则继续向两边拓展
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // 这里要注意，跳出 while 循环时，恰好满足 s.charAt(i) != s.charAt(j)，因此截取的的字符串为[left+1, right-1]
        return s.substring(left + 1, right);
    }
}
```


[enrilwang](https://github.com/enrilwang) 提供 Python 代码：

```python
# 中心扩展算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #用n来装字符串长度，res来装答案
        n = len(s)  
        res = str()
        #字符串长度小于2，就返回本身
        if n < 2: return s
        for i in range(n-1):
            #oddstr是以i为中心的最长回文子串
            oddstr = self.centerExtend(s,i,i)
            #evenstr是以i和i+1为中心的最长回文子串
            evenstr = self.centerExtend(s,i,i+1)
            temp = oddstr if len(oddstr)>len(evenstr) else evenstr
            if len(temp)>len(res):res=temp
        
        return res

    def centerExtend(self,s:str,left,right)->str:
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        #这里要注意，跳出while循环时，恰好s[left] != s[right]
        return s[left+1:right]


```


### 7  如何k个一组反转链表

25.K个一组翻转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


#### 7.1 实现

```java
ListNode reverseKGroup(ListNode head, int k) {
    if (head == null) return null;
    // 区间 [a, b) 包含 k 个待反转元素
    ListNode a, b;
    a = b = head;
    for (int i = 0; i < k; i++) {
        // 不足 k 个，不需要反转，base case
        if (b == null) return head;
        b = b.next;
    }
    // 反转前 k 个元素
    ListNode newHead = reverse(a, b);
    // 递归反转后续链表并连接起来
    a.next = reverseKGroup(b, k);
    return newHead;
}
```


### 8 如何判定括号合法性

题目很简单，输入一个字符串，其中包含 [](){} 六种括号，请你判断这个字符串组成的括号是否合法。

Input: "()[]{}"
Output: true

Input: "([)]"
Output: false

Input: "{[]}"
Output: true

#### 8.1 实现

栈是一种先进后出的数据结构，处理括号问题的时候尤其有用。

我们这道题就用一个名为 `left` 的栈代替之前思路中的 `left` 变量，**遇到左括号就入栈，遇到右括号就去栈中寻找最近的左括号，看是否匹配**。

```cpp
bool isValid(string str) {
    stack<char> left;
    for (char c : str) {
        if (c == '(' || c == '{' || c == '[')
            left.push(c);
        else // 字符 c 是右括号
            if (!left.empty() && leftOf(c) == left.top())
                left.pop();
            else
                // 和最近的左括号不匹配
                return false;
    }
    // 是否所有的左括号都被匹配了
    return left.empty();
}

char leftOf(char c) {
    if (c == '}') return '{';
    if (c == ')') return '(';
    return '[';
}
```

#### 8.2 其他语言实现

[20.有效的括号](https://leetcode-cn.com/problems/valid-parentheses)

**python**

```python
def isValid(self, s: str) -> bool:
    left = []
    leftOf = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for c in s:
        if c in '([{':
            left.append(c)
        elif left and leftOf[c]==left[-1]: # 右括号 + left不为空 + 和最近左括号能匹配
            left.pop()
        else: # 右括号 + （left为空 / 和堆顶括号不匹配）
            return False
        
    # left中所有左括号都被匹配则return True 反之False
    return not left
```



**java**

```java
//基本思想：每次遇到左括号时都将相对应的右括号'）'，']'或'}'推入堆栈
//如果在字符串中出现右括号，则需要检查堆栈是否为空，以及顶部元素是否与该右括号相同。如果不是，则该字符串无效。
//最后，我们还需要检查堆栈是否为空
public boolean isValid(String s) {
  Deque<Character> stack = new ArrayDeque<>();
  for(char c : s.toCharArray()){
    //是左括号就将相对应的右括号入栈
    if(c=='(') {
      stack.offerLast(')');
    }else if(c=='{'){
      stack.offerLast('}');
    }else if(c=='['){
      stack.offerLast(']');   
    }else if(stack.isEmpty() || stack.pollLast()!=c){//出现右括号，检查堆栈是否为空，以及顶部元素是否与该右括号相同
      return false;
    }
  }
  return stack.isEmpty();
}


```

### 9 如何寻找消失的元素

448. 找到所有数组中消失的数字

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]


#### 9.1 实现

刚才我们的思路是把两个和都加出来然后相减，为了避免溢出，干脆一边求和一边减算了。很类似刚才位运算解法的思路，仍然假设 `nums = [0,3,1,4]`，先补一位索引再让元素跟索引配对：


我们让每个索引减去其对应的元素，再把相减的结果加起来，不就是那个缺失的元素吗？

```java
public int missingNumber(int[] nums) {
    int n = nums.length;
    int res = 0;
    // 新补的索引
    res += n - 0;
    // 剩下索引和元素的差加起来
    for (int i = 0; i < n; i++) 
        res += i - nums[i];
    return res;
}
```

#### 9.1 其他语言实现

**python**

```python
def missingNumber(self, nums: List[int]) -> int:
    #思路1，位运算
    res = len(nums)
    for i,num in enumerate(nums):
        res ^= i^num
        return res
```

```python
def missingNumber(self, nums: List[int]) -> int:
    #思路2，求和
    n = len(nums)
    return n*(n+1)//2-sum(nums)
```

```python
def missingNumber(self, nums: List[int]) -> int:
    #思路3，防止整形溢出的优化
    res = len(nums)
    for i,num in enumerate(nums):
        res+=i-num
        return res
```

事实上，在python3中不存在整数溢出的问题（只要内存放得下），思路3的优化提升并不大，不过看上去有内味了哈...

**c++**

[happy-yuxuan](https://github.com/happy-yuxuan) 提供 三种方法的 C++ 代码：

```c++
// 方法：异或元素和索引
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int res = 0;
    // 先和新补的索引异或一下
    res ^= n;
    // 和其他的元素、索引做异或
    for (int i = 0; i < n; i++)
        res ^= i ^ nums[i];
    return res;
}
```

```c++
// 方法：等差数列求和
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    // 公式：(首项 + 末项) * 项数 / 2
    int expect = (0 + n) * (n + 1) / 2;
    int sum = 0;
    for (int x : nums) 
        sum += x;
    return expect - sum;
}
```

```c++
// 方法：防止整型溢出
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int res = 0;
    // 新补的索引
    res += n - 0;
    // 剩下索引和元素的差加起来
    for (int i = 0; i < n; i++) 
        res += i - nums[i];
    return res;
}
```


### 10 如何寻找缺失和重复的元素

[645.错误的集合](https://leetcode-cn.com/problems/set-mismatch)


给一个长度为 N 的数组 nums，其中本来装着 [1..N] 这 N 个元素，无序。但是现在出现了一些错误，nums 中的一个元素出现了重复，也就同时导致了另一个元素的缺失。请你写一个算法，找到 nums 中的重复元素和缺失元素的值。

	// 返回两个数字，分别是 {dup, missing}
	vector<int> findErrorNums(vector<int>& nums);
	
比如说输入：nums = [1,2,2,4]，算法返回 [2,3]。

对于这种数组问题，**关键点在于元素和索引是成对儿出现的，常用的方法是排序、异或、映射**。

映射的思路就是我们刚才的分析，将每个索引和元素映射起来，通过正负号记录某个元素是否被映射。

排序的方法也很好理解，对于这个问题，可以想象如果元素都被从小到大排序，如果发现索引对应的元素如果不相符，就可以找到重复和缺失的元素。

异或运算也是常用的，因为异或性质 `a ^ a = 0, a ^ 0 = a`，如果将索引和元素同时异或，就可以消除成对儿的索引和元素，留下的就是重复或者缺失的元素。可以看看前文「寻找缺失元素」，介绍过这种方法。


#### 10.1 实现

```cpp
vector<int> findErrorNums(vector<int>& nums) {
    int n = nums.size();
    int dup = -1;
    for (int i = 0; i < n; i++) {
        // 现在的元素是从 1 开始的
        int index = abs(nums[i]) - 1;
        if (nums[index] < 0)
            dup = abs(nums[i]);
        else
            nums[index] *= -1;
    }

    int missing = -1;
    for (int i = 0; i < n; i++)
        if (nums[i] > 0)
            // 将索引转换成元素
            missing = i + 1;
    
    return {dup, missing};
}
```

#### 10.2 其他实现

[zhuli](https://github.com/1097452462 "zhuli")提供的Java代码：
```java
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int dup = -1;
        for (int i = 0; i < n; i++) {
	    // 元素是从 1 开始的
            int index = Math.abs(nums[i]) - 1;
            // nums[index] 小于 0 则说明重复访问
            if (nums[index] < 0)
                dup = Math.abs(nums[i]);
            else
                nums[index] *= -1;
        }
        int missing = -1;
        for (int i = 0; i < n; i++)
            // nums[i] 大于 0 则说明没有访问
            if (nums[i] > 0)
		// 将索引转换成元素
                missing = i + 1;
        return new int[]{dup, missing};
    }
}
```






