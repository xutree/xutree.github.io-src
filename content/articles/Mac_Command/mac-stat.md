Title: 利用 Mac stat 添加文件创建时间、最后修改时间
Category: 教程
Date: 2018-10-06 19:07:36
Modified: 2018-10-07 10:38:50
Tags: Mac

[TOC]

Pelican 根据 **.md** 文件生成网页的时候需要 metadata，所以写个命令行自动添加文件创建时间、最后修改时间，这样写博客的时候只需要把 title、category 和 tags 标签填上就行了，其中用了 `stat`命令。

## 1. 自动添加文件创建时间、最后修改时间

`stat`命令的 *a, m, c, B* 参数分别代表上次访问或修改时间文件，上次更改 inode 的时间或 inode 的生成时间（ UNIX 时间戳），所以我们可以通过提取这些信息实现想要的功能。唯一需要注意的是，结果是UNIX时间戳，我们需要将其转换为普通时间。

UNIX 时间，或称 POSIX 时间是 UNIX 或类 UNIX 系统使用的时间表示方式：从协调世界时1970年1月1日0时0分0秒起至现在的总秒数，不考虑闰秒。在多数 UNIX 系统上 UNIX 时间可以通过`date +%s`指令来检查。

在 Mac 系统是由 UNIX 时间戳转化为普通时间的指令为：
![UNIX 时间戳转化为普通时间]({filename}/images/fig7.png)

所以我们先根据`stat`获得文件的创建时间：
![根据stat获得文件的创建时间]({filename}/images/fig8.png)

然后转化为普通时间：
![转化为普通时间]({filename}/images/fig9.png)

以下为脚本：
```
#! /bin/bash

# 输入：需要修改的文件
static=$1

# 提取创建时间
create_time=$(date  -r$(stat -f "%B" $static) "+%Y-%m-%d %H:%M:%S")
# 提取修改时间
modify_time=$(date  -r$(stat -f "%m" $static) "+%Y-%m-%d %H:%M:%S")
# 查找Date标签的行号
num1=$(head -5 $static | grep -n 'Date' | cut -d ":" -f 1)
# 查找Modified标签的行号
num2=$(head -5 $static | grep -n 'Modified'| cut -d ":" -f 1)

# 如果Date标签行号为空，说明不存在Date标签，则插入Date
if [ -z "$num1" ]; then
    sed -i '' -e "2s/^//p; 2s/^.*/Date: $create_time/" $static   
fi
# 如果Modified标签行号为空，插入Modified
if [ -z "$num2" ]; then
    sed -i '' -e "3s/^//p; 3s/^.*/Modified: $modify_time/" $static
else
    # 否则，替换Modified标签到最新时间
    sed -i '' ${num2}d $static
    sed -i '' -e "3s/^//p; 3s/^.*/Modified: $modify_time/" $static
fi
```

## 2. 附：stat 命令详情

`stat`显示有关文件的信息。 不需要读取，写入或执行指定文件的权限，但必须可搜索通向该文件的路径名中列出的所有目录。 如果没有给出参数，`stat`将显示有关标准输入的文件描述符（stdin）的信息。

当作为`readlink`调用时，仅打印符号链接的目标。 如果给定的参数不是符号链接，则`readlink`将不打印任何内容并退出并显示错误。

显示的信息是通过使用给定参数调用`lstat`系统调用并解释返回的结构来获得的。

### 2.1 参数

**\-F**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;与`ls`命令的 **-F** 参数一样，在作为目录的每个路径名之后显示斜杠（'/'），在每个可执行的路径名后面显示星号（'\*'），在每个符号链接后显示at符号（'@'）， 在每个without文件后面显示百分号（'％'），每个套接字后显示等号（'='），以及在每个FIFO文件后面显示一个垂直条（'|'）。 **-F** 的使用意味着 **-l**

**\-f** *format*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用指定的格式显示信息

**\-L**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`stat`而不是`lstat`。 如果文件是符号链接，则stat给出的信息是链接文件目标文件的信息，而不是链接文件本身

**\-l**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将输出以`ls -lT`格式显示，即显示文件的完整时间信息，包括月，日，小时，分钟，秒和年

**\-n**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输出不强制换行

**\-q**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果对`stat`或`lstat`的调用失败，则不显示失败消息。以`readlink`方式运行时，会自动禁止错误消息

**\-r**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;显示原始信息。即，对于stat结构（UNIX/Linux系统中定义的结构体）中的所有字段，显示原始数值（例如，自纪元以来的秒数等）

**\-s**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在“shell输出”中显示信息，适用于初始化变量

**\-t** *timefmt*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用指定的格式显示时间戳。 此格式直接传递给`strftime`命令

**\-x**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从某些Linux发行版中以更详细的方式显示信息

### 2.2 格式

格式字符串类似于`printf`格式，因为它们以 ％ 开头，然后是一系列格式化字符，最后是一个字符，用于选择要格式化的 struct stat 字段。 如果 ％ 后面紧跟 n，t，％ 或 @ 之一，则会打印换行符，制表符，百分号或当前文件号，否则将检查字符串是否包含以下内容：

以下是任何可选标志：

**\#**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为八进制和十六进制输出选择备用输出形式。 非零八进制输出将具有前导零，并且非零十六进制输出将具有前缀“0x”

**+**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;断言应始终打印指示数字是正数还是负数的符号。 非负数通常不打印带符号

**-**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将字符串输出对齐到字段的左侧，而不是右侧

**0**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将左边距的填充字符设置为“0”字符，而不是空格

**space**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在非负有符号输出字段的前面保留一个空格。 如果同时使用**‘+’** ，则**‘+’** 将覆盖空格

以下是任何可选字段：

*size*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可选的十进制数字字符串，指定最小字段宽度

*prec*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由小数点'.'和十进制数字字符串组成的可选精度，指示最大字符串长度，浮点输出中小数点后出现的位数，或数字输出中显示的最小位数

*fmt*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可选的输出格式说明符，它是D，O，U，X，F 或 S 之一。它们分别表示带符号的十进制输出，八进制输出，无符号十进制输出，十六进制输出，浮点输出和字符串输出。 某些输出格式不适用于所有字段。 浮点输出仅适用于 timespec 字段（a，m 和 c 字段）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;特殊输出说明符S可用于指示输出（如果适用）应为字符串格式。 可与以下标志结合使用：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*amc* 以`strftime`格式显示日期

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*dr* 显示实际设备名称

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*gu* 显示组或用户名

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*p* 以`ls -lTd`显示文件模式

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*N* 显示文件名

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*T* 显示文件类型

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Y* 在输出中插入“ -> ”。 请注意，*Y* 的默认输出格式是字符串，但如果明确指定，则会预先添加这四个字符

*sub*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可选的子字段说明符（高，中，低）。仅适用于 p，d，r 和 T 输出格式。 它可以是以下之一：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*H* “高”，指定来自 r 或 d 的设备的主要编号，来自 p 的字符串形式的权限的“用户”位，来自 p 的数字形式的文件“type”位，以及 T 的长输出形式

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*L* “低”，指定来自 r 或 d 的设备的次要编号，来自 p 的字符串形式的权限的“其他”位，来自 p 的数字形式的“用户”，“组”和“其他”位， 当与 T 一起使用时，文件类型的`ls -F`样式输出字符（对此使用 L 是可选的）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*M* “中”，指定 p 的字符串输出形式的权限的“组”位，或 p 的数字形式的 “suid”，“sgid” 和 “sticky” 位

*datum*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;必填字段说明符，是以下之一：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*d* 文件所在的设备

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*i* 文件的inode编号

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*p* 文件类型和权限

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*l* 文件的硬链接数

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*u, g* 文件所有者的用户ID和组ID

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*r* 字符和块设备专用文件的设备编号

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*a, m, c, B* 上次访问或修改时间文件，上次更改 inode 的时间或 inode 的生成时间（UNIX时间戳）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*z* 文件大小（以字节为单位）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*b* 分配给文件的块数

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*k* 最佳文件系统I / O操作块大小

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*f* 用户定义的文件标志

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*v* Inode 生成号

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;以下四个字段说明符不是直接从struct stat中的数据中提取的，而是：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*N* 文件的名称

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*T* 文件类型，类似`ls -F`，如果给出子字段说明符H，则采用更具描述性的形式。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Y* 符号链接的目标

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Z* 从字符或块特殊设备的rdev字段扩展为“major，minor”，并为所有其他设备提供大小输出

只有 ％ 和字段说明符是必需的。大多数字段说明符默认为 U 作为输出形式；p 默认输出形式是 O；a、m、c 默认输出形式是 D，Y、T、N 默认输出形式是 S。
