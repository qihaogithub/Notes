要使用 `pkg` 将你的 Node. Js Web 项目打包为一个可以在 macOS 和 Windows 上运行的独立可执行文件，可以按照以下步骤操作：

### 1. 安装 `pkg`
首先，确保你已经安装了 `pkg`。你可以全局安装它：

```bash
npm install -g pkg
```

### 2. 创建 `package.json` 文件
确保你的项目中有一个 `package.json` 文件，定义了项目的入口文件。例如：

```json
{
  "name": "my-web-app",
  "version": "1.0.0",
  "main": "script.js",  // 替换为你的入口文件
  "scripts": {
    "start": "node script.js"
  },
  "bin": "script.js" // 让 pkg 知道入口文件
}
```

### 3. 修改代码以适应独立运行
确保你的 `script.js` 文件能够独立运行，并且不依赖本地文件系统中的任何模块（除了 Node. Js 内置模块和你打包时指定的依赖项）。如果你的项目中有静态文件，如 HTML、CSS、JavaScript 文件，你可能需要调整代码，将这些文件正确包含到包中。

### 4. 打包项目
使用 `pkg` 命令来打包你的项目：

```bash
pkg . --targets node18-macos-x64,node18-win-x64
```

- `.` 表示你要打包当前目录的项目。
- `--targets` 参数指定了目标平台，这里我们指定了 macOS 和 Windows 的 x 64 架构，使用的是 Node. Js 18 版本。

`pkg` 将生成两个独立的可执行文件，分别用于 macOS 和 Windows。

### 5. 分发可执行文件
一旦打包完成，你会在项目目录中找到生成的可执行文件：

- `my-web-app-macos`
- `my-web-app-win.exe`

你可以将这些文件分发给你的用户，Mac 用户可以直接运行 `my-web-app-macos`，Windows 用户可以直接运行 `my-web-app-win.exe`，无需安装 Node. Js 或其他依赖。



## 报错处理
[[端口被占用]]
[[如何让打包后的文件运行后自动在浏览器打开]]
