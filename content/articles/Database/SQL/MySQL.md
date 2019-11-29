Title: MySQL 教程
Category: 数据库
Tags: MySQL

[TOC]

(https://www.runoob.com/mysql/mysql-tutorial.html)[https://www.runoob.com/mysql/mysql-tutorial.html]

MySQL 是最流行的**关系型数据库管理系统**，在 WEB 应用方面 MySQL 是最好的 RDBMS（Relational Database Management System：关系数据库管理系统）应用软件之一。

数据库（Database）是按照数据结构来组织、存储和管理数据的仓库。

每个数据库都有一个或多个不同的 API 用于创建，访问，管理，搜索和复制所保存的数据。

我们也可以将数据存储在文件中，但是在文件中读写数据速度相对较慢。

所以，现在我们使用关系型数据库管理系统（RDBMS）来存储和管理的大数据量。所谓的关系型数据库，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。

RDBMS 即关系数据库管理系统(Relational Database Management System)的特点：

- 数据以表格的形式出现
- 每行为各种记录名称
- 每列为记录名称所对应的数据域
- 许多的行和列组成一张表单
- 若干的表单组成 database

MySQL 是一个关系型数据库管理系统，关联数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。

- MySQL 是开源的，所以你不需要支付额外的费用
- MySQL 支持大型的数据库。可以处理拥有上千万条记录的大型数据库
- MySQL 使用标准的 SQL 数据语言形式
- MySQL 可以运行于多个系统上，并且支持多种语言。这些编程语言包括 C、C++、Python、Java、Perl、PHP、Eiffel、Ruby 和 Tcl 等
- MySQL 对PHP有很好的支持，PHP 是目前最流行的 Web 开发语言
- MySQL 支持大型数据库，支持 5000 万条记录的数据仓库，32 位系统表文件最大可支持 4GB，64 位系统支持最大的表文件为 8TB
- MySQL 是可以定制的，采用了 GPL 协议，你可以修改源码来开发自己的 MySQL 系统

## 1. 登陆

> mysql -h 主机名 -u 用户名 -p

- -h：指定客户端所要登录的 MySQL 主机名, 登录本机（localhost 或 127.0.0.1）该参数可以省略
- -u：登录的用户名
- -p：告诉服务器将会使用一个密码来登录, 如果所要登录的用户名密码为空, 可以忽略此选项

## 2. 管理

### 2.1 添加用户

```
#创建账户
CREATE USER 'root'@'172.16.10.203' IDENTIFIED BY 'password';

#赋予权限，with grant option 这个选项表示该用户可以将自己拥有的权限授权给别人
GRANT ALL PRIVILEGES ON *.* TO 'root'@'172.16.10.203' WITH GRANT OPTION;

#改密码 & 授权超用户，flush privileges 命令本质上的作用是将当前 user 和 privilige 表中的用户信息/权限设置从 mysql 库（MySQL 数据库的内置库）中提取到内存里
FLUSH PRIVILEGES;
```

### 2.2 管理 MySQL 的命令

- `USE 数据库名;`
- `SHOW DATABASES;`
- `SHOW TABLES;`
- `SHOW COLUMNS FROM 数据表;`
- `SHOW INDEX FROM 数据表;`
- `SHOW TABLE STATUS FROM 数据库名 [LIKE 'pattern'] \G;` 加上 \\G，查询结果按列打印

## 3. 管理数据库

- `CREATE DATABASE 数据库名;` 创建
- `DROP DATABASE 数据库名;` 删除
- `USE 数据库名;` 选择

## 4. 数据类型

MySQL 支持多种类型，大致可以分为三类：**数值**、**日期/时间**和**字符串（字符）** 类型。

### 4.1 数值类型

MySQL 支持所有标准 SQL 数值数据类型。

这些类型包括严格数值数据类型 (INTEGER、SMALLINT、DECIMAL 和 NUMERIC)，以及近似数值数据类型（FLOAT、REAL 和 DOUBLE PRECISION）。

关键字 INT 是 INTEGER 的同义词，关键字 DEC 是 DECIMAL 的同义词。

BIT 数据类型保存位字段值，并且支持 MyISAM、MEMORY、InnoDB 和 BDB 表。

作为 SQL 标准的扩展，MySQL 也支持整数类型 TINYINT、MEDIUMINT 和 BIGINT。下面的表显示了需要的每个整数类型的存储和范围。


| 类型	|大小|	范围（有符号）|	范围（无符号）	|用途|
|:---:|:----:|:---:|:----:|:---:|
|TINYINT|	1 字节|	(-128，127)|	(0，255)|	小整数值|
|SMALLINT|	2 字节|	(-32 768，32 767)|	(0，65 535)|	大整数值|
|MEDIUMINT|	3 字节|	(-8 388 608，8 388 607)|	(0，16 777 215)|	大整数值|
|INT 或 INTEGER	|4 字节	|(-2 147 483 648，2 147 483 647)|	(0，4 294 967 295)|	大整数值|
|BIGINT|	8 字节|	(-9,223,372,036,854,775,808，9 223 372 036 854 775 807)|	(0，18 446 744 073 709 551 615)|	极大整数值|
|FLOAT|	4 字节|	(-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38)|	0，(1.175 494 351 E-38，3.402 823 466 E+38)	|单精度浮点数值|
|DOUBLE|	8 字节|	(-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)|	0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)|	双精度浮点数值|
|DECIMAL	|对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2	|依赖于M和D的值|	依赖于M和D的值|	小数值|

### 4.2 日期和时间类型

每个时间类型有一个有效值范围和一个"零"值，当指定不合法的 MySQL 不能表示的值时使用"零"值。

|类型|	大小(字节)|	范围	|格式|	用途|
|:----:|:----:|:----:|:----:|:----:|
|DATE	|3	|1000-01-01/9999-12-31|	YYYY-MM-DD|	日期值|
|TIME	|3	|'-838:59:59'/'838:59:59'	|HH:MM:SS|	时间值或持续时间|
|YEAR	|1|	1901/2155|	YYYY	|年份值|
|DATETIME	|8	|1000-01-01 00:00:00/9999-12-31 23:59:59|	YYYY-MM-DD HH:MM:SS	|混合日期和时间值|
|TIMESTAMP|	4	|1970-01-01 00:00:00/2038 结束时间是第 2147483647 秒，北京时间 2038-1-19 11:14:07，格林尼治时间 2038年1月19日 凌晨 03:14:07|YYYYMMDD HHMMSS	|混合日期和时间值，时间戳|

### 4.3 字符串类型

|类型|	大小|	用途|
|:----:|:----:|:----:|
|CHAR|	0-255字节|	定长字符串|
|VARCHAR	|0-65535 字节|	变长字符串|
|TINYBLOB|	0-255字节	|不超过 255 个字符的二进制字符串|
|TINYTEXT|	0-255字节|	短文本字符串|
|BLOB|	0-65 535字节|	二进制形式的长文本数据|
|TEXT|	0-65 535字节|	长文本数据|
|MEDIUMBLOB|	0-16 777 215字节|	二进制形式的中等长度文本数据|
|MEDIUMTEXT|	0-16 777 215字节|	中等长度文本数据|
|LONGBLOB|	0-4 294 967 295字节|	二进制形式的极大文本数据|
|LONGTEXT|	0-4 294 967 295字节|	极大文本数据|

CHAR 和 VARCHAR 类型类似，但它们保存和检索的方式不同。它们的最大长度和是否尾部空格被保留等方面也不同。在存储或检索过程中不进行大小写转换。

BINARY 和 VARBINARY 类似于 CHAR 和 VARCHAR，不同的是它们包含二进制字符串而不要非二进制字符串。也就是说，它们包含字节字符串而不是字符字符串。这说明它们没有字符集，并且排序和比较基于列值字节的数值值。

BLOB 是一个二进制大对象，可以容纳可变数量的数据。有 4 种 BLOB 类型：TINYBLOB、BLOB、MEDIUMBLOB 和 LONGBLOB。它们区别在于可容纳存储范围不同。

有 4 种 TEXT 类型：TINYTEXT、TEXT、MEDIUMTEXT 和 LONGTEXT。对应的这 4 种 BLOB 类型，可存储的最大长度不同，可根据实际情况选择。

## 5. 管理表

创建

```
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

删除

```
DROP TABLE table_name;
```

插入数据

```
INSERT INTO table_name ( field1, field2,...fieldN )
VALUES
( value1, value2,...valueN );
```
