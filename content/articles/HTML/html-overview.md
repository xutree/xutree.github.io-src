Title: HTML 入门
Category: 教程
Date: 2018-10-05 17:23
Modified: 2018-10-15 21:17:20
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
|`<!DOCTYPE html>`|声明为 HTML5 文档|

下面是 HTML 版本的“Hello, World！”程序：
```
<!DOCTYPE html>
<html>
   <head>
      <meta charset="utf-8">
      <title>第一个 HTML 例子</title>
   </head>
   <body>
      Hello World!
   </body>
</html>
```

## <!DOCTYPE> 声明

`<!DOCTYPE>`声明有助于浏览器中正确显示网页。网络上有很多不同的文件，如果能够正确声明 HTML 的版本，浏览器就能正确显示网页内容。`doctype`声明是不区分大小写的，以下方式均可：

```
<!DOCTYPE html>
<!DOCTYPE HTML>
<!doctype html>
<!Doctype Html>
```

## 中文编码

目前在大部分浏览器中，直接输出中文会出现中文乱码的情况，这时候我们就需要在头部将字符声明为`<meta charset="utf-8">`。

## 字体标签

|标签|解释|
|--|---|
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

双引号是最常用的，不过使用单引号也没有问题。属性的数值可以通过像素或百分比指定，如

```
<hr width="50px" />
<hr width="50%" />
```

### HTML 全局属性

加粗为 HTML5 新属性。

| 属性 | 描述 |
| :------------- | :------------- |
| accesskey | 设置访问元素的键盘快捷键 |
|class|	规定元素的类名（classname）|
|**contenteditable**|	规定是否可编辑元素的内容|
|**contextmenu**|指定一个元素的上下文菜单，当用户右击该元素，出现上下文菜单|
|**data-\***|	用于存储页面的自定义数据|
|dir	|设置元素中内容的文本方向|
|**draggable**|	指定某个元素是否可以拖动|
|**dropzone**|	指定是否将数据复制，移动，或链接，或删除|
|**hidden**|	hidden 属性规定对元素进行隐藏|
|id|	规定元素的唯一 id|
|lang|	设置元素中内容的语言代码|
|**spellcheck**|	检测元素是否拼写错误|
|style	|规定元素的行内样式（inline style）|
|tabindex|	设置元素的 Tab 键控制次序|
|title|	规定元素的额外信息（可在工具提示中显示）|
|**translate**|	指定是否一个元素的值在页面载入时是否需要翻译|

#### HTML 标签

加粗为 HTML5 新标签。

| 标签 | 描述 |
| :------------- | :------------- |
|<!--...-->	|定义注释|
|<!DOCTYPE>	|定义文档类型
|<abbr>|	定义缩写|
|<acronym>|	定义只取首字母的缩写，不支持 HTML5|
|<address>|	定义文档作者或拥有者的联系信息|
|<applet>|	HTML5 中不赞成使用，定义嵌入的 applet|
|<area>|	定义图像映射内部的区域|
|**<article>**|	定义一个文章区域|
|**<aside>**|	定义页面的侧边栏内容|
|**<audio>**|	定义音频内容|
|<b>|	定义文本粗体|
|<base>|	定义页面中所有链接的默认地址或默认目标|
|<basefont>|	HTML5 不支持，不赞成使用，定义页面中文本的默认字体、颜色或尺寸|
|**<bdi>**|允许您设置一段文本，使其脱离其父元素的文本方向设置|
|<bdo>|	定义文字方向|
|<big>|	定义大号文本，HTML5 不支持|
|<blockquote>|	定义长的引用|
|<body>|	定义文档的主体|
|<br>|	定义换行|
|<button>|	定义一个点击按钮|
|**<canvas>**|	定义图形，比如图表和其他图像,标签只是图形容器，您必须使用脚本来绘制图形|
|<caption>|	定义表格标题|
|<center>|	HTML5 不支持，不赞成使用，定义居中文本|
|<cite>|	定义引用(citation)|
|<code>|	定义计算机代码文本|
|<col>|	定义表格中一个或多个列的属性值|
|<colgroup>|	定义表格中供格式化的列组|
|**<command>**|	定义命令按钮，比如单选按钮、复选框或按钮|
|**<datalist>**|	定义选项列表，请与 input 元素配合使用该元素，来定义 input 可能的值|
|<dd>|	定义定义列表中项目的描述|
|<del>|	定义被删除文本|
|**<details>**|	用于描述文档或文档某个部分的细节|
|<dfn>|	定义定义项目|
|**<dialog>**|	定义对话框，比如提示框|
|<dir>|	HTML5 不支持，不赞成使用，定义目录列表|
|<div>|	定义文档中的节|
|<dl>|	定义列表详情|
|<dt>|	定义列表中的项目|
|<em>|	定义强调文本|
|**<embed>**|	定义嵌入的内容，比如插件|
|<fieldset>|	定义围绕表单中元素的边框|
|**<figcaption>**|	定义 <figure> 元素的标题|
|**<figure>**|	规定独立的流内容（图像、图表、照片、代码等等）|
|<font>|	HTML5 不支持，不赞成使用，定义文字的字体、尺寸和颜色|
|**<footer>**|	定义 section 或 document 的页脚|
|<form>|	定义了 HTML 文档的表单|
|<frame>|	定义框架集的窗口或框架|
|<frameset>|	定义框架集|
|<h1>-<h6>|	定义 HTML 标题|
|<head>|	定义关于文档的信息|
|**<header>**|	定义了文档的头部区域|
|<hr>|	定义水平线|
|<html>|	定义 HTML 文档|
|<i>|	定义斜体字|
|<iframe>|	定义内联框架|
|<img>|	定义图像|
|<input>|	定义输入控件|
|<ins>|	定义被插入文本|
|<kbd>|	定义键盘文本|
|**<keygen>**|	规定用于表单的密钥对生成器字段|
|<label>|	定义 input 元素的标注|
|<legend>|	定义 fieldset 元素的标题|
|<li>|	定义列表的项目|
|<link>|	定义文档与外部资源的关系|
|<map>|	定义图像映射|
|**<mark>**|	定义带有记号的文本，请在需要突出显示文本时使用 <m> 标签|
|<menu>|	不赞成使用，定义菜单列表|
|<meta>|	定义关于 HTML 文档的元信息|
|**<meter>**|	定义度量衡，仅用于已知最大和最小值的度量|
|**<nav>**|	定义导航链接的部分|
|<noframes>|	定义针对不支持框架的用户的替代内容，HTML5 不支持|
|<noscript>|	定义针对不支持客户端脚本的用户的替代内容|
|<object>|	定义内嵌对象|
|<ol>|	定义有序列表|
|<optgroup>|	定义选择列表中相关选项的组合|
|<option>|	定义选择列表中的选项|
|**<output>**|	定义不同类型的输出，比如脚本的输出|
|<p>|	定义段落|
|<param>|	定义对象的参数|
|<pre>|	定义预格式文本|
|**<progress>**|	定义运行中的进度（进程）|
|<q>|	定义短的引用|
|**<rp>**|	<rp> 标签在 ruby 注释中使用，以定义不支持 ruby 元素的浏览器所显示的内容|
|**<rt>**|	<rt> 标签定义字符（中文注音或字符）的解释或发音|
|**<ruby>**|	<ruby> 标签定义 ruby 注释（中文注音或字符）|
|<s>|	不赞成使用，定义加删除线的文本|
|<samp>|	定义计算机代码样本|
|<script>|	定义客户端脚本|
|**<section>**|	<section> 标签定义文档中的节（section、区段），比如章节、页眉、页脚或文档中的其他部分|
|<select>|	定义选择列表（下拉列表）|
|<small>|	定义小号文本|
|**<source>**|	<source> 标签为媒介元素（比如 <video> 和 <audio>）定义媒介资源|
|<span>|	定义文档中的节|
|<strike>|	HTML5 不支持，不赞成使用定义加删除线文本|
|<strong>|	定义强调文本|
|<style>|	定义文档的样式信息|
|<sub>|	定义下标文本|
|**<summary>**|	<summary> 标签包含 details 元素的标题，"details" 元素用于描述有关文档或文档片段的详细信息|
|<sup>|	定义上标文本|
|<table>|	定义表格|
|<tbody>|	定义表格中的主体内容|
|<td>|	定义表格中的单元|
|<textarea>|	定义多行的文本输入控件|
|<tfoot>|	定义表格中的表注内容（脚注）|
|<th>|	定义表格中的表头单元格|
|<thead>|	定义表格中的表头内容|
|**<time>**|	定义日期或时间，或者两者|
|<title>|	定义文档的标题|
|<tr>|	定义表格中的行|
|**<track>**|	<track> 标签为诸如 video 元素之类的媒介规定外部文本轨道|
|<tt>|	定义打字机文本|
|<u>|	不赞成使用定义下划线文本|
|<ul>|	定义无序列表|
|<var>|	定义文本的变量部分|
|**<video>**|	<video> 标签定义视频，比如电影片段或其他视频流|
|**<wbr>**|	规定在文本中的何处适合添加换行符|

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

在 HTML 中，大多数元素被定义为块级或内联元素。|

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
