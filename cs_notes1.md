# 第 1 章 数据库
## 第 1.1 节 数据库系统原理
### 一、事务
#### 概念
#### ACID
##### 1. 原子性（Atomicity）
##### 2. 一致性（Consistency）
##### 3. 隔离性（Isolation）
##### 4. 持久性（Durability）
#### AUTOCOMMIT
### 二、并发一致性问题
#### 丢失修改
#### 读脏数据
#### 不可重复读
#### 幻影读
### 三、封锁
#### 封锁粒度
#### 封锁类型
##### 1. 读写锁
##### 2. 意向锁
#### 封锁协议
##### 1. 三级封锁协议
##### 2. 两段锁协议
#### MySQL 隐式与显示锁定
### 四、隔离级别
#### 未提交读（READ UNCOMMITTED）
#### 提交读（READ COMMITTED）
#### 可重复读（REPEATABLE READ）
#### 可串行化（SERIALIZABLE）
### 五、多版本并发控制
#### 版本号
#### 隐藏的列
#### Undo 日志
#### 实现过程
##### 1. SELECT
##### 2. INSERT
##### 3. DELETE
##### 4. UPDATE
#### 快照读与当前读
##### 1. 快照读
##### 2. 当前读
### 六、Next-Key Locks
#### Record Locks
#### Gap Locks
#### Next-Key Locks
### 七、关系数据库设计理论
#### 函数依赖
#### 异常
#### 范式
##### 1. 第一范式 (1NF)
##### 2. 第二范式 (2NF)
##### 3. 第三范式 (3NF)
### 八、ER 图
#### 实体的三种联系
#### 表示出现多次的关系
#### 联系的多向性
#### 表示子类
### 参考资料
## 第 1.2 节 SQL
### 一、基础
### 二、创建表
### 三、修改表
### 四、插入
### 五、更新
### 六、删除
### 七、查询
#### DISTINCT
#### LIMIT
### 八、排序
### 九、过滤
### 十、通配符
### 十一、计算字段
### 十二、函数
#### 汇总
#### 文本处理
#### 日期和时间处理
#### 数值处理
### 十三、分组
### 十四、子查询
### 十五、连接
#### 内连接
#### 自连接
#### 自然连接
#### 外连接
### 十六、组合查询
### 十七、视图
### 十八、存储过程
### 十九、游标
### 二十、触发器
### 二十一、事务管理
### 二十二、字符集
### 二十三、权限管理
### 参考资料
## 第 1.3 节 Leetcode-Database 题解
### 595. Big Countries
#### Description
#### SQL Schema
#### Solution
### 627. Swap Salary
#### Description
#### SQL Schema
#### Solution
### 620. Not Boring Movies
#### Description
#### SQL Schema
#### Solution
### 596. Classes More Than 5 Students
#### Description
#### SQL Schema
#### Solution
### 182. Duplicate Emails
#### Description
#### SQL Schema
#### Solution
### 196. Delete Duplicate Emails
#### Description
#### SQL Schema
#### Solution
### 175. Combine Two Tables
#### Description
#### SQL Schema
#### Solution
### 181. Employees Earning More Than Their Managers
#### Description
#### SQL Schema
#### Solution
### 183. Customers Who Never Order
#### Description
#### SQL Schema
#### Solution
### 184. Department Highest Salary
#### Description
#### SQL Schema
#### Solution
### 176. Second Highest Salary
#### Description
#### SQL Schema
#### Solution
### 177. Nth Highest Salary
#### Description
#### SQL Schema
#### Solution
### 178. Rank Scores
#### Description
#### SQL Schema
#### Solution
### 180. Consecutive Numbers
#### Description
#### SQL Schema
#### Solution
### 626. Exchange Seats
#### Description
#### SQL Schema
#### Solution
## 第 1.4 节 MySQL
### 一、索引
#### B+ Tree 原理
##### 1. 数据结构
##### 2. 操作
##### 3. 与红黑树的比较
#### MySQL 索引
##### 1. B+Tree 索引
##### 2. 哈希索引
##### 3. 全文索引
##### 4. 空间数据索引
#### 索引优化
##### 1. 独立的列
##### 2. 多列索引
##### 3. 索引列的顺序
##### 4. 前缀索引
##### 5. 覆盖索引
#### 索引的优点
#### 索引的使用条件
### 二、查询性能优化
#### 使用 Explain 进行分析
#### 优化数据访问
##### 1. 减少请求的数据量
##### 2. 减少服务器端扫描的行数
#### 重构查询方式
##### 1. 切分大查询
##### 2. 分解大连接查询
### 三、存储引擎
#### InnoDB
#### MyISAM
#### 比较
### 四、数据类型
#### 整型
#### 浮点数
#### 字符串
#### 时间和日期
##### 1. DATETIME
##### 2. TIMESTAMP
### 五、切分
#### 水平切分
#### 垂直切分
#### Sharding 策略
#### Sharding 存在的问题
##### 1. 事务问题
##### 2. 连接
##### 3. ID 唯一性
### 六、复制
#### 主从复制
#### 读写分离
### 参考资料
## 第 1.5 节 Redis
### 一、概述
### 二、数据类型
#### STRING
#### LIST
#### SET
#### HASH
#### ZSET
### 三、数据结构
#### 字典
#### 跳跃表
### 四、使用场景
#### 计数器
#### 缓存
#### 查找表
#### 消息队列
#### 会话缓存
#### 分布式锁实现
#### 其它
### 五、Redis 与 Memcached
#### 数据类型
#### 数据持久化
#### 分布式
#### 内存管理机制
### 六、键的过期时间
### 七、数据淘汰策略
### 八、持久化
#### RDB 持久化
#### AOF 持久化
### 九、事务
### 十、事件
#### 文件事件
#### 时间事件
#### 事件的调度与执行
### 十一、复制
#### 连接过程
#### 主从链
### 十二、Sentinel
### 十三、分片
### 十四、一个简单的论坛系统分析
#### 文章信息
#### 点赞功能
#### 对文章进行排序
### 参考资料

# 第 2 章 Java
## 第 2.1 节 Java 基础
### 一、数据类型
#### 基本类型
#### 包装类型
#### 缓存池
### 二、String
#### 概览
#### 不可变的好处
#### String, StringBuffer and StringBuilder
#### String Pool
#### new String("abc")
### 三、运算
#### 参数传递
#### float 与 double
#### 隐式类型转换
#### switch
### 四、继承
#### 访问权限
#### 抽象类与接口
#### super
#### 重写与重载
### 五、Object 通用方法
#### 概览
#### equals()
#### hashCode()
#### toString()
#### clone()
### 六、关键字
#### final
#### static
### 七、反射
### 八、异常
### 九、泛型
### 十、注解
### 十一、特性
#### Java 各版本的新特性
#### Java 与 C++ 的区别
#### JRE or JDK
### 参考资料
## 第 2.2 节 Java 容器
### 一、概览
#### Collection
##### 1. Set
##### 2. List
##### 3. Queue
#### Map
### 二、容器中的设计模式
#### 迭代器模式
#### 适配器模式
### 三、源码分析
#### ArrayList
##### 1. 概览
##### 2. 扩容
##### 3. 删除元素
##### 4. Fail-Fast
##### 5. 序列化
#### Vector
##### 1. 同步
##### 2. 与 ArrayList 的比较
##### 3. 替代方案
#### CopyOnWriteArrayList
##### 读写分离
##### 适用场景
#### LinkedList
##### 1. 概览
##### 2. 与 ArrayList 的比较
#### HashMap
##### 1. 存储结构
##### 2. 拉链法的工作原理
##### 3. put 操作
##### 4. 确定桶下标
##### 5. 扩容-基本原理
##### 6. 扩容-重新计算桶下标
##### 7. 计算数组容量
##### 8. 链表转红黑树
##### 9. 与 HashTable 的比较
#### ConcurrentHashMap
##### 1. 存储结构
##### 2. size 操作
##### 3. JDK 1.8 的改动
#### LinkedHashMap
##### 存储结构
##### afterNodeAccess()
##### afterNodeInsertion()
##### LRU 缓存
#### WeakHashMap
##### 存储结构
##### ConcurrentCache
### 参考资料
## 第 2.3 节 Java 并发
### 一、线程状态转换
#### 新建（New）
#### 可运行（Runnable）
#### 阻塞（Blocked）
#### 无限期等待（Waiting）
#### 限期等待（Timed Waiting）
#### 死亡（Terminated）
### 二、使用线程
#### 实现 Runnable 接口
#### 实现 Callable 接口
#### 继承 Thread 类
#### 实现接口 VS 继承 Thread
### 三、基础线程机制
#### Executor
#### Daemon
#### sleep()
#### yield()
### 四、中断
#### InterruptedException
#### interrupted()
#### Executor 的中断操作
### 五、互斥同步
#### synchronized
#### ReentrantLock
#### 比较
#### 使用选择
### 六、线程之间的协作
#### join()
#### wait() notify() notifyAll()
#### await() signal() signalAll()
### 七、J.U.C - AQS
#### CountDownLatch
#### CyclicBarrier
#### Semaphore
### 八、J.U.C - 其它组件
#### FutureTask
#### BlockingQueue
#### ForkJoin
### 九、线程不安全示例
### 十、Java 内存模型
#### 主内存与工作内存
#### 内存间交互操作
#### 内存模型三大特性
##### 1. 原子性
##### 2. 可见性
##### 3. 有序性
#### 先行发生原则
##### 1. 单一线程原则
##### 2. 管程锁定规则
##### 3. volatile 变量规则
##### 4. 线程启动规则
##### 5. 线程加入规则
##### 6. 线程中断规则
##### 7. 对象终结规则
##### 8. 传递性
### 十一、线程安全
#### 不可变
#### 互斥同步
#### 非阻塞同步
##### 1. CAS
##### 2. AtomicInteger
##### 3. ABA
#### 无同步方案
##### 1. 栈封闭
##### 2. 线程本地存储（Thread Local Storage）
##### 3. 可重入代码（Reentrant Code）
### 十二、锁优化
#### 自旋锁
#### 锁消除
#### 锁粗化
#### 轻量级锁
#### 偏向锁
### 十三、多线程开发良好的实践
### 参考资料
## 第 2.4 节 Java 虚拟机
### 一、运行时数据区域
#### 程序计数器
#### Java 虚拟机栈
#### 本地方法栈
#### 堆
#### 方法区
#### 运行时常量池
#### 直接内存
### 二、垃圾收集
#### 判断一个对象是否可被回收
##### 1. 引用计数算法
##### 2. 可达性分析算法
##### 3. 方法区的回收
##### 4. finalize()
#### 引用类型
##### 1. 强引用
##### 2. 软引用
##### 3. 弱引用
##### 4. 虚引用
#### 垃圾收集算法
##### 1. 标记 - 清除
##### 2. 标记 - 整理
##### 3. 复制
##### 4. 分代收集
#### 垃圾收集器
##### 1. Serial 收集器
##### 2. ParNew 收集器
##### 3. Parallel Scavenge 收集器
##### 4. Serial Old 收集器
##### 5. Parallel Old 收集器
##### 6. CMS 收集器
##### 7. G1 收集器
### 三、内存分配与回收策略
#### Minor GC 和 Full GC
#### 内存分配策略
##### 1. 对象优先在 Eden 分配
##### 2. 大对象直接进入老年代
##### 3. 长期存活的对象进入老年代
##### 4. 动态对象年龄判定
##### 5. 空间分配担保
#### Full GC 的触发条件
##### 1. 调用 System.gc()
##### 2. 老年代空间不足
##### 3. 空间分配担保失败
##### 4. JDK 1.7 及以前的永久代空间不足
##### 5. Concurrent Mode Failure
### 四、类加载机制
#### 类的生命周期
#### 类加载过程
##### 1. 加载
##### 2. 验证
##### 3. 准备
##### 4. 解析
##### 5. 初始化
#### 类初始化时机
##### 1. 主动引用
##### 2. 被动引用
#### 类与类加载器
#### 类加载器分类
#### 双亲委派模型
##### 1. 工作过程
##### 2. 好处
##### 3. 实现
#### 自定义类加载器实现
### 参考资料
## 第 2.5 节 Java IO
### 一、概览
### 二、磁盘操作
### 三、字节操作
#### 实现文件复制
#### 装饰者模式
### 四、字符操作
#### 编码与解码
#### String 的编码方式
#### Reader 与 Writer
#### 实现逐行输出文本文件的内容
### 五、对象操作
#### 序列化
#### Serializable
#### transient
### 六、网络操作
#### InetAddress
#### URL
#### Sockets
#### Datagram
### 七、NIO
#### 流与块
#### 通道与缓冲区
##### 1. 通道
##### 2. 缓冲区
#### 缓冲区状态变量
#### 文件 NIO 实例
#### 选择器
##### 1. 创建选择器
##### 2. 将通道注册到选择器上
##### 3. 监听事件
##### 4. 获取到达的事件
##### 5. 事件循环
#### 套接字 NIO 实例
#### 内存映射文件
#### 对比
### 八、参考资料
# 第 3 章 系统设计
## 第 3.1 节 系统设计基础
### 一、性能
#### 性能指标
##### 1. 响应时间
##### 2. 吞吐量
##### 3. 并发用户数
#### 性能优化
##### 1. 集群
##### 2. 缓存
##### 3. 异步
### 二、伸缩性
#### 伸缩性与性能
#### 实现伸缩性
### 三、扩展性
### 四、可用性
#### 冗余
#### 监控
#### 服务降级
### 五、安全性
### 参考资料
## 第 3.2 节 分布式
### 一、分布式锁
#### 数据库的唯一索引
#### Redis 的 SETNX 指令
#### Redis 的 RedLock 算法
#### Zookeeper 的有序节点
##### 1. Zookeeper 抽象模型
##### 2. 节点类型
##### 3. 监听器
##### 4. 分布式锁实现
##### 5. 会话超时
##### 6. 羊群效应
### 二、分布式事务
#### 2PC
##### 1. 运行过程
###### 1.1 准备阶段
###### 1.2 提交阶段
##### 2. 存在的问题
###### 2.1 同步阻塞
###### 2.2 单点问题
###### 2.3 数据不一致
###### 2.4 太过保守
#### 本地消息表
### 三、CAP
#### 一致性
#### 可用性
#### 分区容忍性
#### 权衡
### 四、BASE
#### 基本可用
#### 软状态
#### 最终一致性
### 五、Paxos
#### 执行过程
##### 1. Prepare 阶段
##### 2. Accept 阶段
##### 3. Learn 阶段
#### 约束条件
##### 1\. 正确性
##### 2\. 可终止性
### 六、Raft
#### 单个 Candidate 的竞选
#### 多个 Candidate 竞选
#### 数据同步
### 参考
## 第 3.3 节 集群
### 一、负载均衡
#### 负载均衡算法
##### 1. 轮询（Round Robin）
##### 2. 加权轮询（Weighted Round Robbin）
##### 3. 最少连接（least Connections）
##### 4. 加权最少连接（Weighted Least Connection）
##### 5. 随机算法（Random）
##### 6. 源地址哈希法 (IP Hash)
#### 转发实现
##### 1. HTTP 重定向
##### 2. DNS 域名解析
##### 3. 反向代理服务器
##### 4. 网络层
##### 5. 链路层
### 二、集群下的 Session 管理
#### Sticky Session
#### Session Replication
#### Session Server
## 第 3.4 节 攻击技术
### 一、跨站脚本攻击
#### 概念
#### 攻击原理
#### 危害
#### 防范手段
##### 1. 设置 Cookie 为 HttpOnly
##### 2. 过滤特殊字符
### 二、跨站请求伪造
#### 概念
#### 攻击原理
#### 防范手段
##### 1. 检查 Referer 首部字段
##### 2. 添加校验 Token
##### 3. 输入验证码
### 三、SQL 注入攻击
#### 概念
#### 攻击原理
#### 防范手段
##### 1. 使用参数化查询
##### 2. 单引号转换
### 四、拒绝服务攻击
### 参考资料
## 第 3.5 节 缓存
### 一、缓存特征
#### 命中率
#### 最大空间
#### 淘汰策略
### 二、LRU
### 三、缓存位置
#### 浏览器
#### ISP
#### 反向代理
#### 本地缓存
#### 分布式缓存
#### 数据库缓存
#### Java 内部的缓存
#### CPU 多级缓存
### 四、CDN
### 五、缓存问题
#### 缓存穿透
#### 缓存雪崩
#### 缓存一致性
#### 缓存 “无底洞” 现象
### 六、数据分布
#### 哈希分布
#### 顺序分布
### 七、一致性哈希
#### 基本原理
#### 虚拟节点
### 参考资料
## 第 3.6 节 消息队列
### 一、消息模型
#### 点对点
#### 发布/订阅
### 二、使用场景
#### 异步处理
#### 流量削锋
#### 应用解耦
### 三、可靠性
#### 发送端的可靠性
#### 接收端的可靠性
### 参考资料
# 第 4 章 面向对象
## 第 4.1 节 设计模式
### 一、概述
### 二、创建型
#### 1. 单例（Singleton）
##### Intent
##### Class Diagram
##### Implementation
###### Ⅰ 懒汉式-线程不安全
###### Ⅱ 饿汉式-线程安全
###### Ⅲ 懒汉式-线程安全
###### Ⅳ 双重校验锁-线程安全
###### Ⅴ 静态内部类实现
###### Ⅵ 枚举实现
##### Examples
##### JDK
#### 2. 简单工厂（Simple Factory）
##### Intent
##### Class Diagram
##### Implementation
#### 3. 工厂方法（Factory Method）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 4. 抽象工厂（Abstract Factory）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 5. 生成器（Builder）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 6. 原型模式（Prototype）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
### 三、行为型
#### 1. 责任链（Chain Of Responsibility）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 2. 命令（Command）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 3. 解释器（Interpreter）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 4. 迭代器（Iterator）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 5. 中介者（Mediator）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 6. 备忘录（Memento）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 7. 观察者（Observer）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 8. 状态（State）
##### Intent
##### Class Diagram
##### Implementation
#### 9. 策略（Strategy）
##### Intent
##### Class Diagram
##### 与状态模式的比较
##### Implementation
##### JDK
#### 10. 模板方法（Template Method）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 11. 访问者（Visitor）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 12. 空对象（Null）
##### Intent
##### Class Diagram
##### Implementation
### 四、结构型
#### 1. 适配器（Adapter）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 2. 桥接（Bridge）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 3. 组合（Composite）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 4. 装饰（Decorator）
##### Intent
##### Class Diagram
##### Implementation
##### 设计原则
##### JDK
#### 5. 外观（Facade）
##### Intent
##### Class Diagram
##### Implementation
##### 设计原则
#### 6. 享元（Flyweight）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 7. 代理（Proxy）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
### 参考资料
## 第 4.2 节 面向对象思想
### 一、三大特性
#### 封装
#### 继承
#### 多态
### 二、类图
#### 泛化关系 (Generalization)
#### 实现关系 (Realization)
#### 聚合关系 (Aggregation)
#### 组合关系 (Composition)
#### 关联关系 (Association)
#### 依赖关系 (Dependency)
### 三、设计原则
#### S.O.L.I.D
##### 1. 单一责任原则
##### 2. 开放封闭原则
##### 3. 里氏替换原则
##### 4. 接口分离原则
##### 5. 依赖倒置原则
#### 其他常见原则
##### 1. 迪米特法则
##### 2. 合成复用原则
##### 3. 共同封闭原则
##### 4. 稳定抽象原则
##### 5. 稳定依赖原则
### 参考资料
# 第 5 章 网络
## 第 5.1 节 计算机网络
### 概述
#### 网络的网络
#### ISP
#### 主机之间的通信方式
#### 电路交换与分组交换
##### 1. 电路交换
##### 2. 分组交换
#### 时延
##### 1. 排队时延
##### 2. 处理时延
##### 3. 传输时延
##### 4. 传播时延
#### 计算机网络体系结构
##### 1. 五层协议
##### 2. OSI
##### 3. TCP/IP
##### 4. 数据在各层之间的传递过程
### 物理层
#### 通信方式
#### 带通调制
### 链路层
#### 基本问题
##### 1. 封装成帧
##### 2. 透明传输
##### 3. 差错检测
#### 信道分类
##### 1. 广播信道
##### 2. 点对点信道
#### 信道复用技术
##### 1. 频分复用
##### 2. 时分复用
##### 3. 统计时分复用
##### 4. 波分复用
##### 5. 码分复用
#### CSMA/CD 协议
#### PPP 协议
#### MAC 地址
#### 局域网
#### 以太网
#### 交换机
#### 虚拟局域网
### 网络层
#### 概述
#### IP 数据报格式
#### IP 地址编址方式
##### 1. 分类
##### 2. 子网划分
##### 3. 无分类
#### 地址解析协议 ARP
#### 网际控制报文协议 ICMP
##### 1. Ping
##### 2. Traceroute
#### 虚拟专用网 VPN
#### 网络地址转换 NAT
#### 路由器的结构
#### 路由器分组转发流程
#### 路由选择协议
##### 1. 内部网关协议 RIP
##### 2. 内部网关协议 OSPF
##### 3. 外部网关协议 BGP
### 传输层
#### UDP 和 TCP 的特点
#### UDP 首部格式
#### TCP 首部格式
#### TCP 的三次握手
#### TCP 的四次挥手
#### TCP 可靠传输
#### TCP 滑动窗口
#### TCP 流量控制
#### TCP 拥塞控制
##### 1. 慢开始与拥塞避免
##### 2. 快重传与快恢复
### 应用层
#### 域名系统
#### 文件传送协议
#### 动态主机配置协议
#### 远程登录协议
#### 电子邮件协议
##### 1. SMTP
##### 2. POP3
##### 3. IMAP
#### 常用端口
#### Web 页面请求过程
##### 1. DHCP 配置主机信息
##### 2. ARP 解析 MAC 地址
##### 3. DNS 解析域名
##### 4. HTTP 请求页面
### 参考链接
## 第 5.2 节 HTTP
#### 一 、基础概念
##### URI
##### 请求和响应报文
###### 1. 请求报文
###### 2. 响应报文
#### 二、HTTP 方法
##### GET
##### HEAD
##### POST
##### PUT
##### PATCH
##### DELETE
##### OPTIONS
##### CONNECT
##### TRACE
#### 三、HTTP 状态码
##### 1XX 信息
##### 2XX 成功
##### 3XX 重定向
##### 4XX 客户端错误
##### 5XX 服务器错误
#### 四、HTTP 首部
##### 通用首部字段
##### 请求首部字段
##### 响应首部字段
##### 实体首部字段
#### 五、具体应用
##### 连接管理
###### 1. 短连接与长连接
###### 2. 流水线
##### Cookie
###### 1. 用途
###### 2. 创建过程
###### 3. 分类
###### 4. 作用域
###### 5. JavaScript
###### 6. HttpOnly
###### 7. Secure
###### 8. Session
###### 9. 浏览器禁用 Cookie
###### 10. Cookie 与 Session 选择
##### 缓存
###### 1. 优点
###### 2. 实现方法
###### 3. Cache-Control
###### 4. 缓存验证
##### 内容协商
###### 1. 类型
###### 2. Vary
##### 内容编码
##### 范围请求
###### 1. Range
###### 2. Accept-Ranges
###### 3. 响应状态码
##### 分块传输编码
##### 多部分对象集合
##### 虚拟主机
##### 通信数据转发
###### 1. 代理
###### 2. 网关
###### 3. 隧道
#### 六、HTTPS
##### 加密
###### 1. 对称密钥加密
###### 2.非对称密钥加密
###### 3. HTTPS 采用的加密方式
##### 认证
##### 完整性保护
##### HTTPS 的缺点
#### 七、HTTP/2.0
##### HTTP/1.x 缺陷
##### 二进制分帧层
##### 服务端推送
##### 首部压缩
#### 八、HTTP/1.1 新特性
#### 九、GET 和 POST 比较
##### 作用
##### 参数
##### 安全
##### 幂等性
##### 可缓存
##### XMLHttpRequest
#### 参考资料
