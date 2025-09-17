`pm2` 是一个流行的 Node.js 应用程序的进程管理器，它允许你轻松地管理应用程序的生命周期。以下是如何使用 `pm2` 查看服务状态、启动、停止、重启和删除服务的命令：

1. **查看当前所有服务**：
   使用 `pm2 list` 或 `pm2 ls` 命令来查看所有正在运行的应用程序（服务）。
   ```bash
   pm2 list
   ```
   或者
   ```bash
   pm2 ls
   ```

2. **启动服务**：
   使用 `pm2 start` 命令来启动应用程序。如果你有一个应用程序的配置文件（通常是 `ecosystem.config.js`），可以直接使用该文件启动。
   ```bash
   pm2 start [应用名称或路径]
   ```
   例如，启动一个名为 `temppix` 的应用程序：
   ```bash
   pm2 start temppix
   ```

3. **停止服务**：
   使用 `pm2 stop` 命令来停止一个正在运行的应用程序。
   ```bash
   pm2 stop [应用名称]
   ```
   例如，停止 `temppix`：
   ```bash
   pm2 stop temppix
   ```

4. **重启服务**：
   使用 `pm2 restart` 命令来重启一个应用程序。
   ```bash
   pm2 restart [应用名称]
   ```
   例如，重启 `temppix`：
   ```bash
   pm2 restart temppix
   ```

5. **删除服务**：
   使用 `pm2 delete` 或 `pm2 del` 命令来删除一个应用程序，这将停止该应用程序并从 PM2 的进程列表中移除它。
   ```bash
   pm2 delete [应用名称]
   ```
   或者
   ```bash
   pm2 del [应用名称]
   ```
   例如，删除 `temppix`：
   ```bash
   pm2 delete temppix
   ```

6. **查看单个服务的详细信息**：
   使用 `pm2 describe` 命令来查看特定应用程序的详细信息。
   ```bash
   pm2 describe [应用名称]
   ```

7. **查看日志**：
   使用 `pm2 logs` 命令来查看所有应用程序的日志，或者使用 `pm2 logs [应用名称]` 来查看特定应用程序的日志。
   ```bash
   pm2 logs
   ```
   或者
   ```bash
   pm2 logs [应用名称]
   ```

8. **监控服务**：
   使用 `pm2 monit` 命令来监控应用程序的资源使用情况。

请注意，使用 `pm2` 命令时，你可能需要具有相应的权限，特别是在生产环境中，可能需要使用 `sudo` 来执行这些命令。例如，使用 `sudo` 来以 `www-data` 用户身份执行 `pm2` 命令：
```bash
sudo -u www-data pm2 restart temppix
```

这将确保 `pm2` 命令以 `www-data` 用户的权限执行，这对于在某些服务器配置中管理应用程序是必要的。
