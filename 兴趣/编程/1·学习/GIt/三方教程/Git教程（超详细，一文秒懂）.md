[原文链接](https://blog.csdn.net/weixin_47824895/article/details/130169142)
### 1、Git 概述

#### 1.1 何为版本控制

*   版本控制软件功能：
    
    *   **版本管理**：回退到历史上的任何版本
    *   **共享代码**：团队之间共享代码
    *   团队合作开发-代码整合：
*   版本控制是一种记录文件内容变化，以便将来查阅特定版本修订情况的系统。
    

![](https://img-blog.csdnimg.cn/22b00399ed784320803b793d01eea97f.png)

#### 1.2 为什么需要版本控制

个人开发过渡到团队协作。

**需求**

在项目开发中，团队协作管理代码和文件是每天必须要做的事情。大家一定会碰到如下几个场景和问题？

```
`1：协同修改，多人并行开发修改服务器的文件
2：数据备份
3：版本管理，权限控制
4：如果文件和工程误删了还能找回来吗？
5：分支管理 1.0 2.0
6：遇到了文件冲突如何解决？
7：如何把一些我临时保存的文件不要提交?` 

*   1
*   2
*   3
*   4
*   5
*   6
*   7


```

[Svn](https://so.csdn.net/so/search?q=Svn&spm=1001.2101.3001.7020) 版本控制软件:

![](https://img-blog.csdnimg.cn/b9f718adfb2f42269d6b650811c2bcdf.png)

Git 版本控制器软件:

![](https://img-blog.csdnimg.cn/31c787f8d1cf428bbe6725ecce73f2ae.png)

**小结**

*   svn 和 git 都是做版本控制的，如果不理解一句话: **记录代码的轨迹**就好比每个人的成长阶段一样。

#### 1.3 版本控制工具

![](https://img-blog.csdnimg.cn/288cf7c8d20c4abeb9ba2b7a3dc52cea.png)

➢ 集中式版本控制工具

[CVS](https://so.csdn.net/so/search?q=CVS&spm=1001.2101.3001.7020) 、**SVN**(Subversion)、[VSS](https://so.csdn.net/so/search?q=VSS&spm=1001.2101.3001.7020) ……

集中化的版本控制系统诸如 CVS 、SVN 等，都有一个单一的集中管理的服务器，保存所有文件的修订版本，而协同工作的人们都通过客户端连到这台服务器，取出最新的文件或者提交更新。多年以来，这已成为版本控制系统的标准做法。

这种做法带来了许多好处，每个人都可以在一定程度上看到项目中的其他人正在做些什么。而管理员也可以轻松掌控每个开发者的权限，并且管理一个集中化的版本控制系统，要远比在各个客户端上维护本地数据库来得轻松容易。

事分两面，有好有坏。这么做显而易见的缺点是中央服务器的单点故障。如果服务器宕机一小时，那么在这一小时内，谁都无法提交更新，也就无法协同工作。

集中管理方式在一定程度上看到其他开发人员在干什么，而管理员也可以很轻松掌握每个人的开发权限。

但是相较于其优点而言，集中式版本控制工具缺点很明显：

```
`服务器单点故障
容错性差` 

*   1
*   2


```

➢ 分布式版本控制工具

**Git** 、Mercurial 、Bazaar、Darcs……

像 Git 这种分布式版本控制工具，客户端提取的不是最新版本的文件快照，而是把代码仓库完整地镜像下来 （本地库）。这样任何一处协同工作用的文件发生故障，事后都可以用其他客户端的本地仓库进行恢复。因为每个客户端的每一次文件提取操作，实际上都是一次对整个文件仓库的完整备份。

分布式的版本控制系统出现之后, 解决了集中式版本控制系统的缺陷:

1.  服务器断网的情况下也可以进行开发（因为版本控制是在本地进行的）
2.  每个客户端保存的也都是整个完整的项目（包含历史记录，更加安全）

**小结**

*   svn 它集中式的版本控制，不能离线工作。Git 分布式的版本控制，它版本放在用户自己的电脑。
*   svn 不支持离线工作，版本全部都放在是中央服务器。如果中央服务器挂了。那么版本全部丢失。
*   git 支持离线工作。版本都放用户自己电脑上完成。---- 分布式的版本控制。
*   svn 是项目对仓库，git 是仓库对仓库。

#### 1.4 GIT 的由来及发展史

**概述**

同生活中的许多伟大事件一样，Git 诞生于一个极富纷争大举创新的年代。

Linux 内核开源项目有着为数众广的参与者。绝大多数的 Linux 内核维护工作都花在了提交补丁和保存归档的繁琐事务上（1991－2002 年间）。到 2002 年，Linux 系统已经发展了十年了，代码库之大让 Linus 很难继续通过手工方式管理了，于是整个项目组开始启用分布式版本控制系统 BitKeeper 来管理和维护代码。

到 2005 年的时候，开发 BitKeeper 的商业公司同 Linux 内核开源社区的合作关系结束，他们收回了免费使用 BitKeeper 的权力。这就迫使 Linux 开源社区（特别是 Linux 的缔造者 Linus Torvalds ）不得不吸取教训，只有开发一套属于自己的版本控制系统才不至于重蹈覆辙。他们对新的系统订了若干目标：

```
`• 速度快 
• 简单的设计 
• 对非线性开发模式的强力支持（允许上千个并行开发的分支） 
• 完全分布式 
• 有能力高效管理类似 Linux 内核一样的超大规模项目（速度和数据量）` 

*   1
*   2
*   3
*   4
*   5


```

Linus 花了两周时间自己用 C 写了一个分布式版本控制系统，这就是 Git！一个月之内，Linux 系统的源码已经由 Git 管理了！牛是怎么定义的呢？大家可以体会一下。

Git 迅速成为最流行的分布式版本控制系统，尤其是 2008 年，GitHub 网站上线了，它为开源项目免费提供 Git 存储，无数开源项目开始迁移至 GitHub，包括 jQuery，PHP，Ruby 等等。

历史就是这么偶然，如果不是当年 BitMover 公司威胁 Linux 社区，可能现在我们就没有免费而超级好用的 Git 了。  
![](https://img-blog.csdnimg.cn/a07342f96fc04ad7b892d9007e8d51be.png)

**小结**

*   Git 是一个免费的、开源的分布式版本控制系统，可以快速高效地处理从小型到大型的各种项目。
    
*   Git 易于学习，占地面积小，性能极快。它具有廉价的本地库，方便的暂存区域和多个工作流分支等特性。其性能优于 Subversion、CVS、Perforce 和 ClearCase 等版本控制工具。
    

#### 1.5 Git 工作机制

![](https://img-blog.csdnimg.cn/27c7d6c928be41178e9478ced249899f.png)

1、工作区：存放代码的地方

2、暂存区：临时存储，将工作区的代码让 git 知道，通过 git add 将代码放到暂存区

3、本地库：将暂存区的代码提交到本地库，就会生成对应的历史版本，这个代码就无法删除

4、远程库：将本地库的代码推送到远程库

#### 1.6 Git 和代码托管中心

代码托管中心是基于网络服务器的远程代码仓库，一般我们简单称为远程库。

*   局域网
    *   [GitLab](https://baike.baidu.com/item/gitlab/3059600?fr=aladdin)：自己搭建远程库
    *   [gogs](https://gogs.io/docs)： Gogs 是一款极易搭建的自助 Git 服务
*   互联网
    *   GitHub （外网），可能无法访问
    *   **Gitee 码云**（国内网站）

比较出名的代码托管中心: GitHub 和码云

##### 1.6.1 什么是 GitHub？

确切的说 GitHub 是一家公司，位于旧金山，由 Chris Wanstrath, PJ Hyett 与 Tom Preston-Werner 三位开发者在 2008 年 4 月创办。这是它的 Logo：

![](https://img-blog.csdnimg.cn/08ed4870ffe147de9829c80269f835cb.png)

2008 年 4 月 10 日，GitHub 正式成立，地址：How people build software · GitHub ，主要提供基于 git 的版本托管服务。一经上线，它的发展速度惊为天人，截止目前，GitHub 已经发展成全球最大的开源社区。所以 Git 只是 GitHub 上用来管理项目的一个工具而已，GitHub 的功能可远不止于此！

##### 1.6.2 什么是码云？

我们使用 GitHub 的时候，会感觉比较慢，为什么？ 原因就是 GitHub 在遥远的美国，由于各种原因造成访问速度不怎么好，所以国内的 git 服务提供商，码云就起来了。

![](https://img-blog.csdnimg.cn/5f95771754d14ef0943fef04669c3b5a.png)

##### 1.6.3 产品功能对比

| 功能 | 码云 Gitee | GitHub |
| --- | --- | --- |
| 代码托管，支持 Git/SVN | √ | √ |
| 开源项目、代码片段 | √ | √ |
| Issue | √ | √ |
| Wiki | √ | √ |
| Fork + Pull Request | √ | √ |
| 组织 | √ | √ |
| 私有仓库免费协作人数 | 5 人 | 3 人 |
| 保护分支 | 免费 | 收费 |
| 在线 IDE（Gitee IDE） | √ | 不支持 |
| 仓库自动备份 | √ | 不支持 |
| 禁止 Git 强推 | √ | 不支持 |
| 支持仓库访问 IP 限制 | √ | 不支持 |
| 企业级研发协作 | 5 人免费 | 收费 |
| 敏捷开发管理 | √ |  |
| 任务看板（可灵活定义） | √ |  |
| 支持多级任务、关联任务 | √ |  |
| 自动代码质量分析 | √ |  |
| 快捷生成工作周报 | √ |  |
| 代码克隆检测 | √ |  |
| 自动生成 JavaDoc/PHPDoc | √ |  |
| 多语言 README 自动渲染 | √ |  |
| 支持微信/钉钉通知 | √ |  |

##### 1.6.4 协作开发流程

![](https://img-blog.csdnimg.cn/ac0741480a684df88f293da809fe3434.png)

### 2、软件安装

![](https://img-blog.csdnimg.cn/0e593076fa824d34b34738b6c25bf86d.png)

#### 2.1 Git 下载与安装

百度上搜索 Git

![](https://img-blog.csdnimg.cn/8bc506a3d76948de97ea856b901ad008.png)

官网：  
[https://git-scm.com/](https://git-scm.com/)

![](https://img-blog.csdnimg.cn/7d52d69df81f432198c8dbfb005f5035.png)

下载：[https://git-scm.com/download/win/](https://git-scm.com/download/win/)

![](https://img-blog.csdnimg.cn/13f66e9714d846e8bfb79560b416a8df.png)

下载 Git 安装程序，双击安装 Git-2.9.3.2-64-bit. Exe

![](https://img-blog.csdnimg.cn/e35712ded1fa439b81b13834056a2b5c.png)

配置环境变量 path

![](https://img-blog.csdnimg.cn/823c9b78e93d485080384b8c772dccd6.png)

使用 git --version 查看 git 是否安装成功

![](https://img-blog.csdnimg.cn/26c290ee5871499d82071a657e29207c.png)

#### 2.2 TortoiseGit 下载与安装

下载网址：[https://tortoisegit.org/download/](https://tortoisegit.org/download/)  
![](https://img-blog.csdnimg.cn/8eb0d7ddfd1843e78a3540fe9f9abcfe.png)

在桌面空白处鼠标右键

![](https://img-blog.csdnimg.cn/d899750d470442eeabcc4538d9040b2f.png)

说明 TortoiseGit 已经安装成功

### 3、Git 常用命令

| 命令名称                               | 作用      |
| ---------------------------------- | ------- |
| git config --global user. Name 用户名 | 设置用户名   |
| git config --global user. Email 邮箱 | 设置用户邮箱  |
| git init                           | 初始化本地库  |
| git status                         | 查看本地库状态 |
| git add 文件名                        | 添加到暂存区  |
| git commit -m " 日志信息" 文件名          | 提交到本地库  |
| git reflog                         | 查看历史记录  |
| git reset --hard 版本号               | 版本穿梭    |

#### 3.1 设置用户签名

**1**）基本语法

Git config --global user. Name 用户名

Git config --global user. Email 邮箱

**2**）案例实操

![](https://img-blog.csdnimg.cn/206c43743c9f498d9d36b57170936b11.png)

![](https://img-blog.csdnimg.cn/4c12681689b14ca5b5b1448d9f107835.png)

说明：

签名的作用是区分不同操作者身份。用户的签名信息在每一个版本的提交信息中能够看到，以此确认本次提交是谁做的。 Git 首次安装必须设置一下用户签名，否则无法提交代码。 ※注意： 这里设置用户签名和将来登录 GitHub （或其他代码托管中心）的账号没有任何关系。

#### 3.2 初始化本地库

**1**）基本语法

**git** **init** : 获取目录的管理权

**2**）案例实操

【第一步】在 d 盘创建目录：D:\\git-space\\git-0819

【第二步】进入 D:\\git-space\\git-0819 文件目录，右击鼠标，选择 git bush here

![](https://img-blog.csdnimg.cn/2ea1155998f1409382a8dc3ea10f1ccd.png)

【第三步】输入 git init 命令

![](https://img-blog.csdnimg.cn/ad3e104b42ce4150a81731845082461b.png)

【第四步】结果查看

![](https://img-blog.csdnimg.cn/83bdcfb9c91f4734b1394d6040454abb.png)

#### 3.3 查看本地库状态

**1**）基本语法

**git** **status**：

**2**）案例实操

**3.3.1** 首次查看（工作区没有任何文件）

![](https://img-blog.csdnimg.cn/39f4d58a2b8749e79ab54db5dd9b5775.png)

**3.3.2** 新增文件（**hello. Txt**）

![](https://img-blog.csdnimg.cn/4d9cc3aca1854949bf7e5ab52485920e.png)

(命令：yy 复制，p 粘贴)

3.3.3 再次查看 (检测到未追踪的文件)

红色代表这个文件虽然有了，但是至少存在工作区，git 从来没有追踪过这个文件

![](https://img-blog.csdnimg.cn/addaf0e180a6487f892057149168ab04.png)

#### 3.4 添加暂存区

##### 3.4.1 将工作区的文件添加到暂存区

**1**）基本语法

**git** **add** 文件名

**2**）案例实操

![](https://img-blog.csdnimg.cn/1dd183617b8f42dfa0bba72e0ddb8b94.png)

##### 3.4.2 查看状态（检测到暂存区有新文件）

![](https://img-blog.csdnimg.cn/6b31fa78adbf49808ba5701b1939c1d1.png)

#### 3.5 提交本地库

##### 3.5.1 将暂存区的文件提交到本地库

**1**）基本语法

git commit -m “日志信息” 文件名

**2**）案例实操

![](https://img-blog.csdnimg.cn/8f5b86ec97704a50a0a40d4900beffda.png)

##### 3.5.2 查看状态（没有文件需要提交）

![](https://img-blog.csdnimg.cn/7bd1e4f7154f49bd9b9fd7bce5cad078.png)

![](https://img-blog.csdnimg.cn/b6ca2eab48ad459085b74a78772f7cc7.png)

#### 3.6 修改文件（hello. Txt）

![](https://img-blog.csdnimg.cn/18daeca749434d98b0da97189f352d88.png)

##### 3.6.1 查看状态（检测到工作区有文件被修改）

![](https://img-blog.csdnimg.cn/47fa2abad2fe479b966111a33399942c.png)

##### 3.6.2 将修改的文件再次添加暂存区

![](https://img-blog.csdnimg.cn/a58345d55cd443468e75590122f76d33.png)

##### 3.6.3 查看状态（工作区的修改添加到了暂存区）

![](https://img-blog.csdnimg.cn/73237ba62b074bc0867da566e31cd911.png)

##### 3.6.4 提交到本地库

![](https://img-blog.csdnimg.cn/1eecd8fc905e4d61bc5dbddd4d39bfd3.png)

#### 3.7 历史版本

##### 3.7.1 查看历史版本

**1**）基本语法

**git** **reflog** 查看版本信息

**git** **log** 查看版本详细信息

**2**）案例实操

![](https://img-blog.csdnimg.cn/9787a8b9f58d4487b3a0bf4229534d8c.png)

##### 3.7.2 版本穿梭

**1**）基本语法

**git** **reset** **–hard** 版本号

**2**）案例实操

![](https://img-blog.csdnimg.cn/19551aab08414d309f47ce87f63a87f7.png)

Git 切换版本，底层其实是移动的 HEAD 指针。

### 4、 Git 分支操作

![](https://img-blog.csdnimg.cn/a3674baaae38454182012f32ff5dd8ce.png)

#### 4.1 什么是分支

在版本控制过程中，同时推进多个任务，为每个任务，我们就可以创建每个任务的单独分支。使用分支意味着程序员可以把自己的工作从开发主线上分离开来，开发自己分支的时候，不会影响主线分支的运行。对于初学者而言，分支可以简单理解为副本，一个分支就是一个单独的副本。（分支底层其实也是指针的引用）

#### 4.2 分支的好处

同时并行推进多个功能开发，提高开发效率。

各个分支在开发过程中，如果某一个分支开发失败，不会对其他分支有任何影响。失败的分支删除重新开始即可。

#### 4.3 分支的操作

| 命令名称 | 作用 |
| --- | --- |
| git branch 分支名 | 创建分支 |
| git branch -v | 查看分支 |
| git checkout 分支名 | 切换分支 |
| git merge 分支名 | 把指定的分支合并到当前分支上 |

##### 4.3.1 查看分支

**1**）基本语法

**git** **branch** **-v**

**2**）案例实操

![](https://img-blog.csdnimg.cn/af801b786e004ca0bd6976f6fb302320.png)

##### 4.3.2 创建分支

**1**）基本语法

**git** **branch** 分支名

**2**）案例实操

![](https://img-blog.csdnimg.cn/de83be10e89d49f7a624dcc604dc5417.png)

##### 4.3.3 切换分支

**1**）基本语法

**git** **checkout** 分支名

**2**）案例实操

【第一步】切换分支到 hot-fix，在 hot-fix 分支上做修改

![](https://img-blog.csdnimg.cn/f7e6e73f3d174fad87b7785064bc5d1e.png)

【第二步】修改 hot-fix 分支上的 hello. Txt

![](https://img-blog.csdnimg.cn/373821cea462437b9e47af74af5aa7c8.png)

修改内容如下：

![](https://img-blog.csdnimg.cn/7574aca85910459090899a71d3da29e0.png)

![](https://img-blog.csdnimg.cn/7657848b334b4a1fab7b25dbe5dc2c83.png)

##### 4.3.4 合并分支

**1**）基本语法

**git** **merge** 分支名

**2**）案例实操在 **master** 分支上合并 **hot-fix** 分支

【第一步】切换到 master 分支

![](https://img-blog.csdnimg.cn/40f0f0acd4c54ed7b34e00e080bfb83b.png)

【第二步】合并 hot-fix 分支

![](https://img-blog.csdnimg.cn/22fdb0dea2d249b099f6157f57e0c289.png)

【第三步】查看文件内容

![](https://img-blog.csdnimg.cn/6b67c95199814ba885d58a591735322f.png)

##### 4.3.5 产生冲突

冲突产生的表现： 后面状态为 MERGING

冲突产生的原因：

合并分支时，两个分支在同一个文件的同一个位置有两套完全不同的修改。 Git 无法替我们决定使用哪一个。必须人为决定新代码内容。

查看状态（检测到有文件有两处修改）

制造冲突：

【第一步】 切换到 master 分支上，修改 hello. Txt

![](https://img-blog.csdnimg.cn/27097c7b94264ab3926ab9089aad72de.png)

修改内容如下：

![](https://img-blog.csdnimg.cn/a3088e7c9dd943859b01d5df3c38cb87.png)

【第二步】 切换到 hot-fix 分支上，修改 hello. Txt

![](https://img-blog.csdnimg.cn/6aacc17217344bfab78db7516c520943.png)

修改内容如下：

![](https://img-blog.csdnimg.cn/89470684bf71418c8e9d91ba2e6ef4ea.png)

【第三步】 切换到 master 分支，merge 合并 hot-fix 分支

![](https://img-blog.csdnimg.cn/f01b7d3579cf4492b0a70340f52f7a34.png)

已经产生冲突！！！

![](https://img-blog.csdnimg.cn/8ce6bd5513eb4f559173a8deb61fd7ee.png)

##### 4.3.6 解决冲突

1）编辑有冲突的文件，删除特殊符号，决定要使用的内容

特殊符号： <<<<<<< HEAD 当前分支的代码 ======= 合并过来的代码 >>>>>>> hot-fix

![](https://img-blog.csdnimg.cn/1ba90e4ea40742b399cd58c6bff229ee.png)

​ 修改文件如下：

![](https://img-blog.csdnimg.cn/c98fc2b35e16469a9ec93cc62b32bb19.png)

2）添加到暂存区

![](https://img-blog.csdnimg.cn/bc31cb7f372f41978e53a82620b9b0bb.png)

3）执行提交（注意： 此时使用 git commit 命令时不能带文件名）

![](https://img-blog.csdnimg.cn/b68c5a87b5e144d69952d483c4cdfc41.png)

4）注意

我们修改的只是 master 分支的内容，hot-fix 分支的内容没有发生改变

### 5、 Git 团队协作机制

#### 5.1 团队内协作

![](https://img-blog.csdnimg.cn/495a36417e204173b8a7dbe564cf8ecf.png)

#### 5.2 跨团队协作

![](https://img-blog.csdnimg.cn/0028702b6dd04ae9afe0069cba053b42.png)

### 6、 Gitee 码云操作

码云网址：[https://gitee.com/](https://gitee.com/)

| 账号 | 验证邮箱 |
| --- | --- |
| yuanxinqi 2008 | yuanxinqi2008@126.com |
| yuanxinqi 2009 | yuanxinqi2009@126.com |
| yuanxinqi 2010 | yuanxinqi2010@126.com |

#### 6.1 创建远程仓库

![](https://img-blog.csdnimg.cn/01ad718e8c97475ca40f3a89beeff9cb.png)

![](https://img-blog.csdnimg.cn/142809c80e2f489199013218b45301fe.png)

#### 6.2 远程仓库操作

| 命令名称 | 作用 |
| --- | --- |
| git remote -v | 查看当前所有远程地址别名 |
| git remote add 别名远程地址 | 起别名（第一次） |
| git push 别名分支 | 推送本地分支上的内容到远程仓库 |
| git clone 远程地址 | 将远程仓库的内容克隆到本地（第一次） |
| git pull 远程库地址别名远程分支名 | 将远程仓库对于分支最新内容拉下来后与当前本地分支直接合并 |

##### 6.2.1 创建远程仓库别名

**1**）基本语法

**git** **remote** **-v** 查看当前所有远程地址别名

**git** **remote** **add** 别名远程地址

**2**）案例实操

![](https://img-blog.csdnimg.cn/0c7fd630c7024b1e9c46e3b1cd5f2fb2.png)

[https://gitee.com/yuanxinqi/git0819.git](https://gitee.com/yuanxinqi/git0819.git/)

这个地址在创建完远程仓库后生成的连接，如图所示红框中

![](https://img-blog.csdnimg.cn/4d329f232c0744b9a518987f5ef8b0e7.png)

##### 6.2.2 推送本地分支到远程仓库

**1**）基本语法

**git** **push** 别名分支 : 推送的最小单位是分支，所以一定要指定分支

**2**）案例实操

【第一步】切换到 master 主分支

![](https://img-blog.csdnimg.cn/4a4e51ff63cf47eca01b108b190a4607.png)

【第二步】git push git 0819 master 推送到主分支

![](https://img-blog.csdnimg.cn/08391bb89060432c89a97a3d902802e8.png)

【第三步】推送的时候需要登录

![](https://img-blog.csdnimg.cn/f5ab155e9b604cbf9afaf2d19e63a94e.png)

【第四步】推送成功，此时发现已将我们 master 分支上的内容推送到码云创建的远程仓库。

![](https://img-blog.csdnimg.cn/0d7d7ce2ef624aafb914cdc5eceaac0e.png)

##### 6.2.3 拉取远程仓库内容

**1**）基本语法

**git** **pull** 远程库地址别名远程分支名

**2**）案例实操

【第一步】远程操作修改文件

![](https://img-blog.csdnimg.cn/66c8a9e3941845cfa72478b4baade37b.png)

【第二步】修改内容如下：

![](https://img-blog.csdnimg.cn/82dcaa7c091741cfba2f790844623c42.png)

【第三步】提交修改

![](https://img-blog.csdnimg.cn/ca6dd5112f214322b6f6ed553443b844.png)

【第四步】本地拉取

![](https://img-blog.csdnimg.cn/5639ec86eeec461eafd6e42415cb3e4e.png)

【第五步】查看本地文件

![](https://img-blog.csdnimg.cn/5e564d96d7eb4c2086ad4ad0443dfa23.png)

##### 6.2.4 克隆远程仓库到本地

**1**）基本语法

**git** **clone** 远程地址

**2**）案例实操

【第一步】创建 git-0820 文件夹

![](https://img-blog.csdnimg.cn/7542ad7b48544518a714213f5541b4b6.png)

【第二步】执行克隆命令

![](https://img-blog.csdnimg.cn/b835779f9784477482a0a939372a9525.png)

##### 6.2.5 邀请加入团队

**1**）选择邀请合作者

![](https://img-blog.csdnimg.cn/4c2971df69444e629c5f002635433ec2.png)

**2**）填入想要合作的人

![](https://img-blog.csdnimg.cn/9341cf6146a7426d9d2080a973b58328.png)

**3** ） 复制地址并通过微信钉钉等方式发送给该用户，复制内容如下 ：  
[https://gitee.com/yuanxinqi/git0819/invite_link?invite=fa13a6a6c165941240d612a81902b3c7d3d58b53e8e9499fb7993663152babc51072802d03f1afc25f318cd36bbddc3a](https://gitee.com/yuanxinqi/git0819/invite_link?invite=fa13a6a6c165941240d612a81902b3c7d3d58b53e8e9499fb7993663152babc51072802d03f1afc25f318cd36bbddc3a/)

![](https://img-blog.csdnimg.cn/acce83e6e1e348f19aa19cb3f041818d.png)

**4**）在其他人打开链接，点击接受邀请。

**5**）成功之后可以在 yuanxinqi 2009 这个账号上看到 **git-Test** 的远程仓库。

![](https://img-blog.csdnimg.cn/cf27b5f4c97e47e5b67ab2bed10c998f.png)

**6**）yuanxinqi 2009 可以修改内容并 **push** 到远程仓库。

**7**）回到 yuanxinqi 2008 的 **GitHub** 远程仓库中可以看到，最后一次是 **yuanxinqi 2009**提交的。

#### 6.3 SSH 免密登录

我们可以看到远程仓库中还有一个 SSH 的地址，因此我们也可以使用 SSH 进行访问。

![](https://img-blog.csdnimg.cn/dea3cc1409f9453f8c81e3ed80a25d83.png)

具体操作如下：

【第一步】进入 windows 的家目录，C:\\Users\\yxq，删除. Ssh 文件

【第二步】在此处点击 git bash here

【第三步】输入命令： ssh-keygen -t rsa -C yuanxinqi2008@126.com ，然后点击三次回车

![](https://img-blog.csdnimg.cn/acfabaff9f6d4ea69d1f356c0ae6d136.png)

【第四步】查看. Ssh 文件

![](https://img-blog.csdnimg.cn/c1036437338c4c28b7f299e6df5de99f.png)

【第五步】点击 git bash here，进入. Ssh 目录

![](https://img-blog.csdnimg.cn/be367adee3d2450f907d58950977b50c.png)

【第六步】查看 id_rsa. Pub 文件内容

![](https://img-blog.csdnimg.cn/8cd4523795e74227a3b8a175db0807b9.png)

【第七步】登录 Gitee，点击用户头像→设置→SSH 公钥

![](https://img-blog.csdnimg.cn/e8d17c9fbfde40f4b8235dd546bb237c.png)
  
![](https://img-blog.csdnimg.cn/41171b6ab6074c9e8a209c8f167b076b.png)

【第八步】复制公钥内容，点击确定

![](https://img-blog.csdnimg.cn/bac083dcaaee4f5bbbddd80a8bbb5a61.png)

【第九步】输入密码认证，设置公钥成功

![](https://img-blog.csdnimg.cn/91f835927e4d404895bc78fc307285c1.png)

【第十步】测试

![](https://img-blog.csdnimg.cn/73434f6191e94b4d8b2b53f55401baff.png)

### 7、IDEA 集合 Git

#### 7.1 配置 Git 忽略文件-IDEA 特定文件

问题 \*\*1:\*\*为什么要忽略他们？

答： 与项目的实际功能无关，不参与服务器上部署运行。把它们忽略掉能够屏蔽 IDE 工具之间的差异。

问题 **2**：怎么忽略？

1）创建忽略规则文件 xxxx. Ignore （前缀名随便起，建议是 git. Ignore）

这个文件的存放位置原则上在哪里都可以，为了便于让~/. Gitconfig 文件引用，建议也放在用户家目录下

Git. Ignore 文件模版内容如下：

```
`# Compiled class file
*.class
# Log file
*.log
# BlueJ files
*.ctxt
# Mobile Tools for Java (J2ME)
.mtj.tmp/
# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar
#        virtual        machine        crash        logs,        see
http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
.classpath
.project
.settings
target
.idea
*.iml` 

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png)

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11
*   12
*   13
*   14
*   15
*   16
*   17
*   18
*   19
*   20
*   21
*   22
*   23
*   24
*   25


```

2）在. Gitconfig 文件中引用忽略配置文件（此文件在 Windows 的家目录中）

```
`[user]
	name = yuanxinqi
	email = yuanxinqi2008@126.com
[core]
excludesfile = C:/Users/yxq/git.ignore
	

注意：这里要使用“正斜线（/）”，不要使用“反斜线（\）”` 

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8


```

#### 7.2 定位 Git 程序

IDEA 配置 Git 程序

![](https://img-blog.csdnimg.cn/51ed17024bbe45ebb340a025af878039.png)

#### 7.3 初始化本地库

【目标】在 idea 中初始化项目，将项目纳入 git 管理

【第一步】VCS–> Import into Version Control --> Create Git Repository

![](https://img-blog.csdnimg.cn/76f0f206f7cd401a8af8d9b458bbf555.png)

【第二步】选择要初始化的本地项目

![](https://img-blog.csdnimg.cn/27d171d4cf1a4df480f232cc3b16744b.png)

【第三步】在该项目下生成了 .git 文件

![](https://img-blog.csdnimg.cn/0bace617e6cd42d9b18bc79dc95fb316.png)

#### 7.4 添加到暂存区

右键点击项目选择 Git -> Add 将项目添加到暂存区。

![](https://img-blog.csdnimg.cn/74afa96be2f54fdb8aa10d964ac10fac.png)

#### 7.5 提交到本地库

![](https://img-blog.csdnimg.cn/f4c9a48e9a8248079ecf5a552906fee0.png)

![](https://img-blog.csdnimg.cn/230f728dcd064c248dc4c249102d6602.png)

#### 7.6 切换版本

【第一步】在 IDEA 的左下角，点击 Version Control，然后点击 Log 查看版本

![](https://img-blog.csdnimg.cn/932d69abb9614b9aab62b30c590bc9e6.png)

【第二步】右键选择要切换的版本，然后在菜单里点击 Checkout Revision。

![](https://img-blog.csdnimg.cn/b67663978e024fd79e36b6ab0cd1b78b.png)

#### 7.7 创建分支

【第一步】选择 Git ，在 Repository 里面，点击 Branches 按钮。

![](https://img-blog.csdnimg.cn/a928aa3b59ad4c48ba9355ef12084a7f.png)

【第二步】在弹出的 Git Branches 框里，点击 New Branch 按钮。

![](https://img-blog.csdnimg.cn/ef5005849ff1423e8bfdc342324bb242.png)

【第三步】填写分支名称，创建 hot-fix 分支。

![](https://img-blog.csdnimg.cn/c3701f26d75a4563b55da92254f6ae34.png)

【第四步】在 IDEA 的右下角看到 hot-fix，说明分支创建成功，并且当前已经切换成 hot-fix 分支

![](https://img-blog.csdnimg.cn/40785da1a3da497f84092ca5b5c8107a.png)

#### 7.8 切换分支

【第一步】在 IDEA 窗口的右下角，切换到 master 分支。

![](https://img-blog.csdnimg.cn/6209240142f248ebac7695a69204b445.png)

【第二步】在 IDEA 窗口的右下角看到了 master，说明 master 分支切换成功。

![](https://img-blog.csdnimg.cn/4b50a7b364274b179436a96f64be7e8a.png)

#### 7.9 合并分支

【第一步】在 IDEA 窗口的右下角，将 hot-fix 分支合并到当前 master 分支。

![](https://img-blog.csdnimg.cn/4cd0198af6e0416992aa8089161cfed7.png)

【第二步】如果代码没有冲突，分支直接合并成功，分支合并成功以后，代码自动提交，无需手动提交本地库。

#### 7.10 解决冲突

如图所示，如果 master 分支和 hot-fix 分支都修改了代码，在合并分支的时候就会发生冲突。

【第一步】在 hot-fix 分支上，增加如下代码，并且提交

![](https://img-blog.csdnimg.cn/42e62403551d4079a1b227f694e530d6.png)

![](https://img-blog.csdnimg.cn/726cb9ac8bf44a3a824558cc5f0c3f54.png)

【第二步】在 master 分支上，增加如下代码，并且提交

![](https://img-blog.csdnimg.cn/75d7b7b88ff149008d12cd3ab780e06b.png)

![](https://img-blog.csdnimg.cn/7743265dc3fe4bb7a8eafe12ee98d09c.png)

【第三步】 我们现在站在 master 分支上合并 hot-fix 分支，就会发生代码冲突。

![](https://img-blog.csdnimg.cn/4b863551e25b4c3fa04109236525c93b.png)

点击 Conflicts 框里的 Merge 按钮，进行手动合并代码。

![](https://img-blog.csdnimg.cn/cdc059ede72d44cda9bb626695461ecb.png)

【第四步】手动合并代码

![](https://img-blog.csdnimg.cn/62ec5d05f151420fa720305ef60bf483.png)

手动合并完代码以后，点击右下角的 Apply 按钮。

代码冲突解决，自动提交本地库。

![](https://img-blog.csdnimg.cn/35b860f2da7945f5a7ee25283f9ba96b.png)

### 8、IDEA 集成码云

#### 8.1 IDEA 安装码云插件

【第一步】Idea 默认不带码云插件，我们第一步要安装 Gitee 插件。

如图所示，在 Idea 插件商店搜索 Gitee，然后点击右侧的 Install 按钮。

![](https://img-blog.csdnimg.cn/841c528c5bc2485c93cfe89805bacde0.png)

安装成功后，重启 Idea。

Idea 重启以后在 Version Control 设置里面看到 Gitee，说明码云插件安装成功。

![](https://img-blog.csdnimg.cn/9de7c71e871246c78c07e6ba786cbb66.png)

【第二步】在码云插件里面添加码云帐号，我们就可以用 Idea 连接码云了。![](https://img-blog.csdnimg.cn/322b899588e34d7e86fbd94fb61a49d9.png)

![](https://img-blog.csdnimg.cn/ea32e9804d7a42dd9ce98103031c3426.png)

#### 8.2 分析工程到码云 Gitee

【第一步】选择 Share…

![](https://img-blog.csdnimg.cn/588f14ba2a5f492f9b87e41cc953f87e.png)

【第二步】填入信息，点击 share

![](https://img-blog.csdnimg.cn/0d13c03ae0b442cf9e765e2b0066472b.png)

【第三步】成功提醒：

![](https://img-blog.csdnimg.cn/d7302de139594886b744fb0f4ab020da.png)

【第四步】查看 gitee 码云工程

![](https://img-blog.csdnimg.cn/a0a4662d8fba4da2919b2fe585fd9e5a.png)

#### 8.3 将本地代码 push 到码云远程库

【第一步】点击 push

![](https://img-blog.csdnimg.cn/9dfebf252d45493f812ff38c889b4295.png)

【第二步】自定义远程库链接

![](https://img-blog.csdnimg.cn/fc989381910f4e80abc95cc824efae13.png)

【第三步】给远程库链接定义个 name，然后再 URL 里面填入码云远程库的 HTTPS 链接即可。码云服务器在国内，用 HTTPS 链接即可，没必要用 SSH 免密链接。

![](https://img-blog.csdnimg.cn/b9500c03c4ff490f9f83fbc9bc297865.png)

然后选择定义好的远程链接，点击 Push 即可。

【第四步】看到提示就说明 Push 远程库成功。

![](https://img-blog.csdnimg.cn/ece6cfcf55db419aab5186b0188c3494.png)

【第五步】去码云远程库查看代码。

#### 8.4 pull 拉取远程库到本地库

【第一步】直接在服务器修改代码

![](https://img-blog.csdnimg.cn/821bcb4426c34ce99cb264152fcc9fb5.png)

【第二步】选择 pull

![](https://img-blog.csdnimg.cn/91e23ecb8a6a4f6c96eba2582e566822.png)

【第三步】查看结果

=========================================================

##### 后记

![](https://img-blog.csdnimg.cn/313d0f66be254974a66c39a21391bd9b.gif)

好啦，以上就是本期全部内容，能看到这里的人呀，都是**能人**。

**十年修得同船渡，大家一起点关注。** 

我是♚焕蓝·未来，感谢各位【能人】的：**点赞**、**收藏**和**评论**，我们下期见！

各位能人们的支持就是♚焕蓝·未来前进的巨大动力~

注：如果本篇 Blog 有任何错误和建议，欢迎能人们留言！