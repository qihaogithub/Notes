---
介绍: 用来添加警告块样式块
评级: "4"
---
#软件/obsidian #插件 

[官方文档](https://plugins.javalent.com/admonitions)

Admonition语法结构
```ad-<type> # 警告类型
title:                  # 标题
collapse:               # 创建可折叠的警告。
icon:                   # 覆盖图标。
color:                  # 覆盖颜色。
这里是正文内容
```

```ad-note
title:
将标题字段留空以仅显示警告。
```

```ad-note
title: 创建可折叠警告
collapse: open
使用`collapse`参数创建可折叠的警告。
`collapse: open`将启动在渲染时打开的警告，但允许在单击时折叠。
如果提供了空白标题，则折叠参数将不执行任何操作。
默认情况下，警告可以在设置中设置为可折叠。

```

```ad-note
title: 自定义图标
icon: triforce
警告图标可以使用`icon`参数覆盖。==输入的图标名称必须与 [FontAwesome](https://fontawesome.dashgame.com/) 或 RPGAwesome 中的图标名称完全相同。==

```

```ad-note
title: 自定义颜色
icon: triforce
警告图标可以使用`icon`参数覆盖。==输入的图标名称必须与 FontAwesome 或 RPGAwesome 中的图标名称完全相同。==

```


`````ad-note
title: 嵌套的警告
collapse: open

Hello!

````ad-note
title: 此警告是嵌套的。
这是一个嵌套的警告！

```ad-warning
title: 此警告已关闭。
collapse: close
```

````
这是最初的警告。
`````


````ad-info
在Admonitions中加入代码块
代码块可以使用类似于上述嵌套警告的方法嵌套在警告中。
此外，对于单层，`~~~`可以使用降价代码块语法

```ad-bug
title: 这是嵌套的代码块
~~~javascript
throw new Error("Oops, I'm a bug.");
~~~
```

```javascript
console.log("Hello!");
```
`````

当前支持以下警告类型：
| 类型 | 别名|
| --- | --- |
| note | note, seealso |
| abstract | abstract, summary, tldr |
| info | info, todo |
| tip | tip, hint, important |
| success | success, check, done |
| question | question, help, faq |
| warning | warning, caution, attention |
| failure | failure, fail, missing |
| danger | danger, error |
| bug | bug |
| example | example |
| quote | quote, cite |


```ad-col
<div> 
第一栏
</div>
<div> 
第二栏
</div>

```


```ad-orange
这是用admonition实现的高亮块，你应该学会使用它。*重要*
- <font style="color: #42b983; font-weight: 500">高亮块功能很好用</font>，我可以输入不同颜色的文本
- ==非常棒的功能==
- <font style="background: rgb(253, 226, 226); font-weight: 500; color: rgb(216, 57, 49)">显示有背景的文本高亮</font>
- [开始在 GitHub 上编写和格式化 - GitHub Docs](https://docs.github.com/cn/github/writing-on-github/getting-started-with-writing-and-formatting-on-github)，我也可输入 URL 链接
```

```ad-note
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.
```

