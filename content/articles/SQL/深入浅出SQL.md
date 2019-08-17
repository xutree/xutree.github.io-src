Title: 深入浅出 SQL
Category: 读书笔记
Date: 2019-08-16 18:37:44
Modified: 2019-08-16 18:37:44
Tags: SQL

[TOC]

## 1. 数据和表

- **数据库**是保存表和其他相关SQL的容器，数据库中的所有表应该以某种方式相互关联
- **表**由行（或记录 record）和列（或字段 field）组成。**行**包含某个对象的所有信息，**列**表示各个分类
- 创建数据库 `CREATE DATABASE database_name;`
- 使用数据库 `USE database_name;`
- 显示数据库中的表格 `SHOW TABLES;`
- 创建表格

    ```
    CREATE TABLE table_name
    (
        field1 TYPE1(length1),
        field2 TYPE2(length2)
    );
    ```
- 数据类型
    - char(character) 事先设定好的长度
    - tinyint 有/无符号
    - smallint 有/无符号
    - mediumint 有/无符号
    - int(integer) 无符号整数 0~4294967295
    - int(signed) 有符号整数 -2147483648~2147483647
    - bigint 有/无符号
    - dec(decimal) 实数
    - date 日期 YYYY-MM-DD
    - time（HH:MM:SS）、timestamp（YYYYMMDDHHMMSS）、datetime （YYYY-MM-DD HH:MM:SS）时间
    - varchar 可变长度文本，最长255
    - blob 大量文本数据
    - boolean 0 和 1
- 检查创建的表 `DESC table_name;` （describe）
- 删除表 `DROP table_name;`
- 插入行
    - `INSERT INTO table_name (fiel1,..., fieldN) VALUES (value1,...,valueN);`
    - 可以改变field的顺序，但是相应的value也要改变
    - 可以省略所有field，但是此时value要填入所有数据，并且顺序要正确
    - 可以省略部分field
- 控制数据格式，比如创建表时 `field_name TYPE(length) NOT NULL DEFAULT default_value,`

## 2. SELECT 语句

- `SELECT * FROM table_name WHERE conditions;`
- `SELECT field1,...,fieldN FROM table_name WHERE conditions;`
- 条件
    - 逻辑 `AND`、`OR`
    - 比较 `<`、`>`、`<=`、`>=`、`<>`、`=`
    - 判空 `IS NULL`
    - 通配符 `LIKE`
        - `%` 任何数量未知字符 `WHERE fiel1 LIKE '%im';`
        - `_` 一个未知字符 `WHERE fiel1 LIKE '_im';`
    - 连续范围 `WHERE fiel1 BETWEEN a AND b;`
    - 离散范围 `WHERE fiel1 IN (value1,...,valueN);`
    - `NOT` 可以和 `NULL`、`BETWEEN`、`LIKE` 和 `IN` 一起使用，注意 **`NOT` 要紧接在 `WHERE` 或 `AND` 或 `OR` 后面**

## 3. DELETE 语句

- `DELETE FROM table_name WHERE conditions;`
- 只能删除一行或者多行
- `DELETE` 之前先 `SELECT` 确认一下

## 4. UPDATE 语句

- `UPDATE table_name SET fiel1=value1,...,fieldN=valueN WHERE conditions;`
- 可以使用基础数学运算和函数，如 `UPDATE table_name SET fiel1=f(fiel1),...,fieldN=valueN WHERE conditions;`

## 5. 规范化

### 5.1 原子性

- 同一列中不会有多个类型相同的值（比如爱好列里许多爱好）
- 不会有多个存储同类数据的列（比如三个学生类）

### 5.2 规范化优点

- 规范化表中没有重复的数据，可以减少数据库的大小
- 因为查询的数据较少，你的查询会更快

### 5.3 第一范式（First Normal Form）1NF

- 每个数据行必须包含具有原子性的值
- 每个数据行必须有主键（Primary Key）
- 主键必须不为 `NULL`，不能被修改，插入新数据必须指定
- 创建表格是指定主键 `PRIMARY KEY(field_name)`

```
    CREATE TABLE table_name
    (
        id INT NOT NULL AUTO_INCREMENT,
        field2 TYPE2(length2),
        PRIMARY KEY(id)
    );
```

- `AUTO_INCREMENT` 的列在插入式可以输入 `''` 让 SQL 自动递增
- `SHOW` 命令
    - `SHOW CREATE TABLE table_name;`
    - `SHOW CREATE DATABASE database_name;`
    - `SHOW COLUMNS FROM table_name;`
    - `SHOW INDEX FROM table_name;`
    - `SHOW WARNINGS;`

## 6. ALTER 命令

- 添加新列

```
    ALTER TABLE table_name
    ADD COLUMN id INT NOT NULL AUTO_INCREMENT FIRST,
    ADD PRIMARY KEY(id);
```

- `ADD` 添加列
- `MODIFY` 修改列的数据类型或位置
- `CHANGE` 修改列的名称和数据类型
- `DROP` 删除列
- 修改表名 `ALTER TABLE table_name RENAME TO new_name;`
- 修改列名并设为主键

```
    ALTER TABLE table_name
    CHANGE COLUMN field1 newfield1 INT NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY(newfield1);
```
- 修改多个列，逗号隔开

```
    ALTER TABLE table_name
    CHANGE COLUMN field1 newfield1 TYPE(length),
    CHANGE COLUMN field2 newfield2 TYPE(length);
```

- 删除某一列 `ALTER TABLE table_name DROP COLUMN fiel1;`
- 修改位置 `ALTER TABLE table_name MODIFY COLUMN fieli AFTER fieldj;`
- `FIRST`, `SECOND`, `THIRD`, `FOURTH`, `BEFORE`, `AFTER`, `LAST`
- 一些字符函数
    - `RIGHT(field_name, count)`
    - `LEFT(field_name, count)`
    - `SUBSTRING_INDEX(field_name, letter, pos)`
- 联合使用 `UPDATE table_name SET file1=RIGHT(field2, 2);`

## 7. SELECT 进阶

### 7.1 CASE

- 语法如下，缩进不影响，只是为了看起来方便
```
    UPDATE table_name
    SET category =
    CASE
        WHEN drama='T' THEN 'drama'
        WHEN ...
        ...
        ELSE 'misc'
    END;
```

### 7.2 ORDER BY

- 多列排序 `SELECT * FROM table_name ORDER BY fiel1,...,fieldN;`
- 降序关键字 `DESC` 必须位于需要降序的field名字后面

```
    SELECT * FROM table_name
    ORDER BY field1 ASC, field2 DESC;
```

### 7.3 GROUP BY

- `GROUP BY`必须得配合聚合函数来用
- 常用聚合函数：`SUM`, `AVG`, `MIN`, `MAX`, `COUNT`

### 7.4 其他

- `DISTINCT` 非重复 `SELECT DISTINCT field1 FROM table_name;`
- `LIMIT a, b;` 从a开始显示b个，SQL从零开始计数

## 8. 多张表的数据库设计

- **schema** 对数据库内的数据描述（列和表），以及任何相关对象和各种连接方式的描述称为模式
- **外键**（foreign key）是表中的某一列，它引用到另一个表的主键
    - 外键可能与它引用的主键名称不同
    - 外键使用的主键被称为父键，主键所在的表又被称为父表
    - 外键的值可以是 NULL，即使主键值不可为 NULL（通过外键约束解决）
    - 外键值不需要唯一

### 8.1 外键约束

- SQL 的主键和外键的作用：
    - 外键取值规则：空值或参照的主键值
    - 插入非空值时，如果主键表中没有这个值，则不能插入
    - 更新时，不能改为主键表中没有的值
    - 删除主键表记录时，你可以在建外键时选定外键记录一起级联删除还是拒绝删除
    - 更新主键记录时，同样有级联更新和拒绝执行的选择
- 创建带有外键的表

```
    CREATE TABLE table_name2
    (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    field1 TYPE(length),
    ...,
    fk_field INT NOT NULL,
    CONSTRAINT parenttable_parentkey_fk
    FOREIGN KEY (fk_field)
    REFERENCES parenttable (parentkey)
    );
```

### 8.2 表间的关系

#### 8.2.1 一对一

连接表时用到一对一的关系非常少。使用一对一的时机：

- 抽出数据或许能让你写出更快速的查询。例如大部分时间你只需查询某个 field，那么可以把次 field 单独抽出
- 如果有些列包含还不知道的值，可以单独存储这一列，以避免主表中出现 NULL
- 我们可能希望某些数据不要太常被访问。隔离这些数据即可管制访问次数
- 如果有一大块数据，例如 BLOB 类型，这段数据或许另存为一个表更好

#### 8.2.2 一对多

可用外键处理

#### 8.2.3 多对多

连接表 junction table

#### 8.2.4 组合键

由多个数据列构成的主键，具有唯一性

### 8.3 数据依赖

- `T.x -> T.y`：在关系表 T 中，y 列函数依赖于 x 列
- 部分依赖：非主键列依赖于组合主键的某个部分（但不完全依赖于组合主键）
- 传递依赖：如果改变任何非键列可能造成其他列的改变，即为传递依赖
- 传递函数依赖：任何非键列与另一个非键列有关联

### 8.4 第二范式 2NF

- 先符合 1NF
- 没有部分函数依赖性

只要所有列都是主键的一部分或者表中有唯一主键列符合 1NF 的表也会符合 2NF（这也是指定一个 AUTO_INCREMENT 的好理由）

### 8.5 第三范式 3NF

- 先符合 2NF
- 没有传递函数依赖性

## 9. 联接与多张表的操作

- `LENGTH`, `SUBSTR` 函数
- `AS` 关键字，把查找结果填入表格或者命名别名

```
    CREATE TABLE table_name
    (
    ...
    ) AS
    SELECT ... FROM ...;
```

- 命名别名也可以省略 `AS`，此时别名紧跟着原始表名或列名
- 交叉联接（直积），`CROSS JOIN` 也可不写，用 `,` 代替

```
    SELECT t.toy, b.boy
    FROM toys AS t
    CROSS JOIN
    boys AS b;
```

- 内联接就是通过查询中的条件移除了某些结果数据行后的交叉联接（`ON` 也可用 `WHERE` 代替）

```
    SELECT somecolumns
    FROM table1
    INNER JOIN
    table2
    ON someconditions;
```
- 内联接：相等联接、不等联接、自然联接（`NATURAL JOIN`，利用相同列名）

## 10. 子查询

### 10.1 子查询规则

- 子查询都是单一 `SELECT` 语句
- 子查询总是位于**括号**内
- 子查询没有属于自己的分号

### 10.2 子查询出现的位置

- `SELECT` 子句
- 选出 COLUMN LIST 作为其中一列
- `FROM` 子句
- `HAVING` 子句
- 子查询能与 `INSERT`, `DELETE`, `UPDATE`, `SELECT` 一起使用
- 大多数情况下子查询只能返回一个值，`IN` 关键字除外。
- 如果子查询放在 `SELECT` 语句中，用于表示某个欲选取的列，则一次只能从一列返回一个值。

```
    SELECT mc.first_name, mc.last_name,
    (SELECT state
    FROM zip_code
    WHERE mc.zip_code=zip_code) AS state
    FROM my_contacts mc;
```
### 10.3 非关联子查询

- 子查询可以独立运行且不会引用外层查询的任何结果
- 非关联子查询使用 `IN`、`NOT IN` 来检查子查询返回的值是否为集合的成员之一

### 10.4 关联子查询

- 常见用法是找出外层查询结果中不存在与关联表里的记录
- `EXISTS`, `NOT EXISTS`

```
SELECT mc.first_name firstname, mc.last_name lastname, mc.email email
FROM my_contacts mc
WHERE EXISTS
(
SELECT * FROM contact_interest ci
WHERE mc.contact_id=ci.contact_id
);
```

## 11. 外联接、自联接和联合

### 11.1 外联接

- 内联接是表额顺序不重要，外联接时分左右表
- 外联接一定会提供数据行，无论该行是否能在另一个表中找出相应的匹配
- `LEFT OUTER JOIN` 前左后右，匹配左表中的每一行及右表中符合条件的行
- 左联接结果集中的 NULL 表示右表中没有找到与左表相符的记录
- `RIGHT OUTER JOIN` 前右后左，匹配右表中的每一行及左表中符合条件的行
- 右联接结果集中的 NULL 表示左表中没有找到与右表相符的记录
- `FULL OUTER JOIN` 外全联接，直和，空补 NULL

### 11.2 自联接

通过别名，把单一表当成两张具有完全相同信息的表进行查询。

```
SELECT c1.name, c2.name AS boss
FROM clown_info c1
INNER JOIN clown_info c2
ON c1.boss_id = c2.id;
```

### 11.3 联合 UNION

取查询的并集，规则如下：

- 每个 `SELECT` 语句中列的数量必须一致
- 每个 `SELECT` 语句包含的表达式与统计函数也必须相同
- `SELECT` 语句的顺序不重要，不会改变结果
- SQL 默认会清除联合中的重复值
- 列的数据类型必须相同或者可以相互转换
- 如需重复数据，使用 `UNION ALL`
- 如需排序，需要在最后一条 `SELECT` 语句中加入 `ORDER BY`

由 `UNION` 返回的数据类型不太容易分辨，可以将结果制成表：

```
    CREATE TABLE table_name AS
    ...;
```

### 11.4 交集和差集

- `INTERSECT` (no mysql)
- `EXCEPT` (no mysql)

## 12. 约束、视图和事务

### 12.1 约束

前面讲的 `NOT NULL`  等都是约束。增加约束（更好的办法是建表时指定）(CHEAK no mysql)

```
    ALTER TABLE table_name
    ADD CONSTRAINT CHECK gender IN ('M', 'F');
```

### 12.2 视图

- 创建视图，保存查询语句

```
CREATE VIEW view_name AS
...;
```

- 查看视图 `SELECT * FROM view_name;`
- `FROM` 子句需要表，当 `SELECT` 语句的结果是一个虚拟表时，若没有别名，SQL 就无法取得其中的表
- 优点：
    - 视图把复杂查询简化为一个命令
    - 即使一直改变数据库的结构，也不会破坏依赖表的应用程序
    - 创建视图可以隐藏读者无须看到的信息
- `CHECK OPTION` 检查每个进行 `INSERT` 或 `DELETE` 的查询，它根据视图中的 `WHERE` 子句判断这些查询是否可以执行
- MySQL 可以利用 `CHECK OPTION` 模仿 `CHECK CONSTRAINT` 的功能
- 可更新视图包括引用表里所有为 `NOT NULL` 的列
- 除了使用 `CHECK OPTION`，一般直接操作表执行插入、更新和删除操作
- 使用完毕：`DROP VIRW view_name;`
- 当数据库的使用不止一人时，`CHECK CONSTRAINT` 和视图均有助于维护控制权

### 12.3 事务 transaction

- 事务是一群可完成一组工作的 SQL 语句
- 在事务过程中，如果所有步骤无法不受干扰的完成，则不完成任一单一步骤
- ACID 原则：
    - 原子性（atomicity）：要么完成要么不完成，不可分割
    - 一致性（consistency）：事务完成后应该维持数据库的一致性
    - 隔离性（isolation）：每次事务都会看到具有一致性的数据库
    - 持久性（durability）：事务完成，数据库需要正确的存储数据并保护数据免受断电和其他威胁的伤害
- 事务用法：
```
    START TRANSACTION;
    some operations here;
    COMMIT or ROLLBACK;
```
- 存储引擎必须是 BDB 或者 InnoDB 才支持事务
- 改变引擎 `ALTER TABLE table_name TYPE=InnoDB;`

## 13. 安全性

- 设置账号密码（MySQL 方式）

```
    SET PASSWORD FOR 'root'@'localhost'=PASSWORD('password');
```

- 增加用户

```
    CREATE USER newuser IDENTIFIED BY 'newpassword';
```

- 控制权

```
    GRANT command1(aim),command2(aim) ON table_name TO user1, user2 WITH GRANT OPTION;
    GRANT ALL ON table_name TO user1, user2 WITH GRANT OPTION;
    GRANT ALL ON database_name.* TO user1, user2 WITH GRANT OPTION;
```

- 撤回权限 `REVOKE ... FROM ...` 撤销具有传递性
    - `CASCADE;` 连锁撤销
    - `RESTRICT;` 有别的受影响则返回错误，并且不执行
- 角色（ no MySQL）

```
    CREATE ROLE role_name;
    GRANT command1(aim),command2(aim) ON table_name TO  role_name;
    GRANT role_name TO user;
    DROP ROLE role_name;
```

- `WITH ADMIN OPTION` 让具有该角色的每名用户都能把角色授予他人。撤销角色和上面一样。
- 创建账号的同时设置权限

```
    GRANT SELECT ON tabel TO user IDENTIFIED BY 'password';
```

## 14. 其他

- [http://localhost/phpMyAdmin](http://localhost/phpMyAdmin)
- `> ALL`, `< ANY`
- `SELECT DATE_FORMAT(a_data, '%M %Y') FROM some_dates;`
- 临时表（MySQL）：
    - `CREATE TEMPORARY TABLE table_name AS ...;`
    - `CREATE TEMPORARY TABLE table_name();`
- 类型转换 `CAST(your_column, TYPE)`
- 显示日期时间用户：`SELECT CURRENT_USER(DATE, TIME);`
- 数字函数：
    - `abs, ceil, floor, round, sign`
    - `sin, cos, tan, cot, asin, acos, atan`
    - `exp, ln, log, mod, power, sqrt`
    - `format, radians, pi, rand, truncate`
- 索引能加快速度，为列添加索引：`ALTER TABLE table_name ADD INDEX (field);`

![常用操作]({filename}/images/深入浅出sql1.jpg)
![常用操作]({filename}/images/深入浅出sql2.jpg)
![常用操作]({filename}/images/深入浅出sql3.jpg)
![常用操作]({filename}/images/深入浅出sql4.jpg)
![常用操作]({filename}/images/深入浅出sql5.jpg)
