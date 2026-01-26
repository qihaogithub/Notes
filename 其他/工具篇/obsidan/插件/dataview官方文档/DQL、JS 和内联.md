将[有用的数据添加到相关页面](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/)后，您会希望实际将其显示在某处或对其进行操作。Dataview 以四种不同的方式实现这一点，所有这些都直接在您的 Markdown 中以代码块的形式编写，并在您的库更改时实时重新加载。

数据视图查询语言 (DQL)
--------------

Dataview[**查询语言**](https://blacksmithgu.github.io/obsidian-dataview/queries/structure)（简称**DQL**）是一种类似 SQL 的语言
它是Dataviews 的核心功能。它支持[四种查询类型](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/)以产生不同的输出，用[数据命令](https://blacksmithgu.github.io/obsidian-dataview/queries/data-commands/)来优化、计算或分组您的结果，并且具备[丰富功能](https://blacksmithgu.github.io/obsidian-dataview/reference/functions/)允许您通过大量操作和调整以实现想要的输出的

您使用用作类型的代码块创建**DQL查询：** `dataview`

````
```dataview
TABLE rating AS "Rating", summary AS "Summary" FROM #games
SORT rating DESC
```
```` 

> [!使用反引号] 
> 有效的代码块需要在开始和结束时使用反引号 (`)（各三个）。不要将反引号与外观相似的撇号（'）混淆


[在查询语言参考](https://blacksmithgu.github.io/obsidian-dataview/queries/structure)下查找如何编写 DQL 查询的说明。如果您通过示例学得更好，请查看[查询示例](https://blacksmithgu.github.io/obsidian-dataview/resources/examples)。

# 内嵌 DQL

内联 DQL 使用内联块格式而不是代码块，通过可配置的前缀来将此内联代码块标记为 DQL 块。

> [!DQL前缀的变化] 
>  您可以在“代码块设置”>“内联查询前缀”下的 Dataviews 设置中将其更改`=`为另一个标记（如`dv:`或）`~`

内联 DQL 查询仅在笔记中间某处显示**一个值**。它们无缝融入您的笔记内容：
```
今天是 `= date(today)` - 距离考试还有`= [[exams]].deadline - date(today)`
```
例如，会输入以下结果
今天是2022年11月7日--距离考试还有2个月零5天！

**内联 DQL**不能查询多个页面。它们始终只显示一个值，而不是值列表（或表格）。您可以通过前缀访问**当前页面**的属性，也可以`this.`通过访问不同的页面`[[linkToPage]]`。
```
`= this.file.name`
`= this.file.mtime` 
`= this.someMetadataField` 
`= [[secondPage]].file.name` 
`= [[secondPage]].file.mtime` 
`= [[secondPage]].someMetadataField`
```
您可以在内联 DQL 查询中使用任何可用的[表达式](https://blacksmithgu.github.io/obsidian-dataview/reference/expressions)和[文字，包括](https://blacksmithgu.github.io/obsidian-dataview/reference/literals)[函数](https://blacksmithgu.github.io/obsidian-dataview/reference/functions)。另一方面，查询类型和数据命令**在内联中不可用。**

```
作业截止日期为 `= this.due - date(today)` 
期末论文截止日期 `= [[Computer Science Theory]].due - date(today)` 
🏃‍♂️ 目标达到了吗？ `= choice(this.steps > 10000, "是的", "**不**，行动起来！")` 
你有`= length(filter(link(dateformat(date(today), "yyyy-MM-dd")).file.tasks, (t) => !t.completed))` 要做的任务`= choice(date(today).weekday > 5, "别紧张!", "该把工作做完了！")`
```
## 数据视图JS

Dataview [JavaScript API](https://blacksmithgu.github.io/obsidian-dataview/api/intro)为您提供 JavaScript 的全部功能，并提供用于提取 Dataview 数据和执行查询的 DSL，允许您创建任意复杂的查询和视图。与查询语言类似，您可以通过`dataviewjs`-annotated 代码块创建 Dataview JS 块：
````
```dataviewjs 
let pages = dv.pages("#books and -#books/finished").where(b => b.rating >= 7); for (let group of pages.groupBy(b => b.genre)) { 
	dv.header(3, group.key); 
	dv.list(group.rows.file.name); } 
```
````

在 JS 数据视图块内，您可以通过变量访问完整的数据视图 API `dv`。有关您可以使用它做什么的解释，请参阅[API 文档](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference)或[API 示例](https://blacksmithgu.github.io/obsidian-dataview/api/code-examples)。

> [!高级用法] 
>  编写 Javascript 查询是一项高级技术，需要了解编程和 JS。请注意 JS 查询可以访问您的文件系统，并且在使用其他人的 JS 查询时要小心，尤其是当它们未通过黑曜石社区公开共享时。

## 内联数据视图 JS

与查询语言类似，您可以编写 JS 内联查询，这样您就可以直接嵌入计算出的 JS 值。您通过内联代码块创建 JS 内联查询：

```
`$= dv.current().file.mtime`
```

在内联 DataviewJS 中，您可以访问`dv`变量，就像在`dataviewjs`代码块中一样，并且可以进行所有相同的调用。结果应该是评估为 JavaScript 值的东西，Dataview 将自动适当地呈现该值。

Unline 内联 DQL 查询，内联 JS 查询确实可以访问 Dataview JS 查询可用的所有内容，因此可以查询和输出多个页面。
> [!内联 JS 前缀的更改] 
>  您可以在“代码块设置”>“Javascript 内联查询前缀”下的 Dataviews 设置中将其更改`$=`为另一个标记（如`dvjs:`或`$~`）

