Title: C++ Primer 第十六章 模板与泛型编程
Category: 读书笔记
Date: 2018-10-21 10:23:30
Modified: 2018-10-21 10:23:30
Tags: C++

面向对象编程（OOP）和泛型编程都能处理在编写程序时不知道类型的情况。不同之处是：OOP能处理类型在程序运行之前都未知的情况；而在泛型编程中，在编译时就能获知类型了。

容器、迭代器和算法都是泛型编程的例子。模板是 C++ 中泛型编程的基础。一个模板就是一个创建类或函数的蓝图或者说公式。

## 定义模板

### 函数模板

模板的定义以关键字`template`开始，后面跟一个模板参数列表，用`<>`括起来。

模板有类型参数（type parameter）和非类型参数（nontype parameter）之分。

#### 类型参数

我们可以将类型参数看作类型说明符，就像内置类型或类类型说明符一样使用。

类型参数可以用来指定返回类型或函数的参数类型，以及在函数体内用于变量声明或类型转换。

参数列表中，类型参数前必须使用关键字`class`或`typename`。在模板定义中，模板参数列表不能为空。

```
// 错误，U 之前必须加上 class 或 typename
template <typename T, U>
T calc(const T&, const U&);
```

#### 非类型参数

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

#### inline 和 constexpr 的函数模板

函数模板可以声明为`inline`或`constexpr`的，如同非模板函数一样。`inline`或`constexpr`说明符放在模板参数列表之后，返回类型之前：

```
//正确，inline 说明符跟在模板参数列表之后
template <typename T> inline T min(const T&, const T&);
//错误：inline 说明符的位置不正确
inline template <typename T> T min(const T&, const T&);
```

#### 编写类型无关的代码

为了提高适用性，模板程序应尽量减少对实参类型的要求。

模板中的函数参数是`const`的引用。这样做一方面保证了即使参数类型不支持拷贝，模板程序也能正确运行；另一方面引用不会引起对象的拷贝构造，提高运行性能。

模板中使用到的类型相关的函数或运算符应尽可能的少。

#### 模板编译

当编译器遇到一个模板定义时，它并不生成代码。只有当我们实例化出模板的一个特定版本时，编译器才会生成代码。

通常，当我们调用一个函数时，编译器只需要掌握函数的声明。类似的，当我们使用一个类类型的对象时，类定义必须是可用的，但成员函数的定义不必已经出现。因此，我们将类定义和函数声明放在头文件中，而普通函数和类的成员函数的定义放在源文件中。

为了生成一个实例化版本，编译器需要掌握函数模板或类模板成员函数的定义。因此，与非模板代码不同，模板不能分离式编译，其头文件中通常既包括声明也包括定义。

#### 大多数编译错误在实例化期间报告

模板直到实例化时才会生成代码，大多数编译错误在实例化期间报告。通常，编译器会在三个阶段报告错误。

第一个阶段是编译模板本身时。这个阶段，编译器可以检查语法错误，如忘记分号或者变量名拼错等。

第二个阶段是编译器遇到模板使用时。对于函数模板调用，会检查实参数目是否正确和参数类型是否匹配。对于类模板，则只检查模板实参数目是否正确。

第三个阶段是模板实例化时，只有这个阶段才能发现类型相关的错误。依赖于编译器如何管理实例化，这类错误可能在链接时才报告。

### 类模板

类模板（class template）是用来生成类的蓝图的。与函数模板的不同之处是，编译器不能为类模板推断模板参数类型。使用时，必须显式提供模板实参。

#### 定义类模板

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

#### 实例化模板

当使用一个类模板时，我们必须提供额外信息。我们现在知道这些额外信息是显式模板实参（explicit template argument）列表，它们被绑定到模板参数。例如：

```
Bolb<int> ia;	//空 Bolb<int>
Bolb<int> ia2 = {0,1,2,3,4};	//有5个元素的 Bolb<int>
```

一个类模板的每个实例都形成一个独立的类。Bolb<string> 与任何其他 Bolb 类型没有关联，也不会对任何其他 Bolb 类型的成员有特殊访问权限。

#### 类模板的成员函数

我们既可以在类模板内部，也可以在外部为其定义成员函数。定义在类模板之外的成员函数必须以关键字`template`开始，后接类模板参数列表。

默认情况下，一个类模板的成员函数只有当程序用到它时才进行实例化。这一特性使得即使某种类型不能完全符合模板操作的要求，仍然能用该类型实例化类，但相应操作无法使用！

#### 在类代码内简化模板类型的使用

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

#### 类模板和友元

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

#### 模板类型别名

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

#### 类模板的 static 成员

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

### 模板参数

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

#### 使用类的类型成员

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

#### 默认模板实参

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

### 成员模板

一个类可以包含本身是模板的成员函数。这种成员被称为成员模板（member template）。成员模板不能是虚函数（Member template functions cannot be declared virtual.Current compiler technology experts to be able to determine the size of a class’s virtual function table when the class is parsed.Allowing virtual member template functions woule require knowing all calls to such member functions everywhere in the program ahead of time.This is not feasible,especially for multi-file projects.）

#### 普通（非模板）类的成员模板

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

#### 类模板的成员模板

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

#### 实例化成员模板

为了实例化一个类模板的成员模板，我们必须同时提供类和函数模板的实参：

```
int ia[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
vector<long> vi = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
list<const char*> w = {"now", "is", "the", "time"};
//实例化 Blob<int> 类及其接受两个 int* 参数的构造函数
Blob<int> a1(begin(ia), end(ia));
```

### 控制实例化

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

### 效率与灵活性

...
