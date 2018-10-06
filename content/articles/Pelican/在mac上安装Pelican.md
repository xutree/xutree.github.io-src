Title: 安装 Pelican
Category: 教程
Date: 2018-10-04 10:20
Modified: 2018-10-06 21:15:21
Tags: Pelican

## 安装 Pelican
[Pelican](https://blog.getpelican.com/)目前支持最好的是 Python 2.7 和 3.3+，早期版本的 Python 已经不支持了。有许多不同的方法可以安装 Pelican，最简单的方法是使用 pip，在终端输入：
```
    pip install pelican
```
上面是最简单的方法，官方更为推荐的方法是利用 [virtualenv](http://www.virtualenv.org/) 为 Pelican 建立一个虚拟环境。假设你已经安装好了 virtualenv，下面打开终端，开始为 Pelican 新建一个虚拟环境：
```
    virtualenv ~/virtualenv/pelican
    cd ~/virtualenv/pelican
    source bin/activate
```
当虚拟环境被创建并激活以后，然后利用`pip install pelican`安装 Pelican。

当 Pelican 安装好以后，你可以在终端输入`pelican --help`查看使用选项。

## 可选的 Packages
如果你计划用 [Markdown](http://pypi.python.org/pypi/Markdown) 来书写你的网页的话，你需要安装 Markdown：`pip install Markdown`

通过设置 Pelican 的 pelicanconf.py 文件，你可以对生成的 HTML 文件启用增强语法。但是首先你需要安装 [Typogrify](https://pypi.org/project/typogrify/)：`pip install typorify`

## 更新
更新到最新的稳定版本，使用：
`pip install --upgrade pelican`
