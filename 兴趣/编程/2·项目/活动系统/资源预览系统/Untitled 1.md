对 [01-AI_Demo生成系统.md](file:///Users/qh2/Documents/我的文件/编程/1·工作/Ai活动系统/docs/需求文档/01-AI_Demo生成系统.md) 文档的所有优化建议：

---

## 优化建议总结

### 一、第8章"系统集成"内容扩充

**现状**：只有一句话"提供可配置 Demo 调用接口，其他业务页面通过组件形式引入可配置 Demo 模块"

**建议补充完整内容**：

#### 8.1 预览组件调用接口

**采用 Shadow DOM + CSS-in-JS 方案**：

```tsx
// 组件嵌入方式
<DemoPreview
  demoId="demo-001"
  config={configData}
  mode="preview"
  onConfigChange={(newConfig) => console.log(newConfig)}
  onElementClick={(resourceId) => console.log('Element clicked:', resourceId)}
/>
```

**接口参数定义**：

| 参数名         | 类型                | 必填 | 说明                         |
| -------------- | ------------------- | ---- | ---------------------------- |
| demoId         | string              | 是   | Demo 唯一标识                |
| config         | object              | 是   | 配置数据（符合 Schema）      |
| mode           | 'preview' \| 'edit' | 否   | 预览/编辑模式，默认 preview  |
| onConfigChange | function            | 否   | 配置变更回调                 |
| onElementClick | function            | 否   | 元素点击回调（用于联动高亮） |
| readonly       | boolean             | 否   | 是否只读，默认 false         |

#### 8.2 REST API 接口

**获取 Demo 模板**：
```
GET /api/demos/:id
Response: {
  id: string,
  name: string,
  code: string,
  schema: object,
  previewImage: string
}
```

**获取 Demo 列表**：
```
GET /api/demos
Response: {
  demos: Array<{
    id: string,
    name: string,
    category: string,
    createdAt: string
  }>
}
```

#### 8.3 与设计规范 CMS 的集成

**预览组件嵌入规范**：

```json
{
  "type": "demo-preview",
  "demoId": "demo-001",
  "defaultConfig": {
    "images": {
      "banner": "/resources/default-banner.png"
    },
    "texts": {
      "title": "默认标题"
    }
  },
  "allowOverride": true
}
```

**资源联动高亮机制**：

```tsx
// 设计规范CMS - 父组件
function DesignSpecCMS() {
  const [selectedResource, setSelectedResource] = useState(null);
  const demoPreviewRef = useRef(null);

  // 点击资源卡片，高亮 Demo 对应元素
  const handleResourceClick = (resource) => {
    setSelectedResource(resource);
    demoPreviewRef.current?.highlightElement(resource.id);
  };

  // Demo 元素被点击，高亮对应资源卡片
  const handleElementClick = (resourceId) => {
    setSelectedResource(resourceId);
  };

  return (
    <div className="cms-container">
      <div className="resource-list">
        {resources.map(resource => (
          <div 
            key={resource.id}
            className={`resource-card ${selectedResource === resource.id ? 'active' : ''}`}
            onClick={() => handleResourceClick(resource)}
          >
            {resource.name}
          </div>
        ))}
      </div>
      
      <DemoPreview
        ref={demoPreviewRef}
        demoId="demo-001"
        config={configData}
        onElementClick={handleElementClick}
      />
    </div>
  );
}
```

**资源校验集成**：

```typescript
import { validateResource } from '@scope/demo-sdk';

const result = await validateResource({
  type: 'image',
  file: uploadedFile,
  rules: {
    maxWidth: 750,
    maxSize: 500 * 1024,
    formats: ['jpg', 'png', 'webp']
  }
});
```

#### 8.4 与活动管理系统的集成

**页面详情页集成示例**：

```tsx
function PageDetail({ page }) {
  const demoPreviewRef = useRef(null);

  return (
    <div className="page-detail">
      <DemoPreview
        ref={demoPreviewRef}
        demoId={page.demoTemplateId}
        config={page.config}
        mode="edit"
        onConfigChange={handleConfigChange}
        onElementClick={handleElementClick}
      />
      <ExportButton onClick={exportConfig} />
    </div>
  );
}
```

#### 8.5 Shadow DOM 实现说明

**样式隔离机制**：

```tsx
// DemoPreview 组件内部实现
function DemoPreview({ demoId, config, onElementClick, forwardedRef }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const shadowRootRef = useRef<ShadowRoot | null>(null);

  useEffect(() => {
    if (containerRef.current) {
      // 创建 Shadow DOM
      const shadowRoot = containerRef.current.attachShadow({ mode: 'open' });
      shadowRootRef.current = shadowRoot;

      // 注入样式（完全隔离）
      const style = document.createElement('style');
      style.textContent = `
        .demo-container {
          /* Demo 的样式，不会污染父页面 */
        }
        .highlighted {
          border: 3px solid #ff0000;
          box-shadow: 0 0 10px rgba(255,0,0,0.5);
          animation: pulse 1s infinite;
        }
        @keyframes pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.7; }
        }
      `;
      shadowRoot.appendChild(style);

      // 渲染 Demo 内容
      const demoContainer = document.createElement('div');
      demoContainer.className = 'demo-container';
      shadowRoot.appendChild(demoContainer);

      // 使用 React 渲染到 Shadow DOM
      const root = createRoot(demoContainer);
      root.render(<DemoContent config={config} onElementClick={onElementClick} />);
    }
  }, []);

  // 暴露给父组件的方法
  useImperativeHandle(forwardedRef, () => ({
    highlightElement: (resourceId: string) => {
      const element = shadowRootRef.current?.querySelector(`[data-resource-id="${resourceId}"]`);
      if (element) {
        element.classList.add('highlighted');
      }
    },
    clearHighlight: () => {
      const elements = shadowRootRef.current?.querySelectorAll('.highlighted');
      elements?.forEach(el => el.classList.remove('highlighted'));
    }
  }));

  return <div ref={containerRef} className="demo-preview-wrapper" />;
}

// 使用 forwardRef 暴露方法
export const DemoPreview = forwardRef(DemoPreviewInternal);
```

**优点说明**：
- ✅ 样式完全隔离，不会污染父页面
- ✅ 脚本在同一上下文，通信简单（直接调用方法）
- ✅ 性能好，无额外开销
- ✅ 可以直接操作 DOM，无需 postMessage
- ✅ 支持双向联动（父组件调用方法 + 事件回调）

**注意事项**：
- ⚠️ 需要确保 Demo 代码完全可信
- ⚠️ 全局样式可能通过 `:host` 穿透（需要明确禁止）
- ⚠️ 事件冒泡需要特殊处理（使用 CustomEvent）

---

### 二、第8.4章新增：预览模板标准化规范

#### 8.4.1 模板结构

```
template-demo-001/
├── App.tsx              # 主组件代码
├── config.schema.json   # 配置 Schema
├── preview.png          # 预览缩略图
├── metadata.json        # 模板元数据
└── resources/           # 默认资源（可选）
    ├── default-banner.png
    └── default-icon.svg
```

#### 8.4.2 metadata.json 格式

```json
{
  "id": "demo-001",
  "name": "活动首页模板",
  "category": "活动页面",
  "version": "1.0.0",
  "author": "UI设计师A",
  "createdAt": "2026-01-15",
  "description": "适用于活动首页的通用模板",
  "tags": ["活动", "首页", "大促"],
  "dependencies": {
    "@scope/demo-sdk": "^1.0.0"
  },
  "shadowDOM": true,
  "isolatedStyles": true
}
```

#### 8.4.3 config.schema.json 规范

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "images": {
      "type": "object",
      "properties": {
        "banner": {
          "type": "string",
          "description": "横幅图片",
          "widget": "image-upload",
          "validation": {
            "maxWidth": 750,
            "maxHeight": 400,
            "maxSize": 500000,
            "formats": ["jpg", "png", "webp"]
          }
        }
      }
    },
    "texts": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "页面标题",
          "widget": "text-input",
          "maxLength": 50
        }
      }
    }
  }
}
```

---

### 三、第8.5章新增：版本管理与兼容性

#### 8.5.1 Demo 版本控制

- 每个 Demo 支持多版本管理（v1.0, v1.1, v2.0）
- 版本号遵循语义化版本规范（SemVer）
- 旧版本配置包导入新版 Demo 时需进行字段兼容性检查

#### 8.5.2 Schema 兼容性

**兼容性规则**：
- 新增字段：向后兼容，旧配置包可正常使用
- 修改字段：需提供迁移脚本
- 删除字段：需保留默认值，避免配置包失效

**兼容性检查示例**：

```typescript
function checkCompatibility(config: any, schema: Schema): CompatibilityResult {
  const missingFields = [];
  const deprecatedFields = [];
  
  // 检查缺失字段
  for (const key in schema.properties) {
    if (!(key in config)) {
      missingFields.push(key);
    }
  }
  
  // 检查废弃字段
  for (const key in config) {
    if (!(key in schema.properties)) {
      deprecatedFields.push(key);
    }
  }
  
  return {
    compatible: missingFields.length === 0,
    missingFields,
    deprecatedFields,
    warnings: deprecatedFields.map(f => `字段 ${f} 已废弃，将被忽略`)
  };
}
```

---

### 四、第9章"异常处理"补充集成场景

#### 9.4 集成场景异常处理

| 异常场景                  | 原因                          | 处理方式                                             |
| ------------------------- | ----------------------------- | ---------------------------------------------------- |
| **Demo 模板加载失败**     | Demo ID 不存在或已被删除      | 显示"模板不存在"提示，提供重新选择模板功能           |
| **配置 Schema 不匹配**    | Demo 版本更新导致 Schema 变化 | 自动执行兼容性检查，提示用户更新配置或降级 Demo 版本 |
| **资源校验失败**          | 上传资源不符合规范            | 显示具体错误信息（尺寸、格式、大小），阻止配置生效   |
| **预览组件渲染失败**      | 代码错误或依赖缺失            | 显示错误堆栈，提供"重试"和"联系管理员"选项           |
| **配置包导入失败**        | ZIP 文件损坏或格式错误        | 显示具体错误原因，提供重新上传功能                   |
| **Shadow DOM 初始化失败** | 浏览器不支持 Shadow DOM       | 降级到 iframe 模式，显示兼容性提示                   |
| **高亮元素定位失败**      | 元素不存在或已被移除          | 静默失败，记录错误日志                               |

---

### 五、第14章"交付物清单"补充

**原清单**：
1. Figma 插件安装包
2. DSLP 协议规范文档
3. Web 工作台源码
4. Demo SDK NPM 包
5. 测试报告

**补充后清单**：
1. **Figma 插件安装包** (`.wgt` / 商店链接)
2. **DSLP 协议规范文档** (PDF)
3. **Web 工作台源码** (Next.js Repo)
4. **Demo SDK NPM 包** (`@scope/demo-sdk`)
5. **测试报告** (包含 Figma 复杂布局还原度测试、AI 生成可用性测试)
6. **API 接口文档** (Swagger/OpenAPI 规范)
7. **集成指南** (面向设计规范 CMS 和活动管理系统的集成文档)
8. **组件使用手册** (预览组件的详细使用说明和示例)
9. **Shadow DOM 集成最佳实践** (样式隔离、事件处理、性能优化指南)

---

## 优化建议优先级

| 优先级 | 优化项                    | 章节 | 说明               |
| ------ | ------------------------- | ---- | ------------------ |
| **P0** | 第8章系统集成内容扩充     | 8    | 核心功能，必须补充 |
| **P0** | 第8.4章预览模板标准化规范 | 8.4  | 标准化，必须补充   |
| **P1** | 第9章集成场景异常处理     | 9.4  | 完善性，建议补充   |
| **P1** | 第8.5章版本管理与兼容性   | 8.5  | 完善性，建议补充   |
| **P2** | 第14章交付物清单补充      | 14   | 文档性，可以补充   |

---

## 关键改动说明

1. **集成方式调整**：从 iframe/内嵌双模式改为以 **Shadow DOM + CSS-in-JS** 为主
2. **联动机制明确**：明确支持双向联动（父组件调用方法 + 事件回调）
3. **样式隔离保证**：通过 Shadow DOM 实现完全的样式隔离
4. **通信简化**：无需 postMessage，直接调用方法，降低复杂度

需要我帮你生成完整的第8章内容吗？