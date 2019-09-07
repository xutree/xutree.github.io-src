Title: 算法笔记
Category: 基础知识
Tags: 算法

[TOC]

## 1. 排序

### 1.1 Bubble Sort

- 时间复杂度：最好：$\mathcal{O}(n)$， 最坏：$\mathcal{O}(n^2)$，平均：$\mathcal{O}(n^2)$
- 空间复杂度：$\mathcal{O}(1)$
- 稳定排序
- 外层循环优化：某一趟无交换，终止
- 内层循环优化：记录最后交换的位置，其后为有序区

```
def bubble_sort(arr):
    k = len(arr) - 1
    pos = 0
    for i in range(len(arr)):
        flag = True
        for j in range(k):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
                pos = j
        k = pos
        if flag:
            break
```

### 1.2 选择排序

从无序区选择最小（最大）插入到有序区的最后（最前）。

- 时间复杂度：最好：$\mathcal{O}(n^2)$， 最坏：$\mathcal{O}(n^2)$，平均：$\mathcal{O}(n^2)$
- 空间复杂度：$\mathcal{O}(1)$
- 不稳定排序

```
def selection_sort(arr):
    for i in range(len(A)):

        # Find the minimum element in remaining  
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]
```

### 1.3  插入排序

对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

- 时间复杂度：最好：$\mathcal{O}(n)$， 最坏：$\mathcal{O}(n^2)$，平均：$\mathcal{O}(n^2)$
- 空间复杂度：$\mathcal{O}(1)$
- 稳定排序

```
def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in reversed(range(i)):
            # 单向冒泡 [0, i] 区间
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
```

### 1.4 希尔排序

缩小增量排序，是插入排序的一种更高效的改进版本。

- 时间复杂度：最好：$\mathcal{O}(n)$， 最坏：$\mathcal{O}(n^2)$，平均：增量相关
- 空间复杂度：$\mathcal{O}(1)$
- 不稳定排序

```
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap:
        # 组内插入排序，单向冒泡即可
        for i in range(gap, n):
            j = i
            while (j - gap) >= 0:
                if arr[j - gap] > arr[j]:
                    arr[j - gap], arr[j] = arr[j], arr[j - gap]
                    j -= gap
                else:
                    break
        gap //= 2
```

### 1.5 归并排序

分治法（Divide and Conquer），2-路归并。

- 时间复杂度：最好：$\mathcal{O}(n\log_2n)$， 最坏：$\mathcal{O}(n\log_2n)$，平均：$\mathcal{O}(n\log_2n)$
- 空间复杂度：$\mathcal{O}(n)$
- 稳定排序
- 可优化为 $\mathcal{O}(1)$ 空间复杂度（手摇算法），此时 merge 的时间复杂度为 $\mathcal{O}(n^2)$，算法整体时间复杂度为 $\mathcal{O}(n^2\log_2n)$


```
# Python program for implementation of MergeSort

def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements, shalllow copy
        R = arr[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
```

### 1.6 快速排序

通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

- 时间复杂度：最好：$\mathcal{O}(n\log_2n)$， 最坏：$\mathcal{O}(n^2)$，平均：$\mathcal{O}(n\log_2n)$
- 空间复杂度：$\mathcal{O}(n)$~$\mathcal{O}(\log_2n)$
- 不稳定排序
- 优化1：三平均分区法
- 优化2：当分区的规模达到一定小时，便停止快速排序算法
- 优化3：在递归排序子分区的时候，总是选择优先排序那个最小的分区

归并排序每次递归需要用到一个辅助表，长度与待排序的表相等，虽然递归次数是 $\mathcal{O}(\log_2n)$，但每次递归都会释放掉所占的辅助空间，所以下次递归的栈空间和辅助空间与这部分释放的空间就不相关了，因而空间复杂度还是 $\mathcal{O}(n)$。

而快速排序每次递归都会返回一个中间值的位置，必须使用栈。所以空间复杂度就是递归深度。

```
def quick_sort(arr, left, right):
    if (left < right):
        i, j = left, right
        temp = arr[i]
        while i < j:
            while (i < j and arr[j] > temp):
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1
            while (i < j and arr[i] <= temp):
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = temp
        quick_sort(arr, left, i - 1)
        quick_sort(arr, i + 1, right)
```

### 1.7  堆排序

- 时间复杂度：最好：$\mathcal{O}(n\log_2n)$， 最坏：$\mathcal{O}(n\log_2n)$，平均：$\mathcal{O}(n\log_2n)$
- 空间复杂度：$\mathcal{O}(1)$
- 不稳定排序

```
def heap_sort(arr):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break
    # 创建最大堆
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(start, len(arr) - 1)
    # 堆排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end - 1)
    return arr
```

### 1.8 计数排序

- 时间复杂度：最好：$\mathcal{O}(n+k)$， 最坏：$\mathcal{O}(n+k)$，平均：$\mathcal{O}(n+k)$
- 空间复杂度：$\mathcal{O}(n+k)$
- 稳定排序

```
def counting_sort(arr, k):
    n = len(arr)
    count = [0] * (k + 1)
    temp = [0] * n

    for i in arr:
        count[i] += 1
    for i in range(1, k+1):
        count[i] = count[i] + count[i-1]
    # 反向填充保证稳定性
    for i in arr[::-1]:
        temp[count[i]-1] = i
        count[i] -= 1
    return temp
```

### 1.9 桶排序

桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。

### 1.10 基数排序

基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。

## 2.中位数和顺序统计量

- 查找最大值或最小值只需扫描一遍，挨个比较 $\mathcal{O}(n)$
- 同时查找最大和最小，可以成对处理
- 一般的选择问题可以通过分治划分达到线性时间期望
- 有最坏情况为线性时间的选择算法
