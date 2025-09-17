使用 rsync 传输文件
```bash
rsync -avz path/to/your/vue-project/dist/* username@your-ubuntu-server:/var/www/your-website
```

```
rsync -avz /Volumes/祁昊ssd/工作/网站/vue/uiweb/dist/* qihao@10.130.35.137:/var/www/uipreview
```

这个命令是使用 `rsync` 工具来同步文件和目录的命令。下面是对这个命令各个部分的解释：

- `rsync`：这是用于在本地和远程机器之间同步文件的命令行工具。
- `-avz`：这是命令行选项的组合，分别代表：
    - `-a`：归档模式，这会保留文件的权限、所有权、时间戳、软链接等元数据，并且递归地复制目录。
    - `-v`：详细模式，提供更多的输出信息，这样你可以看到传输过程中的详细信息。
    - `-z`：压缩数据，在传输过程中通过压缩来节省带宽和时间。
- `path/to/your/vue-project/dist/*`：这是源路径，表示你想要同步的本地文件或目录。在这个例子中，它指的是你的 Vue 项目构建生成的 `dist` 目录下的所有文件。
- `username@your-ubuntu-server:/var/www/your-website`：这是目标路径，指定了远程服务器的用户名、服务器地址以及服务器上你想要将文件同步到的目录。你需要替换 `username` 和 `your-ubuntu-server` 为实际的远程登录用户名和服务器地址。
整个命令的作用是：以归档模式、详细输出和压缩数据的方式，将本地 Vue 项目构建的 `dist` 目录下的所有文件同步到远程 Ubuntu 服务器的 `/var/www/your-website` 目录下。这样做可以确保你的网站文件被安全、高效地传输到服务器上，并准备好供 Apache 服务器提供网页服务。