Title: C++ Primer 第八章 IO 库
Category: 读书笔记
Date: 2018-10-09 22:19:51
Modified: 2018-10-09 22:19:51
Tags: C++

[TOC]

## 8.1 IO 类

`iostream`头文件：

`istream`,`wistream`,`ostream`,`wostream`,`iostream`,`wiostream`类型。

`fstream`头文件：

`ifstream`,`wifstream`,`ofstream`,`wofstream`,`fstream`,`wfstream`类型。

`sstream`头文件：

`istringstream`,`wistringstream`,`ostringstream`,`wostringstream`,`stringstream`,`wstringstream`类型。

宽字符版本的类型和函数的名字以一个“w”开始。

IO 对象无拷贝和赋值。进行 IO 操作的函数通常以引用方式传递和返回值。读写一个 IO 对象会改变其状态，因此传递和返回的引用不能是`const`的。

### 8.1.1 条件状态

下表中 *strm* 是一种 IO 类型：

| 状态 | 含义 |
| :------------- | :------------- |
| *strm*::iostate | iostate 是一种机器相关的类型，提供了表达条件状态的完整功能 |
| *strm*::badbit | 流已崩溃 |
| *strm*::failbit | IO 操作失败了 |
| *strm*::eofbit | 流到达了文件结束 |
| *strm*::goodbit | 流未处于错误状态，此值保证为0 |
| s.eof() | 若流 s 的 eofbit 置位，返回 true |
| s.fail() | 若流 s 的 failbit 或 badbit 置位，返回 true |
| s.bad() | 若流 s 的 badbit 置位，返回 true |
| s.good() | 若流 s 处于有效状态，返回 true |
| s.clear() | 将流 s 所以状态位复位，将流的状态设为有效，返回 void |
| s.clear(flags) | 根据 flags 复位，flags 类型为 *strm*::iostate，返回 void |
| s.setstate(flags) | 根据 flags 置位，flags 类型为 *strm*::iostate，返回 void |
| s.rdstate() | 返回流 s 的当前条件状态，返回值类型为 *strm*::iostate |

`badbit`表示系统级错误，如不可恢复的读写错误，一旦被置位，流就无法再使用了。

`failbit`表示可恢复的错误，例如期望读取数值却读到一个字符等错误。这种问题通常是可以修正的，流还可以继续使用。

如果到达文件结尾，`eofbit`和`failbit`都会被置位。

`goodbit`值为0，表示流未发生错误。

如果`badbit`、`failbit`和`eofbit`任一个被置位，则检测流状态的条件会失败。

`good()`函数在所有错误位均未置位的情况下返回`true`。

我们将流当做条件使用的代码等价于`!fail()`。

### 8.1.2 管理条件状态

```
// 记住 cin 的当前状态
auto old_state = cin.rdstate(); // 记住 cin 的当前状态
cin.clean();  // 使 cin 有效
process_input(cin); // 使用 cin
cin.setstate(old_state);  // 将 cin 置为原有状态
```

```
// 复位 failbit 和 badbit，保持其他标志位布标
cin.clear(cin.rdstate() & ~cin.failbit & ~cin.badbit);
```

### 8.1.3 管理输出缓冲

每个输出流都管理一个缓冲区，用来保存程序读写的数据。

导致缓冲刷新（即，数据真正写到输出设备或文件）的原因有很多：

- 程序正常结束，作为`main`函数的`return`操作的一部分，缓冲刷新被执行
- 缓冲区满
- 使用操纵符`endl`（插入换行）、`ends`（插入空字符）、`flush`（什么都不插入）显式刷新
- 在每个输出操作之后，可以用操纵符`unitbuf`设置流的内部状态，来情况缓冲区。默认情况下，对`cerr`是设置`unitbuf`的，因此`cerr`的内容都是立即刷新的
- 一个输出流可以关联到另一个流。当读写被关联的流时，关联到的流的缓冲区会被刷新。默认情况下，`cin`和`cerr`都关联到`cout`。因此读`cin`或者写`cerr`都会导致`cout`的缓冲区被刷新

### 8.1.4 unitbuf 操纵符

如果想在每次输出操作后都刷新缓冲区，可以使用`unitbuf`操纵符。它告诉流在接下来的每次写操作之后都执行一次`flush`刷新。`nounitbuf`操纵符则重置流，使其恢复使用正常的系统管理的缓冲区刷新机制：

```
cout << unitbuf;    // 所有输出操作后都会立即刷新缓冲区
// 任何输出都会立即刷新，无缓冲
cout << nounitbuf;    // 回到正常的缓冲方式
```

### 8.1.5 关联输入和输出流

`tie()`有两个重载的版本：

- 不带参数的版本返回指向输出流的指针。如果本对象当前关联到一个输出流，则返回的就是指向这个流的指针，如果对象未关联到流，则返回空指针
- 第二个版本接受一个指向`ostream`的指针，将自己关联到此`ostream`

每个流同时最多关联到一个流，但多个流可以同时关联到同一个`ostream`

## 8.2 文件输入输出

### 8.2.1 fstream 特有的操作

下表中的 *fstream* 是头文件 fstream 中定义的一个类型：

| 操作 | 含义 |
| :------------- | :------------- |
| *fstream* fstrm; | 创建一个未绑定的文件流 |
| *fstream* fstrm(s); | 创建一个 *fstream*，并打开名为 s 的文件。s 可以是 string 类型或者指向 C 风格字符串的指针。这些构造函数都是`explicit`的。默认的文件模式 mode 依赖于 *fstream* 的类型 |
| *fstream* fstrm(s, mode); | 按 mode 打开文件 |
| fstrm.open(s) | 打开名为 s 的文件并与 fstrm 绑定。s 可以是 string 类型或者指向 C 风格字符串的指针。默认的文件模式 mode 依赖于 *fstream* 的类型。返回`void` |
| fstrm.close() | 关闭与 fstrm 绑定的文件。返回`void` |
| fstrm.is_open() | 返回一个布尔值，指出与 fstrm 关联的文件是否打开成功且尚未关闭 |

如果调用`open()`失败，`failbit`会被置位，条件会为假：`if(open(file))`可用于判定。

对一个已经打开的文件流调用`open()`会失败，并且`failbit`会被置位。为了将文件流关联到另一个文件，必须先关闭已经关联的文件。

当一个`fstream`对象被销毁时，`close`会自动被调用。

### 8.2.2 文件模式

| 文件模式 | 意义 |
| :------------- | :------------- |
| in | 只读 |
| out | 只写（会清空已有数据） |
| app | 每次写操作前均定位到文件末尾|
| ate | 打开文件后立即定位到文件末尾|
| trunc | 截断文件|
| binary | 以二进制方式进行 IO|

`ifstream`默认`in`模式；`ofstream`默认`out`模式；`fstream`默认`in`和`out`模式打开。

## 8.3 string 流

### fstream 特有的操作

下表中的 *sstream* 是头文件 sstream 中定义的一个类型：

| 操作 | 含义 |
| :------------- | :------------- |
| *sstream* strm; | 创建一个未绑定的 stringstream 对象|
| *sstream* strm(s); | strm 是一个 sstream 对象，保存 string s 的一个拷贝。此构造函数时`explicit`的|
| strm.str() | 返回 strm 所保存的 string 的拷贝 |
| strm.str(s)| 将 string s 拷贝到 strm 中，返回 void|
