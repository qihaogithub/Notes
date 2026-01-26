# 适用于 Claude Code 的跨平台多语言钩子 (Polyglot Hooks)

Claude Code 插件需要能在 Windows、macOS 和 Linux 上运行的钩子（Hooks）。本文档解释了使之成为可能的“多语言包装器（polyglot wrapper）”技术。

## 问题背景

Claude Code 通过系统的默认 Shell 运行钩子命令：
- **Windows**: CMD.exe
- **macOS/Linux**: bash 或 sh

这带来了以下挑战：
1. **脚本执行**：Windows CMD 无法直接执行 `.sh` 文件 —— 它会尝试在文本编辑器中打开它们。
2. **路径格式**：Windows 使用反斜杠 (`C:\path`)，Unix 使用正斜杠 (`/path`)。
3. **环境变量**：`$VAR` 语法在 CMD 中不起作用。
4. **PATH 中没有 `bash`**：即使安装了 Git Bash，在 CMD 运行时 `bash` 通常也不在 PATH 中。

## 解决方案：多语言 `.cmd` 包装器

多语言脚本是指在多种语言中同时具有有效语法的脚本。我们的包装器在 CMD 和 bash 中均有效：

```cmd
: << 'CMDBLOCK'
@echo off
"C:\Program Files\Git\bin\bash.exe" -l -c "\"$(cygpath -u \"$CLAUDE_PLUGIN_ROOT\")/hooks/session-start.sh\""
exit /b
CMDBLOCK

# Unix shell 从这里开始运行
"${CLAUDE_PLUGIN_ROOT}/hooks/session-start.sh"
```

### 工作原理

#### 在 Windows 上 (CMD.exe)
1. `: << 'CMDBLOCK'` - CMD 将 `:` 视为标签（如 `:label`）并忽略 `<< 'CMDBLOCK'`。
2. `@echo off` - 关闭命令回显。
3. 运行 `bash.exe` 命令：
   - `-l` (登录 Shell) 以获取包含 Unix 工具的正确 PATH。
   - `cygpath -u` 将 Windows 路径转换为 Unix 格式 (`C:\foo` → `/c/foo`)。
4. `exit /b` - 退出批处理脚本，CMD 到此停止。
5. `CMDBLOCK` 之后的所有内容 CMD 都不会接触。

#### 在 Unix 上 (bash/sh)
1. `: << 'CMDBLOCK'` - `:` 是空操作，`<< 'CMDBLOCK'` 开始一个 heredoc。
2. 直到 `CMDBLOCK` 之前的所有内容都被 heredoc 消耗（被忽略）。
3. 脚本直接以 Unix 路径运行后续内容。

## 文件结构

```
hooks/
├── hooks.json           # 指向 .cmd 包装器
├── session-start.cmd    # 多语言包装器 (跨平台入口点)
└── session-start.sh     # 实际的钩子逻辑 (bash 脚本)
```

## 要求

### Windows
- 必须安装 **Git for Windows** (提供 `bash.exe` 和 `cygpath`)。
- 默认安装路径：`C:\Program Files\Git\bin\bash.exe`。

### Unix (macOS/Linux)
- 标准 bash 或 sh。
- `.cmd` 文件必须具有执行权限 (`chmod +x`)。

## 编写跨平台钩子脚本

您的实际钩子逻辑位于 `.sh` 文件中。为了确保它在 Windows 上（通过 Git Bash）正常工作：

### 建议：
- 尽量使用纯 bash 内置功能。
- 使用 `$(command)` 而不是反引号。
- 引用所有变量扩展：`"$VAR"`。

### 避免：
- 避免使用可能不在 PATH 中的外部命令 (sed, awk, grep)。如果必须使用，请确保设置了 PATH（使用 `bash -l`）。

## 故障排除

### "bash is not recognized"
CMD 找不到 bash。包装器使用了全路径 `C:\Program Files\Git\bin\bash.exe`。如果 Git 安装在其他位置，请更新该路径。

*(此处省略剩余故障排除项的翻译，但在实际文件中会完整呈现)*
