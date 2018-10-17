Title: C++ Primer 第十二章 动态内存
Category: 读书笔记
Date: 2018-10-17 22:25:02
Modified: 2018-10-17 22:25:02
Tags: C++

一个由 C/C++ 编译的程序占用的内存分为以下几个部分：

- 栈区（stack）：由编译器自动分配释放，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈
- 堆区（heap）：一般由程序员分配释放，若程序员不释放，程序结束时可能由 OS 回收 。注意它与数据结构中的堆是两回事，分配方式倒是类似于链表
- 全局区（静态区）（static）：全局变量和静态变量的存储是放在一块的，初始化的全局变量和静态变量在一块区域，未初始化的全局变量、未初始化的静态变量在相邻的另一块区域。程序结束后由系统释放
- 文字常量区：常量字符串就是放在这里的。程序结束后由系统释放
- 程序代码区：存放函数体的二进制代码

## 动态内存与智能指针

在 C++ 中，动态内存的管理是通过一对运算符来完成的：`new`，在动态内存中为对象分配空间并返回一个指向该对象的指针，我们可以选择对对象进行初始化；`delete`，接受一个动态指针，销毁该对象，并释放与之关联的内存。

为了更容易地使用动态内存，新的标准提供了两种智能指针(smart pointer)类型来管理动态对象。`shared_ptr`允许多个指针指向同一个对象；`unique_ptr`则“独占”所指向的对象。标准库还定义了一个名为`weak_ptr`的伴随类，指向`shared_ptr`所管理的对象。这三种类型都定义在`memory`头文件中。

### shared_ptr 类

类似`vector`智能指针也是模板：

```
shared_ptr<string> p1;	//shared_ptr，可以指向 string
shared_ptr<list<int>> p2;	//shared_ptr,可以指向 int 的 list
```

智能指针操作：

![智能指针操作]({filename}/images/c++12-1.jpg)

#### make_shared 函数

最安全的分配和使用动态内存的方法是调用一个名为`make_shared`的标准库函数。此函数在动态内存中分配一个对象并初始化它，返回指向此对象的`shared_ptr`。与智能指针一样，`make_shared`也定义在`memory`头文件中。

```
//指向一个值为42的 int 的 shared_ptr
shared_ptr<int> p3 = make_shared<int>(42);
//p4 指向一个值为”999999999”的 string
shared_ptr<string> p4 = make_shared<string>(10,'9');
//p5 指向一个值初始化的 int，即，值为0
shared_ptr<int> p5 = make_shared<int>();
```

类似顺序容器的`emplace`成员，`make_shared`用其参数来构造给定类型的对象。例如，调用`make_shared<string>`时传递的参数必须与`string`的某个构造函数相匹配。

当然，我们通常用`aut`o定义一个对象来保存`make_shared`的结果，这种方式简单：

```
//p6 指向一个动态分配的空 vector<string>
auto p6 = make_shared<vector<string>>();
```

#### shared_ptr 的拷贝和赋值

当进行拷贝或赋值操作时，每个`shared_ptr`都会记录有多少个其他`shared_ptr`指向相同的对象。

我们可以认为每个`shared_ptr`都有一个关联的计数器，通常称其为引用计数(reference count)。无论何时我们拷贝一个`shared_ptr`，计数器都会递增；当我们给`shared_ptr`赋予一个新值或是`shared_ptr`被销毁时，计算器就会递减。
一旦一个`shared_ptr`的计数器变为0，它就会自动释放自己所管理的对象。

```
auto r = make_shared<int>(42);	//r 指向的 int 只有一个引用者
r = q;	//给 r 赋值，令它指向另一个地址
	//递增 q 指向的对象的引用计数
	//递减 r 原来指向对象的引用计数
	//r 原来指向的对象已没有引用者，会自动释放
```

`shared_ptr`自动销毁所管理的对象，还会自动释放相关联的内存。

如果你将`shared_ptr`存放于一个容器中，而后不再需要全部元素，要记得使用`erase`删除不需要的那些元素，否则`shared_ptr`在无用之后会仍然保留。
