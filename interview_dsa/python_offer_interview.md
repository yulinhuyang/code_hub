


### 13  机器人的运动范围

def digit_num(num):
    sum = 0
    while num:
        sum = sum + num%10
        num = num//10
    return sum
 
class Solution:
        def movingCount(self, m: int, n: int, k: int) -> int:
            
            vis = set([(0,0)])
            
            for i in range(m):
                for j in range(n):
                    if ((i-1,j) in vis or (i,j-1) in vis) and digit_num(i) + digit_num(j) <= k:
                        vis.add((i,j))
            
            return len(vis)


**Notes:**

**set**

用set来表示一个无序不重复元素的序列。set的只要作用就是用来给数据去重。 

可以使用大括号 { } 或者 set() 函数创建集合

eg: 

添加一对数：

vis = set([(0, 0)])

vis.add((i, j))


/ 除以，带小数

//整除

**dict**

创建字典：

d = {key1 : value1, key2 : value2 }

eg；

dict = {'a': 1, 'b': 2, 'b': '3'}

**tuple**

tup1 = ('physics', 'chemistry', 1997, 2000)


