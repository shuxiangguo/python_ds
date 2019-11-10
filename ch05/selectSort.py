# 选择排序，每次选择最小的元素


def selectSort(alist):
    for i in range(len(alist) - 1):
        minIdx = i
        for j in range(i+1, len(alist), 1):
            if alist[j] < alist[minIdx]:
                minIdx = j
        alist[i], alist[minIdx] = alist[minIdx], alist[i]


# 选择排序，每次选择最大的元素
def selectSortMax(alist):
    for i in range(len(alist)-1, 0, -1):
        maxidx = i
        for j in range(0, i):
            if alist[j] > alist[maxidx]:
                maxidx = j
        alist[i], alist[maxidx] = alist[maxidx], alist[i]


a = [1,4,3,6,5]
selectSortMax(a)
print(a)


