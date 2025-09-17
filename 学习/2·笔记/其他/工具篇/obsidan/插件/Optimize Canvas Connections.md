---
介绍: 一个插件，通过使用笔记的最近边缘重新连接笔记来整理画布。
标签:
  - canvas
评级: "1"
---
github:: [GitHub](https://github.com/felixchenier/obsidian-optimize-canvas-connections)

假设你开始画布。

[![图1](https://github.com/felixchenier/obsidian-optimize-canvas-connections/raw/master/images/fig1.png)](https://github.com/felixchenier/obsidian-optimize-canvas-connections/raw/master/images/fig1.png)

然后你在集思广益的同时移动所有东西。音符之间的联系可能很快就会变得一团糟。

[![图 2](https://github.com/felixchenier/obsidian-optimize-canvas-connections/raw/master/images/fig2.png)](https://github.com/felixchenier/obsidian-optimize-canvas-connections/raw/master/images/fig2.png)

这个简单的插件使用最近的边缘自动将音符重新连接在一起。

选择要重新连接的笔记，然后运行命令：

`Optimize Canvas Connections: Optimize selection (preserve axes)`

或者

`Optimize Canvas Connections: Optimize selection (shortest path)`

[![图 3](https://github.com/felixchenier/obsidian-optimize-canvas-connections/raw/master/images/fig3.png)](https://github.com/felixchenier/obsidian-optimize-canvas-connections/raw/master/images/fig3.png)

## [](https://github.com/felixchenier/obsidian-optimize-canvas-connections#shortest-path)最短的路径

该`shortest path`选项使用最近的边缘重新连接音符，始终使用可能的最短路径。这是最激进的做法。

## [](https://github.com/felixchenier/obsidian-optimize-canvas-connections#preserve-axes)保留轴

该`preserve axes`选项还使用最近的边缘重新连接音符，但它尊重连接最初开始和结束的轴。例如，从音符右侧开始的连接可以更改为从左侧开始，但不能从顶部或底部开始。使用此选项可保留垂直和水平流中的含义（例如，从上到下 = 时间，从左到右 = 细节）。

**有疑问，使用`preserve axes`.**

在这两种情况下，当没有选择音符时，优化将应用于整个画布。