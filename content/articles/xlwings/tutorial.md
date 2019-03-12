Title: xlwings 教程
Category: 教程
Date: 2019-03-12 13:13:45
Modified: 2019-03-12 13:13:45
Tags: xlwings, Excel, python

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

- `sht2.range('B3:F6').add_hyperlink(address, text_to_display=None, screen_tip=None)` 为区域内单元格添加超链接
- `sht2.range('B3:F6').autofit()` 自动调整区域内单元格的宽度和高度
- `sht2.range('B3:F6').columns.autofit()` 自动调整区域内单元格的宽度
- `sht2.range('B3:F6').rows.autofit()` 自动调整区域内单元格的高度
- `sht2.range('B3:F6').clear()` 清除区域内单元格的内容和格式
- `sht2.range('B3:F6').clear_contents()` 清除区域内单元格的内容，保留格式
- `sht2.range('B3:F6').address` 将返回字符串 `$B$3:$F$6'`
- `sht2.range('B3:F6').color` 将返回区域内单元格的颜色，若区域内单元格颜色不一致，返回 (0,0,0)，若无颜色，返回空
- `sht2.range('B3:F6').color = (255, 0, 0)` 设置区域内单元格的颜色
- `sht2.range('B3:F6').column` 将返回区域内单元格第一列的索引（整数），本例返回 2
- `sht2.range('B3:F6').column_width` 将返回区域内单元格的列宽（浮点数），如果列宽不一致，返回 `None`
- `sht2.range('B3:F6').column_width = 23` 设置区域内单元格的列宽，列宽范围必须为 [0,255]
- `sht2.range('B3:F6').columns` 将返回一个 `RangeColumns` 对象，代表区域里的列，本例返回 `RangeColumns(<Range [test.xlsx]Sheet2!$B$3:$F$6>)`
- `sht2.range('B3:F6').count` 返回单元格的数量
- `sht2.range('B3:F6').current_region` 返回一个 `Range` 对象，代表去除区域空白边界的范围，本类返回 `<Range [test.xlsx]Sheet2!$A$1:$C$3>`
- `sht2.range('B3:F6').end(args)` 参数 `args` 可为 left、right、up、down，该函数返回 `Range` 对象，表示指定区域近邻的边界单元格，如近邻的单元格无内容，则继续查找下一个近邻
- `sht2.range('B3:F6').expand(args)` `args` 可为 table、down、right，该函数根据参数扩展当前区域范围，并范围 `Range` 对象，table 为向右向下扩展，若扩展方向下一个单元格内容为空，则停止扩展；若扩展后的区域仍为空，则返回 `None`（例如，从空的单元格往右扩展，但是右边一个单元格也是空的情况）
- `sht2.range('B3:F6').get_address(row_absolute=True, column_absolute=True, include_sheetname=False, external=False)` 返回字符串，代表区域单元的地址，根据参数的不同可以用不同返回形式，具体参考[这里](https://docs.xlwings.org/en/stable/api.html)
