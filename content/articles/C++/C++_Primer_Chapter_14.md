Title: C++ Primer 第十四章 重载运算与类型转换
Category: 读书笔记
Date: 2018-10-20 20:59:28
Modified: 2018-10-20 20:59:28
Tags: C++

[TOC]

## 14.1 基本概念

重载的运算符是具有特殊名字的函数：它们的名字由关键字`operator`和其后要定义的运算符号共同组成。和其他函数一样，重载的运算符也包含返回类型、参数列表以及函数体。

对一个运算符函数来说，它或者是类的成员，或者至少含有一个类类型的参数，这一约定意味着当运算符作用于内置类型的运算对象时，我们无法改变该运算符的含义：

```
//错误：不能为 int 重定义内置的运算符
int operator+(int, int);
```

我们只能重载已存在的运算符，而无权发明新的运算符。重载运算符无法改变优先级和结合律。

![运算符重载表]({filename}/images/c++14-1.jpg)

### 14.1.1 直接调用一个重载的运算符函数

```
//一个非成员运算符函数的等价调用
data1 + data2;	//普通的表达式
operator+(data1, data2);	//等价的函数调用

//一个成员运算符函数的等价调用
data1 +=data2;	//基于“调用”的表达式
data1.operator+(data2);	//等成员运算符函数的等价调用
```

### 14.1.2 选择作为成员或者非成员

当定义重载的运算符时，必须首先决定是将其声明为类的成员函数还是声明为一个普通的非成员函数。在某些时候我们别无选择，因为有的运算符必须作为成员；另一个情况下，运算符作为普通函数比作为成员更好。下面的准则有助于选择：

- 赋值(=)、下标([ ])、调用( () )和成员访问箭头(->)运算符必须是成员
- 复合赋值运算符一般来说应该是成员，但并非必须，这一点与赋值运算符略有不同
- 改变对象状态的运算符或者与给定类型密切相关的运算符，如递增、递减和解引用运算符，通常应该是成员
- 具有对称性的运算符可能转换任意一端的运算对象，例如算术、相等性、关系和位运算符等，因此它们通常应该是普通的非成员函数

## 14.2 输入和输出运算符

### 14.2.1 重载输出运算符 <<

通常，输出运算符的第一个形参是一个非常量`ostream`对象的引用。之所以`ostream`是非常量是因为向流写入内容会改变其状态；而该形参是引用是因为我们无法直接复制一个`ostream`对象。

第二个形参一般来说是一个常量的引用，该常量是我们想要打印的类类型。第二个形参是引用的原因是我们希望避免复制实参；而之所以该形参可以是常量是因为(通常情况下)打印对象不会改变对象的内容。

为了与其他输出运算符保持一致，`operator<<`一般要返回它的`ostream`形参。

Sales_data的输出运算符：

```
ostream &operat<< (ostream &os, const Sales_data &item)
{
	os << item.isbn() << " " << item.units_sold << " "
		<< item.revenue << " " << item.avg_price();
	return os;
}
```

输出运算符尽量减少格式化操作通常，输出运算符应该主要负责打印对象的内容而非控制格式，输出运算符不应该打印换行符。

输入输出运算符必须是非成员函数：与`iostream`标准库兼容的输入输出运算符必须是普通的非成员函数，而不能是类的成员函数。否则，它们的左侧运算对象将是我们的类的一个对象：

```
Sales_data data;
data << cout;    //如果 operator<< 是 Sales_data 的成员
```

假设输入输出运算符是某个类的成员，则它们也必须是`istream`或`ostream`的成员。然而，这两个类属于标准库，并且我们无法给标准库中的类添加任何成员。因此，我们必须将其定义成非成员函数。当然，`IO`运算符通常需要读写类的非公有数据成员，所以`IO`运算符一般被声明为友元。

### 14.2.2 重载输入运算符 >>

通常，输入运算符的第一个形参是运算符将要读取的流的引用，第二个形参是将要读入到的(非常量)对象的引用。该运算符通常会返回某个给定流的引用。第二个形参之所以是个非常量是因为输入运算符的目的就是将数据读入到这个对象中。

Sales_data的输入运算符：

```
istream &operator>>(istream &is, Sales_data &item)
{
	double price;	//不需要初始化，因为我们将先读入数据到 price，之后才使用它
	is >> item.bookNo >> item.units_sold >> price;
	if (is)	//检查输入是否成功
		item.revenue = item.units_sold * price;
	else
		item = Sales_data();	//输入失败：对象被赋予默认的状态
	return is;
}
```

输入运算符必须处理输入可能失败的情况，而输出运算符不需要。当读取操作发生错误时，输入运算符应该负责从错误中恢复。

## 14.3 算术和关系运算符

通常情况下，我们将算术和关系运算符定义成非成员函数以允许对左侧或右侧的运算对象进行转换。因为这些运算符一般不需要改变运算对象的状态，所以形参都是常量的引用。

```
Sales_data operator+(const Sales_data &lhs, const Sales_data &rhs)
{
	Sales_data sum = lhs;	//把lhs的数据成员拷贝给sum
	sum += rhs;	//将rhs加到sum中
	return sum;
}
```

如果类同时定义了算术运算符和相关的复合赋值运算符，则通常情况下应该使用复合赋值来实现算术运算符。

### 14.3.1 相等运算符

```
bool operator==(const Sales_data &lhs,const Sales_data &rhs)
{
	return lhs.isbn() == rhs.isbn() &&
			lhs.units_sold == rhs.units_sold &&
			lhs.revenue == rhs.revenue;
}
bool operator!=(const Sales_data &lhs, const Sales_data &rhs)
{
	return !(lhs == rhs);
}
```

如果某个类在逻辑上有相等性的含义，则该类应该定义`operator==`，这样做可以使得用户更容易使用标准库算法来处理这个类。

### 14.3.2 关系运算符

定义了相等运算符的类也常常(但不总是)包含关系运算符。特别是，因为关联容器和一些算法要用到小于运算符，所以定义`operator<`会比较有用。

## 14.4 赋值运算符

我们可以重载赋值运算符。不论形参 的类型是什么，赋值运算符都必须定义为成员函数。

### 14.4.1 复合赋值运算符

复合赋值运算符不非得是类的成员，不过我们还是倾向于把包括复合赋值在内的所有赋值运算都定义在类的内部。

```
//作为成员的二元运算符：左侧运算对象绑定到隐式地 this 指针
//假定两个对象表示的是同一本书
Sales_data& Sales_data::operator+=(const Sales_data &rhs)
{
	units_sold += rhs.units_sold;
	revenue += rhs.revenue;
	return *this;
}
```

这两类运算符都应该返回左侧运算对象的引用。

## 14.5 下标运算符

表示容器的类通常可以通过元素在容器中的位置访问元素，这些类一般会定义下标运算符`operator[]`。下标运算符必须是成员函数。

为了与下标的原始定义兼容，下标运算符通常以所访问元素的引用作为返回值，这样做的好处是下标可以出现在赋值运算符的任意一端。

如果一个类包含下标运算符，则它通常会定义两个版本：一个返回普通引用，另一个是类的常量成员并且返回常量引用。

## 14.6 递增和递减运算符

C++ 语言并不要求递增和递减运算符必须的类的成员，但是因为它们改变的正好是所操作对象的状态，所以建议将其设定为成员函数。

定义递增和递减运算符的应该同时定义前置后后置版本。这些运算符通常应该被定义成类的成员。

### 14.6.1 定义前置递增/递减运算符

```
class StrBlobPtr{
public:
	//递增和递减运算符
	StrBlobPtr& operator++();	//前置运算符
	StrBlobPtr& operator--();
	//其他成员和之前版本一致
};

//前置版本：返回递增/递减对象的引用
StrBlobPtr& StrBlobPtr::operator++()
{
	//如果curr已经指向了容器的尾后位置，则无法递增它
	check(curr, "increment past end of StrBlobPtr");
	++curr;	//将curr在当前状态下向前移动一个元素
	return *this;
}
StrBlobPtr& StrBlobPtr::operator--()
{
	//如果curr是0，则继续递减它将产生一个无效下标
	--curr;	//将curr在当前状态下向后移动一个元素
	check(curr, "decrement past begin of StrBlobPtr");
	return *this;
}
```

### 14.6.2 区分前置和后置运算符

后置版本接受一个额外的(不使用)`int`类型的形参。这个形参的唯一作用就是区分前置版本和后置版本的函数，而不是真的要在实现后置版本时参与运算。

```
class StrBlobPtr{
public:
	//递增和递减运算符
	StrBlobPtr operator++(int);	//后置运算符
	StrBlobPtr operator--(int);
	//其他成员和之前版本一致
};

//后置版本：递增/递减对象的值但是返回原值
StrBlobPtr StrBlobPtr::operator++(int)
{
	//此处无须检查有效性，调用前置递增运算时才需要检查
	StrBlobPtr ret = *this;	//记录当前的值
	++*this;	//向前移动一个元素，前置++需要检查递增的有效性
	return ret;	//返回之前记录的状态
}
StrBlobPtr StrBlobPtr::operator--(int)
{
	//此处无须检查有效性，调用前置递减运算时才需要检查
	StrBlobPtr ret = *this;	//记录当前值
	--*this;	//向后移动一个元素，前置--需要检查递减的有效性
	return ret;	//返回之前记录的状态
}
```

### 14.6.3 显示地调用后置运算符

如果我们想通过函数调用的方式调用后置版本，则必须为它的整型参数传递一个值：

```
StrBlobPtr p(a1);	//p 指向 a1 中的 vector
p.operator++(0);	//调用后置版本的 operator++
p.operator++();		//调用前置版本的 operator++
```

## 14.7 成员访问运算符

```
class StrBlobPtr{
public:
	std::string& operator*() const
	{
		auto p = check(curr, "dereference past end");
		return (*p)[curr];	//(*p)是对象所指的 vector
	}
	std::string* operator->() const
	{
		//将实际工作委托给解引用运算符
		return & this->opreator*();
	}
	//其他成员与之前的版本一致
};
```

解引用运算符首先检测 curr 是否仍在作用范围内，如果是，则返回 curr 所指元素的一个引用。箭头运算符不执行任何自己的操作，而是调用解引用运算符并返回解引用结果元素的地址。

箭头运算符必须是类的成员，解引用运算符通常也是类的成员，尽管并非必须如此。

值得注意的是，我们将这两个运算符定义成了`const`成员，这是因为与递增和递减运算符不一样，获取一个元素并不会改变 StrBlobPtr 对象的状态。

## 14.8 函数调用运算符

如果类重载了函数调用运算符，则我们可以像使用函数一样使用该类的对象。

举个🌰 ，下面这个名为 absInt 的`struct`含有一个调用运算符，该运算符负责返回其参数的绝对值：

```
struct absInt{
	int operator()(int val) const{
		return val > 0 ? val:-val;
	}
};
```

我们使用调用运算符的方式是令一个 absInt 对象作用于一个实参列表，这一过程看起来非常像调用函数的过程：

```
int i = -42;
absInt absObj;	//含有函数调用运算符的对象
int ui = absObj(i);	//将 i 传递给 absObj.operator()
```

函数调用运算符必须是成员函数。一个类可以定义多个不同版本的调用运算符，相互之间应该在参数数量或类型上有所区别。
如果定义了调用运算符，则该类的对象称为函数对象（function object）。

### 14.8.1 含有状态的函数对象类

和其他类一样，函数对象除了`operator()`之外也可以包含其他成员。函数对象类通常含有一些数据成员，这些成员被用于定制调用运算符中的操作。

```
class PrintString{
public:
	PrintString (ostream &o = cout, char c = ' '):os(o), sep(c){}
void operator()(const string &s) const {os << s << sep;}
private:
	ostream &os;	//用于写入的目的流
	char sep;	//用于将不同输出隔开的字符
};
```

当定义 PrintString 的对象时，对于分隔符及输出流即可以使用默认值也可以提供自己的值：

```
PrintString printer;	//使用默认值，打印到 cout
printer(s);	//在 cout 中打印 s，后面跟一个空格
PrintString errors(cerr, '\n');
errors(s);	//在 cerr 中打印 s，后面跟一个换行符
```

函数对象常常作为泛型算法的实参：

```
//例如可以使用标准库 for_each 算法和我自己的 PrintString 类来打印容器内容
for_each(vs.begin(), vs.end(), PrintString(cerr, '\n'));
```

### 14.8.2 lambda 是函数对象

当我们编写了一个`lambda`后，编译器将该表达式翻译成一个未命名类的未命名对象。在`lambda`表达式产生的类中含有一个重载的函数调用运算符。

```
stable_sort(words.begin(), words.end(),
			[](const string &a, const &b)
			{return a.size() < b.size();});
//其行为类似于下面这个类的一个未命名对象
class ShorterString {
public:
	bool operator()(const string &s1, const string &s2) const
	{return s1.size() < s2.size();}
};
```

产生的类只有一个函数调用运算符成员它负责接受两个`string`并比较他们的长度，它的形参列表和函数体与lambda表达式完全一样。

默认情况下`lambda`不能改变它捕获的变量。因此在默认情况下，由`lambda`产生的类当中的函数调用运算符是一个`const`成员函数。如果`lambda`被声明为可变的，则调用运算符就不是`const`的了。

#### 表示 lambda 及相应捕获行为的类

当一个`lambda`表达式通过引用捕获变量时，将有程序负责确保`lambda`执行时引用所引的对象确实存在。因此编译器可以直接使用该引用而无须在`lambda`产生的类中将其存储为数据成员。

相反，通过值捕获的变量被拷贝到`lambda`中。因此，这种`lambda`产生的类必须为每个值捕获的变量建立对应的数据成员，同时创建构造函数，令其使用捕获的变量的值来初始化数据成员。

`lambda`表达式产生的类不含默认构造函数、赋值构造函数及默认析构函数，它是否含有默认的拷贝/移动构造函数则通常要视捕获的数据成员类型而定。

### 14.8.3 标准库定义的函数对象

下表所列的类型定义在`functional`头文件中：

![标准库定义的函数对象]({filename}/images/c++14-2.jpg)

#### 在算法中使用标准库函数对象

在默认情况下排序算法使用`operator<`将序列按照升序排列。如果要执行降序排列的话，我们可以传入一个`greater`类型的对象。例如：

```
//svec 是一个 vector<string>
//传入一个临时的函数对象用于执行两个 string 对象的 > 比较运算
sort(svec.begin(), svec.end(), greater<string>());
```

则上面的语句将按照降序对 svec 进行排序。第三个实参是`greater<string>`类型的一个未命名的对象。

需要特别注意的是，标准库规定其函数对象对于指针同样适用。我们之前曾介绍过比较两个无关指针将产生未定义的行为，然而我们可能会希望通过比较指针的内存地址来`sort`指针的`vector`。直接这么做会产生未定义的行为，但是我们可以用标准库函数对象来实现：

```
vector<string *> nameTable;
sort(nameTable.begin(), nameTable.end(), [] (string *a, sting *b { return a < b; }));   //错误
sort(nameTable.begin(), nameTable.end(), less<string *>()); //正确
```

### 14.8.4 可调用对象和 function

C++ 语言中的几种可调用对象：

- 函数
- 函数指针
- lambda 表达式
- bind 创建的对象
- 重载了函数调用运算符的类

与其他对象一样，可调用的对象也有类型。例如，每个`lambda`有它自己唯一的（未命名）的类型；函数及函数指针的类型则由其返回值类型和实参类型决定。

调用形式：指明了调用返回的类型以及传递给调用的实参类型。

### 14.8.5 不同类型可能具有相同的调用形式

```
//普通函数
int add(int i, int j) { return i + j; }
//lambda，其产生一个未命名的函数对象类
auto mod = [] (int i, int j) { return i % j; }
//函数对象类
struct divide{
    int operator()(int denominator, int divisor){
        return denominator / divisor;
    }
}
```

上面的类型共享同一个调用形式：`int(int, int)`。

若我们想把它们存入同一个函数表：

```
map<string, int(*)(int, int)> binops;
binops.insert({"+", add});  //正确，add 是一个指向正确类型函数的指针
binops.insert({"%",mod});   //错误，mod 不是一个函数指针
```

### 14.8.6 标准库 function 类型

我们可以使用一个名为`function`的新标准库类型解决上述问题，它定义在`functional`头文件中，支持的操作如下：

![标准库function类型]({filename}/images/c++14-3.jpg)

```
map<string, function<int(int, int)>> binops = {
    {"+", add}, //函数指针
    {"-", std::minus<int>()},   //标准库函数对象
    {"/", divide()},    //未命名的 lambda
    {"*", [] (int i, int j) { return i * j; }}, //命名了的 lambda
    {"%", mod}};    //
```

#### 重载的函数与 function

我们不能（直接）将重载函数的名字存入`function`类型的对象中：

```
int add(int i, int j) { return i + j; }
Sales_data add(const Sales_data&, const Sales_data&);
map<string, function<int(int, int)>> binops;
binops.insert({"+", add});  //错误，哪个 add？
```

解决上述二义性问题的一条途径是存储函数指针而非函数名字：

```
int (*fp)(int, int) = add;
binops.insert({"+",fp});
```

同样，也可以使用`lambda`来消除二义性：

```
binops.insert({"+", [] (int i, int j) { return add(i, j); }});
```

## 14.9 重载、类型转换与运算符

### 14.9.1 类型转换运算符

类型转换运算符（conversion operator）是类的一种特殊成员函数，它负责将一个类类型的值转换成其他类型。一般形式：

```
operator type() const;
```

其中type表示某种类型。


我们不允许转换成数组或函数类型，但允许转换成指针(包括数组指针及函数指针)或引用类型。

类型转换运算符既没有显示的返回类型，也没有形参，而且必须定义成类的成员函数。类型转换运算符通常不应该改变待转换对象的内容，因此，类型转换运算符一般被定义成`const`成员。

#### 14.9.1.1 定义含有类型转换符的类

```
class SmallInt {
public:
	SmallInt(int i = 0): val(i)
	{
		if (i < 0 || i > 255)
			throw std::out_of_range("Bad SmallInt value");
	}
	operator int() const { return val; }
private:
	std::size_t val;
};
```

SmallInt 类既定义了向类类型的转换，也定义了从类类型向其他类型的转换。其中构造函数将算符类型的值转换成 SmallInt 对象，而类型转换运算符将 SmallInt 对象转换成`int`:

```
SmallInt si;
si = 4;    //首先将4隐式地转换成 SmallInt，然后调用 SmallInt::operator=
si + 3;    //首先将 si 隐式地转换成 int，然后执行整数的加法
```

尽管编译器一次只能执行一个用户定义的类型转换，但是隐式的用户定义类型转换可以置于一个标准（内置）类型转换之前或之后：

```
//内置类型转换将 double 实参转换为 int
SmallInt si = 3.14; //调用 SmallInt(int) 构造函数
//SmallInt 的类型转换运算符将 si 转换为 int
si + 3.14;  //内置类型转换将所得的 int 继续转换成 double
```

#### 14.9.1.2 类型转换运算符可能产生意外结果

在实践中，类很少提供类型转换运算符。在大多数情况下，如果类型转换自动发生，用户可能会感到比较意外，而不是感到受到了帮助。然而这条经验法则存在一种例外情况：对于类来说，定义向`bool`的类型转换还是比较普遍的现象。

在 C++ 标准的早期版本中，如果类想定义一个向`bool`的类型转换，则它常常遇到一个问题：因为`bool`是一种算术类型，所以类类型的对象转换成`bool`后就能被用在任何需要算术类型的上下文中。这样的类型转换可能引发意想不到的结果，特别是当`istream`含有向`bool`的类型转换时，下面的代码仍能编译通过：

```
int i = 42;
cin << i;
```

该程序试图将输出运算符作用在输入流。因为`istream`本身没有定义`<<`，所以本来这段代码应该产生错误。然而，该代码能使用`istream`的`bool`类型转换运算符将`cin`转换成`bool`，而这个`bool`值会接着被提升成`int`并用作内置的左移运算符的左侧运算对象。这样一来，提升后的`bool`值（1或0）最终会被左移42个位置。这一结果显然与我们的预期大相径庭。

#### 14.9.1.3 显示的类型转换运算符

为了防止这样的异常情况发生，C++ 11新标准引入了显示的类型转换运算符（explicit conversion operator）：

```
class SmallInt {
public:
	//编译器不会自动执行这一类型转换
	explicit operator int() const { return val; }
	//其他成员与之前的版本一致
};
```

和显示的构造函数一样，编译器(通常)也不会将一个显式的类型转换运算符用于隐式类型转换：

```
SmallInt si = 3;	//正确：SmallInt 的构造函数不是显式的
si + 3;	//错误：此处需要隐式的类型转换，但类的运算符是显式的
static_cast<int>(si) + 3;	//正确：显式地请求类型转换
```

该规定存在一个例外，即如果表达式被用作条件，则编译器会将显式地类型转换自动应用于它。换句话说，当表达式出现在下列位置时，显示的类型转换将被隐式地执行：

- `if`、`while`及`do`语句的条件部分
- `for`语句头的条件表达式
- 逻辑非运算符(`!`)、逻辑或(`||`)、逻辑与(`&&`)的运算对象
- 条件表达式(`? :`)的条件表达式

#### 14.9.1.4转换为 bool

在标准库的早期版本中，`IO`类型定义了向`void*`的转换规则，以避免上面提到的问题。但 C++ 11新标准通过显示的类型转换运算符实现同样的目的。
