
> 目标：掌握复合选择器作用和写法；使用background属性添加背景效果

## 01-复合选择器

定义：由两个或多个基础选择器，通过不同的方式组合而成。

作用：更准确、更高效的选择目标元素（标签）。

### 后代选择器

后代选择器：**选中某元素的后代元素**。

选择器写法：父选择器  子选择器 { CSS 属性}，父子选择器之间用**空格**隔开。

```html
<style>
  div span {
    color: red;
  }
</style>
<span> span 标签</span>
<div>
  <span>这是 div 的儿子 span</span >
</div>
```

### 子代选择器

子代选择器：选中某元素的子代元素（**最近的子级**）。

选择器写法：父选择器 > 子选择器 { CSS 属性}，父子选择器之间用 **>** 隔开。

```html
<style>
  div > span {
    color: red;
  }
</style>

<div>
  <span>这是 div 里面的 span</span>
  <p>
    <span>这是 div 里面的 p 里面的 span</span>
  </p>
</div>

```

#### 后代选择器和子代选择器区别
后代选择器选择器会选中所有父元素下的所有后代，而子代选择器只选择那些父元素的直接子元素，不包含子元素的子元素
### 并集选择器

并集选择器：选中**多组标签**设置**相同**的样式。

选择器写法：选择器1, 选择器2, …, 选择器N { CSS 属性}，选择器之间用 **,** 隔开。

```html
<style>
  div,
  p,
  span {
    color: red;
  }
</style>

<div> div 标签</div>
<p>p 标签</p>
<span>span 标签</span>
```

### 交集选择器 

交集选择器：选中**同时满足多个条件**的元素。

选择器写法：选择器1选择器2 { CSS 属性}，选择器之间连写，没有任何符号。 

```html
<style>
  p.box {
  color: red;
}
</style>

<p class="box">p 标签，使用了类选择器 box</p>
<p>p 标签</p>
<div class="box">div 标签，使用了类选择器 box</div>
```

> 注意：如果交集选择器中有标签选择器，标签选择器必须书写在最前面。 

### 伪类选择器 

伪类选择器：伪类表示元素**状态**，选中元素的某个状态设置样式。

鼠标悬停状态：**选择器:hover { CSS 属性 }**

```html
<style>
  a:hover {
    color: red;
  }
  .box:hover {
    color: green;
  }
</style>

<a href="#">a 标签</a>
<div class="box">div 标签</div>
```
#### 常用伪类选择器
1. `:hover` - 当鼠标悬停在元素上时应用样式。
2. `:active` - 当元素被激活（通常是点击）时应用样式。
3. `:focus` - 当元素获得焦点时应用样式，例如点击输入框或链接。
4. `:visited` - 用于访问过的链接。
5. `:link` - 用于未访问过的链接。
6. `:first-child` - 选择一个父元素的第一个子元素。
7. `:last-child` - 选择一个父元素的最后一个子元素。
8. `:nth-child(n)` - 选择一个父元素的第n个子元素。
9. `:nth-last-child(n)` - 选择一个父元素倒数第n个子元素。
10. `:first-of-type` - 选择同类型的第一个子元素。
11. `:last-of-type` - 选择同类型的最后一个子元素。
12. `:nth-of-type(n)` - 选择同类型中的第n个元素。
13. `:nth-last-of-type(n)` - 选择同类型中的倒数第n个元素。
14. `:not(selector)` - 排除匹配给定选择器的元素。
15. `:checked` - 用于被选中的radio按钮或checkbox。
16. `:enabled` - 用于启用的表单元素。
17. `:disabled` - 用于禁用的表单元素。
18. `:empty` - 用于没有子元素的元素。
19. `:target` - 用于当前活动的URL片段标识符指向的元素。
20. `:lang(language)` - 用于指定语言的元素。
#### 超链接伪类

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680319272736.png)

> 提示：如果要给超链接设置以上四个状态，需要按 LVHA 的顺序书写。 
>
> 经验：工作中，一个 a 标签选择器设置超链接的样式， hover状态特殊设置 

```css
a {
  color: red;
}

a:hover {
  color: green;
}
```

## 02-CSS特性

CSS特性：化简代码 / 定位问题，并解决问题

* 继承性
* 层叠性
* 优先级

### 继承性

继承性：子级默认继承父级的**文字控制属性**。 

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680319376438.png)

> 注意：如果标签有默认文字样式会继承失败。 例如：a 标签的颜色、标题的字体大小。

### 层叠性

特点：

* 相同的属性会覆盖：**后面的 CSS 属性覆盖前面的 CSS 属性**
* 不同的属性会叠加：**不同的 CSS 属性都生效**

```html
<style>
  div {
    color: red;
    font-weight: 700;
  }
  div {
    color: green;
    font-size: 30px;
  }
</style>

<div>div 标签</div>
```

> 注意：选择器类型相同则遵循层叠性，否则按选择器优先级判断。 

### 优先级

优先级：也叫权重，当一个标签**使用了多种选择器时**，基于不同种类的选择器的**匹配规则**。

```html
<style>
  div {
    color: red;
  }
  .box {
    color: green;
  }
</style>

<div class="box">div 标签</div>
```

#### 基础选择器

规则：选择器**优先级高的样式生效**。

公式：**通配符选择器 < 标签选择器 < 类选择器 < id选择器 < 行内样式 < !important**

​           **（选中标签的范围越大，优先级越低）**

#### 复合选择器-叠加

叠加计算：如果是复合选择器，则需要**权重叠加**计算。

公式：（每一级之间不存在进位）

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680319646205.png)

规则：

* 从左向右依次比较选个数，同一级个数多的优先级高，如果个数相同，则向后比较
* **!important 权重最高**
* 继承权重最低

## 03-Emmet 写法

Emmet写法：代码的**简写**方式，输入缩写 VS Code 会自动生成对应的代码。 

* HTML标签

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680319897697.png)

* CSS：大多数简写方式为属性单词的**首字母** 

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680319926111.png)

## 04-背景属性

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680319971861.png)

### 背景图

网页中，使用背景图实现装饰性的图片效果。

* 属性名：**background-image**（bgi）
* 属性值：url(背景图 URL)

```css
div {
  width: 400px;
  height: 400px;

  background-image: url(./images/1.png);
}
```

> 提示：背景图默认有**平铺（复制）效果**。 

### 平铺方式

属性名：**background-repeat**（bgr） 

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320072292.png)

```css
div {
  width: 400px;
  height: 400px;
  background-color: pink;
  background-image: url(./images/1.png);

  background-repeat: no-repeat;
}
```

### 背景图位置

属性名：**background-position**（bgp）

属性值：水平方向位置 垂直方向位置

* 关键字

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320211424.png)

* 坐标
  * 水平：正数向右；负数向左
  * 垂直：正数向下；负数向上

```css
div {
  width: 400px;
  height: 400px;
  background-color: pink;
  background-image: url(./images/1.png);
  background-repeat: no-repeat;

  background-position: center bottom;
  background-position: 50px -100px;
  background-position: 50px center;
}
```

> 提示：
>
> * 关键字取值方式写法，可以颠倒取值顺序
> * 可以只写一个关键字，另一个方向默认为居中；数字只写一个值表示水平方向，垂直方向为居中

### 背景图缩放

作用：设置背景图大小

属性名：**background-size**（bgz）

常用属性值：

* 关键字
  *  cover：等比例缩放背景图片以完全覆盖背景区，可能背景图片部分看不见
  * contain：等比例缩放背景图片以完全装入背景区，可能背景区部分空白

* 百分比：根据盒子尺寸计算图片大小
* 数字 + 单位（例如：px）

```css
div {
  width: 500px;
  height: 400px;
  background-color: pink;
  background-image: url(./images/1.png);
  background-repeat: no-repeat;
  
  background-size: cover;
  background-size: contain;
}
```

> 提示：工作中，**图片比例与盒子比例相同**，使用 cover 或 contain 缩放背景图效果相同。

### 背景图固定

作用：背景不会随着元素的内容滚动。

属性名：**background-attachment**（bga）

属性值：**fixed**

```css
body {
  background-image: url(./images/bg.jpg);
  background-repeat: no-repeat;
  background-attachment: fixed;
}
```

### 背景复合属性

属性名：**background**（bg）

属性值：背景色 背景图 背景图平铺方式 背景图位置/背景图缩放  背景图固定（**空格隔开各个属性值，不区分顺序**）

```css
div {
  width: 400px;
  height: 400px;

  background: pink url(./images/1.png) no-repeat right center/cover;
}
```

## 05-显示模式

显示模式：标签（元素）的显示方式。 

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320464551.png)

作用：布局网页的时候，根据标签的显示模式选择合适的标签摆放内容。 

### 块级元素

特点：

* 独占一行
* 宽度默认是父级的100%
* 添加宽高属性生效

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320578369.png)

### 行内元素

特点：

* 一行可以显示多个
* 设置宽高属性不生效
* 宽高尺寸由内容撑开

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320583985.png)

### 行内块元素 

特点：

* 一行可以显示多个
* 设置宽高属性生效
* 宽高尺寸也可以由内容撑开

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320590005.png)

### 转换显示模式

##### 属性 ：**display**

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320613034.png)

## CSS变量
在CSS中，`var(--name, value)` 是一个CSS自定义属性（也称为CSS变量）的语法，用于定义一个变量并给它赋一个默认值。这种语法允许您在不同的场合使用同一个变量，并在需要的时候覆盖它的值。

具体来说，`border-radius: var(--name, 4px);` 这行代码的意思是：

- `--name` 是自定义属性的名称，您可以根据需要给它起一个有意义的名字。在实际使用中，您应该替换 `--name` 为一个具体的变量名，例如 `--my-border-radius`。
- `4px` 是这个变量的默认值。如果在其他地方没有为这个变量指定一个值，那么它将使用这个默认值。

使用CSS变量的一个好处是，您可以在CSS的其他地方或者在HTML中通过内联样式来设置这个变量的值，并且当您更改变量的值时，所有使用了这个变量的地方都会自动更新。

例如，您可以在CSS中这样定义和使用变量：

```css
:root {
  --my-border-radius: 8px; /* 定义变量并设置默认值 */
}

.element {
  border-radius: var(--my-border-radius); /* 使用变量 */
}

/* 然后在另一个地方，您可以覆盖这个变量的值 */
.element特殊情况 {
  --my-border-radius: 12px; /* 覆盖变量的值 */
}
```

在这个例子中，所有使用 `.element` 类的元素都会有一个8像素的边框圆角。但是对于使用 `.element特殊情况` 类的元素，边框圆角将被覆盖为12像素，因为这里为 `--my-border-radius` 变量指定了一个新的值。

请注意，CSS变量的名称必须以两个破折号（`--`）开头，这是它们的标识符。在实际开发中，为了避免命名冲突，通常建议使用有特定前缀的变量名，例如 `--app-theme-color`。

### :root
`:root` 是一个CSS伪类，它匹配文档树的根元素。在HTML文档中，`:root` 几乎总是对应于 `<html>` 标签。`:root` 伪类非常有用，因为它允许我们在文档的最顶层定义CSS变量（自定义属性），这些变量可以在整个文档中使用。

在CSS中，使用 `:root` 来定义全局CSS变量是一种常见的做法。这些变量可以被文档中的任何元素继承，除非在更具体的元素上明确地覆盖了它们。这样做的好处是提供了一个集中的地方来定义和管理全局样式，使得样式更容易维护和重用。

例如：

```css
:root {
  --my-border-radius: 8px; /* 定义全局CSS变量 */
  --my-text-color: #333; /* 定义另一个全局CSS变量 */
}

.element {
  border-radius: var(--my-border-radius); /* 使用全局CSS变量 */
  color: var(--my-text-color); /* 使用另一个全局CSS变量 */
}
```

在这个例子中，我们在 `:root` 上定义了两个CSS变量：`--my-border-radius` 和 `--my-text-color`。这些变量可以在文档中的任何地方使用，通过 `var(--变量名)` 的形式来引用。`.element` 类使用了这些变量来设置元素的边框圆角和文本颜色。

`:root` 并不是CSS变量的固定写法，但在大多数情况下，它是定义全局CSS变量的首选位置。当然，CSS变量也可以在其他选择器中定义，但它们的继承和作用域规则会有所不同。

## 06-综合案例一-热词

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320664821.png)

### HTML标签

```html
<a href="#">HTML</a>
<a href="#">CSS</a>
<a href="#">JavaScript</a>
<a href="#">Vue</a>
<a href="#">React</a>
```

### CSS样式

```html
<style>
/* 默认效果 */
a {
display: block;
width: 200px;
height: 80px;
background-color: #3064bb;
color: #fff;
text-decoration: none;
text-align: center;
line-height: 80px;
font-size: 18px;
}

/* 鼠标悬停的效果 */
a:hover {
background-color: #608dd9;
}
</style>
```

## 07-综合案例二 – banner 效果 

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1680320758496.png)

### HTML标签

```html
<div class="banner">
  <h2>让创造产生价值</h2>
  <p>我们希望小游戏平台可以提供无限的可能性，让每一个创作者都可以将他们的才华和创意传递给用户。</p>
  <a href="#">我要报名</a>
</div>
```



### CSS样式

```html
<style>
  .banner {
    height: 500px;
    background-color: #f3f3f4;
    background-image: url(./images/bk.png);
    background-repeat: no-repeat;
    background-position: left bottom;

    /* 文字控制属性，继承给子级 */
    text-align: right;
    color: #333;
  }

  .banner h2 {
    font-size: 36px;
    font-weight: 400;
    line-height: 100px;
  }

  .banner p {
    font-size: 20px;
  }

  .banner a {
    width: 125px;
    height: 40px;
    background-color: #f06b1f;

    display: inline-block;
    /* 转块级无法右对齐，因为块元素独占一行 */
    /* display: block; */

    text-align: center;
    line-height: 40px;
    color: #fff;
    text-decoration: none;
    font-size: 20px;
  }
</style>
```

