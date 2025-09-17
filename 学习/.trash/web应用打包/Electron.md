不必须全局安装 Electron。你可以在你的项目中作为依赖项安装 Electron，这样可以避免全局安装带来的版本管理问题。以下是如何在项目中局部安装 Electron 的步骤：

### 1. 在 Vue 项目中安装 Electron
在你的 Vue 项目的根目录中，使用以下命令安装 Electron：

```bash
npm install electron --save-dev
```

### 2. 创建 `main.js` 文件
在项目根目录下创建一个 `main.js` 文件，内容如下：

```javascript
const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), // 可选，如果不需要可以去掉
    },
  });

  win.loadURL('file://' + path.join(__dirname, 'dist/index.html')); // 指向 Vue 项目打包后的文件
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
```

### 3. 更新 `package.json`
在 `package.json` 中添加启动脚本：

```json
"scripts": {
  "start": "electron ."
}
```

### 4. 打包 Vue 项目
在运行 Electron 之前，确保你的 Vue 项目已经被打包。使用以下命令打包 Vue 项目：

```bash
npm run build
```

### 5. 运行 Electron 应用
在项目根目录中，运行以下命令启动 Electron 应用：

```bash
npm start
```

### 6. 打包成可执行文件
要将应用打包成可执行文件，可以使用 `electron-builder` 或 `electron-packager`。以 `electron-builder` 为例：

1. 安装 `electron-builder`：

   ```bash
   npm install electron-builder --save-dev
   ```

2. 在 `package.json` 中添加构建配置：

   ```json
   "build": {
     "appId": "com.example.yourapp",
     "mac": {
       "target": "dmg"
     },
     "win": {
       "target": "nsis"
     }
   }
   ```

3. 添加打包脚本：

   ```json
   "scripts": {
     "build": "vue-cli-service build",
     "dist": "electron-builder"
   }
   ```

4. 运行打包命令：

   ```bash
   npm run dist
   ```

这样，你就可以生成适用于 Mac 和 Windows 的可执行文件了！