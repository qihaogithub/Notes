---
介绍: 此插件添加了创建具有多列可见内容的标记文档的功能
评级: "0"
---
拿你无聊的 markdown 文档，给它添加一些列！使用 Multi Column Markdown 而不是将文档布局限制为单个线性文件，您现在可以定义要水平相邻放置的数据块。这个附加功能让您可以自由地以更有创意的方式来组织您的笔记

效果如下

```start-multi-column  
ID: ExampleRegion1  
number of columns: 2  
largest column: left  
```

第1列中显示的文本。

--- end-column ---

第2列中显示的文本。

=== end-multi-column


### **区域开始标记：

每个多列区域必须以以下之一开头：

````
```start-multi-column  
ID: A\_unique\_region_ID  
```
````
或者

````
```multi-column-start  
ID: A_unique_region_ID_1  
```
````

定义开始标记后，您必须为该区域声明一个 ID。如果同一文档中有多个，则使用 ID 来区分不同的区域。

每个 ID 在同一文档中必须是唯一的，否则可能会出现意外的呈现问题。一个 ID 可以跨多个文档使用，例如，您可以在用于 Periodic Notes 的模板中使用 ID“dailynote”。

通过使用“插入多列区域”命令（详见下文），起始 ID 将预先设置为随机生成的 4 个字符的字符串。

您还可以使用“修复丢失的 ID”命令，该命令将搜索当前打开的文档并将随机 ID 附加到所有丢失的区域。

  

### **有效语法标签：

可以使用以下选项定义每种标签类型：

#### **启动多列区域：


````
```start-multi-column  
ID: A\_unique\_region_ID  
_Any Additional Settings (see below)_  
```
````

````
```multi-column-start
ID: A_unique_region_ID_2
Any Additional Settings (see below)
```
````

#### **结束专栏：

```
--- column-end ---
--- end-column ---
--- column-break ---
--- break-column ---
```

#### 结束多列区域


`=== end-multi-column
=== multi-column-end `



### **有效设置选项：

#### **ID：

*   任意字符串。
*   如果同一文档中有多个，则使用 ID 来区分不同的区域。
*   每个 ID 在同一文档中必须是唯一的，否则可能会出现意外的呈现问题。一个 ID 可以跨多个文档使用，例如，您可以在用于 Periodic Notes 的模板中使用 ID“dailynote”。
*   如果文档中只有一个列区域，则可以省略。

#### **列数：

*   1、2 或 3

#### **最大的列：

默认情况下，如果省略此选项，所有列都将设置为相等大小。
对于 2 列或 3 列布局
-   Standard
-   Left
-   First
-   Right
-   Second 
仅适用于 3 列布局
-   Center
-   Third
-   Middle

#### **边界：

默认情况下，边框是启用的，但可以通过以下方式删除：

-   disabled
-   off
-   false

#### **阴影：

默认情况下打开，可以通过以下方式删除：

-   disabled
-   off
-   false

#### **列大小：

仅与单列选项一起使用。
有效选项：
-   Small
-   Medium
-   Large
-   Full

#### **列位置或列位置：
仅与单列选项一起使用。
有效选项：
-   Left
-   Right
-   Center
-   Middle

#### **列间距：

*   用于设置所有列之间的距离。
*   允许_大多数_CSS 单位长度（px、pt、% 等）。
*   没有定义单位类型的数字默认为 pt 单位。

#### **内容溢出：

列是否应该切断列边界之外的任何内容，或者它应该是可滚动的。
有效选项：
-   Scroll (Default)
-   Hidden

#### **结盟：

选择列中内容的对齐方式。
有效选项
-   Left (Default)
-   Center
-   Right

  

自动布局
自动布局区域不使用定义的分栏符。相反，这些类型的多列区域将尝试在列之间平均平衡所有内容。还尝试保留标题，以便标题块不会结束列，而是将移动到具有相应内容的下一列的顶部。

要使用此功能，请在区域设置中设置“Auto Layout: true”。


实时预览
Multi-Column Markdown 现在支持实时预览，但是此模式可能支持也可能不支持与其他插件的交叉兼容性。由于自定义实时预览插件是如何在 CodeMirror6 中实现并挂接到 Obsidian 的，我无法保证此时所有插件都能在实时预览中正确呈现。不立即呈现其内容的插件（例如需要等待数据视图查询）无法正确呈现。然而，大多数插件在阅读模式下查看列时仍保持交叉兼容性。


# **完整示例：**

````
```start-multi-column  
ID: ExampleRegion3  
```
````
# 第 1 列
=== end-column ===
# 第 2 列
=== end-multi-column

效果如下
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230418180636.png)


````
```start-multi-column  
ID: ExampleRegion4  
number of columns: 3  
border: off  
```
````
# Column 1
--- end-column ---
# Column 2
--- end-column ---
# Column 3
=== end-multi-column

效果如下
[![Eample_3Column_1](https://github.com/ckRobinson/multi-column-markdown/raw/master/images/Example_3Column_1.png?raw=true)]( https://github.com/ckRobinson/multi-column-markdown/blob/master/images/Example_3Column_1.png?raw=true )

````
```start-multi-column  
ID: ExampleRegion5  
number of columns: 3  
largest column: center  
```
````
#### Column 1
--- end-column ---
# Column 2
--- end-column ---
#### Column 3
=== end-multi-column 

呈现为:
[![Eample_3Column_2](https://github.com/ckRobinson/multi-column-markdown/raw/master/images/Example_3Column_2.png?raw=true)](https://github.com/ckRobinson/multi-column-markdown/blob/master/images/Example_3Column_2.png?raw=true)

````
```start-multi-column  
ID: ExampleRegion6  
number of columns: 1  
column size: medium  
column position: left  
```
````
#### Single Left Aligned Column

=== end-multi-column

呈现为: 
[![Example_4Column_1](https://github.com/ckRobinson/multi-column-markdown/raw/master/images/Example_4Column_1.png?raw=true)]( https://github.com/ckRobinson/multi-column-markdown/blob/master/images/Example_4Column_1.png?raw=true )





### 需要注意的事项:

您不能将一个多列区域嵌套在另一个多列区域中。

### **可用命令：


您可以使用 ctrl/command - P 访问命令托盘。

#### **插入多列区域**

将创建一个两列区域，其中光标所在的位置具有随机生成的 ID 和创建的默认设置块。当前选择的任何内容都将移到插入区域的末尾之外，以免覆盖任何数据。

#### **修复多列区域的缺失 ID**

将在当前文档中搜索任何缺少 ID 的区域开始标记，并为每个区域随机生成新的 ID。
Toggle 移动渲染 - 多列 Markdown**

仅在移动设备上启用或禁用列呈现。


