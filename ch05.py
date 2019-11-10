# 有序列表的顺序搜索
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            return pos
        elif alist[pos] > item:
            stop = True
        else:
            pos = pos + 1
    return found


# 二分搜索
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    midpoint = 0

    while first <= last and not found:
        midpoint = (first+last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    print(found)
    if found:
        return midpoint
    else:
        return -1


# 二分搜索的递归版本
def binarySearchRecv(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return midpoint
        else:
            if item < alist[midpoint]:
                return binarySearchRecv(alist[:midpoint], item)
            else:
                return binarySearchRecv(alist[midpoint+1:], item)


print(binarySearchRecv([1,2,3,4,5,6,7,8], 5))