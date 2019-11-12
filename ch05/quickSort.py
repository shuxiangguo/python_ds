# 快速排序


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    print("Quick sort ", alist, alist[first], alist[last])
    if first < last:
        splitpoint = partition2(alist, first, last)
        quick_sort_helper(alist, first, splitpoint-1)
        quick_sort_helper(alist, splitpoint+1, last)


def partition(alist, first, last):
    print("Partition ", alist, alist[first])
    pivot_value = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark = leftmark + 1
        while leftmark <= rightmark and alist[rightmark] >= pivot_value:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    return rightmark


# 三数取中作为基准值
def partition2(alist, first, last):
    mid = (first + last) // 2
    l = [alist[first], alist[mid], alist[last]]
    l.sort()

    pivot_value = a[1]
    alist[first], pivot_value = pivot_value, alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark = leftmark + 1
        while leftmark <= rightmark and alist[rightmark] >= pivot_value:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    return rightmark


a = [31, 26, 20, 17, 44, 54, 77, 55, 95]
quick_sort(a)
