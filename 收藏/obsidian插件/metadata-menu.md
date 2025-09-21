---
简介: 图形化的元数据管理器，基于Dataview增强，方便修改YAML和内联字段值
分类:
  - 知识组织与可视化
---
obsidian社区插件

Obsidian 插件：Metadata Menu 图形化的 Frontmater 管理器

* * *

插件ID：metadata-menu metadata-menu metadata menu：Obsidian 插件：Metadata Menu插件是基于dataview的一个功能增强的插件。它基于\`属性::值\`的一种结构，可以很方便的修改一个特定属性的值。比如：\`性别::男\`。通过插件，就可以通过鼠标点击，来直接修改为\`女\`

Metadata Menu插件是为数据质量爱好者和Dataview用户设计的，可以访问和管理Obsidian笔记的元数据。该插件通过右键单击链接或在Dataview表格中，添加上下文菜单项来修改目标笔记的前置字段和“内联字段”（dataview语法）。用户可以在插件设置中全局定义预设类型和值，也可以通过文件类别定义在文件级别上定义。此外，插件还支持内联字段的自动完成，提供基于预设值的建议值。Metadata Menu可以管理位于前置（YAML语法）

Metadata Menu插件是为数据质量爱好者和Dataview用户设计的，可以访问和管理Obsidian笔记的元数据。该插件通过右键单击链接或在Dataview表格中，添加上下文菜单项来修改目标笔记的前置字段和“内联字段”（dataview语法）。用户可以在插件设置中全局定义预设类型和值，也可以通过文件类别定义在文件级别上定义。此外，插件还支持内联字段的自动完成，提供基于预设值的建议值。Metadata Menu可以管理位于前置（YAML语法）或笔记正文中的任何元数据字段，提供多种字段类型，如Input、Boolean、Number、Select等，满足不同需求。插件提供多种操作控制方式，包括自动完成、右键菜单、Dataview表格等，为用户提供便捷的元数据管理功能。

> **插件名片**
> 
> *   插件名称：Metadata Menu
> *   插件版本：0.4.21
> *   插件作者：mdelobelle
> *   插件说明：Metadata Menu 是方便修改 YAML 值的一个工具
> *   插件分类：编辑工具, 效率, YAML, 定制属性，修改，属性预览
> *   插件项目地址：[点我访问](https://github.com/mdelobelle/metadatamenu)
> *   国内下载地址：[下载安装](https://pkmer.cn/products/plugin/pluginMarket/?metadata-menu)

概述
--

Metadata Menu 插件是基于 dataview 的一个功能增强的插件。它基于 `属性::值` 的一种结构，可以很方便的修改一个特定属性的值。比如：`性别::男`。通过插件，就可以通过鼠标点击，来直接修改为 `女`。

插件配置
----

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604145024.png!pkmer)

在五个配置项中，我们只关注 `Preset Fields settings`。在这里面定义的功能，可以在任意一个文档中使用。

现在我们添加一个字段，来进行使用。

### 字段类型

元数据菜单为每个字段提供了一个类型。

可用的类型有：

*   `Input`（自由文本）：如果没有为该字段设置任何内容（参见＃字段设置），则默认应用此类型。它将 `接受任何值`
*   `Boolean`：可以 `接受true或false` 或 null 值的字段
*   `Number`：可以 `接受数字`（浮点数）值，可选地在范围（`min`，`max`）内，并且可以通过 `step` 值（默认为 1）进行增加/减少
*   `Select`：可以从列表中 `接受单个值` 的字段
*   `Multi`：可以从列表中 `接受多个值` 的字段
*   `Cycle`：将从列表中 `循环显示值` 的字段
*   `File`：将从您的保险库中 `接受文件链接` 的字段
*   `MultiFile`：将 `接受多个链接` 的字段
*   `Date`：将 `接受日期` 的字段
*   `Lookup`：将 `接受查找查询` 的字段
*   `Canvas`：将根据画布中的链接 `更新` 的字段
*   `Canvas Group`：将根据画布中的组 `更新` 的字段
*   `Canvas Group Link`：将根据画布中的组链接 `更新` 的字段

全局属性修改
------

### 添加全局字段

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150251.png!pkmer)

1.  点击 `Add new`，打开字段配置界面

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150306.png!pkmer)

1.  将自己想要管理的字段输入到 `Field Name` 后面的输入框中，点击√即可完成。

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150311.png!pkmer)

1.  完成效果图

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150321.png!pkmer)

### 全局字段使用

1.  新建一个文档，点开右键菜单

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150351.png!pkmer)

1.  选择 `Add field at cursor`，将数据添加到当前行。

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150355.png!pkmer)

1.  选择 `名称` 这个选项，并在其中输入想要输入的内容

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150400.png!pkmer)

1.  结果显示

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150405.png!pkmer)

这样，我们就可以在任何一个文档中，对自己定义的属性进行添加。

文件类
---

接下来，我们讲解一下新功能**文件类**。

下面是它的功能说明：

*   可以只针对单个文件
*   可以修改的属性由引用的模板决定
*   可以针对某一种类型，定制需要的属性

### 设置

对面板进行设置

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150434.png!pkmer)

1.  文件类的存放的文件夹
2.  fileclass 的自定义名称（可以使用任何名字）

已经设置好的配置如下：

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150440.png!pkmer)

### 建立一个文件类模板

1.  在模板文件夹中建立一个文件 `笔记类`

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150449.png!pkmer)

1.  输入想要创建的文件类名字，并点击创建

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150454.png!pkmer)

1.  打开命令界面，选择下面提示的命令

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150458.png!pkmer)

1.  输入要添加的属性名称，点击√即可

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150503.png!pkmer)

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150515.png!pkmer)

1.  按照前面提到的方式，继续添加自己想要添加的属性

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150520.png!pkmer)

接下来，我们就可以使用刚才创建的 `笔记类` 模板了。

### 使用文件类模板

1.  在想要使用文件类的文档中，点击右键

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150526.png!pkmer)

1.  选择想要添加的文件类

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150533.png!pkmer)

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150538.png!pkmer)

1.  添加预设置的属性

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150543.png!pkmer)

1.  选择要添加的属性

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150549.png!pkmer)

1.  输入对应属性的值

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150555.png!pkmer)

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150941.png!pkmer)

1.  按照上面的 3-5 步，添加其他的属性值

![](https://cdn.pkmer.cn/images/Pasted%20image%2020230604150604.png!pkmer)

总结
--

这就是 Metadata Menu 的基础教程了。一共介绍了两种文件类的方式，全局文件类与模板文件类。全局文件类，可以适用于任何文档中的属性修改（使用了模板文件类的除外）。但是这些属性，只能是一些很通用、很常用的属性，且数量不会很多，10 个以内。而模板文件类，只能应用于单个文档。它的好处就是可以定制于专属的属性，可以将一个物品的属性列到很详细，几十个没有问题。

> **讨论**
> 
> 若阁下有独到的见解或新颖的想法，诚邀您在文章下方留言，与大家共同探讨。

metadata-menuObsidian社区插件

pkmer forum 论坛相关