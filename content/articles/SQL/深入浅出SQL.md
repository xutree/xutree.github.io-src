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
    - int(integer) 整数
    - dec(decimal) 实数
    - date 日期
    - time、timestamp、datetime 时间
    - varchar 可变长度文本，最长255
    - blob 大量文本数据
- 检查创建的表 `DESC table_name;` （describe）
- 删除表 `DROP table_name;`
- 插入行
    - `INSERT INFO table_name (fiel1,..., fieldN) VALUE (value1,...,valueN);`
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
