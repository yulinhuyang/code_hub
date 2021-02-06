## 题目描述

```
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

 

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

 

示例：

LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4

```

## 前置知识

- 链表
- HashMap


 1. put(1, 1), 
    - 首先查找 nodeMap 中有没有 key=1 对应的 value，
        没有就新建 node(key, value, freq) -> node1(1, 1, 1), 插入 nodeMap，{[1, node1]}
    - 查找 freqMap 中有没有 freq=1 对应的 value，
        没有就新建 doublylinkedlist(head, tail), 把 node1 插入 doublylinkedlist head->next = node1.
    如下图，
 ```
![460.lfu-cache-1](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu4z6wr1j314x0u0q61.jpg)
 ```
 2. put(2, 2), 
    - 首先查找 nodeMap 中有没有 key=2 对应的 value，
        没有就新建 node(key, value, freq) -> node2(2, 2, 1), 插入 nodeMap，{[1, node1], [2, node2]}
    - 查找 freqMap 中有没有 freq=1 对应的 value，
        没有就新建 doublylinkedlist(head, tail), 把 node2 插入 doublylinkedlist head->next = node2.
    如下图，
 ```
![460.lfu-cache-2](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu4zqh7wj314k0u0adh.jpg)
 ```
 3. get(1), 
    - 首先查找 nodeMap 中有没有 key=1 对应的 value，nodeMap:{[1, node1], [2, node2]},
        找到 node1，把 node1 freq+1 -> node1(1,1,2)
    - 更新 freqMap，删除 freq=1，node1
    - 更新 freqMap，插入 freq=2，node1
    如下图，
 ```
![460.lfu-cache-3](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu53jotrj313p0u0tdi.jpg)
 ```
 4. put(3, 3), 
    - 判断 cache 的 capacity，已满，需要淘汰使用次数最少的元素，找到最小的 freq=1，删除双链表 tail node.prev 
        如果 tailnode.prev != null, 删除。然后从 nodeMap 中删除对应的 key。
    - 首先查找 nodeMap 中有没有 key=3 对应的 value，
        没有就新建 node(key, value, freq) -> node3(3, 3, 1), 插入 nodeMap，{[1, node1], [3, node3]}
    - 查找 freqMap 中有没有 freq=1 对应的 value，
        没有就新建 doublylinkedlist(head, tail), 把 node3 插入 doublylinkedlist head->next = node3.
    如下图，
 ```
![460.lfu-cache-4](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu54ffzrj313l0qwdkf.jpg)
 ```
 5. get(2) 
    - 查找 nodeMap，如果没有对应的 key 的 value，返回 -1。
  
 6. get(3)
    - 首先查找 nodeMap 中有没有 key=3 对应的 value，nodeMap:{[1, node1], [3, node3]},
        找到 node3，把 node3 freq+1 -> node3(3,3,2)
    - 更新 freqMap，删除 freq=1，node3
    - 更新 freqMap，插入 freq=2，node3
    如下图，
 ```
![460.lfu-cache-5](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu54r66gj31380r1af4.jpg)
 ```
 7. put(4, 4), 
    - 判断 cache 的 capacity，已满，需要淘汰使用次数最少的元素，找到最小的 freq=1，删除双链表 tail node.prev 
        如果 tailnode.prev != null, 删除。然后从 nodeMap 中删除对应的 key。
    - 首先查找 nodeMap 中有没有 key=4 对应的 value，
        没有就新建 node(key, value, freq) -> node4(4, 4, 1), 插入 nodeMap，{[4, node4], [3, node3]}
    - 查找 freqMap 中有没有 freq=1 对应的 value，
        没有就新建 doublylinkedlist(head, tail), 把 node4 插入 doublylinkedlist head->next = node4.
    如下图，
 ```
![460.lfu-cache-6](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu558d63j317s0trgrk.jpg)
 ```
 8. get(1) 
    - 查找 nodeMap，如果没有对应的 key 的 value，返回 -1。
  
 9. get(3)
    - 首先查找 nodeMap 中有没有 key=3 对应的 value，nodeMap:{[4, node4], [3, node3]},
        找到 node3，把 node3 freq+1 -> node3(3,3,3)
    - 更新 freqMap，删除 freq=2，node3
    - 更新 freqMap，插入 freq=3，node3
    如下图，
 ```
![460.lfu-cache-7](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu56bzvhj313u0u0q7w.jpg)
 ```
 10. get(4)
    - 首先查找 nodeMap 中有没有 key=4 对应的 value，nodeMap:{[4, node4], [3, node3]},
        找到 node4，把 node4 freq+1 -> node4(4,4,2)
    - 更新 freqMap，删除 freq=1，node4
    - 更新 freqMap，插入 freq=2，node4
    如下图，

    


# Time:  O(1), per operation
# Space: O(k), k is the capacity of cache

import collections


# using OrderedDict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__capa = capacity
        self.__size = 0
        self.__min_freq = float("inf")
        self.__freq_to_nodes = collections.defaultdict(collections.OrderedDict)
        self.__key_to_freq = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.__key_to_freq:
            return -1
        value = self.__freq_to_nodes[self.__key_to_freq[key]][key]
        self.__update(key, value)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.__capa <= 0:
            return

        if key not in self.__key_to_freq and self.__size == self.__capa:
            del self.__key_to_freq[self.__freq_to_nodes[self.__min_freq].popitem(last=False)[0]]
            if not self.__freq_to_nodes[self.__min_freq]:
                del self.__freq_to_nodes[self.__min_freq]
            self.__size -= 1
        self.__update(key, value)
        
    def __update(self, key, value):
        freq = 0
        if key in self.__key_to_freq:
            freq = self.__key_to_freq[key]
            del self.__freq_to_nodes[freq][key]
            if not self.__freq_to_nodes[freq]:
                del self.__freq_to_nodes[freq]
                if self.__min_freq == freq:
                    self.__min_freq += 1
            self.__size -= 1

        freq += 1
        self.__min_freq = min(self.__min_freq, freq)
        self.__key_to_freq[key] = freq
        self.__freq_to_nodes[freq][key] = value
        self.__size += 1


# Time:  O(1), per operation
# Space: O(k), k is the capacity of cache
import collections


class ListNode(object):
    def __init__(self, key, value, freq):
        self.key = key
        self.val = value
        self.freq = freq
        self.next = None
        self.prev = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        node.next, node.prev = None, None  # avoid dirty node
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next, node.prev = None, None  # make node clean


class LFUCache2(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__capa = capacity
        self.__size = 0
        self.__min_freq = float("inf")
        self.__freq_to_nodes = collections.defaultdict(LinkedList)
        self.__key_to_node = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.__key_to_node:
            return -1
        value = self.__key_to_node[key].val
        self.__update(key, value)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.__capa <= 0:
            return

        if key not in self.__key_to_node and self.__size == self.__capa:
            del self.__key_to_node[self.__freq_to_nodes[self.__min_freq].head.key]
            self.__freq_to_nodes[self.__min_freq].delete(self.__freq_to_nodes[self.__min_freq].head)
            if not self.__freq_to_nodes[self.__min_freq].head:
                del self.__freq_to_nodes[self.__min_freq]
            self.__size -= 1
        self.__update(key, value)
        
    def __update(self, key, value):
        freq = 0
        if key in self.__key_to_node:
            old_node = self.__key_to_node[key]
            freq = old_node.freq
            self.__freq_to_nodes[freq].delete(old_node)
            if not self.__freq_to_nodes[freq].head:
                del self.__freq_to_nodes[freq]
                if self.__min_freq == freq:
                    self.__min_freq += 1
            self.__size -= 1

        freq += 1
        self.__min_freq = min(self.__min_freq, freq)
        self.__key_to_node[key] = ListNode(key, value, freq)
        self.__freq_to_nodes[freq].append(self.__key_to_node[key])
        self.__size += 1
