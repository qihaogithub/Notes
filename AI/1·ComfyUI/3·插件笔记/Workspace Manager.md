---
banner: https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-4.jpg
banner_y: "9.5"
Created: 效率
类型:
  - 界面
简介: 工作流与模型管理
---
文章原地址：

[效率翻倍！ComfyUI 必装的工作流+模型管理插件 Workspace Manager - 优设网 - 学设计上优设](https://www.uisdc.com/workspace-manager)

ComfyUI 插件 Workspace Manager，它可以让我们轻松管理、调用自己的工作流文件和模型，有效提升我们使用 ComfyUI 的效率。

# 安装方式

## 通过 ComfyUI Manager 安装（推荐）。

进入 ComfyUI 工作界面后，点击右下角面板的 Manager 选项，进入后选择 Inatall Custom Nodes，在列表里搜索 Workspace manager 进行安装，完成后记得重启 ComfyUI。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-2.jpg](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-2.jpg)

## 通过 git 网址安装

这要求我们先安装好 git 以及 powershell 软件，然后进入 ComfyUI 根目录的 custom_nodes 文件夹，在空白处单击右键，选择 「在终端中打开」，然后在将下方代码粘贴到命令窗口，按 Enter 执行安装即可，完成后依旧需要重启 ComfyUI。

安装代码：git clone [https://github.com/11cafe/comfyui-workspace-manager.git](https://link.uisdc.com/?redirect=https%3A%2F%2Fgithub.com%2F11cafe%2Fcomfyui-workspace-manager.git)

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-3.jpg](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-3.jpg)

安装成功后，ComfyUI 工作界面左上角就是 Workspace 的工作流管理工具栏，右上角蓝色的 「Models」按钮用于管理模型。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-4.jpg](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-4.jpg)

## 使用方法
Workspace Manager 可以让我们轻松实现工作流的切换浏览、历史版本保存、分类管理，批量导入下载，具体操作如下：

① 之前 ComfyUI 的界面一次只能打开一个工作流，非常不方便，而安装 workspace 后，我们可以在一键导入多个工作流，并通过左侧列表随时切换查看。导入方式为点击左上角的 “文件小图标” 唤出左侧列表，再点击 Import 可以导入本地工作流文件或文件夹。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-5.gif](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-5.gif)

② 在左侧列表中单击右键，可以 Duplicate 复制这个工作流。也直接将一个工作流作为子工作流，拖入到当前界面中。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-6.gif](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-6.gif)

③ 当我们用工作流生成图像或视频后，这些图像会保存在工作流的图库中，我们可以通过点击顶部的 “照片小图标” 查看所有生成的图像。其中包含的功能有加载图像对应的工作流；点击卡片查看图像生成元数据（提示、采样器、使用的模型等）；或者将图像设置为工作流列表的缩略图，方便我们识别其用途。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-7.jpg](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-7.jpg)

④ 点击顶部的「保存」小图标或按快捷键 Shift+S 可以手动保存工作流。每这样保存一次， Workspace 都会创建一条新历史记录，这样就方便我们找回之前的操作。如果你想保存同一个工作流的不同参数版本，可以点击 「File」下的 Create Version 选项 ，对当前版本进行命名保存。比如我先保存一个 cfg=7 的版本，再保存一个 cfg=8 的版本，之后想使用不同参数时直接找到对应的版本就可以了。

点击顶部的蓝色「File」按钮，选择 Version History 中可以查看并调用所有保存过的版本及历史记录，这比新建一个工作流更简洁方便。而点击 Discard 选项可以将目前的工作流恢复至你最后一次保存的状态。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-8.gif](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-8.gif)

⑤ 当上传的工作流过多，为了方便查看和管理，可以通过文件夹对工作流分类：点击左侧窗口左上角的带加号的 “文件夹图标” 新建一个文件夹，然后将工作流拖入其中即可；还可以为工作流打上标签，方便后期筛选查找。我们所有导入的工作流 Workspace 都可以自动保存，只需进入右上角的 Settings 设置里，在 save directory 中填写一个目标文件夹路径即可。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-9.jpg](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-9.jpg)

⑥ Workspace 还支持批量修改工作流，方法为点击左侧窗口 - 左上角的 “清单小图标” ，进入多选模式，勾选需要处理的工作流，然后删除或者打包下载。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-10.jpg](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-10.jpg)

点击工作界面右上角蓝色的 「Models」按钮，可以查看所有我们已经安装好的模型，包括 checkpoints、lora、vae、embeddings、controlnet、upscale、animatediff、ip-adapter、sam 等多种类型，支持通过关键词筛选。将模型拖入工作界面，会自动变成一个 load 节点，这样我们就不需要在文字列表里一个个翻找了。

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-11.gif](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-11.gif)

### 安装模型
对 Civitai 或其他网站上存在的模型，Workspace 会自动拉取它的封面图，这样我们选择起来也会更直观。想安装新模型的话，也可以直接点击右上角的 “Install Models” 按钮，会显示一个新的界面，上面有 Civitai 及 Hugging Face 上的各种模型，我们可以直接下载。（注意：这种方式下载的模型会安装到 ComfyUI 根目录的文件夹中，因此可能不适合与 WebUI 共享模型目录的用户）

![https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-12.jpg](https://image.uisdc.com/wp-content/uploads/2024/02/uisdc-cj-20240207-12.jpg)