
## 一、变量简介
在CSS中，变量（也称为自定义属性）是一种强大的功能，允许我们定义可重用的值，并在整个样式表中多次引用它们。这不仅可以提高代码的可维护性，还可以让样式表的编写更加灵活和高效。
## 二、声明变量
在CSS中声明变量非常简单，使用`--`前缀来定义变量名。变量的声明通常放在`:root`伪类中，这使得变量在全局范围内可用。
### 1. 基本语法
```css
:root {
  --main-color: #333; /* 声明一个颜色变量 */
  --font-size: 16px; /* 声明一个字体大小变量 */
}
```
### 2. 使用变量
使用`var()`函数来引用变量。如果变量未定义，可以提供一个默认值。
```css
body {
  color: var(--main-color); /* 使用颜色变量 */
  font-size: var(--font-size); /* 使用字体大小变量 */
}
```
## 三、变量作用域
CSS变量具有作用域，这意味着它们可以在局部范围内声明并覆盖全局范围内的同名变量。
### 1. 局部变量
```css
.component {
  --component-color: #555; /* 局部变量 */
  background-color: var(--component-color);
}
```
### 2. 全局变量与局部变量
```css
:root {
  --color: blue; /* 全局变量 */
}
div {
  --color: green; /* 局部变量，覆盖全局变量 */
  color: var(--color); /* 使用局部变量 */
}
```
## 四、变量类型
CSS变量可以是任何有效的CSS值，包括字符串、数值、颜色、长度等。
### 1. 字符串
```css
--greeting: "Hello, World!";
```
### 2. 数值
```css
--padding: 10px;
```
### 3. 颜色
```css
--primary-color: #00f;
```
### 4. 长度
```css
--base-font-size: 16px;
```
## 五、变量继承
与普通CSS属性一样，变量也可以继承。如果一个元素没有定义某个变量，它会从其父元素继承该变量。
```css
.parent {
  --text-color: red;
}
.child {
  color: var(--text-color); /* 继承父元素的变量 */
}
```
## 六、变量与calc()结合使用
变量可以与`calc()`函数结合使用，以进行更复杂的计算。
```css
--base-font-size: 16px;
--header-font-size: calc(var(--base-font-size) * 1.5);
```
## 七、浏览器兼容性
大多数现代浏览器都支持CSS变量，但为了确保兼容性，可能需要为旧版浏览器提供回退方案。
```css
body {
  color: #333; /* 回退方案 */
  color: var(--main-color); /* 使用变量 */
}
```
## 八、总结
CSS变量为样式表的编写带来了极大的便利，它们使得代码更加模块化、易于维护。通过合理使用变量，可以减少重复代码，提高开发效率。在构建大型项目时，CSS变量的优势尤为明显。
