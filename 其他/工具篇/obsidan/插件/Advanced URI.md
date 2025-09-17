---
介绍: 允许您通过打开一些 URI 来控制黑曜石中的许多不同特性
评级: "1"
---

[Documentation](https://vinzent03.github.io/obsidian-advanced-uri)

## 概述

[Obsidian Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) 允许您控制obsidan中的许多不同功能，只需打开一些 URI。因为它们只是文本，不需要任何鼠标点击或键盘输入，它们非常适合自动化您的黑曜石工作流程。

例如
- [打开文件](https://vinzent03.github.io/obsidian-advanced-uri/actions/navigation)
- [编辑文件](https://vinzent03.github.io/obsidian-advanced-uri/actions/writing)
- [创建文件](https://vinzent03.github.io/obsidian-advanced-uri/actions/writing)
- [开放式工作区](https://vinzent03.github.io/obsidian-advanced-uri/actions/navigation)
- [打开书签](https://vinzent03.github.io/obsidian-advanced-uri/actions/bookmarks)
- [导航到标题/块](https://vinzent03.github.io/obsidian-advanced-uri/actions/navigation)
- [在文件中自动搜索和替换](https://vinzent03.github.io/obsidian-advanced-uri/actions/search)
- [调用命令](https://vinzent03.github.io/obsidian-advanced-uri/actions/commands)
- [从frontmatter编辑和阅读](https://vinzent03.github.io/obsidian-advanced-uri/actions/frontmatter)
- and much more

请阅读[文档](https://vinzent03.github.io/obsidian-advanced-uri)以了解详细的解释。

## Examples

### 将剪贴板中的内容附加到今天的日记中
```uri
obsidian://advanced-uri?vault=<your-vault>&daily=true&clipboard=true&mode=append
```

### 调用命令
```uri
obsidian://advanced-uri?vault=<your-vault>&filepath=<your-file>&commandid=workspace%253Aclose
```

### 文件中的打开标题
```uri
obsidian://advanced-uri?vault=<your-vault>&filepath=my-file&heading=Goal
```

