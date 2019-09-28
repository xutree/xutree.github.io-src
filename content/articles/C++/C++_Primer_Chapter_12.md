Title: C++ Primer 第十二章 动态内存
Category: C++
Date: 2018-10-17 22:25:02
Modified: 2018-10-20 14:50:55
Tags: C++

[TOC]

一个由 C/C++ 编译的程序占用的内存分为以下几个部分：

- 栈区（stack）：由编译器自动分配释放，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈
- 堆区（heap）：一般由程序员分配释放，若程序员不释放，程序结束时可能由 OS 回收 。注意它与数据结构中的堆是两回事，分配方式倒是类似于链表
- 全局区（静态区）（static）：全局变量和静态变量的存储是放在一块的，初始化的全局变量和静态变量在一块区域，未初始化的全局变量、未初始化的静态变量在相邻的另一块区域。程序结束后由系统释放
- 文字常量区：常量字符串就是放在这里的。程序结束后由系统释放
- 程序代码区：存放函数体的二进制代码

## 12.1 动态内存与智能指针

在 C++ 中，动态内存的管理是通过一对运算符来完成的：`new`，在动态内存中为对象分配空间并返回一个指向该对象的指针，我们可以选择对对象进行初始化；`delete`，接受一个动态指针，销毁该对象，并释放与之关联的内存。

为了更容易地使用动态内存，新的标准提供了两种智能指针(smart pointer)类型来管理动态对象。`shared_ptr`允许多个指针指向同一个对象；`unique_ptr`则“独占”所指向的对象。标准库还定义了一个名为`weak_ptr`的伴随类，指向`shared_ptr`所管理的对象。这三种类型都定义在`memory`头文件中。

### 12.1.1 shared_ptr 类

类似`vector`智能指针也是模板：

```
shared_ptr<string> p1;	//shared_ptr，可以指向 string
shared_ptr<list<int>> p2;	//shared_ptr,可以指向 int 的 list
```

当我们创建`shared_ptr`时，可以传递一个（可选的）指向删除器函数的参数。

智能指针操作：

![智能指针操作]({filename}/images/c++12-1.jpg)

#### 12.1.1.1 make_shared 函数

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

当然，我们通常用`auto`定义一个对象来保存`make_shared`的结果，这种方式简单：

```
//p6 指向一个动态分配的空 vector<string>
auto p6 = make_shared<vector<string>>();
```

#### 12.1.1.2 shared_ptr 的拷贝和赋值

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

### 12.1.2 直接管理内存

C++ 语言定义了两个运算符来分配和释放动态内存。运算符`new`分配内存，`delete`释放`new`分配的内存。相对于智能指针，使用这两个运算符管理内存非常容易出错。

#### 12.1.2.1 使用 new 动态分配和初始化对象

在自由空间分配的内存是无名的，因此`new`无法为其分配的对象命名，而是返回一个指向该对象的指针：

```
int *pi = new int;    //pi 指向一个动态分配的、未初始化的无名对象
```

默认情况下，动态分配的对象是默认初始化的，这意味着内置类型或组合类型的对象的值将是未定义的，而类类型对象将用默认构造函数进行初始化：

```
string *ps = new string;	//初始化为空 string
int *pi = new int;	//pi 指向一个未初始化的 int

//可以使用直接初始化方式来初始化一个动态分配的对象
int *pi = new int(1024);	//pi 指向的对象的值为1024
string *ps = new string(10,'9');	//*ps 为“999999999”
//vector 有10个元素，值依次从0到9
vector<int> *pv = new vector<int>{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
```

也可以对动态分配的对象进行值初始化，只需在类型名之后跟一对空括号即可：

```
string *ps1 = new string;	//默认初始化为空 string
string *ps = new string();	//值初始化为空 string
int *pi1 = new int;		//默认初始化；*pi1 的值未定义
int *pi2 = new int();		//值初始化为0；*pi2 为0
```

如果我们提供了一个括号包围的初始化器，就可以用`auto`从此初始化器推断我们想要分配的对象的类型。但是由于编译器要用初始化器类型来推断分配的类型，只有当括号中仅有单一初始化器时才可以使用`auto`（这也意味着不能用`auto`动态分配数组）。

#### 12.1.2.2 动态分配的 const 对象

```
//分配并初始化一个 const int
const int *pci = new const int(1024);
//分配并默认初始化一个 const 的空 string
const string *pcs =new const string;
```

类似其他任何`const`对象，一个动态分配的`const`对象必须进行初始化。对于一个定义了默认构造函数的类类型，其`const`动态对象可以隐式初始化，而其他类型的对象就必须显式初始化。由于分配的对象是`const`的，`new`返回的指针是一个指向`const`的指针。

#### 12.1.2.3 内存耗尽

默认情况下，如果`new`不能分配所要求的内存空间，它会抛出一个类型为`bad_alloc`的异常。我们可以改变使用`new`的方式来阻止它抛出异常：

```
//若果分配失败，new返回一个空指针
int *p1 = new int;	//如果分配失败，new 抛出std::bad_alloc
int *p2 = new (nothrow) int;	//如果分配失败，new 返回一个空指针
```

我们称这种形式的`new`为定位`new`，`bad_alloc`和`nothrow`都定义在`new`头文件中。

#### 12.1.2.4 释放动态内存

为了防止内存耗尽，在动态内存使用完毕后，必须将其归还给系统。我们通过`delete`表达式(delete expression)来将动态内存归还给系统。

与`new`类似，`delete`表达式也执行两个动作：销毁给定的指针指向的对象；释放对应的内存。在`delete`之后，指针就变成了人们所说的空悬指针，即指向一块曾经保存数据对象但现在已经无效的内存的指针。如果需要保留指针，可以在`delete`之后将`nullptr`赋予指针。

#### 12.1.2.5 使用 new 和 delete 管理动态内存存在的三个常见问题

忘记`delete`内存。忘记释放动态内存会导致人们常说的“内存泄露”问题，因为这种内存永远不可能归还给自由空间了。查找内存泄露错误是非常困难的。

使用已经释放掉的对象。通过在释放内存后将指针置为空，有时可以检测出这种错误。

同一块内存释放两次。当两个指针指向相同的动态分配对象时，可能发生这种错误。

### 12.1.3 shared_ptr 和 new 结合使用

如前所述，如果我们不初始化一个智能指针，他就会被初始化为一个空指针。如下表所示，我们还可以用`new`返回的指针来初始化智能指针：

![智能指针其他操作]({filename}/images/c++12-2.jpg)

![智能指针其他操作]({filename}/images/c++12-3.jpg)

```
shared_ptr<double> p1;	//shared_ptr 可以指向一个 double
shared_ptr<int> p2(new int (42));	//p2 指向一个值为42的 int
```

接受指针参数的智能指针构造函数是`explicit`的。因此，我们不能将一个内置指针隐式转换为一个智能指针，必须使用直接初始化形式来初始化一个智能指针：

```
shared_ptr<int> p1 = new int(1024);	//错误：必须使用直接初始化形式
shared_ptr<int> p2(new int (1024));	//正确：使用了直接初始化
```

出于相同的原因，一个返回`shared_ptr`的函数不能在其返回语句中隐式转换一个普通指针：

```
shared_ptr<int> clone(int p){
	return new int(p);	//错误：隐式转换为 shared_ptr<int>
}
//我们必须将 shared_ptr 显式绑定到一个想要返回的指针上：
shared_ptr<int> clone(int p){
	//正确：显式地用 int* 创建 shared_ptr<int>
	return shared_ptr<int>(new int(p));
}
```

默认情况下，一个用来初始化智能指针的普通指针必须指向动态内存，因为智能指针默认使用`delete`释放它所关联的对象。

不要混合使用普通指针和智能指针：

![不要混合使用普通指针和智能指针]({filename}/images/c++12-4.jpg)

也不要使用get初始化另一个智能指针或为智能指针赋值：

![不要使用get初始化另一个智能指针或为智能指针赋值]({filename}/images/c++12-5.jpg)

### 12.1.4 unique_ptr 指针

一个`unique_ptr`“拥有”它所指向的对象。与`shared_ptr`不同，某个时刻只能有一个`unique_ptr`指向一个给定对象。

与`shared_ptr`不同，没有类似`make_shared`的标准库函数返回一个`unique_ptr`。当我们定义一个`unique_ptr`时，需要将其绑定到一个`new`返回的指针上。类似`shared_ptr`，初始化`unique_ptr`必须采用直接初始化形式：

```
unique_ptr<double> p1;	//可以指向一个 double 的 unique_ptr
unique_ptr<int> p2(new int(42));	//p2 指向一个值为42的 int
```

由于一个`unique_ptr`拥有它指向的对象，因此`unique_ptr`不支持普通的拷贝或赋值操作：

```
unique_ptr<string> p1(new string("Stegosaurus");
unique_ptr<string> p2(p1);	//错误：unique_ptr 不支持拷贝
unique_ptr<string> p3;
p3 = p2;	//错误：unique_ptr 不支持赋值
```

`unique_ptr`特有的操作：

![unique_ptr特有的操作]({filename}/images/c++12-6.jpg)

虽然我不能拷贝或赋值`unique_ptr`，但可以通过调用`release`或`reset`将指针的所有权从一个（非`const`）`unique_ptr`转移给另一个`unique`：

```
//将所有权从 p1（指向 string Stegosaurus）转移给 p2
unique_ptr<string> p2(p1.release());	//release 将 p1 置为空
unique_ptr<string> p3(new string("Trex"));
//将所有权从 p3 转移给 p2
p2.reset(p3.release());	//reset 释放了 p2 原来指向的内存
```

调用`release`会切断`unique_ptr`和它原来管理的对象间的联系。`release`返回的指针通常被用来初始化另一个智能指针或给另一个智能指针赋值。

#### 12.1.4.1 传递 unique_ptr 参数和返回 unique_ptr

不能拷贝`unique_ptr`的规则有一个例外：我们可以拷贝或赋值一个将要被销毁的`unique_ptr`。最常见的例子是从函数返回一个`unique_ptr`：

```
unique_ptr<int> clone(int p){
	//正确：从int*创建一个unique_ptr<int>
	return unique_ptr<int>(new int(p));
}
//还可以返回一个局部对象的拷贝
unique_ptr<int> clone(int p){
	unique_ptr<int> ret(new int(p));
	//...
	return ret;
}
```

对于两段代码，编译器都知道要返回的对象将要销毁。在此情况下，编译器执行一种特殊的“拷贝”。

#### 12.1.4.2 向 unique_ptr 传递删除器

类似`shared_ptr`，`unique_ptr`默认情况下用`delete`释放它指向的对象。与`shared_ptr`一样，我们可以重载一个`unique_ptr`中默认的删除器。与重载关联容器的比较操作类似，我们必须在尖括号中`unique_ptr`指向类型之后提供删除器类型。在创建或`reset`一个这种`unique_ptr`类型对象时，必须提供一个指定类型的可调用对象（删除器）：

```
//p指向一个类型为 objT 的对象，并使用一个类型为 delT 的对象释放 objT 对象
//它会调用一个名为 fcn 的 delT 类型对象
unique_ptr<objT, delT> p(new objT,fcn);

//作为一个更具体的例子，我们将重写连接程序，用 unique_ptr 代替 shared_ptr
void f(destination &d /*其他需要的参数*/)
{
	connection c = connect(&d);	//打开连接
	//当 p 被销毁时，连接将会关闭
	unique_ptr<connection, decltype(end_connection)*>
		p(&c, end_connection);
	//使用连接
	//当 f 退出时，connection 会被正确关闭
}
```

### 12.1.5 weak_ptr

`weak_ptr`是一种不控制所指向对象生存期的智能指针，它指向由一个`shared_ptr`管理的对象。将一个`weak_ptr`绑定到一个`shared_ptr`不会改变`shared_ptr`的引用计数。

一旦最后一个指向对象的`shared_ptr`被销毁，对象就会被释放，即使有`weak_ptr`指向对象。

`weak_ptr`操作：

![weak_ptr操作]({filename}/images/c++12-7.jpg)

当创建一个`weak_ptr`时，要用一个`shared_ptr`来初始化它：

```
auto p = make_shared<int>(42);
weak_ptr<int> wp(p);	//wp 弱共享 p；p 的引用计数未改变
```

由于对象可能不存在，我们不能使用`weak_ptr`直接访问对象，而必须调用`lock`。此函数检查`weak_ptr`指向的对象是否存在。

## 12.2 动态数组

`new`和`delete`运算符一次分配/释放一个对象，但某些应用需要一次为很多对象分配内存的功能。为了支持这种需求，C++ 语言和标准库提供了两种一次分配一个对象数组的方法。C++ 语言定义了一种`new`表达式，可以分配并初始化一个对象数组。
标准库中包含一个名为`allocator`的类，允许我们将分配和初始化分离。使用`allocator`通常会提供更好的性能和更灵活的内存管理能力。

大多数应用应该使用标准库容器而不是动态分配的数组。使用容器更为简单、更不容易出现内存管理错误并且可能有更好的性能。

### 12.2.1 new 和数组

```
//调用 get_size 确定分配多少个 int
int *pia = new int[get_size];   //pia 指向第一个 int
//方括号中的大小必须是整型，但不必是常量
```

```
typedef int arrT[42];	//arrT 表示42个 int 的数组类型
int *p = new arrT;	//
```

#### 12.2.1.1 分配一个数组会得到一个元素类型的指针

虽然我们通常称`new T[]`分配的内存为“动态数组”，但这种叫法某种程度上有些误导。当用`new`分配一个数组时，我们并未得到一个数组类型的对象，而是得到一个数组元素类型的指针。

由于分配的内存并不是一个数组类型，因此不能对动态数组调用`begin`和`end`。这些函数使用数组维度来返回指向首元素和尾元素的指针。处于相同的原因，也不能用范围`for`语句来处理（所谓的）动态数组中的元素。

**要记住我们所说的动态数组并不是数组类型，这是很重要的。**

#### 12.2.1.2 初始化动态分配对象的数组

默认情况下，`new`分配的对象，不管是单个分配的还是数组中的，都是默认初始化的。可以对数组中的元素进行值初始化，方法是在大小之后跟一对空括号。

```
int *pia = new int[10];	//10个未初始化的 int
int *pia2 = new int[10]();	//10个值初始化为0的 int
string *psa = new string[10];	//10个空 string
string *psa2 = new string[10]();	//10个空 string
//在新标准中，我们还提供一个元素初始化器的花括号列表：
//10个 int 分别用列表中对应的初始化器初始化
int *pia3 = new int[10] {0,1,2,3,4,5,6,7,8,9};
//10个 string，前4个用给定的初始化器初始化，剩余的进行值初始化
string *psa3 = new string[10]{"a", "an", "the", string(3,'x')};
```

如果初始化器数目大于元素数目，则`new`表达式失败，不会分配任何内存，并抛出`bad_array_new_length`的异常，类似于`bad_alloc`，此类型定义在头文件`new`中。

#### 12.2.1.3 动态分配一个空数组是合法的

我们在使用`new`分配一个动态数组时，可以指定分配数组的大小为0，这样做是合法的：

```
char *pc = new char(0);
```

此时`new`返回一个与其他`new`表达式返回类型都不同的指针类型， 该指针不能解引用，就像一个数组的尾后迭代器一样。

#### 12.2.1.4 释放动态数组

为了释放动态数组，我们使用一种特殊形式的`delete`——在指针前加上一个空括号对：

```
delete p;    //p 必须指向一个动态分配的对象或为空
delete [] pa;  //pa 必须指向一个动态分配的数组或为空
```

第二条语句销毁 pa 指向的数组中的元素，并释放对应的内存。数组中的元素按逆序销毁，即，最后一个元素首先被销毁，然后是倒数第二个，以此类推。

当我们释放一个动态数组时，空方括号是必须的，它指示编译器此指针指向一个对象数组的第一个元素。 `delete`一个动态数组时未添加空方括号或`delete`一个普通指针时添加了空方括号，其行为都是未定义的。

前面我们讲到， 可以使用`typedef`来给动态数组起一个别名，这样在`new`一个动态数组时就不必添加方括号`[]`，即使这样，我们在释放一个动态数组时，仍然需要添加方括号`[]`，因为它本质上还是一个动态数组。

#### 12.2.1.5 智能指针和动态数组

`unique_ptr`智能指针有个可以管理`new`分配的动态数组的版本，为了使用一个`unique_ptr`来管理动态数组，需要在对象类型后加一个空方括号`[]`:

```
unique_ptr<int[]> up(new int[10]());
up.release(); // 自动调用 delete [] 销毁其指针
```

当一个`unique_ptr`指向一个数组时，我们不能使用点和箭头成员运算符，毕竟，`unique_ptr`指向的是一个数组而不是单个对象。不过，我们可以使用下表运算符来访问数组中的元素：

```

for (size_t i = 0; i < 10; ++i)
    up[i] = i;
```

`shared_ptr`不支持动态数组，如果希望使用`shared_ptr`管理一个动态数组，我们需要提供自己的删除器：

```
shared_ptr<int> sp(new int[10], [](int* p){ delete [] p; });
sp.reset();
```

我们在这个例子中使用`lambda`做为`shared_ptr`的删除器，如果我们不提供删除器，这样的行为是未定义的，因为默认情况下`shared_ptr`使用`delete`来释放内存，使用`delete`来释放一个动态数组的定位是未定义的。

`shared_ptr`不支持动态数组这一特性会影响我们访问数组中的元素：

```
for (size_t i = 0; i != 10; ++i)
    *(sp.get() + i) = i;
```

`shared_ptr`没有定义下标运算符，而且智能指针不支持指针算术运算。因此，为了访问数组中的元素，我们必须用`get`成员函数获取一个内置指针，然后使用该内置指针来访问数租元素。

### 12.2.2 allocator 类

标准库`allocator`类定义在头文件`memory`中。它帮助我们将内存分配和构造分离开来，它分配的内存是原始的、未构造的。

类似`vector`，`allocator`也是一个模板类，我们在定义一个`allocator`类类型的时候需要制定它要分配内存的类型，它会根据给定的对象类型来确定恰当的内存大小和对齐位置：

```
allocator<string> alloc;
auto const p = alloc.allocate(n); // 分配 n 个未初始化的 string
```

`allocator`类及其算法：

| 操作 | 意义 |
| :------------- | :------------- |
| allocator<T> a | 定义了一个名为 a 的 allocator 对象，可以为类型为 T 的对象分配内存 |
| a.allocate(n) | 分配一段原始的、未构造的内存，保存 n 个类型为 T 的对象 |
| a.deallocate(p, n) | 释放从 T* 指针 p 中地址开始的内存，这块内存保存了 n 个类型为 T 的对象；p 必须是一个先前由 allocate 成员函数返回的指针，且 n 必须是创建时候的大小，在调用 deallocate 之前，用户必须对每个在在这块内存中创建的对象调用 destroy 函数|
| a.construct(p, args) | p 必须是一个类型为 T* 的指针，指向一块原始内存，args 被传递给类型为 T 的构造函数 |
| a.destroy(p) | p 为 T* 类型的指针，此算法对 p 执行析构函数 |

#### 12.2.2.1 allocator 分配未构造的内存

```
auto q = p;	//q 指向最后构造的元素之后的位置
alloc.construct(q++);	//*q 为空字符串
alloc.construct(q++, 10, 'c');	//*q 为cccccccccc
alloc.construct(q++, "hi");	//*q 为hi
```

为了使用`allocate`返回的内存，我们必须用`construct`构造对象。使用未构造的内存，其行为是未定义的。

当我们用完对象后，必须对每个构造的元素调用`destroy`来销毁它们。函数`destroy`接受一个指针，对指向的对象执行析构函数：

```
while(q != p)
	alloc.destroy(--q);	//释放我们真正构造的 string
```

一旦元素被销毁后，就可以重新使用这部分内存来保存其他`string`，也可以将其归还给系统。释放内存通过调用`deallocate`来完成：

```
alloc.deallocate(p, n);
//传递给 deallocate 的指针不能为空，它必须指向由 allocate 分配的内存
//传递给 deallcoate 的大小参数必须与调用 allocate 分配内存时提供的大小参数具有一样的值
```

我们只能对真正构造了的元素进行`destroy`操作。

#### 12.2.2.2 拷贝和填充为初始化内存的算法

标准库为`allocator`类定义了两个伴随算法，可以在未初始化内存中创建对象：

| 操作 | 意义 |
| :------------- | :------------- |
| uninitialized_copy(b, e, b2) | 从迭代器 b 和 e 指出的输入范围中拷贝元素到迭代器 b2 指定的未构造的原始内存中，b2 指向的内存必须足够大，能容下输入序列中的元素的拷贝 |
| uninitialized_copy_n(b, n, b2) | 从迭代器 b 指向的元素开始，拷贝 n 个元素到 b2 开始的原始内存中 |
| uninitialized_fill(b, e, t) | 在迭代器 b 和 e 指定的原始内存范围中创建对象，值均为 t 的拷贝 |
| uninitialized_fill_n(b, n, t) | 从迭代器 b 指向的原始内存地址开始创建 n 个对象，b 必须指向足够大的未构造的原始内存，能容纳给定数量的对象 |

这些函数在给定目的位置创建元素，而不是由系统分配内存给他们。

```
vector<int> vec{0, 1, 2, 3, 4, 5};
auto p = alloc.allocate(vec.size() * 2);
auto q = uninitialized_copy(vec.begin(), vec.end(), p);
uninitialize_fill_n(q, vec.size(), 42);
```

`uninitialized_copy`在给定位置构造元素，函数返回递增后的目的位置迭代器。因此，一个`uninitialized_copy`调用会返回一个指针，指向 最后一个构造的元素之后的位置。
