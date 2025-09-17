---
来源: https://www.aivi.fyi/aiagents/introduce-Gemini-CLI
作者: "[[AI超元域]]"
发布时间: 2025-06-25T00:00:00+08:00
创建日期: 2025-06-30T09:34:22+08:00
描述: Google最近推出了Gemini CLI，这是一个基于Gemini 1.5 Pro模型的开源命令行界面工具，将人工智能直接引入开发者的终端环境。这一创新工具代表了开发者生产力的重大进步，将传统命令行从刚性的命令执行器转变为智能的对话伙伴。
tags:
  - clippings
---
[中文文档](https://gemini-doc.haleclipse.de/zh/guide.html)

## 基础操作：

- **添加上下文** ：使用 @ 指定文件作为上下文（例如：@src/myFile.ts）来定位特定文件或文件夹
- **Shell 模式** ：通过! 执行shell命令（例如：!npm run start）或使用自然语言（例如：启动服务器）

 ## 命令列表：

- `/help` - 显示 gemini-cli 的帮助信息
- `/docs` - 在浏览器中打开完整的 Gemini CLI 文档
- `/clear` - 清除屏幕和对话历史
- `/theme` - 更改主题
- `/auth` - 更改认证方法
- `/editor` - 设置外部编辑器偏好
- `/stats` - 检查会话统计信息
- `/mcp` - 列出已配置的 MCP 服务器和工具
- | `/memory` - 管理内存。用法：/memory <show | refresh | add> \[用于添加的文本\] |
	| --- | --- | --- |
- `/tools` - 列出可用的 Gemini CLI 工具
- `/about` - 显示版本信息
- `/bug` - 提交错误报告
- | `/chat` - 管理对话历史。用法：/chat <list | save | resume> \[标签\] |
	| --- | --- | --- |
- `/quit` - 退出命令行界面
- `/compress` - 通过将上下文替换为摘要来压缩上下文
- `!` - shell 命令

## 键盘快捷键：

- **Enter** - 发送消息
- **Shift+Enter** - 换行
- **Up/Down** - 在提示历史中循环
- **Alt+Left/Right** - 在输入中按单词跳转
- **Esc** - 取消操作
- **Ctrl+C** - 退出应用程序

## MCP Server配置命令

`mkdir -p ~/.gemini`

`cd ~/.gemini`

`nano settings.json`

配置文件(context7为例)

```json
{
  "theme": "Default",
  "selectedAuthType": "oauth-personal",
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "taskmaster-ai": {
      "command": "npx",
      "args": ["-y", "--package=task-master-ai", "task-master-ai"],
      "env": {
        "ANTHROPIC_API_KEY": "sk-ant-"
        "OPENAI_API_KEY": "sk-proj-"
        "GOOGLE_API_KEY": "sk-proj-"
      }
    }
  }
```

## GEMINI.md配置示例

```bash
# AutoGen AI智能体开发项目

## 项目概述
使用 AutoGen 0.4 最新版本开发AI智能体，Python 3.11，venv虚拟环境。

## 环境配置

### Python环境
- Python版本：3.11
- 虚拟环境：使用venv
- 包管理：pip + requirements.txt

### 安装步骤

# 创建虚拟环境
python3.11 -m venv .venv

# 激活环境
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 安装AutoGen
pip install -U "autogen-agentchat" "autogen-ext[openai]"

## 编程规范

### 导入约定

import asyncio
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

### 代码风格
- 所有操作使用 async/await（AutoGen 0.4是异步架构）
- 使用类型提示
- 函数和类添加中文注释
- 错误处理要完善

### 基本模式

async def main():
    # 创建模型客户端
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    
    # 创建智能体
    agent = AssistantAgent("助手", model_client=model_client)
    
    # 运行任务
    result = await agent.run(task="你的任务")
    
    # 关闭连接
    await model_client.close()

## 项目结构

项目目录/
├── .venv/           # 虚拟环境（不提交到git）
├── .env             # 环境变量（不提交到git）
├── requirements.txt # 依赖包
├── agents/          # 智能体实现
├── main.py          # 主程序入口
└── GEMINI.md        # 本配置文件

## 环境变量设置

# .env 文件
OPENAI_API_KEY=你的API密钥
MODEL_NAME=gpt-4o

## 开发要点

### 智能体类型
- **AssistantAgent**: LLM驱动的助手智能体
- **CodeExecutorAgent**: 代码执行智能体

### 团队模式
- **RoundRobinGroupChat**: 轮询组聊天
- 支持多智能体协作

### 最佳实践
- 先单独测试智能体，再组合成团队
- 使用async/await处理所有操作
- 正确关闭模型客户端连接
- 环境变量管理敏感信息
- 虚拟环境不提交到版本控制

## 文档和资源获取

### MCP服务器配置
始终使用 **context7 MCP server** 搜索AutoGen最新文档和代码规范：
- 优先查询AutoGen 0.4官方文档
- 获取最新的API参考和最佳实践
- 查找代码示例和模式
- 验证版本兼容性和新特性

### 搜索策略
当需要AutoGen相关信息时：
1. 首先使用context7搜索官方文档
2. 重点关注0.4版本的变更和新特性
3. 获取异步编程模式的最新示例
4. 查找多智能体协作的最佳实践

## 注意事项
- AutoGen 0.4与0.2版本完全不同，使用新的异步架构
- AgentChat适合快速原型开发
- 需要Python 3.11
- 所有示例代码使用中文注释
- 遇到问题时优先通过context7搜索最新解决方案
```

## Gemini CLI 高级用法指南

## 安装与认证

### 快速安装

```bash
# 直接运行（推荐）
npx https://github.com/google-gemini/gemini-cli

# 或全局安装
npm install -g @google/gemini-cli
```

### 高级认证配置

```bash
# 使用 API 密钥（适用于企业用户）
export GEMINI_API_KEY="your_api_key_here"

# Google Workspace 账户认证
gemini auth --workspace

# 检查认证状态
gemini auth status
```

## MCP 服务器集成

```
cd ~/.gemini
nano settings.json
```

## 更新

在终端或命令提示符中运行以下命令，npm 会自动将全局安装的 `@google/gemini-cli` 更新到最新版本：

```bash
npm update -g @google/gemini-cli
```
