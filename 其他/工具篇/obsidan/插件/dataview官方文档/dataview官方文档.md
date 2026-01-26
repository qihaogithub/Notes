https://blacksmithgu.github.io/obsidian-dataview/

[[其他/工具篇/obsidan/插件/dataview官方文档/概述]]
[[元数据]]
[[其他/工具篇/obsidan/插件/dataview官方文档/DQL、JS 和内联]]
查询语言
	[[其他/工具篇/obsidan/插件/dataview官方文档/查询的结构]]
	[[其他/工具篇/obsidan/插件/dataview官方文档/数据命令]]
JavaScript 参考
常见问题解答和资源
数据视图之友
变更日志


[[其他/工具篇/obsidan/插件/dataview官方文档/翻译文档·知乎]]
# 例子

查找未完成任务
````
```dataview
task
WHERE !completed
```
````

未完成并截止时间为空
````
```dataview
list
from "4·工作/2·待办/任务文档"
WHERE 状态 = false AND 截止时间 = ""
```
````


[知乎·Obsidian DataView 入门保姆级引导手册](https://zhuanlan.zhihu.com/p/614881764)