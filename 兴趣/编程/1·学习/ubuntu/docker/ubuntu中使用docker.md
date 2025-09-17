在Ubuntu系统中使用Docker，你需要先确保Docker已经安装在你的系统上。以下是安装和使用Docker的基本步骤：

1. **安装Docker**：
   - 首先，更新你的包索引：
     ```bash
     sudo apt update
     ```
   - 安装Docker：
     ```bash
     sudo apt install docker.io
     ```
   - 验证Docker是否安装成功：
```bash
 sudo docker --version
```

2. **添加用户到docker组**：
   - 为了不使用`sudo`来运行Docker命令，你可以将你的用户添加到docker组：
```bash
sudo usermod -aG docker $USER
```
   - 然后，注销并重新登录以使组更改生效。

3. **运行Docker容器**：
   - 拉取一个Docker镜像（例如，Ubuntu镜像）：
     ```bash
     sudo docker pull ubuntu
     ```
   - 运行一个Docker容器：
     ```bash
     sudo docker run -it ubuntu /bin/bash
     ```
     这将启动一个新的Ubuntu容器，并打开一个bash会话。

4. **管理Docker容器**：
   - 列出所有运行中的容器：
     ```bash
     sudo docker ps
     ```
   - 列出所有容器（包括停止的）：
     ```bash
     sudo docker ps -a
     ```
   - 停止一个容器：
     ```bash
     sudo docker stop [容器ID或名称]
     ```
   - 删除一个容器：
     ```bash
     sudo docker rm [容器ID或名称]
     ```

5. **查看Docker镜像**：
   - 列出所有镜像：
     ```bash
     sudo docker images
     ```
   - 删除一个镜像：
     ```bash
     sudo docker rmi [镜像ID或名称]
     ```

6. **构建Docker镜像**：
   - 创建一个`Dockerfile`，这是一个文本文件，包含了所有构建Docker镜像所需的指令。
   - 使用`docker build`命令来构建镜像：
     ```bash
     sudo docker build -t [镜像名称] .
     ```
     这里的`.`指的是Dockerfile所在的当前目录。

7. **Docker Compose**：
   - 对于需要多个容器的复杂应用，可以使用Docker Compose来定义和运行多容器Docker应用程序。
   - 安装Docker Compose：
     ```bash
     sudo apt install docker-compose
     ```
   - 创建一个`docker-compose.yml`文件来定义你的服务，然后使用`docker-compose up`来启动所有服务。

请注意，这些步骤可能会随着Docker版本的更新而有所变化，所以最好查看Docker的官方文档以获取最新的安装和使用指南。
