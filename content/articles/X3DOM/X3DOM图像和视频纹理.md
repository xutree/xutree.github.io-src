Title: X3DOM 图像和视频纹理
Category: 教程
Date: 2018-10-05 17:14
Modified: 2018-10-06 21:02:53
Tags: X3DOM

本章你将知道哪些图像类型和视频格式可以用作 X3DOM 的纹理，以及纹理的特性和限制。

你可以使用 [*PNG*](http://en.wikipedia.org/wiki/Portable_Network_Graphics)，[*LPEG*](http://en.wikipedia.org/wiki/Jpeg) 或者 [*GIF*](https://en.wikipedia.org/wiki/Gif) 来编码你的静态纹理数据。*JPG* 图像需要的内存少但是存在压缩损失而且没有 *alpha* 通道。*PNG* 图像属于无损压缩并且有 *alpha* 通道，*GIF* 也是无损压缩并且有 *alpha* 通道。一般来讲：如果你不需要 *alpha* 通道并且图像中不包含硬边界(例如：文本)，使用 *JPG*，否则使用 *PNG*。你应该避免使用 *GIF*。

## 图像

利用 *ImageTexture* 节点把图像作为纹理：
```
<x3d width='500px' height='400px'>
<scene>
    <shape>
    <appearance>
    <ImageTexture url="myTexture.png"><ImageTexture/>
    </appearance>
    <box> </box>
    </shape>
</scene>
</x3d>
```

## 视频

利用 *MovieTexture* 节点可以把视频作为纹理。但是目前还没有哪一种视频格式支持所有的用户。可以使用 X3DOM 格式[示例](https://x3dom.org/x3dom/example/x3dom_video.xhtml)来确定你的浏览器支持的格式。目前最好的解决方法是将你的视频编码成 *MP4* 和 *OGV* 格式并在 *MovieTexture* 节点中提供这两个选项：
```
<x3d width='500px' height='400px'>
<scene>
    <shape>
    <appearance>
    <MovieTexture url='”foo.mp4″,”foo.ogv”'><MovieTexture/>
    </appearance>
    <box> </box>
    </shape>
</scene>
</x3d>
```
