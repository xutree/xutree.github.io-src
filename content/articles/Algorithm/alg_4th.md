Title: 算法（第四版）
Category: 读书笔记
Date: 2019-09-24 20:15:14
Modified: 2019-09-24 20:15:14
Tags: 算法

[TOC]

[https://book.douban.com/subject/19952400/](https://book.douban.com/subject/19952400/)

## 1. 基础

### 1.1 二分查找

适用于有序数组。

```
public static int rank(int key, int[] a) {
    int lo = 0;
    int hi = a.length - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (key < a[mid])
            hi = mid - 1;
        else if (key > a[mid])
            lo = mid + 1;
        else
            return mid;
    }
    return -1;
}
```

### 1.2 Dijkstra 双栈算术表达式求值算法

表达式又括号、运算符和操作数组成，从左往右开始处理：
- 将操作数压入操作数栈
- 将运算符压入运算符栈
- 忽略左括号
- 在遇到右括号时，弹出一个运算符，弹出所需数量的操作数，并将运算符和操作数的运算结果压入操作数

### 1.3 下压栈（链表实现）

```
public class Stack<Item> implements Iterable<Item> {
    private Node<Item> first;     // 栈顶
    private int n;                // 元素数量

    // 定义节点的嵌套类
    private static class Node<Item> {
        private Item item;
        private Node<Item> next;
    }

    // 构造函数初始化
    public Stack() {
        first = null;
        n = 0;
    }

    public boolean isEmpty() {
        return first == null;
    }

    public int size() {
        return n;
    }

    public void push(Item item) {
        Node<Item> oldfirst = first;
        first = new Node<Item>();
        first.item = item;
        first.next = oldfirst;
        n++;
    }

    public Item pop() {
        if (isEmpty()) throw new NoSuchElementException("Stack underflow");
        Item item = first.item;
        first = first.next;
        n--;
        return item;
    }

    public Item peek() {
        if (isEmpty()) throw new NoSuchElementException("Stack underflow");
        return first.item;
    }

    // 重写
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (Item item : this) {
            s.append(item);
            s.append(' ');
        }
        return s.toString();
    }

    // 重写迭代
    public Iterator<Item> iterator() {
       return new ListIterator(first);
   }

   private class ListIterator implements Iterator<Item> {
       private Node<Item> current;

       public ListIterator(Node<Item> first) {
           current = first;
       }

       public boolean hasNext() {
           return current != null;
       }

       public void remove() {
           throw new UnsupportedOperationException();
       }

       public Item next() {
           if (!hasNext()) throw new NoSuchElementException();
           Item item = current.item;
           current = current.next;
           return item;
       }
   }
}
```

### 1.4 队列（链表实现）

```
public class Queue<Item> implements Iterable<Item> {
    private Node<Item> first;
    private Node<Item> last;
    private int n;

    private static class Node<Item> {
        private Item item;
        private Node<Item> next;
    }

    public Queue() {
        first = null;
        last  = null;
        n = 0;
    }

    public boolean isEmpty() {
        return first == null;
    }

    public int size() {
        return n;
    }

    public Item peek() {
        if (isEmpty()) throw new NoSuchElementException("Queue underflow");
        return first.item;
    }

    public void enqueue(Item item) {
        Node<Item> oldlast = last;
        last = new Node<Item>();
        last.item = item;
        last.next = null;
        if (isEmpty()) first = last;
        else           oldlast.next = last;
        n++;
    }

    public Item dequeue() {
        if (isEmpty()) throw new NoSuchElementException("Queue underflow");
        Item item = first.item;
        first = first.next;
        n--;
        if (isEmpty()) last = null;
        return item;
    }

    public String toString() {
        StringBuilder s = new StringBuilder();
        for (Item item : this) {
            s.append(item);
            s.append(' ');
        }
        return s.toString();
    }

    public Iterator<Item> iterator()  {
        return new ListIterator(first);  
    }

    private class ListIterator implements Iterator<Item> {
        private Node<Item> current;

        public ListIterator(Node<Item> first) {
            current = first;
        }

        public boolean hasNext()  { return current != null;                     }
        public void remove()      { throw new UnsupportedOperationException();  }

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }
}
```

### 1.5 内存

以下讨论针对 64 位机器，机器地址需要 8 字节。

#### 1.5.1 对象

内存 =  所有实例变量 + 对象本身的开销（一般是 16 个字节）

开销包括：一个指向对象的类的引用、垃圾收集信息和同步信息

一般的内存会被填充成 8 字节的倍数。

`Integer`：24 字节 = 16（开销） + 4（int） + 4（填充）

`Date`：32 字节 = 16 + 3 * 4 + 4

#### 1.5.2 链表

如果嵌套的类是非静态的，还需要额外 8 个字节（指向外部类的引用），因此一个 Node 对象需要 40 字节。

`Node`：40 字节 = 16（开销） + 2 * 8（指向 Item 和 Node 对象）+ 8（额外）
`Stack`：32 + 64$N$ = 16 + 8（Node 引用）+ 4（int）+ 4（填充）+ （40 + 24） * $N$

#### 1.5.3 数组

一个原始数据类型的数组一般需要 24 字节的头信息。

24 = 16（开销）+ 4（长度）+ 4（填充）

数组的字节数等于头信息加上内部存储类型的字节数。

例如，$N$ 个字符的字符数组需要：24 + 2$N$ 字节

#### 1.5.4 字符串对象

`String` 的实现有 4 个实例变量：一个指向字符数组的引用（8 字节）和三个 `int` 值（各 4 字节）。

第一个 `int`：字符数组中的偏移量
第二个 `int`：字符串的长度
第三个 `int`：是一个散列值

每个 `String` 对象需要 40 字节。

40 = 16 + 8 + 3 * 4 + 4（填充）

`String` 数组需要：40 + 24 + 2$N$ 字节。

`String` 的 `char` 数组通常在多个字符串之间共享，因为 `String` 对象是不可变的，这种设计使它能够在多个对象都含有相同的 `value[]` 数组时节省内存。

当你调用 `substring()` 方法是，就创建了一个新的 `String` 对象（40 字节），但它仍然重用了相同的 `value[]` 数组，因此该字符串的子字符串只会使用 40 字节的内存。

一个子字符串所需的额外内存是一个常数，构造一个子字符串所需的时间也是常数。


### 1.x 答疑

- `Java` 字节码是程序的一种低级表示，可以运行于 `Java` 的虚拟机，将程序抽象为字节码可以保证代码可以运行在各种设备之上
- 原始数据类型“原始”是因为缺少溢出检查
- `Math.abs(-2147483648)` 返回 `-2147483648`
- `Double.POSITIVE_INFINITY`、`Double.NEGATIVE_INFINITY`
- `1/0`：除零异常，`1.0/0.0`：`Infinity`
- 不能对 `String` 对象使用比较运算符，只有原始数据类型定义了这些操作
- 商向 0 取整，余数保证 `(a / b) * b + a % b` 恒等于 `a`
- `while` 循环结束后递增变量仍然可用，这是和 `for` 的主要区别
- 在 `Java` 中，一个静态方法不能将另一个静态方法作为参数
- `Java` 编程的基础主要是使用 `class` 关键字构造被称为**引用类型**的数据类型
- 每次调用 `new()`：为新的对象分配内存空间；调用构造函数；返回该函数的一个引用
- 原始数据类型更接近计算机硬件所支持的数据类型，使用它们的程序比使用引用类型的程序快，这是其存在的意义
- 创建一个含有 $N$ 个对象的数据，需要使用 $N+1$ 次 `new` 关键字，数组创建一次，每个对象各需要一个
- **背包**：是一种不支持从中删除元素的集合数据类型，它的目的就是帮助用例收集元素并迭代遍历所有收集到的元素
- 私有嵌套类只有包含它的类能够直接访问他的实例变量，因此无需将它的实例变量声明为私有的或共有的
- `Java` 的命名规则会使用 `$` 分割外部类和内部类，比如 *Stack$Node.class*
- 我们可以用 `foreach` 循环访问数组，尽管数组没有实现 `Iterable` 接口
- 我们不可以用 `foreach` 循环访问 `String`，因为其没有实现 `Iterable` 接口
- 尽量避免宽接口，`Java` 中的 `java.util.ArrayList`、`java.util.LinkedList`、`java.util.Stack` 都是宽接口

## 2. 排序

### 2.1 选择排序

对于长度为 $N$ 的数组，选择排序需要大约 $N^2/2$ 次比较和 $N$ 次交换。

- 数据移动是最少的
- 运行时间和输入无关
- 不稳定排序
- 时间复杂度：$\Theta (n^2)$
- 空间复杂度：$O(1)$

```
public static void sort(int[] a) {
    int N = a.length;
    for (int i = 0; i < N; i++) {
        int min = i;
        for (int j = i + 1; j < N; j++) {
            if (a[j] < a[min]) min = j;
        }
        swap(a, i, min);
    }
}
```

### 2.2 插入排序

对于长度为 $N$ 且无重复元素的数组，平均情况下插入排序需要大约 $N^2/4$ 次比较和 $N^2/4$ 次交换，最坏情况下需要大约 $N^2/2$ 次比较和 $N^2/2$ 次交换，最好情况下需要 $N-1$ 次比较和 0 次交换。

常用于部分有序的数组和少量元素数组的排序。

- 最坏时间复杂度：$O(n^2)$
- 最优时间复杂度：$O(n)$
- 平均时间复杂度：$\Theta (n^2)$
- 最坏空间复杂度：$O(1)$
- 稳定排序

```
public static void sort(int[] a) {
    int N = a.length;
    for (int i = 1; i < N; i++) {
        for (int j = i; j > 0 && a[j] < a[j - 1]; j--) {
            swap(a, j, j - 1);
        }
    }
}
```

### 2.3 希尔排序

- 最坏时间复杂度：$O(n^2)$
- 最优时间复杂度：$O(n)$
- 平均时间复杂度：$O(n^{1.3})$
- 最坏空间复杂度：$O(1)$
- 不稳定排序

```
public static void sort(int[] a) {
    int N = a.length;
    int h = N / 2;
    while (h >= 1) {
        for (int i = h; i < N; i++) {
            for (int j = i; j >= h && a[j] < a[j - h]; j-= h) {
                swap(a, j, j - h);
            }
        }
        h = h / 2;
    }
}
```

### 2.4 归并排序

- 时间复杂度：$\Theta (n \log n)$
- 空间复杂度：$O(n)$
- 稳定排序

```
public static void merge(int[] a, int lo, int mid, int hi) {
    int i = lo, j = mid + 1;
    for (int k = lo; k <= hi; k++) {
        aux[k] = a[k];
    }
    for (int k = lo; k <= hi; k++) {
        if (i > mid) {
            a[k] = aux[j++];
        } else if (j > hi) {
            a[k] = aux[i++];
        } else if (aux[j] < aux[i]) {
            a[k] = aux[j++];
        } else {
            a[k] = aux[i++];
        }
    }
}
```

#### 2.4.1 自顶向下

```
public static void sort(int[] a, int lo, int hi) {
    if (hi <= lo) return;
    int mid = (lo + hi) / 2;
    sort(a, lo, mid);
    sort(a, mid + 1, hi);
    merge(a, lo, mid, hi);
}
```

#### 2.4.2 自底向上

```
public static void sort(int[] a) {
    int N = a.length;
    for (int sz = 1; sz < N; sz = sz + sz) {
        for (int lo = 0; lo < N - sz; lo += sz + sz) {
            merge(a, lo, lo + sz - 1, Math.min(lo + sz + sz - 1, N - 1))
        }
    }
}
```

比较适合链表组织的结构，不需要任何新的链表节点，只需要重新组织链表就可以原地排序。

### 2.5 快速排序

包含大量相同元素会影响性能，可随机打乱或者利用三向切分。

- 最坏时间复杂度：$O(n^2)$
- 最优时间复杂度：$O(n\log n)$
- 平均时间复杂度：$O(n\log n)$
- 空间复杂度：$O(\log n) ~ O(n)$
- 不稳定排序

```
private static int partition(int[] a, int lo, int hi) {
    int i = lo, j = hi + 1;
    int v = a[lo];
    while (true) {
        while (a[++i] < v) if (i == hi) break;
        while (v < a[--j]) if (j == lo) break;
        if (i >= j) break;
        swap(a, i, j)
    }
    swap(a, lo, j);
    return j;
}

public static void sort(int[] a, int lo, int hi) {
    if (hi <= lo) return;
    int j = partition(a, lo, hi);
    sort(a, lo, j - 1);
    sort(a, j + 1, hi);
}
```

```
public static void sort(int[] a, int lo, int hi) {
    if (hi <= lo) return;
    int lt = lo, i = lo + 1, gt = hi;
    int v = a[lo];
    while (i <= gt) {
        if (a[i] < v) swap(a, lt++, i++);
        else if (a[i] > v) swap(a, i, gt--);
        else i++;
    }
    sort(a, lo, lt - 1);
    sort(a, gt + 1, hi);
}
```

一个应用，查找第 $k$ 个元素：

```
public static int select(int[] a, int k) {
    int lo = 0, hi = a.length - 1;
    while (hi > lo) {
        int j = partition(a, lo, hi);
        if (j == k) return a[k];
        else if (j > k) hi = j - 1;
        else if (j < k) lo = j + 1;
    }
    return a[k];
}
```

### 2.6 堆排序（针对大顶堆）

- 时间复杂度：$O(n\log n)$
- 空间复杂度：$O(1)$
- 不稳定排序

堆排序是已知的唯一能够同时最优利用时间和空间的方法，在最坏的情况下也能保证使用 $2n\log n$ 次比较和恒定的额外空间。

在现代系统的许多应用中很少使用它，因为它无法利用缓存，堆排序时数组元素很少和相邻的其他元素比较，缓存命中很低。

用堆实现的优先队列在现代应用程序中越来越重要，因为它能在插入操作和删除最大元素操作混合的动态场景中保证对数级别的运行时间。

下沉操作

```
public static void sink(int[] a, int k, int N) {
    while (2 * k + 1 < N) {
        int j = 2 * k + 1;
        if (j + 1 < N && a[j] < a[j + 1]) j++;
        if (a[j] < a[k]) break;
        swap(a, k, j);
        k = j;
    }
}
```

上浮操作

```
public static void swim(int[] a, int k, int N) {
    while (k > 0 && a[(k - 1) / 2] < a[k]) {
        swap(a, (k - 1) / 2, k);
        k = (k - 1) / 2;
    }
}
```

```
public static void sort(int[] a) {
    int N = a.length;
    for (int k = N / 2 - 1; k >= 0; k--) {
        sink(a, k, N);
    }
    while (N > 0) {
        swap(a, 0, --N);
        sink(a, 0, N);
    }
}
```

### 2.x  答疑

- 在研究排序算法时，我们需要计算比较和交换的数量，对于不交换元素的算法，我们会计算访问数组的次数
- **优先队列**：在某些数据处理的例子中，比如 TopM 和 Multiway，总数据量太大，无法排序（甚至无法全部装进内存）。例如 10 亿里面找 10 个，有了优先队列，只需要一个能存储十个元素的队列即可
- `Java` 中的优先队列：`java.util.PriorityQueue`

## 3. 查找
