https://blog.csdn.net/lingdjim/article/details/130660005

在 [PVE](https://so.csdn.net/so/search?q=PVE&spm=1001.2101.3001.7020) 中除了装PVE的硬盘，其他硬盘都是需要手动挂载的，这点不如ESXI方便，但是挂载硬盘方式也不难，下面就来看看PVE下怎么新增一块硬盘，不管是机械还是固态都是一样的。

![](https://i-blog.csdnimg.cn/blog_migrate/d3e77fee6733950359928dd115aa4095.jpeg)

 可以看到pve上已经识别了我的480g[固态硬盘](https://so.csdn.net/so/search?q=%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98&spm=1001.2101.3001.7020)，硬盘有三个分区，看到ntfs就可以想到之前是在windows下使用的，这是windows独有的分区格式，所以我们要在pve下使用，就要将他格式化掉，然后建立一个新的分区，再格式化成我们想要的格式

![](https://i-blog.csdnimg.cn/blog_migrate/ce69424789a65411988719753cab40e6.jpeg)

 进入pve管理后台的shell窗口

![](https://i-blog.csdnimg.cn/blog_migrate/567624d1cc9d64d2f708d75b2594ee76.jpeg)

输入fdisk /dev/sdb 提示输入命令

```null
fdisk /dev/sdb
```

补充知识–可跳过不看：linux下一切都是文件，包括你的设备，/dev这个目录可以理解为设备目录，类似于windows下的设备管理器，所以你的硬盘就在这个目录下，我的480g固态硬盘就是/dev/sdb 而/dev/sdb1 /dev/sdb2 /dev/sdb3 是它的三个分区，硬盘存在，但是需要挂载后才能使用。

fdisk是一个在linux下的分区工具，pve本来就是linux系统，所以可以直接使用该命令，这个工具和windows上的diskgenius一样强大，区别是在命令行下操作的，在输入fdisk后 如果不知道要输入什么命令 就输m, 这个相当于帮助文档，会提示你不同字母代表什么含义。使用工具，一般建议查看帮助文档，而不要去看傻瓜式的博客文章，因为也许工具的版本不同，命令的格式也不同。

![](https://i-blog.csdnimg.cn/blog_migrate/d7e2d5c871e968b34ceba8ed3e0123f1.jpeg)

按照提示，我们首先要做的是删除分区，提示告诉我们删除分区是输入d，输入后我们按照提示将分区都删掉


接着我们要创建一个分区，帮助文档上说是n，我们输入n
接着选择会让选择分区类型，我们选择 p
接着要建立几个分区，我们建一个就输1，然后后面就是输入分区的起始地址和终止地址，不需要自定义的话不用输入直接回车就好，有一个默认值，
建好分区，按w然后回车就可以执行你上面的操作。

最终在/dev下会有一个sdb1的分区就是已经建好的分区。

![](https://i-blog.csdnimg.cn/blog_migrate/0abf23228bd7d22a4c2a71c44314514f.jpeg)

格式化我们通过另一个命令mkfs,输入mkfs -t ext4 /dev/sdb1

```null
mkfs -t ext4 /dev/sdb1
```

mkfs -t ext4 /dev/sdb1 将分区格式化成ext4格式的，常见的硬盘格式有ext3、reiserfs 、ext2 、fat32 、ext4、msdos等，可以根据自己需要格式化成自己想要的格式，如果要查看mkfs的其他用法，输入mkfs -h 可以了解到更多的信息。

![](https://i-blog.csdnimg.cn/blog_migrate/17118826608d1db6a17a6762708ab902.jpeg)

cd /mnt 、 mkdir ssd-480g 创建一个文件名是ssd-480g的目录 

补充知识：要实现设备到目录的挂载，就要有个目录，在/mnt下创建一个文件夹，名字自己命名，我这边叫ssd-480g，为什么要在/mnt下而不是其他目录，因为mnt这个目录就是用来挂载u盘、硬盘等设备用的，可以说这是一种标准，至于你要放其他目录也无所谓。

将 /dev/​sdb1 分区挂载在 /mnt/​ssd-480g上：
```null
mount -t ext4 /dev/sdb1 /mnt/ssd-480g
```

设置开机挂载 fstab
![](https://i-blog.csdnimg.cn/blog_migrate/0a696c54556d0e1656a60e5fc1c36867.jpeg)
```
echo /dev/sdb1 /mnt/ssd-480g ext4 defaults 1 2 >> /etc/fstab
```
 


补充知识: echo 命令是控制台打印，echo …. >> 是将控制台打印转变成输入到某个文件中，这个 输入到了/etc/fstab文件中,也就是在 /etc/fstab 文件中 加入/dev/sdb1 /mnt/ssd-480g ext4 defaults 1 2这行文字，fstab是一个配置文件，开机的时候会加载，从而实现开机挂载硬盘功能,格式为 ||||||||||||要挂载的分区 要挂载的目录 分区的格式 挂载时候的参数 后面两个数字第一个数字是dump工具会根据这个数字来决定什么时候备份，第二个数字表示fsck工具检查的优先级

![](https://i-blog.csdnimg.cn/blog_migrate/74937cb29b299de82b2473bc6e47ffc2.jpeg)

 做完上面的操作，我们在PVE后台—>数据中心—>存储—>添加，就可以添加我们挂载的磁盘了

![](https://i-blog.csdnimg.cn/blog_migrate/2d01269b45529a573016cfff05db2501.jpeg)

 ID自己命名，目录填入你挂载的目录，内容建议全部选上，这个关系到你能不能在这个目录放ISO，或者放容器，放虚拟机等，全部选上就表示你可以放PVE所支持的所有内容。

![](https://i-blog.csdnimg.cn/blog_migrate/662e6d83ec18702cf85c0f46984db4ff.jpeg)

 最终看到虚拟机下面就会有一个新的存储。
