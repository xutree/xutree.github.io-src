Title: HTML 入门
Category: HTML
Date: 2018-10-05 17:23
Modified: 2018-10-06 21:20:21
Tags: HTML

**HTML**，即超文本标记语言（**H**yper**T**ext **M**arkup **L**anguage）。与脚本或编程语言不同，标记语言使用标记（**tag**）来标识内容。

下面是一个 HTML tag 的例子：

`<p> 这是一个段落。</p>`

`<p>`称为开始标签，`</p>`称为结束标签。

## 网页的结构

- HTML：结构
- CSS：样式
- JavaScript：行为
- PHP 或类似语言：后端
- CMS：内容管理

## 基本 HTML 文件结构

|标签|解释|
|---|---|
|`<html></html>`|HTML文件的所有内容都包含在其中|
|`<head></head>`|HTML文件的头部包含有助于使页面工作的所有非可视元素|
|`<body></body>`|所有可视化元素都包含在body标签中|
|`<title></title>`|包含网页选项卡上现实的标题内容|

下面是 HTML 版本的“Hello, World！”程序：
```
<html>
   <head>
   </head>
   <body>
      Hello World!
   </body>
</html>
```

## 字体标签

|标签|解释|
|---|---|
|`<p></p>`|段落标签（浏览器会在段落前后自动添加空行）|
|`<br />`|换行而不开启新段落（它没有结束标记）|
|`<b></b>`|粗体|
|`<big></big>`|大号文本|
|`<i></i>`|斜体|
|`<small></small>`|小号文本|
|`<strong></strong>`|强调（一种phrase tag）|
|`<sub></sub>`|下标|
|`<sup></sup>`|上标|
|`<ins></ins>`|插入线|
|`<del></del>`|删除线|

浏览器将`<strong>`显示为`<b>`，将`<em>`显示为`<i>`。但是，这些标记的含义不同：`<b>`和`<i>`分别定义粗体和斜体文本，而`<strong>`和`<em>`表示文本“重要”。

## 标题标签

`<h1></h1>`，`<h2></h2>`，`<h3></h3>`，`<h4></h4>`，`<h5></h5>`，`<h6></h6>`六种标题，`<h1></h1>`字号最大。

## 标签属性

属性提供有关元素或标记的附加信息，同时还可以修改它们。例如
```
<p align="center">
   This text is aligned to center
</p>
```
会将段落居中显示（`<p>`标签的align属性在HTML5中不再支持）。

属性的数值可以通过像素或百分比指定，如

```
<hr width="50px" />
<hr width="50%" />
```

## 图像标签

`<img src="" height="" width="" border="" alt=""/>`

src：图像名称

height：图像高

width：图像宽

border：边界宽度

alt：如果无法显示图像，则alt属性指定以单词形式描述图像的替代文本


## 链接标签

`<a href="" target=""></a>`

href：目标网址

target：指定打开链接文档的位置，\_blank值将在新窗口或新标签中打开链接

## 列表标签

### 有序列表

```
<html>
   <head>
      <title>first page</title>
   </head>
   <body>
      <ol>
        <li>Red</li>
        <li>Blue</li>
        <li>Green</li>
      </ol>  
   </body>
</html>
```

### 无序列表

```
<html>
   <head>
      <title>first page</title>
   </head>        
   <body>
      <ul>
        <li>Red</li>
        <li>Blue</li>
        <li>Green</li>
      </ul>  
   </body>
</html>
```

## 表格标签

```
<table  border="" align="">
  <tr>
    <td bgcolor="red">Red</td>
    <td>Blue</td>
    <td>Green</td>
   </tr>
   <tr>
    <td>Yellow</td>
    <td colspan="2">Orange</td>
   </tr>
</table>
```

## 其他

|标签|解释|
|---|---|
|`<hr />`|水平线|
|`<!--...-->`|注释|

## HTML 元素类型

在 HTML 中，大多数元素被定义为块级或内联元素。

- 块级元素从新行开始，如`<h1>, <form>, <li>, <ol>, <ul>, <p>, <pre>, <table>, <div>`等
- 内联元素通常显示没有换行符，如`<b>, <a>, <strong>, <img>, <input>, <em>, <span>`等

`<div>`元素是一个块级元素，通常用作其他 HTML 元素的容器。与一些 CSS 样式一起使用时，`<div>`元素可用于设置内容块的样式。

同样，`<span>`元素是一个内联元素，通常用作某些文本的容器。与 CSS 一起使用时，`<span>`元素可用于设置文本的部分样式。

其他元素可以用作块级元素或内联元素。 这包括以下这些：

- APPLET - 嵌入式 Java 小程序
- IFRAME - 内联框架
- INS - 插入文本
- MAP - 图像映射
- OBJECT - 嵌入对象
- SCRIPT - HTML 文档中的脚本

你可以在块元素内插入内联元素。 例如，可以在`<div>`元素中包含多个`<span>`元素。反之不行。

## 表单标签

HTML 表单用于从用户收集信息。使用`<form>`元素及其开始和结束标记定义表单，使用 action 属性指向将在用户提交表单后加载的网页：
```
<body>
   <form action="" method="">…</form>
</body>
```
method 属性指定在提交表单时使用的 HTTP 方法（GET 或 POST）：

- 使用 GET 时，表单数据将显示在页面地址中
- 如果表单正在更新数据，请使用 POST，或者包含敏感信息（密码）。POST 提供了更好的安全性，因为提交的数据在页面地址中不可见

要接受用户输入，需要相应的表单元素，例如文本字段。 `<input>`元素有许多变体，具体取决于 type 属性。 它可以是文本，密码，广播，URL，提交等。
```
<form>
   <input type="text" name="username" /><br />
   <input type="password" name="password" />
</form>
```

# `<frame>`标签

可以使用特殊帧文档将页面划分为帧。

`<frame>`标签定义`<frameset>`中的一个特定窗口（框架）。`<frameset>`中的每个`<frame>`可以具有不同的属性，例如边框，滚动，调整大小的能力等。

`<frameset>`元素指定框架集中的列数或行数，以及每个框架占空间像素的百分比或数量。
```
<frameset cols="25%,50%,25%">
   <frame src="a.htm" />
   <frame src="b.htm" />
   <frame src="c.htm" />
   <noframes>Frames not supported!</noframes>
</frameset>
```

使用`<noresize>`属性指定用户无法调整`<frame>`元素的大小：

`<frame noresize="noresize">`

HTML5 中不支持`<frame>`标签。

## 颜色

### 颜色值

HTML 颜色表示为十六进制值，0~F。零表示最低值，F表示最高值。

### 颜色模式

颜色以红色，绿色和蓝色光（RGB）的组合显示。

十六进制值使用＃标签符号，后跟六个十六进制字符。所有浏览器都支持 RGB 颜色值。
