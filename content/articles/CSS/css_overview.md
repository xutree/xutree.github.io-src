Title: CSS 入门
Category: CSS
Date: 2018-10-07 11:24:03
Modified: 2018-10-07 12:29:23
Tags: CSS

## 什么是 CSS

CSS（**C** ascading **S** tyle **S** heets），即层叠样式表。

层叠是指 CSS 将一种样式应用于另一种样式的方式。样式表控制 Web 文档的外观。

## 为什么使用 CSS

- CSS 允许你将特定样式应用于特定 HTML 元素
- CSS 的主要好处是它允许您将样式与内容分开
- 仅使用 HTML，所有样式和格式都在同一个地方，随着页面的增长，这变得相当难以维护

## CSS 三种形式

### 内联 CSS：inline CSS

使用内联样式是插入样式表的方法之一。 使用内联样式，将独特的样式应用于单个元素。

要使用内联样式，请将style属性添加到相关标记。

```
<p style="color:white; background-color:gray;">
    This is an example of inline styling.
</p>
```

### 嵌入式/内部 CSS：Embedded/Internal CSS

内部样式在 HTML 页面的`head`部分内的`<style>`元素中定义。

```
<html>
   <head>
      <style>
      p {
         color:white;
         background-color:gray;
      }
      </style>
   </head>
   <body>
      <p>This is my first paragraph. </p>
      <p>This is my second paragraph. </p>
   </body>
</html>
```

### 外部 CSS：External CSS

使用此方法，所有样式规则都包含在单个文本文件中，该文件以 .css 扩展名保存。

然后使用`<link>`标记在 HTML 中引用此 CSS 文件。`<link>`元素位于`head`部分内部。

```
<head>
   <link rel="stylesheet" href="example.css">
</head>
<body>
   <p>This is my first paragraph.</p>
   <p>This is my second paragraph. </p>
   <p>This is my third paragraph. </p>
</body>
```

## CSS 语法

CSS 由浏览器解释的样式规则组成，然后应用于文档中的相应元素。样式规则有三个部分：`selector`，`property`和`value`。

例如，标题颜色可以定义为：`h1 { color: orange; }`

选择器指向要设置样式的HTML元素。声明块包含一个或多个声明，以分号分隔。每个声明都包含一个属性名称和一个以冒号分隔的值。CSS 声明始终以分号结尾，声明组由大括号括起。

### 类型选择器

最常见且易于理解的选择器是类型选择器。 此选择器针对页面上的元素类型。

例如，要定位页面上的所有段落：

```
p {
   color: red;
   font-size:130%;
}
```

### id 和 clss 选择器

id 选择器允许您设置具有 id 属性的 HTML 元素的样式，而不管它们在文档树中的位置如何。 以下是 id 选择器的示例：

HTML 文件：

```
<div id="intro">
   <p> This paragraph is in the intro section.</p>
</div>
<p> This paragraph is not in the intro section.</p>
```

CSS 文件:

```
#intro {
   color: white;
   background-color: gray;
}
```

要选择具有特定 id 的元素，请使用井号 **#** 字符，然后使用元素的 id 跟随它。

类选择器以类似的方式工作。 主要区别在于 id 每页只能应用一次，而类可以根据需要在页面上多次使用。

在下面的示例中，具有“first”类的两个段落都将受到 CSS 的影响：

HTML 文件：

```
<div>
   <p class="first">This is a paragraph</p>
   <p> This is the second paragraph. </p>
</div>
<p class="first"> This is not in the intro section</p>
<p> The second paragraph is not in the intro section. </p>
```

CSS 文件：

```
.first {font-size: 200%;}
```

要选择具有特定类的元素，请使用句点 **.** 字符，后跟类的名称。不要用数字开始一个类或 id 名称。

### 后代选择器

这些选择器用于选择作为另一个元素的后代的元素。 选择级别时，您可以根据需要选择多个级别。

例如，要仅定位“intro”部分第一段中的 <em\> 元素：

HTML 文件：

```
<div id="intro">
   <p class="first">This is a <em> paragraph.</em></p>
   <p> This is the second paragraph. </p>
</div>
<p class="first"> This is not in the intro section.</p>
<p> The second paragraph is not in the intro section. </p>
```

CSS 文件：

```
#intro .first em {
   color: pink;
   background-color:gray;
}
```

后代选择器匹配作为指定元素后代的所有元素。

## 注释

注释用于解释你的代码，浏览器会忽略。`/* Comment goes here */`

## 层叠

网页的最终外观是不同样式规则的结果。形成层叠的三种主要风格来源是：

- 页面作者创建的样式表
- 浏览器的默认样式
- 用户指定的样式

继承是指属性在页面中流动的方式。 除非另有定义，否则子元素通常会采用父元素的特征。
