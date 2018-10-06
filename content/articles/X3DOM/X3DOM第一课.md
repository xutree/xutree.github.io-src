Title: X3DOM 第一课
Category: X3DOM
Date: 2018-10-04 11:31
Modified: 2018-10-06 21:13:34
Tags: X3DOM

下面的指南可以作为 X3DOM 使用者和开发者的入门资料。本指南包括许多重要的内容，例如怎么配置你的环境去运行 X3DOM 的示例。如果你没有足够的时间阅读这篇入门文章，又或许你已经熟悉一点关于 X3D 的知识，你可以迅速的浏览下第3部分和第4部分的一些内容去设置你的环境，然后根据[tutorials](https://doc.x3dom.org/tutorials/index.html)的指导去完成你的第一个 X3DOM 应用。

## 背景：什么是X3DOM，它可以用来做什么？

### 无需插件即可在浏览器中显示的3D场景

X3DOM（发音：“X-Freedom”）是一个开源的 JaveScript 框架，用于在网页中创建 declarative 3D 场景。由于它基于标准的浏览器技术，你的浏览器不需要其他任何插件就可以显示 X3DOM 场景。概括地说，declarative 3D 意味着你可以使用结构化的文本表示去创建和显示 3D 场景，而不需要去编写代码。在 X3DOM 中，这种文本表示是表示网页的 HTML 文件的一部分。也就是说，3D 内容成为了网页元素的一部分，就像网页中的文本、链接、图片和视频一样。

### X3DOM = X3D + DOM

X3DOM 这个名字是由两个缩写组合而成。第一个缩写是[X3D](http://www.web3d.org/x3d/what-x3d)（“Extensible 3D Graphics”），指代一个 3D 图形的免版税 ISO 标准。第二个缩写是[DOM](https://www.w3.org/DOM/)（“Document Object Model”），描述与HTML文档的内容相关联的交互概念和分层表示。X3DOM 使用 X3D 的一个专门的子集（所谓的[HTML Profile](https://www.x3dom.org/nodes-2/)）来作为网页内 3D 内容的描述语言。X3D（OM)元素可以通过 DOM 操作，就像其他的 HTML 元素一样。例如，你可以动态地改变一个 3D 物体的颜色通过 JavaScript 调用相应 DOM 元素的 *setAttribute(...)* 函数，这就像你可以动态改变一个普通网页里一个标签的内容一样。

### 使用 X3DOM 的原因

使用 X3DOM 而不是其他的基于浏览器的库或者 X3D 播放器是因为 X3DOM 具有以下几个优势：

- 显示 X3DOM 场景不需要额外插件，因为 X3DOM 是完全基于标准浏览器技术，例如[HTML5](http://www.w3schools.com/html/html5_intro.asp)和[WebGL](http://get.webgl.org/)
- 基于 ISO 标准 X3D 的一种新的 HTML 配置，X3DOM 绝大部分都是标准一致的。这大大方便了 X3DOM 的学习
- 从2009年至今，X3DOM 已经具有了很大的使用者和开发者群体
- 如果你知道怎么创建简单的网页，你就可以利用你现有的关于 HTML 和 DOM 的知识，而不需要学习新的 API

### 怎么做？

如果你想开发你的第一个 X3DOM 应用，你只需要一个浏览器和一个文本编辑器。当然，你也可以选择功能更多的 HTML 和 JavaScript 开发环境，比如[WebStorm](http://www.jetbrains.com/webstorm/)。

## 一些基本 X3D 概念：Nodes、Components 和 Profiles

### X3D Nodes

X3D 定义每一个 3D 场景都是由一组 node 组成。每一个 node 代表 3D 场景中一个确定的部分：光线、物体、物体表面的材质等等。场景里的所用 node 排列成树结构或者图结构，整体结构被叫做 *scene-graph*。每一个 node 的行为，比如材质的颜色，可以通过node的 *fields* 设置。例如，一个用来设置某物体表面颜色为红色（RGB编码 1 0 0）的node的 XML 描述为：

```
<Material diffuseColor='1 0 0'></Material>
```
你可能已经意识到，描述 X3D node 的 XML 很像常规的 HTML 代码，属性值 *diffuseColor* 的设置也像 HTML 属性的设置一样。事实上，如果你熟悉 HTML，那么就很容易理解 X3DOM 中的 node 了。你可以在[tutorials](https://doc.x3dom.org/tutorials/index.html)中学习怎样使用 node。如果你想了解更多 X3D 中 node 的概念，可以参考[external X3D documentation resources](https://doc.x3dom.org/index.html#X3DExternalDoc)。

### X3D Components

一组具有相同功能的 node 称为 components。例如定义光线的 node，*PointLight* 和 *SpotLight*，在 *Lighting* component 里。关于 Components 的全部信息可以在[这里](https://doc.x3dom.org/node/Components.html)找到。

### X3D Profiles 和 X3DOM HTML Profile

X3D 标准定义了大量的 node，一些特殊用途的 node 对大多说用户来说并不重要。因此，X3D 引入了 profile 的概念，把许多组 node 放在一起成为一个包，每一个包代表一类特殊的应用。例如，*CAD* 包，*Immersive* 包是用于交互环境的。profile 是在 component 之上的一个概念。

X3DOM 使用的 X3D component 经过十分仔细的选择，以提供一个最合适的 X3D 子集来满足现代 HTML 应用的需要。X3DOM 通过定义一个特殊的 profile，即 HTML profile，来解决这一问题。这个 HTML profile 也包括一些处于试验阶段的 X3D 没有的 node 和 filed，这些 node 和 filed 是专门为 X3DOM 设计的。具体来说，有些 X3D node 在 X3DOM 里没有，而有些 node X3DOM 里有但是 X3D 里没有。你可以在[这里](https://doc.x3dom.org/author/index.html)找到每个 node 的起源。如果你想学习更多关于 HTML profile 的知识以及它与现有的 X3D component、profile 的关系，可以查看[这里](http://www.x3dom.org/?page_id=158)。

最后，X3DOM 也提供一些不在原始HTML profile 中的 X3D node。这些 node 不在 X3DOM 的标准发行版本中，只在 *X3DOM-Full* 版本中。

## 选择一个 X3DOM 版本

### 版本和 Components

有许多可供选择的 X3DOM 版本，你可能想知道对特殊的目的哪一个才是最好的。一般来讲，我们推荐最新的 release 版本。但是，如果你需要采用的新特性在 release 版中没有，那么 dev 版本可能更适合你。当你完成了网页应用的主要开发工作进而部署时，你可能需要用来开发的 X3DOM 的版本信息。你也可能，出于某种原因需要老版本的 X3DOM，比如你的网页应用包含了一些试验特性只在老版本出现，而在新版本中被移除了。

所有的 X3DOM release 版本，包括 dev 版本，都被打包好了，里面包括一个 JavaScript 文件（如 x3dom.js），一个 css文件（如 x3dom.css）和一个可选的 shockwave 文件（如 x3dom.swf，对于那些支持 flash 的版本），可在[这里](http://x3dom.org/download/)下载：

- 版本1.0到1.2的文件以 x3dom-v 标记，后面跟着版本号（如[ http://x3dom.org/download/x3dom-v1.1.js]( http://x3dom.org/download/x3dom-v1.1.js)）
- 从版本1.3开始，x3dom.js, x3dom.css, x3dom.swf 和一个 .zip 存档文件b被放置在一个以版本号为名字的子文件夹里（如[ http://x3dom.org/download/1.3/x3dom.js]( http://x3dom.org/download/1.3/x3dom.js)）
- 从版本1.3开始，一些 HTML profile 之外的 component 出现了。这些 component 在文件 x3dom-full.js 中。如果你只需要使用其中一个 component，你也可以考虑仍使用 x3dom.js 然后包含所需的 component 的文件（如[ http://x3dom.org/download/1.3/components/]( http://x3dom.org/download/1.3/components/)）
- 最新的稳定 release 版总是位于：[http://x3dom.org/release/x3dom.js](http://x3dom.org/release/x3dom.js)
- 目前的 development 版本总是位于 dec 子文件夹：[http://x3dom.org/download/dev/x3dom.js](http://x3dom.org/download/dev/x3dom.js)

为使用最新版本 release X3DOM，你可以在你的HTML页面中包含下面的标签：
```
<script src="http://www.x3dom.org/release/x3dom.js"></script>
<link rel="stylesheet" href="http://www.x3dom.org/release/x3dom.css">
```
为使用最新的 development 版本，使用下面的标签：
```
<script src="http://www.x3dom.org/download/dev/x3dom.js"></script>
<link rel="stylesheet" href="http://www.x3dom.org/download/dev/x3dom.css">
```
为使用版本1.5的 X3DOM-Full 版本，使用下面的标签：
```
<script src="http://www.x3dom.org/download/1.5/x3dom-full.js"></script>
<link rel="stylesheet" href="http://www.x3dom.org/download/1.5/x3dom.css">
```
最后，为使用1.3版本的 release X3DOM 和额外的 Geospatial component 和另外的 flash 支持，使用下面的标签：
```
<script src="http://www.x3dom.org/download/1.3/x3dom.js"></script>
<script src="http://www.x3dom.org/download/1.3/components/Geospatial.js"></script>
<script src="http://www.x3dom.org/download/1.3/x3dom.swf"></script>
<link rel="stylesheet" href="http://www.x3dom.org/download/1.3/x3dom.css">
```

### Debugging

如果在 debug 你的应用的时候你想看到 X3DOM 的源码，只需将 x3dom.js 替换成 x3dom.debug.js 或者将 x3dom-full.js 替换成 x3dom-full.debug.js。其注意，此特性只适用于版本1.4以后的 X3DOM。相比于常规版本，debug 版本包含缩进和注释，所以比较大。所以，当你最终发布你的 Web 应用时，请不要使用 debug 版本的 js。

## 运行 X3DOM 应用

### 通过简单的 Python 服务器

一个简便的方法在服务器上来测试你的 Web 应用是使用 Python 的 HTTP 服务器模块。你只需要安装一个 Python 解释器。你可以在[这里](http://python.org/)下载。你可以用 Python 做许多有趣的事情。首先，打开命令行窗口，定位到 X3DOM 文件夹。如果你的 Python 是2.X版本，你可以使用 *SimpleHTTP* 服务器模块如下所示：
```
python -m SimpleHTTPServer
```
如果你的 Python 是3.x版本，如下所示：
```
python3 -m http.server
```
默认情况下，服务器使用8000端口。如果你想改变端口，直接在命令后面加上端口号即可，例如：
```
python -m SimpleHTTPServer 8023
```
然后，通过浏览器输入如下地址就可以到达你的服务器：
```
http://localhost:8023
```
如果你在启动 Python 服务器的文件夹里放置了 index.html 文件，那么这个文件的内容就会显示在浏览器窗口里。否则，你会看到服务器所在文件夹内的文件列表。

### 在 Web 服务器上运行 X3DOM

通常，你会在Web服务器上运行你的 X3DOM 应用，本节针对一些普通的 Web 服务器，如 Apache 和 IIS，给出具体的方法。

Apache 是使用最多的 Web 服务器。它是开源的可以在[这里](http://httpd.apache.org/)下载。最新版本是2.4，但是版本2.2仍然被支持。

如果你的应用需要一整套 Web 服务器组件，我们推荐[XAMPP](https://www.apachefriends.org/index.html)，它包含 Apache、MySQL、PHP 和 Perl 的最新发行版。

互联网信息服务（IIS）被集成在微软的任何的最新版本的 Windows 当中。但是，对于非服务器操作系统，同时连接数会受到限制。
