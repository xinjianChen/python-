# python-

###取一个长度10000的随机数组
data = np.random.randint(1,10000,[10000])
data1 = np.copy(data)
data2 = np.copy(data)
###迭代耗时
quickSortIter(data1)
0.053882 s
###递归耗时
quickSortRec(data2)
0.056117 s

##python体验快速排序，递归竟然和迭代消耗的时间很接近，可能python内部对递归做了优化?
