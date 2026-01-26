[PVE虚拟化平台之安装Ubuntu Desktop系统-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2400432) 


# 一、Ubuntu 介绍

### 1.1 Ubuntu 简介

> Ubuntu，是一款基于 Debian Linux 的以桌面应用为主的操作系统，内容涵盖文字处理、电子邮件、软件开发工具和 Web 服务等，可供用户免费下载、使用和分享。

### 1.2 Ubuntu 版本

> Ubuntu 发行版主要提供以下版本:

*   Ubuntu Desktop：适用于桌面计算机的主要版本。
*   Ubuntu Server：适用于服务器的版本。

### 1.3 ubuntu 命名规则

*   ubuntu 命名规则：前两位数字为发行时的年份年份的最后两位数字，后两位为发行的月份，中间以一个英文小数点隔开。 LTS 表示长期支持版本，表示 ubuntu 会在一定时间范围内对这个版本进行维护和更新。
*   Ubuntu 每六个月发布一个非 LTS 版本，每两年发布一个 LTS 版本，每个 LTS 有 5 年的维护时间。
*   Ubuntu 还有一个代号，以字母顺序依次命名自己的版本。每一个版本的代号都是由两个单词组成，第一个单词是以字母顺序排列的动物名称，第二个单词是以字母顺序排列的形容词。如 Ubuntu 20.04 的代号是"Focal Fossa"，其中"Focal"是形容词，"Fossa"是动物名。

命令示例：

*   18.04 LTS：Bionic Beaver（仿生海狸）
*   16.04 LTS：Xenial Xerus（异域松鼠）
*   14.04 LTS：Trusty Tahr（可靠的大羚羊）
*   12.04 LTS：Precise Pangolin（精准穿山甲）

二、上传镜像到 PVE
----------

### 2.1 检查 PVE 环境

> 登录访问 PVE 平台，检查 PVE 环境状态正常。

![](https://developer.qcloudimg.com/http-save/4995888/12d201b401d741379fdb21826c44fcaf.png)

### 2.2 上传镜像到 PVE

[Ubunto官网](https://cn.ubuntu.com/)下载镜像，将 ubuntu-23.04-desktop-amd 64. Iso 镜像文件上传到 PVE 存储。


![](https://developer.qcloudimg.com/http-save/4995888/b478c3a0da5d21ec79463b184fc55bbf.png)

![](https://developer.qcloudimg.com/http-save/4995888/89bf509fced9cfde174e42eb9dfac09f.png)

三、新建虚拟机
-------

### 3.1 设置虚拟机名称

> 设置虚拟机名称 Ubuntu-Desktop

![](https://developer.qcloudimg.com/http-save/4995888/8304574d4d0fb9a596830e21ef672bd8.png)

### 3.2 操作系统设置

> 选择镜像存储位置，选择 ISO 镜像 ubuntu-23.04-desktop-amd 64. Iso。

![](https://developer.qcloudimg.com/http-save/4995888/0fd81f11a00875619660c8b51b60254d.png)

### 3.3 系统设置

> 选择默认配置即可。

![](https://developer.qcloudimg.com/http-save/4995888/21ac32a5d0e30fa826bba0517538cb13.png)

### 3.4 磁盘设置

> 选择存储，磁盘大小根据需要自行设置，这里设置 300 G 大小，其余默认，下一步即可。

![](https://developer.qcloudimg.com/http-save/4995888/cd85201536da7f3545b65e90c8d5d50e.png)

### 3.5 cpu 设置

> 根据机器配置和自身需要自定义设置，这里设置 cpu 2 个核心。

![](https://developer.qcloudimg.com/http-save/4995888/2973cb5741422dec7c76b9d7de349f50.png)

### 3.6 内存设置

> 可根据自身需要设置内存大小，这里选择设置 4 G。

![](https://developer.qcloudimg.com/http-save/4995888/f1350dff100e735e7a243de67af33075.png)

### 3.7 网络设置

> 默认配置即可。

![](https://developer.qcloudimg.com/http-save/4995888/fa1b9c2b0f25e8eee477a6c4933e0cae.png)

### 3.8 确认虚拟机配置信息

> 检查虚拟机配置信息，确认新建虚拟机。

![](https://developer.qcloudimg.com/http-save/4995888/1f6c27df537575beb219e97535c85402.png)

四、安装 Ubuntu Desktop
------------------

### 4.1 打开虚拟机

> 打开新建虚拟机，进入控制台界面。

![](https://developer.qcloudimg.com/http-save/4995888/3f369f5ec368337ecc8a25080b8457c6.png)

### 4.2 选择安装系统

> 选择第一个选项，安装 ubuntu。

![](https://developer.qcloudimg.com/http-save/4995888/05a840e22c61d4b5b3946a80795a7d9c.png)

![](https://developer.qcloudimg.com/http-save/4995888/49fd26290c20562e55ae21e1c7c749e3.png)

### 4.2 选择语言

> 选择简体中文。

![](https://developer.qcloudimg.com/http-save/4995888/b57fe1d5bfd7dcb92bd49225144d7a9c.png)

### 4.3 选择安装 ubuntu

> 选择安装 ubuntu

![](https://developer.qcloudimg.com/http-save/4995888/08fa9716b5241ea4b768c304c31eb512.png)

### 4.4 键盘布局设置

> 选择汉语。

![](https://developer.qcloudimg.com/http-save/4995888/0db37220a52cf7309163ee2513973dca.png)

### 4.5 连接互联网

> 使用有线连接互联网。

![](https://developer.qcloudimg.com/http-save/4995888/dd83cb612d08862e53f10f77ca15ba78.png)

### 4.6 应用安装

> 选择正常安装，其他选项，可根据需要选择，这里都勾选。

![](https://developer.qcloudimg.com/http-save/4995888/d89baac5296f66efae1b13b2a166ae01.png)

### 4.7 手动分区

> 选择手动分区，根据自身需求进行分区，根 windows 的磁盘划分类似，根分区尽量大些。

![](https://developer.qcloudimg.com/http-save/4995888/6b573c5e06c206809a62ed8b6ca468ae.png)

![](https://developer.qcloudimg.com/http-save/4995888/e0f286ea437256eaa1cb7e7b9a8f88c1.png)

### 4.8 选择时区

> 准备安装系统，选择上海时区。

![](https://developer.qcloudimg.com/http-save/4995888/e8d8e4ffbf0dfdebc99142089e8b56d2.png)

![](https://developer.qcloudimg.com/http-save/4995888/54a0a0897f57b939bff1080eefe284b7.png)

### 4.9 设置账户

> 设置电脑信息，用户名自定义设置即可。

![](https://developer.qcloudimg.com/http-save/4995888/e12fd0076395e1c5bc26c575a3b9a98d.png)

### 4.10 开始安装系统

> 开始安装系统，等待系统安装完毕。

![](https://developer.qcloudimg.com/http-save/4995888/b7f85b7752945f944225efa5eec58f35.png)

五、Ubuntu Desktop 的基本使用
---------------------

### 5.1 进入本地控制台

> 安装完毕后，按提示重启虚拟机，进入系统。

![](https://developer.qcloudimg.com/http-save/4995888/3949c8dd0767da84718d3ad40cf9bc33.png)

![](https://developer.qcloudimg.com/http-save/4995888/b2539a955d57c58d47f8964bd49fdb8a.png)

### 5.2 打开命令行终端

> 打开命令行终端

![](https://developer.qcloudimg.com/http-save/4995888/7de53982a908895b7f6d9de3585d19d3.png)

![](https://developer.qcloudimg.com/http-save/4995888/558b031cadd3b61e456ac8f29bf95993.png)

### 5.3 打开浏览器

> 打开火狐浏览器，访问网页。

![](https://developer.qcloudimg.com/http-save/4995888/28e145fa3d0c4a7961471ad2bec70e06.png)

### 5.4 打开 LibreOffice Writer

> LibreOffice 套件是一个受欢迎的替代性免费办公套件，它包含了文档、电子表格、演示文稿、计算等方面的产品。其中，LibreOffice Writer 是一个广泛的办公文档工具。它有许多顶级功能，如传统的字体管理器、字体定制器、页眉、页边距等。它的用户界面与其他办公产品非常相似。

![](https://developer.qcloudimg.com/http-save/4995888/15585e11746e9386bd452279114c31b2.png)

### 5.5 查看本地 IP 地址

> 查看本地的 IP 地址

![](https://developer.qcloudimg.com/http-save/4995888/d86c724d7f93d9d95891fdef4aecdf7a.png)

### 5.6 更改 root 密码

> 在命令行终端，更改 root 密码

代码语言：bash

复制

```
$sudo -i
$sudo passwd root #然后两次输入密码和确认密码即可修改成功
```

![](https://developer.qcloudimg.com/http-save/4995888/825d9ae70152706c4d8985b8f399bcae.png)

