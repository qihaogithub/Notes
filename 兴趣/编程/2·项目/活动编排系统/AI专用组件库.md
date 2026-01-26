使用代码生成的页面，会使其无法二次编辑，但我需要绘制的不是高保真页面，而是原型图，我能否做一个组件库，通过CDN引入，组件库里放Tldraw风格的基础组件，给AI规则，使其生成代码时只能用Tldraw组件生成，然后绘制好的页面可以以Tldraw 的 `ShapeUtil` 内部使用 `HTMLContainer`展示，后续也可以比较低难度的把代码转为Tldraw组成，因为代码中都是规范的Tldraw基础组件，Tldraw图层类型有对应关系。

这是一个非常精妙且具有高度可行性的架构设计。

你的核心思路是：**利用 Web (HTML/CSS) 强大的布局引擎（Flex/Grid）来弥补 AI 无法处理绝对坐标的短板，同时利用“同构组件”的映射关系，实现从“代码”到“原生 Tldraw 图形”的无损转换。**

这个方案完美解决了“AI 排版难”和“生成后无法深度编辑”的一对矛盾。我们称之为 **“布局烘焙 (Layout Baking)”** 方案。

以下是详细的设计方案：

### 1. 核心思想：先布局，后烘焙

整个流程分为三个阶段：

1.  **AI 布局阶段 (Code Phase)**：AI 生成基于 Flexbox/Grid 的 React 代码（使用特定组件库）。此时组件在 Tldraw 中以 `HTMLContainer` 形式存在，利用浏览器进行自动排版。
2.  **渲染预览阶段 (DOM Phase)**：用户看到渲染好的 UI。此时它是一个整体，内部不可独立选中，但布局是完美的（居中、对齐、自适应）。
3.  **烘焙转换阶段 (Baking Phase)**：**（关键步骤）** 系统遍历这个 `HTMLContainer` 内部的 DOM 树，获取每个元素计算后的真实坐标 (`getBoundingClientRect`)，然后将其“炸开”替换为原生的 Tldraw Shapes。

---

### 2. 步骤一：构建“Tldraw 风格”的原型组件库 (The DSL)

你需要建立一个轻量级的 React 组件库，这套组件库的视觉风格要模仿 Tldraw，且属性要与 Tldraw Shape 的属性一一对应。

**组件库示例 (`@/components/proto-ui`)**：

这些组件本质上是普通的 HTML/CSS，但带有特殊的 `data-attributes` 用于后续转换。

```tsx
// 1. 容器组件 (对应 Tldraw 的 Group 或 Box)
export const ProtoBox = ({ children, layout = 'flex', dir = 'row', align, ...props }) => (
  <div 
    data-proto-type="geo-rect" // 标记转换目标类型
    style={{ 
      display: layout, 
      flexDirection: dir, 
      alignItems: align, 
      border: '2px solid black', // 模拟手绘风格边框
      borderRadius: '2px',
      ...props.style 
    }}
  >
    {children}
  </div>
);

// 2. 按钮组件 (对应 Tldraw 的 Geo Shape + Text)
export const ProtoButton = ({ text }) => (
  <button 
    data-proto-type="geo-button" 
    style={{ border: '2px solid black', padding: '8px 16px', fontFamily: 'Virgil' }}
  >
    <span data-proto-type="text">{text}</span>
  </button>
);

// 3. 占位图组件 (对应 Tldraw 的 Image Shape)
export const ProtoImage = () => (
  <div 
    data-proto-type="geo-image-placeholder"
    style={{ background: '#eee', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
  >
    <svg>...</svg>
  </div>
);
```

---

### 3. 步骤二：AI 生成代码

Prompt 核心逻辑：
> "请使用 `<ProtoBox>`, `<ProtoButton>`, `<ProtoImage>` 组件构建一个登录页。使用 Flexbox 进行布局。不要使用绝对定位。"

AI 生成的代码示例：
```jsx
<ProtoBox dir="column" align="center" style={{ padding: 20, width: 300 }}>
  <ProtoImage style={{ width: 100, height: 100, marginBottom: 20 }} />
  <ProtoBox style={{ marginBottom: 10, width: '100%' }}>
    <ProtoText>用户名</ProtoText>
  </ProtoBox>
  <ProtoButton text="登录" />
</ProtoBox>
```

---

### 4. 步骤三：渲染与“烘焙” (The Baking Algorithm)

这是最核心的技术实现。当用户觉得 AI 生成的预览没问题，点击“**转为可编辑**”时，执行以下逻辑：

#### 4.1 算法流程

1.  **锁定容器**：获取当前 `HTMLContainer` shape 在 Tldraw 画布上的绝对坐标 `(CanvasX, CanvasY)`。
2.  **DOM 遍历**：遍历 `HTMLContainer` 内部的真实 DOM 节点。
3.  **坐标映射**：
    *   对每个带有 `data-proto-type` 的 DOM 节点，调用 `domElement.getBoundingClientRect()`。
    *   计算相对坐标：`ShapeX = DomRect.x - ContainerRect.x + CanvasX`。
    *   计算尺寸：`ShapeW = DomRect.width`。
4.  **生成 Tldraw JSON**：
    *   根据 `data-proto-type` 映射到 Tldraw 的 `type` (如 `geo`, `text`, `arrow`)。
    *   读取 DOM 的计算样式 (Computed Style)，如背景色、字体大小，转换为 Tldraw props。
5.  **替换**：
    *   调用 `editor.createShapes([...newShapes])`。
    *   调用 `editor.deleteShape(htmlContainerId)`。

#### 4.2 代码逻辑示意

```typescript
function bakeProtoToShapes(editor, containerShapeId) {
  // 1. 获取 HTMLContainer 的 DOM 根节点
  const containerElement = document.getElementById(`html-container-${containerShapeId}`);
  if (!containerElement) return;

  const containerRect = containerElement.getBoundingClientRect();
  const { x: shapeX, y: shapeY } = editor.getShapePageBounds(containerShapeId);

  const newShapes = [];

  // 2. 查找所有标记了原型的子元素
  const protoElements = containerElement.querySelectorAll('[data-proto-type]');

  protoElements.forEach(el => {
    const rect = el.getBoundingClientRect();
    const type = el.dataset.protoType; // e.g., 'geo-button'

    // 3. 坐标转换核心公式：
    // 元素在画布的X = (元素在屏幕X - 容器在屏幕X) + 容器在画布X
    const relativeX = rect.left - containerRect.left;
    const relativeY = rect.top - containerRect.top;
    
    // 生成原生 Tldraw Shape 数据
    const tldrawShape = {
      id: createShapeId(),
      type: mapTypeToTldraw(type), // 'geo' or 'text'
      x: shapeX + relativeX,
      y: shapeY + relativeY,
      props: {
        w: rect.width,
        h: rect.height,
        text: el.innerText, // 如果是按钮或文本
        // ... 提取颜色等样式
      }
    };
    
    newShapes.push(tldrawShape);
  });

  // 4. 事务提交：删除旧的，添加新的
  editor.run(() => {
    editor.createShapes(newShapes);
    editor.deleteShape(containerShapeId);
  });
}
```

---

### 5. 方案优势分析

1.  **AI 发挥所长**：AI 不需要计算 `x=120, y=340` 这种它不擅长的数学题，只需要写它最擅长的 `display: flex; justify-content: center`。浏览器引擎帮我们完成了复杂的布局计算。
2.  **所见即所得的转换**：因为“组件库”的视觉样式是模仿 Tldraw 的，所以从 `HTMLContainer` 变为 `Native Shapes` 时，视觉跳变极小，用户体验非常流畅。
3.  **完全原生化**：一旦转换完成，它们就是标准的 Tldraw 矩形和文本。用户可以用 Tldraw 的所有工具（箭头连线、改变颜色、分组）来继续处理。
4.  **支持响应式原型**：在转换之前（HTMLContainer 状态），用户甚至可以拖拽边缘改变宽度，内部内容会自动 Flex 适应！这是纯 Canvas 绘图很难做到的。

### 6. 潜在挑战与解决

*   **挑战**：字体的渲染差异。浏览器渲染的字体宽度可能与 Canvas 渲染的略有不同，导致转换后换行位置改变。
    *   *解决*：在组件库中使用 Tldraw 同款字体（如 Virgil），并留有一定的 padding 余量。
*   **挑战**：层级关系 (Z-Index)。
    *   *解决*：DOM 是自然层级（后出现的在上面）。转换时，按照 DOM 树的遍历顺序生成 Shape，后生成的 Shape 默认就在上面。

### 7. 结论

这个 **“基于 DOM 布局烘焙”** 的方案是目前业界解决 AI 生成可编辑图形的最佳实践之一（类似于 Figma 的 "HTML to Design" 插件原理，但我们是在内部闭环实现）。



