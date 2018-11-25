Title: 几个奇葩的 Linux 命令
Category: 趣闻
Date: 2018-10-08 22:58:12
Modified: 2018-10-09 11:39:49
Tags: Linux

Linux 中有一些很奇葩的命令，可能你的发行版默认没有安装，你可以自己安装：
```
[me@linuxbox ~]$ apt-get install 命令          (Debian)
[me@linuxbox ~]$ yum install 命令              (Red Hat）
[me@linuxbox ~]$ brew install 命令            （Mac）
```
## rev

`rev`命令反转输入的内容（来自文件或者标准输入或者管道）：
```
[me@linuxbox ~]$ echo Hello, World! | rev
!dlroW ,olleH
```

## tac

`cat`命令的反写，执行效果也和`cat`相反，即，将文件列表中的每一个文件输出到标准输出，行号大的优先。

## sl

你可能知道命令`ls`,并经常使用它来查看文件夹的内容。但是由于错误输入有时会导致`sl`，如何在终端获得一点乐趣而不是“command not found”？`sl`命令！

当你把`ls`错误打成`sl`时，一辆蒸汽机车（**s**team **l**ocomotive）会在屏幕上驶过...

![图1 一辆蒸汽机车（steam locomotive）会在屏幕上驶过]({static}/images/linux_1.png)

## yes

yes命令将进入一个循环，一遍又一遍地重复相同的字符串。默认重复“y”，你可以指定其他字符串。

```
[me@linuxbox ~]$ yes "这是一个测试"
这是一个测试
这是一个测试
这是一个测试
这是一个测试
这是一个测试
这是一个测试
这是一个测试
```

利用`Ctrl C`终止。

## cowsay

屏幕上会出现一只 ASCII 码拼成的奶牛。。。你可以指定奶牛要说的话。这个命令还有其他版本，如`xcowsay`，`cowthink`。

![图2 一只 ASCII 码拼成的奶牛]({static}/images/linux_2.png)

## figlet

这个算不上奇葩，他它利用 ASCII 码拼成你输出字符串的横幅，而且有许多参数可以定制。还有个`toilet`命令和`figlet`很类似。比如，`figlet good`：

![图3 利用 ASCII 码拼成你输出字符串的横幅]({static}/images/linux_3.png)

## fortune

会显示你的未来（ 😆 )。可以试试：`[me@linuxbox ~]$ fortune | cowsay`

![图4 显示未来的奶牛]({static}/images/linux_4.png)

## cmatrix

会像《黑客帝国》里那样显示。

![图5 黑客帝国]({static}/images/linux_5.png)

## Fork 炸弹

```
[me@linuxbox ~]$ :(){ :|:& }:
```

不要尝试不要尝试不要尝试...

## asciiquarium 水族馆

![图6 水族馆]({static}/images/linux_6.png)

## lolcat

`lolcat`可以在终端产生彩虹。

`lolcat`是一个 RubyGem 因此它必须有你的系统上安装了 Ruby 的最新版本。利用文章开头部分的方法安装好`lolcat`
后，在终端执行`gem install lolcat`安装。

`[me@linuxbox ~]$ git log -1 | cowsay -f dragon-and-cow | lolcat`

![图7 lolcat]({static}/images/linux_7.png)

`lolcat`接受管道输入，所以你可以试试：`[me@linuxbox ~]$ sl | lolcat`
