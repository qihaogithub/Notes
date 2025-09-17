Cursor AI 最近非常火，我付费使用它已经有一段时间。

今天详细介绍下它，适合已初步了解 Cursor 的朋友阅读。

https://www.cursor.com/

| 快捷键 | 功能 |
| --- | --- |
| Ctrl/⌘ + L | 切换 AI 面板并聚焦到聊天 |
| Ctrl/⌘ + Alt/Option + L | 打开聊天历史 |
| Ctrl/⌘ + Shift + J | 打开 Cursor 特定设置面板 |
| Ctrl/⌘ + Shift + P | 打开命令面板 (可用于访问 VS Code 设置) |
| Ctrl/⌘ + K | 打开用于代码生成/编辑的提示栏 |
| Ctrl/⌘ + / | 在聊天中切换 AI 模型 |
| Ctrl/⌘ + . | 切换不同的聊天模式 (在长上下文聊天中) |
| Ctrl/⌘ + Enter | 在聊天中：扫描已索引的代码库以查找相关代码 |
| Alt/Option + Enter | 在提示栏中：快速问答模式 |
| Ctrl/⌘ + Enter | 在终端 Cmd K 中：立即运行生成的命令 |
| Ctrl/⌘ + Shift + E | 对 linter 错误进行 AI 修复 |
| Tab | 在 Cursor Tab 中接受 AI 建议 |
| Esc | 在 Cursor Tab 中拒绝 AI 建议 |
| Ctrl/⌘ + → | 在 Cursor Tab 中逐字部分接受 AI 建议 |
| Ctrl/⌘ + Enter | 接受已应用的代码块更改 |
| Ctrl/⌘ + Backspace | 拒绝已应用的代码块更改 |

注意：在 Windows/Linux 上，使用 Ctrl 键代替 ⌘ (Command) 键。

1\. 从 VS Code 迁移
----------------

Cursor 是 VS Code 的一个分支，因此它提供了从 VS Code 迁移的简便方法。

**主要特点：** 

*   一键导入 VS Code 配置
    
*   支持导入扩展、主题、设置和键绑定

**使用方法：** 

*   导航到 Cursor 设置 > 通用 > 帐户
    
*   使用一键导入功能

**示例：** 如果你在 VS Code 中有自定义的颜色主题和键绑定，你可以轻松地将它们导入到 Cursor 中，使得转换过程更加顺畅。

2\. Cursor Tab（自动完成）
--------------------

Cursor Tab 是 Cursor 的原生自动完成功能，比 GitHub Copilot 更强大，能够提供整个差异建议，并具有特别好的记忆能力。

**主要特点：** 

*   可以在光标周围进行编辑，而不仅仅是插入额外的代码
    
*   可以一次修改多行
    
*   基于您最近的更改和 linter 错误提供建议

**使用方法：** 

*   接受建议：按 Tab 键
    
*   拒绝建议：按 Esc 键或继续输入
    
*   逐字接受建议：按 Ctrl/⌘ + →

### 使用 Cursor 预测功能进行快速编辑

**技巧描述**：Cursor 可以预测你在接受一个编辑后可能会去的下一个位置，允许你快速连续进行多个编辑。

**使用方法**：

1.  接受一个 Cursor 建议
    
2.  如果有下一个预测位置，可以再次按 Tab 键跳转并编辑
    
3.  连续按 Tab 键可以在多个预测位置之间跳转

**示例场景**：快速重构一个类的多个方法。

3\. Cursor Chat（AI 聊天）
----------------------

Cursor Chat 允许你在编辑器中使用最先进的语言模型提问或解决问题。

**主要特点：** 

*   自动包含整个代码库的上下文
    
*   可以搜索网络
    
*   可以索引文档
    
*   支持用户指定的代码块引用

**使用方法：** 

*   打开 AI 面板：按 Ctrl/⌘ + L
    
*   提交查询：在输入框中输入后按 Enter
    
*   切换 AI 模型：按 Ctrl/⌘ + /

4\. Cmd K（代码生成和编辑）
------------------

Cmd K（在 Windows/Linux 上是 Ctrl K）允许你在编辑器窗口中生成新代码或编辑现有代码。

**主要特点：** 

*   内联生成：在未选择代码时生成新代码
    
*   内联编辑：选择代码后进行编辑
    
*   支持跟进指令：可以进一步细化提示

**使用方法：** 

*   按 Ctrl/⌘ + K 打开提示栏
    
*   输入指令并按 Enter 生成或编辑代码
    
*   使用 @ 符号引用其他上下文

5\. 代码库索引
---------

代码库索引功能可以提高使用 @codebase 或 Ctrl/⌘ + Enter 时的代码库答案的准确性。

**主要特点：** 

*   自动同步最新的代码库更改
    
*   可配置忽略特定文件
    
*   支持项目特定的索引设置

**使用方法：** 

*   在 Cursor 设置 > 功能 > 代码库索引中启用
    
*   **使用 .cursorignore 文件排除不需要索引的文件**

**示例：** 假设你有一个大型项目，但不想索引 dist 目录和日志文件，你可以创建一个 .cursorignore 文件：

``# 忽略所有在 `dist` 目录中的文件  
Dist/  
# 忽略所有 `.log` 文件  
*. Log  
``

![](https://mmbiz.qpic.cn/mmbiz_png/VzoLjU1b4dibD5rXbSXs6wrCUfFIicHqN7tphiavDLk6LRC4BlibJDlGofgBIpkK9LgTCW0ZKFMlaTReH8Ye30VQWA/640?wx_fmt=png&from=appmsg)

6\. 结合 Cmd K 和 AI 审查进行代码重构
--------------------------

**方法**：在 Cursor 设置中启用 AI 审查功能，使用 Cmd K 生成重构建议，然后使用 AI 审查验证更改。

**步骤**：

1.  选择需要重构的代码块
    
2.  使用 Cmd K 请求重构建议
    
3.  应用更改
    
4.  运行 AI 审查检查潜在问题

**示例 Cmd K 提示**：

`重构这段代码以提高性能和可读性，使用现代 JavaScript 特性  
`

![](https://mmbiz.qpic.cn/mmbiz_png/VzoLjU1b4dibD5rXbSXs6wrCUfFIicHqN7Oic0P5zXk2jZU19SALRLd58fsZP8rKMhju8JqDSmlNYrMicUbR2VjVhg/640?wx_fmt=png&from=appmsg)

7\. 隐私模式
--------

隐私模式确保你的代码不会被 Cursor 或任何第三方存储（OpenAI 除外，他们出于信任和安全原因会保留提示 30 天，除非你使用商业计划）。

**主要特点：** 

*   防止代码被存储
    
*   仍然允许使用 AI 功能
    
*   适用于处理敏感数据的项目

**使用方法：** 

*   在 Cursor 设置 > 通用 > 隐私模式中启用

![](https://mmbiz.qpic.cn/mmbiz_png/VzoLjU1b4dibD5rXbSXs6wrCUfFIicHqN73WzoR1AA2C9JyowTdKQyj3gyn4J6eYnDQaWaLXiaphiauspxZXWl417A/640?wx_fmt=png&from=appmsg)

8\. 自定义 API 密钥
--------------

Cursor 允许你使用自己的 API 密钥，以便以自己的成本发送无限量的 AI 消息。

**支持的 API：** 

*   OpenAI API
    
*   Anthropic API
    
*   Google API
    
*   Azure OpenAI

**使用方法：** 

*   在 Cursor 设置 > 模型中输入相应的 API 密钥
    
*   点击 "验证" 按钮以确认密钥有效

注：

1.  可以把 Groq 的 API 和 base URL 设置到 OpenAI API 那栏。
    
2.  使用 Gemini API。
    
3.  以上两个 API 都是免费的。
    
4.  需要注意，用 Groq 的 API，需要添加并选择 Groq 里对应的模型，其他的模型要关掉。用 Gemini 模型时，也要关掉 OpenAI 的设置，可以和 Cursor 收费的模型共存。
    
5.  当然，你也可以用 Deepseek 的 API 或其他和 OpenAI 接口兼容的 API。

![](https://mmbiz.qpic.cn/mmbiz_png/VzoLjU1b4dibD5rXbSXs6wrCUfFIicHqN78DuosFF3Qv6630OhmTHwWa2mAeuQkUAzslm7tNGPGpfOicRtNTEfPqA/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/VzoLjU1b4dibD5rXbSXs6wrCUfFIicHqN7jAohhDY3c3iboUFCgUIbCSPWmxFOb0kljuzQBeXN23on5eS1ibfMVYHQ/640?wx_fmt=png&from=appmsg)

9\. 模型选择
--------

**可用模型：** 

*   GPT-4 o
    
*   Claude 3.5 Sonnet
    
*   cursor-small（Cursor 的自定义模型）
    
*   长上下文模型（如 gpt-4 o-128 k, gemini-1.5-flash-500 k 等）

**使用方法：** 

*   在 AI 输入框下方使用模型下拉菜单选择模型
    
*   使用 Ctrl/⌘ + / 快捷键在模型之间切换

**示例：** 对于简单的代码补全任务，你可能会选择更快的 cursor-small 模型：

`def greet(name):  
    # cursor-small 可能会快速补全这个函数  
    Return f"Hello, {name}!"  
`

而对于更复杂的任务，你可能会选择 GPT-4 o 或 Claude 3.5 Sonnet。

10\. 长上下文聊天（测试版）
----------------

长上下文聊天允许你在聊天中包含更大的上下文窗口，从而处理更复杂的问题和更大的代码库。

**主要特点：** 

*   支持包含整个文件夹作为上下文
    
*   使用具有更大上下文窗口的模型

**使用方法：** 

*   在 Cursor 设置 > 测试版 > 长上下文聊天中启用
    
*   使用 Ctrl/⌘ + . 切换不同的聊天模式

**示例：** 在长上下文聊天中，你可以询问关于整个项目结构的问题：

`请分析我们项目中所有 JavaScript 文件的依赖关系，并提出可能的优化建议。  
`

11\. 终端 Cmd K
-------------

在 Cursor 内置终端中，你可以使用 Cmd K（Windows/Linux 上是 Ctrl K）来生成终端命令。

**主要特点：** 

*   根据描述生成终端命令
    
*   可以查看最近的终端历史作为上下文

**使用方法：** 

*   在终端中按 Ctrl/⌘ + K 打开提示栏
    
*   描述你想要执行的操作
    
*   使用 Esc 接受命令，或 Ctrl/⌘ + Enter 立即运行命令

**示例：** 你可以在提示栏中输入："查找所有大于 100 MB 的文件并列出它们的大小" Cursor 可能会生成如下命令：

`find . -type f -size +100M -exec du -h {} + | sort -rh  
`

**这个功能很好用，类似 Warp AI 的效果，直接输出命令，少废话，快捷键直接运行。** 

12\. 自定义 AI 规则
--------------

你可以为 Cursor 添加自定义指令，这些指令将应用于 Cursor Chat 和 Ctrl/⌘ K 等功能。

**主要特点：** 

*   可以设置**全局规则**
    
*   支持项目**特定的规则**

**使用方法：** 

*   全局规则：在 Cursor 设置 > 通用 > AI 规则中修改
    
    ![](https://mmbiz.qpic.cn/mmbiz_png/VzoLjU1b4dibD5rXbSXs6wrCUfFIicHqN7xQpicuJZC0SDjibP1c30ysibCZalUeawTMceZnT32kIJDXG5tBnXjW15A/640?wx_fmt=png&from=appmsg)
    
*   项目特定规则：在项目根目录创建 .cursorrules 文件

**示例：** 在 .cursorrules 文件中添加：

`始终使用 TypeScript 类型注解  
遵循 Angular 风格指南  
使用函数式编程范式  
注释应该解释为什么，而不是如何  
`

13\. 应用代码块
----------

Cursor 的应用功能允许你快速将聊天中的代码块建议集成到你的代码中。

**主要特点：** 

*   可以直接从聊天中应用代码更改
    
*   支持接受或拒绝各个更改

**使用方法：** 

*   点击聊天中代码块右上角的播放按钮
    
*   使用 Ctrl/⌘ + Enter 接受更改
    
*   使用 Ctrl/⌘ + Backspace 拒绝更改

14\. 使用 Slash Edit 命令进行快速编辑
---------------------------

**技巧描述**：利用 `/edit` 命令快速描述并实现对当前文件的更改。

**使用方法**：

1.  在聊天输入框中输入 `/edit`
    
2.  描述你想对当前文件进行的更改
    
3.  Cursor 会使用专门的模型来实现这些更改，跳过未更改的部分以提高响应速度

**示例命令**：

`/edit 将所有 for 循环重构为 map 和 filter 操作  
`

15\. 利用网页搜索增强 AI 回答
-------------------

**技巧描述**：启用网页搜索功能，让 AI 在回答问题时能够获取最新信息。

**使用方法**：

1.  在 Cursor 设置 > 功能 > 聊天中启用 "始终搜索网页寻找答案"
    
2.  在聊天中提问时，AI 会自动搜索网页以获取最新信息

**示例场景**：询问关于最新技术趋势或刚发布的库的问题。

