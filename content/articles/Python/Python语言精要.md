Title: Python 语言精要
Category: 读书笔记
Date: 2018-11-14 12:32:08
Modified: 2018-11-14 12:32:08
Tags: Python

## 1. 基础知识

- 缩进，而不是大括号
- Python 语句还能不依分号结束，不过分号也是可以有的，如
    ```
    a = 5; b = 6; c = 7
    ```
- 万物皆对象
    - Python 解释器中的任何数值、字符串、数据结构、函数、类、模块等都待在自己的“盒子”里，而这个”盒子”就是 Python 对象
    - 每个对象都有一个与之相关的类型（比如字符串和函数）以及内部数据
- 变量和按引用传递
    - 列表和元组的赋值皆为引用
    - 若想拷贝，则利用切片
    ```
    >>> a = [1, 2, 3]
    >>> b = a[:] #拷贝
    >>> c = a #引用
    ```
    - 切片只能赋值第一层列表，若列表中还包含列表，则内部列表仍为引用。元组内的列表也是。
        ```
        >>> a = [1, 2, [3, 4, 5], 6]
        >>> a
        [1, 2, [3, 4, 5], 6]
        >>> b=a[:]
        >>> b
        [1, 2, [3, 4, 5], 6]
        >>> b.append(7)
        >>> b
        [1, 2, [3, 4, 5], 6, 7]
        >>> a
        [1, 2, [3, 4, 5], 6]
        >>> b[2].append(6)
        >>> b
        [1, 2, [3, 4, 5, 6], 6, 7]
        >>> a
        [1, 2, [3, 4, 5, 6], 6]
        ```
    - 当你将对象以参数的形式传入函数时，其实只是传入一个引用而已
- 跟许多编译型语言（如 Java 和 C++）相反，Python 中的对象引用没有与之关联的类型信息。下面这些代码不会有什么问题。对象的类型信息是保存在它自己内部的
    ```
    >>> a = 5
    >>> type(a)
    <class 'int'>
    >>> a = 'foo'
    >>> type(a)
    <class 'str'>
    ```
- Python 可以别认为是一种强类型语言，所有对象都有一个特定的类型（或类），隐式转换只在很明显的情况下才会发生，例如浮点转化为整数参与相加运算，而字符串则不行
- isinstance 函数检查一个对象是否是某个特定类型的的实例
    ```
    >>> a = 5
    >>> isinstance(a,int)
    True
    ```
    isinstance 可以接受由类型组成的元组
    ```
    >>> a = 5; b = 4.5
    >>> isinstance(a, (int, float))
    True
    ```
- 属性和方法(. + tab 键)
    ```
    >>> a = 5
    >>> a.
    a.__abs__(           a.__format__(        a.__mul__(           a.__rlshift__(       a.__sub__(
    a.__add__(           a.__ge__(            a.__ne__(            a.__rmod__(          a.__subclasshook__(
    a.__and__(           a.__getattribute__(  a.__neg__(           a.__rmul__(          a.__truediv__(
    a.__bool__(          a.__getnewargs__(    a.__new__(           a.__ror__(           a.__trunc__(
    a.__ceil__(          a.__gt__(            a.__or__(            a.__round__(         a.__xor__(
    a.__class__(         a.__hash__(          a.__pos__(           a.__rpow__(          a.bit_length(
    a.__delattr__(       a.__index__(         a.__pow__(           a.__rrshift__(       a.conjugate(
    a.__dir__(           a.__init__(          a.__radd__(          a.__rshift__(        a.denominator
    a.__divmod__(        a.__int__(           a.__rand__(          a.__rsub__(          a.from_bytes(
    a.__doc__            a.__invert__(        a.__rdivmod__(       a.__rtruediv__(      a.imag
    a.__eq__(            a.__le__(            a.__reduce__(        a.__rxor__(          a.numerator
    a.__float__(         a.__lshift__(        a.__reduce_ex__(     a.__setattr__(       a.real
    a.__floor__(         a.__lt__(            a.__repr__(          a.__sizeof__(        a.to_bytes(
    a.__floordiv__(      a.__mod__(           a.__rfloordiv__(     a.__str__(
    ```
    getattr、hasattr 和 setattr 函数也很实用
- 是否可以迭代
    - 验证
        ```
        def isiterable(obj):
                try:
                    iter(obj)
                    return True
                except TypeError:
                    return False
        ```
    - 转换
        ```
        if not isinstance(x, list) and isiterable(x):
                x = list(x)
        ```
- 要判断两个引用是否指向同一个对象，可以用 is 和 is not 关键字
    ```
    >>> a = [1, 2, 3]
    >>> b = a
    >>> c = list(a) #list 函数始终会创建新列表
    >>> a is b
    True
    >>> a is c
    False
    >>> a == c
    True
    ```
- is 和 is not 常常用于判断变量是否为 None，因为 None 的实例只有一个
    ```
    >>> a = None
    >>> a is None
    True
    ```
- 二元运算符

    | 运算 | 说明 |
    | :---| :---|
    | a + b |     |
    | a - b |     |
    | a * b |     |
    | a / b |     |
    | a // b|丢弃小数|
    | a ** b|a 的 b 次方|
    | a & b |与，整数位与|
    | a \| b |或，整数位或|
    | a ^ b |异或，整数位异或|
    | a == b, a != b, a <= b, a < b, a >= b, a > b | |
    | a *is* b, a *is not* b| |
- 在 Python 中，求值会立刻发生，而不是用到的时候计算，有一些技术可以实现延迟计算
- 字符串和元组是不可变的
- 标量类型

    | 类型 | 说明   |
    | :------------- | :------------- |
    | None |    |
    | str| |
    |unicode|Unicode 字符串类型|
    |float|双精度（64 位）浮点数。注意，没有 double |
    |bool| |
    |int |有符号整数，其最大值由平台决定 |
    |long|任意精度的有符号整数。大的 int 值会被自动转换为 long|
- 虚数单位用 j 表示
- 对于带有换行的多行字符串，可以用三重引号
- Python 的字符串是不可变的，想修改只能创建一个新的
- list(str)
- r"..."
- 字符串格式化
    ```
    >>> template = '%.2f %s are worth $%d'
    >>> template % (4.5560, 'Argentine Pesos', 1)
    '4.56 Argentine Pesos are worth $1'
    ```
- 几乎所有 Python 内置类型以及任何定义了 \_\_nonzero\_\_ 方法的类都能在 if 语句中被解释为 True 和 False。可用 bool( )函数测试。
- 类型转换：str( )、 bool( )、 int( )、 float( )等
- None 不是一个保留字，它只是 NoneType 的一个实例
- 时间和日期
    ```
    >>> from datetime import datetime, date, time
    >>> dt = datetime(2018, 4, 5, 14, 1, 23)
    >>> dt.strftime('%m/%d/%Y %H:%M')
    '04/05/2018 14:01'
    >>> datetime.strptime('20180401','%Y%m%d')
    datetime.datetime(2018, 4, 1, 0, 0)
    >>> dt.replace(minute=0, second=0)
    datetime.datetime(2018, 4, 5, 14, 0)
    ```
    两个 datetime 对象的差会产生一个 datetime.timedelta 对象。datetime.timedelta 加到一个 datetime 上会产生一个新的 datetime

## 2. 控制流

- if、elif 和 else
```
if x < 0:
        print("It's negative")
elif x == 0:
        print("Equal to zero")
elif 0 < x < 5:
        print("Positive but smaller than 5")
else:
        print("Positive and larger than or equal to 5")
```
- for
```
for value in collection:
        #操作
```
- break、continue 和 pass
- while
- 异常处理
    - 把可能发生异常的语句放在 try/except 块中
    - except 后面可不跟参数表示捕获所有异常，或者跟一个异常元组
    - finally 用于不管 try 成功与否都能被执行
    - 你也可以让某些代码只在 try 块成功时执行，使用 else 即可
    ```
    f = open(path, 'w')
    try:
            write_to_file(f)
    except:
            print('Failed')
    else:
            print('Succeeded')
    finally:
            f.close()
    ```
- range 产生序列,不包括结束值
```
range(起始，结束，步长)
```
- 三元表达式
```
>>> a = 5
>>> 'Non-negative' if a >= 0 else 'Negative'
'Non-negative'
```

## 3. 数据结构和序列

- 元组
    - 元组（tuple）是一种一维的、定长的、不可变的 Python 对象序列
    -  逗号分隔
    ```
    >>> tup = 4, 5, 6
    >>> tup
    (4, 5, 6)
    ```
    - tuple 函数可将任何序列或迭代器转换为元组
    ```
    >>> tup = 4, 5, 6
    >>> tup
    (4, 5, 6)
    >>> tuple([1, 2, 3])
    (1, 2, 3)
    >>> tup = tuple('xushu')
    >>> tup
    ('x', 'u', 's', 'h', 'u')
    ```
    - 用[ ] 索引，从 0 开始
    - 存储在元组中的对象本身可能是可变的，但一旦创建完毕，存放在各个插槽中的对象就不能再修改了
    - 元组可以通过 + 号运算符连接成更长的元组
    - 跟列表一样，对一个元组乘以一个整数，相当于连接该元组的多个副本
    ```
    >>> a=1, [2, 3, 4], 5
    >>> a
    (1, [2, 3, 4], 5)
    >>> b=a*3
    >>> b
    (1, [2, 3, 4], 5, 1, [2, 3, 4], 5, 1, [2, 3, 4], 5)
    >>> a[1].append(6)
    >>> a
    (1, [2, 3, 4, 6], 5)
    >>> b #注意 b 变了
    (1, [2, 3, 4, 6], 5, 1, [2, 3, 4, 6], 5, 1, [2, 3, 4, 6], 5)
    ```
    对象本身不会被复制，这里涉及到的是它们的引用
    - 元组拆包（unpacking）
    ```
    >>> tup = (4, 5, 6)
    >>> a, b, c = tup
    >>> b
    5
    >>> tup = 4, 5, (6, 7)
    >>> a, b, (c, d) = tup
    >>> d
    7
    ```
    交换变量名
    ```
    a, b = b, a
    ```
    变量拆包功能常用于对由元组或列表组成的序列进行迭代
    ```
    seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    for a, b, c in seq:
            pass
    ```
    另一种常见的用法是处理从函数返回的多个值
    - 元组方法：由于元组的大小和内存不能被修改，所以实例方法很少。最有用的是 count( )，它用于计算指定值出现的次数
    ```
    >>> tup
    (4, 5, [6, 7, 4])
    >>> tup.count([6,7,4])
    1
    ```
- 列表
    - 可变长，内容可修改
    - 通过[ ]或者 list 函数定义
    - 添加尾部：list.append(a)
    - 插入位置: list.insert(1,a)
    - 移除并返回指定索引的元素：b = list.pop(2)
    - 删除第一个符号要求的值：list.remove(a)
    - 是否在列表中：a in list
        - 注意：判断列表是否含有某个值的操作比字典（dict）和集合（set）慢得多，因为 python 会对列表进行线性扫描，而另外两个（基于哈希表）则可以瞬间完成判断
        - 散列表（Hash table，也叫哈希表），是根据键（Key）而直接访问在内存存储位置的数据结构。也就是说，它通过计算一个关于键值的函数，将所需查询的数据映射到表中一个位置来访问记录，这加快了查找速度。这个映射函数称做散列函数，存放记录的数组称做散列表
    - 一次添加多个元素：list.extend(a, b, c)
    - 合并列表：list + list
        - 注意：列表的合并是一种相当耗费资源的操作，需要新建列表并复制，而 extend 会好很多
        ```
        #高效
        everything = []
        for chunk in list_of_lists:
                everything.extend(chunk)
        #低效
        everything = []
        for chunk in list_of_lists:
                everything = everything + (chunk)
        ```
    - 就地排序：list.sort()
    - 按键就地排序：list.sort(key=len)
    - 二分搜索
        - 内置的 bisect 模块实现了二分搜索和插入操作
        - bisect.bisect 可以找出新元素被插入到哪个位置才能保持原列表的有序性
        - bisect.insort 则将新元素插入到那个位置
        - bisect 模块不会判断原列表是否有序，因开销太大，所以不要应用于无序列表
    - 切片
        - seq[1:5:2]
        - 为切片赋值：seq[3:4] = [6, 3]，即将这一段替换
        ```
        >>> seq
        [1, 2, 3, 4, 5, 6]
        >>> seq[3:4]=[8,8,8]
        >>> seq
        [1, 2, 3, 8, 8, 8, 5, 6]
        >>> seq[3:4]=[8,[8,8]]
        >>> seq
        [1, 2, 3, 8, [8, 8], 8, 8, 5, 6]
        ```
        - 全切：seq[:]
        - 负数表示从末尾开始切：seq[-4:]
        - 反序：seq[::-1]
    - 内置的序列函数
        - enumerate
            - 在对一个序列进行迭代时，常常需要跟踪当前项的索引。下面是一种 diy 的办法
            ```
            i = 0
            for value in collection:
                    #用 value 做一些事情
                    i += 1
            ```
            而 enumerate 函数返回序列的(i, value)元组：
            ```
            for i, value in enumerate(collection):
                    #用 value 做一些事情
            ```
            - 在对数据进行索引时，enumerate 还有一种不错的使用模式，即求取一个将序列值（假定是唯一的）映射到其所在位置的字典
            ```
            >>> some_list = ['foo', 'bar', 'baz']
            >>> mapping = dict((v, i) for i, v in enumerate(some_list))
            >>> mapping
            {'bar': 1, 'baz': 2, 'foo': 0}
            ```
        - 非就地排序：sorted(list)
        - zip：压缩配对
        ```
        >>> seq1 = ['foo', 'bar', 'baz']
        >>> seq2 = ['one', 'two', 'three']
        >>> zip(seq1, seq2)
        <zip object at 0x1040c8f48>
        >>> list(zip(seq1, seq2))
        [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
        >>> seq3 = [False, True]
        >>> zip(seq1, seq2, seq3)
        <zip object at 0x1040c8fc8>
        >>> list(zip(seq1, seq2, seq3)) #取决于最短的列表
        [('foo', 'one', False), ('bar', 'two', True)]
        ```
        解压缩
        ```
        >>> test = [(1,'one'), (2, 'two')]
        >>> first, second = zip(*test)
        >>> first
        (1, 2)
        >>> second
        ('one', 'two')
        ```
        - reversed：逆序迭代
        ```
        >>> list(reversed(range(10)))
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        ```
    - 字典
        - 哈希映射（hash map）、相联数组（associative array）
        - 通过键访问键值
        - 判断键是否在字典内：a in dict
        - 删除：del[key]
        - 删除返回指定值： dict.pop(key)
        - 键、值列表：dict.keys( )、 dict.values( )，虽然键值对没有特定的顺序，但这两个函数会以相同的顺序输出键和值。python3 会返回迭代器
        - 合并字典：dict1.update(dict2)
        - 默认值
            - dict 的 get 和 pop 方法可以接受一个可供返回的默认值
            - 根据首字母分类
            ```
            words = ['apple', 'bat', 'bar', 'atom', 'book']
            >>> by_words = {}
            >>> for word in words:
            ...     letter = word[0]
            ...     if letter not in by_words:
            ...             by_words[letter] = [word]
            ...     else:
            ...             by_words[letter].append(word)
            ...
            >>> by_words
            {'b': ['bat', 'bar', 'book'], 'a': ['apple', 'atom']}
            ```
            字典的 setdefault 方法可以达到上述目的。上面的 if-else 块可以写作
            ```
            by_words.setdefault(letter, []).append(word)
            ```
            内置的 collections 模块有一个叫做 defaultdict 的类，它使该过程更简单。传入一个类型或函数（用于生成字典各插槽所使用的默认值）即可创建出一个 defaultdict：
            ```
            from collections import defaultdict
            by_letter = defaultdict(list)
            for word in words:
                    by_letter[word[0]].append(word)
            ```
            defaultdict 的初始化器只需要一个可调用对象（例如各种函数），并不需要明确的类型。因此，如果你将默认值设置成 4，只需传入一个能返回 4 的函数即可：
            ```
            counts = defaultdict(lambda: 4)
            ```
        - 字典键的有效类型：键必须是不可变对象，如标量类型（整数，浮点数，字符串）或元组（元组中的所有对象也必须是不可变的），即可哈希性（hashability）。通过 hash 函数，可以判断是否是可哈希的。如果要将列表当做键，最简单的就是将其转换为元组
- 集合
    - 元素唯一
    - set 创建或者大括号
    - 集合运算

    | 函数 | 其他表示法 | 说明|
    | :------------- | :------------- | :------------- |
    | a.add(x)       | N/A   |添加 x 元素到集合 a|
    | a.remove(x)   | N/A | 删除|
    | a.union(b)    | a \| b |并|
    | a.intersection(b)|a \& b|交|
    | a.difference(b)| a - b|a 中不属于 b 的元素|
    | a.symmetric_difference(b)|a ^ b|对称差（异或），a 或 b 中不同时属于 a 和 b 的元素|
    | a.issubset(b)|N/A|a 是 b 的子集为 True|
    | a.issuperset(b)|N/A|b 是 a 的子集为 True|
    | a.isdisjoint(b)|N/A|如果 a 和 b 没有公共元素，为 True|
- 列表、集合以及字典的推导式
    - 列表：
    ```
    [expr for val in collection if condition]
    ```
    - 字典：
    ```
    {key-expr : value-expr for val in collection if condition}
    ```
    - 集合：
    ```
    {expr for val in collection if condition}
    ```

## 4. 函数

- 注意作用域
```
a = []
>>> def func():
...     for i in range(5):
...             a.append(i)
...
>>> func()
>>> a
[0, 1, 2, 3, 4]
```
下面的例子若想改变 a，则需要在函数内部加上 global a 语句
```
>>> a = 1
>>> def func():
...     a = 2
...
>>> func()
>>> a
1
```
- 可以返回字典和元组
- 函数也是对象
下面代码用于清理数据
```
>>> states = ['    Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FIOrIda', 'south     carolina##', 'West virginia?']
>>> import re
>>> def clean_string(strings):
...     result = []
...     for value in strings:
...             value = value.strip()
...             value = re.sub('[!#?]', '', value)      #移除标点符号
...             value = value.title()
...             result.append(value)
...     return result
...
>>> clean_string(states)
['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Fiorida', 'South     Carolina', 'West Virginia']
```
其实还有另外一种不错的方法：将需要在一组给定字符串上执行的所有运算做成一个列表：
```
>>> def remove_punctuation(value):
...     return re.sub('[!#?]', '', value)
...
>>> cleans_ops = [str.strip, remove_punctuation, str.title]
>>> def clean_strings(strings, ops):
...     result = []
...     for value in strings:
...             for function in ops:
...                     value = function(value)
...             result.append(value)
...     return result
...
>>> clean_strings(states, cleans_ops)
['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Fiorida', 'South     Carolina', 'West Virginia']
```
这种多函数模式使你能在很高的层次上轻松修改字符串的转换方式，还可以将函数用作其他函数的参数，比如内置的 map 函数，它用于在一组数据上应用一个函数
```
>>> map(remove_punctuation, states)
<map object at 0x1040cc0f0>
>>> list(map(remove_punctuation, states))
['    Alabama ', 'Georgia', 'Georgia', 'georgia', 'FIOrIda', 'south     carolina', 'West virginia']
```
- 匿名函数（lambda 函数）
```
def short_function(x):
        return x * 2
#等价于
equiv_anon = lambda x: x * 2
```
另外一个例子，根据列表中各字符串中不同字母的数量排序：
```
>>> strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
>>> strings.sort(key=lambda x: len(set(list(x))))
>>> strings
['aaaa', 'foo', 'abab', 'bar', 'card']
```
- 闭包（closure）：返回函数的函数
    - 由其他函数动态生成并返回的函数
    - 被返回函数可以访问其创建者的局部命名空间中的变量
    ```
    >>> def make_closure(a):
    ...     def closure():
    ...             print('I know the secret: %d' % a)
    ...     return closure
    ...
    >>> closure = make_closure(5)
    >>> closure()
    I know the secret: 5
    ```
    - 虽然闭包的内部状态一般都是静态的，但也允许使用可变对象。例如，下面这个函数可以返回一个能够记录其参数（曾经传入的一切参数）的函数：
    ```
    >>> def make_watcher():
    ...     have_seen = {}
    ...     def has_been_seen(x):
    ...             if x in have_seen:
    ...                     return True
    ...             else:
    ...                     have_seen[x] = True
    ...                     return False
    ...     return has_been_seen
    ...
    >>> watcher = make_watcher()
    >>> vals = [5, 6, 1, 5, 1, 6, 3, 5]
    >>> [watcher(x) for x in vals]
    [False, False, False, True, True, True, False, True]
    ```
    - 一个技术限制：虽然可以修改内部状态对象（比如说向字典添加键值对），但不能绑定外层函数作用域中的变量。一个解决办法是：修改字典或列表，而不是绑定变量
    ```
    >>> def make_counter():
    ...     count = [0]
    ...     def counter():
    ...             #增加并返回当前的 count
    ...             count[0] += 1
    ...             return count[0]
    ...     return counter
    ...
    >>> counter = make_counter()
    >>> counter()
    1
    >>> counter()
    2
    >>> counter()
    3
    ```
    - 在实际工作中，你可以编写带有大量选项的非常一般化的函数，然后再组装出更检点更专门化的函数。下面的例子中创建一个字符串格式化函数：
    ```
    >>> def format_and_pad(template, space):
    ...     def formatter(x):
    ...             return (template % x).rjust(space)
    ...     return formatter
    ```
    然后，你可以创建一个始终返回 15 位字符串的浮点数格式化器
    ```
    >>> fmt = format_and_pad('%.4f', 15)
    >>> fmt(1.756)
    '         1.7560'
    ```
- 扩展调用语法和\*args、\*\*kwargs
    - 调用函数时，位置参数被打包成元组，关键字参数被打包成字典
    - 函数实际接收的是一个元组\*args 和一个字典\*\*kwargs
    ```
    >>> def say_hello_then_call_f(f, *args, **kwargs):
    ...     print('args is ' + str(args))
    ...     print('kwargs is ' + str(kwargs))
    ...     print("Hello! Now I'm going to call %s" % f)
    ...     return f(*args, **kwargs)
    ...
    >>> def g(x, y, z=1):
    ...     return (x + y) / z
    ...
    >>> say_hello_then_call_f(g, 1, 2, z=5.)
    args is (1, 2)
    kwargs is {'z': 5.0}
    Hello! Now I'm going to call <function g at 0x1040c5950>
    0.6
    ```
- 柯里化（currying）：部分参数应用（partial argument application）
```
def add_numbers(x, y):
        return x + y
add_five = lambda y: add_numbers(5, y)
```
add_numbers 的第二个参数称为“柯里化的”。内置的 functools 模块可以用 partial 函数将此过程简化
```
from functools import partial
add_five = partial(add_numbers, 5)
```
- 生成器
    -  生成器是构造新的可迭代对象的一种简单方式。一般的函数执行之后会返回单个值，而生成器则是延迟返回一个值序列，即每返回一个值之后暂停，直到下一个值被请求时再继续
    - 要创建一个生成器，只需将函数中的 return 替换为 yield 即可
    - 生成器表达式
    ```
    >>> gen = (x ** 2 for x in range(100))
    >>> gen
    <generator object <genexpr> at 0x1040bbbf8>
    >>> sum(gen)
    328350
    ```
    - itertools 模块：标准库 iterator 模块中有一组用于许多常见数据算法的生成器。例如，groupby 可以接受任何序列和一个函数。它根据函数的返回值对序列中的连续元素进行分组
    ```
    >>> import itertools
    >>> first_letter = lambda x: x[0]
    >>> names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
    >>> for letter, names in itertools.groupby(names, first_letter):
    ...     print(letter + ' ' + str(list(names))) #names 是一个生成器
    ...
    A ['Alan', 'Adam']
    W ['Wes', 'Will']
    A ['Albert']
    S ['Steven']
    ```
    - 一些常用的 itertools 函数

    | 函数 | 说明 |
    | :------------- | :------------- |
    | imap(func, \*iterables) | 内置函数 map 的生成器版，将 func 应用于参数序列的各个打包元组   |
    |ifilter(func,iterable)|内置函数 filter 的生成器版，当 func(x)为 True 时输出元素 x|
    |combinations(iterable,k)|生成一个由 iterable 中所有可能的 k 元元组组成的序列（不考虑顺序）|
    |permutations(iterable,k)|生成一个由 iterable 中所有可能的 k 元元组组成的序列（考虑顺序）|
    |groupby(iterable,keyfunc)|为每个唯一键生成一个(key,sub-iterator)|

## 5. 文件和操作系统

- 打开
```
path = './test.txt'
f = oepn(path)
```
默认只读模式（'r'）
- 行迭代
```
for lines in f:
        pass
```
- 得到没有 EOL
```
lines = [x.rstrip() for x in open(path)]
```
- 文件模式

| 模式 | 说明 |
| :------------- | :------------- |
| r | 只读    |
|w|只写。创建新文件（删除同名的任何文件）|
|a|附加到现有文件（不存在就创建一个）|
|r+|读写模式|
|b|附加说明某模式用于二进制文件，即'rb'或'wb'|
|U|通用换行模式。单独使用 U 或附加到其他读模式（如'rU'）|
- 写：write 或 writelines
- 重要的 Python 文件方法或属性

| 方法 | 属性 |
| :------------- | :------------- |
| read([size]) | 以字符串形式返回文件数据，可选的 size 参数用于说明读取的字节数 |
|readlines([size])|将文件返回为行列表，可选参数 size|
|write(str)|将字符串写入文件|
|close()|关闭句柄|
|flush()|清空内部 I/O 缓存区，并将数据强行写回磁盘|
|seek(pos)|移动到指定的文件位置（整数）|
|tell()|以整数形式返回当前文件位置|
|closed|如果文件已关闭，则为 True|
