https://zhuanlan.zhihu.com/p/392618246


最简单的部署
------

首先，还是先手把手教大家部署一个简单的页面，让大家先体验体验部署的快乐。

第一步，在 Github 随便创建一个项目，比如我这里起的名字叫 **first-page**。

![](https://pic1.zhimg.com/v2-5ff1d35dd4a0464f6fe89177d40ce22c_b.jpg)

然后创造 index. Html, styles. Css, main. Js 三个文件：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>First Page</title>
</head>
<body>
    <h2>This is my first page</h2>
    <script src="main.js"></script>
</body>
</html>
alert('xxx')
h2 {
    color: red;
}
```

在本地用 http-server 跑一下：

在 `localhost:8080` 就可以看预览效果了

![](https://pic4.zhimg.com/v2-ae5804d460a712c0dfdf0971a4ac3997_b.jpg)

OK，现在我们把代码提交到 Github：

```text
git add ./

git commit -m 'feat: 初始化'

git push
```

进入 Github 项目的 Settings。

![](https://pic3.zhimg.com/v2-ef6207561ecc295cc060266c20e66612_b.jpg)

拉到最下面的 Github Pages。

![](https://pic1.zhimg.com/v2-d00d953a8032e126baf724be572d4c88_b.jpg)

选择里面的 master 分支，再点一下 Save 按钮，收工。

![](https://pic3.zhimg.com/v2-bb5f138554ffb42554946631cb84a9b2_b.jpg)

稍等一下，就可以在 [http://username.github.io/first-page/](https://link.zhihu.com/?target=http%3A//username.github.io/first-page/) 上可以访问了 **（注意：这里的 username 就是你的 Github 用户名，比如我的就是 Haixiang 6123。）**。

好，以上就是一个最最最简单的 Github 页面的部署了。下面来聊一聊原理。

原理
--

刚刚我们通过 `http://localhost:8080` 就能访问我们的页面，本质上是访问了本地的 `index.html`。相应地，访问 `http://username.github.io/first-page` 则是访问远程的 `index.html`。

![](https://pic2.zhimg.com/v2-778b127f1c0dcfc8f2cd8f4aa2c5ab1d_b.jpg)

这里的部署只是把文件上传到 Github 而已，具体做法就是 **add + commit + push** 一把梭子。

如果我们非要写个部署脚本，可以这么写：

```text
git add ./
git commit -m 'deploy'
git push
```

复杂项目部署
------

上面只说了简单的 `index.html + styles.css + main.js` 部署，但是我们平常都是用 Vue 或者 React 开发的呀，这要怎么部署呢？

首先，不要被框架“迷惑”了，框架只是为了提高我们的开发效率，本质上当我们访问网页时还是 `index.html + styles.css + main.js`。

**无论是 React 还 Vue，都会有类似 `npm run build` 这样的打包命令。它会将 jsx/. Vue 这些鬼东西通过 Webpack 全部转换为 index. Html + styles. Css + main. Js。** 

这里我用 React 来做演示，先用 CRA 创建一个项目：

```bash
create-react-app hello --template=typescript
```

然后在项目里跑打包命令：

运行之后会在根目录得到一个 `/build` 的目录，里面就装着我们需要的 html, css, js 文件。

![](https://pic1.zhimg.com/v2-b90d891e047d733f22a69e885cf77344_b.jpg)

通过刚刚的部署经验，我们得知，只要将这些 html, css 和 js 都推到一个分支上，在 Settings 里选择这个分支，最后点一下 "Save" 按钮就 OJBK 了。那么问题来了：怎么才能推呢？

我们不妨再仔细品品 `git push` 这个命令，它的加长版写法应该是这样的：

`origin` 是项目的 clone 地址，`master` 则是我们分支。如果我把 master 换成别的分支，比如就叫 `x` 分支不就好了？

但是如果这么写，很容易出现 push 之后出现代码冲突，导致 push 失败。一般情况下，每次部署要把上次的部署覆盖掉的，所以可以直接 **强推**：

还是有问题：目前这个项目是在 `first-page` 下面，add-commit-push 素质三连除了把 `/build` push 还会把 `/src`，`/node_modules` 之类的也 push 到 `x` 分支了，我们只希望 push `/build` 目录怎么办？

答案很简单，先去往 `/build` 目录，再 `git init` 一下，相当于在 first-page 项目仓库下的 build 目录再创建一个 git 仓库。设置 origin 为原来项目的 clone 地址即可。

上面这么解释头有点晕，我把部署代码放出来：

```bash
# 出错就停止部署
set -e

# 本地打包构建
npm run build

# 进入 build 目录
cd build

# 创建本地 Git 仓库
git init 
# 添加和提交
git add -A
git commit -m 'deploy'
# 指定 origin 和分支，直接强推
git push -f git@github.com:Haixiang6123/first-page.git master

# 回到原来的目录
cd -
```

以上就是所有项目的 **一键部署方法**，可以看到无论是什么项目，只要是有打包功能的，都可以用上面的方法来一键部署。

> Tip: 上面的 origin 直接用 `git@github.com:Haixiang6123/first-page.git` 替代了，也就说项目代码可以存到随便一个仓库，只需要推到对应的 git 地址就可以完成对应项目的部署了。目前我的个人网站就是这么部署的：开发一个仓库，部署时把产物推到另一个仓库，以另一个仓库来部署静态网页。

第三方部署工具
-------

上面的部署脚本我也是抄了 [Vue 官方提供的部署脚本](https://link.zhihu.com/?target=https%3A//cli.vuejs.org/zh/guide/deployment.html%23github-pages)。

Vue 官方是让开发者自己抄这个脚本来部署的，而 React 则可以用 [react-gh-pages](https://link.zhihu.com/?target=https%3A//github.com/gitname/react-gh-pages) 这个第三方工具来部署。

第三方部署工具的好处就是可以自己不写 bash 脚本。

**另一个好处就是可以帮助让你避免 404**，相信很多人第一次部署 Github 静态网页都会遇到这个问题。99% 的原因都是因为 `publicPath` 没有设置好。

而这些第三方部署工具都会在 Getting Started 这一步提醒你要配置好 `publicPath`，要么直接帮你配置好了。

特殊功能
----

通过上面的步骤已经可以部署一个类似 **[http://xxx.github.io/first-page](https://link.zhihu.com/?target=http%3A//xxx.github.io/first-page)** 的项目了。但是，我们在部署个人网站或者博客时不想要这个 `first-page` 的后缀，直接 **[https://xxx.github.io](https://link.zhihu.com/?target=https%3A//xxx.github.io)** 会更好看。

创建一个名为 **[http://xxx.github.io](https://link.zhihu.com/?target=http%3A//xxx.github.io)** 的项目（xxx 是你的用户名），然后再以上面的方式去部署可以得到没有后缀的 **[http://xxx.github.io](https://link.zhihu.com/?target=http%3A//xxx.github.io)** 。

比如我的 Github 用户名为 **Haixiang 6123**，那就创建一个名为 **[http://Haixiang6123.github.io](https://link.zhihu.com/?target=http%3A//Haixiang6123.github.io)** 的仓库，然后在这上面部署。

![](https://pic4.zhimg.com/v2-dd2665ed169d9dfaac037f078c2aac7f_b.jpg)

为什么会这么设计呢？其实这算是 Github 留给用户的一个小彩蛋吧，不过这种大家都希望用到的功能也不能太算为彩蛋了，所以，我更愿意称其为 **特殊功能**。

除了这个，Github 还有很多的特殊功能，比如你直接创建一个以自己 Github 用户名的仓库（以我自己的 Haixiang 6123 为例）：

![](https://pic2.zhimg.com/v2-6e3c4a9c00612f2b3a3a09a58a787fe9_b.jpg)

然后在上面添加一个 README. Md，它就可以变成你的 Profile 了：

![](https://pic4.zhimg.com/v2-6a1514f0deaf0a72179448f10dd2a5ff_b.jpg)

说回部署，在以前并不能像现在这么自如地想在哪个分支部署就哪个分支部署，只能在 **gh-pages** 这个特殊分支上部署。而且也可能部署根目录的 `index.html`，不像现在还能部署 `/docs` 目录下的 `index.html`。

![](https://pic1.zhimg.com/v2-6b8657579e95de4c0173c0a3a817e03c_b.jpg)

所以，在以前那段时间，Github 部署静态页面更多是被当作一个 **特殊功能**，导致很多人都会觉得部署一个网页怎么这么麻烦。

总结
--

总结一下，部署本质上就是上传 html, css, js 文件到另一个硬盘（COS 桶、CDN 等），然后远程访问 `index.html`。

使用 Github 部署的关键就是用 add-commit-push 素质三连把 html, css, js 都 push 到仓库上，然后在 Settings 里点一下部署按钮就可以了。

对于需要打包的项目，部署前需要 cd 到打包后的目录，常见的有 `/build` 或 `/dist` 目录，然后通过 `git init` 创建本地仓库，然后将整个目录所有东西都强推到项目分支上就好了。

> 对了，最近刚建了个公众号【写代码的海怪】，觉得我写得不错就随缘关注一下喽~