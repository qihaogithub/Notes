Hello，这里是东哥。这节课，我们要学习的是，「长乐未央全栈系列：Node. Js 项目实践」课程的第 3 回：编辑器与创建 Express 项目，在这节课里，我们将探讨：

*   开发 Node. Js，哪个编辑器最好？
*   Node. Js 的框架哪个更好？
*   创建 Express 项目以及输出 JSON
*   使用 nodemon 监听 Express 项目

_1\. 开发编辑器_
-----------

在正式开发之前，我们简单说一下编辑器问题。开发 `Node.js`，最常见的两个编辑器是 `WebStorm` 和 `VS Code`，我这里分别放了它们的下载地址

*   [https://www.jetbrains.com/webstorm/download/](https://www.jetbrains.com/webstorm/download/)
*   [https://code.visualstudio.com/](https://code.visualstudio.com/)

请大家自行安装即可。对于新手朋友，我非常推荐大家使用 `WebStorm`。因为它的功能齐全，几乎无需配置，开箱可用。而且语法提示、拼写纠错能力很强。新手朋友们，初学开发，最大的一个问题就是英文单词拼写非常容易打错。

在 `WebStorm` 中如果你的拼写有错误，它会马上进行提示。`WebStorm` 的缺点是商业使用需要收费，但是个人学习使用是免费的。

`VS Code` 的功能就相对较弱，而且里面有大量插件需要自己安装，调整。纠错能力很弱，代码跳转能力也不太行。对新手同学来说，就可能在一个很小的拼写问题上面，要花费大量的时间来人工肉眼检查错误。当然它也有优点，它优点就是可以免费使用。。。

我们课程中用来演示的是都 `WebStorm`，除非你有丰富的开发经验，否则我还是推荐你安装好 `WebStorm`。

_2\. Express 与 Koa_
-------------------

使用 `Node.js` 开发后端，最流行的框架有 `Express` 和 `Koa`。其中

*   在 Github 上：[Express](https://github.com/expressjs/express) 的星标有 6 万 3 千多个，[Koa](https://github.com/koajs/koa) 有 3 万 4 千多个。
*   在 npm 上：[Express](https://www.npmjs.com/package/express) 的周下载量是 2~3000 多万次，[Koa](https://www.npmjs.com/package/koa) 是 100 多万次。

这么简单的对比一下，我们就选择 Express。

_3\. 创建 Express 项目_
-------------------

正式开发 `Express` 项目，我们在工作中，一般不会自己手动一点点创建项目文件。而是使用 `express-generator` 脚手架，通过它，一个命令就会自动生成项目所需要的结构了。

那么现在先来安装：

```
npm i -g express-generator@4 
```

注意下，我们需要使用 `-g` 参数，来全局安装它。

现在还需要一个专门来放项目的地方。使用 macOS，那么推荐大家可以放在家目录的 `Developer` 文件夹下。如果你还没有这个文件夹的话，可以使用这个命令来创建它，并进入其中

```
mkdir ~/Developer && cd ~/Developer 
```

Windows 的同学，找一个自己熟悉的目录就好。但请务必注意，路径中不要有中文，不能有空格，否则在开发中，有可能会出现各种奇怪的错误。建好目录后，一样需要在命令行中，通过 `cd` 命令，进入其中

接着就要来创建项目了。

```
# 创建项目
express --no-view clwy-api 

# 注意：Windows有可能碰到提示：express : 无法加载文件 C:\Program Files\nodejs\express.ps1，因为在此系统上禁止运行脚本。
# 如果碰到这个错误，需要用`管理员身份`打开PowerShell，然后运行：
Set-ExecutionPolicy RemoteSigned

# 进入项目之中
cd clwy-api 
```

这里要注意，我们使用了 `--no-view参数`，它的意思是不需要任何视图模板，因为我们这个项目专门做后端接口的。将来渲染页面会使用 `Vue` 和 `React` 之类的框架，所以不需要视图。然后我们项目的名字叫做 `clwy-api`

>如果已经创建好了项目文件夹， 直接输入express --no-view 可以当前文件夹直接开始创建

项目创建成功后，通过命令，安装依赖包。

```
npm i 
```

这样项目所需要的依赖包，都会自动下载到项目之中了

最后，运行命令，启动服务

```
npm start 
```

现在就可以通过 [http://localhost:3000](http://localhost:3000/)，来访问我们的第一个项目了。

这时候会看到欢迎页面，恭喜你，到这里，你已经成功的跑起来 `Node.js` 了。

[![](https://assets.clwy.cn/uploads/qqlptgjyrgqnrwzzalt12a7jywki!large)
]( https://assets.clwy.cn/uploads/qqlptgjyrgqnrwzzalt12a7jywki!large )

_4\. 输出 json_
-------------

继续来改，我们这个项目是专门开发接口的，而接口所需要的是 `json` 格式，而不是直接输出 `HTML`。

那么找到 `routes/index.js` 文件，将中间这行改为

```
router.get('/', function (req, res, next) {
  res.json({ message: 'Hello Node.js' });
}); 
```

它的意思就是以 `json` 格式来输出 `Hello Node.js`

这时候我们刷新浏览器，会发现它没有任何变化，还是显示以前的内容。这是因为当修改代码后，`Express` 并没有一直监听我们的修改，运行的一直是之前的东西。想要显示最新修改的内容，需要重启服务。

回到命令行，按 `ctrl + c` 键，可以停止服务，接着再次运行 `npm start` 来启动服务。接着还要删掉 `public/index.html` 文件。刷新浏览器后，可以看到返回的 `json` 数据了

[![](https://assets.clwy.cn/uploads/rtcwcg1fyfexv8y7qzhzclyl9jfv!large)
]( https://assets.clwy.cn/uploads/rtcwcg1fyfexv8y7qzhzclyl9jfv!large )

> 如图所示的页面样式比较好看，是因为安装了浏览器插件[JSON-handle](https://chromewebstore.google.com/detail/json-handle/iahnhfdhidomcpggpaimmmahffihkfnj)

再次恭喜你，你成功的完成了第一个 `Node` 接口了。

大家看到的浏览器中显示的样子，可能会和我的有一些小小的区别。这是因为我给浏览器安装了 [JSON-handle](https://chromewebstore.google.com/detail/json-handle/iahnhfdhidomcpggpaimmmahffihkfnj) 插件，有兴趣的同学可以自行安装。如果安装碰到困难了，不安装其实也没关系。因为我们后面会学习使用 `apifox`，它是一个专门用来调试接口的工具，而不会一直使用浏览器来调试。

_5\. Nodemon 监听修改_
------------------

做到这里，大家也发现了，当我们修改代码后，你不重启服务，它根本就不会生效。但是我们开发中，需要不断的修改代码，那要不停的重启，岂不是非常麻烦？

当然也有办法解决啦，可以安装一个叫做 `nodemon` 的包来解决这个小问题。按 `ctrl + c` 停止服务后，运行

```
npm i nodemon 
```

然后打开项目根目录下的 `package.json`，将 `start` 这里修改为

```
"scripts":  {  "start":  "nodemon ./bin/www"  }, 
```

改完后，我们再次启动服务

```
npm start 
```

先来刷新一下，确定看到的是 `Hello Node.js`。然后马上来修改 `routes/index.js`，

```
router.get('/', function (req, res, next) {
  res.json({ message: 'Hello 长乐未央' });
}); 
```

无需重启，我们直接刷新，可以看到显示的内容，已经变成：`Hello 长乐未央` 了

[![](https://assets.clwy.cn/uploads/cu44holly06evpdi2jhuhya7cgxz!large)
]( https://assets.clwy.cn/uploads/cu44holly06evpdi2jhuhya7cgxz!large )

_6\. 总结一下_
----------

| 命令 | 说明 |
| --- | --- |
| npm i -g express-generator@4 | 安装 express-generator |
| express --no-view 项目名 | 创建 Node. Js 项目 |

*   开发 `Node.js` 项目，要先安装 `express-generator`，这样才能使用命令，创建项目
*   创建项目的命令是 `express --no-view` 加上 `项目名`
*   后端接口所使用的格式是：`json`，而不是：`HTML`
*   还要给项目安装、配置 `nodemon`，这样 `Express` 才能监听你的代码