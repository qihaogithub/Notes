# OpenCode 支持设计

**日期：** 2025-11-22
**作者：** Bot & Jesse
**状态：** 设计完成，等待实施

## 概述

使用原生的 OpenCode 插件架构为 OpenCode.ai 添加完整的 Superpowers 支持，该架构与现有的 Codex 实现共享核心功能。

## 背景

OpenCode.ai 是一个类似于 Claude Code 和 Codex 的编程代理。之前尝试将 Superpowers 移植到 OpenCode（PR #93, PR #116）时采用了文件复制的方法。本设计采用了不同的方法：利用 OpenCode 的 JavaScript/TypeScript 插件系统构建原生插件，同时与 Codex 实现共享代码。

### 平台间的关键差异

- **Claude Code**：原生的 Anthropic 插件系统 + 基于文件的技能
- **Codex**：无插件系统 → 引导 Markdown + CLI 脚本
- **OpenCode**：带有事件钩子和自定义工具 API 的 JavaScript/TypeScript 插件

### OpenCode 的代理系统

- **主要代理**：Build（默认，完全访问权限）和 Plan（受限，只读）
- **子代理**：General（研究、搜索、多步骤任务）
- **调用方式**：由主要代理自动派发，或使用手动 `@mention` 语法
- **配置**：在 `opencode.json` 或 `~/.config/opencode/agent/` 中的自定义代理

## 架构

### 高层结构

1. **共享核心模块** (`lib/skills-core.js`)
   - 通用的技能发现和解析逻辑
   - 被 Codex 和 OpenCode 实现共同使用

2. **平台特定包装器**
   - Codex：CLI 脚本 (`.codex/superpowers-codex`)
   - OpenCode：插件模块 (`.opencode/plugin/superpowers.js`)

3. **技能目录**
   - 核心技能：`~/.config/opencode/superpowers/skills/`（或安装位置）
   - 个人技能：`~/.config/opencode/skills/`（覆盖核心技能）

### 代码复用策略

将 `.codex/superpowers-codex` 中的通用功能提取到共享模块中：

```javascript
// lib/skills-core.js
module.exports = {
  extractFrontmatter(filePath),      // 从 YAML 解析名称和描述
  findSkillsInDir(dir, maxDepth),    // 递归发现 SKILL.md
  findAllSkills(dirs),               // 扫描多个目录
  resolveSkillPath(skillName, dirs), // 处理覆盖 (个人 > 核心)
  checkForUpdates(repoDir)           // Git fetch/状态检查
};
```

### 技能前置数据（Frontmatter）格式

当前格式（无 `when_to_use` 字段）：

```yaml
---
name: skill-name
description: 当 [条件] 时使用 - [它的作用]; [额外背景]
---
```

## OpenCode 插件实现

### 自定义工具

**工具 1：`use_skill`**

将特定技能的内容加载到对话中（相当于 Claude 的 Skill 工具）。

```javascript
{
  name: 'use_skill',
  description: '加载并阅读特定技能以指导您的工作',
  schema: z.object({
    skill_name: z.string().describe('技能名称 (例如 "superpowers:brainstorming")')
  }),
  execute: async ({ skill_name }) => {
    const { skillPath, content, frontmatter } = resolveAndReadSkill(skill_name);
    const skillDir = path.dirname(skillPath);

    return `# ${frontmatter.name}
# ${frontmatter.description}
# 支持工具和文档位于 ${skillDir}
# ============================================

${content}`;
  }
}
```

**工具 2：`find_skills`**

列出所有带有元数据的可用技能。

```javascript
{
  name: 'find_skills',
  description: '列出所有可用技能',
  schema: z.object({}),
  execute: async () => {
    const skills = discoverAllSkills();
    return skills.map(s =>
      `${s.namespace}:${s.name}
  ${s.description}
  目录: ${s.directory}
`).join('\n');
  }
}
```

### 会话启动钩子

当新会话开始时 (`session.started` 事件)：

1. **注入 using-superpowers 内容**
   - using-superpowers 技能的全部内容
   - 确立强制性的工作流

2. **自动运行 find_skills**
   - 预先显示可用技能的完整列表
   - 包含每个技能的目录

3. **注入工具映射指令**
   ```markdown
   **OpenCode 工具映射：**
   当技能引用了您没有的工具时，请进行替换：
   - `TodoWrite` → `update_plan`
   - 带有子代理的 `Task` → 使用 OpenCode 子代理系统 (@mention)
   - `Skill` 工具 → `use_skill` 自定义工具
   - Read, Write, Edit, Bash → 您的原生等效工具

   **技能目录包含：**
   - 支持脚本 (使用 bash 运行)
   - 额外文档 (使用 read 工具阅读)
   - 该技能特有的实用程序
   ```

4. **检查更新**（非阻塞）
   - 带有超时的快速 git fetch
   - 如果有可用更新则通知

### 插件结构

```javascript
// .opencode/plugin/superpowers.js
const skillsCore = require('../../lib/skills-core');
const path = require('path');
const fs = require('fs');
const { z } = require('zod');

export const SuperpowersPlugin = async ({ client, directory, $ }) => {
  const superpowersDir = path.join(process.env.HOME, '.config/opencode/superpowers');
  const personalDir = path.join(process.env.HOME, '.config/opencode/skills');

  return {
    'session.started': async () => {
      const usingSuperpowers = await readSkill('using-superpowers');
      const skillsList = await findAllSkills();
      const toolMapping = getToolMappingInstructions();

      return {
        context: `${usingSuperpowers}\n\n${skillsList}\n\n${toolMapping}`
      };
    },

    tools: [
      {
        name: 'use_skill',
        description: '加载并阅读特定技能',
        schema: z.object({
          skill_name: z.string()
        }),
        execute: async ({ skill_name }) => {
          // 使用 skillsCore 实现
        }
      },
      {
        name: 'find_skills',
        description: '列出所有可用技能',
        schema: z.object({}),
        execute: async () => {
          // 使用 skillsCore 实现
        }
      }
    ]
  };
};
```

## 文件结构

```
superpowers/
├── lib/
│   └── skills-core.js           # 新增：共享技能逻辑
├── .codex/
│   ├── superpowers-codex        # 更新：使用 skills-core
│   ├── superpowers-bootstrap.md
│   └── INSTALL.md
├── .opencode/
│   ├── plugin/
│   │   └── superpowers.js       # 新增：OpenCode 插件
│   └── INSTALL.md               # 新增：安装指南
└── skills/                       # 未更动
```

## 实施计划

### 第 1 阶段：重构共享核心

1. 创建 `lib/skills-core.js`
   - 从 `.codex/superpowers-codex` 提取前置数据解析
   - 提取技能发现逻辑
   - 提取路径解析 (带覆盖功能)
   - 更新为仅使用 `name` 和 `description` (不含 `when_to_use`)

2. 更新 `.codex/superpowers-codex` 以使用共享核心
   - 从 `../lib/skills-core.js` 导入
   - 移除重复代码
   - 保留 CLI 包装逻辑

3. 测试 Codex 实现是否仍然工作
   - 验证 bootstrap 命令
   - 验证 use-skill 命令
   - 验证 find-skills 命令

### 第 2 阶段：构建 OpenCode 插件

1. 创建 `.opencode/plugin/superpowers.js`
   - 从 `../../lib/skills-core.js` 导入共享核心
   - 实现插件函数
   - 定义自定义工具 (use_skill, find_skills)
   - 实现 session.started 钩子

2. 创建 `.opencode/INSTALL.md`
   - 安装说明
   - 目录设置
   - 配置指南

3. 测试 OpenCode 实现
   - 验证会话启动引导
   - 验证 use_skill 工具工作正常
   - 验证 find_skills 工具工作正常
   - 验证技能目录可访问

### 第 3 阶段：文档与完善

1. 更新 README 以包含 OpenCode 支持
2. 在主文档中添加 OpenCode 安装说明
3. 更新发布说明 (RELEASE-NOTES)
4. 测试 Codex 和 OpenCode 是否都能正确工作

## 下一步

1. **创建隔离的工作空间** (使用 git worktrees)
   - 分支：`feature/opencode-support`

2. **在适用处遵循 TDD**
   - 测试共享核心函数
   - 测试技能发现和解析
   - 针对两个平台的集成测试

3. **增量实施**
   - 第 1 阶段：重构共享核心 + 更新 Codex
   - 在继续之前验证 Codex 是否仍然工作
   - 第 2 阶段：构建 OpenCode 插件
   - 第 3 阶段：文档和完善

4. **测试策略**
   - 使用真实的 OpenCode 安装进行手动测试
   - 验证技能加载、目录、脚本是否工作
   - 并排测试 Codex 和 OpenCode
   - 验证工具映射是否正确工作

5. **PR 与合并**
   - 创建包含完整实现的 PR
   - 在干净的环境中测试
   - 合并到主分支

## 收益

- **代码复用**：技能发现/解析的单一事实来源
- **可维护性**：错误修复适用于两个平台
- **可扩展性**：易于添加未来的平台 (Cursor, Windsurf 等)
- **原生集成**：正确使用 OpenCode 的插件系统
- **一致性**：跨所有平台拥有相同的技能体验
