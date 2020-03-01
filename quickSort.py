#递归的快速排序
def quickSortRec(data):
    if len(data)<=1:
        return
    i=0
    j=len(data)-1
    flag = data[i]
    while i<j:
        while i<j and data[j]>=flag:
            j-=1
        while i<j and data[i]<=flag:
            i+=1
        if i<j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
    data[0] = data[j]
    data[j] = flag
    quickSortRec(data[:j])
    quickSortRec(data[j+1:])
    
    
    
#迭代的快速排序
def quickSortIter(data):
    #lte数组，储存未排序的子数组，其实只有一个数组，用i,j括起来的算一个数组
    ite = []
    ite.append((0,len(data)-1))
    while len(ite)>0:
        #取出一个未排数组
        li = ite.pop()
        #i,j代表数组的前后位置
        i = li[0]
        j = li[1]
        #取该数组第一个为基准数据
        flag = data[i]
        while i<j:
            #为保证ij重合时指向的数小于等于基准数据，j先动
            #j从右边找到比基准数据小的数
            while i<j and data[j]>=flag:
                j-=1
            #i从左边找到比基准数据打的数
            while i<j and data[i]<=flag:
                i+=1
            #i,j指向的数交换
            if i<j:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
        #i,j重合，指向的数与基准数交换
        #从基准数分割成两个数组，左边数组小于等于基准数，右边大于等于基准数
        data[li[0]] = data[j]
        data[j] = flag
        #储存左右长度大于等于2的数组
        if li[0]< j-1:
            ite.append((li[0],j-1))
        if j+1<li[1]:
            ite.append((j+1,li[1]))
