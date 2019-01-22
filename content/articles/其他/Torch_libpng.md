Title: 为 Torch 安装特定版本的 libpng
Category: 教程
Date: 2019-01-22 14:23:05
Modified: 2019-01-22 14:37:18

为了跑别人的程序，遇到了下面的问题

```
libpng warning: Application built with libpng-1.4.12 but running with 1.6.35
```

利用 ```brew info libpng``` 查询本机安装版本，输出如下

```
/usr/local/Cellar/libpng/1.6.29 (26 files, 1.2MB)
  Poured from bottle on 2017-06-25 at 21:23:18
/usr/local/Cellar/libpng/1.6.31 (26 files, 1.2MB)
  Poured from bottle on 2017-08-22 at 12:35:00
/usr/local/Cellar/libpng/1.6.34 (26 files, 1.2MB)
  Poured from bottle on 2017-12-04 at 23:07:49
/usr/local/Cellar/libpng/1.6.35 (26 files, 1.2MB)
  Poured from bottle on 2018-10-07 at 17:36:58
```

用下面代码查看了 brew 中 libpng 的 commit 信息
```
cd $(brew --repository)/Library/Taps/homebrew/homebrew-core
git log master --  Formula/libpng.rb
```
发现并没有版本 1.4.12，于是自己编译

```
cd /usr/local/src
curl --remote-name --location http://download.sourceforge.net/libpng/libpng-1.4.12.tar.gz
tar -xzvf libpng-1.4.12.tar.gz
cd libpng-1.4.12
./configure --prefix=/usr/local/Cellar/libpng/1.4.12
make
make install
```

上面的 prefix 我设置为 brew 安装 libpng 的位置。安装好以后执行

```
brew switch libpng 1.4.12
```

切换到 1.4.12 版本。还有最后一步工作，之前 Torch 是 luarocks 使用 libpng-1.6.35 编译，现在要重新编译

```
luarocks remove image
luarocks install image
```

参考：

- [https://github.com/torch/image/issues/137](https://github.com/torch/image/issues/137)
- [https://mac-dev-env.patrickbougie.com/libpng/](https://mac-dev-env.patrickbougie.com/libpng/)
- [https://stackoverflow.com/questions/3987683/homebrew-install-specific-version-of-formula](https://stackoverflow.com/questions/3987683/homebrew-install-specific-version-of-formula)
