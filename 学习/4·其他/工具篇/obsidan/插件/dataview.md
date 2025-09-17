---
介绍: 将您的Obsidian Vault视为可以从中查询的数据库。提供 JavaScript API 和基于管道的查询语言，用于从 Markdown 页面过滤、排序和提取数据
评级: "5"
---

[obsidian插件之dataview入门 - 经验分享 - Obsidian 中文论坛](https://forum-zh.obsidian.md/t/topic/195)
[官方文档](https://blacksmithgu.github.io/obsidian-dataview/)

# 案例
列出笔记里所有笔记
````
```dataview 
LIST 
```
````

24小时内被修改的文件
```
LIST 
WHERE file.mtime >= date(today) - dur(1 day)
```
某个文件夹里的内容，按照修改时间排序
```
list
from "笔记/常用"
sort file.mtime desc
````
列出目标文件夹下的所有任务

```text
```dataview
task from "1·常用"
```
查询本周代办

````text
```dataview  
TASK  
WHERE !fullyCompleted AND due >= date(sow) AND due <= date(eow)  
GROUP BY section  
```
````

查询最近的10项待办事项。
````text
```dataview
task where !completed
sort file.ctime desc
limit 10
```
````
未完成任务
````
```dataview
task
WHERE !completed
```
````
`WHERE !completed` 表示未完成任务
查询 `4·工作/2·待办/项目文档` 文件夹中标签为  `#工作/App` 扥 LIST 
````
```dataview 
LIST 
from #工作/App AND "4·工作/2·待办/项目文档"
```
````

# 笔记
dataview 分为四个字段
## 1、视图
表示显示成什么样子，开头有三种，分别是list、table、task，意思是列表、表格、任务。
## 2、数据来源
开头是from。可以是文件夹，标签，链接。
## 3、筛选条件
样式为contains(属性名,"属性" )，括号中写条件。例如contains(file.name,"习惯")，意思是匹配文件名中包含“习惯”两个字的笔记。
Dataview 会自动为每个页面添加大量元数据：
-   `file.name`：文件标题（字符串）。
-   `file.folder`：该文件所属文件夹的路径。
-   `file.path`：完整的文件路径（字符串）。
-   `file.ext`: 文件类型的扩展名；通常是“.md”（一个字符串）。
-   `file.link`：文件的链接（链接）。
-   `file.size`：文件的大小（以字节为单位）（一个数字）。
-   `file.ctime`：文件的创建日期（日期+时间）。
-   `file.cday`：文件的创建日期（只是一个日期）。
-   `file.mtime`：文件最后修改的日期（日期+时间）。
-   `file.mday`：文件最后修改的日期（只是一个日期）。
-   `file.tags`：笔记中所有唯一标签的数组。子标签按每个级别细分，因此`#Tag/1/A`将存储在数组中`[#Tag, #Tag/1, #Tag/1/A]`。
-   `file.etags`：注释中所有显式标签的数组；不像`file.tags`, 不包括子标签。
-   `file.inlinks`：指向此文件的所有传入链接的数组。
-   `file.outlinks`：此文件中所有传出链接的数组。
-   `file.aliases`：笔记的所有别名的数组。
-   `file.tasks``- [ ] blah blah blah`：此文件中所有任务（即，）的数组。
-   `file.lists`：文件中所有列表元素的数组（包括任务）；这些元素是有效的任务，可以在任务视图中呈现。
-   `file.frontmatter`：包含所有frontmatter的原始值；主要用于检查原始 frontmatter 值或动态列出 frontmatter 键。

如果文件在其标题（表单`yyyy-mm-dd`或`yyyymmdd`）中有日期，或者有一个`Date`字段/内联字段，它还具有以下属性：

-   `file.day`：与文件关联的明确日期。

如果您使用 Obsidian 默认的“加星标文件”插件，还可以使用以下元数据：

-   `file.starred`：如果此文件已被“星星”黑曜石插件加注星标。

## 4、排序
开头写sort，有升序和降序，分别是为asc和desc。

## 自定义字段
可以通过**fields添加其他数据，无论是在**[每个 YAML Frontmatter 的](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/#frontmatter)文件顶部，还是通过语法在您的内容中间使用[Inline Fields](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/#inline-fields)`[key:: value]`。Dataview将这些数据_编入索引_，以便您查询。

> [!note] 
>  Dataview 索引[某些信息](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/#implicit-fields)，如标签和列表项以及您通过字段添加的数据。Dataview 查询中只有索引数据可用！

例如，文件可能如下所示：

```
---
author: "Edgar Allan Poe" 
published: 1845 
tags: poems
---

# The Raven 
Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore—

``` 
或者像这样：
```
#poems 
# The Raven 
From [author:: Edgar Allan Poe], written in (published:: 1845) Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore—
```


就索引元数据（或您可以查询的内容）而言，它们是相同的，只是注释样式不同。如何[注释元数据](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/)取决于您和您的个人喜好。使用此文件，您将拥有可用的**元数据字段** `author`，并且 Dataview会[自动将所有内容作为隐式字段](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-pages/)提供给您，例如标签或注释标题。

> [!数据需要被索引] 
> 在上面的示例中，您在 Dataview 中_没有_可用的诗歌本身：它是一个段落，没有元数据字段，也没有 Dataview 自动索引。它不是 Dataviews 索引的一部分，因此您将无法查询它。 

````
```dataview 
LIST 
FROM #poems 
WHERE author = "Edgar Allan Poe" 
```
````
上面代码的意思是找出具有标签`#poems`和以值命名的[字段](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/)的所有文件。该查询将从上面找到我们的示例页面。`author``Edgar Allan Poe`


# 官方文档翻译
[[dataview官方文档]]
