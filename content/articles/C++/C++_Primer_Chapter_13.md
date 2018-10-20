Title: C++ Primer 第十三章 拷贝控制
Category: 读书笔记
Date: 2018-10-20 16:41:10
Modified: 2018-10-20 16:41:10
Tags: C++

当定义一个类时，我们显示地或隐式地指定在此类型的对象拷贝、移动、赋值和销毁时做什么。一个类通过定义五种特殊的成员函数来控制这些操作，包括：拷贝构造函数（copy constructor）、拷贝赋值运算符（copy-assignment operator）、移动构造函数（move constructor）、移动赋值运算符（move-assignment operator）和析构函数（destructor）。

拷贝和移动构造函数定义了当用同类型的另一个对象初始化本对象时做什么。

拷贝和移动赋值运算符定义了将一个对象赋予同类型的另一个对象时做什么。

析构函数定义了当此类型对象销毁时做什么。

我们称这些操作为拷贝控制操作（copy control）。

## 拷贝、赋值和销毁

### 拷贝构造函数

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

#### 合成拷贝构造函数（synthesized copy constructor）

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

#### 拷贝初始化（copy initialization）

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

#### 参数和返回值

在函数调用过程中，具有非引用类型的参数要进行拷贝初始化。

拷贝构造函数被用来初始化非引用类类型参数，这一特性解释了为什么拷贝构造函数自己的参数必须是引用类型。如果其参数不是引用类型，则调用永远也不会成功——为了调用拷贝构造函数，我们必须拷贝它的实参，但为了拷贝实参，我们又需要调用拷贝构造函数，如此无限循环。

#### 拷贝初始化的限制

如前所述，如果我们使用的初始化值要求通过一个`explicit`的构造函数来进行类型转换，那么使用拷贝初始化还是直接初始化就不是无关紧要的了：

```
vector<int> v1(10); //正确，直接初始化
vector<int> v2 = 10;    //错误：接受大小参数的构造函数是 explicit 的
void f(vector<int>);    //f 的参数进行拷贝初始化
f(10);  //错误：不能用一个 explicit 的构造函数拷贝一个实参
f(vector<int>(10)); //正确：从一个 int 直接构造一个临时的 vector
```

#### 编译器可以绕过拷贝构造函数

在拷贝初始化的过程中，编译器可以（但不是必须）跳过拷贝/移动构造函数，直接创建对象。即，编译器允许将下面的代码：

```
string null_book = "9-999-99999-9"; //拷贝初始化
```

改写为：

```
string null_book("9-999-99999-9");  //编译器略过了拷贝构造函数
```

但是，即使编译器略过拷贝/移动构造函数，但在这个程序点上，拷贝/移动构造函数必须是存在并且是可访问的（例如，不能是 private 的）。

### 拷贝赋值运算符

与控制其对象如何初始化一样，类也可以控制其对象如何赋值：

```
Sales_data trans, accum;
trans = accum;    //使用 Sales_data 的拷贝赋值运算符
```

#### 重载赋值运算符

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

#### 合成拷贝赋值运算符

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

### 析构函数

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

#### 什么时候会调用析构函数

无论何时一个对象被销毁，就会自动调用其析构函数：

- 变量在离开作用域时被销毁
- 当一个对象被销毁时，其成员被销毁
- 容器（无论是标准库容器还是数组）被销毁时，其元素被销毁
- 对于动态分配的对象，当对指向它的指针应用`delete`运算符时被销毁
- 对于临时对象，当创建它的完整表达式结束时被销毁

#### 合成析构函数（synthesized destructor）

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

### 三/五法则

如前所述，有三个基本操作可以控制类的拷贝操作：拷贝构造函数、拷贝赋值运算符和析构函数。而且，在新标准下，一个类还可以定义一个移动构造函数和一个移动赋值运算符。

#### 需要析构函数的类也需要拷贝和赋值操作

当我们决定一个类是否要定义它自己版本的拷贝控制成员时，一个基本的原则是首先确定这个类是否需要一个析构函数。如果这个类需要一个自定义析构函数，我几乎可以肯定它也需要自定义拷贝构造函数和自定义拷贝赋值运算符。

如果类在构造函数中分配动态内存。合成析构函数不会`delete`一个指针数据成员。因此，此类需要定义一个析构函数来释放构造函数分配的内存。

#### 需要拷贝操作的类也需要赋值操作，反之亦然

虽然很多类需要定义所有(或是不需要定义任何)拷贝控制成员，但某些类所要完成的工作，只需要拷贝或赋值操作，不需要析构函数。第二个基本原则：如果一个类需要一个拷贝构造函数，几乎可以肯定它也需要一个拷贝赋值运算符。反之亦然。

### 使用 =default

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

### 阻止拷贝

大多数类应该定义默认构造函数、拷贝构造函数和拷贝赋值运算符，无论是隐式地还是显示地。

但是，在某些情况下，定义类时必须采用某种机制阻止拷贝或赋值。例如，`iostream`类阻止了拷贝，以避免多个对象写入或读取相同的 IO 缓冲。

为了阻止拷贝，看起来可能应该不定义拷贝控制成员。但是，这种策略是无效的：如果我们的类未定义这些操作，编译器为它生成合成的版本。

#### 定义删除的函数

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

#### 析构函数不能是删除的成员

值得注意的是，我们不能删除析构函数。如果析构函数被删除，就无法销毁此类型的的对象了。对于析构函数已删除的类型，不能定义该类型的变量或释放指向该类型动态分配对象的指针，但是可以动态分配这种类型的对象（然而动态分配后不能释放）。

#### 合成的拷贝控制成员可能是删除的

如果一个类有数据成员不能默认构造、拷贝、复制或销毁，则对应的成员函数将被定义为删除的。

#### private 拷贝控制

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

为了阻止友元和成员函数进行拷贝，我们将这些拷贝控制成员声明为`private`的，但并不定义它们。声明但不定义一个成员函数是合法的(除了在继承中需要覆盖基类的情况)。

通过声明（但不定义）`private`的拷贝构造函数，我们可以预先阻止任何拷贝该类对象的企图：试图拷贝对象的用户代码将在编译阶段被标记为错误；成员函数或友元函数的拷贝操作将会导致链接时错误。

建议：希望阻止拷贝的类应该使用`=delete`来定义它们自己的拷贝构造函数和拷贝赋值运算符，而不应该将它们声明为`private`的。

## 拷贝控制和资源管理

为了定义这些成员，我们首先必须确定此类型对象的拷贝语义。一般来说，有两种选择：可以定义拷贝操作，使类的行为看起来像一个值或者像一个指针。

类的行为像一个值，意味着它应该也有自己的状态。当我们拷贝一个像值的对象时，副本和原对象是完全独立的。改变副本不会对原对象有任何影响，反之亦然；

行为像指针的类则共享状态。当我们拷贝一个这种类的对象时，副本和原对象使用相同的底层数据。改变副本也会改变原对象，反之亦然。

### 行为像值的类

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

### 定义行为像指针的类

待续 ...