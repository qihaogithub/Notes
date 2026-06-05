

## 1. 问题概述

  

当前同一份 Figma 设计稿分别导出为 HTML 和 React/TSX 后，图片节点在画面中的位置不一致。

  

具体表现：

  

* HTML 版本中，图片位于画面中间靠上的位置，符合 Figma 原始设计。

* React/TSX 版本中，图片出现在画面左上角，位置明显错误。

* 两个版本使用的是同一张图片资源，图片尺寸一致，但布局位置不一致。

  

因此问题不是图片资源本身，也不是图片加载失败，而是 React/TSX 导出时丢失了 Figma 节点的定位信息。

  

---

  

## 2. 复现文件

  

相关文件：

  

```txt

figma-export2.html

figma-export2.tsx

```

  

设计画布尺寸：

  

```txt

375px × 812px

```

  

图片尺寸：

  

```txt

161px × 161px

```

  

Figma 父节点：

  

```txt

id: 223:1562

type: FRAME

name: Frame 48097196

width: 375

height: 812

layoutMode: NONE

clipsContent: true

```

  

Figma 图片节点：

  

```txt

id: 223:1564

type: RECTANGLE

name: #slot:img:图片

isAsset: true

width: 161

height: 161

x: 107

y: 280

```

  

---

  

## 3. HTML 导出结果

  

HTML 版本中的图片节点包含完整定位信息：

  

```html

<img

style="width: 161px; height: 161px; left: 107px; top: 280px; position: absolute"

src="https://r2-asset-worker.qihaogo.workers.dev/figma/h_85212ab6.png"

/>

```

  

父容器是相对定位：

  

```html

<div style="width: 375px; height: 812px; position: relative; background: white; overflow: hidden">

```

  

所以 HTML 中图片实际布局为：

  

```txt

父容器：

position: relative

width: 375px

height: 812px

  

子图片：

position: absolute

left: 107px

top: 280px

width: 161px

height: 161px

```

  

因此 HTML 预览位置正确。

  

---

  

## 4. React/TSX 导出结果

  

React/TSX 版本中的图片节点目前是：

  

```tsx

<img

id="图片"

data-figma-id="223:1564"

style={{ width: 161, height: 161 }}

src={field}

alt="图片"

/>

```

  

这里仅保留了：

  

```txt

width: 161

height: 161

```

  

但丢失了：

  

```txt

position: absolute

left: 107

top: 280

```

  

由于 React 中的 `<img>` 没有绝对定位，它会按照普通文档流渲染，因此默认出现在父容器左上角。

  

这就是 React 预览图片位置错误的直接原因。

  

---

  

## 5. Figma 节点数据证明

  

这次额外导出的 Figma 节点数据中，已经可以明确看到图片节点本身有正确的位置和尺寸信息。

  

图片节点数据如下：

  

```json

{

"id": "223:1564",

"type": "RECTANGLE",

"name": "#slot:img:图片",

"isAsset": true,

"relativeTransform": [

[1, 0, 107],

[0, 1, 280]

],

"absoluteTransform": [

[1, 0, 3439],

[0, 1, 1520]

],

"x": 107,

"y": 280,

"width": 161,

"height": 161,

"absoluteBoundingBox": {

"x": 3439,

"y": 1520,

"width": 161,

"height": 161

}

}

```

  

从这段数据可以确认：

  

```txt

图片节点相对父级的位置：

x = 107

y = 280

  

图片节点尺寸：

width = 161

height = 161

```

  

也就是说，Figma 节点数据中并没有丢失坐标。

  

问题不是 Figma 原始数据缺少位置，而是 TSX 导出阶段没有把这些坐标写入 React 节点样式。

  

---

  

## 6. 父子节点坐标关系

  

父级 Frame 数据：

  

```json

{

"id": "223:1562",

"type": "FRAME",

"x": 3332,

"y": 1240,

"width": 375,

"height": 812,

"absoluteBoundingBox": {

"x": 3332,

"y": 1240,

"width": 375,

"height": 812

}

}

```

  

子图片节点数据：

  

```json

{

"id": "223:1564",

"type": "RECTANGLE",

"x": 107,

"y": 280,

"width": 161,

"height": 161,

"absoluteBoundingBox": {

"x": 3439,

"y": 1520,

"width": 161,

"height": 161

}

}

```

  

根据 absoluteBoundingBox 也可以计算出相对位置：

  

```txt

left = child.absoluteBoundingBox.x - parent.absoluteBoundingBox.x

= 3439 - 3332

= 107

  

top = child.absoluteBoundingBox.y - parent.absoluteBoundingBox.y

= 1520 - 1240

= 280

```

  

这与 Figma 节点上的 `x: 107`、`y: 280` 完全一致，也与 HTML 导出的 `left: 107px; top: 280px` 完全一致。

  

因此 React/TSX 导出时应该使用：

  

```txt

left: 107

top: 280

width: 161

height: 161

position: absolute

```

  

---

  

## 7. 需要注意：不要误用 inferredAutoLayout

  

父级 Frame 节点中有一段 `inferredAutoLayout`：

  

```json

"inferredAutoLayout": {

"layoutMode": "VERTICAL",

"paddingLeft": 107,

"paddingRight": 107,

"paddingTop": 280,

"paddingBottom": 371,

"counterAxisSizingMode": "FIXED",

"primaryAxisSizingMode": "FIXED",

"primaryAxisAlignItems": "MIN",

"counterAxisAlignItems": "CENTER",

"layoutAlign": "MIN",

"layoutGrow": 0,

"itemSpacing": 0,

"layoutPositioning": "AUTO"

}

```

  

但父级真实 layoutMode 是：

  

```txt

layoutMode: NONE

```

  

这说明该 Frame 并不是真正的 Auto Layout 容器。

  

因此 TSX 导出时不应该基于 `inferredAutoLayout` 把子节点当作普通流式布局处理。

  

正确逻辑应该是：

  

```txt

如果父级 layoutMode === "NONE"，子节点应按 Figma 坐标进行绝对定位。

```

  

也就是：

  

```tsx

position: 'absolute',

left: node.x,

top: node.y,

width: node.width,

height: node.height

```

  

或通过 absoluteBoundingBox 差值计算：

  

```txt

left = child.absoluteBoundingBox.x - parent.absoluteBoundingBox.x

top = child.absoluteBoundingBox.y - parent.absoluteBoundingBox.y

```

  

---

  

## 8. 根因判断

  

当前问题大概率出在 TSX 生成器的布局样式转换逻辑中。

  

HTML 导出器已经正确输出了 Figma 节点的几何信息：

  

```txt

position

left

top

width

height

```

  

但 TSX 导出器只输出了：

  

```txt

width

height

```

  

导致 React 预览无法还原 Figma 中的节点坐标。

  

这属于 HTML 导出和 TSX 导出的布局属性不一致问题。

  

---

  

## 9. 期望修复结果

  

React/TSX 版本中的图片节点应该补齐绝对定位信息。

  

期望结果如下：

  

```tsx

<img

id="图片"

data-figma-id="223:1564"

style={{

width: 161,

height: 161,

position: 'absolute',

left: 107,

top: 280,

}}

src={field}

alt="图片"

/>

```

  

完整组件可参考：

  

```tsx

import React from 'react';

  

interface Props {

// @title 图片 @format uri @widget image-upload @group Frame 48097196 @order 10 @viewport 375x812 @default https://r2-asset-worker.qihaogo.workers.dev/figma/h_85212ab6.png

field: string;

}

  

export default function Frame48097196({ field }: Props) {

return (

<div

className="w-[375px] h-[812px] relative bg-[#ffffff] overflow-hidden"

data-figma-id="223:1562"

>

<img

id="图片"

data-figma-id="223:1564"

style={{

width: 161,

height: 161,

position: 'absolute',

left: 107,

top: 280,

}}

src={field}

alt="图片"

/>

</div>

);

}

```

  

---

  

## 10. 建议修复方向

  

请检查 Figma 到 React/TSX 的导出逻辑，尤其是子节点样式生成部分。

  

当父级 Frame 是普通 Frame，也就是：

  

```txt

layoutMode: NONE

```

  

并且子节点在 Figma 中有明确坐标时，TSX 应该输出完整布局样式：

  

```txt

position: absolute

left

top

width

height

```

  

不要只输出：

  

```txt

width

height

```

  

否则 React 会把节点当作普通文档流元素渲染，从而默认出现在左上角。

  

---

  

## 11. 建议的坐标生成规则

  

建议在 TSX 导出器中增加如下规则：

  

### 11.1 父级为普通 Frame

  

当父级满足：

  

```txt

parent.type === "FRAME"

parent.layoutMode === "NONE"

```

  

子节点应该使用绝对定位：

  

```tsx

style={{

position: 'absolute',

left: child.x,

top: child.y,

width: child.width,

height: child.height,

}}

```

  

如果 `child.x` / `child.y` 不可靠，则使用：

  

```txt

left = child.absoluteBoundingBox.x - parent.absoluteBoundingBox.x

top = child.absoluteBoundingBox.y - parent.absoluteBoundingBox.y

```

  

### 11.2 子节点为图片资源

  

当前图片节点在 Figma 中是：

  

```txt

type: RECTANGLE

name: #slot:img:图片

fills[0].type: IMAGE

isAsset: true

```

  

虽然最终导出成 React `<img>`，但它在布局上仍然是 Figma 里的一个子节点，不能因为转换成 `<img>` 就丢失坐标。

  

因此图片资源节点也应该保留：

  

```txt

position

left

top

width

height

```

  

### 11.3 不要因为 layoutPositioning 为 AUTO 就跳过坐标

  

当前子节点中有：

  

```txt

layoutPositioning: AUTO

```

  

但父级 Frame 的：

  

```txt

layoutMode: NONE

```

  

所以该节点仍然应该按普通 Frame 下的绝对坐标处理。

  

不能仅凭 `layoutPositioning: AUTO` 就把它当作流式布局节点。

  

---

  

## 12. 需要重点检查的代码位置

  

建议重点排查以下逻辑：

  

### 12.1 TSX 子节点 style 生成逻辑

  

检查是否存在类似逻辑：

  

```txt

img 节点只输出 width / height

```

  

如果有，需要补充 position / left / top。

  

### 12.2 图片节点特殊处理逻辑

  

当前 Figma 图片实际是：

  

```txt

RECTANGLE + IMAGE fill

```

  

导出 React 时被转换成：

  

```tsx

<img />

```

  

这一步转换可能只处理了图片地址和尺寸，没有继承原 Rectangle 的布局样式。

  

需要确保转换后：

  

```txt

原 Rectangle 的布局属性仍然进入 img style

```

  

### 12.3 Auto Layout 推断逻辑

  

父级节点有 `inferredAutoLayout`，但真实 `layoutMode` 是 `NONE`。

  

如果当前 TSX 生成器使用了 `inferredAutoLayout` 去生成普通流式布局，可能会导致子节点不加绝对定位。

  

建议优先以真实字段为准：

  

```txt

layoutMode

```

  

而不是：

  

```txt

inferredAutoLayout

```

  

---

  

## 13. 验收标准

  

修复后需要满足：

  

1. HTML 预览和 React/TSX 预览中的图片位置一致。

2. 图片在 375×812 画布中位于：

  

```txt

left: 107px

top: 280px

```

  

3. 图片尺寸保持：

  

```txt

width: 161px

height: 161px

```

  

4. React 版本中图片不再默认出现在左上角。

5. 对于父级 `layoutMode: NONE` 的 Figma Frame，子节点都应按照 Figma 坐标进行绝对定位。

6. 对于 `RECTANGLE + IMAGE fill` 转换成 `<img>` 的节点，也必须保留原始布局坐标。

7. 不应因为 `inferredAutoLayout` 或 `layoutPositioning: AUTO` 误判为普通文档流布局。

  

---

  

## 14. 结论

  

当前 bug 的核心是：

  

```txt

React/TSX 导出结果丢失了 Figma 子节点的 position / left / top 定位信息。

```

  

Figma 节点数据中已经明确存在：

  

```txt

x: 107

y: 280

width: 161

height: 161

```

  

HTML 导出也已经正确使用了：

  

```txt

position: absolute

left: 107px

top: 280px

width: 161px

height: 161px

```

  

但 TSX 导出只保留了：

  

```txt

width: 161

height: 161

```

  

所以 React 预览中图片会回到左上角。

  

请将 TSX 导出逻辑与 HTML 导出逻辑保持一致：在父级 `layoutMode: NONE` 的普通 Frame 中，子节点需要按照 Figma 原始坐标输出绝对定位样式。