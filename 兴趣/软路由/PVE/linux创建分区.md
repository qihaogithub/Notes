
   - 如果你希望在`sdb`上创建新的分区并挂载，可以使用`fdisk`或`parted`工具来创建分区，然后格式化并挂载。
   - 具体步骤：
     1. 创建分区：
        ```bash
        sudo fdisk /dev/sdb
        ```
        - 输入`n`创建新分区
        - 选择分区类型（主分区或扩展分区）
        - 选择分区号
        - 输入起始和结束扇区（可以按默认值）
        - 输入`w`保存并退出
     2. 格式化分区（例如，创建一个ext4文件系统）：
        ```bash
        sudo mkfs.ext4 /dev/sdb1
        ```
     3. 创建挂载点并挂载：
        ```bash
        sudo mkdir /mnt/newdisk
        sudo mount /dev/sdb1 /mnt/newdisk
        ```
     4. 为了在系统启动时自动挂载，可以编辑`/etc/fstab`文件：
        ```bash
        sudo nano /etc/fstab
        ```
        添加以下行：
        ```plaintext
        /dev/sdb1 /mnt/newdisk ext4 defaults 0 2
        ```
