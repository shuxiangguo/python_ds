# 插入排序


def insertSort(alist):
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentValue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentValue

a = [1,6,4,3,5]
insertSort(a)
print(a)