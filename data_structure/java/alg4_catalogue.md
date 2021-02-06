
目录

## 第1章　 基础 　 

1.1　基础编程模型　　 

1.1.1　Java程序的基本结构　　 

1.1.2　原始数据类型与表达式　 

1.1.3　 语句　　 

1.1.4　 简便记法　　 

1.1.5　 数组　　 

1.1.6　 静态方法　　 

1.1.7　 API　　 

1.1.8　 字符串　　 

1.1.9　 输入输出　　 

1.1.10　 二分查找　　 

1.1.11　 展望　　 

1.2　 数据抽象　　 

1.2.1　 使用抽象数据类型　　 

1.2.2　 抽象数据类型举例　　 

1.2.3　 抽象数据类型的实现　　 

1.2.4　 更多抽象数据类型的实现　　 

1.2.5　 数据类型的设计　 

1.3　 背包、队列和栈　　 

1.3.1　 API　　 

1.3.2　 集合类数据类型的实现　　 

1.3.3　 链表　　 

1.3.4　 综述　　 

1.4　 算法分析　　 

1.4.1　 科学方法　　 

1.4.2　 观察　　 

1.4.3　 数学模型　　 

1.4.4　 增长数量级的分类　　 

1.4.5　 设计更快的算法　　 

1.4.6　 倍率实验　　 

1.4.7　 注意事项　 

1.4.8　 处理对于输入的依赖　　 

1.4.9　 内存　　 

1.4.10　 展望　　 

1.5　 案例研究：union-find算法　　 

1.5.1　 动态连通性　　 

1.5.2　 实现　　 

1.5.3　 展望　

代码： 

|序号|题目|级别|
|:-----|:-----|:-----|
||BinarySearch.java|binary search| 
||RandomSeq.java|random numbers in a given range| 
||Average.java|average of a sequence of numbers| 
||Cat.java|concatenate files|
||Knuth.java|Knuth shuffle|
||Counter.java|counter|
||StaticSETofInts.java|set of integers|
||Allowlist.java|allowlist client|
||Vector.java|Euclidean vector|
||Date.java|date|
||Transaction.java|transaction|
||Point2D.java|point|
||RectHV.java|axis-aligned rectangle|
||Interval1D.java|1d interval|
||Interval2D.java|2d interval|
||Accumulator.java|running average and stddev|
|1.1|ResizingArrayStack.java|LIFO stack (resizing array)|
|1.2|LinkedStack.java|LIFO stack (linked list)|
||Stack.java|LIFO stack|
||ResizingArrayQueue.java|FIFO queue (resizing array)|
|1.3|LinkedQueue.java|FIFO queue (linked list)|
||Queue.java|FIFO queue|
||ResizingArrayBag.java|multiset (resizing array)|
|1.4|LinkedBag.java|multiset (linked list)|
||Bag.java|multiset|
||Stopwatch.java|timer (wall time)|
||StopwatchCPU.java|timer (CPU time)|
||LinearRegression.java|simple linear regression|
||ThreeSum.java|brute-force three sum|
||ThreeSumFast.java|faster three sum|
||DoublingTest.java|doubling test|
||DoublingRatio.java|doubling ratio|
||QuickFindUF.java|quick find|
||QuickUnionUF.java|quick union|
|1.5|WeightedQuickUnionUF.java|weighted quick union|
||UF.java|union-by-rank with path halving|



## 第2章　 排序 　 

2.1　 初级排序算法　　 

2.1.1　 游戏规则　　 

2.1.2　 选择排序　　 

2.1.3　 插入排序　　 

2.1.4　 排序算法的可视化　　 

2.1.5　 比较两种排序算法　　 

2.1.6　 希尔排序　　 

2.2　 归并排序　　 

2.2.1　 原地归并的抽象方法　　 

2.2.2　 自顶向下的归并排序　　 

2.2.3　 自底向上的归并排序　　 

2.2.4　 排序算法的复杂度　　 

2.3　 快速排序　　 

2.3.1　 基本算法　　 

2.3.2　 性能特点　　 

2.3.3　 算法改进　　 

2.4　 优先队列　　 

2.4.1　 API　　 

2.4.2　 初级实现　　 

2.4.3　 堆的定义　　 

2.4.4　 堆的算法　　 

2.4.5　 堆排序　　 

2.5　 应用　　 

2.5.1　 将各种数据排序　　 

2.5.2　 我应该使用哪种排序算法　　 

2.5.3　 问题的归约　　 

2.5.4　 排序应用一览

代码: 

|序号|题目|级别|
|:-----|:-----|:-----|
|2.1|Insertion.java|insertion sort|
||InsertionX.java|insertion sort (optimized)|
||BinaryInsertion.java|binary insertion sort|
|2.2|Selection.java|selection sort|
|2.3|Shell.java|shellsort|
|2.4|Merge.java|top-down mergesort|
||MergeBU.java|bottom-up mergesort|
||MergeX.java|optimized mergesort|
||Inversions.java|number of inversions|
|2.5|Quick.java|quicksort|
||Quick3way.java|quicksort with 3-way partitioning|
||QuickX.java|optimized 2-way quicksort|
||QuickBentleyMcIlroy.java|optimized 3-way quicksort|
||TopM.java|priority queue client|
|2.6|MaxPQ.java|max heap priority queue|
||MinPQ.java|min heap priority queue|
||IndexMinPQ.java|index min heap priority queue|
||IndexMaxPQ.java|index max heap priority queue|
||Multiway.java|multiway merge|
|2.7|Heap.java|heapsort|

## 第3章　查找 　 

3.1　符号表　　 

3.1.1　API　　 

3.1.2　有序符号表　　 

3.1.3　用例举例　　 

3.1.4　无序链表中的顺序查找　　 

3.1.5　有序数组中的二分查找　　 

3.1.6　对二分查找的分析　　 

3.1.7　预览　　 

3.2　二叉查找树　　 

3.2.1　基本实现　　 

3.2.2　分析　　 

3.2.3　有序性相关的方法与删除操作　　 

3.3　平衡查找树　　 

3.3.1　2-3查找树　　 

3.3.2　红黑二叉查找树　　 

3.3.3　实现　　 

3.3.4　删除操作　　 

3.3.5　红黑树的性质　　 

3.4　散列表　　 

3.4.1　散列函数　　 

3.4.2　基于拉链法的散列表　　 

3.4.3　基于线性探测法的散列表　　 

3.4.4　调整数组大小　　 

3.4.5　内存使用　　 

3.5　应用　　 

3.5.1　我应该使用符号表的哪种实现　　 

3.5.2　集合的API　　 

3.5.3　字典类用例　　 

3.5.4　索引类用例　　 

3.5.5　稀疏向量　　

代码：

python:

|序号|题目|级别|
|:-----|:-----|:-----|
||FrequencyCounter.java|frequency counter|
|3.1|SequentialSearchST.java|sequential search|
|3.2|BinarySearchST.java|binary search|
|3.3|BST.java|binary search tree|
|3.4|RedBlackBST.java|red-black tree|
|3.5|SeparateChainingHashST.java|separate chaining hash table|
|3.6|LinearProbingHashST.java|linear probing hash table|
||ST.java|ordered symbol table|
||SET.java|ordered set|
||DeDup.java|remove duplicates|
||AllowFilter.java|allowlist filter|
||BlockFilter.java|blocklist filter|
||LookupCSV.java|dictionary lookup|
||LookupIndex.java|index and inverted index|
||FileIndex.java|file indexing|
||SparseVector.java|sparse vector|


## 第4章　 图 　　 

4.1　 无向图　　 

4.1.1　 术语表　　 

4.1.2　 表示无向图的数据类型　　 

4.1.3　 深度优先搜索　　 

4.1.4　 寻找路径　　 

4.1.5　 广度优先搜索　　 

4.1.6　 连通分量　　 

4.1.7　 符号图　　 

4.1.8　 总结　　 

4.2　 有向图　　 

4.2.1　 术语 

4.2.2　 有向图的数据类型　　 

4.2.3　 有向图中的可达性　　 

4.2.4　 环和有向无环图　　 

4.2.5　 有向图中的强连通性　　 

4.2.6　 总结　　 

4.3　 最小生成树　　 

4.3.1　 原理　　 

4.3.2　 加权无向图的数据类型　　 

4.3.3　 最小生成树的API和测试用例　　 

4.3.4　 Prim算法　　 

4.3.5　 Prim算法的即时实现　　 

4.3.6　 Kruskal算法　　 

4.3.7　 展望　　 

4.4　 最短路径　　 

4.4.1　 最短路径的性质　 

4.4.2　 加权有向图的数据结构　　 

4.4.3　 最短路径算法的理论基础　　 

4.4.4　 Dijkstra算法　 

4.4.5　 无环加权有向图中的最短路径算法　 

4.4.6　 一般加权有向图中的最短路径问题　　 

4.4.7　 展望　　 

代码：

python:

|序号|题目|级别|
|:-----|:-----|:-----|
||Graph.java|undirected graph|
||GraphGenerator.java|generate random graphs|
||DepthFirstSearch.java|depth-first search in a graph|
||NonrecursiveDFS.java|DFS in a graph (nonrecursive)|
|4.1|DepthFirstPaths.java|paths in a graph (DFS)|
|4.2|BreadthFirstPaths.java|paths in a graph (BFS)|
|4.3|CC.java|connected components of a graph|
||Bipartite.java|bipartite or odd cycle (DFS)|
||BipartiteX.java|bipartite or odd cycle (BFS)|
||Cycle.java|cycle in a graph|
||EulerianCycle.java|Eulerian cycle in a graph|
||EulerianPath.java|Eulerian path in a graph|
||SymbolGraph.java|symbol graph|
||DegreesOfSeparation.java|degrees of separation|
||Digraph.java|directed graph|
||DigraphGenerator.java|generate random digraphs|
|4.4|DirectedDFS.java|depth-first search in a digraph|
||NonrecursiveDirectedDFS.java|DFS in a digraph (nonrecursive)|
||DepthFirstDirectedPaths.java|paths in a digraph (DFS)|
||BreadthFirstDirectedPaths.java|paths in a digraph (BFS)|
||DirectedCycle.java|cycle in a digraph|
||DirectedCycleX.java|cycle in a digraph (nonrecursive)|
||DirectedEulerianCycle.java|Eulerian cycle in a digraph|
||DirectedEulerianPath.java|Eulerian path in a digraph|
||DepthFirstOrder.java|depth-first order in a digraph|
|4.5|Topological.java|topological order in a DAG|
||TopologicalX.java|topological order (nonrecursive)|
||TransitiveClosure.java|transitive closure|
||SymbolDigraph.java|symbol digraph|
|4.6|KosarajuSharirSCC.java|strong components (KosarajuSharir)|
||TarjanSCC.java|strong components (Tarjan)|
||GabowSCC.java|strong components (Gabow)|
||EdgeWeightedGraph.java|edge-weighted graph|
||Edge.java|weighted edge|
||LazyPrimMST.java|MST (lazy Prim)|
|4.7|PrimMST.java|MST (Prim)|
|4.8|KruskalMST.java|MST (Kruskal)|
||BoruvkaMST.java|MST (Boruvka)|
||EdgeWeightedDigraph.java|edge-weighted digraph|
||DirectedEdge.java|"weighted| directed edge"|
|4.9|DijkstraSP.java|shortest paths (Dijkstra)|
||DijkstraUndirectedSP.java|undirected shortest paths (Dijkstra)|
||DijkstraAllPairsSP.java|all-pairs shortest paths|
|4.1|AcyclicSP.java|shortest paths in a DAG|
||AcyclicLP.java|longest paths in a DAG|
||CPM.java|critical path method|
|4.11|BellmanFordSP.java|shortest paths (BellmanFord)|
||EdgeWeightedDirectedCycle.java|cycle in an edge-weighted digraph|
||Arbitrage.java|arbitrage detection|
||FloydWarshall.java|all-pairs shortest paths (dense)|
||AdjMatrixEdgeWeightedDigraph.java|edge-weighted graph (dense)|


## 第5章　 字符串  

5.1　 字符串排序　　 

5.1.1　 键索引计数法　　 

5.1.2　 低位优先的字符串排序　　 

5.1.3　 高位优先的字符串排序　　 

5.1.4　 三向字符串快速排序　　 

5.1.5　 字符串排序算法的选择　　 

5.2　 单词查找树　　 

5.2.1　 单词查找树　　 

5.2.2　 单词查找树的性质　　 

5.2.3　 三向单词查找树　　 

5.2.4　 三向单词查找树的性质　　 

5.2.5　 应该使用字符串符号表的哪种实现　　 

5.3　 子字符串查找　　 

5.3.1　 历史简介　　 

5.3.2　 暴力子字符串查找算法　　 

5.3.3　 Knuth-Morris-Pratt子字符串查找算法　　 

5.3.4　 Boyer-Moore字符串查找算法　　 

5.3.5　 Rabin-Karp指纹字符串查找算法　　 

5.3.6　 总结 

5.4　 正则表达式　　 

5.4.1　 使用正则表达式描述模式　　 

5.4.2　 缩略写法　　 

5.4.3　 正则表达式的实际应用　　 

5.4.4　 非确定有限状态自动机　　 

5.4.5　 模拟NFA的运行　　 

5.4.6　 构造与正则表达式对应的

5.5　 数据压缩　　 

5.5.1　 游戏规则　　 

5.5.2　 读写二进制数据　　 

5.5.3　 局限　　 

5.5.4　 热身运动：基因组　　 

5.5.5　 游程编码　　 

5.5.6　 霍夫曼压缩　　 

代码： 

|序号|题目|级别|
|:-----|:-----|:-----|
||Alphabet.java|alphabet|
||Count.java|alphabet client|
|5.1|LSD.java|LSD radix sort|
|5.2|MSD.java|MSD radix sort|
||InplaceMSD.java|In-place MSD radix sort1|
|5.3|Quick3string.java|3-way string quicksort|
||AmericanFlag.java|American flag sort1|
||AmericanFlagX.java|non-recursive American flag sort1|
|5.4|TrieST.java|multiway trie symbol table|
||TrieSET.java|multiway trie set|
|5.5|TST.java|ternary search trie|
|5.6|KMP.java|substring search (KnuthMorrisPratt)|
|5.7|BoyerMoore.java|substring search (BoyerMoore)|
|5.8|RabinKarp.java|substring search (RabinKarp)|
|5.9|NFA.java|NFA for regular expressions|
||GREP.java|grep|
||BinaryDump.java|binary dump|
||HexDump.java|hex dump|
||PictureDump.java|picture dump|
||Genome.java|genomic code|
||RunLength.java|data compression (run-length coding)|
|5.1|Huffman.java|data compression (Huffman)|
|5.11|LZW.java|data compression (LempelZivWelch)|

## 第6章　 背景 　

|序号|题目|级别|
|:-----|:-----|:-----|
|6.1|CollisionSystem.java|collision system|
||Particle.java|particle|
|6.2|BTree.java|B-tree|
|6.3|SuffixArray.java|suffix array (suffix sorting)|
||SuffixArrayX.java|suffix array (optimized)|
||LongestRepeatedSubstring.java|longest repeated substring|
||KWIK.java|keyword in context|
||LongestCommonSubstring.java|longest common substring|
|6.4|FordFulkerson.java|maxflowmincut|
||FlowNetwork.java|capacitated network|
||FlowEdge.java|capacitated edge with flow|
||GlobalMincut.java|global mincut (StoerWagner)5|
||BipartiteMatching.java|bipartite matching (alternating path)|
||HopcroftKarp.java|bipartite matching (HopcroftKarp)|
||AssignmentProblem.java|weighted bipartite matching|
||LinearProgramming.java|linear programming (simplex)|
||TwoPersonZeroSumGame.java|two-person zero-sum game|


9	BEYOND

|序号|题目|级别|
|:-----|:-----|:-----|
||GaussianElimination.java|Gaussian elimination|
||GaussJordanElimination.java|GaussJordan elimination|
||FFT.java|Fast Fourier transform|
||Complex.java|complex number|
||Polynomial.java|polynomial (integer)|
||GrahamScan.java|2d convex hull (Graham scan)|
||FarthestPair.java|2d farthest pair (rotating calipers)|
||ClosestPair.java|2d closest pair|
||FenwickTree.java|Fenwich tree2|
||SegmentTree.java|Segment tree2|
||PatriciaST.java|PATRICIA trie symbol table3|
||PatriciaSET.java|PATRICIA trie set3|
||MultiwayMinPQ.java|Multiway heap4|
||IndexMultiwayMinPQ.java|Index multiway heap4|
||BinomialMinPQ.java|Binomial heap4|
||IndexBinomialMinPQ.java|Index binomial heap4|
||FibonacciMinPQ.java|Fibonacci heap4|
||IndexFibonacciMinPQ.java|Index Fibonacci heap4|
||AVLTreeST.java|AVL tree5|
