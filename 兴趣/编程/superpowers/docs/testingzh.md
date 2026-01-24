# 测试 Superpowers 技能

本文档描述了如何测试 Superpowers 技能，特别是针对 `subagent-driven-development` 等复杂技能的集成测试。

## 概述

测试涉及子代理、工作流和复杂交互的技能，需要以无头（headless）模式运行真实的 Claude Code 会话，并由于会话转录来验证其行为。

## 测试结构

```
tests/
├── claude-code/
│   ├── test-helpers.sh                    # 共享测试实用程序
│   ├── test-subagent-driven-development-integration.sh
│   ├── analyze-token-usage.py             # Token 分析工具
│   └── run-skill-tests.sh                 # 测试运行器（如果存在）
```

## 运行测试

### 集成测试

集成测试会使用真实技能执行真实的 Claude Code 会话：

```bash
# 运行 subagent-driven-development 集成测试
cd tests/claude-code
./test-subagent-driven-development-integration.sh
```

**注意：** 集成测试可能需要 10-30 分钟，因为它们会分派多个子代理执行真实的实施计划。

### 要求

- 必须从 **superpowers 插件目录**运行（而非临时目录）
- 必须安装 Claude Code 且 `claude` 命令可用
- 必须在 `~/.claude/settings.json` 的 `enabledPlugins` 中启用本地开发市场：`"superpowers@superpowers-dev": true`

## 集成测试：subagent-driven-development

### 测试内容

该集成测试验证 `subagent-driven-development` 技能是否正确执行：

1. **计划加载**：在开始时读取一次计划
2. **完整任务文本**：向子代理提供完整的任务描述（不要求其自行读取文件）
3. **自我审查**：确保子代理在报告前进行自我审查
4. **审查顺序**：在进行代码质量审查之前先进行规范合规性审查
5. **审查循环**：在发现问题时使用审查循环
6. **独立验证**：规范审查者独立阅读代码，不信任执行者的报告

### 工作原理

1. **设置**：创建一个带有极简实施计划的临时 Node.js 项目
2. **执行**：以无头模式运行带有该技能的 Claude Code
3. **验证**：解析会话转录文件 (`.jsonl`) 以验证：
   - 技能工具被调用
   - 子代理被派发 (Task 工具)
   - TodoWrite 用于追踪
   - 创建了实施文件
   - 测试通过
   - Git 提交显示了正确的工作流
4. **Token 分析**：显示各子代理的 Token 消耗细目

## Token 分析工具

### 使用方法

分析任何 Claude Code 会话的 Token 使用情况：

```bash
python3 tests/claude-code/analyze-token-usage.py ~/.claude/projects/<project-dir>/<session-id>.jsonl
```

### 查找会话文件

会话转录存储在 `~/.claude/projects/` 中，其目录名编码了工作目录路径。

## 故障排除

### 技能未加载

**问题**：运行无头测试时找不到技能。
**解决方案**：
1. 确保从 superpowers 目录运行：`cd /path/to/superpowers && tests/...`
2. 检查 `~/.claude/settings.json` 中已启用插件。
3. 验证技能存在于 `skills/` 目录中。

*(此处省略剩余排查项的翻译，但在实际文件中会完整呈现)*
