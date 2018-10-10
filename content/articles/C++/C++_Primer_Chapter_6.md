Title: C++ Primer 第六章 函数
Category: 读书笔记
Date: 2018-10-09 15:55:08
Modified: 2018-10-09 15:55:08
Tags: C++

函数是一个命名了的代码块。

## 函数基础

为了与 C 语言兼容，可以使用关键字`void`表示函数没有形参。

函数的返回值不能是数组或者函数类型，但可以返回指向数组和函数的指针。

自动对象：只存在于块执行期间的对象。当块的执行结束后，块中创建的自动对象的值就变成未定义的了。

局部静态对象：在程序执行路径第一次经过对象定义语句时初始化，并且直到程序终止才销毁。如果没有显示初始化，则执行值初始化，内置类型的局部静态变量初始化为0。

## 参数传递

值传递和引用传递。

当某种类型不支持拷贝操作时，函数只能通过引用形参访问该类型的对象。如 IO 类型。

### const 形参和实参

如果函数无须改变引用形参的值，最好将其声明为常量引用。

此外，使用引用而非常量引用也会极大地限制函数所能接受的实参类型。例如，我们不能把`const`对象、字面值或者需要类型转换的对象传递给普通的引用形参，这种绝不像看起来那么简单，它可能造成出人意料的后果。考虑如下函数：

```
string::size_type find_char(string &s, char c, string::size_type &occurs);
```

则只能将 find_char 函数用于`string`对象。类似下面的调用将在编译时发生错误：

```
find_char("Hello World", 'o', ctr);
```

还有一个更难察觉的问题。假如其它函数（正确的）将它们的形参定义成常量引用，那么上述的 find_char 函数无法在此类函数中正常使用。例如

```
bool is_sentence(const string &s)
{
        string::size_type ctr = 0;
        return find_char(s, '.', ctr) == s.size() - 1 && ctr == 1;
}
```

正确的修改思路是改正 find_char 函数的形参。如果实在不能修改 find_char，就在 is_sentence 内部定义一个`string`类型的变量，令其为 s 的副本，然后把这个对象传递给 find_char。

用实参初始化形参时，会忽略顶层`const`。也就是说，当形参是顶层`const`时，传给它常量对象或者非常量对象都是可以的。

可以使用一个非常量初始化一个底层`const`对象，但反过来不行。

### 数组形参

数组的两个性质：不允许拷贝数组；使用数组时会将其转换成指针。

当我们为函数传递一个数组时，实际上传递的是指向数组首元素的指针。

尽管不能以值传递的方式传递数组，但是我们可以把形参写成类似数组的形式：

```
void print(const int*);
void print(const int[]);
void print(const int[10]);
```

尽管表现形式不同，但是上面的三个函数是等价的：每个函数的唯一形参都是`const int*`类型的。如果我们传给 print 函数的是一个数组，则实参自动的转换成指向数组首元素的指针，数组的大小对函数的调用没有影响。

因为数组是以指针的形式传递给函数的，所以一开始函数并不知道数组的确切尺寸，调用者应该为此提供一些额外的信息：

- 使用标记指定数组长度：让数组本身包含一个结束标记，例如 C 风格字符串
- 使用标准库规范，`begin()`和`end()`函数
- 显示传递一个表示数组大小的形参

当函数不需要对数组元素执行写操作的时候，数组形参应该是指向`const`的指针，注意下面的函数只能作用于大小为10的数组

```
void print(int (&arr)[10])
{
        for (auto elem : arr)
                cout << elem << endl;
}
```

### main：处理命令行选项

```
int main(int argc, char *argv[]) { ... }
```

第二个形参 argv 是一个数组，它的元素是指向 C 风格字符串的指针；第一个形参 argc 表示数组中字符串的数量。因为第二个形参是数组，所以 main 函数也可以定义成：

```
int main(int argc, char **argv) { ... }
```

当实参传给 main 函数之后，argv 的第一个元素指向程序的名字或者一个空字符串，接下来的元素依次传递命令行提供的实参，最后一个指针之后的元素值保证为0。

### 含有可变形参的函数

为了编写能够处理不同数量实参的函数，C++11 新标准提供了两种主要的方法：

- 如果所有实参类型相同，可以传递一个名为`initializer_list`的标准库类型
- 如果实参的类型不同，可以编写可变参数模板

C++ 还有一种特殊的形参类型（即省略号），可以用它传递可变数量的实参，不过需要注意的是，这种功能一般只用于与 C 函数交互的接口程序

#### initializer_list 形参

`initializer_list`类型定义在同名的头文件中。

`initializer_list`是一种类型模板，提供的操作如下：

`initializer_list <T> lst;`默认初始化；T 类型元素的空列表。

`initializer_list <T> lst{a,b,c...};`lst 的元素数量和初始值一样多；lst 的元素是对应初始值的副本；列表中的元素是 const。

`lst2(lst);`拷贝或赋值一个`initializer_list`对象不会拷贝列表中的元素；拷贝后，原始列表和副本共享元素。

`lst2 = lst;`等价于`lst2(lst)`。

`lst.size();`列表中的元素数量。

`lst.begin();`返回指向 lst 中首元素的指针。

`lst.end();`返回指向 lst 中尾元素下一位置的指针。

`initializer_list`和`vector`一样，也是类型模板，定义`initializer_list`对象时，必须说明列表中所含对象的类型。和`vector`不一样的是，`initializer_list`对象中的元素永远是常量值。

如果想向`initializer_list`形参中传递一个值的序列，则必须把序列放在一对花括号内：

```
//expected和actual是string对象
if (expected != actual)
        error_msg({"functionX", expected, actual});
else
        error_msg({"functionX", "okay"});
```

#### 省略符形参

省略符形参是为了便于 C++ 程序访问某些特殊的 C 代码而设置的，这些代码使用了名为 varargs 的 C 标准库功能。通常，省略符形参不应用于其他目的。你的 C 编译器文档会描述如何使用 varargs。

省略符形参只能出现在形参列表的最后一个位置，无外乎两种形式，在第一种形式中，形参声明后面的逗号是可选的：

```
void foo(parm_list,...);
void foo(...);
```

## 返回类型和 return 语句

返回`void`的函数不要求非得有`return`语句，以为这类函数的最后一句会隐式的执行`return`。

返回的值用于初始化调用点的一个临时量，该临时量就是函数调用的结果。

不要返回局部对象的引用或指针。

调用一个返回引用的函数得到左值，其他返回类型得到右值。

C++ 11新标准规定，函数可以返回花括号包围的值的列表，类似于其他返回结果，此处的列表也用来对表示函数返回的临时量进行初始化。如果列表为空，临时量执行值初始化。如果函数返回的是内置类型，则花括号包围的列表最多包含一个值，且该值所占空间不应该大于目标类型的空间。如果返回的是类类型，由类本身定义初始值如何使用。

如果控制语句到达了 main 函数的结尾处而且没有`return`语句，编译器会隐式的插入一条返回0的`return`语句。

cstdlib 头文件定义了两个预处理变量表示成功与失败：`EXIT_SUCCESS`，`EXIT_FAILURE`。

`int (*func(int i))[10];`func 是一个函数指针，指向：接受一个`int`参数，返回值是包含10个`int`数组的地址的函数。也可以利用尾置返回类型（C++ 11）写为：`auto func(int i) -> int(*)[10];`

还有一种情况，如果我们知道函数返回的指针将指向哪个数组，就可以使用`decltype`关键字声明返回类型。例如，下面的函数返回一个指针，该指针根据参数i的不同指向两个已知数组中的某一个：

```
int odd[] = {1, 3, 5, 7, 9};
int even[] = {0, 2, 4, 6, 8};
//返回一个指针，该指针指向含有5个整数的数组
decltype(odd) *arrPtr(int i)
{
        return (i % 2) ? &odd : &even;
}
```

arrPtr 使用关键字`decltype`表示它的返回类型是个指针，并且该指针所指的对象与 odd 的类型一致。因为 odd 是数组，所以 arrPtr 返回一个指向含有5个整数的数组的指针。有一个地方需要注意，`decltype`并不负责把数组类型转换成对应的指针，所以`decltype`的结果是个数组，要想表示 arrPtr 返回指针还必须在函数声明时加一个 \* 符号。

## 函数重载

### 顶层 const

顶层`const`不影响传入函数的对象。一个用于顶层`const`的形参无法和一个没有顶层`const`的形参区分开，无法重载：

```
Record lookup(Phone);
Record lookup(const Phone);
//
Record lookup(Phone*);
Record lookup(Phone* const);
```

### 底层 const

底层`const`可以实现重载。当我们传递一个非常量对象或者指向非常量对象的指针时，编译器会优先选用非常量的版本：

```
Record lookup(Account&);
Record lookup(const Account&);
//
Record lookup(Account*);
Record lookup(const Account*);
```

### const_cast和重载

```
//函数1
const string &shorterString(const string &s1, const strinf &s2)
{
        return s1.size() <= s2.size() ? s1 : s2;
}
//函数2
string &shorterString(string &s1, string &s2)
{
        auto &r = shorterString(const_cast<const string &>(s1),
                                const_cast<const string&>(s2));
        return const_cast<string&>(r);
}
```

函数1的参数和返回类型都是`const string`的引用。我们当然可以对两个非常量的`string`实参调用这个函数，但返回的结果仍然是`const string`的引用。

### 作用域与重载

编译器首先在当前作用域寻找函数，一旦找到，就会忽略掉外层作用域中的同名实体，剩下的工作就是检查函数调用是否有效了。

在C++语言中，名字查找发生在类型检查之前。

## 特殊用于语言特性

### 默认实参

一旦一个形参被赋予了默认值，它后面的所有形参都必须有默认值。

在给定的作用域中，一个形参只能被赋予一次默认实参。

局部变量不能作为默认实参。

用作函数实参的名字在函数声明所在的作用域内解析，而这些名字的求值过程发生在函数调用时：

```
sz wd = 80;
char def = '';
sz ht();
string screen(sz = ht(), sz = wd, char = def);

void f()
{
    def = '*';  //改变默认实参的值
    sz wd = 100;    //隐藏了外层定义的wd，但是没有改变默认值
    window = screen();  //调用 screen(ht(), 80, '*')
}
```

### 内联函数

以空间换时间。在函数返回类型前面加上关键字`inline`。内联说明只是向编译器发出一个请求，编译器可以选择忽略这个请求。

### constexpr 函数

能用于常量表达式的函数。函数的返回类型及所有的形参类型都得是字面值类型。函数体中必须有且只有一条`return`语句。

```
constexpr int new_sz() { return 42; }
constexpr int foo = new_sz();
```

编译器在程序编译时验证 new_sz 函数的返回类型。执行初始化任务时，编译器把对`constexpr`函数的调用替换成其结果值。为了能在编译过程中随时展开，`constexpr`函数被隐式指定为内联函数。

`constexpr`函数体内也可以包含其他语句，只要这些语句在运行时不执行任何操作就行，例如，空语句、类型别名及`using`声明。

`constexpr`函数不一定返回常量表达式，当把这类函数用在需要常量表达式的上下文中时，会出错。

把内联函数和`constexpr`函数放在头文件内。

和其它函数不一样，内联函数和`constexpr`函数可以在程序中多次定义，但是多个定义必须完全一致。

### 调试帮助

#### assert 预处理宏

所谓预处理宏其实是一个预处理变量，它的行为有点类似于内联函数。`assert`宏使用一个表达式作为它的条件：`assert(expr);`

首先对 expr 求值，如果表达式为假，`assert`输出信息并终止程序的执行。如果表达式为真，`assert`什么也不做。

`assert`定义在cassert头文件中，`assert`宏常用于检查“不能发生”的条件。

#### NDEBUG 预处理变量

`assert`的行为依赖于`NDEBUG`预处理变量的状态。如果定义了`NDEBUG`，`assert`什么都不做，默认情况下没有定义`NDEBUG`，`assert`将执行运行时检查。我们可以使用一个`#define`语句定义`NDEBUG`，从而关闭调试状态。同时，很多编译器都提供了一个命令行选项使我们可以定义预处理变量：

```
$ CC -D NDEBUG main.C #use /D with the Mocrosoft compiler.
```

除了使用`assert`外，也可以使用`NDEBUG`编写自己的条件调试代码。如果`NDEBUG`未定义，将执行`#ifndef`和`#endif`之间的代码；如果定义了`NDEBUG`，这些代码将被忽略掉。

编译器为每个函数都定义了`__func__`，它是一个`const char`局部静态数组，用于存放函数的名字，除了 C++ 编译器定义的`__func__`之外，预处理器还定义了另外4个对于程序调试很有用的名字：

- `__FILE__` 存放文件名的字符串字面值
- `__LINE__` 存放当前行号的整型字面值
- `__TIME__` 存放文件编译时间的字符串字面值
- `__DATE__` 存放文件编译日期的字符串字面值

## 函数匹配

候选函数：函数匹配的第一步是选定本次调用对应的重载函数集。

可行函数：形参数量与本次提供的实参数量相等（默认形参可以少于）；每个实参的类型与对应的形参相同，或者可以转换成形参的类型。

寻找最佳匹配（如果有的话）：该函数每个实参的匹配都不劣于其他可行函数需要的匹配；至少有一个实参的匹配优于其他可行函数提供的匹配。

如果没找到可行函数：编译器报告无匹配函数的错误；如果最佳匹配不唯一，编译器报告二义性错误。

## 函数指针

要声明一个函数指针，只需要用指针替换函数名：

```
bool (*pf)(const string &, const string &); //未初始化，pf 两端括号必不可少
```

当把函数名作为一个值使用时，该函数自动转换为指针，也就是说取地址符是可选的。同样，我们可以直接用函数指针调用函数，解引用符也是可选的。

不同类型的函数指针之前不存在转换规则。

函数指针没有指向任何一个函数：将函数指针赋为0或者 `nullptr`。

和数组类似，虽然不能定义函数类型的形参，但是可以定义指向函数的指针。此时，形参看起来是函数，实际上被当成指针使用：

```
//形参是函数类型，会自动转化为指向函数的指针
void test(bool pf(const string &, const string &));
//等价的定义
void test(bool (*pf)(const string &, const string &));
```

如果函数返回指向函数的指针，那么必须显示的将返回类型指定为指针。