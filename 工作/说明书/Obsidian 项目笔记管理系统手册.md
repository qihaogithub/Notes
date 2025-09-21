本文档旨在为 UI 设计师、产品经理等角色，提供一套基于 Obsidian 的结构化项目笔记管理方案。它强调项目中心、人机分离，并为未来的 AI 智能体集成做好了准备。

---

## 1. 核心设计原则

本系统的构建遵循以下六大原则，确保其高效、可扩展且易于维护。

| 原则           | 说明                                                                        |
| :------------- | :-------------------------------------------------------------------------- |
| **项目为中心** | 所有会议、文档、周报等资料，均围绕“项目”组织，通过 `projects` 字段关联。    |
| **人机分离**   | AI 生成内容与人工撰写内容**物理分离**，存于不同文档，避免 AI 干扰核心思考。 |
| **机器友好**   | 文件命名、YAML 字段、小标题结构标准化，便于 Dataview 聚合与未来 AI 解析。   |
| **层级可扩展** | 项目支持 `parent_project` 字段，可建立父子关系，无限嵌套。                  |
| **动态聚合**   | 利用 Dataview 自动生成看板与列表，无需手动维护项目状态与文档链接。          |

---

## 2. 系统构成

### 2.1. 文件夹结构

清晰的文件夹结构是系统的基础，实现不同类型信息的物理隔离。

```
📁 项目/
├── 📁 2025/
│   ├── 📄 2025-04-05_重做官网首页_UI.md    ← 🧑 人工主笔记
│   └── 📄 2025-04-05_极速做官网首页_UI_AI.md    ← 🤖 AI辅助笔记
└── 📄 📊 项目总览.md

📁 资料/
├── 📁 会议记录/
│   └── 📄 2025-04-06_会议_需求对齐.md
├── 📁 产品文档/
│   └── 📄 官网V3_PRD.md
├── 📁 周报/
│	├── 📁 2025/
│	│   ├── 📄 2025-W14_我的周报.md
│	│   └── 📄 2025-W14_张三_产品经理周报.md
└── └── 📄 📊 周报总览.md

📁 人员/
└── 📄 张三_产品经理.md

📁 模版/
├── 📄 Project_Human.md          ← 人工主笔记模板
├── 📄 Project_AI.md             ← AI笔记模板
└── ...

📁 附件/                  ← 截图、PDF等附件
```

### 2.2. 文档类型与职责

系统包含三类核心文档，各司其职。

#### ① 人工主笔记（核心）

- **命名**: `YYYY-MM-DD_项目名.md`
- **位置**: `项目/YYYY/`
- **职责**: 记录您的深度思考、设计策略、主观判断和最终决策，是项目的权威版本。

#### ② AI 辅助笔记（聚合器）

- **命名**: `YYYY-MM-DD_项目名_AI.md`
- **位置**: `项目/YYYY/`
- **职责**: 由 AI 根据所有相关源文档自动生成和更新，作为项目信息的“初稿”和“聚合器”，供您快速参考。

#### ③ 源文档（信息源）

- **命名**: `YYYY-MM-DD_类型_描述.md` 或 `文档名_类型.md`
- **职责**: 记录会议、PRD、周报等原始信息。
- **关键要求**: 必须包含 `projects` 字段，以链接到对应的项目。
  ```yaml
  # 示例：关联到多个项目
  projects:
    - "[[2025-04-05_重做官网首页_UI]]"
    - "[[2025-03-01_品牌升级总项目]]"
  ```

---

## 3. 日常工作流程

### 3.1. 新建项目

1.  使用 Templater 新建“项目笔记”。
2.  模板将自动生成人工主笔记 (`项目名.md`)。
3.  在人工主笔记中填写背景、目标、策略等核心内容。

### 3.2. 日常更新

1.  **记录过程**: 创建会议、PRD 等源文档，并使用 `projects` 字段关联到当前项目。
2.  **AI 辅助笔记**: AI 智能体将检查自动巡查相关文档变化，并生成对应项目的 AI 辅助笔记 (`项目名_AI.md`)。
3.  **提炼决策**: 定期查看 AI 笔记，将有价值的信息（如会议决议、需求变更）提炼、重写后，更新到您的人工主笔记中。

### 3.3. 项目完结

1.  在人工主笔记中，补充“结果、数据、复盘”等内容。
2.  将 YAML 中的 `status` 字段更新为 `#已完成`。

---

## 4. 关联与聚合

### 4.1. 管理父子项目

通过在子项目中添加 `parent_project` 字段，可以建立项目层级关系。

- **子项目设置**:
  ```yaml
  ---
  parent_project: "[[2025-03-01_品牌升级总项目]]"
  ---
  ```
- **父项目自动聚合**: 在父项目笔记中使用 Dataview 查询，即可自动展示所有子项目列表。
  ```dataview
  ## 🧩 子项目列表
  TABLE status, updated
  FROM "项目/2025"
  WHERE parent_project = this.file.link
  ```

### 4.2. 看板与总览

#### 项目总览 (`项目/📊 项目总览.md`)

此看板展示所有人工创建的项目，并自动排除 AI 笔记。

## 进行中项目

```dataview
TABLE priority, updated
FROM "项目"
WHERE contains(status, "进行中") AND file.name != this.file.name AND !contains(file.name, "_AI")
SORT updated DESC
```

## 已完成项目

```dataview
TABLE priority, updated
FROM "项目"
WHERE contains(status, "已完成") AND file.name != this.file.name AND !contains(file.name, "_AI")
SORT updated DESC
```

#### 周报总览 (`资料/周报/📊 周报总览.md`)

独立归档和检索所有周报。

```dataview
TABLE author, date
FROM "资料/周报/2025"
SORT date DESC
```

---

## 5. 模板参考

### 项目主笔记模板 (`模版/Project_Human.md`)

````
---
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
status: #进行中
projects:
parent_project:
stakeholders: []
tags: #UI设计
---

# {{title}}

> ✍️ 此为主笔记，由设计师人工撰写，包含深度思考与最终决策。

## 📅 背景与目标

## 👥 相关人员

## 🔄 关键过程

## ⚠️ 风险摘要

## 📌 待办汇总

## 🏁 结果与复盘

## 🔗 相关文档
- 笔记:  [[{{title}}_AI]]
- 会议：
    ```dataview
    LIST FROM "资料/会议记录"
    WHERE contains(projects, this.file.link)
    SORT file.mtime DESC
    ```
- PRD：
    ```dataview
    LIST FROM "资料/产品文档"
    WHERE contains(projects, this.file.link)
    SORT file.mtime DESC
    ```
- Figma：
[设计稿](https://www.figma.com/design/xxxxxx)
````

## 6. AI 功能

详见：[[AI 功能实现方案]]
