[视频教程](https://www.bilibili.com/video/BV1VC4y117Ud/?spm_id_from=333.788.top_right_bar_window_history.content.click&vd_source=81223299ca5d449a34daaab3e1102d1d) 

本教程介绍如何使用sd-trainer by [秋葉aaaki](https://space.bilibili.com/12566101) 进行Lora模型的训练。



背景 
---------------------------

SD-Trainer是stable diffusion进行LoRA训练的webui，LoRA，英文全称Low-Rank Adaptation of Large Language Models， 是微软的研究人员为了解决大语言模型微调而开发的一项技术。有了SD-Trainer，只需要少许图片，每个人都能够方便快捷地训练出属于自 己的stable diffusion模型，可以让图片按照你的想法进行呈现。

第一步 启动秋叶训练器 
-------------------------------------------------------------------------------------------------------------

目前秋叶训练器我们提供了应用启动器和自定义创建手动启动两种方式启动。如果您是新手，请使用应用启动器启动，无需输入任何命令，参考方法一；如果您习惯使用终端代码调试，参考方法二。

### 方法一：新手推荐-应用启动器：启动一步走 

进入「应用启动器」页面，选择「秋葉炼丹炉SD-Trainer」训练器，点击「部署」按钮，点击「立即创建」，会进入「工作空间」页面；

![](https://doc-rde.lanrui-ai.com/assets/trainer-qdq0.png)

![](https://doc-rde.lanrui-ai.com/assets/trainer-qdq00.png)

创建完成后稍等片刻，无需其他任何操作，等待「打开应用」按钮可点击后，点击该按钮就可以进入sd-trainer界面训练啦.

![](https://doc-rde.lanrui-ai.com/assets/trainer-qdq1.png)

![](https://doc-rde.lanrui-ai.com/assets/trainer6.png)

**提醒**：启动器不需要自己输入命令哦，如果查看启动/打标/训练进度，进入工作空间详情-日志查看。

![](https://doc-rde.lanrui-ai.com/assets/trainer-qdq2.png)

### 方法二：熟手推荐-自定义创建：启动三步走，自主操控 [#](#%e6%96%b9%e6%b3%95%e4%ba%8c%e7%86%9f%e6%89%8b%e6%8e%a8%e8%8d%90-%e8%87%aa%e5%ae%9a%e4%b9%89%e5%88%9b%e5%bb%ba%e5%90%af%e5%8a%a8%e4%b8%89%e6%ad%a5%e8%b5%b0%e8%87%aa%e4%b8%bb%e6%93%8d%e6%8e%a7)

#### 一、购买算力创建工作空间 

点击[去市场](https://www.lanrui-ai.com/index/compute4)，选择一台3090或4090的机器，点击自定义创建，按照以下内容配置，点击立即创建（如图所示）：

*   镜像：选择【秋葉炼丹炉SD-Trainer】；
*   网盘：默认挂载；
*   数据集：默认挂载sd-base(sd-base中有常用sdxl模型/sd1.5底模/lora模型/VAE模型均可以使用)；
*   启动方式：选择手动启动；

![](https://doc-rde.lanrui-ai.com/assets/zdy01.png)

![](https://doc-rde.lanrui-ai.com/assets/trainer8.png)

#### 二、开启工作空间 [#](#%e4%ba%8c%e5%bc%80%e5%90%af%e5%b7%a5%e4%bd%9c%e7%a9%ba%e9%97%b4)

点击创建后，一般1-2分钟可启动成功，待实例状态由启动中变为运行中后，点击进入vscode

![](https://doc-rde.lanrui-ai.com/assets/trainer9.png)

#### 三、启动sd-trainer [#](#%e4%b8%89%e5%90%af%e5%8a%a8sd-trainer)

1、进入vscode后，点击【打开文件夹】，输入/home/user/后点击OK，选择信任，最后我们在左侧栏就能看到目录文件。

*   如果您需要使用sd-base数据集中的模型作为训练底模文件等，可以找到模型后右键单击【复制路径】可获取模型完整路径，下面训练时候会用到这个路径，需要特别记住一下。
    
*   sd底模路径：`/home/user/imported_datasets/sd-base/models/Stable-diffusion/模型文件名称`
*   sdxl模型路径：`/home/user/imported_datasets/sd-base/sdxl/模型文件名称`
*   VAE模型路径：`/home/user/imported_datasets/sd-base/models/VAE/模型文件名称`
    
```
常用路径：
sd_xl_base：
/home/user/imported_datasets/sd-base/sdxl/sd_xl_base_1.0.safetensors

sdxl：
/home/user/imported_datasets/sd-base/models/VAE/sdxl_vae.safetensors

dreamshaper_8：
/home/user/imported_datasets/sd-base/models/Stable-diffusion/dreamshaper_8.safetensors

dreamshaperXL_v21Turbo：
/home/user/imported_datasets/sd-base/models/Stable-diffusion/dreamshaperXL_v21TurboDPMSDE.safetensors

VAE：
/home/user/imported_datasets/sd-base/models/VAE/sdxl_vae.safetensors
/home/user/imported_datasets/sd-base/models/VAE/vae-ft-mse-840000-ema-pruned.safetensors

```

* 
    ![](https://doc-rde.lanrui-ai.com/assets/trainer2.png)
     ![](https://doc-rde.lanrui-ai.com/assets/trainer3.png)
     ![](https://doc-rde.lanrui-ai.com/assets/trainer4.png)
    

2、点击左上角新建terminal终端，

![](https://doc-rde.lanrui-ai.com/assets/lora-9.png)

运行以下启动命令，然后按回车键；

```
nohup bash /home/user/start.sh > train.log 2>&1 &

```

启动/训练进度输入以下命令查看：

```
tail -fn 500 train.log

```

运行结果显示为“TensorBoard 2.101 at http://0.00.:6006/ ”代表运行完成，即可进入sd-trainer的页面进行训练。（如图所示）

![](https://doc-rde.lanrui-ai.com/assets/trainer5.png)

如果您在训练中想要停止重新训练，可输入以下停止命令，然后重新运行启动命令：

```
pkill -9 -f '27777'  &&  pkill -9 -f 'lora-scripts' 

```

第二步 开始训练 [#](#%e7%ac%ac%e4%ba%8c%e6%ad%a5-%e5%bc%80%e5%a7%8b%e8%ae%ad%e7%bb%83)
-------------------------------------------------------------------------------

### 打开sd-trainer页面 [#](#%e6%89%93%e5%bc%80sd-trainer%e9%a1%b5%e9%9d%a2)

请返回工作空间点击打开调试地址（应用启动器点击打开应用），就可以进入sd-trainer的页面啦。

![](https://doc-rde.lanrui-ai.com/assets/v4-6.png)

![](https://doc-rde.lanrui-ai.com/assets/trainer6.png)

### 训练前准备 

**准备待训练数据集和训练底模**

首先进入左侧导航网盘data目录，新建训练文件夹sd\_train\_dataset，再新建二级文件夹分别为img/outputs/model/log的文件夹，该文件夹路径为`/ark-contexts/data/sd_train_dataset/XXX`，点击「复制地址」按钮即可复制完整路径。

点击网盘右侧的上传文件夹，或通过[文件管理](https://doc-rde.lanrui-ai.com/docs/yong-hu-shou-ce/shu-ju-guan-li/file-browser/)功能上传；

![](https://doc-rde.lanrui-ai.com/assets/trainer1.png)

img文件夹：放训练的数据集文件夹，上传图片文件夹格式为：“xx\_XXXXX”,其中xx是数字，代表训练步数，XXXXX为自定义名称，例如10\_item

model文件夹：放训练用的底膜（[快速上传模型方法](https://doc-rde.lanrui-ai.com/docs/yong-hu-shou-ce/shu-ju-guan-li/wai-bu-shu-ju-guan-li/#%e5%a4%96%e9%83%a8url%e6%95%b0%e6%8d%ae-%e4%bd%bf%e7%94%a8%e6%96%b9%e6%b3%95)），也可直接选用上面提到的sd-base数据集中的模型来使用就行。

outputs文件夹：模型保存路径

log文件夹：日志输出路径

### 图片预处理打标

点击左侧导航【WD 1.4 标签器】，复制训练集路径放到图片文件夹路径下，点击启动，打标完成网盘会输出对应的txt文件。

用上面提到的上传10\_item文件夹为例，图片文件夹路径就是：`/ark-contexts/data/sd_train_dataset/img/10_item`

![](https://doc-rde.lanrui-ai.com/assets/trainer7.png)

![](https://doc-rde.lanrui-ai.com/assets/trainer10.png)

![](https://doc-rde.lanrui-ai.com/assets/trainer10-1.png)

### 输入路径，开始训练 [#](#%e8%be%93%e5%85%a5%e8%b7%af%e5%be%84%e5%bc%80%e5%a7%8b%e8%ae%ad%e7%bb%83)

选择新手或专家两种模式，新手模式暴露的参数更少，如果对此流程不熟悉，推荐新手模式，本例中使用专家模式，可根据训练需要调整参数.

**其中路径类参数必须修改，否则保存的模型重启会丢失**

*   底模文件路径：使用sd-base数据集中的模型,或用自己上传的底膜底膜路径。我这里用的数据集中的模型，路径为`/home/user/imported_datasets/sd-base/models/Stable-diffusion/3Guofeng3_v33.safetensors`
*   训练数据集路径： `/ark-contexts/data/sd_train_dataset/img/`
*   模型保存文件夹：`/ark-contexts/data/sd_train_dataset/outputs/`
*   日志保存文件夹：`/ark-contexts/data/sd_train_dataset/log/`
*   tag文件扩展名：默认.txt

![](https://doc-rde.lanrui-ai.com/assets/trainer12.png)
 ![](https://doc-rde.lanrui-ai.com/assets/trainer13.png)
 ![](https://doc-rde.lanrui-ai.com/assets/trainer14.png)

如果是训练sdxl的lora，需要注意（如图所示）

*   训练种类选择:sdxl-lora
*   模型保存精度&训练混合精度默认fp16，需加个sdxl的VAE，输入路径：`/home/user/imported_datasets/sd-base/models/VAE/madebyollin-sdxl-vae-fp16-fix.safetensors` ，不然会训练失败；或模型保存精度&训练混合精度都改为bf16，无需加vae就可以。
*   ![](https://doc-rde.lanrui-ai.com/assets/trainer12-1.png)
    

检查配置完成后，可点击“直接开始训练”，在您前面开启的终端中可监控模型训练结果

备注：如果出现训练失败，可以稍等一分钟，再重新点击开始训练。
 
### 查看训练进度 [#](#%e6%9f%a5%e7%9c%8b%e8%ae%ad%e7%bb%83%e8%bf%9b%e5%ba%a6)

*   如是使用应用启动器或自动启动方式的，您可点击工作空间详情-日志，查看打标/训练进度 ![](https://doc-rde.lanrui-ai.com/assets/trainer-qdqxl.png)
    
*   如使用手动启动的，在您前面使用的终端中查看训练进度
    

![](https://doc-rde.lanrui-ai.com/assets/1687779581558.png)

提示训练完成后，在您之前创建的`data/sd_train_dataset/outputs` 文件夹即可找到您的模型. ![](https://doc-rde.lanrui-ai.com/assets/trainer-output.png)

通过[文件管理功能](https://doc-rde.lanrui-ai.com/docs/yong-hu-shou-ce/shu-ju-guan-li/file-browser/)传输到[Stable Diffusion Web UI](https://doc-rde.lanrui-ai.com/docs/yong-hu-shou-ce/ying-yong-zhuan-qu/sd-zhuan-qu/webui-mu-lu/#%e6%a8%a1%e5%9e%8b%e7%9b%ae%e5%bd%95)网盘data/sd-4/models/Lora目录就可以使用啦!