Title: Linux 中的扩展和引用
Category: Linux
Date: 2018-10-08 16:25:59
Modified: 2018-10-08 22:36:33
Tags: Linux, 教程

## 扩展

当我们每次在命令行按下`Enter`键时，bash 会在执行命令之前对文本进行多重处理。产生这个结果的处理过程称为扩展（expansion）。

一个 🌰 :`echo *`会将当前目录下所有的非隐藏文件名打印出来。

### 路径名扩展

通过使用通配符来实现扩展的机制称为路径名扩展（pathname expansion）。

### 波浪线扩展（~）

如果把它用在一个单词的开头，那么它将被扩展为指定用户的主目录名；如果没有指定用户名，则扩展为当前用户的主目录：

```
[me@linuxbox ~]$ ech ~
/home/me
```

```
[me@linuxbox ~]$ ech ~foo
/home/foo
```

### 算术扩展

shell 支持通过扩展来运行算术表达式。这允许我们把 shell 提示符当做计算器来使用：

```
[me@linuxbox ~]$ echo $((2+2))
4
```

算术扩展使用形式：**$((expression))**，其中 expression 是包含数值和算术操作符的算术表达式。算术扩展**只支持整数**。

#### 运算符

| 运算符 | 描述 |
| :------------- | :------------- |
| + | 加 |
| - | 减 |
| * | 乘 |
| / | 除（结果为整数） |
| % | 取余 |
| ** | 取幂 |

空格在算术表达式中无意义，表达式可以嵌套：

```
[me@linuxbox ~]$ echo $(($((5**2)) * 3))
75
```

还可以使用一对括号来组合多个子表达式：

```
[me@linuxbox ~]$ echo $(((5**2) * 3))
75
```

#### 数字进制

| 符号 | 描述 |
| :------------- | :------------- |
| number | 默认情况下，number 没有任何符号，将作为十进制数字 |
| 0number | 在数字表达式中，以0开始的数字被视为八进制数字 |
| 0xnumber | 十六进制数 |
| base#number | base 进制的 number |

🌰 ：

```
[me@linuxbox ~]$ echo $((0xff))
255
[me@linuxbox ~]$ echo $((3#11))
4
```

### 花括号扩展

花括号扩展可以用于创建多种文本字符串，例如

```
[me@linuxbox ~]$ echo Front-{A,B,C}-Back
Front-A-Back Front-B-Back Front-C-Back
```

用于花括号扩展的模式信息可以包含一个称为**前导字符**的开头部分和一个称为**附言**的结尾部分。花括号表达式本身可以包含一些列逗号分隔的字符串，也可以包含一系列整数或者单个字符。

模式信息不能包含内嵌的空白。

花括号扩展最普遍的应用是创建一系列的文件或者目录：

```
[me@linuxbox ~]$ mkdir {2009..2011}-0{1..9} {2009..2010}-{10..12}
```

### 参数扩展

shell 提供了多种参数扩展的形式。

#### 基本参数

参数扩展的最简单形式体现在平时对变量的使用中。举例来说，`$a`扩展后成为变量 a 所包含的内容，无论 a 包含什么。

简单参数可以被括号包围，如`${a}`，当变量相邻与其他文本时，必须使用括号，否则可能让 shell 混淆。

```
[me@linuxbox ~]$ a="foo"
[me@linuxbox ~]$ echo "$a_file"

[me@linuxbox ~]$ echo "${a}_file"
foo_file
```
因为不存在 a_file 变量，所以 shell 输出空。

同样，对于大于9的位置参数可以通过给相应数字加上括号来访问，例如访问第11个位置参数：`${11}`

#### 空变量扩展的管理

有的参数扩展用于处理不存在的变量和空变量。这些参数扩展在处理缺失的位置参数和给参数赋默认值时很有用。

`${parameter:-word}`：如果 parameter 未被设定或者是空参数，则其扩展为 word 的值。如果 parameter 非空，则扩展为 parameter 的值。

```
[me@linuxbox ~]$ foo=
[me@linuxbox ~]$ echo ${foo:-"substitute value if unset"}
substitute value if unset
[me@linuxbox ~]$ echo $foo
[me@linuxbox ~]$ foo=bar
[me@linuxbox ~]$ echo ${foo:-"substitute value if unset"}
bar
[me@linuxbox ~]$ echo $foo
bar
```

`${parameter:=word}`：如果 parameter 未被设定或者是空参数，则其扩展为 word 的值；此外，word 的值也将赋给 parameter。如果 parameter 非空，则扩展为 parameter 的值。注意：位置参数和其他特殊参数不能以这种方式赋值。

```
[me@linuxbox ~]$ foo=
[me@linuxbox ~]$ echo ${foo:="deafult value if unset"}
deafult value if unset
[me@linuxbox ~]$ echo $foo
deafult value if unset
[me@linuxbox ~]$ foo=bar
[me@linuxbox ~]$ echo ${foo:-"deafult value if unset"}
bar
[me@linuxbox ~]$ echo $foo
bar
```

`${parameter:？word}`：如果 parameter 未被设定或者是空参数，这样扩展会致使脚本出错而退出，并且 word 的内容输出到标准错误。如果 parameter 非空，则扩展为 parameter 的值。

```
[me@linuxbox ~]$ foo=
[me@linuxbox ~]$ echo ${foo:?"parameter is empty"}
bash: foo: parameter is empty
[me@linuxbox ~]$ echo $?
1
[me@linuxbox ~]$ foo=bar
[me@linuxbox ~]$ echo ${foo:?"parameter is empty"}
bar
[me@linuxbox ~]$ echo $?
0
```

`${parameter:+word}`：如果 parameter 未被设定或者是空参数，则不产生任何扩展。若 parameter 非空，word 的值将取代 parameter 的值产生扩展；然而，parameter 的值并不发生变化。

```
[me@linuxbox ~]$ foo=
[me@linuxbox ~]$ echo ${foo:+"substitute value if unset"}
[me@linuxbox ~]$ foo=bar

[me@linuxbox ~]$ echo ${foo:+"substitute value if unset"}
substitute value if unset
[me@linuxbox ~]$ echo $foo
bar
```

#### 返回变量名的扩展

shell 具有返回变量名的扩展。这种功能在相当特殊的情况下才会使用。

```
${!prefix*}
${!prefix@}
```

该扩展返回当前以 prefix 开通的变量名。根据 bash 文档，这两种形式的扩展形式执行的效果一模一样。

#### 字符串操作

`${#parameter}`：扩展为 parameter 内包含的字符串的长度。如果 parameter 是 “@” 或 “\*”，那么扩展的结果就是位置参数的个数。

```
[me@linuxbox ~]$ foo="This string is long."
[me@linuxbox ~]$ echo "'$foo' is ${#foo} characters long."
'This string is long.' is 20 characters long.
```

`{parameter:offset}`和`{parameter:offset:length}`：这个扩展提取一部分字符串。扩展以 offset 字符开始，直到字符串末尾，除非 length 特别指定它。

```
[me@linuxbox ~]$ foo="This string is long."
[me@linuxbox ~]$ echo ${foo:5}
string is long.
[me@linuxbox ~]$ echo ${foo:5:6}
string
```

如果 offset 为负，默认表示从字符串末尾开始。**注意，负值前必须有一个空格**，以防和`${parameter:-word}`扩展混淆。length 不能小于0。

```
[me@linuxbox ~]$ foo="This string is long."
[me@linuxbox ~]$ echo ${foo: -5}
long.
[me@linuxbox ~]$ echo ${foo: -5:2}
lo
```

如果参数是 “@”，扩展的结果则是从 offset 开始，length 为位置参数。

`${parameter#pattern}`和`${parameter##pattern}`：pattern 是一个通配符模式，“#” 去除最短匹配，”##” 去除最长匹配。

```
[me@linuxbox ~]$ foo=file.txt.zip
[me@linuxbox ~]$ echo ${foo#*.}
txt.zip
[me@linuxbox ~]$ echo ${foo##*.}
zip
```

`${parameter%pattern}`和`${parameter%%pattern}`：从尾部去除。pattern 是一个通配符模式，“%” 去除最短匹配，”%%” 去除最长匹配。

```
[me@linuxbox ~]$ foo=file.txt.zip
[me@linuxbox ~]$ echo ${foo%*.}
file.txt
[me@linuxbox ~]$ echo ${foo%%*.}
file
```

`${parameter/pattern/string}`：查找替换，只替换第一个出现的

`${parameter//pattern/string}`：替换所有的

`${parameter/#pattern/string}`：要求匹配出现在字符串开头

`${parameter/%pattern/string}`：要求匹配出现在字符串末尾

`/string`可以省略，此时匹配到的字符被删除

```
[me@linuxbox ~]$ foo=JPG.JPG
[me@linuxbox ~]$ echo ${foo/JPG/jpg}
jpg.JPG
[me@linuxbox ~]$ echo ${foo//JPG/jpg}
jpg.jpg
[me@linuxbox ~]$ echo ${foo/#JPG/jpg}
jpg.JPG
[me@linuxbox ~]$ echo ${foo/%JPG/jpg}
JPG.jpg
```
