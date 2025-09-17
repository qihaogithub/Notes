## Linux 权限管理：查看与修改

本篇笔记主要介绍如何在 Linux 系统中查看和修改用户、组以及文件/目录的权限。

### 查看用户和组

在 Linux 系统中，用户和组的管理至关重要。以下是一些常用的命令，用于查看用户和组的信息：

*   **查看所有用户:**
    ```bash
    cat /etc/passwd
    ```
    此命令会显示系统中所有用户的详细信息，包括用户名、用户ID (UID)、组ID (GID)、家目录和默认 Shell 等。

*   **查看所有组:**
    ```bash
    cat /etc/group
    ```
    此命令会显示系统中所有组的详细信息，包括组名、组ID (GID) 以及组成员。

*   **查看当前用户所属的组:**
    ```bash
    groups
    ```
    或
    ```bash
    id -Gn
    ```
    这两个命令都会显示当前用户所属的所有组。

*   **查看特定用户信息:**
    ```bash
    id <用户名>
    ```
    例如，`id user1` 将显示 `user1` 用户的详细信息，包括 UID、GID 以及所属组。

*   **查看特定组信息:**
    ```bash
    getent group <组名>
    ```
    例如，`getent group group1` 将显示 `group1` 组的详细信息，包括 GID 和组成员。

### 查看文件和目录权限

使用 `ls -l` 命令可以查看文件或目录的详细权限信息：
```bash
ls -l <文件或目录路径>
```
例如，要查看 `/var/www/site1` 的权限，可以使用命令 `ls -l /var/www/site1`。
输出结果会显示如下列信息：
```
drwxr-xr-x 2 user group 4096 Oct 26 10:00 directory
-rw-r--r-- 1 user group 1234 Oct 26 10:00 file.txt
```
第一列 `drwxr-xr-x` 或 `-rw-r--r--` 表示文件类型和权限:
- 第一个字符表示文件类型 (`d` 表示目录, `-` 表示文件)
- 接下来三位 `rwx` 表示所有者权限（读、写、执行）
- 再接下来三位 `r-x` 表示所属组权限
- 最后三位 `r-x` 表示其他用户权限
剩余列分别表示：
- 硬链接数
- 文件所有者
- 文件所属组
- 文件大小
- 最后修改时间
- 文件/目录名称

### 修改文件和目录权限

要修改文件和目录的权限，通常使用 `chown` 和 `chmod` 命令。
例如，要让 `qihao` 和 `www` 用户都能够对 `/www/wwwroot/gallery/jietu.library` 目录及其内容有读、写和执行权限，可以执行以下步骤：

1.  **更改所有者和组:**
    ```bash
    sudo chown -R www:www /www/wwwroot/gallery/jietu.library
    ```
    此命令将 `/www/wwwroot/gallery/jietu.library` 目录及其所有子目录和文件的所有者和组都更改为 `www`。 `-R` 选项表示递归更改。

2.  **更改权限:**
    ```bash
    sudo chmod -R 775 /www/wwwroot/gallery/jietu.library
    ```
    此命令将 `/www/wwwroot/gallery/jietu.library` 目录及其所有子目录和文件的权限都更改为 `775`。

    *   **775 权限解释:**
        *   **7 (所有者权限):**  `4 (读) + 2 (写) + 1 (执行) = 7`，表示所有者具有读、写、执行的权限。
        *   **7 (组权限):** `4 (读) + 2 (写) + 1 (执行) = 7`，表示组用户具有读、写、执行的权限。
        *   **5 (其他用户权限):** `4 (读) + 0 (写) + 1 (执行) = 5`，表示其他用户具有读和执行的权限。

**示例:**
假设 `/www/wwwroot/gallery/jietu.library` 目录下有如下文件和目录：
```
-rwxrwxrwx    1 www   www        2  1月  5 20:10 actions.json
drwxrwxrwx    2 www   www     4096  1月 16 09:53 backup
-rwxrwxrwx    1 www   www       75  1月  5 20:10 Desktop.ini
drwxrwxrwx 2505 www   www   110592  1月 16 09:53 images
-rw-------    1 qihao qihao   9190  1月 16 09:53 metadata.json
-rw-------    1 qihao qihao  75102  1月 16 09:53 mtime.json
-rwxrwxrwx    1 www   www   266959  1月  5 20:10 OCR-history.json
-rwxrwxrwx    1 www   www        2  1月  5 20:10 saved-filters.json
-rw-------    1 qihao qihao    574  1月 16 09:53 tags.json
```
执行以上 `chown` 和 `chmod` 命令后，所有文件的所有者和组都会变成 `www`，权限会变成 `rwxrwxr-x`。
```
-rwxrwxr-x    1 www   www        2  1月  5 20:10 actions.json
drwxrwxr-x    2 www   www     4096  1月 16 09:53 backup
-rwxrwxr-x    1 www   www       75  1月  5 20:10 Desktop.ini
drwxrwxr-x 2505 www   www   110592  1月 16 09:53 images
-rwxrwxr-x    1 www   www   9190  1月 16 09:53 metadata.json
-rwxrwxr-x    1 www   www  75102  1月 16 09:53 mtime.json
-rwxrwxr-x    1 www   www   266959  1月  5 20:10 OCR-history.json
-rwxrwxr-x    1 www   www        2  1月  5 20:10 saved-filters.json
-rwxrwxr-x    1 www   www    574  1月 16 09:53 tags.json
```
这样，`qihao` （作为 `www` 组的一员）和 `www` 用户就都拥有了对该目录下所有文件的读、写和执行权限。

### 总结

本笔记涵盖了 Linux 中用户和组的管理，以及如何使用 `ls -l` 查看权限，并使用 `chown` 和 `chmod` 修改权限。正确理解和使用这些命令对于管理 Linux 系统至关重要。
```
