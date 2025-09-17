您好，针对您在PVE上安装群晖DSM时进度卡在57%的问题，根据搜索结果，这里有几个可能的解决方案供您参考：

1. **使用telnet登录并创建块设备**：
   - 在57%报错界面使用telnet登录NAS的IP地址，用户名为root，密码为空。
   - 输入命令`cat /proc/partitions`来记录下sda的3个值。
   - 然后使用`mknod`命令创建块设备文件，例如：
     ```
     mknod /dev/synoboot b 80 1
     mknod /dev/synoboot1 b 80 2
     mknod /dev/synoboot2 b 80 3
     ```
   - 替换上述命令中的80、1、2、3为您自己的实际值，然后继续安装。

2. **更改虚拟机SATA位置**：
   - 有用户反映，通过将虚拟机的SATA位置改为（0，0）解决了卡在55%的问题。

3. **检查硬盘健康状态**：
   - 使用厂家的诊断工具在Windows计算机上执行全面的磁盘扫描，以确定硬盘是否正常。您可以参考WD HDD (Lifeguard)、Seagate HDD (SeaTools)、Hitachi HDD (Drive Fitness Test)等工具。

4. **网络连接和安全软件设置**：
   - 确保使用以太网线将Synology NAS直接连接到计算机而无需通过路由器。
   - 确认在DSM安装或Synology Assistant程序运行时，其他安全软件被禁用，因为ZoneAlarm和Kaspersky等安全软件可能会阻止连接。

5. **使用Synology Assistant安装DSM**：
   - 尝试使用Synology Assistant在Synology NAS上安装DSM。

请尝试上述方法之一或组合使用，看是否能够解决您的问题。如果问题依旧存在，可能需要进一步的技术支持。希望这些信息对您有所帮助！

```
135      242      51200 synoboot2
 135      243     945152 synoboot3
   8      128  514966160 sdi
   8      129    8388608 sdi1
   8      130    2097152 sdi2
   8      131          1 sdi3
   8      133  504240176 sdi5
   8      112   41943040 sdh
   8      113    8388608 sdh1
   8      114    2097152 sdh2
   8      115          1 sdh3
   8      117   31214288 sdh5
   9        0    8388544 md0
   9        1    2097088 md1
```

根据您提供的`/proc/partitions`的输出结果，我们需要找到`synoboot2`和`synoboot3`对应的主设备号（major）和次设备号（minor）。从您提供的信息中，我们可以看到：

- `synoboot2`的主设备号是135，次设备号是242。
- `synoboot3`的主设备号是135，次设备号是243。

接下来，您需要使用`mknod`命令来创建块设备文件。以下是根据您提供的信息生成的命令：

```bash
mknod /dev/synoboot b 135 242
mknod /dev/synoboot1 b 135 243
```

这里`/dev/synoboot`和`/dev/synoboot1`是您创建的设备文件，`b`表示这是一个块设备，135是主设备号，242和243分别是`synoboot2`和`synoboot3`的次设备号。

执行完上述命令后，您可以尝试重新启动DSM的安装过程。如果问题依旧存在，可能需要进一步的诊断和解决步骤。希望这些信息能够帮助您解决问题。


```
DiskStation> mknod /dev/synoboot b 135 242
mknod: /dev/synoboot: File exists
DiskStation> mknod /dev/synoboot1 b 135 243
mknod: /dev/synoboot1: File exists
```

根据您在PVE上安装群晖DSM时遇到的`mknod: File exists`错误，您可以尝试以下步骤来解决问题：

1. **删除已存在的设备节点**：
   由于您尝试创建的设备节点已经存在，您需要先删除这些节点。可以使用以下命令：
   ```bash
   rm /dev/synoboot
   rm /dev/synoboot1
   ```
   这将删除已存在的设备文件。

2. **重新创建设备节点**：
   删除后，您可以再次尝试创建设备节点：
   ```bash
   mknod /dev/synoboot b 135 242
   mknod /dev/synoboot1 b 135 243
   ```

3. **检查其他可能的设备节点**：
   如果您在创建其他设备节点时也遇到类似问题，请确保删除所有相关的设备节点，然后重新创建。

4. **参考相关文档**：
   如果问题仍然存在，建议您查看一些相关的安装文档和解决方案。例如，有用户在安装过程中遇到类似问题并成功解决，您可以参考他们的经验 。

请尝试上述步骤，看是否能够解决您的问题。如果问题依旧，请提供更多信息以便进一步诊断。
