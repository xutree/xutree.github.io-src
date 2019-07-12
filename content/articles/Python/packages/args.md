Title: Python argparse 模块
Category: 教程
Date: 2018-11-10 12:11:25
Modified: 2018-11-10 12:11:25
Tags: Python, argparse

argparse 是 Python 标准库中推荐的命令行解析模块。

```
# 导入
import argparse
# 添加帮助信息的整体描述
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
# 冲突选项
group = parser.add_mutually_exclusive_group()
# 以下两个参数是冲突的，只能存在一个
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
# 一个 - 是简写，-- 是全写，action 表示默认参数为 true

# 添加位置参数
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
# 获得参数
args = parser.parse_args()
# 使用参数
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
```

输出

```
usage: prog.py [-h] [-v | -q] x y

calculate X to the power of Y

positional arguments:
  x              the base
  y              the exponent

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet
```

另外还有一个 `parse_known_args()` 函数，在接受多于程序需要的参数时保证不出错，返回一个 `tuple` 类型的命名空间和一个保存着余下的命令行字符的 `list`。

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    '--flag_int',
    type=float,
    default=0.01,
    help='flag_int.'
)
FLAGS, unparsed = parser.parse_known_args()
print(FLAGS)
print(unparsed)
```

输出

```
[In 1]: python prog.py --flag_int 0.02 --double 0.03 a 1
[Out 1]: Namespace(flag_int=0.02) ['--double', '0.03', 'a', '1']
```
