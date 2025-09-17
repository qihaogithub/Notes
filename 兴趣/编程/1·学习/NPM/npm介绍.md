NPM（Node Package Manager）是一个JavaScript编程语言的包管理器，用于Node.js环境。它允许开发者安装、共享和管理具有重复使用价值的代码包，也就是我们常说的"模块"或"库"。以下是一份

## 1. 什么是NPM？
- **NPM** 是Node.js的包管理器，用于管理项目依赖。
- 它允许用户安装、更新和管理项目所需的第三方库。

## 2. NPM的安装
- 安装Node.js时，NPM通常会自动安装。
- 可以通过访问[Node.js官网](https://nodejs.org/)下载安装包。

## 3. 使用NPM
- **命令行界面**：NPM主要通过命令行界面（CLI）使用。

## 4. 常用NPM命令
- `npm init`：初始化一个新的Node.js项目，创建`package.json`文件。
- [[npm install]]：安装项目依赖
- `npm uninstall <package>`：卸载一个包。
- `npm update <package>`：更新一个包到最新版本。
- `npm list`：列出安装的包。
- `npm cache clean`：清除缓存。



## 5. package.json
- 项目的配置文件，记录项目依赖和元数据。
- 包含`dependencies`和`devDependencies`字段。

## 6. 依赖版本
- 依赖版本号通常遵循语义化版本控制（SemVer）规则。
- 例如：`1.0.0`，其中1是主版本号，0是次版本号，0是补丁号。

## 7. npm scripts
- 在`package.json`中定义脚本，可以通过`npm run <script>`执行。
- 常用于自动化测试、构建等任务。

## 8. npm配置
- 可以通过`npm config`命令设置NPM的配置选项。

## 9. npm registry
- NPM使用注册表来存储包的元数据。
- 默认使用[npmjs.com](https://www.npmjs.com/)作为公共注册表。

## 10. 私有包和组织
- 可以在私有注册表上发布私有包。
- 支持组织和团队协作。

## 11. 环境变量
- NPM支持环境变量，可以在脚本中使用。

## 12. 安全性
- 使用`npm audit`检查项目依赖中的安全漏洞。
- 使用`npm outdated`查看过时的包。

## 13. npm的替代品
- Yarn：Facebook开发的包管理器，与NPM类似但有一些性能优势。

## 14. 进阶使用
- 使用`npm link`在本地开发包。
- 使用`npm dedupe`减少依赖的重复。

