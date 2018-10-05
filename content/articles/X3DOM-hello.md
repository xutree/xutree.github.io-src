Title: Hello，X3DOM！
Category: X3DOM
Date: 2018-10-04 18:29
Tags: X3DOM

本教程将教会你怎么配置和运行你的第一个X3DOM应用。你只需要一个相容于WebGL的浏览器和一个文本编辑器。整个X3DOM应用是常规网页的一部分，并且编写方式也与HTML很相似，所以如果你的编辑器支持HTML或者XML的语法高亮那将更好，像[WebStorm](http://www.jetbrains.com/webstorm/)这种Web编程IDE也是可以的。如果你手头有一个网页浏览器和一个文本编辑器，并且你知道怎么在浏览器中打开网页(参考[这里](https://doc.x3dom.org/gettingStarted/index.html))，那么你可以开始你的第一个X3DOM应用了。

首先，创建一个新文件 *HelloX3DOM.html*。然后将下面的内容复制粘贴进这个空文件：
```
<html>
    <head>
        <title>My first X3DOM page</title>
        <script type='text/javascript' src='http://www.x3dom.org/download/x3dom.js'> </script>
        <link rel='stylesheet' type='text/css' href='http://www.x3dom.org/download/x3dom.css'></link>
    </head>
    <body>
    <h1>Hello, X3DOM!</h1>
    <p>
        This is my first html page with some 3d objects.
    </p>
    </body>
</html>
```
如果你在浏览器中打开这个文件，你会看到一个包含一个文本信息的常规HTML页面。你可能已经注意到，我们已经在我们的网页中添加了一些X3DOM元素，因为我们已经包含X3DOM作为一个JaveScript库，还包含了X3DOM CSS文件，用于规则的显示X3DOM元素。在上面的HTML代码中，我们通过 *script* 和 *link* 标签是用了 *development* 版本的X3DOM。

让我们继续添加一些3D内容。首先，我们需要一个 *x3d* 元素，用来描述X3DOM内容在哪个 *scene* 显示。和HTML元素 *p*、*div* 类似，*x3d* 在HTML里定义了一个矩形范围。整个X3DOM的3D内容用 *scene* 描述，所以我们在 *x3d* 标签里添加一个 *scene* 标签。这种结构是来自于X3D标准。一个 *scene* 可以包含很多不同的 *node*，例如，*lights*、*groups*、*viewpoint* 和 *objects*。在第一个例子里，我们通过 *shape* 简单地定义一个3D物体。我们用 *box* 定义这个物体的几何形状。现在，你可以将下面的代码添加在你的HTML文件闭合 *p* 标签之后：
```
<x3d width='600px' height='400px'>
    <scene>
    <shape>
        <box></box>
    </shape>
    </scene>
</x3d>
```
如果你现在在浏览器中打开这个文件，会像下面这样：

![图1    注意box标签没有颜色，所以无法在图中看到]({filename}/images/fig1.png)

由于 *box* 目前没有颜色，所以无法看到它，为了看到它我们需要声明 *material*，X3DOM基于X3D标准选择了一个白色的 *material*，由于网页的背景也是白色的，所以我们看不到它。为了改变 *material* 的颜色，我们首先需要在 *shape* 中插入 *appearance*。在 *appearance* 里面，我们就可以插入 *material*，利用 *material* 的 *diffuseColor* 我们可以定义 *material* 的颜色，我们现在将它定义为RGB颜色的红色：
```
<shape>
    <appearance>
    <material diffuseColor='1 0 0'></material>
    </appearance>
    <box></box>
</shape>
```
现在，在你的浏览器中，网页将变成：

![图2    现在 *box* 具有红色的 *material*]({filename}/images/fig2.png)

现在，你可以利用鼠标进行交互了。按住鼠标左键并移动鼠标，你可以旋转视角，按住鼠标右键并移动鼠标，你可以放大和缩小。

我们继续在这个 *scene* 中添加两个物体：一个蓝色的球体和一个绿色的圆锥。这和我们添加 *box* 类似，但是，在 *sphere* 和 *cone* 节点处，我们需要移动球和圆锥以避免他们相互重叠，因为所有的3D物体都默认不进行任何的坐标转换，也就是说它们会重叠在一起。像X3D和其他的图像相关标准(例如，OpenGL)一样，X3DOM的坐标系统Y轴指向上，X轴指向右，Z轴指向外：

![图3  X3DOM的坐标系统]({filename}/images/fig3.png)

在添加绿色圆锥之前，我们将坐标往左移动3个单位；在添加蓝色球之前，我们将坐标往右移动3个单位。如下所示：
```
<shape>
    <appearance>
    <material diffuseColor='1 0 0'></material>
    </appearance>
    <box></box>
</shape>
<transform translation='-3 0 0'>
<shape>
    <appearance>
    <material diffuseColor='0 1 0'></material>
    </appearance>
    <cone></cone>
</shape>
</transform>
<transform translation='3 0 0'>
<shape>
    <appearance>
    <material diffuseColor='0 0 1'></material>
    </appearance>
    <sphere></sphere>
</shape>
</transform>
```
现在，在你的浏览器中，你将看到如下内容：

![图4 三个物体]({filename}/images/fig4.png)

如果你在浏览器中看到了图1.4的结果，恭喜你！你刚刚使用了一系列的X3D *node* 创建了你的第一个X3DOM *scene*。
