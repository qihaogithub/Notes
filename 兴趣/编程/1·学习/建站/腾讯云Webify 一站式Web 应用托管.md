[教你如何用最简单的方法上线一个新网站 - 掘金](https://juejin.cn/post/7024704650620174350) 

 上线网站极简教程[#]( https://link.juejin.cn/?target=https%3A%2F%2Fwebify.cloudbase.net%2Fblog%2F5%25E5%2588%2586%25E9%2592%259F%25EF%25BC%2581%25E6%2588%2591%25E4%25B8%258A%25E7%25BA%25BF%25E4%25BA%2586%25E6%2596%25B0%25E7%25BD%2591%25E7%25AB%2599%23%25E4%25B8%258A%25E7%25BA%25BF%25E7%25BD%2591%25E7%25AB%2599%25E6%259E%2581%25E7%25AE%2580%25E6%2595%2599%25E7%25A8%258B " https://webify.cloudbase.net/blog/5%E5%88%86%E9%92%9F%EF%BC%81%E6%88%91%E4%B8%8A%E7%BA%BF%E4%BA%86%E6%96%B0%E7%BD%91%E7%AB%99#%E4%B8%8A%E7%BA%BF%E7%BD%91%E7%AB%99%E6%9E%81%E7%AE%80%E6%95%99%E7%A8%8B" )
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

让我们先来了解下传统的上线网站流程。

### 传统方式[#]( https://link.juejin.cn/?target=https%3A%2F%2Fwebify.cloudbase.net%2Fblog%2F5%25E5%2588%2586%25E9%2592%259F%25EF%25BC%2581%25E6%2588%2591%25E4%25B8%258A%25E7%25BA%25BF%25E4%25BA%2586%25E6%2596%25B0%25E7%25BD%2591%25E7%25AB%2599%23%25E4%25BC%25A0%25E7%25BB%259F%25E6%2596%25B9%25E5%25BC%258F " https://webify.cloudbase.net/blog/5%E5%88%86%E9%92%9F%EF%BC%81%E6%88%91%E4%B8%8A%E7%BA%BF%E4%BA%86%E6%96%B0%E7%BD%91%E7%AB%99#%E4%BC%A0%E7%BB%9F%E6%96%B9%E5%BC%8F" )

假如我们要上线个人博客网站，供其他同学访问，那么需要经历如下步骤：

1.  准备一份个人博客网站的源代码
2.  购买一台有公网 IP 的服务器
3.  把网站文件放到服务器上，并安装 web 服务器软件提供网页访问能力
4.  购买一个域名
5.  配置 DNS 解析，把域名指向服务器的 IP 地址
6.  如果要提高网站访问速度，自行购买 CDN 流程图如下： ![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/771a9e02e24748d7acb7e65fe0aca98f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)
    

听起来就觉得麻烦，而且这一套流程下来最少也要 1 个小时。这也是为啥很多同学只是有上线个人网站的想法，却从未实现。但是，昨天我却只用 5 分钟，就上线了自己的网站，怎么做到的呢？ 下面引出今天的主角 `Webify` 。

### Webify[#]( https://link.juejin.cn/?target=https%3A%2F%2Fwebify.cloudbase.net%2Fblog%2F5%25E5%2588%2586%25E9%2592%259F%25EF%25BC%2581%25E6%2588%2591%25E4%25B8%258A%25E7%25BA%25BF%25E4%25BA%2586%25E6%2596%25B0%25E7%25BD%2591%25E7%25AB%2599%23webify " https://webify.cloudbase.net/blog/5%E5%88%86%E9%92%9F%EF%BC%81%E6%88%91%E4%B8%8A%E7%BA%BF%E4%BA%86%E6%96%B0%E7%BD%91%E7%AB%99#webify" )

Webify 是腾讯云提供的 **一站式** Web 应用托管服务，帮助大家极速开发、部署、上线网站项目。

什么是一站式呢？

就是一条龙服务，只要你有一套网页代码，无论是静态、动态网站还是其他类型的 web 应用，都能使用 Webify 傻瓜式部署。由它提供服务器、默认域名、自定义域名、HTTPS、CDN 加速，提升 Web 应用的性能和安全性。换言之，如果使用 Webify 上线个人博客，你只需要：

1.  准备一份个人博客网站的源代码
2.  进入 Webify 控制台，选择源码和配置
3.  一键发布

流程大大精简了！ ![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2e9392f2de84ff68eb7e5dd039881ca~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)
 此外，Webify 还提供基于 Git 工作流的 DevOps 流程，每次修改代码都能自动重新构建部署，不用再登录服务器自己操作了！

听起来挺爽，下面我们一起试着用 Webify 上线个人博客。

### Webify 实战[#]( https://link.juejin.cn/?target=https%3A%2F%2Fwebify.cloudbase.net%2Fblog%2F5%25E5%2588%2586%25E9%2592%259F%25EF%25BC%2581%25E6%2588%2591%25E4%25B8%258A%25E7%25BA%25BF%25E4%25BA%2586%25E6%2596%25B0%25E7%25BD%2591%25E7%25AB%2599%23webify-%25E5%25AE%259E%25E6%2588%2598 " https://webify.cloudbase.net/blog/5%E5%88%86%E9%92%9F%EF%BC%81%E6%88%91%E4%B8%8A%E7%BA%BF%E4%BA%86%E6%96%B0%E7%BD%91%E7%AB%99#webify-%E5%AE%9E%E6%88%98" )

地址：[cloud. Tencent. Com/product/web…]( https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Fwebify " https://cloud.tencent.com/product/webify" )

首先进入 Web 应用托管平台，新建一个应用。

一个应用对应一个网站项目，这里提供两种新建应用的方式：Git 导入和从模板创建。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b2ddbb89bc4d28a4b27d973de9cda3~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

#### Git 导入创建应用[#]( https://link.juejin.cn/?target=https%3A%2F%2Fwebify.cloudbase.net%2Fblog%2F5%25E5%2588%2586%25E9%2592%259F%25EF%25BC%2581%25E6%2588%2591%25E4%25B8%258A%25E7%25BA%25BF%25E4%25BA%2586%25E6%2596%25B0%25E7%25BD%2591%25E7%25AB%2599%23git-%25E5%25AF%25BC%25E5%2585%25A5%25E5%2588%259B%25E5%25BB%25BA%25E5%25BA%2594%25E7%2594%25A8 " https://webify.cloudbase.net/blog/5%E5%88%86%E9%92%9F%EF%BC%81%E6%88%91%E4%B8%8A%E7%BA%BF%E4%BA%86%E6%96%B0%E7%BD%91%E7%AB%99#git-%E5%AF%BC%E5%85%A5%E5%88%9B%E5%BB%BA%E5%BA%94%E7%94%A8" )

Git 导入适用于已有网站源代码的方式，只要你的代码存在于 Git 托管平台，就能直接在 Webify 导入。

比如我们想要上线个人博客，先要有一套博客源代码。可以自己写代码；也可以直接使用一些现成的站点生成器，比如 Hugo、Hexo 等（后面详细介绍），自动生成源代码；当然还可以下载、克隆别人的项目代码。搞到代码后，把它上传到 GitHub 或 Gitee 等代码托管平台就可以被 Webify 导入了。

导入之后需要根据应用的技术栈和类型，填写构建命令等配置。这里可以直接选择预设配置，比如你的项目用到了 Vue. Js，可以直接选择对应的预设，不用填写就能自动配置：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3ad90f4542c4b76b81607357d55e602~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

#### 从模板创建应用[#]( https://link.juejin.cn/?target=https%3A%2F%2Fwebify.cloudbase.net%2Fblog%2F5%25E5%2588%2586%25E9%2592%259F%25EF%25BC%2581%25E6%2588%2591%25E4%25B8%258A%25E7%25BA%25BF%25E4%25BA%2586%25E6%2596%25B0%25E7%25BD%2591%25E7%25AB%2599%23%25E4%25BB%258E%25E6%25A8%25A1%25E6%259D%25BF%25E5%2588%259B%25E5%25BB%25BA%25E5%25BA%2594%25E7%2594%25A8 " https://webify.cloudbase.net/blog/5%E5%88%86%E9%92%9F%EF%BC%81%E6%88%91%E4%B8%8A%E7%BA%BF%E4%BA%86%E6%96%B0%E7%BD%91%E7%AB%99#%E4%BB%8E%E6%A8%A1%E6%9D%BF%E5%88%9B%E5%BB%BA%E5%BA%94%E7%94%A8" )

如果我们啥代码都没有，也搞不来代码，咋办？

也没有关系，Webify 内置了一些项目模板，直接选择需要的应用创建即可。比如我们要做个人博客，可以选择 Docusaurus 2 这款主流的站点生成器：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3dfe67328842cc82a285369dd4344a~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

选中模板后，系统会自动把代码模板复制到新的 Git 仓库，和应用关联。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e69ac7651e84d92ad3ab272a5298979~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

Webify 会自动给 Git 仓库配置 Webhooks，后续每当仓库的代码发生变更（push）时，都会自动触发应用的重新部署，无需再跑到服务器上改代码了！

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed217b362b1a4fa3babc77f770f0664e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

点击下一步，进入应用配置，由于我们使用的是系统预设模板，什么都不用改，用默认配置就行了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9685e15fe0914f278a94d8d9773568b4~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

点击部署按钮，稍等几分钟，应用就创建成功了！

#### [](https://link.juejin.cn/?target=)应用详情[#]( https://link.juejin.cn/?target=https%3A%2F%2Fwebify.cloudbase.net%2Fblog%2F5%25E5%2588%2586%25E9%2592%259F%25EF%25BC%2581%25E6%2588%2591%25E4%25B8%258A%25E7%25BA%25BF%25E4%25BA%2586%25E6%2596%25B0%25E7%25BD%2591%25E7%25AB%2599%23%25E5%25BA%2594%25E7%2594%25A8%25E8%25AF%25A6%25E6%2583%2585 " https://webify.cloudbase.net/blog/5%E5%88%86%E9%92%9F%EF%BC%81%E6%88%91%E4%B8%8A%E7%BA%BF%E4%BA%86%E6%96%B0%E7%BD%91%E7%AB%99#%E5%BA%94%E7%94%A8%E8%AF%A6%E6%83%85" )

可以在应用列表和部署记录中查看到新建完成的应用：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/480c68804e944422a79e9606faa035aa~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

点击新建的应用，进入应用详情页：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1600518fd8b14bc09f67e93364ce678e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

可以查看到应用的详细信息，比如系统为我们提供的默认项目域名，点击之后就能访问到已上线的博客网站啦！

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83d31302a0cc4befa41bc31f7fffb9cc~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

应用详情中还有一个所属环境信息，那是啥呢？

其实在部署过程中，系统会自动创建一个 `云开发` 环境，根据配置的命令自动构建项目，将构建产物放到 `静态网站托管` 上。

可以在云开发控制台看到已经上传到服务器上的文件：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdbbc1411d414cabb4094892e5f42fe6~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

在静态网站托管页面，可以修改已上传的文件，修改 CDN 缓存设置等：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd5a1741ebd2406fa18f9caf93eed604~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

进入应用详情的设置页，可以给项目添加自定义域名、修改应用构建配置、删除应用等：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e74af7f2786464592720dd7d4032cd1~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

#### 使用感受[#]( https://link.juejin.cn/?target=https%3A%2F%2Fwebify.cloudbase.net%2Fblog%2F5%25E5%2588%2586%25E9%2592%259F%25EF%25BC%2581%25E6%2588%2591%25E4%25B8%258A%25E7%25BA%25BF%25E4%25BA%2586%25E6%2596%25B0%25E7%25BD%2591%25E7%25AB%2599%23%25E4%25BD%25BF%25E7%2594%25A8%25E6%2584%259F%25E5%258F%2597 " https://webify.cloudbase.net/blog/5%E5%88%86%E9%92%9F%EF%BC%81%E6%88%91%E4%B8%8A%E7%BA%BF%E4%BA%86%E6%96%B0%E7%BD%91%E7%AB%99#%E4%BD%BF%E7%94%A8%E6%84%9F%E5%8F%97" )

其实这个东西并不算新技术了，产品形态和体验上类似 Vercel 和 Github Pages。不过优点是 Webify 在国内，提供了高速 CDN；还能够和其他云产品打通、形成体系。

使用 Webify 上线网站还是很爽的，整个流程非常简单、易上手，着实省去了很多自己上线网站的琐碎流程。无论是对想快速上线自己网站的同学、还是 web 开发爱好者，都是不错的选择。

还有重要的一点要提醒大家，世上没有免费的午餐，Webify 依托于云开发，也是要收费的（提供 1 个月的免费体验），但相对于自己购买服务器（即使是学生机），性价比也是更高的。