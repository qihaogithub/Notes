---
介绍: 允许用户设置自定义正则表达式规则以自动设置注释的格式。
评级: "0"
---
# 去除空行
安装Regex Pipeline插件
command+p，运行插件
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20221031100840.png)
添加正则表达式：
```
"^\s*$\n"gm->"empty"x  
" +$"gm->"empty"x
```
运行即可去除空格和结尾空行

## 书写规则
```
"要搜索的内容"gmu->"要替换的内容"
```

## 教程文章
[Regex Pipeline guideline.md · GitHub](https://gist.github.com/No3371/f1750b178376f0659df6650ccaf57c12)