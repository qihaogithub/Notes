Deck: JavaScript

## 单词
START
单词
Selector
语音: 
音标: 
释义: 
笔记: 
Tags:
<!--ID: 1701252552824-->
END

START
单词
Element
语音: 
音标: 
释义: 
笔记: 
Tags:
<!--ID: 1701252552829-->
END


START
单词
Inner
语音: 
音标: 
释义: 
笔记: 
<!--ID: 1701240022833-->
END

START
单词
Splice
语音: 
音标: 
释义: 
方法用于添加或删除数组中的元素。
笔记
[[Splice ()]] 
<!--ID: 1701239040106-->
END

## Web APIs 基础

START
Basic
console. Log 
Back: 
`console.log` 是 JavaScript 中用于在控制台输出信息的函数。它可以用来打印文本、变量、表达式的值或任何需要输出的内容。
Tags:  
<!--ID: 1741014631369-->
END


START
KaTeX and Markdown Basic
什么是 DOM
Back: 
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20231124154716.png)
<!--ID: 1701252648804-->
END


## 获取 DOM 对象
START
KaTeX and Markdown Basic
QuerySelector 和 QuerySelectorAll 的区别
Back: 
1. QuerySelector   满足条件的第一个元素
2. QuerySelectorAll  满足条件的元素集合返回伪数组
<!--ID: 1701252648811-->
END

START
KaTeX and Markdown Basic
获取 DOM 对象的方法
Back: 
 QuerySelector   满足条件的第一个元素
QuerySelectorAll  满足条件的元素集合返回伪数组
GetElementById  专门获取元素类型节点，根据标签的 `id`  属性查找
GetElementsByTagName
<!--ID: 1701252648815-->
END


## 操作元素内容



START
KaTeX and Markdown Basic
操作元素内容的方法有哪些
Back: 
`innerHTML` 将文本内容添加/更新到任意标签位置，**文本中包含的标签会被解析。**
`innerText` 将文本内容添加/更新到任意标签位置，**文本中包含的标签不会被解析。**
<!--ID: 1701252648818-->
END

START
KaTeX and Markdown Basic
InnerHTML
Back: 
`innerHTML` 将文本内容添加/更新到任意标签位置，**文本中包含的标签会被解析。**
如果文本内容中包含 `html` 标签时推荐使用 `innerHTML`，否则建议使用 `innerText` 属性。
<!--ID: 1701252648823-->
END

START
KaTeX and Markdown Basic
innerText
Back: 
`innerText` 将文本内容添加/更新到任意标签位置，**文本中包含的标签不会被解析。**
<!--ID: 1701252648828-->
END


## 操作元素属性

操作元素属性的方法有哪些





## 事件监听


START
KaTeX and Markdown Basic
事件监听
Back: 
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20231129173501.png)
举例：
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20231129173651.png)
注意：
1. 事件类型要加引号
2. 函数是点击之后再去执行，每次点击都会执行一次
<!--ID: 1701252648832-->
END

## 事件类型

START
KaTeX and Markdown Basic
事件类型
Back: 
鼠标单击 click、鼠标经过 mouseover 等
`click` 译成中文是【点击】的意思，它的含义是监听（等着）用户鼠标的单击操作，除了【单击】还有【双击】 `dblclick`  
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20231129182251.png)
【事件类型】决定了事件被触发的方式，如 `click` 代表鼠标单击，`dblclick` 代表鼠标双击。
<!--ID: 1701252920512-->
END



START
KaTeX and Markdown Basic
鼠标事件
Back: 
鼠标事件是指跟鼠标操作相关的事件，如单击、双击、移动等。
1. `mouseenter 监听鼠标是否移入 DOM 元素
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20231129182805.png)

1. `mouseleave 监听鼠标是否移出 DOM 元素
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20231129182754.png)
<!--ID: 1701252648840-->
END




