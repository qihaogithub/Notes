

## 一、容器属性（Container）

### 1. 启用flex布局
```css
.container {
  display: flex;  /* 块级容器 */
  /* 或 */
  display: inline-flex;  /* 行内容器 */
}
```

### 2. 主轴方向 (flex-direction)
```css
.container {
  flex-direction: row;            /* 默认值：从左到右 */
  flex-direction: row-reverse;    /* 从右到左 */
  flex-direction: column;         /* 从上到下 */
  flex-direction: column-reverse; /* 从下到上 */
}
```

### 3. 换行方式 (flex-wrap)
```css
.container {
  flex-wrap: nowrap;       /* 默认值：不换行 */
  flex-wrap: wrap;         /* 换行 */
  flex-wrap: wrap-reverse; /* 换行并反转 */
}
```

### 4. 主轴对齐方式 (justify-content)
```css
.container {
  justify-content: flex-start;    /* 默认值：左对齐 */
  justify-content: flex-end;      /* 右对齐 */
  justify-content: center;        /* 居中对齐 */
  justify-content: space-between; /* 两端对齐 */
  justify-content: space-around;  /* 项目两侧间隔相等 */
  justify-content: space-evenly;  /* 项目间隔完全相等 */
}
```

### 5. 交叉轴对齐方式 (align-items)
```css
.container {
  align-items: flex-start; /* 顶部对齐 */
  align-items: flex-end;   /* 底部对齐 */
  align-items: center;     /* 居中对齐 */
  align-items: stretch;    /* 默认值：如果项目未设置高度，将占满整个容器的高度 */
  align-items: baseline;   /* 项目的第一行文字的基线对齐 */
}
```

### 6. 多行对齐方式 (align-content)
```css
.container {
  align-content: flex-start;    /* 顶部堆叠 */
  align-content: flex-end;      /* 底部堆叠 */
  align-content: center;        /* 中间堆叠 */
  align-content: space-between; /* 两端堆叠 */
  align-content: space-around;  /* 每行间隔相等 */
  align-content: stretch;       /* 默认值：拉伸占满 */
}
```

## 二、项目属性（Items）

### 1. 排序 (order)
```css
.item {
  order: 0;  /* 默认值 */
  order: 1;  /* 数值越大，排列越靠后 */
  order: -1; /* 数值越小，排列越靠前 */
}
```

### 2. 弹性增长 (flex-grow)
```css
.item {
  flex-grow: 0;  /* 默认值：不放大 */
  flex-grow: 1;  /* 放大比例为1 */
  flex-grow: 2;  /* 放大比例为2 */
}
```

### 3. 弹性收缩 (flex-shrink)
```css
.item {
  flex-shrink: 1;  /* 默认值：等比例收缩 */
  flex-shrink: 0;  /* 不收缩 */
  flex-shrink: 2;  /* 收缩比例为2 */
}
```

### 4. 基准大小 (flex-basis)
```css
.item {
  flex-basis: auto;   /* 默认值：项目本来的大小 */
  flex-basis: 0;      /* 项目将根据flex-grow的值进行分配 */
  flex-basis: 200px;  /* 指定固定大小 */
}
```

### 5. flex简写属性
```css
.item {
  flex: none;         /* 0 0 auto */
  flex: auto;         /* 1 1 auto */
  flex: 1;            /* 1 1 0% */
  flex: 0 0 200px;    /* grow shrink basis */
}
```

### 6. 单个项目对齐方式 (align-self)
```css
.item {
  align-self: auto;       /* 默认值：继承父元素的align-items属性 */
  align-self: flex-start; /* 顶部对齐 */
  align-self: flex-end;   /* 底部对齐 */
  align-self: center;     /* 居中对齐 */
  align-self: stretch;    /* 拉伸对齐 */
  align-self: baseline;   /* 基线对齐 */
}
```

## 三、常用布局示例

### 1. 水平垂直居中
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```
### 从上到下排列，并且左右居中
```css
.container {
  display: flex; /* 启用Flex布局 */
  flex-direction: column; /* 设置主轴方向为垂直 */
  align-items: center; /* 设置交叉轴的对齐方式为居中 */
  justify-content: center; /* 设置主轴的对齐方式为居中 */
  height: 100%; /* 确保父容器有足够的高度 */
}
```

### 2. 两端对齐，中间自适应
```css
.container {
  display: flex;
}
.side {
  flex: 0 0 200px;
}
.main {
  flex: 1;
}
```

### 3. 等分布局
```css
.container {
  display: flex;
}
.item {
  flex: 1;
}
```

### 4. 圣杯布局
```css
.container {
  display: flex;
}
.center {
  flex: 1;
  order: 2;
}
.left {
  flex: 0 0 200px;
  order: 1;
}
.right {
  flex: 0 0 200px;
  order: 3;
}
```

## 四、注意事项

1. 设置了`flex`布局的元素，子元素的`float`、`clear`、`vertical-align`属性将失效

2. 使用`flex-grow`时，如果所有项目的`flex-grow`之和小于1，则按比例分配剩余空间

3. 使用`flex-basis`和`width`同时存在时，`flex-basis`优先级更高

4. 常用的`flex`简写值：
   - `flex: 1` = `flex: 1 1 0%`
   - `flex: auto` = `flex: 1 1 auto`
   - `flex: none` = `flex: 0 0 auto`

5. 性能优化：
   - 避免频繁改变flex相关属性
   - 使用`transform`代替改变flex值来实现动画
   - 合理使用`flex-wrap`避免不必要的重排