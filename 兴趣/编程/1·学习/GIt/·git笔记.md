[菜鸟git 教程](https://www.runoob.com/git/git-basic-operations.html)

##  Git环境搭建
- **安装Git**
    - 操作系统的安装步骤
    - Git的安装和配置
- **Git的基本概念**
    - 仓库（Repository）
    - 分支（Branch）
    - 提交（Commit）
## 创建和初始化仓库
- **创建新仓库**
    - 使用`git init`命令
    - 仓库结构
- **初始化仓库**
    - 使用`git init`命令
    - 仓库初始化与配置
## 基本操作

### **添加文件**
#### 使用 `git add` 命令
1. **添加单个文件**：
    `git add <filename>`
    其中 `<filename>` 是你想要添加到暂存区的文件名。 ^s7jguv
2. **添加多个文件**：
    `git add <filename1> <filename2> ...`
    你可以在 `git add` 命令后面列出所有你想要添加的文件名。
3. **添加整个目录**：
    `git add <directory>/`
    或者使用通配符添加目录下的所有文件：
    `git add <directory>/*`
4. **添加所有更改（包括新文件和修改过的文件）**：
    `git add .`
    这个命令会将当前目录及其子目录下的所有更改添加到暂存区。
#### 暂存更改
**提交更改**
    使用`git commit`命令
    提交信息的编写
**查看状态**
    使用`git status`命令
    状态显示的解释

| git init                                   | 初始化本地仓库             |
| ------------------------------------------ | ------------------- |
| git clone                                  | 拷贝一份远程仓库，也就是下载一个项目。 |
| git status                                 | 查看本地库状态             |
| git add 文件名                                | 添加暂存区               |
| [[git commit]] -m “日志信息” 文件名              | 提交本地库               |
| git reset --hard origin/branch_        ame | 重置本地分支              |
| git checkout                               | 丢弃工作目录中的未提交更改       |
| git reset HE                               | 清除暂存区的更改            |

**重置本地分支（Reset Local Branch）** 使用 `git reset` 命令将本地分支的HEAD指针指向特定的远程分支的状态。这将重置本地分支，但不会影响本地的工作目录。
`git reset --hard origin/branch_name`
其中 `branch_name` 是你想要同步的远程分支的名称。
    
**清理本地更改（Clean Local Changes）** 如果你的本地工作目录中有未提交的更改或暂存区的更改，你需要先清理这些更改，以确保完全覆盖。

丢弃工作目录中的未提交更改：
`git checkout -- .`

清除暂存区的更改：
`git reset HEAD .`

###  忽略文件 .gitignore
忽略文件常见格式

```yaml
# 所有以.a 结尾的文件讲被忽略(递归)
*.a
# 不管其他规则怎样,强制不忽略  lib.a
!lib.a
# 只忽略 文件 TODO (注意这里是文件)
/TODO
# 忽略 build文件夹下所有内容(递归) 这里是文件夹
build/
# 忽略 doc 目录下以 *.txt 结尾的文件 (不递归)
doc/*.txt
# 忽略 doc 目录下以 *.pdf 结尾的文件 (递归)
doc/**/*.pdf
```

编辑.gitignore 文件后，需要继续处理才能生效，分一下几种情况：

1、**文件已被跟踪**：
	如果文件在 .gitignore 更新之前已经被 Git 跟踪，那么这些文件仍然会被 Git 跟踪，直到你明确地告诉 Git 停止跟踪它们。你需要使用以下命令来停止跟踪这些文件：
	`git rm --cached <file>`
2、**目录已被跟踪**：如果是一个目录及其内部文件需要被忽略，你可能需要递归地停止跟踪：
	`git rm -r --cached <directory>`
3、**检查 .git/info/exclude**
	有时候 Git 会在这个文件中记录一些需要忽略的路径，这可能会覆盖 `.gitignore` 的设置。
4、**检查 .gitattributes文件**
	`.gitattributes` 文件可以覆盖 `.gitignore` 的设置，确保没有冲突
5、**清理缓存**：
	有时候清理 Git 缓存可以解决问题：
	`git gc --prune=now` 
	`git remote prune origin`
6、添加跟踪
	[[#使用 git add 命令| git add]]
	若要添加的跟踪已经被忽略，可以使用使用 -f 参数
	git add -f  {file}

[[从 Git 的索引中移除文件或目录]]

## 分支管理

列出分支 

```
git branch
```

- **创建分支**
    - 使用`git branch`命令
    - 分支的命名规则

```
git branch 分支名称
```

- **切换分支**
    - 使用`git checkout`命令
    - 分支切换的注意事项

```
# git checkout 分支名称
```

创建新分支并切换

```
git checkout -b 分支名称
```

删除分支

```
git branch -d 分支名称
```

分支合并
第一步：切换到想要合并到的分支，例如切换到master

```
git checkout master
```

第二步：将某个分支合并到master

```
git merge 分支名称
```

### 修改本地分支名称

1. 使用 `git branch -m` 命令重命名一个分支。例如，将本地分支 `feature` 重命名为 `new-feature`：
    
    `git branch -m feature new-feature`
    
    或者使用以下简写形式：
    
    `git branch -m new-feature feature`
    
2. 如果要重命名当前所在的分支，可以使用 `-m` 后跟新分支名：
    
    `git branch -m new-feature`

### 修改远程分支名称

1. 首先，重命名本地分支，然后推送到远程仓库：
    
    `git branch -m old-branch-name new-branch-name git push origin -m new-branch-name`
    
    这里的 `old-branch-name` 是要修改的分支的旧名称，`new-branch-name` 是新的分支名称。
    
2. 如果你只想在远程仓库中重命名分支，而不修改本地分支名称，可以使用以下命令：
    
    `git push origin :old-branch-name new-branch-name`
    
    这条命令会告诉Git先删除远程的 `old-branch-name` 分支，然后以 `new-branch-name` 的名称推送当前分支。

## 远程仓库

| git fetch origin --force             | 强制拉取   |
| ------------------------------------ | ------ |
| git push origin branch_name --force  | 强制推送   |
| git pull origin branch_name --rebase | 拉取远程分支 |
|                                      |        |

**强制拉取（Forced Fetch）** 使用 `git fetch` 命令配合 `--force` 或 `--update-head-ok` 选项强制更新本地分支，使其与远程分支同步。但请注意，这种方法并不常用，因为它会重写本地的分支历史。
`git fetch origin --force`

**拉取远程分支（Pull Remote Branch）** 在清理了本地更改之后，你可以使用 `git pull` 命令拉取远程分支的内容。如果你想要避免合并，可以使用 `--rebase` 选项进行变基操作。
`git pull origin branch_name --rebase`

**强制推送（Forced Push）** 如果你在本地进行了重置或清理操作，并且想要将这些更改推送到远程仓库，你需要使用 `--force` 选项强制推送。
`git push 远程仓库名称 本地分支名称 --force`
远程仓库名称一般都是origin

## 提交与修改

[[git push 命令]]

## 异常处理
- **解决冲突**
    - 冲突的识别
    - 冲突的解决策略
- **修复错误**
    - 使用`git checkout`命令修复错误
    - 修复错误的注意事项

### 重置当前分支
使用 `git reset` 命令将当前分支重置为远程分支的状态。这将重置你的本地分支的指针到 `origin/master` 的状态，但不会影响工作目录中的文件。
    
    `git reset --hard origin/master`
    
这个命令会重置当前分支的 HEAD 到 `origin/master` 的状态，并且会重置暂存区和工作目录，使其与 `origin/master` 相匹配。这意味着所有本地分支的更改将会丢失，因此请确保在执行此操作之前备份任何重要的本地更改。

### 提交消息不符合 `commitlint` 的规则
`commitlint`是一个用于确保你的提交消息遵循约定式提交格式的工具。根据你提供的错误信息，具体的问题如下：

1. `subject may not be empty [subject-empty]`：这表明提交消息的主题部分不能为空。在约定式提交格式中，主题是紧随类型（type）和作用域（scope）之后的简短描述。

2. `type may not be empty [type-empty]`：这表明提交消息的类型部分不能为空。类型是用于描述提交目的的关键字，比如`feat`（新特性）、`fix`（修复）、`docs`（文档更新）等。

错误信息还提供了一个链接到`commitlint`的GitHub页面，那里有关于如何正确使用`commitlint`的详细信息。根据你提供的链接内容，`commitlint`期望的提交消息格式通常如下：

```
type(scope?): subject  #scope是可选的；支持多个作用域（当前分隔符选项："/", "\" 和 ","）
```

一些常见的类型包括：

- build
- chore
- ci
- docs
- feat
- fix 修复
- perf
- refactor
- revert
- style
- test

这些类型可以根据你自己的配置进行修改。

为了解决这个问题，你需要确保你的提交消息遵循这个格式。例如，如果你想要提交一个修复服务器端点的提交，你可以使用如下格式：

```
fix(server): send cors headers
```

如果你想要跳过`commitlint`的检查，可以在提交时添加`--no-verify`标志，但这通常不推荐，因为它会绕过你设置的提交规则，可能导致不规范的提交消息进入你的版本历史。

如果你正在使用`husky`作为Git钩子管理工具，确保你的`.husky/pre-commit`脚本配置了`commitlint`，并且你的提交消息符合`commitlint`的规则。如果你需要修改`commitlint`的配置，可以查看项目的`commitlint`配置文件，通常位于`.commitlintrc`或`commitlint.config.js`。

如果你不熟悉如何修复这个问题，你可能需要查看你的项目的 `commitlint` 配置，或者咨询项目维护者以获取帮助。

### 重写 Git 存储库历史
这条指令 `git filter-repo --force --invert-paths --path config/oss-config.js` 使用了 `git filter-repo` 工具，这是一个用于高效重写 Git 存储库历史的工具。具体来说，这个命令的目的是从 Git 仓库的提交历史中排除或包括某些文件或路径。现在，让我们详细解析这条命令的各个部分：

1. **git filter-repo**: 这是命令的主体，用于重写 Git 仓库的提交历史。
2. **--force**: 这个选项告诉 `git filter-repo` 强制执行操作，即使这可能导致数据丢失或覆盖现有提交。这通常用于确保命令会执行，即使它可能具有破坏性。
3. **--invert-paths**: 这个选项是关键。默认情况下，`--path` 选项会包含指定的路径。但是，使用 `--invert-paths` 会反转这个行为，即排除指定的路径，而不是包含它。换句话说，它会从提交历史中删除与指定路径相关的所有更改。
4. **--path config/oss-config.js**: 这个选项指定了要从提交历史中排除或包括的路径。但是，由于我们使用了 `--invert-paths`，所以这个路径会被排除。

综上所述，这条命令的意思是：“从 Git 仓库的提交历史中排除所有与 `config/oss-config.js` 路径相关的更改，并强制执行此操作。”

执行此命令后，所有包含对 `config/oss-config.js` 文件的更改的提交都将被重写，从而删除这些更改。这可以用于清理敏感信息、缩小仓库大小或其他需要删除特定文件或路径的更改的情况。但是，请注意，这个操作是破坏性的，并且会改变 Git 仓库的提交历史。在执行此操作之前，最好备份您的仓库，并确保您了解其潜在影响。

### 配置本地仓库的远程SSH形式URL 
如果你的仓库是通过HTTPS克隆的，你需要添加一个SSH形式的远程URL：

`git remote set-url origin git@github.com:username/repo.git`

### [[从 Git 的索引中移除文件或目录]]

## 版本控制进阶

- **标签管理**
    - 使用`git tag`命令
    - 标签的创建和使用
- **回退**
    - 使用`git reset`命令
    - 回退的注意事项
- **比较**
    - 使用`git diff`命令
    - 比较的用法

## 安全性

- **保护仓库**
    - 使用`.gitignore`文件
    - 仓库的权限设置
- **安全操作**
    - 避免敏感信息泄露
    - 保护仓库不被恶意攻击