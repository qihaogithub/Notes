一、COMFYUI 模型共享插件教程
------------------

### 1.1 插件特性

*   **跨盘符共享模型文件**：可以将模型文件放在固态硬盘中，提升出图效率。
*   **解决 COMFYUI 原版模型共享配置无法对所有模型进行引用的问题**。
*   **多 COMFYUI 共享模型文件**：只需保留一份模型文件即可实现所有整合包共用。

### 1.2 插件介绍

模型共享插件可用于解决多个 COMFYUI 之间的模型共享问题。只需要保留其中一份模型文件，即可实现所有整合包共用。如果你想在 COMFYUI 整合包中使用共享模型插件，可以按照以下步骤进行配置。

### 1.3 链接

插件下载链接：[https://pan.baidu.com/s/1xOYC0wheBpeyp00LMNL\_Yw?pwd=gp04](https://pan.baidu.com/s/1xOYC0wheBpeyp00LMNL_Yw?pwd=gp04) 提取码：gp 04

二、详细配置步骤
--------

### 2.1 开启开发者选项

首先，在 Windows 系统设置中找到开发者选项并开启。打开后才能创建虚拟文件[软链接](https://so.csdn.net/so/search?q=%E8%BD%AF%E9%93%BE%E6%8E%A5&spm=1001.2101.3001.7020)，从而实现共享模型。

### 2.2 放置插件文件

将 rick\_share\_models. Py 插件放到整合包的 custom\_nodes 目录下。

插件文件路径  
![](https://i-blog.csdnimg.cn/direct/9c107e93914c447d927849e9137e0103.png)

### 2.3 放置配置文件

将 rick\_easy. Conf 文件放到整合包根路径下。

配置文件路径  
![](https://i-blog.csdnimg.cn/direct/54fd4e10d3074304b413d93c5167ef03.png)

### 2.4 编辑配置文件

编辑 rick\_easy. Conf 配置文件，修改共享模型的路径。

配置文件编辑  
![](https://i-blog.csdnimg.cn/direct/a574c234a7d74f4397b8c720ad11c937.png)

打开文件后找到 ext\_models\_path 配置项，将拓展模型路径粘贴到=号后面。可以通过该方法将整合包和模型分离，也可用于多个 COMFYUI 共享模型。

#### 2.4.1 其他配置项

*   enable 配置项表示是否开启共享，默认打开。
*   share\_mode 支持两种共享模型模式：
*   merge（默认方式）：现有 COMFYUI 目录下的模型文件和拓展模型文件保持之前的存储位置不变，通过挂载方式虚拟共享。
*   move：现有 COMFYUI 目录下的模型文件全部移动到拓展模型目录，然后通过虚拟目录访问拓展文件夹中的模型。

三、启动 COMFYUI 并验证
--------------

### 3.1 启动 COMFYUI

配置完成后启动 COMFYUI 整合包，观察启动过程中的日志信息，确认是否创建了挂载。

启动日志  
![](https://i-blog.csdnimg.cn/direct/6766e658ad2b4912a8f763ecb5437036.png)

### 3.2 验证模型共享

回到整合包的路径，刷新查看模型文件，确认是否被自动创建。

共享模型目录  
![](https://i-blog.csdnimg.cn/direct/c0a4299524034d76b293f351fa1b9c87.png)

*   如果模型文件已被创建为快捷方式，说明模型共享成功。

### 3.3 多整合包共享配置

如果你有多个整合包，可以在每个整合包中放置插件和配置文件，指向同一个模型文件夹地址。通过这种方式，你电脑上不管有多少个 COMFYUI 的整合包，只需要保留一份模型文件即可。

多整合包共享  
![](https://i-blog.csdnimg.cn/direct/acc6b4b9f86f4d08a7f5940fce0c2576.png)

四、总结
----

通过以上步骤，你可以成功配置 COMFYUI 模型共享插件，实现多个整合包之间的模型共享。这样不仅可以节省存储空间，还能提升 AI 出图效率。希望本教程对你有所帮助！

感谢 b 站博主分享的视频教程跟插件：[https://www.bilibili.com/video/BV1Rx4y1B7nW/?spm\_id\_from=333.337.search-card.all.click&vd\_source=6d16396235f77f5698a668dd8452b2eb](https://www.bilibili.com/video/BV1Rx4y1B7nW/?spm_id_from=333.337.search-card.all.click&vd_source=6d16396235f77f5698a668dd8452b2eb)

五、Comfyui 工作流封装成 web 站点、H 5、小程序、App 的源码介绍
------------------------------------

项目中接入了国内外各大平台的 gpt 聊天模型，使用 milvus 作为向量数据库，可上传知识库文档。可 AI 接管微信、QQ、钉钉、企业微信等社媒平台！绘图接入了 comfyui 和 dalle，实现了电商换装、换脸、ai 抠图、图片变高清、智能扩图、艺术二维码等功能。  
![](https://i-blog.csdnimg.cn/blog_migrate/2ad51b000d7d1c2a2d81231bd60d8714.png)
  
![](https://i-blog.csdnimg.cn/blog_migrate/9f207b7ee82aac3dfb9b115098e5c0c6.png)
  
![](https://i-blog.csdnimg.cn/blog_migrate/1f2162411ae048a11009eaa4cb2374fb.png)
  
源码地址：  
[https://wailikeji.com/index.php/2023/07/15/chat\_draw/](https://wailikeji.com/index.php/2023/07/15/chat_draw/)

项目体验地址：  
[https://pcai.wailikeji.com/](https://pcai.wailikeji.com/)