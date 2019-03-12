Title: xlwings 教程
Category: 教程
Date: 2019-03-12 13:13:45
Modified: 2019-03-12 15:43:58
Tags: xlwings, Excel, python

[TOC]

xlwings 是一个 python 包用来和 Excel 进行交互，它包含四个层次：App $\rightarrow$ Book $\rightarrow$ Sheet $\rightarrow$ Range。

- App：用来索引打开的 Excel 实例。因为我们可能同时打开很多 Excel 应用程序，类似于我们可以在电脑是同时登陆多个 QQ 应用一样
- Book：用来索引 Excel 实例中的工作簿，因为我们的 Excel 中可能用多个工作簿
- Sheet：用来索引 Excel 工作簿中的表单，因为我们的工作簿中可能有多个表单
- Range：用来所以表单中的单元格

## 1. 新建 xlsx 文件

新建 xlsx 文件经历如下几个步骤：

1. 首先建立一个 App 对象 `app = xw.App()`，这会打开电脑上的 Excel 应用程序
2. 然后建立一个 Book 对象 `book = xw.Book()` 这会在第一步打开的 Excel 中建立一个工作簿
3. 然后即可以保存 xlsx 文件，`book.save('filename.xlsx')`，如果没有提供路径，则保存在程序当前目录
4. 关闭 App 对象，`app.quit()`

```
[In 1]: import xlwings as xw

[In 2]: app = xw.App()
[In 3]: book = xw.Book()
[In 4]: book.save('filename.xlsx')
[In 5]: app.quit()
```

## 2. 打开 xlsx 文件

执行 `book = xw.Book('path//to//file')` 会直接打开指定文件

```
[In 1]: import xlwing as xw

[In 2]: book = xw.Book('path//to//file')
```

## 3. 操作 xlsx 文件中的表单


### 3.1 获得 xlsx 文件中的表单数目

xlsx 文件中可能有多个表单，所以首先我们需要知道到底有多少个表单

```
[In 1]: import xlwing as xw

[In 2]: book = xw.Book('path//to//file')
[In 3]: book.sheets
[Out 3]: Sheets([<Sheet [test.xlsx]Sheet1>, <Sheet [test.xlsx]Sheet2>])
```

利用 `book.sheets` 我们得到了当前工作簿中所有的表单名称，当前工作簿有两个表单，名字分别为 *Sheet1*、*Sheet2*。

### 3.2 索引需要的表单

知道了表单的名称和个数以后，我们就可以索引到我们想要的表单了，有四种索引方法，例如我们需要索引 *Sheet2*：

- `sht2 = book.sheets[1]`，这种索引方法是 Python 的索引，表单的编号从 0 开始，故 *Sheet2* 的编号为 1
- `sht2 = book.sheets(2)`，这种索引方法是 Excel 的索引，表单编号从 1 开始，故 *Sheet2* 的编号为 2
- `sht2 = book.sheets['Sheet2']`，这种索引方法是直接利用表单名字索引的
- `sht2 = book.sheets('Sheet2')`，这种索引方法也是直接利用表单名字索引的

## 4. 操作表单中的单元格

### 4.1 索引单元格

所以单元格有如下方法：

- 索引单个单元格 `sht2.range('B3')` 或 `sht2.range((3,2))` 指明是第三行第二列单元格
- 索引区域 `sht2.range('B3:F6')` 或 `sht2.range((3,2),(6,6))`

### 4.2 操作单元格

#### 4.2.1 超链接

- `sht2.range('B3:F6').add_hyperlink(address, text_to_display=None, screen_tip=None)` 为区域内单元格添加超链接
- `sht2.range('B3').hyperlink` 获取单元格的超链接，**只适用于单元格**

#### 4.2.2 列宽行高

- `sht2.range('B3:F6').autofit()` 自动调整区域内单元格的宽度和高度
- `sht2.range('B3:F6').columns.autofit()` 自动调整区域内单元格的宽度
- `sht2.range('B3:F6').rows.autofit()` 自动调整区域内单元格的高度
- `sht2.range('B3:F6').column_width` 将返回区域内单元格的列宽（浮点数），单位是 point，如果列宽不一致，返回 `None`
- `sht2.range('B3:F6').row_height` 将返回区域内单元格的行高（浮点数），单位是 point，如果列宽不一致，返回 `None`
- `sht2.range('B3:F6').column_width = 23` 设置区域内单元格的列宽，范围必须为 [0, 255]
- `sht2.range('B3:F6').row_height = 23` 设置区域内单元格的行高（浮点数），范围必须是 [0, 409.5]
- `sht2.range('B3:F6').height` 返回区域单元格的总高度（浮点数），单位是 point
- `sht2.range('B3:F6').width` 返回区域单元格的总宽度（浮点数），单位是 point

#### 4.2.3 格式和内容

- `sht2.range('B3:F6').value` 获得区域内单元格的内容
- `sht2.range('B3:F6').value = ‘x'’` 设置区域内单元格的内容
- `sht2.range('B3:F6').clear()` 清除区域内单元格的内容和格式
- `sht2.range('B3:F6').clear_contents()` 清除区域内单元格的内容，保留格式

#### 4.2.4 获得区域字符串

- `sht2.range('B3:F6').address` 将返回字符串 `$B$3:$F$6'`
- `sht2.range('B3:F6').get_address(row_absolute=True,
    column_absolute=True, include_sheetname=False, external=False)` 返回字符串，代表区域单元的地址，根据参数的不同可以用不同返回形式，具体参考[这里](https://docs.xlwings.org/en/stable/api.html#xlwings.Range.get_address)

#### 4.2.5 单元格颜色

- `sht2.range('B3:F6').color` 将返回区域内单元格的颜色，若区域内单元格颜色不一致，返回 (0,0,0)，若无颜色，返回空
- `sht2.range('B3:F6').color = (255, 0, 0)` 设置区域内单元格的颜色

#### 4.2.6 单元格数量

- `sht2.range('B3:F6').count` 返回单元格的数量，也可用 `sht2.range('B3:F6').size`

#### 4.2.7 区域单元格特殊位置

- `sht2.range('B3:F6').column` 将返回区域内单元格第一列的索引（整数），本例返回 2
- `sht2.range('B3:F6').row` 将返回区域内单元格第一行的索引（整数），本例返回 3
- `sht2.range('B3:F6').last_cell` 返回一个 `Range` 对象，表示区域内最右下单元格的位置

- `sht2.range('B3:F6').top` 返回一个浮点数，表示从 行 1 的上边界到此区域上边界的距离，单位是 point
- `sht2.range('B3:F6').left` 返回一个浮点数，表示从 A 栏的左边界到此区域左边界的距离，单位是 point

- `sht2.range('B3:F6').columns` 将返回一个 `RangeColumns` 对象，代表区域里的列，本例返回 `RangeColumns(<Range [test.xlsx]Sheet2!$B$3:$F$6>)`
- `sht2.range('B3:F6').rows` 将返回一个 `RangeRows` 对象，代表区域里的行，本例返回 `RangeRows(<Range [test.xlsx]Sheet2!$B$3:$F$6>)`

上面这两个对象都有一个 `count` 数据成员，可以很方便的得到总行数和列数。

- `sht2.range('B3:F6').current_region` 返回一个 `Range` 对象，代表去除区域空白边界的范围，本类返回 `<Range [test.xlsx]Sheet2!$A$1:$C$3>`
- `sht2.range('B3:F6').end(args)` 参数 `args` 可为 left、right、up、down，该函数返回 `Range` 对象，表示指定区域近邻的边界单元格，如近邻的单元格无内容，则继续查找下一个近邻
- `sht2.range('B3:F6').expand(args)` `args` 可为 table、down、right，该函数根据参数扩展当前区域范围，并范围 `Range` 对象，table 为向右向下扩展，若扩展方向下一个单元格内容为空，则停止扩展；若扩展后的区域仍为空，则返回 `None`（例如，从空的单元格往右扩展，但是右边一个单元格也是空的情况）

#### 4.2.8 区域大小

- `sht2.range('B3:F6').resize(row_size=None, column_size=None)` 重设区域大小
- `sht2.range('B3:F6').shape` 返回元组，表示区域大小

#### 4.2.9 区域名称和数字格式

- `sht2.range('B3:F6').name` 返回区域的名字
- `sht2.range('B3:F6').name = 'test'` 设置区域的名字为 test
- `sht2.range('B3:F6').number_format` 获得区域内数字的格式
- `sht2.range('B3:F6').number_format = '0.00%'` 设置区域内数字的格式
- `sht2.range('B3:F6').offset(row_offset=0, column_offset=0)` 返回 `Range` 对象，代表偏移后的范围
- `sht2.range('B3:F6').options(convert=None, **options)` 可设置数值转换规则等，具体见[这里](https://docs.xlwings.org/en/stable/api.html#xlwings.Range.options)

#### 4.2.10 其他

- `sht2.range('B3:F6').raw_value` 直接加载数据，不经过 xlwings 转换，对速度要求高的应用可以考虑这个选项
- `sht2.range('B3:F6').sheet` 返回区域属于的表单

## 5. 操作表单中的形状

### 5.1 获取形状数量

```
[In 1]: sht2.shapes
[Out 1]: Shapes([<Shape 'Isosceles Triangle 1' in <Sheet [test.xlsx]Sheet2>>])
[In 2]: sht2.shapes.count
[Out 2]: 1
```

### 5.2 索引形状

有四种索引方法，例如我们需要索引 *Isosceles Triangle 1*：

- `shp = sht2.shapes[0]`，这种索引方法是 Python 的索引，形状的编号从 0 开始
- `shp = sht2.shapes(1)`，这种索引方法是 Excel 的索引，形状编号从 1 开始
- `shp = sht2.shapes['Isosceles Triangle 1']`，这种索引方法是直接利用形状名字索引的
- `shp = sht2.shapes['Isosceles Triangle 1')`，这种索引方法也是直接利用形状名字索引的

### 5.3 操作形状

- `shp.activate()` 激活形状
- `shp.delete()` 删除形状
- `shp.height` 返回或设置形状的高度，单位是 point
- `shp.width` 返回或设置形状的宽度，单位是 point
- `shp.top` 返回或设置形状的水平位置，单位是 point
- `shp.left` 返回或设置形状的竖直位置，单位是 point
- `shp.name` 返回或设置形状的名字
- `shp.parent` 返回形状的前驱
- `shp.type`返回形状的类型

## 6. 操作表单中的表格

### 6.1 获取表格数量

```
[In 1]: sht2.charts
[Out 1]: Charts([<Chart 'Chart 2' in <Sheet [test.xlsx]Sheet2>>])
[In 2]: sht2.charts.count
[Out 2]: 1
```

### 6.2 添加表格

利用 `add(left=0, top=0, width=355, height=211)` 函数：

```
[In 1]: import xlwings as xw

[In 2]: sht = xw.Book().sheets[0]
[In 3]: sht.range('A1').value = [['Foo1', 'Foo2'], [1, 2]]
[In 4]: chart = sht2.charts.add()
[In 5]: chart.set_source_data(sht.range('A1').expand())
[In 6]: chart.chart_type = 'line'
[In 7]: chart.name
[Out 7]: 'Chart1'
```

### 6.3 索引表格

有四种索引方法，例如我们需要索引 *Chart 2*：

- `cha = sht2.charts[0]`，这种索引方法是 Python 的索引，表格的编号从 0 开始
- `cha = sht2.charts(1)`，这种索引方法是 Excel 的索引，表格编号从 1 开始
- `cha = sht2.charts['Chart 2']`，这种索引方法是直接利用表格名字索引的
- `cha = sht2.charts['Chart 2')`，这种索引方法也是直接利用表格名字索引的


### 6.4 操作表格

- `cha.delete()` 删除表格
- `cha.height` 返回或设置表格的高度，单位是 point
- `cha.width` 返回或设置表格的宽度，单位是 point
- `cha.top` 返回或设置表格的水平位置，单位是 point
- `cha.left` 返回或设置表格的竖直位置，单位是 point
- `cha.name` 返回或设置表格的名字
- `cha.parent` 返回表格的前驱
- `cha.chart_type`返回表格的类型
- `cha.set_source_data(args)`  设置表格的数据来源，`args` 为 `Range` 对象

## 7. 操作表单中的图像

### 7.1 获取图像数量

```
[In 1]: sht2.pictures
[Out 1]: Charts([<Chart 'Chart 2' in <Sheet [test.xlsx]Sheet2>>])
[In 2]: sht2.pictures.count
[Out 2]: 1
```

### 7.2 添加图像

利用 `add(image, link_to_file=False, save_with_document=True, left=0, top=0, width=None, height=None, name=None, update=False)` 函数，第一参数可以是计算机中图像的路径（字符串）或者是 `Matplotlib` 对象：

```
[In 1]: import xlwings as xw

[In 2]: sht = xw.Book().sheets[0]
[In 3]: sht.pictures.add('path//to//file')
```

或者

```
[In 1]: import matplotlib.pyplot as plt
[In 2]: fig = plt.figure()
[In 3]: plt.plot([1, 2, 3, 4, 5])
[In 4]: sht.pictures.add(fig, name='MyPlot', update=True)
```

### 7.3 索引图像

有四种索引方法，例如我们需要索引 *Picture 1*：

- `pic = sht2.pictures[0]`，这种索引方法是 Python 的索引，图像的编号从 0 开始
- `pic = sht2.pictures(1)`，这种索引方法是 Excel 的索引，图像编号从 1 开始
- `pic = sht2.pictures['Picture 1']`，这种索引方法是直接利用图像名字索引的
- `pic = sht2.pictures['Picture 1')`，这种索引方法也是直接利用图像名字索引的


### 7.4 操作图像

- `pic.delete()` 删除图像
- `pic.height` 返回或设置图像的高度，单位是 point
- `pic.width` 返回或设置图像的宽度，单位是 point
- `pic.top` 返回或设置图像的水平位置，单位是 point
- `pic.left` 返回或设置图像的竖直位置，单位是 point
- `pic.name` 返回或设置图像的名字
- `pic.parent` 返回图像的前驱
- `pic.update(image)` 用新的图像替换当前图像，图像属性不变
