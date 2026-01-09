# Git  rm --cached  命令

## 简介
`git rm --cached` 是一个 Git 命令，用于从 Git 的索引中移除文件或目录，但不会删除它们在本地文件系统中的副本。这个命令常用于撤销之前的 `git add` 操作，或者从版本控制中移除已经跟踪的文件，同时保留在本地。

例如下面代码，可删除跟踪，但不删除文件
```
git rm -r --cached .obsidian/plugins/recent-files-obsidian
```

## 使用场景
- 当你不小心将某个文件添加到版本控制中，但实际上你不想跟踪这个文件时。
- 当你想要从版本控制中移除一个目录及其所有文件，但还想保留它们在本地时。

## 语法
git rm --cached <file_or_directory>

- `--cached`：告诉 Git 我们只想从索引中移除文件，而不是从工作目录中删除。
- `<file_or_directory>`：要移除的文件或目录的路径。

### 文件
如果你想移除一个文件，命令如下：
git rm --cached important_document.txt

### 目录
如果你想递归地移除一个目录及其所有内容，需要使用 `-r` 选项：
git rm --cached -r some_directory/

## 提交更改
移除文件或目录后，需要提交这个更改，以便它们不再被版本控制系统跟踪：
  
git commit -m "Removed <file_or_directory> from tracking"

## 推送到远程仓库
如果需要将这个更改推送到远程仓库，使用：
git push origin <branch_name>

## 注意事项
- 使用 `git rm --cached` 之前，请确保你不想保留该文件或目录在版本历史中的记录。
- 如果文件或目录已经被推送到远程仓库，你可能需要先在本地执行上述操作，然后再推送到远程。
- 如果你只是想忽略未跟踪的文件，而不是从索引中移除已跟踪的文件，应该使用 `.gitignore` 文件。

## 结语
`git rm --cached` 是一个简单但强大的命令，可以帮助你精细控制哪些文件被版本控制系统跟踪。正确使用这个命令，可以避免不必要的文件被错误地包含在版本历史中。