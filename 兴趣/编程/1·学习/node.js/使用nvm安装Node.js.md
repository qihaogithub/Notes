来源：[使用 nvm 安装 Node.js - 长乐未央全栈系列：Node.js 项目实践（2024 版） - 免费编程视频课程 - 长乐未央](https://clwy.cn/chapters/fullstack-node-nvm)

## 摘录内容 
Hello，这里是东哥。这节课，我们要学习的是，「长乐未央全栈系列：Node. Js 项目实践」课程的第 2 回：使用 nvm 安装 Node. Js，在这节课里，我们将探讨：

*   为何要用 nvm？
*   Windows 和 macOS 安装 nvm 的方式
*   使用 nvm 安装 Node. Js
*   如何切换 Node. Js 的版本
*   配置 npm 中国镜像

开发 `Node.js`，首先就必须要安装 `Node.js` 自身。如果你已经安装好了 `Node.js` 了，可以略过本节课程，直接开始学习开发。

_1\. 为何要用 nvm？_
---------------

安装 `Node.js`，最简单办法，就是直接在[官网](https://nodejs.org/en/)下载了安装。但这种方法，却不是最好的办法。因为如果需要更新 `Node.js` 的版本，那就需要把之前的卸载了，再去下载安装其他版本，这样就非常的麻烦了。

这里推荐大家使用 `nvm` 来安装，可以使用它来安装多个不同版本的 `Node.js`，并且根据需要随意的切换所需版本。

_2\. Windows 安装 nvm-windows_
----------------------------

Windows 与 macOS 的安装方法有些不同。Windows 的同学，请在这里下载 [https://github.com/coreybutler/nvm-windows/](https://github.com/coreybutler/nvm-windows/) 了，直接安装就好，然后点击右侧的 `Releases`，这里就是下载的地方了。接着，找到最新版本，选择 `nvm-setup.exe` 下载。

[![](https://assets.clwy.cn/uploads/os9x0c6pcrf2kb3adyq7k08tc9pe!large)
]( https://assets.clwy.cn/uploads/os9x0c6pcrf2kb3adyq7k08tc9pe!large )

下好后，就大家直接安装上，然后将自己电脑的 `PowerShell` 或者终端打开，运行 `nvm`，只要出来东西了，就是安装好了。

[![](https://assets.clwy.cn/uploads/xieg7g8miptqap565lj0maoc2ta6!large)
]( https://assets.clwy.cn/uploads/xieg7g8miptqap565lj0maoc2ta6!large )

_3\. MacOS 安装 nvm_
------------------

使用苹果电脑的各位同学，我们打开 `nvm` 的 github，[https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating)

复制这里的命令，打开自己电脑的 `终端`，粘贴进去

```


`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash` 
```

直接运行，但是非常有可能碰到错误

[![](https://assets.clwy.cn/uploads/gp6xtoefdccno7tprnsh2jze5aa6!large)
]( https://assets.clwy.cn/uploads/gp6xtoefdccno7tprnsh2jze5aa6!large )

如果看到这问题，说明这个地址被墙了，需要开启 VPN，不然是访问不到的。

[![](https://assets.clwy.cn/uploads/m3pptojqcyre9ikak23agh9cqdnq!large)
]( https://assets.clwy.cn/uploads/m3pptojqcyre9ikak23agh9cqdnq!large )

完成后，直接关闭命令行，再重新打开。这样环境变量才会生效，才能使用 `nvm` 相关的命令。

_4\. 使用 nvm 安装 Node. Js_
-----------------------

接着我们查看一下，现在最新的 `Node.js LTS` 的版本号，`LTS` 也就是长期支持版本。Windows 与 macOS 的命令也有一点儿区别，因为我是 macOS 的，所以我就运行 `nvm ls-remote`。Windows 的同学记得要用上面这条命令，不要搞错了

```
# Windows 运行
nvm list available

# macOS 运行
nvm ls-remote
```

可以看到最新的 `LTS` 版本，现在是 `v22.12.0`，那么就安装这个版本

```
nvm install 22.12.0

# 下面这个命令，在Windows上需要运行，macOS上则无需运行
nvm use 22.12.0
```

完成后，它会自动将这个版本设置成默认版本，可以来查看一下

```
node -v
```

果然已经是 `20.12.2` 版本了。至此，Node. Js 就安装完成了。

_5\. 如何切换 Node. Js 的版本_
----------------------

`nvm` 毕竟是一个版本控制器，所以如果咱们的电脑上同时有几个项目，每个项目依赖的 `Node.js` 版本又不相同的时候，就可以用 `nvm` 来安装多个不同的 Node. Js 版本，并且进行切换了。现在来演示一下如何切换 Node. Js 的版本。

我们现在安装一个老一些的 `Node.js`

```
nvm install 18.20.2
```

装好之后

```
# windows 运行
nvm list

# macOS 运行
nvm ls
```

可以看到所有安装过的版本。那么，如何切换默认的 `Node.js` 版本呢？

```
# windows 运行
nvm use 18.20.2

# macOS 运行
nvm alias default 18.20.2
```

再次运行 `node -v`，可以看到，已经是 `18.20.2` 了。好了，试一下就好，我们现在就先切换回来。

```
# windows 运行
nvm use 20.12.2

# macOS 运行
nvm alias default 20.12.2` 
```

> PS：需要注意的是，在 macOS 也可以运行 `nvm use` 命令。但在 mac 上，这样只是临时切换成这个版本，重启命令行后会失效。MacOS 上，需要运行 `nvm alias default`，才能设置为全局。

_6\. 配置 npm 中国镜像_
-----------------

装好 Node. Js 后，还会自带 `npm` 命令。`npm` 是 Node. Js 的包管理器，可以用它来安装项目相关的依赖包。接着我们需要配置 `npm` 的中国镜像，这样它的下载速度会更快。

```
npm config set registry https://registry.npmmirror.com/
```

_7\. 总结一下_
----------

总结几句：

*   首先安装 `Node.js` 的方式并不唯一，而使用 `nvm` 安装是目前最为专业的一种方式。
*   实际中使用也非常的方便，只要先安装好 `nvm` 这个工具，然后通过命令，就查看所有可安装的版本。
*   然后用 `nvm install 版本号` 就可以安装了，一般来说，需要安装 `LTS` 版本。
*   如果系统上同时安装了多个 `Node.js` 版本，还可以通过命令来切换。
*   如果在国内开发，记得安装 `npm 中国镜像`。
