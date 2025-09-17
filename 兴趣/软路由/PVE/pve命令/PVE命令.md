**pvesm status**- **作用**：在 Proxmox VE（一种虚拟化管理平台）环境中，用于查看存储资源的状态。

- **输出内容**：会显示存储资源的名称、类型、总容量、已使用容量、可用容量等详细信息。通过这个命令，我们可以清楚地知道各个存储资源的使用情况，便于进行存储资源的管理和规划。

三、存储资源管理命令（Proxmox VE 环境）

### （一）存储资源删除与添加

- **pvesm remove hdd-500g**
  - **作用**：删除名为`hdd-500g`的存储资源。
  - **注意事项**：在删除存储资源之前，需要确保该存储资源没有被虚拟机或其他服务使用，否则可能会导致数据丢失或服务中断。
- **pvesm add dir hdd-500g -path /mnt/sdb1 -maxsize 458G**
  - **作用**：添加一个名为`hdd-500g`的目录类型的存储资源，指定其路径为`/mnt/sdb1`，最大容量为 458G。
  - **应用场景**：当我们需要在 Proxmox VE 环境中添加新的存储资源，用于存储虚拟机镜像、容器数据等时，可以使用这个命令进行配置。
- **pvesm add dir hdd-500g -path /mnt/sdb1 -content images**
  - **作用**：为名为`hdd-500g`的存储资源添加内容类型限制，指定其只能存储虚拟机镜像（images）。
  - **应用场景**：通过设置内容类型，可以更好地管理和组织存储资源中的数据，确保不同类型的文件存储在合适的存储资源中，提高存储的效率和安全性。

### （二）PVE 常用命令

- `qm start <vmid>`: 启动虚拟机，`<vmid>` 为虚拟机 ID。
- `qm stop <vmid>`: 停止虚拟机。
- `qm shutdown <vmid>`: 关闭虚拟机，发送ACPI shutdown信号，推荐使用。
- `qm reset <vmid>`: 重启虚拟机。
- `qm suspend <vmid>`: 挂起虚拟机。
- `qm resume <vmid>`: 恢复挂起的虚拟机。
- `qm clone <vmid> <new_vmid> --name <new_name>`: 克隆虚拟机，`<new_vmid>` 为新虚拟机的 ID，`<new_name>` 为新虚拟机的名称。
- `qm migrate <vmid> <target_node>`: 将虚拟机迁移到目标节点。
- `qm monitor <vmid>`: 打开虚拟机的 QEMU 监控器。
- `qm status <vmid>`: 查看虚拟机状态。
- `qm config <vmid>`: 查看虚拟机配置。
- `qm destroy <vmid>`: 删除虚拟机。
- `pct start <ctid>`: 启动容器，`<ctid>` 为容器 ID。
- `pct stop <ctid>`: 停止容器。
- `pct shutdown <ctid>`: 关闭容器。
- `pct restart <ctid>`: 重启容器。
- `pct suspend <ctid>`: 挂起容器。
- `pct resume <ctid>`: 恢复挂起的容器。
- `pct clone <ctid> <new_ctid> --name <new_name>`: 克隆容器，`<new_ctid>` 为新容器的 ID，`<new_name>` 为新容器的名称。
- `pct migrate <ctid> <target_node>`: 将容器迁移到目标节点。
- `pct status <ctid>`: 查看容器状态。
- `pct config <ctid>`: 查看容器配置。
- `pct destroy <ctid>`: 删除容器。
```
