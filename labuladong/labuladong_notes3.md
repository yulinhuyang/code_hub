## 第二章、数据结构系列

### 1 学习算法和刷题的思路指南

数据结构的基本操作

数组遍历框架，典型的线性迭代结构：

```java
void traverse(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        // 迭代访问 arr[i]
    }
}
```

链表遍历框架，兼具迭代和递归结构：

```java
/* 基本的单链表节点 */
class ListNode {
    int val;
    ListNode next;
}

void traverse(ListNode head) {
    for (ListNode p = head; p != null; p = p.next) {
        // 迭代访问 p.val
    }
}

void traverse(ListNode head) {
    // 递归访问 head.val
    traverse(head.next)
}
```

二叉树遍历框架，典型的非线性递归遍历结构：

```java
/* 基本的二叉树节点 */
class TreeNode {
    int val;
    TreeNode left, right;
}

void traverse(TreeNode root) {
    traverse(root.left)
    traverse(root.right)
}
```

你看二叉树的递归遍历方式和链表的递归遍历方式，相似不？再看看二叉树结构和单链表结构，相似不？如果再多几条叉，N 叉树你会不会遍历？

二叉树框架可以扩展为 N 叉树的遍历框架：

```java
/* 基本的 N 叉树节点 */
class TreeNode {
    int val;
    TreeNode[] children;
}

void traverse(TreeNode root) {
    for (TreeNode child : root.children)
        traverse(child);
}
```

N 叉树的遍历又可以扩展为图的遍历，因为图就是好几 N 叉棵树的结合体。你说图是可能出现环的？这个很好办，用个布尔数组 visited 做标记就行了，这里就不写代码了。

### 2 二叉堆详解实现优先级队列

因为，二叉堆其实就是一种特殊的二叉树（完全二叉树），只不过存储在数组里。一般的链表二叉树，我们操作节点的指针，而在数组里，我们把数组索引作为指针：

```java
// 父节点的索引
int parent(int root) {
    return root / 2;
}
// 左孩子的索引
int left(int root) {
    return root * 2;
}
// 右孩子的索引
int right(int root) {
    return root * 2 + 1;
}
```
数据结构的功能无非增删查该，优先级队列有两个主要 API，分别是 `insert` 插入一个元素和 `delMax` 删除最大元素（如果底层用最小堆，那么就是 `delMin`）。

```java
public class MaxPQ
    <Key extends Comparable<Key>> {
    // 存储元素的数组
    private Key[] pq;
    // 当前 Priority Queue 中的元素个数
    private int N = 0;

    public MaxPQ(int cap) {
        // 索引 0 不用，所以多分配一个空间
        pq = (Key[]) new Comparable[cap + 1];
    }

    /* 返回当前队列中最大元素 */
    public Key max() {
        return pq[1];
    }

    /* 插入元素 e */
    public void insert(Key e) {...}

    /* 删除并返回当前队列中最大元素 */
    public Key delMax() {...}

    /* 上浮第 k 个元素，以维护最大堆性质 */
    private void swim(int k) {...}

    /* 下沉第 k 个元素，以维护最大堆性质 */
    private void sink(int k) {...}

    /* 交换数组的两个元素 */
    private void exch(int i, int j) {
        Key temp = pq[i];
        pq[i] = pq[j];
        pq[j] = temp;
    }

    /* pq[i] 是否比 pq[j] 小？ */
    private boolean less(int i, int j) {
        return pq[i].compareTo(pq[j]) < 0;
    }

    /* 还有 left, right, parent 三个方法 */
}
```


**上浮的代码实现：**

```java
private void swim(int k) {
    // 如果浮到堆顶，就不能再上浮了
    while (k > 1 && less(parent(k), k)) {
        // 如果第 k 个元素比上层大
        // 将 k 换上去
        exch(parent(k), k);
        k = parent(k);
    }
}
```

```java
private void sink(int k) {
    // 如果沉到堆底，就沉不下去了
    while (left(k) <= N) {
        // 先假设左边节点较大
        int older = left(k);
        // 如果右边节点存在，比一下大小
        if (right(k) <= N && less(older, right(k)))
            older = right(k);
        // 结点 k 比俩孩子都大，就不必下沉了
        if (less(older, k)) break;
        // 否则，不符合最大堆的结构，下沉 k 结点
        exch(k, older);
        k = older;
    }
}
```


```java
public void insert(Key e) {
    N++;
    // 先把新元素加到最后
    pq[N] = e;
    // 然后让它上浮到正确的位置
    swim(N);
}
```


```java
public Key delMax() {
    // 最大堆的堆顶就是最大元素
    Key max = pq[1];
    // 把这个最大元素换到最后，删除之
    exch(1, N);
    pq[N] = null;
    N--;
    // 让 pq[1] 下沉到正确位置
    sink(1);
    return max;
}
```


###  3 LRU算法

LRU 缓存淘汰算法就是一种常用策略。LRU 的全称是 Least Recently Used，也就是说我们认为最近使用过的数据应该是是「有用的」，很久都没用过的数据应该是无用的，内存满了就优先删那些很久没用过的数据。

[146.LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)

#### 3.1 实现

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

#### 3.2 其他语言实现

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

### 4 二叉搜索树操作集锦

#### 4.1 设计思路

100.相同的树

450.删除二叉搜索树中的节点

701.二叉搜索树中的插入操作

700.二叉搜索树中的搜索

98.验证二叉搜索树

二叉树算法的设计的总路线：明确一个节点要做的事情，然后剩下的事抛给框架。

void traverse(TreeNode root) {
    // root 需要做什么？在这做。
    // 其他的不用 root 操心，抛给框架
    traverse(root.left);
    traverse(root.right);
}

举两个简单的例子体会一下这个思路，热热身。

**1. 如何把二叉树所有的节点中的值加一？**

```java
void plusOne(TreeNode root) {
    if (root == null) return;
    root.val += 1;

    plusOne(root.left);
    plusOne(root.right);
}
```

**2. 如何判断两棵二叉树是否完全相同？**

```java
boolean isSameTree(TreeNode root1, TreeNode root2) {
    // 都为空的话，显然相同
    if (root1 == null && root2 == null) return true;
    // 一个为空，一个非空，显然不同
    if (root1 == null || root2 == null) return false;
    // 两个都非空，但 val 不一样也不行
    if (root1.val != root2.val) return false;

    // root1 和 root2 该比的都比完了
    return isSameTree(root1.left, root2.left)
        && isSameTree(root1.right, root2.right);
}
```

**在 BST 中查找一个数是否存在**

```java
boolean isInBST(TreeNode root, int target) {
    if (root == null) return false;
    if (root.val == target) return true;

    return isInBST(root.left, target)
        || isInBST(root.right, target);
}
```


**零、判断 BST 的合法性**

```java
boolean isValidBST(TreeNode root) {
    return isValidBST(root, null, null);
}

boolean isValidBST(TreeNode root, TreeNode min, TreeNode max) {
    if (root == null) return true;
    if (min != null && root.val <= min.val) return false;
    if (max != null && root.val >= max.val) return false;
    return isValidBST(root.left, min, root) 
        && isValidBST(root.right, root, max);
}
```

**针对 BST 的遍历框架**：

```java
void BST(TreeNode root, int target) {
    if (root.val == target)
        // 找到目标，做点什么
    if (root.val < target) 
        BST(root.right, target);
    if (root.val > target)
        BST(root.left, target);
}
```

**在 BST 中插入一个数**

```java
TreeNode insertIntoBST(TreeNode root, int val) {
    // 找到空位置插入新节点
    if (root == null) return new TreeNode(val);
    // if (root.val == val)
    //     BST 中一般不会插入已存在元素
    if (root.val < val) 
        root.right = insertIntoBST(root.right, val);
    if (root.val > val) 
        root.left = insertIntoBST(root.left, val);
    return root;
}
```

**在 BST 中删除一个数**

```java
TreeNode deleteNode(TreeNode root, int key) {
    if (root == null) return null;
    if (root.val == key) {
        // 这两个 if 把情况 1 和 2 都正确处理了
        if (root.left == null) return root.right;
        if (root.right == null) return root.left;
        // 处理情况 3
        TreeNode minNode = getMin(root.right);
        root.val = minNode.val;
        root.right = deleteNode(root.right, minNode.val);
    } else if (root.val > key) {
        root.left = deleteNode(root.left, key);
    } else if (root.val < key) {
        root.right = deleteNode(root.right, key);
    }
    return root;
}

TreeNode getMin(TreeNode node) {
    // BST 最左边的就是最小的
    while (node.left != null) node = node.left;
    return node;
} 
```

#### 4.2 其他语言实现


[100.相同的树](https://leetcode-cn.com/problems/same-tree)

[450.删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst)

[701.二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree)

[700.二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree)

[98.验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree)


**c++实现**

[dekunma](https://www.linkedin.com/in/dekun-ma-036a9b198/)提供第98题C++代码：

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // 用helper method求解
        return isValidBST(root, nullptr, nullptr);
    }

    bool isValidBST(TreeNode* root, TreeNode* min, TreeNode* max) {
        // base case, root为nullptr
        if (!root) return true;

        // 不符合BST的条件
        if (min && root->val <= min->val) return false;
        if (max && root->val >= max->val) return false;

        // 向左右子树分别递归求解
        return isValidBST(root->left, min, root) 
            && isValidBST(root->right, root, max);
    }
};
```


[yanggg1997](https://github.com/yanggg1997)提供第100题C++代码：

``` c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
		// 若当前节点均为空，则此处相同
        if(!p && !q) return true;	
        // 若当前节点在一棵树上有而另一棵树上为空，则两棵树不同
        if(!p && q) return false;	
        if(p && !q) return false;
        // 若当前节点在两棵树上均存在。
        if(p->val != q->val)
        {
            return false;
        }
        else
        {
            // 向左右子树分别递归判断
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
    }
};
```

**python实现**

[ChenjieXu](https://github.com/ChenjieXu)提供第98题Python3代码：

```python
def isValidBST(self, root):
        # 递归函数
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            # 右节点
            if not helper(node.right, val, upper):
                return False
            # 左节点
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
        
```

[lixiandea](https://github.com/lixiandea)提供第100题Python3代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    '''
    当前节点值相等且树的子树相等，则树相等。
    递归退出条件：两个节点存在一个节点为空
    '''
        if p == None:
            if q == None:
                return True
            else:
                return False
        if q == None:
            return False
        # 当前节点相同且左子树和右子树分别相同
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```


[Edwenc](https://github.com/Edwenc) 提供 leetcode第450题的python3 代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        #  如果没有树  直接返回None
        if root == None:
            return None

        #  如果要删除的结点  就是当前结点
        if root.val == key:
            #  左子树为空  只有右子树需要被更新  直接返回
            if root.left == None:
                return root.right
            #  右子树为空  只有左子树需要被更新  直接返回
            if root.right== None:
                return root.left

            #  找出此结点左子树的最大值
            #  用这个最大值  来代替当前结点
            #  再在左子树中递归地删除这个最大值结点
            big = self.getMax( root.left )
            root.val = big.val
            root.left = self.deleteNode( root.left , big.val )
        
        #  当前结点较大  它的左子树中需要删除节点  递归到左子树
        elif root.val > key:
            root.left = self.deleteNode( root.left , key)
        #  当前结点较小  它的右子树中需要删除节点  递归到右子树
        else:
            root.right= self.deleteNode( root.right, key)

        return root

    #  辅助函数
    #  功能是找出此二叉搜索树中最大元素的结点  并返回此结点
    def getMax( self , node ):
        #  一直找它的右子树  直到为空
        while node.right:
            node = node.right
        return node
```

**java实现**


```
/**
* 第【98】题的扩展解法：
* 对于BST，有一个重要的性质，即“BST的中序遍历是单调递增的”。抓住这个性质，我们可以通过中序遍历来判断该二叉树是不是BST。
* 我们定义preNode节点表示上一个遍历的节点，在中序遍历的时候，比较当前节点和preNode节点的大小，一旦有节点小于或等于前一个节点，则不满足BST的规则，直接返回false，否则遍历结束，返回true。
*/
TreeNode preNode = null;
public boolean isValidBST(TreeNode root) {
    if (root == null) return true;

    boolean leftRes = isValidBST(root.left);

    if (preNode != null && root.val <= preNode.val) {
        return false;
    }
    preNode = root;

    boolean rightRes = isValidBST(root.right);

    return leftRes && rightRes;
}
```

###  5 特殊数据结构：单调栈

单调栈实际上就是栈，只是利用了一些巧妙的逻辑，使得每次新元素入栈后，栈内的元素都保持有序（单调递增或单调递减）。

Next Greater Number 的原始问题，这是力扣第 496 题「下一个更大元素 I」：

给你一个数组，返回一个等长的数组，对应索引存储着下一个更大元素，如果没有更大的元素，就存 -1。

函数签名如下：

	vector<int> nextGreaterElement(vector<int>& nums);
	比如说，输入一个数组 nums = [2,1,2,4,3]，你返回数组 [4,2,4,-1,-1]。


#### 5.1 单调栈模板

```cpp
vector<int> nextGreaterElement(vector<int>& nums) {
    vector<int> res(nums.size()); // 存放答案的数组
    stack<int> s;
    // 倒着往栈里放
    for (int i = nums.size() - 1; i >= 0; i--) {
        // 判定个子高矮
        while (!s.empty() && s.top() <= nums[i]) {
            // 矮个起开，反正也被挡着了。。。
            s.pop();
        }
        // nums[i] 身后的 next great number
        res[i] = s.empty() ? -1 : s.top();
        // 
        s.push(nums[i]);
    }
    return res;
}
```

这就是单调队列解决问题的模板。for 循环要从后往前扫描元素，因为我们借助的是栈的结构，倒着入栈，其实是正着出栈。while 循环是把两个「个子高」元素之间的元素排除，因为他们的存在没有意义，前面挡着个「更高」的元素，所以他们不可能被作为后续进来的元素的 Next Great Number 了。


环形数组： 通过 % 运算符求模（余数），来获得环形特效：


```java
int[] arr = {1,2,3,4,5};
int n = arr.length, index = 0;
while (true) {
    print(arr[index % n]);
    index++;
}
```


#### 5.2 实现

```java
// 496.下一个更大元素
// 单调栈解法
public int[] nextGreaterElement(int[] nums1, int[] nums2) {
    Stack<Integer> stack = new Stack <>();
    HashMap<Integer, Integer> map = new HashMap <>();
    int[] result = new int[nums1.length];
    for (int value : nums2) {
        while (!stack.empty() && value > stack.peek()) {
            map.put(stack.pop(), value);
        }
        stack.push(value);
    }
    while (!stack.empty()) {
        map.put(stack.pop(), -1);
    }
    for (int i = 0; i < nums1.length; i++) {
        result[i] = map.get(nums1[i]);
    }
    return result;
}
```

[ZakAnun](https://github.com/ZakAnun) 提供代码

```java
// 739. Daily Temperatures
class Solution {
    public int[] dailyTemperatures(int[] T) {
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[T.length];
        for (int i = 0; i < T.length; i++) {
            // 如果压栈之后不满足单调递减，弹出元素，直至保持单调性
            while (!stack.isEmpty() && T[i] > T[stack.peek()]) {
                int index = stack.pop();
                // 被弹出的元素（T[index]）都是小于当前的元素(T[i])，由于栈内元素单调递减，大于被弹出元素（index）的最近的就是当前元素(i)
                ans[index] = i - index;
            }
            stack.push(i);
        }
        return ans;
    }
}
```

[JiangangZhao](https://github.com/JiangangZhao)提供【503.下一个更大元素II】【java】

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        //数组长度
        int n = nums.length;
        //逻辑拼接，数组长度翻倍
        int len = n*2 - 1;
        //存储结果数组
        int[] res = new int[n];
        //存放索引，不是元素
        LinkedList<Integer> s = new LinkedList<>();
        //从前往后遍历
        for (int i = 0; i < len; ++i) {
            //索引要取模
            int val = nums[i % n];
            //当前元素比栈顶元素大，即是栈顶元素的下一个更大的元素
            while (!s.isEmpty() && val > nums[s.peek()]) {
                res[s.pop()] = val;
            }
            //i<n时入栈
            if (i < n) {
                s.push(i);
            }
        }
        //栈中剩余的索引不存在下一个更大的元素，赋值-1
        while (!s.isEmpty()) {
            res[s.pop()] = -1;
        }
        return res;
    }
}
```

### 6 特殊数据结构：单调队列

239.滑动窗口最大值

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例 1：

	输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
	输出：[3,3,5,5,6,7]
	解释：
	滑动窗口的位置                最大值
	---------------               -----
	[1  3  -1] -3  5  3  6  7       3
	 1 [3  -1  -3] 5  3  6  7       3
	 1  3 [-1  -3  5] 3  6  7       5
	 1  3  -1 [-3  5  3] 6  7       5
	 1  3  -1  -3 [5  3  6] 7       6
	 1  3  -1  -3  5 [3  6  7]      7


#### 6.1 单调队列模板

```cpp
class MonotonicQueue {
private:
    deque<int> data;
public:
    void push(int n) {
        while (!data.empty() && data.back() < n) 
            data.pop_back();
        data.push_back(n);
    }
    
    int max() { return data.front(); }
    
    void pop(int n) {
        if (!data.empty() && data.front() == n)
            data.pop_front();
    }
};

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    MonotonicQueue window;
    vector<int> res;
    for (int i = 0; i < nums.size(); i++) {
        if (i < k - 1) { //先填满窗口的前 k - 1
            window.push(nums[i]);
        } else { // 窗口向前滑动
            window.push(nums[i]);
            res.push_back(window.max());
            window.pop(nums[i - k + 1]);
        }
    }
    return res;
}
```


#### 6.2 其他语言实现

**python**

由[SCUHZS](ttps://github.com/brucecat)提供


```python
from collections import deque

class MonotonicQueue(object):
    def __init__(self):
        # 双端队列
        self.data = deque()

    def push(self, n):
        # 实现单调队列的push方法
        while self.data and self.data[-1] < n:
            self.data.pop()
        self.data.append(n)

    def max(self):
        # 取得单调队列中的最大值
        return self.data[0]

    def pop(self, n):
        # 实现单调队列的pop方法
        if self.data and self.data[0] == n:
            self.data.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列实现的窗口
        window = MonotonicQueue()

        # 结果
        res = []
        
        for i in range(0, len(nums)):
            
            if i < k-1:
                # 先填满窗口前k-1
                window.push(nums[i])
            else:
                # 窗口向前滑动
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i-k+1])
        return res

```

**java**


```java
class Twitter {
    private static int timestamp = 0;
    private static class Tweet {}
    private static class User {}

    /* 还有那几个 API 方法 */
    public void postTweet(int userId, int tweetId) {}
    public List<Integer> getNewsFeed(int userId) {}
    public void follow(int followerId, int followeeId) {}
    public void unfollow(int followerId, int followeeId) {}
}
```


```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int len = nums.length;
        // 判断数组或者窗口长度为0的情况
        if (len * k == 0) {
            return new int[0];
        }

        /*
        采用两端扫描的方法
        将数组分成大小为 k 的若干个窗口, 对每个窗口分别从左往右和从右往左扫描, 记录扫描的最大值
        left[] 记录从左往右扫描的最大值
        right[] 记录从右往左扫描的最大值
         */
        int[] left = new int[len];
        int[] right = new int[len];

        for (int i = 0; i < len; i = i + k) {
            // 每个窗口中的第一个值
            left[i] = nums[i];
            // 窗口的最后边界
            int index = i + k - 1 >= len ? len - 1 : i + k - 1;
            // 每个窗口的最后一个值
            right[index] = nums[index];
            // 对该窗口从左往右扫描
            for (int j = i + 1; j <= index; j++) {
                left[j] = Math.max(left[j - 1], nums[j]);
            }
            // 对该窗口从右往左扫描
            for (int j = index - 1; j >= i; j--) {
                right[j] = Math.max(right[j + 1], nums[j]);
            }
        }

        int[] arr = new int[len - k + 1];

        // 对于第 i 个位置, 它一定是该窗口从右往左扫描数组中的最后一个值, 相对的 i + k - 1 是该窗口从左向右扫描数组中的最后一个位置
        // 对两者取最大值即可
        for (int i = 0; i < len - k + 1; i++) {
            arr[i] = Math.max(right[i], left[i + k - 1]);
        }

        return arr;
    }
}
```

### 7 设计Twitter

355.设计推特

#### 题目

Twitter 和微博功能差不多，我们主要要实现这样几个 API：

```java
class Twitter {

    /** user 发表一条 tweet 动态 */
    public void postTweet(int userId, int tweetId) {}
    
    /** 返回该 user 关注的人（包括他自己）最近的动态 id，
    最多 10 条，而且这些动态必须按从新到旧的时间线顺序排列。*/
    public List<Integer> getNewsFeed(int userId) {}
    
    /** follower 关注 followee，如果 Id 不存在则新建 */
    public void follow(int followerId, int followeeId) {}
    
    /** follower 取关 followee，如果 Id 不存在则什么都不做 */
    public void unfollow(int followerId, int followeeId) {}
}
```

举个具体的例子，方便大家理解 API 的具体用法：

```java
Twitter twitter = new Twitter();

twitter.postTweet(1, 5);
// 用户 1 发送了一条新推文 5

twitter.getNewsFeed(1);
// return [5]，因为自己是关注自己的

twitter.follow(1, 2);
// 用户 1 关注了用户 2

twitter.postTweet(2, 6);
// 用户2发送了一个新推文 (id = 6)

twitter.getNewsFeed(1);
// return [6, 5]
// 解释：用户 1 关注了自己和用户 2，所以返回他们的最近推文
// 而且 6 必须在 5 之前，因为 6 是最近发送的

twitter.unfollow(1, 2);
// 用户 1 取消关注了用户 2

twitter.getNewsFeed(1);
// return [5]
```

这个场景在我们的现实生活中非常常见。拿朋友圈举例，比如我刚加到女神的微信，然后我去刷新一下我的朋友圈动态，那么女神的动态就会出现在我的动态列表，而且会和其他动态按时间排好序。只不过 Twitter 是单向关注，微信好友相当于双向关注。除非，被屏蔽...

这几个 API 中大部分都很好实现，最核心的功能难点应该是 `getNewsFeed`，因为返回的结果必须在时间上有序，但问题是用户的关注是动态变化的，怎么办？

**这里就涉及到算法了**：如果我们把每个用户各自的推文存储在链表里，每个链表节点存储文章 id 和一个时间戳 time（记录发帖时间以便比较），而且这个链表是按 time 有序的，那么如果某个用户关注了 k 个用户，我们就可以用合并 k 个有序链表的算法合并出有序的推文列表，正确地 `getNewsFeed` 了！

具体的算法等会讲解。不过，就算我们掌握了算法，应该如何编程表示用户 user 和推文动态 tweet 才能把算法流畅地用出来呢？**这就涉及简单的面向对象设计了**，下面我们来由浅入深，一步一步进行设计。

```java
class Tweet {
    private int id;
    private int time;
    private Tweet next;

    // 需要传入推文内容（id）和发文时间
    public Tweet(int id, int time) {
        this.id = id;
        this.time = time;
        this.next = null;
    }
}
```


```java
// static int timestamp = 0
class User {
    private int id;
    public Set<Integer> followed;
    // 用户发表的推文链表头结点
    public Tweet head;

    public User(int userId) {
        followed = new HashSet<>();
        this.id = userId;
        this.head = null;
        // 关注一下自己
        follow(id);
    }

    public void follow(int userId) {
        followed.add(userId);
    }

    public void unfollow(int userId) {
        // 不可以取关自己
        if (userId != this.id)
            followed.remove(userId);
    }

    public void post(int tweetId) {
        Tweet twt = new Tweet(tweetId, timestamp);
        timestamp++;
        // 将新建的推文插入链表头
        // 越靠前的推文 time 值越大
        twt.next = head;
        head = twt;
    }
}
```

```java
class Twitter {
    private static int timestamp = 0;
    private static class Tweet {...}
    private static class User {...}

    // 我们需要一个映射将 userId 和 User 对象对应起来
    private HashMap<Integer, User> userMap = new HashMap<>();

    /** user 发表一条 tweet 动态 */
    public void postTweet(int userId, int tweetId) {
        // 若 userId 不存在，则新建
        if (!userMap.containsKey(userId))
            userMap.put(userId, new User(userId));
        User u = userMap.get(userId);
        u.post(tweetId);
    }
    
    /** follower 关注 followee */
    public void follow(int followerId, int followeeId) {
        // 若 follower 不存在，则新建
		if(!userMap.containsKey(followerId)){
			User u = new User(followerId);
			userMap.put(followerId, u);
		}
        // 若 followee 不存在，则新建
		if(!userMap.containsKey(followeeId)){
			User u = new User(followeeId);
			userMap.put(followeeId, u);
		}
		userMap.get(followerId).follow(followeeId);
    }
    
    /** follower 取关 followee，如果 Id 不存在则什么都不做 */
    public void unfollow(int followerId, int followeeId) {
        if (userMap.containsKey(followerId)) {
            User flwer = userMap.get(followerId);
            flwer.unfollow(followeeId);
        }
    }

    /** 返回该 user 关注的人（包括他自己）最近的动态 id，
    最多 10 条，而且这些动态必须按从新到旧的时间线顺序排列。*/
    public List<Integer> getNewsFeed(int userId) {
        // 需要理解算法，见下文
    }
}
```


```java
public List<Integer> getNewsFeed(int userId) {
    List<Integer> res = new ArrayList<>();
    if (!userMap.containsKey(userId)) return res;
    // 关注列表的用户 Id
    Set<Integer> users = userMap.get(userId).followed;
    // 自动通过 time 属性从大到小排序，容量为 users 的大小
    PriorityQueue<Tweet> pq = 
        new PriorityQueue<>(users.size(), (a, b)->(b.time - a.time));

    // 先将所有链表头节点插入优先级队列
    for (int id : users) {
        Tweet twt = userMap.get(id).head;
        if (twt == null) continue;
        pq.add(twt);
    }

    while (!pq.isEmpty()) {
        // 最多返回 10 条就够了
        if (res.size() == 10) break;
        // 弹出 time 值最大的（最近发表的）
        Tweet twt = pq.poll();
        res.add(twt.id);
        // 将下一篇 Tweet 插入进行排序
        if (twt.next != null) 
            pq.add(twt.next);
    }
    return res;
}
```


#### 7.2 其他语言实现

**C++**

[happy-yuxuan](https://github.com/happy-yuxuan) 提供 C++ 代码：

```c++
static int timestamp = 0;
class Tweet {
private:
    int id;
    int time;
public:
    Tweet *next;
    // id为推文内容，time为发文时间
    Tweet(int id, int time) {
        this->id = id;
        this->time = time;
        next = nullptr;
    }
    int getId() const {
        return this->id;
    }
    int getTime() const {
        return this->time;
    }
};
class User {
private:
    int id;
public:
    Tweet *head;  // 发布的Twitter，用链表表示
    unordered_set<int> followed;  // 用户关注了那些人
    User(int userId) {
        this->id = userId;
        head = nullptr;
        // 要先把自己关注了
        followed.insert(id);
    }
    void follow(int userId) {
        followed.insert(userId);
    }
    void unfollow(int userId) {
        // 不可以取关自己
        if (userId != this->id)
            followed.erase(userId);
    }
    void post(int contentId) {
        Tweet *twt = new Tweet(contentId, timestamp);
        timestamp++;
        // 将新建的推文插入链表头
        // 越靠前的推文 timestamp 值越大
        twt->next = head;
        head = twt;
    }
};
class Twitter {
private:
    // 映射将 userId 和 User 对象对应起来
    unordered_map<int, User*> userMap;
    // 判断该用户存不存在系统中,即userMap中存不存在id
    inline bool contain(int id) {
        return userMap.find(id) != userMap.end();
    }
public:
    Twitter() {
        userMap.clear();
    }
    /* user 发表一条 tweet 动态 */
    void postTweet(int userId, int tweetId) {
        if (!contain(userId))
            userMap[userId] = new User(userId);
        userMap[userId]->post(tweetId);
    }
    /* 返回该 user 关注的人（包括他自己）最近的动态 id，
    最多 10 条，而且这些动态必须按从新到旧的时间线顺序排列。*/
    vector<int> getNewsFeed(int userId) {
        vector<int> ret;
        if (!contain(userId)) return ret;
        // 构造一个自动通过Tweet发布的time属性从大到小排序的二叉堆
        typedef function<bool(const Tweet*, const Tweet*)> Compare;
        Compare cmp = [](const Tweet *a, const Tweet *b) {
            return a->getTime() < b->getTime();
        };
        priority_queue<Tweet*, vector<Tweet*>, Compare> q(cmp);
        // 关注列表的用户Id
        unordered_set<int> &users = userMap[userId]->followed;
        // 先将所有链表头节点插入优先级队列
        for (int id : users) {
            if (!contain(id)) continue;
            Tweet *twt = userMap[id]->head;
            if (twt == nullptr) continue;
            q.push(twt);
        }
        while (!q.empty()) {
            Tweet *t = q.top(); q.pop();
            ret.push_back(t->getId());
            if (ret.size() == 10) return ret;  // 最多返回 10 条就够了
            if (t->next)
                q.push(t->next);
        }
        return ret;
    }
    /* follower 关注 followee */
    void follow(int followerId, int followeeId) {
        // 若 follower 不存在，则新建
        if (!contain(followerId))
            userMap[followerId] = new User(followerId);
        // 若 followee 不存在，则新建
        if (!contain(followeeId))
            userMap[followeeId] = new User(followeeId);
        userMap[followerId]->follow(followeeId);
    }
    /* follower 取关 followee，如果 Id 不存在则什么都不做 */
    void unfollow(int followerId, int followeeId) {
        if (contain(followerId))
            userMap[followerId]->unfollow(followeeId);
    }
};
```



**python**

```python
import heapq

class Tweet:
    def __init__(self, tid: int, time: int) -> None:
        self.tid = tid
        self.time = time
        self.next = None

class User:
    def __init__(self, uid: int):
        self.uid = uid
        self.following = set()
        self.tweetlst = None
        self.follow(uid)

    def post(self, tid: int, time: int) -> None:
        tweet = Tweet(tid, time)
        tweet.next = self.tweetlst
        self.tweetlst = tweet

    def follow(self, uid: int) -> None:
        if uid not in self.following:
            self.following.add(uid)

    def unfollow(self, uid: int) -> None:
        # one cannot unfollow itself
        if uid != self.uid and uid in self.following:
            self.following.remove(uid)

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.id2user = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.id2user: self.id2user[userId] = User(userId)
        user = self.id2user[userId]
        user.post(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap, user = [], self.id2user.get(userId)

        if user:
            for uid in user.following:
                tweets = self.id2user[uid].tweetlst
                while tweets:
                    heap.append(tweets)
                    tweets = tweets.next
            return [twt.tid for twt in heapq.nlargest(10, heap, key= lambda twt: twt.time)]
        else: return []

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.id2user:
            self.id2user[followerId] = User(followerId)
        if followeeId not in self.id2user:
            self.id2user[followeeId] = User(followeeId)
        self.id2user[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.id2user:
            self.id2user[followerId].unfollow(followeeId)
```


### 8 递归反转链表的一部分

#### 8.1 递归反转整个链表

```java
ListNode reverse(ListNode head) {
    if (head.next == null) return head;
    ListNode last = reverse(head.next);
    head.next.next = head;
    head.next = null;
    return last;
}
```

#### 8.2 反转链表前 N 个节点

```java
ListNode successor = null; // 后驱节点

// 反转以 head 为起点的 n 个节点，返回新的头结点
ListNode reverseN(ListNode head, int n) {
    if (n == 1) { 
        // 记录第 n + 1 个节点
        successor = head.next;
        return head;
    }
    // 以 head.next 为起点，需要反转前 n - 1 个节点
    ListNode last = reverseN(head.next, n - 1);

    head.next.next = head;
    // 让反转之后的 head 节点和后面的节点连起来
    head.next = successor;
    return last;
}    
```

#### 8.3 反转链表的一部分

```java
ListNode reverseBetween(ListNode head, int m, int n) {
    // base case
    if (m == 1) {
        return reverseN(head, n);
    }
    // 前进到反转的起点触发 base case
    head.next = reverseBetween(head.next, m - 1, n - 1);
    return head;
}
```

#### 8.4 其他语言实现


**c++** 

[shilei](https://github.com/ShileiGuo) 提供C++解法代码:

思想:

   1.head表示需要反转的头节点，pre表示需要反转头节点的前驱节点

   2.对于从m到n的节点反转，需要反转n-m次，将head的next节点移动到需要反转链表部分的首部，需要反转链表部分剩余节点依旧保持相对顺序即可

   3.示例 当m=2, n=5时 

   第一次反转：1(pre) 2(head) 3(next) 4 5 反转为 1 3 2 4 5

   第二次反转：1(pre) 3 2(head) 4(next) 5 反转为 1 4 3 2 5

   第三次发转：1(pre) 4 3 2(head) 5(next) 反转为 1 5 4 3 2

```CPP
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        //初始化哨兵节点
        ListNode* dummy=new ListNode(-1);
        //初始化待反转区间的前一个节点
        ListNode* pre=dummy;
        //哨兵节点下一个节点指向head头节点
        dummy->next=head;
        
        //获取待反转节点的前一个节点
        for(int i=0;i<m-1;i++)
            pre=pre->next;        
        //获取待反转节点的第一个节点
        head=pre->next;  
        //迭代反转n-m次，将head的next节点移动到需要反转链表部分的首部
        for(int i=m;i<n;i++){
            ListNode* t=head->next;       
            head->next=t->next;          
            t->next=pre->next;         
            pre->next=t;                
        }
        //返回哨兵节点
        return dummy->next;
    }
};
```

**python**

[DiamondI](https://github.com/DiamondI) 提供python3版本代码：

思路：递归。时间复杂度为O(n)，由于递归调用需要借助栈的空间，因此空间复杂度亦为O(n)。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def __init__(self):
    self.__successor = None

    def __reverseN(self, head: ListNode, n: int) -> ListNode:
      if n == 1:  
        # 记录第 n + 1 个节点
        self.__successor = head.next;
        return head;
      # 以 head.next 为起点，需要反转前 n - 1 个节点
      last = self.__reverseN(head.next, n - 1);

      head.next.next = head;
      # 让反转之后的 head 节点和后面的节点连起来
      head.next = self.__successor;
      return last;

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
      # base case
      if m == 1:
        return self.__reverseN(head, n);
      # 前进到反转的起点触发 base case
      head.next = self.reverseBetween(head.next, m - 1, n - 1);
      return head;
```



