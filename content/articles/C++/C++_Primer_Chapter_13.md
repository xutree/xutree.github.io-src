Title: C++ Primer 第十三章 拷贝控制
Category: C++
Date: 2018-10-20 16:41:10
Modified: 2018-10-20 19:14:52
Tags: C++

[TOC]

当定义一个类时，我们显示地或隐式地指定在此类型的对象拷贝、移动、赋值和销毁时做什么。一个类通过定义五种特殊的成员函数来控制这些操作，包括：拷贝构造函数（copy constructor）、拷贝赋值运算符（copy-assignment operator）、移动构造函数（move constructor）、移动赋值运算符（move-assignment operator）和析构函数（destructor）。

拷贝和移动构造函数定义了当用同类型的另一个对象初始化本对象时做什么。

拷贝和移动赋值运算符定义了将一个对象赋予同类型的另一个对象时做什么。

析构函数定义了当此类型对象销毁时做什么。

我们称这些操作为拷贝控制操作（copy control）。

## 13.1 拷贝、赋值和销毁

### 13.1.1 拷贝构造函数

如果一个构造函数的第一个参数是自身类类型的引用，且任何额外参数都有默认值，则此构造函数是拷贝构造函数。

```
class Foo{
public:
	Foo();	//默认构造函数
	Foo(const Foo&);	//拷贝构造函数
	//...
};
```

拷贝构造函数的第一个参数必须是一个引用类型，虽然我们可以定义一个接受非`const`引用的拷贝构造函数，但此参数几乎总是一个`const`引用。拷贝构造函数在几种情况下都会被隐式地使用。因此，拷贝构造函数通常不应该是`explicit`的。

#### 13.1.1.1 合成拷贝构造函数（synthesized copy constructor）

如果我们没有为一个类定义拷贝构造函数，编译器会为我们定义一个。与合成默认构造函数不同，即使我们定义了其他构造函数，编译器也会为我们合成一个拷贝构造函数。

每个成员的类型决定了它如何拷贝：对类类型成员，会使用其拷贝构造函数来拷贝；内置类型的成员则直接拷贝。Sales_data 类的合成拷贝构造函数等价于：

```
class Slaes_data{
public:
	//其他成员和构造函数的定义，如前
	//与合成的拷贝构造函数等价的拷贝构造函数的声明
	Sales_data(const Sales_data&);
private:
	std::string bookNo;
	int units_sold = 0;
	double revenue = 0.0;
};
//与 Sales_data 的合成的拷贝构造函数等价
Sales_data::Sales_data(const Sales_data&orig):
	bookNo(orig.bookNo),	//使用string的拷贝构造函数
	units_sold(orig.units_sold)，	//拷贝orig.units_sold
	revenue(orig.revenue)	//拷贝orig.revenue
	{ }	//空函数体
```

#### 13.1.1.2 拷贝初始化（copy initialization）

```
string dots(10,'.');	//直接初始化
string s(dots);		//直接初始化
string s2 = dots;	//拷贝初始化
string null_book = "9-999-99999-9";	//拷贝初始化
string nines = string(100, '9');	//拷贝初始化
```

当使用直接初始化时，我们实际上是要求编译器使用普通的函数匹配来选择与我们提供的实参最匹配的构造函数。当我们使用拷贝初始化时，我们要求编译器将右侧运算对象拷贝到正在创建的对象中，如果需要的话还要进行类型转换。

拷贝初始化通常通过拷贝构造函数来完成，但是，如果一个类有一个移动构造函数，则拷贝初始化有时会使用移动构造函数而非拷贝构造函数来完成。

拷贝初始化不仅在外面用=定义变量时会发生，在下列情况下也会发生：

- 将一个对象作为实参传递给一个非引用类型的形参
- 从一个返回类型为非引用类型的函数返回一个对象
- 用花括号列表初始化一个数组中的元素或一个聚合类中的成员

某些类类型还会对它们所分配的对象使用拷贝初始化。例如，当我们初始化标准库容器或是调用其`insert`或`push`成员时，容器会对其元素进行拷贝初始化。与之相对，用`emplace`成员创建的元素都进行直接初始化。

#### 13.1.1.3 参数和返回值

在函数调用过程中，具有非引用类型的参数要进行拷贝初始化。

拷贝构造函数被用来初始化非引用类类型参数，这一特性解释了为什么拷贝构造函数自己的参数必须是引用类型。如果其参数不是引用类型，则调用永远也不会成功——为了调用拷贝构造函数，我们必须拷贝它的实参，但为了拷贝实参，我们又需要调用拷贝构造函数，如此无限循环。

#### 13.1.1.4 拷贝初始化的限制

如前所述，如果我们使用的初始化值要求通过一个`explicit`的构造函数来进行类型转换，那么使用拷贝初始化还是直接初始化就不是无关紧要的了：

```
vector<int> v1(10); //正确，直接初始化
vector<int> v2 = 10;    //错误：接受大小参数的构造函数是 explicit 的
void f(vector<int>);    //f 的参数进行拷贝初始化
f(10);  //错误：不能用一个 explicit 的构造函数拷贝一个实参
f(vector<int>(10)); //正确：从一个 int 直接构造一个临时的 vector
```

#### 13.1.1.5 编译器可以绕过拷贝构造函数

在拷贝初始化的过程中，编译器可以（但不是必须）跳过拷贝/移动构造函数，直接创建对象。即，编译器允许将下面的代码：

```
string null_book = "9-999-99999-9"; //拷贝初始化
```

改写为：

```
string null_book("9-999-99999-9");  //编译器略过了拷贝构造函数
```

但是，即使编译器略过拷贝/移动构造函数，但在这个程序点上，拷贝/移动构造函数必须是存在并且是可访问的（例如，不能是 private 的）。

### 13.1.2 拷贝赋值运算符

与控制其对象如何初始化一样，类也可以控制其对象如何赋值：

```
Sales_data trans, accum;
trans = accum;    //使用 Sales_data 的拷贝赋值运算符
```

#### 13.1.2.1 重载赋值运算符

重载运算符本质上是函数，其名字由`operator`关键字后接表示要定义的运算符的符号组成。因此，赋值运算符就是一个名为`operator=`的函数。

某些运算符，包括赋值运算符，必须定义为成员函数。如果一个运算符是一个成员函数，其左侧运算对象就绑定到隐式的`this`参数。对于一个二元运算符，例如赋值运算符，其右侧运算对象作为显式参数传递。

```
//拷贝赋值运算符接受一个与其所在类相同类型的参数
class Foo{
public:
	Foo &operator=(const Foo&);	//赋值运算符
	//...
};
```

为了与内置类型的赋值保持一致，赋值运算符通常返回一个指向其左侧运算对象的引用。

#### 13.1.2.2 合成拷贝赋值运算符

```
//等价于合成拷贝赋值运算符
Sales_data& Sales_data::operator=(const Sales_data &rhs)
{
	bookNo = rhs.bookNo；	//调用 string::operator=
	units_sold = rhs.units_sold;	//使用内置的 int 赋值
	revenue = rhs.revenue;	//使用内置的 double 赋值
	return *this;
}
```

### 13.1.3 析构函数

析构函数执行与构造函数相反的操作：构造函数初始化对象的非`static`数据成员，还可能做一些其他工作；析构函数释放对象使用的资源，并销毁对象的非`static`数据成员。

析构函数是类的一个成员函数，名字由波浪号接类名构成，没有返回值，也不接受参数：

```
class Foo{
public:
	~Foo();	//析构函数
	//...
};
```

由于析构函数不接受参数，因此它不能被重载。对一个给定类，只会有唯一一个析构函数。

在一个析构函数中，首先执行函数体，然后销毁成员。成员按初始化顺序的逆序销毁。

在一个析构函数中，不存在类似构造函数中初始化列表的东西来控制成员如何销毁，析构部分是隐式的。**成员销毁时发生什么完全依赖于成员的类型。**

销毁类类型成员需要执行成员自己的析构函数。内置类型没有析构函数，因此销毁内置类型成员什么也不需要做。所以：

- 隐式销毁一个内置指针类型的成员不会`delete`它所指向的对象
- 当指向一个对象的引用或指针离开作用域时，析构函数不会执行

```
{ //新作用域
    //p 和 p2 指向动态分配的内存
    Sales_data *p = new Sales_data; //p 是一个内置指针
    auto p2 = make_shared<Sales_data>();    //p2 是一个 shared_ptr
    Sales_data item(*p);    //拷贝构造函数将 p 拷贝到 item 中
    vector<Sales_data> vec; //局部变量
    vec.push_back(*p2); //拷贝 p2 指向的对象
    delete p;   //对 p 指向的对象进行析构函数
} //退出局部作用域；对 item、p2 和 vec 调用析构函数
  //销毁 p2 会递减其引用计数；如果引用计数为0，对象被释放
  //销毁 vec 会销毁它的元素
```

#### 13.1.3.1 什么时候会调用析构函数

无论何时一个对象被销毁，就会自动调用其析构函数：

- 变量在离开作用域时被销毁
- 当一个对象被销毁时，其成员被销毁
- 容器（无论是标准库容器还是数组）被销毁时，其元素被销毁
- 对于动态分配的对象，当对指向它的指针应用`delete`运算符时被销毁
- 对于临时对象，当创建它的完整表达式结束时被销毁

#### 13.1.3.2 合成析构函数（synthesized destructor）

当一个类未定义自己的析构函数时，编译器会为他定义一个合成析构函数。例如，下面的代码等价于 Sales_data 的合成析构函数：

```
class Sales_data{
public:
	//成员会被自动销毁，除此之外不需要做其他事情
	~Sales_data() {}
	//其他成员的定义，如前
};
```

在（空）析构函数体执行完毕后，成员会被自动销毁。特别的，`string`的析构函数会被调用，它将释放 bookNo 成员所用的内存。认识到析构函数本身并不直接销毁成员是非常重要的。成员是在析构函数体之后隐含的析构阶段中被销毁的。在整个对象销毁过程中，析构函数体是作为成员销毁步骤之外的另一部分而进行的。

### 13.1.4 三/五法则

如前所述，有三个基本操作可以控制类的拷贝操作：拷贝构造函数、拷贝赋值运算符和析构函数。而且，在新标准下，一个类还可以定义一个移动构造函数和一个移动赋值运算符。

#### 13.1.4.1 需要析构函数的类也需要拷贝和赋值操作

当我们决定一个类是否要定义它自己版本的拷贝控制成员时，一个基本的原则是首先确定这个类是否需要一个析构函数。如果这个类需要一个自定义析构函数，我几乎可以肯定它也需要自定义拷贝构造函数和自定义拷贝赋值运算符。

如果类在构造函数中分配动态内存。合成析构函数不会`delete`一个指针数据成员。因此，此类需要定义一个析构函数来释放构造函数分配的内存。

#### 13.1.4.2 需要拷贝操作的类也需要赋值操作，反之亦然

虽然很多类需要定义所有(或是不需要定义任何)拷贝控制成员，但某些类所要完成的工作，只需要拷贝或赋值操作，不需要析构函数。第二个基本原则：如果一个类需要一个拷贝构造函数，几乎可以肯定它也需要一个拷贝赋值运算符。反之亦然。

### 13.1.5 使用 =default

我们可以通过将拷贝控制成员定义为=default来显示地要求编译器生成合成的版本：

```
class Sales_data{
public:
	//拷贝控制成员；使用default
	Sales_data() = default;
	Sales_data(const Sales_data &) = default;
	Sales_data& operator=(const Sales_data &);
	~Sales_data() =default;
	//其他成员的定义，如前
};
Sales_data& Sales_data::operator=(const Sales_data&) = default;
```

当我们在类内使用`=default`修饰成员的声明时，合成的函数将隐式地声明为内联的。如果我们不希望合成的成员是内联函数，应该只对成员的类外定义使用`=default`，就像对拷贝赋值运算符所做的那样。

**我们只能对具有合成版本的成员函数使用`=default`(即，默认构造函数或拷贝控制成员)。**

### 13.1.6 阻止拷贝

大多数类应该定义默认构造函数、拷贝构造函数和拷贝赋值运算符，无论是隐式地还是显示地。

但是，在某些情况下，定义类时必须采用某种机制阻止拷贝或赋值。例如，`iostream`类阻止了拷贝，以避免多个对象写入或读取相同的 IO 缓冲。

为了阻止拷贝，看起来可能应该不定义拷贝控制成员。但是，这种策略是无效的：如果我们的类未定义这些操作，编译器为它生成合成的版本。

#### 13.1.6.1 定义删除的函数

在新标准下，我们可以通过将拷贝构造函数和拷贝赋值运算符定义为删除的函数（deleted function）来阻止拷贝。删除的函数是这样一种函数：我们虽然声明了它们但不能以任何方式使用它们：

```
struct NoCopy{
	NoCopy() = default;	//使用合成的默认构造函数
	NoCopy(const NoCopy&) = delete;	//阻止拷贝
	NoCopy &operator=(const NoCopy&) = delete;	//阻止赋值
	~NoCopy() = delete;	//使用合成的析构函数
	//其他成员
};
```

- `=delete`通知编译器（以及我们代码的读者），我们不希望定义这些成员
- 与`=default`不同，`=delete`必须出现在函数第一次声明的时候
- 与`=default`的另一不同之处是，我们可以对任何函数指定`=delete`（我们只能对编译器可以合成的默认构造函数或拷贝控制成员使用`=default`）

#### 13.1.6.2 析构函数不能是删除的成员

值得注意的是，我们不能删除析构函数。如果析构函数被删除，就无法销毁此类型的的对象了。对于析构函数已删除的类型，不能定义该类型的变量或释放指向该类型动态分配对象的指针，但是可以动态分配这种类型的对象（然而动态分配后不能释放）。

#### 13.1.6.3 合成的拷贝控制成员可能是删除的

如果一个类有数据成员不能默认构造、拷贝、复制或销毁，则对应的成员函数将被定义为删除的。

#### 13.1.6.4 private 拷贝控制

在新标准发布之前，类是通过将其拷贝构造函数和拷贝赋值运算符声明为`private`的来阻止拷贝：

```
class PrivateCopy{
	//无访问说明符；接下来的成员默认为 private 的
	//拷贝控制成员是 private 的，因此普通用户代码无法访问
	PrivateCopy(const PrivateCopy&);
	PrivateCopy &operator=(const PrivateCopy&);
	//其他成员
public：
	PrivateCopy() = default;	//使用合成的默认构造函数
	~PrivateCopy();	//用户可以定义此类型的对象，但无法拷贝它们
};
```

为了阻止友元和成员函数进行拷贝，我们将这些拷贝控制成员声明为`private`的，但并不定义它们。声明但不定义一个成员函数是合法的(例外：我们必须为每一个虚函数都提供定义，而不管它是否被用到，这是因为连编译器也无法确定到底会使用哪个虚函数)。

通过声明（但不定义）`private`的拷贝构造函数，我们可以预先阻止任何拷贝该类对象的企图：试图拷贝对象的用户代码将在编译阶段被标记为错误；成员函数或友元函数的拷贝操作将会导致链接时错误。

建议：希望阻止拷贝的类应该使用`=delete`来定义它们自己的拷贝构造函数和拷贝赋值运算符，而不应该将它们声明为`private`的。

## 13.2 拷贝控制和资源管理

为了定义这些成员，我们首先必须确定此类型对象的拷贝语义。一般来说，有两种选择：可以定义拷贝操作，使类的行为看起来像一个值或者像一个指针。

类的行为像一个值，意味着它应该也有自己的状态。当我们拷贝一个像值的对象时，副本和原对象是完全独立的。改变副本不会对原对象有任何影响，反之亦然；

行为像指针的类则共享状态。当我们拷贝一个这种类的对象时，副本和原对象使用相同的底层数据。改变副本也会改变原对象，反之亦然。

### 13.2.1 行为像值的类

```
class HasPtr{
public:
	HasPtr(const std::string &s = std::string()):ps(new std::string(s)),
			i(0){ }
	//ps 指向的 string，每个 HasPtr 对象都有自己的拷贝
	HasPtr(const HasPtr &p):
			ps(new std::string (*p.ps)), i(p.i) {}
	HasPtr& operator=(const HasPtr &);
	~HasPtr() {delete ps;}
private:
	std::string *ps;
	int i;
};
```

类值拷贝赋值运算符赋值运算符通常组合了析构函数和构造函数的操作：类似析构函数，赋值操作会销毁左侧运算对象的资源；类似拷贝构造函数，赋值操作会从右侧运算对象拷贝数据。

本例中，通过先拷贝右侧运算对象，我们可以处理自赋值情况，并能保证异常发生时代码也是安全的。在完成拷贝后，我们释放左侧运算对象的资源，并更新指针指向新分配的`string`：

```
HasPtr& HasPtr::operator=(const HasPtr&rhs)
{
	auto newp = new string(*rhs.ps);	//拷贝底层 string，注意成员选择优先级大于解引用，故等价于*(rhs.ps)
	delete ps;	//释放旧内存
	ps = newp;	//从右侧运算对象拷贝数据到本对象
	i = rhs.i;
	return *this;	//返回本对象
}
```

当你编写赋值运算符时，有两点需要记住：

- 如果将一个对象赋予它自身，赋值运算符必须能正确工作
- 大多数赋值运算符组合了析构函数和拷贝构造函数的工作

当你编写一个赋值运算符时，一个好的模式是先将右侧运算对象拷贝到一个局部临时对象中。当拷贝完成后，销毁左侧运算对象的现有成员就是安全的了。一旦左侧运算对象的资源被销毁，就只剩下将数据从临时对象拷贝到左侧运算对象的成员中了。

为了说明防范自赋值操作的重要性，看下面一个错误的例子：

```
//这样编写赋值运算符是错误的！
HasPtr& HasPtr::operator=(const HasPtr &rhs)
{
	delete ps;	//释放对象指向的 string
	//如果 rhs 和 *this 是同一个对象，我们就将从已释放的内存中拷贝数据！
	ps = new string(*(rhs.ps));
	i = rhs.i;
	return *this;
}
```

如果 rhs 和本对象是同一个对象，`delete ps`会释放`*this`和 rhs 指向的`string`。接下来，当我们在`new`表达式中试图拷贝`*(rhs.ps)`时，就会访问一个指向无效内存的指针，其行为和结果是未定义的。

### 13.2.2 定义行为像指针的类

对于行为类似指针的类，我们需要为其定义拷贝构造函数和拷贝赋值运算符，来拷贝指针成员本身而不是它指向的`string`。我们的类仍然需要自己的析构函数来释放接受`string`参数的构造函数分配的内存。但是，析构函数不能单方面地释放关联的`string`，只有当最后一个指向`string`的对象销毁时，才可以释放`string`。

令一个类展现类似指针的行为最好的方法是使用`shared_ptr`来管理类中的资源。如果我们希望直接管理资源，可以使用引用计数（reference count）。下面我们不使用`shared_ptr`而是使用引用计数来实现行为像指针的类。

#### 引用计数

引用计数的工作方式如下：

- 除了初始化对象之外，每个构造函数(拷贝构造函数除外)都要创建一个引用计数，用来记录有多少对象共享正在创建的对象共享状态，当创建一个对象时，引用计数为1，因为此时只有一个对象共享
- 拷贝构造函数不分配新得引用计数器，拷贝给定对象的数据成员，包括引用计数器，拷贝构造函数递增共享的计数器，表示给定对象更的状态又被一个新用户所共享
- 拷贝赋值运算符递减左侧运算对象的引用计数器，递增右侧对象的引用计数器，如果左侧对象的引用计数器为0，则销毁左侧对象
- 析构函数判断引用计数是否为0，如果为0，则销毁左侧对象

引用计数的实现：我们假设有下面的情况：

```
HasPtr h1;
HasPtr h2(h1);
HasPtr h3(h1);
```

HasPtr 是一个行为像指针的类，新创建的 h1的引用计数为1，创建 h2，用 h1 初始化 h2，会递增 h1 的引用计数值，此时 h2 保存了 h1 中的引用计数，在创建 h3 的时候，递增了 h1 的引用计数值，而且我们必须做的是要更新 h2 中的引用计数值，此时无法更新 h2 中的引用计数值。因此，我们需要将引用计数保存在动态内存中，这样原对象和其他副本对象都会指向相同的计数器，这样就可以自动更新引用计数在每个共享对象中的状态。

```
class HasPtr {
public:
	//构造函数分配新的 string 和新的计数器，将计数器置为1
	HasPtr(const std::string& s = std::string()) : ps(new std::string(s)), i(0), use(new size_t(1)) {}
	//拷贝构造函数拷贝所以三个数据成员，并递增计数器
	HasPtr(const HasPtr &p) :  ps(p.ps), i(p.i), use(p.use) { ++*use; }
	HasPtr& operator = (const HasPtr&);
	~HasPtr();
private:
	std::string *ps;
	int	i;
	std::size_t *use; // 引用计数
};

HasPtr::HasPtr& operator = (const HasPtr& has) {
	++*has.use;	//递增右侧运算对象的引用计数
	if (0 == --*use) { //然后递减本对象的引用计数
		delete ps;
		delete use;
	}
	ps = has.ps;
	i = has.i;
	use = has.use;
	return *this;
}

HasPtr::~HasPtr() {
	if (--*use == 0) {
		delete ps;
		delete use;
	}
}
```

## 13.3 交换操作

通常，管理资源的类除了定义拷贝控制成员之外，还会定义交换操作的函数`swap`。

如果一个类定义了自己的`swap`，那么算法将使用类自定义版本，否则，将使用标准库定义的`swap`。

理论上来说，我们的`swap`函数应该是这样的：

```
//交换两个类值 HasPtr 对象的代码可能像下面这样：
HasPtr temp = v1;	//创建 v1 的值的一个临时副本
v1 = v2;	//将 v2 的值赋予 v1
v2 = temp;	//将保存的 v1 的值赋予 v2
```

这样的代码将 v1 中`string`拷贝了两次，但是这样做是没有必要的，我们希望`swap`交换指针，而不是分配`string`的副本：

```
string *temp = v1.ps;	//为 v1.ps 中的指针创建一个副本
v1.ps = v2.ps;	//将 v2.ps 中的指针赋予 v1.ps1
v2.ps = temp;	//将保存的 v1.ps 中原来的指针赋予 v2.ps
```

### 13.3.1 编写我们自己的 swap 函数

```
class HasPtr {
	friend void swap (HasPtr&, HasPtr&);
	//其他成员定义
};
inline void swap (HasPtr &lhs, HasPtr &rhs)
{
	using std::swap;
	swap(lhs.ps, rhs.ps);	//交换指针，而不是string数据
	swap(lhs.i, rhs.i);	//交换 int 成员
}
```

我们首先将`swap`定义为`friend`以便能访问 HasPtr 的（private的）数据成员。由于`swap`的存在就是为了优化代码，我们将其声明为`inline`函数。

与拷贝控制成员不同，`swap`并不是必要的。但是，对于分配了资源的类，定义`swap`可能是一种很重要的优化手段。

### 13.3.2 swap 函数应该调用 swap，而不是 std::swap

在`swap`函数中，使用了`using std::swap`，如果这个类有自己的`swap`函数，匹配程度会高于标准库`swap`，会优先使用类自己的`swap`，如果没有，则使用标准库的`swap`。

`swap`里交换类的指针和`int`成员，并不会发生递归循环，HasPtr 的数据成员是内置类型的，这时候会调用标准库版本的`swap`。

### 13.3.3 在赋值运算符中使用 swap

定义`swap`的类通常用`swap`来定义它们的赋值运算符。这些运算符使用了一种名为拷贝并交换（copy and swap）的技术。这种技术将左侧运算对象与右侧运算对象的一个副本进行交换：

```
//注意 rhs 是按值传递的，意味着 HasPtr 的拷贝构造函数将
//右侧运算对象中的 string 拷贝到 rhs
HasPtr& HasPtr::operator=(HasPtr rhs)
{
	//交换左侧运算对象和局部变量 rhs 的内容
	swap(*this, rhs);	//rhs 现在指向本对象曾经使用的内存
	return *this;	//rhs 被销毁，从而 delete 了 rhs 中的指针
}
```

在进行 HasPtr 类的赋值运算中，先将右侧对象拷贝到拷贝赋值运算符函数里，然后交换左侧对象的指针和右侧对象的指针，交换后，右侧对象赋值给了左侧对象，左侧对象相应的`string`指针也指向了右侧对象副本的对应成员，而右侧对象的`string`指针则指向了左侧对象的相应成员。在这个函数结束后，右侧对象的副本被销毁，于是原来左侧对象的资源被释放，而左侧对象现在保存的是右侧对象的成员。

拷贝并交换的操作，和之前的拷贝赋值运算符的实现原理是相同的， 在改变左侧对象之前拷贝右侧对象。保证了这样的操作异常的安全。

## 13.4 对象移动

新标准的一个最主要的特性是可以移动而非拷贝对象的能力。在某些情况下对象拷贝后就立即被销毁了。在这些情况下，移动而非拷贝对象会大幅度提升性能。

使用移动而不是拷贝的另一个原因源于`IO`类或`unique_ptr`这样的类。这些类都包括不能被共享的资源。因此，这些类型的对象不能拷贝但可以移动。

类似的，在旧版本的标准库中，容器所保存的类必须是可拷贝的，但在新标准中，我们可以用容器保存不可拷贝的类型，只要它们能被移动就行。

标准库容器、`string`和`shared_ptr`类既支持移动也支持拷贝。`IO`类和`unique_ptr`类可以移动但不能拷贝。

### 13.4.1 右值引用

为了支持移动操作，新标准引入了一种新的引用类型——右值引用（rvalue reference）。我们通过`&&`而不是`&`来获得右值引用。右值引用一个重要性质——只能绑定到一个将要销毁的对象。

一般而言，一个左值表达式表示的是一个对象的身份，而一个右值表达式表示的是对象的值。

对于常规引用(我们可以称之为左值引用)，我们不能将其绑定到要求转换的表达式、字面常量或是返回右值的表达式。右值引用有着完全相反的特性：我们可以将一个右值引用绑定到这类表达式上，但不能将一个右值引用直接绑定到一个左值上：

```
int i = 42;
int &r = i;	//正确：r 引用 i
int &&rr = i;	//错误：不能将一个右值引用绑定到一个左值上
int &r2 = i * 42;	//错误：i * 42是一个右值
const int &r3 = i * 42;	//正确：我们可以将一个 const 的引用绑定到一个右值上
int &&rr2 = i * 42;	//正确：将 rr2 绑定到乘法结果上
```

返回左值引用的函数，连同赋值、下标、解引用和前置递增/递减运算符，都是返回左值的表达式的例子，我们可以将一个左值引用绑定到这类表达式的结果上。

返回非引用类型的函数，连同算术、关系、位以及后置递增/递减运算符，都生成右值。我们不能将一个左值引用绑定到这类表达式上，但我们可以将一个`const`的左值引用或者一个右值引用绑定到这类表达式上。

#### 13.4.1.1 左值持久；右值短暂

由于右值引用只能绑定到临时对象，我们得知：

- 所引用的对象将要被销毁
- 该对象没有其他用户

这两个特性意味着：使用右值引用的代码可以自由地接管所引用的对象的资源。右值引用指向将要被销毁的对象。因此，我们可以从绑定到右值引用的对象“窃取”状态。

#### 13.4.1.2 变量是左值

变量可以看作只有一个运算对象而没有运算符的表达式。变量表达式都是左值，这意味着我们不能讲一个右值引用绑定到一个右值引用类型的变量上：

```
int &&rr1 = 42;   //正确：字面常量是右值
it &&rr2 = rr1;   //错误：表达式 rr1 是左值！
```

其实有了右值表示临时对象这一观察结果，变量是左值这一特性并不令人惊讶。毕竟，变量是持久的，直至离开作用域时才被销毁。

**变量是左值，因此我们不能将一个右值引用直接绑定到一个变量上，即使这个变量是右值引用类型也不行。**

#### 13.4.1.3 标准库 move 函数

虽然不能将一个右值引用直接绑定到一个左值上，但我们可以显示地将一个左值转换为对应的右值引用类型。我们还可以通过调用一个名为`move`的新标准库函数来获得绑定到左值上的右值引用。`move`定义在头文件`utility`中。

```
#inclue <utility>
int &&rr3 = std::move(rr1);   //ok
```

`move`调用告诉编译器：我们有一个左值，但我们希望像一个右值一样处理它。我们必须认识到，调用`move`就意味承诺：除了对 rr1 赋值或销毁它外，我们将不再使用它。

**我们可以销毁一个移后源对象，也可以赋予它新值，但不能使用一个移后源对象的值。**

对`move`我们不提供`using`声明。我们直接调用`std::move`而不是`move`。这样可以避免潜在的名字冲突。

### 13.4.2 移动构造函数和移动赋值运算符

类似`string`类（及其他标准库类），如果我们自己的类也同时支持移动和拷贝，那么也能从中受益。这两个成员类似对应的拷贝操作，但它们从给定对象“窃取”资源而不是拷贝资源。

类似拷贝构造函数，移动构造函数的第一个参数是该类类型的一个引用。不同于拷贝构造函数的是，这个引用参数在移动构造函数中是一个右值引用。与拷贝构造函数一样，任何额外的参数都必须有默认实参。

除了完成资源移动，移动构造函数还必须确保移后源对象处于这样一个状态——销毁它是无害的。

作为一个例子，我们为 StrVec 类定义移动构造函数，实现从一个 StrVec 到另一个 StrVec 的元素移动而非拷贝：

```
StrVec::StrVec(StrVec &&s) noexcept	//移动操作不应抛出任何异常
//c成员初始化器接管s中的资源
  ：elements(s.elements), first_free(s.first_free), cap(s.cap)
{
	//令s进入这样的状态———对其运行析构函数是安全的
	s.elements = s.first_free = s.cap = nullptr;
}
```

#### 13.4.2.1 移动操作、标准库容器和异常

由于移动操作“窃取”资源，它通常不分配任何资源。因此，移动操作通常不会抛出任何异常。一种通知标准库的方法是在我们的构造函数中指明`noexcept`。`noexcept`是新标准引入的。在一个构造函数中，`noexcept`出现在参数列表被初始化列表开始的冒号之间。我们必须在类头文件声明和定义中（如果定义在类外的话）都指定`noexcept`。

**不抛出异常的移动构造函数和移动赋值运算符必须标记为`noexcept`。**

![为什么指定noexcept]({filename}/images/c++13-1.jpg)

#### 13.4.2.2 移动赋值运算符

移动赋值运算符执行与析构函数和移动构造函数相同的工作。

```
StrVec &StrVec::operator=(StrVec &&rhs) noexcept
{
	//直接检测自赋值
	if (this != &rhs){
		free();	//释放已有元素
		elements = rhs.elements;	//从 rhs 接管资源
		first_free = rhs.first_free;
		cap = rhs.cap;
		//将 rhs 置于可析构状态
		rhs.elements = rhs.first_free = rhs.cap = nullptr;
	}
	return *this;
}
```

我们进行自赋值检查的原因是此右值可能是`move`调用的返回结果。

#### 13.4.2.3 移后源对象必须可析构

在移动操作之后，移后源对象必须保持有效的、可析构的状态，但是用户不能对其值进行任何假设。

#### 13.4.2.4 合成的移动操作

只有当一个类没有定义任何自己版本的拷贝控制成员，且类的每个非`static`数据成员都可以移动时，编译器才会为它合成移动构造函数或移动赋值运算符。

与拷贝操作不同，移动操作永远不会隐式定义为删除的函数。但是，如果我们显示地要求编译器生成`=default`的移动操作，且编译器不能移动所有成员，则编译器会将移动操作定义为删除的函数。

移动操作和合成的拷贝控制成员之间还有最后一个相互作用关系：一个类是否定义了自己的移动操作对拷贝操作如何合成有影响。如果类定义了一个移动构造函数和/或一个移动赋值运算符，则该类的合成拷贝构造函数和拷贝赋值运算符会被定义为删除的。

#### 13.4.2.5 移动右值，拷贝左值

如果一个类既有移动构造函数，也有拷贝构造函数，编译器使用普通的函数匹配规则来确定使用哪个构造函数。赋值操作的情况类似。

#### 13.4.2.6 但如果没有移动构造函数，右值也被拷贝

使用拷贝构造函数代替移动构造函数几乎肯定是安全的。

#### 13.4.2.7 拷贝并交换赋值运算符和移动操作

![拷贝并交换赋值运算符和移动操作]({filename}/images/c++13-2.jpg)

#### 13.4.2.8 更新的三/五法则

一般来说，如果一个类定义了任何一个拷贝操作，它就应该定义所有五个操作。

#### 13.4.2.9 移动迭代器

新标准库中定义了一种移动迭代器（move iterator）适配器。一个移动迭代器通过改变给定迭代器的解引用运算符的行为来适配此迭代器。一般来说，一个迭代器的解引用运算符返回一个指向元素的左值。与其他迭代器不同，移动迭代器的解引用运算符生成一个右值引用。

我们通过调用标准库的`make_move_iterator`函数将一个普通迭代器转换为一个移动迭代器。此函数接受一个迭代器参数，返回一个移动迭代器。

原迭代器的所有其他操作在移动迭代器中都照常工作。由于移动迭代器支持正常的迭代器操作，我们可以将一对移动迭代器传递给算法。特别地，可以将移动迭代器传递给`uninitialized_copy`：

```
void StrVec::reallocate()
{
	//分配大小两倍于当前规模的内存空间
	auto newcapacity = size() ? 2 * size() : 1;
	auto first = alloc.allocate(newcapacity);
	//移动元素
	auto last = uninitialized_copy(make_move_iterator(begin()), make_move_iterator(end()), first);
	free();	//释放旧空间
	elements = first;	//更新指针
	first_free = last;
	cap = elements + newcapacity;
}
```

不要随意使用移动操作，由于一个移后源对象具有不确定的状态，对其调用`std::move`是危险的。当我们调用`move`时，必须绝对确认移后源对象没有其他用户。

通过在类代码中小心地使用`move`，可以大幅度提升性能。而如果随意在普通用户代码（与类实现代码相对）中使用移动操作，很可能导致莫名其妙的、难以查找的错误，而难以提升应用程序性能。

### 13.4.3 右值引用和成员函数

除了构造函数和赋值运算符外，如果一个成员函数同时提供拷贝和移动操作，它也能从中受益。一个版本接受一个指向`const`的左值引用，另一个版本接受指向非`const`的右值引用。

一般来说，我们不需要为函数操作定义接受一个`const X&&`或是一个（普通的）`X&`参数的版本。当我们希望从实参“窃取”数据时，通常传递一个右值引用。为了达到这一目的，实参不能是`const`的。类似的，从一个对象进行拷贝的操作不应该改变该对象，因此，通常不需要定义一个接受（普通的）`X&`参数的版本。

区分移动和拷贝的重载函数通常有一个版本接受一个`const T&`，而另一个版本接受`T&&`。

```
class StrVec{
public:
	void push_back(const std::string &); //移动元素
	void push_back(std::string &&);	//拷贝元素
	//其他成员的定义
};

void StrVec:push_back(const string& s){
	chk_n_alloc();	//确保有空间容纳新元素
	//在 first_free 指向的元素中构造 s 的一个副本
	alloc.constructor(first_free++, s);
}

void StrVec::push_back(string &&){
	chk_n_alloc();	//如果需要的话为 StrVec 重新分配内存
	alloc.constructor(first_free++, std::move(s));
}
```

`constructor`函数使用第二个和随后的实参类型来确定使用哪个构造函数。由于`move`返回一个右值引用，因此，会使用`string`的移动构造函数来构造新元素。

#### 13.4.3.1 左值和右值引用成员函数

![左值和右值引用成员函数]({filename}/images/c++13-3.jpg)

#### 13.4.3.2 重载和引用函数

就像一个成员函数可以根据是否有`const`来区分其重载版本一样，引用限定符也可以区分重载版本。而且，我们可以综合引用限定符和`const`来区分一个成员函数的重载版本。

当我们定义`const`成员函数时，可以定义两个版本，唯一的差别是一个版本有`const`限定而另一个没有。引用限定的函数则不一样。如果我们定义两个或两个以上具有相同名字和相同参数列表的成员函数，就必须对所有函数都加上引用限定符，或者所有都不加。
