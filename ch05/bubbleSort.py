def bubbleSort(alist):

    for i in range(len(alist) - 1):
        for j in range(len(alist)-i-1):
            if alist[j+1] < alist[j]:
                # temp = alist[j+1]
                # alist[j+1] = alist[j]
                # alist[j] = temp
                alist[j+1], alist[j] = alist[j], alist[j+1]


# 优化后的冒泡排序，如果某次冒泡未发生交换，则表明已经有序了，停止
def bubbleSort2(alist):
    exchange = True
    passNum = len(alist) - 1
    while passNum > 0 and exchange:
        exchange = False
        for i in range(passNum):
            if alist[i+1] < alist[i]:
                alist[i+1], alist[i] = alist[i], alist[i+1]
                exchange = True
        passNum = passNum - 1


a = [1,4,6,3,2]
bubbleSort2(a)
print(a)