---
介绍: 任务管理
评级: "4"
---
[官方用户指南](https://publish.obsidian.md/tasks/Getting+Started/Global+Filter)
[【效率办公】Obsidain插件之Tasks-任务管理利器 - 哔哩哔哩](https://www.bilibili.com/read/cv14259903)

# 语法
### 日期格式 :
2021-11-23 或 2022-05-01
Today、 tomorrow、 in three weeks、 Last Monday、 next Friday 、after -3 week、before in two weeks

### 截止日期：
截止：due before/after/on {日期}
无截止日期：no due date

### 特定任务
最多显示 50 个任务
limit 50
仅在特定标题下显示任务
heading includes Task
从特定路径中排除任务
path regex does not match {路径}
过期任务
Due before Today

### 完成或未完成 ：
Done 或 not done
Done before/after/on 日期
### 路径：（路径和关键字不用加引号） 
包含路径：path includes 
路径不包含：path does not include 
路径多条路径要分开写
### 任务内容
包含内容：description includes 关键宇
不包含内容：description does not include 关键字
### 标题 (任务项前面最近的＃标题）：
包含标题：heading includes 关键字
不包含标题：heading does not include 关键字（带有该标题的文件中所有任务都不包含）
### 隐藏相关样式 
短模式：Short mode  (时间和链接等会显示为图标)
隐藏编辑按钮：hide edit button 
隐藏链接：hide backlink
隐藏完成日期：hide done date 
隐藏执行日期：hide scheduled date 
隐藏截止日期：hide due date 
隐藏循环规则：hide recurrence rule 
隐藏任务数理：hide task count 
隐藏优先级：hide priority





![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230414214715.png)

### 示例
> 三个点后面要加 tasks 才会生效

```
not done
due today
sort by due
```

```
done
sort by priority reverse
```

```
not done
due before next monday
sort by status
sort by description reverse
sort by path
```

```
no due date
path includes GitHub
hide recurrence rule
hide task count
hide backlink
```

```
not done
heading includes OB插件
hide backlink
exclude sub-items
short mode
limit 2
sort by priority
```


未完成任务

````
```tasks
short mode
not done
has due date
hide start date
hide created date 
sort by path
```
````

没有完成时间的任务
```tasks
short mode
not done
no due date
sort by path
sort by due
path includes 4·工作
```
近一个月完成任务
```tasks
short mode
done after -4week
hide start date
hide created date 
hide due date
hide done date 
sort by done
path includes 4·工作

```