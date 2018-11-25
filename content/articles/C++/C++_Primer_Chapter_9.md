Title: C++ Primer 第九章 顺序容器
Category: 读书笔记
Date: 2018-10-16 22:43:16
Modified: 2018-10-17 11:12:28
Tags: C++

一个容器就是一些特定类型对象的集合。顺序容器（sequential container）为程序员提供了控制元素存储和访问顺序的能力。这种顺序不依赖于元素的值，而是与元素加入容器时的位置相对应。

## 顺序容器概述

| 类型 | 简介 |
| :------------- | :------------- |
| `vector` | 可变大小数组。支持快速随机访问。在尾部之外的位置插入或删除元素可能很慢 |
| `deque`  | 双端队列。支持快速随机访问。在头尾位置插入或删除速度很快 |
| `list`   | 双向链表。只支持双向顺序访问。在任何位置进行插入或删除都很快 |
| `forward_list` | 单向链表。只支持单向顺序访问。在任何位置进行插入或删除都很快 |
| `array` | 固定大小数组。支持快速随机访问。不能添加或删除元素 |
| `string` | 与`vector`相似的容器，专门用于保存字符。随机访问快。在尾部插入或删除快 |

`string`和`vector`保存在连续的内存空间中，因此由下标计算地址非常快速。

`forward_list`的设计目标是达到与最好的手写的单向链表数据结构相当的性能，因此不提供`size`操作，因为保存和计算大小会增加开销。

通常，`vector`是最好的选择。

每个容器都定义在同名的头文件中，容器均是模板类。

## 容器库概览

### 类型别名

| 类型别名 | 意义 |
| :------------- | :------------- |
| `iterator` | 此容器类型的迭代器类型 |
| `const_iterator` | 常量迭代器类型 |
| `size_type` | 无符号整数，足够保存此种容器的最大大小 |
| `difference_type` | 带符号整数，足够保存两个迭代器之间的距离 |
| `value_type` | 元素类型 |
| `reference` | 元素的左值类型，与`value_type&`含义相同 |
| `const_reference` | 常量左值类型 |

### 构造函数

| 构造函数 | 意义 |
| :------------- | :------------- |
| C c; | 默认构造函数，构造空容器。如果 c 是一个`array`，则元素按默认方式初始化|
| C c1(c2); | 构造 c2 的拷贝 c1，必须为相同类型，且保存元素也相同|
| C c1 = c2; | 同上 |
| C c(b, e); | 构造 c，将迭代器指定的范围内的元素拷贝到 c，类型要相容（`array`不支持）|
| C c{a, b, c...}; | 列表初始化，类型要相容，遗漏元素值初始化 |
| C c = {a, b, c...}; | 同上 |
| C seq(n); | 包含 n 个元素并进行值初始化，是`explicit`构造函数（`string`不要求explicit）|
| C seq(n, t); | 包含 n 个初始值为 t 的元素|

只有顺序容器（不包括`array`的构造函数才能接受大小参数）。如果元素类型没有默认构造函数，除了大小参数外，还需要显式指定元素初始值。`array`支持拷贝和赋值（内置数组不行）。

### 赋值与 swap

| 赋值与 swap | 意义 |
| :------------- | :------------- |
| c1 = c2; | 将 c1 中的元素替换成 c2 中的元素，类型要相同 |
| c1 = {a, b, c...}; | 将 c1 中的元素替换成列表中的元素（`array`不支持）|
| a.swap(b); | 交换 a 和 b 的元素，类型要相同，此操作通常比拷贝元素快得多|
| swap(a, b); | 与上面等价 |
| seq.assign(b, e) | 将 seq 中的元素替换为迭代器范围中的元素，迭代器不能指向 seq 的元素 |
| seq.assign(il) | 用初始化列表替换 |
| seq.assign(n, t) | 用 n 个 t 替换 |

由于右边运算对象的大小可能与左边不同，因此`array`不支持`assign`，也不运行用花括号包围的值列表赋值。`assign`不适用于关联容器。`assign`仅要求类型相容。

赋值相关操作会导致指向左边容器内部的迭代器、引用和指针失效，而`swap`操作不会导致失效（`array`和`string`除外），它们仍指向交换之前的那些元素。

除`array`外，`swap`不对任何元素进行拷贝、删除和插入操作，因此可以保证在常数时间完成，它只是交换了两个容器的内部数据结构。

`swap`两个`array`会真正交换它们的元素。在操作之后，指针、引用和迭代器所绑定的元素保持不变，但元素值已经和另一个`array`中对应元素的值进行了交换。

统一使用非成员版本的`swap`是一个好习惯。

### 容器大小操作

| 大小 | 意义 |
| :------------- | :------------- |
| c.size(); | c 中元素的数目，`forward_list`不支持 |
| c.max_size(); | c 可保存的最大元素数目 |
| c.empty(); | 判空 |

| 关系运算符 | 意义 |
| :------------- | :------------- |
| ==、!= | 所有容器都支持 |
| <、<=、>、>= | 无序关联容器不支持，类型相同，保存元素也要相同 |

### 添加元素

| 添加元素 | 意义 |
| :------------- | :------------- |
| c.push_back(t) | 在尾部创建值为 t 的元素，返回`void` |
| c.emplace_back(args) | 在尾部用参数构造元素，返回`void` |
| c.push_front(t) | 在头部创建值为 t 的元素，返回`void` |
| c.emplace_front(t) | 在头部用参数构造元素，返回`void` |
| c.insert(p, t) | 在迭代器 p 指向的元素之前创建值为 t 的元素，返回指向新添加元素迭代器 |
| c.emplace(p, args) | 在迭代器 p 指向的元素之前构造值为 t 的元素，返回指向新添加元素迭代器 |
| c.insert(p, b, e) | 在迭代器 p 指向的元素之前插入迭代器范围指定的元素，返回指向新添加的第一个元素的迭代器，若范围为空，返回 p |
| c.insert(p, n, t) | n 个 t |
| c.insert(p, il) | 列表 |

这些操作会改变容器大小，`array`不支持。

`forward_list`有自己版本的 insert 和 emplace。`forward_list`不支持 push_back 和 emplace_back。

`vector`和`string`不支持push_front 和 emplace_front。

`emplace`函数会在容器管理的内存空间中直接创建对象，而`push`函数会创建一个局部临时变量，并将其压入容器中。传递给`emplace`的参数必须与元素类型的构造函数相匹配。

### 访问元素

| 访问元素 | 意义 |
| :------------- | :------------- |
| c.back() | 返回尾元素引用。若 c 为空，行为未定义 |
| c.front() | 返回首元素引用。若 c 为空，行为未定义 |
| c[n] | 返回下标为 n 元素的引用，n 是一个无符号整数。若 n >= c.size()，行为未定义 |
| c.at(n) | 返回下标为 n 元素的引用，若 n 越界，抛出 out_of_range 异常 |

`at`和下标操作只适用于`string`、`vector`、`deque`和`array`。`back`不适用于`forward_list`。

### 删除元素

| 删除元素 | 意义 |
| :------------- | :------------- |
| c.pop_back() | 删除尾元素。若 c 为空，行为未定义。返回`void`|
| c.pop_front() | 删除首元素。若 c 为空，行为未定义。返回`void`|
| c.erase(p); | 删除迭代器所指元素，返回被删除元素之后元素的迭代器，若 p 为尾后迭代器，行为未定义 |
| c.erase(b, e); | 删除迭代器所指元素，返回最后一个被删除元素之后元素的迭代器，若 e 为尾后迭代器，函数返回尾后迭代器 |
| c.clear(); | 清空，返回`void` |

这些操作会改变容器大小，`array`不支持。

`forward_list`有自己版本的 erase。`forward_list`不支持 pop_back。

`vector`和`string`不支持pop_front。

删除元素的成员函数并不检查其参数。在删除元素前，程序员必须确保它们是存在的。

### 迭代器

| 迭代器 | 意义 |
| :------------- | :------------- |
| c.begin(), c.end() | 首尾迭代器 |
| c.cbegin(), c.cend() | 首尾常量迭代器 |

| 反向容器额外成员 | 意义 |
| :------------- | :------------- |
| reverse_iterator | 按逆序寻址元素的迭代器 |
| const_reverse_iterator | 按逆序寻址元素的常量迭代器 |
| c.rbegin(), c.rend() | 尾首迭代器 |
| c.crbegin(), c.crend() | 尾首常量迭代器 |

注：`forward_list`不支持

### 特殊的 forward_list 操作

为了理解`forward_list`为什么有特殊版本的添加和删除操作，考虑当我们从一个单向链表中删除一个元素时会发生什么。当添加或删除一个元素时，删除或添加的元素之前的那个元素的后继会发生变化。为了添加或删除一个元素，我们需要访问其前驱，以便改变前驱改变前驱的链接。但是，`forward_list`是单向链表。在一个单向链表中，没有简单的方法来获取一个元素的前驱，出于这个原因，在一个`forward_list`中添加或删除元素的操作是通过改变给定元素之后的元素来完成的。这样，我们总是可以访问到被添加或删除元素所影响的元素。

由于这些操作与其他容器上的操作有实现方式不同，`forward_list`并未定义`insert`、`emplace`和`erase`，而是定义了名为`insert_after`、`emplace_after`和`erase_after`的操作。为了支持这些操作，`forward_list`也定义了`before_begin`,它返回一个首前迭代器。这个迭代器允许我们在链表首元素之前并不存在的元素“之后”添加或删除元素（亦即在链表首元素之前添加删除元素）。

| 操作 | 意义 |
| :------------- | :------------- |
| lst.before_begin() | 返回指向链表首元素之前并不存在的元素的迭代器，此迭代器不能解引用 |
| lst.cbefore_begin()　| cbefore_begin() 返回一个 const_iterator |
| lst.insert_after(p, t) | 在迭代器 p 之后的位置插入元素 t，若 p 为尾后迭代器，则函数的行为未定义。若范围为空，返回 p |
| lst.insert_after(p, n, t) | 在迭代器 p 之后的位置插入 n 个 t|
| lst.insert_after(p, b, e) | 在迭代器 p 之后的位置插入迭代器范围表示的元素|
| lst.insert_after(p,il) | 在迭代器 p 之后的位置插入花括号列表|
| emplace_after(p,args)　|　使用 args 在 p 指定的位置之后构造一个元素，返回一个指向这个新元素的迭代器。若 p 为尾后迭代器，则函数的行为未定义 |
| lst.erase_after(p) | 删除 p 指向的位置之后的元素，返回一个指向被删除元素之后元素的迭代器，若不存在这样的元素，则返回尾后迭代器，如果 p 指向 lst 的尾元素或者是一个尾后迭代器，则函数的行为未定义 |
| lst.erase_after(b, e) | 删除从 b 之后直到（但不包含）e 之间的元素 |

### 改变容器大小

| 操作 | 含义 |
| :------------- | :------------- |
| c.resize(n) | 调整 c 的大小为 n 个元素。若 n < c.size()，多出的元素被丢弃。若必须添加新元素，则新元素采取值初始化 |
| c.resize(n, t) | 调整 c 的大小为 n 个元素。，多出的元素被丢弃。若必须添加新元素，则新元素初始化为 t |
| c.shrink_to_fit() | 请求将`capacity()`减小为与`size()`相同，具体的实现可能忽略此请求 |
| c.capacity() | 不重新分配内存的话，c 可以保存多少元素 |
| c.reserve(n) | 分配至少能容纳 n 个元素的内存空间 |

`shrink_to_fit()`只适用于`vector`、`string`和`deque`。

`capacity()`和`reserve(n)`只适用于`vector`和`string`。

## 迭代器失效

### 添加元素

`vector`或`string`：

- 存储空间重新分配：迭代器、指针、引用均失效
- 未重新分配：插入位置之前的有效，之后的失效

`deque`：

- 插入首尾之外：均失效
- 插入首尾：迭代器失效，指针、引用不失效

`list`或`forward_list`：都有效（包括尾后和首前）

### 删除元素

`list`或`forward_list`：都有效（包括尾后和首前）

`deque`：

- 删除首尾之外：均失效
- 删除首：首前失效，其他有效
- 删除尾：尾后失效，其他有效

`vector`或`string`：被删除元素之前的都有效

当我们删除元素时，尾后迭代器总是会失效（除了删除`deque`首元素外），所以不要保存`end`返回的迭代器。

## 额外的 string 操作

### 构造 string 的其他方法

| 方法 | 解释 |
| :------------- | :------------- |
| string s(cp, n) | s 是 cp 指向的数组中前 n 个字符的拷贝。此数组至少应该包含 n 个字符 |
| string s(s2, pos2) | s 是 string s2 从下标 pos2 开始的字符的拷贝。若 pos2 > s2.size()，行为未定义 |
|| string s(s2, pos2, len2) | s 是 string s2 从下标 pos2 开始 len2 个字符的拷贝。若 pos2 > s2.size()，行为未定义，抛出 out_of_range异常。不管 len2 值是多少，至多拷贝 s2.size()-pos2 个字符 |

这些构造函数接受一个`string`或`const char*`参数。从`const char*`拷贝时，指针指向的数组必须以空字符结尾，如果还传递了一个计数值，数组就不必以空字符结尾。

### substr 操作

`s.substr(pos, n)`返回一个`string`，包含 s 中从 pos 开始的 n 个字符的拷贝。pos 的默认值是0，n 的默认值是 s.size()-pos，即拷贝从 pos 开始的所有字符。如果开始位置超出`string`的大小，抛出 out_of_range 异常，不管 n 值为多少，最多拷贝到`string`的末尾。

### 其他修改 string 的操作

![修改 string 的操作]({static}/images/c++9-1.jpg)

![repalce 和 insert参数类型]({static}/images/c++9-2.jpg)

### string 搜索操作

`string`类提供了6个不同的搜索函数，每个函数有4个重载版本。每个搜索操作都返回`string::size_type`值，表示匹配发生的下标。如果搜索失败，则返回`string::npos`的`static`成员。标准库将`string::npos`定义成一个`const string::size_type`，并初始化为-1。由于 npos 是一个无符号数，此初始值意味着 npos 等于任何`string`最大的可能大小。

![string 搜索操作]({static}/images/c++9-3.jpg)

![string 搜索操作参数]({static}/images/c++9-4.jpg)

### compare 函数

![compare 函数]({static}/images/c++9-5.jpg)

### 数值转换

![string 数值转换]({static}/images/c++9-6.jpg)

```
string s2 = "pi = 3.14";
d = stod(s2.substr(s2.find_first_of("+-.0123456789")));
```

## 容器适配器

适配器（adaptors）是标准库中的一个通用概念，容器、迭代器和函数都有适配器。本质上，一个适配器是一种机制，能使某种事物的行为看起来像另外一种事物一样。一个容器适配器（Container adaptors）接受一种已有的容器类型，使其行为看起来像一种不同的类型。标准库定义了三个序列容器适配器：`stack`、`queue`和`priority_queue`。

### 所以适配器都支持的的操作和类型

| 名称 | 意义 |
| :------------- | :------------- |
| size_type | 一种类型，足以保存当前类型的最大对象的大小 |
| value_type | 元素类型 |
| container_type | 实现适配器的底层容器类型 |
| A a; | 创建一个名为 a 的空适配器 |
| A a(c); | 创建一个名为 a 的适配器，带有容器 c 的一个拷贝 |
| 关系运算符 | 每个适配器都支持所有关系运算符。这些关系运算符返回底层容器的比较结果 |
| a.empty() | 判空 |
| a.size() | 元素数目 |
| swap(a, b) | 交换，类型要相同，包括底层容器类型也必须相同 |
| a.swap(b) | 同上 |

### 定义适配器

- `stack`默认基于`deque`实现，要求`push_back`、`pop_back`和`back`操作，可使用除`array`和`forward_list`之外的任何容器构造

- `queue`默认基于`deque`实现，要求`back`、`push_back`、`front`、`push_front`操作，可使用`list`和`deque`构造

- `priority_queue`默认基于`vector`实现，要求`front`、`push_back`和`pop_back`操作，还需要随机访问能力，可使用`vector`和`deque`构造

两种构造方法：默认构造函数创建一个空对象；接受一个容器的构造函数拷贝该容器来初始化适配器。

```
//假设 deq 是一个 deque<int>
stack<int> stk(deq);    //从 deq 拷贝元素到 stk
```

我们可以在创建一个适配器时将一个命名的顺序容器作为第二个类型参数，来重载默认容器类型：

```
//在 vector 上实现的空栈
stack<string, vector<string>> str_stk;
//在 vector 上实现的空栈，初始化时保存 svec 的拷贝
stack<string, vector<string>> str_stk2（svec);
```

### 栈适配器

`stack`类型定义在同名头文件中。下面展示了如何使用：

```
stack<int> intStack;  //空栈
//填满栈
for (size_t ix = 0; ix != 10; ++ix)
    intStack.push(ix);  //栈保存0-9十个数
while (!intStack.empty()) { //栈中有值就继续循环
    int value = intStack.top();
    //使用栈顶值的代码
    intStack.pop(); //弹出栈顶元素，继续循环
}
```

| 操作 | 意义 |
| :------------- | :------------- |
| s.pop() | 删除栈顶元素，但不返回该元素值 |
| s.push(item) | 创建一个新元素压入栈顶，该元素通过拷贝或移动 item 而来 |
| s.emplace(args) | 构造一个新元素压入栈顶，该元素通过 args 构造 |
| s.top() | 返回栈顶元素，但不将元素弹出栈 |

每个容器适配器都基于底层容器类型的操作定义了自己的特殊操作，我们只能使用适配器操作，而不能使用底层容器类型的操作。

### 队列适配器

`queue`和`priority_queue`定义在头文件 queue 中。操作方法如下：

| 操作 | 意义 |
| :------------- | :------------- |
| q.pop() | 删除 queue 的首元素或 priority_queue 的最高优先级的元素，但不返回该元素 |
| q.front() | 返回首元素，但不删除此元素，只适用于 queue |
| q.back() | 返回尾元素，但不删除此元素，只适用于 queue |
| q.top() | 返回优先级最高的元素，但不删除该元素，只适用于 priority_queue |
|  q.push(item) | 在 queue 末尾或 priority_queue 中恰当的位置创建一个元素，其值为 item |
|  q.emplace(args) | 在 queue 末尾或 priority_queue 中恰当的位置由 args 参数构造一个元素 |
