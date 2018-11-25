Title: X3DOM，HTML，CSS 和 JavaScript
Category: 教程
Date: 2018-10-05 11:22
Modified: 2018-10-06 21:02:31
Tags: X3DOM

本节，你将学习关于 X3DOM, HTML 和 CSS的更多知识，以及怎么利用 HTML 和 CSS 技术构建出强大的 3D 应用。在本节最后，你讲学习怎么在你的应用中使用 JavaScript。我们将继续使用前一节的例子。拷贝 HelloX3DOM.html 文件并重命名为 HTMLEventsCSS.html。

## X3DOM 和 CSS

我们首先来看下怎么通过 CSS 操控 X3DOM 元素。你可能已经注意到，在 HelloX3DOM.html 中，3D 内容位于一个被黑色边界包围的白色区域中。X3DOM 有一个单独的 css 文件，自从版本1.3以后，名字一直为 x3dom.css，在这个文件中可以找到关于 X3DOM 元素的所有 css 定义以及 debug 信息。假设你的页面使用灰色和橙色作为主要颜色。你可以通过许多方式改变 X3DOM 默认的 CSS 属性：

- 在 x3dom.css 后包含你自己的 CSS 文件(External Style Sheet)
- 在 x3dom.css 之后，利用 *style* 标签定制 css(Internal
Style Sheet)
- 直接操纵相关元素的 *style* 属性(Inline Styles)

关于 CSS 有很多网上教程，例如[这里](http://www.w3schools.com/css/css_howto.asp)。我们现在利用第二种方法改变 css，通常不推荐第三种方法。为了定制 x3d 代表的 X3DOM 边界，在你的 HTML 文件头部 x3dom.css 之后插入 *style* 标签：
```
<html>
    <head>
    <title>My first X3DOM page</title>
    <script type='text/javascript' src='http://www.x3dom.org/download/x3dom.js'> </script>
    <link rel='stylesheet' type='text/css' href='http://www.x3dom.org/download/x3dom.css'></link>
    <style>
        x3d
        {
            border:2px solid darkorange;
        }
    </style>
</head>
<body>
    <h1>Hello, X3DOM!</h1>
    <p>
    This is my first html page with some 3d objects.
    </p>
    <x3d width='600px' height='400px'>
    ...
    </x3d>

</body>
</html>
```
现在，X3DOM 的边界颜色已经改变了。假设你的网页已经有了橙色和灰色风格，使用 *pattern.png* 作为背景(背景图片在[这里](https://doc.x3dom.org/tutorials/basics/htmlCSS/pattern.png))。那么完整的 *style sheet* 如下所示：
```
x3d
{
    border:2px solid darkorange;
}
body
{
    font-size:110%;
    font-family:verdana, sans-serif;
    background-image: url('pattern.png');
    margin: 3em;
    color: lightgray;
}
h1
{
    color: darkorange;
}
```
现在你的网页看起来如下所示：

![图1  默认情况下，X3DOM使用与网页相同的背景]({filename}/images/fig5.png)

从图中可以看出，X3DOM 使用与网页相同的背景。这是一个很重要的行为：你的 X3DOM *scene* 是在 HTML 之上进行渲染的。让我们设置 *x3d* 元素为半透明背景：
```
x3d
{
    border:2px solid darkorange;
    background: rgba(128, 128, 128, 0.4);
}
```
现在结果看起来如下所示：

![图2  具有半透明背景的X3DOM]({filename}/images/fig6.png)

## X3DOM, HTML 事件和 JavaScript

使用 HTML 和 JavaScript，你可以使用大量有用的回调函数来操纵大多数 DOM 元素。X3DOM 为 *node* 提供了相似的函数。例如，当我们点击红色立方体的时候，可以弹出一个文本信息，在 *shape* 里插入一个 *onclick* 函数就可以实现这个功能：
```
<shape onclick="alert('Hello, click!');">
    <appearance>
    <material diffuseColor='1 0 0'></material>
    </appearance>
    <box></box>
</shape>
```

目前，你可以对 X3DOM 使用 *onmousemove*，*onmousedown*， *onmouseup*，*onmouseover* 和 *onmouseout* 事件。你不仅可以在 *shape* 节点插入事件，也可以在组节点，例如 *transform* 插入事件。这样你就可以使用一个回调函数捕捉多个节点的事件。

你可以在每个 DOM 元素上使用 JavaScript，所以你可以随心所欲的操纵 *node*。你已经知道怎么使用 *onclick* 事件，让我们尝试当点击时，改变立方体的颜色。如果你从没使用过 JavaScript，这个[网站](http://www.w3schools.com/js/default.asp)或许可以帮助你。

首先，给你想操纵的节点一个 *id*：
```
<shape onclick="alert('Hello, click!');">
    <appearance>
    <material id="color" diffuseColor='1 0 0'></material>
    </appearance>
    <box></box>
</shape>
```
然后，你就可以通过下面这个函数改变颜色：
```
<script>
    function changeColor()
    {
        if(document.getElementById("color").getAttribute('diffuseColor')=="1 0 0")
            document.getElementById("color").setAttribute('diffuseColor', '0 0 1');
        else
            document.getElementById("color").setAttribute('diffuseColor', '1 0 0');
    }
</script>
```
```
<shape onclick="changeColor();">
```

## 下一步：自动创建 (X)HTML

如果你有大量的模型数据，你想把这些数据分配到不同的页面上。那么自动生成实际的页面而不是手动编写代码将更加有趣。你可以使用自动化工具，例如 XSLT，允许你直接将 X3DOM 文件转化为 XHTML 网页。[这里](http://www.web3d.org/x3d/stylesheets/X3dToXhtmlStylesheetExamples.zip)是一个例子。
