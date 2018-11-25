Title: C++ Primer 第十七章 标准库特殊设施
Category: 读书笔记
Date: 2018-10-21 17:04:34
Modified: 2018-10-21 17:04:34
Tags: C++

[TOC]

## 17.1 tuple 类型

当我们希望将一些数据组合成单一对象，但又不想麻烦地定义一个新数据结构来表示这些数据时，可以使用`tuple`类型。与`pair`类似，但`tuple`可以有任意数量的成员。它的一个常见用途就是从一个函数返回多个值。`tuple`定义在同名的头文件中。

支持的操作：

![tuple支持的操作]({filename}/images/c++17-1.jpg)

要访问一个`tuple`的成员，使用`get`标准库模板。为了使用`get`，我们必须指定一个显式模板参数，它指明我们想要访问第几个成员。这个显式模板参数必须是一个整型常量表达式，从0开始计数，返回指定成员的引用。

```
auto book = get<0>(item);  // 返回 item 的第一个成员
get<0>(item) *= 0.8;       // 修改书的单价
```

借助辅助类模板`tuple_size`和`tuple_element`，可以查询`tuple`成员的数量和类型。不过使用这两个类，必须知道 `tuple`对象的类型，这可以通过`decltype`很简单地得到：

```
typedef decltype(item) trans;
// 返回 trans 类型对象中成员的数量
size_t sz = tuple_size<trans>::value;  // 返回 3
// cnt 的类型与 item 中第二个成员相同，是一个 int
tuple_element<1, trans>::type cnt = get<1>(item);
```

只有两个`tuple`具有相同数量的成员，且每对成员使用`==`或`<`是合法时，才能比较两个`tuple`。另外，由于`tuple`定义了`<`和`==`运算符，可以将`tuple`序列传递给算法，并且可以在无序容器中将`tuple`作为关键字类型。

## 17.2 bitset 类型

`bitset`类，可以方便地将整型运算对象当作二进制位集合处理，并且能够处理超过最长整型类型大小的位集合。`bitset`定义在同名的头文件中。

支持的操作：

![bitset支持的操作]({filename}/images/c++17-2.jpg)

**使用字符串初始化`bitset`时，下标最小的字符对应`bitset`中的高位。**

```
bitset<32> bitvec4("1100");   // 2、3两位为1，剩余位为0
```

![bitset支持的操作]({filename}/images/c++17-3.jpg)

## 17.3 正则表达式

RE 库定义在头文件`regex`中。

| 组件 | 意义 |
| :------------- | :------------- |
| regex | 表示有一个正则表达式的类 |
| regex_match | 将一个字符序列与一个正则表达式匹配，整串匹配返回`true` |
| regex_search | 寻找第一个与正则表达式匹配的子序列，有子串匹配，返回`true` |
| regex_replace | 使用给定格式替换一个正则表达式 |
| regex_iterator | 迭代器适配器，调用`regex_search`来遍历一个`string`中所有匹配的子串 |
| smatch | 容器类，保存`string`中搜索的结果 |
| ssub_match  | `string`中匹配的子表达式的结果 |

`regex_search`和`regex_search`的参数如下，这些操作都返回`bool`，指出是否找到匹配：

`(seq, m, r, mft)`或`(seq, r, mft)`：在字符序列 seq 中查找 regex 对象 r 中的正则表达式。seq 可以是一个`string`、表示范围的一对迭代器以及一个指向空字符结尾的字符数组的指针。m 是一个`match`对象，用来保存匹配结果的相关细节。m 和 seq 必须具有兼容的类型。mft 是一个可选的`regex_constants::match_flag_type`值，它们会影响匹配过程。

待续...
