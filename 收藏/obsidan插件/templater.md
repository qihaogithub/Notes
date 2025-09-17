# templater 插件说明

## 插件简介
templater 是 Obsidian 的一个强大的模板系统插件，它极大地扩展了 Obsidian 原生的模板功能，提供了动态内容生成、变量替换和脚本执行能力。这个插件特别适合那些希望自动化笔记创建流程、插入动态内容、或基于模板构建复杂笔记结构的用户，可以显著提高笔记创建和管理的效率。

## 主要功能

### 1. 增强的模板系统
- 支持丰富的内置变量（日期、时间、文件路径等）
- 可以创建和使用自定义变量
- 提供条件语句和循环结构
- 支持模板嵌套和包含
- 可以定义模板的默认保存位置

### 2. 动态内容生成
- 在模板中执行 JavaScript 代码
- 访问 Obsidian API 和 Templater API
- 生成基于上下文的动态内容
- 支持从外部源获取数据
- 可以创建交互式模板

### 3. 自动化工作流
- 为模板分配触发条件
- 支持基于事件的模板应用
- 提供批量应用模板的功能
- 可以创建模板自动化命令
- 支持模板组合和串联

### 4. 高级模板编辑
- 提供模板预览功能
- 支持模板语法高亮
- 可以设置模板快捷键
- 提供模板导入和导出
- 支持版本控制和历史记录

## 安装方法
1. 在 Obsidian 的设置中打开社区插件
2. 禁用安全模式
3. 点击"浏览社区插件"
4. 搜索"templater"
5. 点击"安装"，然后启用插件

## 使用教程

### 基本模板创建
- 在 Obsidian 中创建一个新的笔记作为模板
- 在笔记中使用 `<%` 和 `%>` 标签插入变量和代码
- 例如：`<% tp.date.now("YYYY-MM-DD") %>` 插入当前日期
- 保存模板到指定的模板文件夹
- 在设置中配置模板文件夹路径

### 应用模板
- 使用命令面板搜索"Templater: Insert Template"选择并应用模板
- 或者使用快捷键触发模板插入
- 对于新文件，可以使用"Templater: Create new note from template"命令
- 查看模板执行结果，包括变量替换和代码执行结果
- 根据需要调整模板内容和逻辑

### 创建动态模板
- 在模板中使用 JavaScript 代码块：`<%* /* 你的代码 */ %>`
- 利用 Templater API 访问 Obsidian 功能
- 例如：`<%* const title = tp.system.prompt("请输入标题："); %>`
- 在代码中设置变量，然后在模板的其他部分使用：`<% title %>`
- 使用条件语句和循环构建复杂逻辑

### 自动化模板应用
- 在 Templater 设置中，配置模板触发条件
- 设置文件创建时自动应用的模板
- 创建基于文件路径或内容的条件模板规则
- 使用命令面板中的"Templater: Reload templates"刷新模板配置
- 测试自动化规则，确保按预期工作

## 配置选项说明

### 基本设置
- **Template folder location**: 设置模板文件夹位置
- **Enable folder templates**: 启用文件夹模板
- **Trigger on file creation**: 在文件创建时触发
- **Auto-reload modified templates**: 自动重新加载修改的模板
- **Show icon in ribbon**: 在功能区显示图标

### 语法设置
- **Syntax highlight templates**: 语法高亮模板
- **Evaluate on load**: 在加载时评估
- **Enable system commands**: 启用系统命令
- **Shell command output encoding**: Shell 命令输出编码
- **Shell command timeout**: Shell 命令超时时间

### 变量和函数设置
- **User functions folder**: 用户函数文件夹
- **Enable user functions**: 启用用户函数
- **Cache user functions**: 缓存用户函数
- **Enable core plugins functions**: 启用核心插件函数
- **Enable community plugins functions**: 启用社区插件函数

### 高级设置
- **Enable debug mode**: 启用调试模式
- **Debug output folder**: 调试输出文件夹
- **Log level**: 日志级别
- **Max execution time**: 最大执行时间
- **Allow overriding new file location**: 允许覆盖新文件位置

## 高级功能

### 自定义脚本和函数
- 创建可重用的自定义函数
- 将函数组织到模块中以保持整洁
- 为常用操作创建封装函数
- 分享和重用社区创建的函数库
- 可以通过 API 访问其他插件功能

### 复杂工作流集成
- 与其他插件（如 QuickAdd、Dataview 等）集成
- 创建多步骤自动化工作流
- 支持条件分支和错误处理
- 可以基于文件内容执行不同的模板逻辑
- 提供事件钩子，响应 Obsidian 中的各种事件

### 交互式模板
- 创建带有用户输入的模板
- 使用表单收集信息
- 提供选项和选择器
- 支持实时预览和反馈
- 可以保存用户偏好和设置

### 外部数据集成
- 从本地文件或网络资源获取数据
- 解析和处理 JSON、CSV 等格式的数据
- 与外部 API 交互
- 支持数据缓存和刷新策略
- 可以创建基于外部数据的动态内容

## 注意事项
- 高级功能（如 JavaScript 代码）需要一定的编程知识
- 复杂的模板可能会影响性能，尤其是在大型笔记库中
- 使用系统命令和外部 API 时请注意安全风险
- 在修改模板前，建议备份重要的模板和笔记
- 与某些插件可能存在兼容性问题，特别是其他模板或自动化相关的插件
- 模板中的错误可能导致内容生成不正确，请仔细测试

## 常见问题解答

### Q: Templater 和 QuickAdd 有什么区别？
A: Templater 更专注于模板内容的动态生成和处理，而 QuickAdd 更专注于触发和管理模板的应用过程。两者可以互补使用，创建强大的自动化工作流。

### Q: 如何创建一个交互式模板？
A: 您可以使用 Templater 的 `tp.system.prompt()`、`tp.system.suggester()` 等函数来创建交互式元素。例如：`<%* const name = tp.system.prompt("请输入名称："); %>` 会弹出一个提示框收集用户输入。

### Q: 可以在模板中访问其他笔记的内容吗？
A: 是的，您可以使用 Templater API 如 `tp.file.find_tfile()` 和 `app.vault.read()` 来访问其他笔记的内容。这允许您创建基于现有笔记内容的动态模板。

### Q: 模板中的代码执行权限如何控制？
A: Templater 提供了设置选项来控制代码执行权限，包括是否允许系统命令、外部 API 调用等。在使用不受信任的模板时，请仔细检查其代码内容和权限设置。