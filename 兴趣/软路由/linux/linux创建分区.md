---
创建日期: 2025-03-21T02:09:30+08:00
修改日期: 2025-11-12T14:51:43+08:00
---

## 背景

PVE 挂载硬盘后，并将硬盘分配给 Linux 虚拟机后，还需要创建分区才能使用。

Linux 终端输入 `lsblk`，输出如下：

```bash
qihao@qihao-Standard-PC-i440FX-PIIX-1996:~$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
...
sda      8:0    0   116G  0 disk 
├─sda1   8:1    0     1M  0 part 
└─sda2   8:2    0   116G  0 part /
sdb      8:16   0   490G  0 disk 
...
```

500 G 的硬盘对应设备是 **`/dev/sdb`** 并没有挂载，接下来需要创建分区。

## 具体步骤

### 步骤 1：确认 `sdb` 是否有分区

`lsblk` 显示 `sdb` 下面没有子分区（如 `sdb1`），说明这块硬盘可能是**未分区、未格式化**的状态，需要先分区和格式化才能使用。

### 步骤 2：分区（以 `fdisk` 工具为例）

1. 打开终端，执行以下命令进入分区工具（操作 `sdb`）：
   ```bash
   sudo fdisk /dev/sdb
   ```

2. 按提示操作（创建一个主分区）：
   - 输入 `n`（新建分区）
   - 按回车（默认主分区）
   - 按回车（默认分区号 1）
   - 按回车（默认起始扇区）
   - 按回车（默认使用全部空间）
   - 输入 `w`（保存分区表）

完成后，`lsblk` 会显示 `sdb` 下新增 `sdb1` 分区（即 `/dev/sdb1`）。

```
sda      8:0    0   116G  0 disk 
├─sda1   8:1    0     1M  0 part 
└─sda2   8:2    0   116G  0 part /
sdb      8:16   0   490G  0 disk 
└─sdb1   8:17   0   490G  0 part 
```

### 步骤 3：格式化分区（推荐 `ext4` 格式）

将新分区格式化为 Linux 常用的 `ext4` 格式（会清除数据，确认硬盘为空）：
```bash
sudo mkfs.ext4 /dev/sdb1
```

### 步骤 4：创建挂载点并挂载

1. 创建一个目录作为挂载点（例如 `/mnt/mydisk`）：
   ```bash
   sudo mkdir -p /mnt/mydisk
   ```

2. 挂载分区到该目录：
   ```bash
   sudo mount /dev/sdb1 /mnt/mydisk
   ```

### 步骤 5：查看挂载目录

此时，`sdb1` 已挂载到 `/mnt/mydisk`，可以通过以下命令确认：
```bash
lsblk /dev/sdb  # 会显示 MOUNTPOINTS 为 /mnt/mydisk
```

之后，你就可以通过 `/mnt/mydisk` 目录访问这块 500 G 硬盘的内容（例如通过文件管理器进入该目录，或终端执行 `cd /mnt/mydisk`）。