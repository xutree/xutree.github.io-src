Title: Atom 快捷键
Category: 教程
Date: 2018-10-16 14:47:35
Modified: 2018-10-16 15:55:00
Tags: Atom, Mac

参考：[https://www.jianshu.com/p/e33f864981bb](https://www.jianshu.com/p/e33f864981bb)、[https://github.com/nwinkler/atom-keyboard-shortcuts](https://github.com/nwinkler/atom-keyboard-shortcuts)

## 基本快捷键

|快捷键|快捷键的功能|
|:---|:---------|
|`cmd-,`|打开设置面板|
|`shift-cmd-p`|打开和关闭命令面板|
|`ctrl-alt-cmd-l`|重启|
|`alt-cmd-i`|打开开发者工具|

## 文件切换

|快捷键|快捷键的功能|
|:---|:---------|
|`cmd-shift-o`|打开目录|
|`ctrl-0`|焦点移到目录树,注意这里是数字0，非常实用也可以用cmd+\\来变相达到效果|
|`a, m, d, delete`|目录树下，增加，修改，另存为和删除|
|`cmd-t 或 cmd-p`|查找文件（模糊查找）|
|`cmd-b`|在打开的文件之间切换|
|`cmd-shift-b`|只搜索从上次 git commit 后修改或者新增的文件|
|`alt-cmd-left`|在打开的标签页往左切换|
|`alt-cmd-right`|在打开的标签页往右切换|

## 导航

|快捷键|快捷键的功能|
|:----|:---------|
|`ctrl-p`|前一行|
|`ctrl-n`|后一行|
|`ctrl-f`|后一个字符|
|`ctrl-b`|前一个字符|
|`alt-b, alt-left`|移动到单词开始|
|`alt-f, alt-right`|移动到单词末尾|
|`cmd-right, ctrl-e`|移动到一行结束|
|`cmd-left, ctrl-a`|移动到一行开始|
|`cmd-up`|移动到文件开始|
|`cmd-down`|移动到文件结束|
|`cmd-r`|在方法之间跳转|

## 窗口管理

|快捷键|快捷键的功能|
|:----|:---------|
|`cmd-n`|新建文件|
|`shift-cmd-n`|新建窗口|
|`cmd-o`|打开文件|
|`cmd-shift-o`|打开文件夹|
|`cmd-s`|保存|
|`shift-cmd-s`|另存为|
|`alt-cmd-s`|保存所有|
|`cmd-w`|关闭标签|
|`shift-cmd-w`|关闭窗口|
|`cmd-k up/down/left/right`|分隔窗口|
|`cmd-k cmd-up/down/left/right`|聚焦窗口|
|`ctrl-cmd-f`|全屏|

## 目录树操作

|快捷键|快捷键的功能|
|:----|:---------|
|`cmd-\`|显示(隐藏)目录树|
|`ctrl-0`|焦点切换到目录树(再按一次或者 Esc 退出目录树)|
|`alt-right 和 alt-left`|展开(隐藏)所有目录|
|`ctrl-alt-] 和 ctrl-alt-[`|同上|
|`ctrl-[ 和 ctrl-]`|展开(隐藏)当前目录|
|`ctrl-shift-c`|复制当前文件绝对路径|
|`cmd-k h 或 cmd-k left`|在左半视图中打开文件|
|`cmd-k j 或 cmd-k down`|在下半视图中打开文件|
|`cmd-k k 或 cmd-k up`|在上半视图中打开文件|
|`cmd-k l 或 cmd-k right`|在右半视图中打开文件|

`cmd-k h`为先按下`cmd-k`，松开后按`h`。

## 书签

|快捷键|快捷键的功能|
|:----|:---------|
|`cmd-F2`|在本行增加书签|
|`F2`|跳到当前文件的下一条书签|
|`shift-F2`|跳到当前文件的上一条书签|

## 选取

|快捷键|快捷键的功能|
|:----|:---------|
|`ctrl-shift-p`|选取至上一行
|`ctrl-shift-n`|选取至下一行|
|`ctrl-shift-b`|选取至前一个字符|
|`ctrl-shift-f`|选取至后一个字符|
|`alt-shift-b, alt-shift-left`|选取至字符开始|
|`alt-shift-f, alt-shift-right`|选取至字符结束|
|`ctrl-shift-e, cmd-shift-right`|选取至本行结束|
|`ctrl-shift-a, cmd-shift-left`|选取至本行开始|
|`cmd-shift-up`|选取至文件开始|
|`cmd-shift-down`|选取至文件结尾|
|`cmd-a`|全选|
|`cmd-l`|选取一行，继续按会继续选取下一行|
|`ctrl-shift-w`|选取当前单词|

## 编辑和删除文本

|快捷键|快捷键的功能|
|:----|:---------|
|`ctrl-t`|使光标前后字符交换|
|`cmd-j`|将下一行与当前行合并|
|`ctrl-cmd-up, ctrl-cmd-down`|使当前行向上或者向下移动|
|`cmd-shift-d`|复制当前行到下一行|
|`cmd-/`|将选择的文件加入注释|


## Atom 大小写转换

|快捷键|快捷键的功能|
|:----|:---------|
|`cmd-k, cmd-u`|使当前字符大写|
|`cmd-k, cmd-l`|使当前字符小写|

`cmd-k, cmd-u`为先按`cmd-k`再按`cmd-u`。

## 删除和剪切

|快捷键|快捷键的功能|
|:----|:---------|
|`ctrl-shift-k`|删除当前行|
|`ctrl-k`|剪切到当前行结束|
|`alt-h 或 alt-delete`|删除到当前单词开始|
|`alt-d`|删除到当前单词结束|

## 多光标和多处选取

|快捷键|快捷键的功能|
|:----|:---------|
|`cmd-click`|增加新光标|
|`cmd-shift-l`|将多行选取改为多行光标|
|`ctrl-shift-up, ctrl-shift-down`|增加上（下）一行光标|
|`cmd-d`|选取文档中和当前单词相同的下一处|
|`cmd-u`|取消选择|
|`ctrl-cmd-g`|选取文档中所有和当前光标单词相同的位置|

## 跳转

|快捷键|快捷键的功能|
|:----|:---------|
|`ctrl-m`|相应括号之间，html tag之间等跳转|
|`ctrl-g`|移动到指定行 row:column 处|
|`ctrl-cmd-m`|括号(tag)之间文本选取|
|`alt-cmd-.|关闭当前XML/HTML tag`|
|`ctrl-shift-o`|打开链接|

## 编码方式，文件类型，Markdown 预览

|快捷键|快捷键的功能|
|:----|:---------|
|`ctrl-shift-u`|调出切换编码选项|
|`ctrl-shift-l`|选择文本类型|
|`ctrl-shift-m`|Markdown 预览|

## 查找和替换

|快捷键|快捷键的功能|
|:----|:---------|
|`cmd-f`|在buffer中查找|
|`cmd-g`|查找下一个|
|`shift-cmd-g`|查找上一个|
|`cmd-shift-f`|在整个工程中查找|

## 折叠

|快捷键|快捷键的功能|
|:----|:---------|
|`alt-cmd-[`|折叠|
|`alt-cmd-]`|展开|
|`alt-cmd-shift-{`|折叠全部|
|`alt-cmd-shift-}`|展开全部|
|`cmd-k cmd-n`|指定折叠层级，n为层级数|

## git 操作

|快捷键|快捷键的功能|
|:----|:---------|
|`cmd-alt-z`|checkout HEAD 版本|
|`cmd-shift-b`|弹出 untracked 和 modified 文件列表|
|`alt-g down alt-g up`|在修改处跳转|
|`alt-g d`|弹出diff列表|
|`alt-g o`|在 github 上打开文件|
|`alt-g g`|在 github 上打开项目地址|
|`alt-g b`|在 github 上打开文件 blame|
|`alt-g h`|在 github 上打开文件 history|
|`alt-g i`|在 github 上打开 issues|
|`alt-g r`|在 github 打开分支比较|
|`alt-g c`|拷贝当前文件在 gihub 上的网址|
