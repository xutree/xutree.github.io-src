Title: C++ Primer 第十六章 模板与泛型编程
Category: 读书笔记
Date: 2018-10-21 10:23:30
Modified: 2018-10-21 13:39:16
Tags: C++

[TOC]

面向对象编程（OOP）和泛型编程都能处理在编写程序时不知道类型的情况。不同之处是：OOP能处理类型在程序运行之前都未知的情况；而在泛型编程中，在编译时就能获知类型了。

容器、迭代器和算法都是泛型编程的例子。模板是 C++ 中泛型编程的基础。一个模板就是一个创建类或函数的蓝图或者说公式。

## 16.1 定义模板

### 16.1.1 函数模板

模板的定义以关键字`template`开始，后面跟一个模板参数列表，用`<>`括起来。

模板有类型参数（type parameter）和非类型参数（nontype parameter）之分。

#### 16.1.1.1 类型参数

我们可以将类型参数看作类型说明符，就像内置类型或类类型说明符一样使用。

类型参数可以用来指定返回类型或函数的参数类型，以及在函数体内用于变量声明或类型转换。

参数列表中，类型参数前必须使用关键字`class`或`typename`。在模板定义中，模板参数列表不能为空。

```
// 错误，U 之前必须加上 class 或 typename
template <typename T, U>
T calc(const T&, const U&);
```

#### 16.1.1.2 非类型参数

除了定义类型参数，还可以在模板中定义非类型参数，通过一个特定的类型名而非关键字`class`或`typename`来指定非类型参数。

因为编译器需要在编译时实例化模板，此时非类型参数会被一个用户提供的或编译器推断出的值所代替，所以这些值必须是常量表达式。

非类型参数可以是一个整型，对应的模板实参必须是常量表达式。而在模板定义内，可以将这个非类型参数用在任何需要常量表达式的地方，如指定数组大小。

```
template <unsigned N, unsigned M>
int compare(const cahr (&p1)[N], const cahr (&p2)[M])
[
   return strcmp(p1, p2);
}
compare("hi", "mom");
// 上式调用会实例化处如下版本，注意字符串字面常量的末尾有一个空字符！
int compare(const cahr (&p1)[3], const cahr (&p2)[4])
```

也可以是一个指向对象或函数类型的指针或（左值）引用。绑定到指针或引用非类型参数的实参必须具有静态的生存期。

#### 16.1.1.3 inline 和 constexpr 的函数模板

函数模板可以声明为`inline`或`constexpr`的，如同非模板函数一样。`inline`或`constexpr`说明符放在模板参数列表之后，返回类型之前：

```
//正确，inline 说明符跟在模板参数列表之后
template <typename T> inline T min(const T&, const T&);
//错误：inline 说明符的位置不正确
inline template <typename T> T min(const T&, const T&);
```

#### 16.1.1.4 编写类型无关的代码

为了提高适用性，模板程序应尽量减少对实参类型的要求。

模板中的函数参数是`const`的引用。这样做一方面保证了即使参数类型不支持拷贝，模板程序也能正确运行；另一方面引用不会引起对象的拷贝构造，提高运行性能。

模板中使用到的类型相关的函数或运算符应尽可能的少。

#### 16.1.1.5 模板编译

当编译器遇到一个模板定义时，它并不生成代码。只有当我们实例化出模板的一个特定版本时，编译器才会生成代码。

通常，当我们调用一个函数时，编译器只需要掌握函数的声明。类似的，当我们使用一个类类型的对象时，类定义必须是可用的，但成员函数的定义不必已经出现。因此，我们将类定义和函数声明放在头文件中，而普通函数和类的成员函数的定义放在源文件中。

为了生成一个实例化版本，编译器需要掌握函数模板或类模板成员函数的定义。因此，与非模板代码不同，模板不能分离式编译，其头文件中通常既包括声明也包括定义。

#### 16.1.1.6 大多数编译错误在实例化期间报告

模板直到实例化时才会生成代码，大多数编译错误在实例化期间报告。通常，编译器会在三个阶段报告错误。

第一个阶段是编译模板本身时。这个阶段，编译器可以检查语法错误，如忘记分号或者变量名拼错等。

第二个阶段是编译器遇到模板使用时。对于函数模板调用，会检查实参数目是否正确和参数类型是否匹配。对于类模板，则只检查模板实参数目是否正确。

第三个阶段是模板实例化时，只有这个阶段才能发现类型相关的错误。依赖于编译器如何管理实例化，这类错误可能在链接时才报告。

### 16.1.2 类模板

类模板（class template）是用来生成类的蓝图的。与函数模板的不同之处是，编译器不能为类模板推断模板参数类型。使用时，必须显式提供模板实参。

#### 16.1.2.1 定义类模板

在类模板（及其成员）的定义中，我们将模板参数当做替身，代替使用模板时用户需要提供的类型或值：

```
template <typename T>
class Bolb {
public:
	typedef T value_type;
	typedef typename std::vector<T>::size_type size_type;
	//构造函数
	Bolb();
	Bolb(std::initializer_list<T> il);
	//Bolb中的元素数目
	size_type size() const { return data->size(); }
	bool empty() const { return data->empty(); }
	//添加和删除元素
	void push_back(const T &t) { data->push_back(t); }
	//移动版本
	void push_back(T &&t) { data->push_back(std::move(t)); }
	void pop_back();
	//元素访问
	T& back();
	T& operator[](size_type i);
private:
	std::shared_ptr<std::vector<T>> data;
	//若data[i]无效，则抛出msg
	void check(size_type i, const std::string &msg) const;
};
```

#### 16.1.2.2 实例化模板

当使用一个类模板时，我们必须提供额外信息。我们现在知道这些额外信息是显式模板实参（explicit template argument）列表，它们被绑定到模板参数。例如：

```
Bolb<int> ia;	//空 Bolb<int>
Bolb<int> ia2 = {0,1,2,3,4};	//有5个元素的 Bolb<int>
```

一个类模板的每个实例都形成一个独立的类。Bolb<string> 与任何其他 Bolb 类型没有关联，也不会对任何其他 Bolb 类型的成员有特殊访问权限。

#### 16.1.2.3 类模板的成员函数

我们既可以在类模板内部，也可以在外部为其定义成员函数。定义在类模板之外的成员函数必须以关键字`template`开始，后接类模板参数列表。

默认情况下，一个类模板的成员函数只有当程序用到它时才进行实例化。这一特性使得即使某种类型不能完全符合模板操作的要求，仍然能用该类型实例化类，但相应操作无法使用！

#### 16.1.2.4 在类代码内简化模板类型的使用

在类模板自己的作用域中，我们可以直接使用模板名而不提供实参，其他情况下都必须提供模板实参。：

```
template <typename T>
class BolbPtr {
public:
...
//递增和递减
BolbPtr& operator++();	//前置运算符
BolbPtr& operator--();
...
};
```

上述 BolbPtr 的前置递增和递减成员返回 BolbPtr&，而不是 BolbPtr<T>&。当我们处于一个类模板的作用域时，编译器处理模板自身引用时就好像我们已经提供了与模板参数匹配的实参一样。

```
template <typename T>
// 返回类型，处于类的作用域之外，需要提供模板实参
BlobPtr<T> BlobPtr<T>::operator++(int)
{
   // 函数体内，处于类的作用域之内
   BlobPtr ret = *this;
   ...
}
```

#### 16.1.2.5 类模板和友元

如果一个类模板包含一个非模板友元，则友元被授权可以访问所有模板实例；如果友元自身是模板，类可以授权给所有友元模板实例，也可以只授权给特定实例。

一对一友好关系。用相同模板实参实例化的友元是该类的友元，可以访问非`public`部分，而对于用其他实参实例化的实例则没有特殊访问权限。

```
// 为了在 Blob 中声明友元，需要前置声明
template<typename T> class BlobPtr;
template<typename T> class Blob;   // 声明运算符 == 中的参数所需要的
template<typename T>
  bool operator==(const Blob<T> &lhs, const Blob<T> &rhs);
template <typename T>
class Blob
{
   // 每个 Blob 实例将访问权限授予用相同类型实例化的 BlobPtr 和相等运算符
   friend class BlobPtr<T>;
   friend bool operator==<T>
            (const MyBlobPtr &lhs, const MyBlobPtr &rhs);
   // 其它成员定义
};
// BlobPtr<char> 的成员可以访问 ca（或任何其它 Blob<char>对象）的非 public 部分
Blob<char> ca;
Blob<int> ia;
```

通用和特定的模板友好关系。为了让所有实例成为友元，友元声明中必须使用与类模板本身不同的模板参数。

```
// 前置声明，在将模板的一个特定实例声明为友元时要用到
template <typename T> class Pal;
class C {   // C是一个普通的非模板类
   friend class Pal<C>;   // 用类 C 实例化的 Pal 是 C 的一个友元
   // Pal2 的所有实例都是 C 的友元，这种情况无须前置声明
   template<typename T> friend class Pal2;
};
template<typename T> class C2 {  // C2 本身是一个模板
   // C2 的每个实例将相同实例化的 Pal 声明为友元
   friend class Pal<T>;   // Pal 的模板声明必须在作用域之内
   // Pal2 的所有实例都是 C2 的每个实例的友元，不需要前置声明
   template<typename X> friend class Pal2;
   // Pal3 是一个非模板类，它是 C2 所有实例的友元
   friend class Pal3;   // 不需要 Pal3 的前置声明
};
```

令模板自己的类型参数成为友元。在 C++11 新标准中，我们可以将模板类型参数声明为友元：

```
template <typename Type>
class Bar {
	friend Type;	//将访问权限授予用来实例化 Bar 的类型
	//...
};
```

因此，对于某个类型名 Foo，Foo 将成为 Bar<Foo> 的友元。

#### 16.1.2.6 模板类型别名

类模板的一个实例定义了一个类型，与任何其他类类型一样，我们可以定义一个`typedef`来引用实例化的类：`typedef Blob<string> StrBlob;`

由于模板不是一个类型，我们不能定义一个`typedef`引用一个模板。即，无法定义一个`typedef`引用 Blob<T>。

但是，C++11 新标准允许我们为类模板定义一个类型别名：

```
template <typename T>
using twin = pair<T,T>;
twin<string> authors;	//autohors 是一个 pair<string,string>
```

当我们定义一个模板类型别名时，可以固定一个或多个模板参数：

```
template <typename T>
using partNo = pair<T, unsigned>;
partNo<string> books;	//books 是一个 pair<string, unsigned>
partNo<Vehicle> cars;	//cars 是一个 pair<Vehicle, unsigned>
partNo<Student> kids;	//kids 是一个 pair<Student, unsigned>
```

#### 16.1.2.7 类模板的 static 成员

对于类模板 Foo 中的`static`成员 ctr，对于任意给定类型 X，都有一个 Foo::ctr 成员。所有 Foo 类型的对象共享相同的 ctr 成员：

```
template <typename T> class Foo {
public:
   static std::size_t count() { return ctr; }
   // 其它接口成员
private:
   static std::size_t ctr;
   // 其它数据成员
};
// 所有三个对象共享相同的 Foo<int>::ctr 和 Foo<int>::count 成员
Foo<int> fi, fi2, fi3;
```

类模板的`static`成员，可以通过类类型对象来访问，也可以用作用域运算符直接访问该成员，不过必须提供一个特定的模板实参。另外，`static`成员函数也是只在使用时才会被初始化：

```
Foo<int> fi;                  // 实例化 Foo<int> 类和 static 数据成员 ctr
auto ct = Foo<int>::count();  // 实例化 Foo<int>::count
ct = fi.count();              // 使用 Foo<int>::count
ct = Foo::count();            // 错误，无法确定使用哪个模板实例化的 count
```

### 16.1.3 模板参数

一个模板参数的名字也没有什么内在含义，我们通常将类型参数命名为 T，但实际上我们可以使用任何名字。

模板参数名的可用范围是在其声明之后，至模板声明或定义结束之前。模板参数会隐藏外层作用域中声明的相同名字，但是在模板内不能重用模板参数名。

```
typedef double A;
template <typename A, typename B> void f(A a, B b)
{
   A tmp = a;  // tmp的类型为模板参数 A 的类型，而非 double
   double B;   // 错误，重声明模板参数 B
}
```

模板声明必须包含模板参数，声明中的模板参数的名字不必与定义中相同。

```
template <typename T> class Blob;  // 声明但不定义
```

#### 16.1.3.1 使用类的类型成员

假定 T 是一个模板类型参数，当编译器遇到类似 T::mem 这样的代码时，它不知道 mem 是一个类型成员还是一个`static`数据成员，直至实例化时才会知道。

但是为了处理模板，编译器必须知道名字是否表示一个类型。例如：`T::size_type * p;`。编译器需要知道我们是在定义一个名为 p 的变量还是将一个名为 size_type 的`static`数据成员与名为 p 的变量相乘。

默认情况，C++ 语言假定通过作用域运算符访问的名字不是类型。因此，如果我们希望使用一个模板类型参数的类型成员，就必须显式告诉编译器该名字是一个类型。

我们通过使用关键字`typename`来实现这一点：

```
template <typename T>
typename T::value_type top(const T& c)
{
	if (!c.empty())
		return c.back();
	else
		return typename T::value_type();
}
```

#### 16.1.3.2 默认模板实参

在新标准中，我们可以为函数和类模板提供默认实参。而更早的 C++ 标准只允许为类模板提供默认实参。

```
//compare有一个默认模板实参 less<T> 和一个默认函数实参 F()
template <typename T, typename F = less<T>>
int compare(const T &v1, const T &b2, F f = F())
{
	if (f(v1, v2)) return -1;
	if (f(v2, v1)) return 1;
	return 0;
}
```

如果一个类模板为其所有模板参数都提供了模板实参，且我们希望使用这些默认实参，就必须在模板名之后跟一个空尖括号对。

### 16.1.4 成员模板

一个类可以包含本身是模板的成员函数。这种成员被称为成员模板（member template）。成员模板不能是虚函数（Member template functions cannot be declared virtual.Current compiler technology experts to be able to determine the size of a class’s virtual function table when the class is parsed.Allowing virtual member template functions woule require knowing all calls to such member functions everywhere in the program ahead of time.This is not feasible,especially for multi-file projects.）

#### 16.1.4.1 普通（非模板）类的成员模板

我们定义一个类，类似`unique_ptr`所使用的默认删除器类型：

```
//函数对象类，对给定指针执行 delete
class DebugDelete {
public:
	DebugDelete(std::ostream &s = std::cerr) : os(s) {}
	//与任何函数模板相同，T 的类型由编译器推断
	template <typename T> void operator()(T *p) const
	{ os << "deleting unqiue_ptr" << std::endl; delete p; }
private:
	std::ostream &os;
};
```

我们可以用这个类代替`delete`：

```
double *p = new double;
DebugDelete d;	//可像 delete 表达式一样使用的对象
d(p);	//调用 DebugDelete::operator()(double*),释放 p
int* ip = new int;
//在一个临时 DebugDelete 对象上调用 operator()(int*)
DebugDelete()(ip);
```

#### 16.1.4.2 类模板的成员模板

在此情况下，类和成员各有自己的独立的模板参数。例如，我们将 Blob 类定义一个构造函数，它接受两个迭代器，表示要拷贝的元素范围，我们希望支持不同类型序列的迭代器：

```
template <typename T>
class Blob {
	template <typename It> Blob(It b, It e);
	//...
};
```

当我们在类模板外定义一个成员模板时，必须同时为类模板和成员模板提供模板参数列表。类模板的参数列表在前，后跟成员自己的模板参数列表：

```
template <typename T>
template <typename It>
	Blob<T>::Blob(It b, It e) :
		data(std::make_shared<std::vector<T>(b,e)) {}
```

#### 16.1.4.3 实例化成员模板

为了实例化一个类模板的成员模板，我们必须同时提供类和函数模板的实参：

```
int ia[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
vector<long> vi = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
list<const char*> w = {"now", "is", "the", "time"};
//实例化 Blob<int> 类及其接受两个 int* 参数的构造函数
Blob<int> a1(begin(ia), end(ia));
```

### 16.1.5 控制实例化

模板被使用时才会进行实例化，这意味着，当两个或多个独立编译的源文件使用了相同的模板，并提供了相同的模板参数时，每个文件中就都会有该模板的一个实例。

相同的实例可能出现在多个对象文件中，在多个文件中实例化相同模板的额外开销可能非常大。在新标准中，我们可以通过显示实例化（explicit instantiation）来避免这种开销。

形式：

```
extern template declaration;        //实例化声明
template declaration;        //实例化定义
```

declaration 是一个类或函数声明，其中所有模板参数已被替换为模板实参，例如：

```
//实例化声明与定义
extern template class Blob<string>;	//声明
template int compare(const int&, const int&);	//定义
```

当编译器遇到`extern`模板声明时，它不会在本文件中生成实例代码。将一个实例化声明为`extern`就表示承诺在程序其他位置有该实例化的一个非`extern`声明（定义）。对于一个给定的实例化版本，可能有多个`extern`声明，但必须只有一个定义。

由于编译器在使用一个模板时自动对其实例化，因此`extern`声明必须出现在任何使用此实例化版本的代码之前：

```
// Application.cc
// 这些模板类型必须在程序其它位置进行实例化
extern template class Blob<string>;
extern template int compare(const int&, const int&);
Blob<string> sa1, sa2;  // 实例化会出现在其他位置
// Blob<int>及其接受 initializer_list 的构造函数在本文件中实例化
Blob<int> a1 = {0, 1, 2, 3, 4};
Blob<int> a2(a1);  // 拷贝构造函数在本文件中实例化
int i = compare(a1[0], a2[0]);  // 实例化出现在其他位置
// templateBuild.cc
// 实例化文件必须为每个在其他文件中声明为 extern 的类型和函数提供一个（非 extern）的定义
template int compare(const int&, const int&);
template class Blob<string>;
```

与类模板的普通实例化不同，类模板的显式实例化定义会实例化该模板的所有成员。因此，用来显示实例化一个类模板的类型，必须能用于模板的所有成员。

### 16.1.6 效率与灵活性

对模板设计者所面对的设计选择，标准库智能指针类型给出了一个很好的展示。

`shared_ptr`和`unique_ptr`之间的明显不同是它们管理所保存的指针的策略——前者给予我们共享指针所有权的能力；后置则独占指针。

这两个类的另一差异是它们允许用户重载默认删除器的方式：我们可以很容器地重载一个`shared_ptr`的删除器，只要在创建或`reset`指针时传递给他一个可调用对象即可；与之相反，删除器类型是`unique_ptr`对象类型的一部分，用户必须在定义`unique_ptr`时以显示模板实参的形式提供删除器的类型。


#### 16.1.6.1 在运行时绑定删除器（shared_ptr）

虽然我们不知道标准库类型是如何实现的，但可以推断出，`shared_ptr`必须能直接访问其删除器。即删除器必须保存为一个指针或封装了指针的类。

我们可以确定`shared_ptr`不是将删除器直接保存为一个成员，因为删除器的类型运行时才会知道。

#### 16.1.6.2 在编译时绑定删除器（unique_ptr）

现在，让我来考察`unique_ptr`可能的工作方式：

在这个类中，删除器的类型是类类型的一部分。即`unique_ptr`有两个模板参数，一个表示它所管理的指针，另一个表示删除器的类型。

由于删除器类型是`unique_ptr`的一部分，因此删除器成员的类型在编译时是知道的，从而删除器可以直接保存在`unique_ptr`对象中。

总结：通过在编译时绑定删除器，`unique_ptr`避免了间接调用删除器的运行时开销。通过在运行时绑定删除器，`shared_ptr`使用户重载删除器更为方便。

## 16.2 模板实参推断

我们已经看到，对于函数模板，编译器利用调用中的函数实参来确定其模板实参。从函数实参来确定模板实参的过程被称为模板实参推断（template argument deduction）。

### 16.2.1 类型转换与模板类型参数

只有很有限的几种类型转换会自动地应用于模板实参，编译器通常不是对实参进行类型转换，而是生成一个新的模板实例：

- 顶层`const`，无论是在形参还是实参中，都会被忽略
- `const`转换，可以将一个非`const`对象的引用（或指针）传递给一个`const`的引用（或指针）形参
- 数组或函数指针转换：如果函数形参不是引用类型，则可以对数组或函数类型的实参应用正常的指针转换
- 其他类型转换，如算术转换，派生类向基类转换以及用户定义的转换都不能应用于函数模板

```
template <typename T>
T fobj(T, T);	//实参被拷贝
template <typename T>
T fref(const T&, const T&);	//引用捕获方式；c 显示捕获，值捕获方式
string s1("a value");
const string s2("another value");
fobj(s1, s2);	//调用 fobj(string, string);const 被忽略
fref(s1, s2);	//调用 fref(const string&, const string&),将 s1 转换为 const 是允许的

int a[10], b[42];
fobj(a, b);	//调用 f(int*, int*)
fref(a, b);	//错误：数组类型不匹配
```

**将实参传递给带模板类型的函数形参时，能够自动应用的类型转换只有`const`转换以及数组或函数到指针的转换。**

#### 正常类型转换应用于普通函数实参

函数模板可以有用普通类型定义的参数，即，不涉及模板类型参数的类型。这种函数实参不进行特殊处理；它们正常转换为对应形参的类型。例如：

```
template <typename T>
ostream &print(ostream &os, const T &obj)
{
	return os << obj;
}
//第一个函数参数是一个已知类型 ostream&。第二个参数 obj 则是模板参数类型
//由于 os 的类型是固定的，因此当调用 print 时，传递给它的实参会进行正常的
//类型转换
print(const , 42);	//实例化 print(ostream&, int)
ofstream f("output");
print(f, 10);	//使用 print(ostream&, int);将 f 转换为 ostream&
```

**如果函数参数类型不是模板参数，则对实参进行正常的类型转换。**

### 16.2.2 函数模板显式实参

在某些情况下，编译器无法推断出模板实参的类型。其他一些情况下，我们希望允许用户控制模板实例化。

#### 16.2.2.1 指定显式模板实参

```
//编译器无法推断 T1，它未出现在函数参数列表中
template <typename T1, typename T2, typename T3>
T1 sum(T2, T3);
```

本例中，没有任何函数实参的类型可用来推断 T1 的类型。每次调用 sum 时调用者都必须为 T1 提供一个显式模板实参（explicit template argument）。如下：

```
//T1 是显示指定的，T2 和 T3 是从函数实参类型推断而来的
auto val3 = sum<long long>(i, lng);	//long long sum(int, long)
```

显示模板实参按由左至右的顺序与对应的模板参数匹配。推断不出的模板参数的类型在定义时应该放在参数列表的最左边。

#### 16.2.2.2 正常类型转换应用于普通函数实参

对于模板类型参数已经显式指定了的函数实参，可以进行正常的类型转换。

```
long lng;
compare(lng, 1024);           // 错误，模板参数不匹配
compare<long>(lng, 1024);     // 正确，1024自动转化为 long
```

### 16.2.3 尾置返回类型与类型转换

例如，我们可能希望编写一个函数，接受表示序列的一对迭代器和返回序列中一个元素的引用。但是，我们并不知道返回结果的准确类型，但知道所需类型是处理的序列的元素类型。由于尾置返回出现在参数列表之后，它可以使用函数的参数：

```
//尾置返回允许我们在参数列表之后声明返回类型
template <typename It>
auto fcn(It beg, It end) -> decltype(*beg)
{
	//处理序列
	return *beg;	//返回序列中一个元素的引用
}
```

#### 使用类型转换的标准库模板类

为了获取元素类型，我们可以使用标准库的类型转换（type transformation）模板。这些模板定义在头文件`type_traits`中。这个头文件的类通常用于模板元编程设计。

```
// 返回一个序列中的元素值
// 为了使用模板参数的类型成员，必须使用 typename
template <typename It>
auto fcn(It beg, It end) ->
   typename remove_reference<decltype(*beg)>::type;
{
   // 处理序列
   return *beg;
}
```

![标准类型转换模板]({filename}/images/c++16-1.jpg)

### 16.2.4 函数指针和实参推断

使用函数模板初始化一个函数指针或为一个函数指针赋值时，编译器使用指针的类型来推断模板实参。如果不能从函数指针类型确定模板实参，则产生错误。

```
template <typename T> int compare(const T&, const T&);
// func 的重载版本，每个版本接受一个不同的函数指针类型
void func(int(*)(const string&, const string&));
void func(int(*)(const int&, const int&));
func(compare);   // 错误，不能确定使用哪一个实例
// 正确的做法是可以显式指出实例化哪个版本
func(compare<int>);
```

### 16.2.5 模板实参推断和引用

![模板实参推断和引用]({filename}/images/c++16-2.jpg)

![模板实参推断和引用]({filename}/images/c++16-3.jpg)

![模板实参推断和引用]({filename}/images/c++16-4.jpg)


#### 16.2.5.1 从左值引用函数参数推断类型

`template <typename T> void f(T &p)`：实参必须是一个左值。如果实参是`const`的，则 T 将被推断为`const`类型。

`template <typename T> void f(const T &p)`：实参可以是任意类型(包括右值在内)，即使实参是`const`的，T 的推断类型也不会是一个`const`类型。

#### 16.2.5.2 从右值引用函数参数推断类型

传递的实参为右值。推断出的 T 的类型是该右值实参的类型。

传递的实参为左值。此时得到的模板参数和函数参数都是左值引用。

对于接受右值引用参数的模板函数，当分别传递右值和左值实参时，模板参数类型可能是普通类型，也可能是引用类型。有时这可能会造成意想不到的结果。解决这种问题的办法是，使用基于函数参数的模板重载，来将实参分别为右值或左值时的情况分离开来：

```
template <typename T> void f3(T&&)
{
   T t = val;    // 实参为右值时，赋值语句
                 // 实参为左值时，绑定引用
   t = fcn(t);   // 实参为右值时，只改变 t
                 // 实参为左值时，既改变 t，也改变 val
}
// 定义一组重载函数，解决上述问题
template <typename T> void f(T&&);         // 绑定到非 const 右值
template <typename T> void f(const T&);    // 绑定到左值和 const 右值
```

### 16.2.6 理解 std::move

由于`move`本质上可以接受任何类型的实参，因此我们不会惊讶于它是一个函数模板。

标准库是这样定义`move`的：

```
//在返回类型和类型转换中也要用到 typename
template <typename T>
typename remove_reference<T>::type&& move(T&& t)
{
    //特例：可以使用 static_cast 显式地将左值转换为右值
    return static_cast<typename remove_reference<T>::type&&>(t);
}
```

### 16.2.7 转发

某些函数需要将其一个或多个实参连同类型不变地转发给其它参数，需要保持转发实参的所有性质，包括实参类型是否是`const`的以及实参是左值还是右值。

```
// 该模板将两个额外参数逆序传递给指定的可调用对象
template<typename F, typename T1, typename T2>
   void flip1(F f, T1 t1, T2 t2)
{
   f(t2, t1);
}
// flip1 一般情况下工作的很好，但是当用它调用一个接受引用参数的函数时会出现问题
void f(int v1, int &v2)
{
    cout << v1 << " " << ++v2 << endl;
}
f(42, i);        // f 改变了实参 i
flip1(f, j, 42)  // j 的值不会改变
```

如果一个函数参数是指向模板类型参数的右值引用（如 T&&），它对应的实参的`const`属性和左值/右值属性将得到保持。使用这种方案改写上面的 flip1 函数。

```
// 该模板将两个额外参数逆序传递给指定的可调用对象
template<typename F, typename T1, typename T2>
   void flip2(F f, T1 &&t1, T2 &&t2)
{
   f(t2, t1);
}
// flip2 对接受左值引用函数工作的很好，但不能用于接受右值引用的函数
void g(int &&v1, int &v2)
{
    cout << v1 << " " << v2 << endl;
}
g(42, i);        // 正确
flip1(g, i, 42)  // 错误，g 中接收到的 “42” 是左值
```

当我们试图通过 flip2 调用 g，则参数 t2 将被传递给 g 的右值引用参数（即使我们传递一个右值给 filp2，也会被拷贝到 t2）。函数参数是左值表达式，不能用于实例化右值。

当用于一个指向模板参数类型的右值引用函数（T&&）时，`forward`会保持实参类型的所有细节。与`move`不同，`forward`必须通过显式模板实参来调用。`forward`也定义在`utility`头文件中。下面使用`forward`重写翻转函数：

```
template<typename F, typename T1, typename T2>
void flip3(F f, T1 &&t1, T2 &&t2)
{
    f( std::forward<T2>(t2), std::forward<T1>(t1) );
}
```

## 16.3 重载与模板

函数模板可以被另一个模板或一个普通非函数模板重载，与往常一样，名字相同的函数，必须具有不同数量或类型的参数。如果涉及函数模板，则函数匹配规则会在以下几个方面受到影响:

- 对于一个调用，其候选函数包括所有模板实参推断成功的函数模板实例
- 候选的函数模板总是可行的，因为模板实参推断会排除任何不可行的模板
- 与往常一样，可行函数（模板与非模板）按类型转换（如果对此调用需要的话）来排序。当然，可以用于函数模板调用的类型转换是非常有限的（参考前文）
- 与往常一样，如果恰有一个函数提供比任何其他函数都更好的匹配，则选择此函数。但是如果有多个函数提供同样好的匹配，则：（1）如果同样好的函数中只有一个是非模板函数，则选择此函数；（2）如果同样好的函数中没有非模板函数，而有多个函数模板，且其中一个模板比其它模板更特例化则选择此模板；（3）否则，此调用有歧义

```
// 通用模板，返回 T 型对象 t 的 string 表示
template <typename T>
string debug_rep(const T &t)
{
    std::ostringstream ret;
    ret << t;
    return ret.str();
}
// 通用模板，返回 T 型指针 p 的 string 表示
template <typename T>
string debug_rep(T *p)
{
    std::ostringstream ret;
    // 打印指针本身的值
    ret << "pointer: " << p;
    // p不为空，则打印 p指向的值
    if (p)
        ret << " " << debug_rep(*p);
    else
        ret << " null pointer";
    return ret.str();
}
// 对于下面的代码调用，只会使用第一个模板
string s("hi");
cout << debug_rep(s) << endl;
// 对于下面的代码调用，最终会调用第二个模板
cout << debug_rep(&s) << endl;
// 对于下面的代码调用，最终会调用第二个模板
const string *sp = "hi";
cout << debug_rep(sp) << endl;
// 再定义一个普通非模板函数，打印双引号包围的 string
string debug_rep(const string &s)
{
    cout << '"' + s + '"';
}
// 对于下面的代码调用，会使用普通非模板函数
cout << debug_rep(s) << endl;
// 对于下面的代码调用，最终会调用第二个模板
cout << debug_rep("hi") << endl;
```

对于第一个模板参数`const T &t`，当实例化`string *`参数时，模板参数是`string *`，而函数参数是`string * const &t`，表示 t 是引用，引用自`string`型指针（本身是常量）。在进行模板实参推断之后会进行普通函数的函数匹配过程。而 `string * const &t`中的顶层`const`属性也会被略去，即`f(string * const &t)和 f(string *t)`存在二义性。此时后者更特例化，所以编译器实际执行的是后者。

对于第一个模板参数`const T &t`，当实例化`const string *`参数时，模板参数是`const string *`，而函数参数是 `const string * const &t`，表示 t 是引用，引用自`string`型指针（指向常量，且本身是常量）。所以，同样地，`f(const string * const &t)和 f(const string *t)`存在二义性。此时后者更特例化，所以编译器实际执行的是后者。

对于第一个模板，T 的类型为`char[3]`；对于第二个模板，T 的类型是`const char`；对于普通非模板函数，要求从`const char*`到`string`的类型转换。此时，3个候选函数都是可行的。普通函数由于需要进行类型转换，可以首先排除掉。而剩下两个模板函数，后者更特例化，所以编译器实际执行的是后者。

在定义任何函数之前，记得声明所有重载的函数版本。这样就不必担心编译器由于未遇到你希望调用的函数，而实例化一个并非你所需的版本:

```
template <typename T> string debug_rep(const T &t);
template <typename T> string debug_rep(T *p);
// 为了使 debug_rep(char*) 的定义正确工作，下面的声明必须在作用域中
string debug_rep(const string &);
string debug_rep(char *p)
{
   // 如果接受一个 const string&的版本的声明不在作用域中，
   // 返回语句将调用 debug_rep(const T &t) 的 T 实例化为 string 的版本
   return debug_rep(string(p));
}
```

## 16.4 可变参数模板

一个可变参数模板（variadic template）就是一个接受可变数目参数的模板函数或模板类。可变数目的参数被称为参数包（parameter packet）。存在两种参数包：模板参数包，函数参数包。

在一个模板参数列表中，`class...`或`typename...`指出，接下来的参数表是零个或多个类型的列表；一个类型名后面跟一个省略号表示零个或多个给定类型的非类型参数的列表。在函数参数列表中，如果一个参数的类型是一个模板参数包，则此参数也是一个函数参数包。

```
// Args 是一个模板参数包； rest 是一个函数参数包
// Args 表示零个或多个模板类型参数
// rest 表示零个或多个函数参数
template <typename T, typename... Args>
void foo(const T &t, const Args& ... rest);
// 对于下面调用
int i = 0;
foo(i, "hi");  // 包中有一个参数，实例化为 foo(const int &, const char[3]&);
foo("hi");     // 空包，实例化为 foo(const char[3]&);
```

`sizeof...`运算符可以返回一个常量表达式，表示包中的元素个数，而且不会对其实参求值：

```
template<typename... Args> void g(Args... args) {
   cout << sizeof...(Args) << endl;  // 类型参数的数目
   cout << sizeof...(args) << endl;  // 类型参数的数目
}
```

### 16.4.1 编写可变参数函数模板

`initializer_list`用来表示一组类型相同的可变数目参数，而当类型也是未知时，则需要使用可变参数函数模板。可变参数函数通常是递归的，第一步调用处理包中的第一个实参，然后用剩余实参调用自身。

```
// 用来终止递归并打印最后一个元素的函数
// 此函数必须在可变参数版本的 print 定义之前声明
template<typename T>
ostream& print(ostream &os, const T &t)
{
   return os << t;  // 包中最后一个元素之后不打印分隔符
}
// 包中除了最后一个元素之外的其他元素都会调用这个版本的 print
template<typename T, typename... Args>
ostream& print(ostream &os, const T &t, const Args&... rest)
{
   os << t << ", "; // 打印第一个实参
   return print(os, rest...);  // 递归调用，打印其他实参
}
```

给定 print(cout, i, s, 42)，其调用过程如下：

![编写可变参数函数模板]({filename}/images/c++16-5.jpg)

对于最后一次递归调用 print(cout, 42)，两个 print 版本都是可行的。但是因为非可变参数模板比可变参数模板更特例化，因此编译器选择非可变参数版本。另外，定义可变参数版本的 print 时，非可变参数版本的声明必须在作用域中，否则，可变参数版本会无限递归。

### 16.4.2 包扩展

当扩展一个包时，可以提供用于每个扩展元素的模式。扩展一个包就是将它分解为构成的元素，对每个元素应用模式，获得扩展后的列表。通过在模式右边放一个省略号（...）来触发扩展操作。

```
template<typename T, typename... Args>
ostream& print(ostream &os, const T &t, const Args&... rest)  // 扩展 Args
{
   os << t << ", ";
   return print(os, rest...);                                 // 扩展 rest
}
// 对 Args 的扩展中，将模式 const Arg& 应用到模板参数包 Args 中的每个元素
print(cout, i, s, 42);
// 实例化的形式为
ostream&
print(ostream &, const int&, const string&, const int&);
```

print 中的函数参数包扩展仅仅将包扩展为其构成元素，还可以进行更复杂的扩展模式。比如，对其每个实参调用之前出现过的  debug_rep：

```
template<typename... Args>
ostream& errorMsg(ostream &os, const Args&... rest)
{
   print(os, debug_rep(rest)...);
   // 上式等价于
   print(os, debug_rep(a1), debug_rep(a2), ..., debug_rep(a3));
   // 注意，不可以写成下式形式
   print(os, debug_rep(rest...));  // 错误，此调用无匹配函数
   return os;
}
```

扩展中的模式会独立地应用于包中的每个元素。

### 16.4.3 转发参数包

可变参数函数通常将它们的参数转发给其他函数，这种函数具有与容器中的`emplace_back`函数一样的形式。work 调用中的扩展既扩展了模板参数包也扩展了函数参数包：

```
// fun 有零个或多个参数，每个参数都是一个模板参数类型的右值引用
template<typename... Args>
void fun(Args&&... args)  // 将 Args 扩展为一个右值引用的列表
{
   // work的实参既扩展 Args又扩展 args
   work( std::forward<Args>(args)... );
}
```

## 16.5 模板特例化

在某些情况下，通用模板的定义可能编译失败、做的不正确，或者利用特定知识来编写更高效的代码，而不是从通用模板实例化。这时可以定义类或函数模板的一个特例化版本。

当我们特例化一个函数模板时，必须为元模板中的每个模板参数都提供实参。为了指出我们正在实例化一个模板，应使用关键字 `template`后跟一个空尖括号对（<>）。空尖括号指出我们将为原模板的所有模板参数提供实参。

```
// 第一个版本，可以比较任意两个类型
template <typename T>
int compare(const T&, const T&);
// 第二个版本，处理字符串字面常量
template <size_t N, size_t M>
int compare(const cahr (&p1)[N], const cahr (&p2)[M]);
const char *p1 = "hi", *p2 = "mom";
compare(p1, p2);          // 调用第一个版本
compare("hi", "mom");     // 调用第二个版本
// compare 的特例化版本，处理字符数组的指针
template <>
int compare(const char* const &p1, const char* const &p2)
{
    return strcmp(p1, p2);
}
// 参数类型为指针，不能调用第二个版本，这里调用的是特例化版本
compare(p1, p2);
```

我们希望定义此函数的一个特例化版本，其中 T 的类型为`const char *`。我们的函数要求一个指向此类型的`const`版本的引用。所以 p1 是一个指向`const char`的`const`指针的引用。

### 16.5.1 函数重载与模板特例化

当定义函数模板的特例化版本时，我们本质上接管了编译器的工作，一个特例化版本本质上是一个实例，而非函数名的一个重载版本。因此，特例化不影响函数匹配。

模板及其特例化版本应该声明在同一个头文件中。所有同名模板的声明应该放在前面，然后是这些模板的特例化版本。

### 16.5.2 类模板特例化

作为例子，这里为 Sales_data 类定义特例化版本的`hash`模板。而定义了`hash`模板的特例化版本的类类型，可以存储在无序容器中。为了让 Sales_data 类的用户能使用`hash`的特例化版本，应该在 Sales_data 的头文件中定义该特例化版本。一个特例化`hash`类必须定义：

- 一个重载的调用运算符，它接受一个容器关键字类型的对象，返回一个`size_t`
- 两个类型成员，`result_type`和`argument_type`，分别表示调用运算符的返回类型和参数类型
- 默认构造函数和拷贝赋值运算符（可以隐式定义）

```
template <typename T> struct std::hash;
class Sales_data
{
   friend struct std::hash<Sales_data>;
   // 其它数据成员
};
// 为了使 Sales_data 能存储在无序容器中，特例化 hash 模板
// 注意， Sales_data 类应支持 == 操作
namespace std {
    template <>
    struct hash<Sales_data>
    {
        typedef size_t result_type;
        typedef Sales_data argument_type;
        size_t operator()(const Sales_data &s) const;
    };
    inline size_t
    hash<Sales_data>::operator()(const Sales_data & s) const
    {
        std::cout << "hash模板的 Sales_data特例化版本" << std::endl;
        return hash<string>()(s.bookNo) ^
            hash<unsigned>()(s.units_sold) ^
            hash<double>()(s.revenue);
    }
}
```

### 16.5.3 类模板部分特例化

可以指定一部分而非所有模板参数，或是参数的一部分而非全部特性。一个类模板的部分特例化本身是一个模板，使用它时用户还必须为那些在特例化版本中未指定的模板参数提供实参。只能部分特例化类模板，而不能部分特例化函数模板。

### 16.5.4 特例化成员而不是类

```
template <typename T> struct Foo {
   Foo(cosnt T &t = T()) : men(t) {}
   void Bar() { /* ... */ }
   T men;
   // Foo 的其他成员
};
template<>                  // 表示正在特例化一个模板
void Foo<int>::Bar()        // 正在特例化 Foo<int> 的成员 Bar
{
   // 进行应用于 int的特例化处理
}
Foo<string> fs;        // 实例化 Foo<string>::Foo()
fs.Bar();              // 实例化 Foo<string>::Bar()
Foo<int> fi;           // 实例化 Foo<int>::Foo()
fi.Bar();              // 使用特例化版本的 Foo<int>::Bar()
```
