# 希尔排序


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "the list is", alist)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentValue = alist[i]
        position = i

        while position > gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position = position-gap
        alist[position] = currentValue


a = [1,6,4,3,5,7]
shellSort(a)
print(a)