在 Mac 电脑上设置 npm 的源，您可以使用以下方法：
1. **使用命令行设置淘宝源**：
   打开终端，然后使用以下命令设置 npm 的源为淘宝镜像源：
   ```
   npm config set registry https://registry.npm.taobao.org
   ```
   设置完成后，您可以通过以下命令验证是否成功：
   ```
   npm config get registry
   ```
   或者
   ```
   npm info express
   ```
   如果您想清除已设置的淘宝镜像，可以使用以下命令：
   ```
   npm config delete registry
   npm config delete disturl
   ```
   或者打开配置文件编辑：
   ```
   npm config edit
   ```
   在文件中找到与淘宝相关的行并删除。
2. **使用 `.npmrc` 文件修改源**：
   打开终端，切换到根路径，然后执行以下命令：
   ```
   open .npmrc
   ```
   或者
   ```
   vim .npmrc
   ```
   在打开的文件中，输入以下命令更换国内源：
   ```
   npm config set registry https://registry.npmmirror.com/
   ```
   若要换回默认源，使用以下命令：
   ```
   npm config set registry https://registry.npmjs.org/
   ```
3. **使用 `nrm` 切换镜像源**：
   `nrm` 是一个 npm 源管理器，可以方便地切换和查看 npm 镜像源。首先安装 `nrm`：
   ```
   npm install nrm -g
   ```
   然后使用以下命令查看所有镜像源或当前使用的源：
   ```
   nrm ls
   ```
   切换到淘宝源可以使用：
   ```
   nrm use taobao
   ```
以上方法适用于 npm、yarn 和 pnpm。选择适合您需求的方法进行设置即可。
