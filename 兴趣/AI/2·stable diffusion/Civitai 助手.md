[GitHub 地址](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper)

Civitai 的 SD Webui 扩展，可帮助您更轻松地处理模型。

# 特征

-   **扫描所有模型，从 Civitai 下载模型信息和预览图像。**
    
-   **通过 civitai url 将本地模型链接到 civitai 模型**
    
-   **通过 Civitai Url 下载模型（带信息+预览）到 SD 的模型文件夹或子文件夹中。**
    
-   **下载可以断点续传。**
    
-   **从 Civitai 检查所有本地模型的新版本**
    
-   **将新版本直接下载到 SD 模型文件夹中（带信息+预览）**
    
-   **修改内置“Extra Network”卡，在每张卡上添加以下按钮：**
    
    -   🖼: 将“替换预览”文字修改为该图标
        
    -   **🌐: 在新标签页中打开此模型的 Civitai 网址**
        
    -   **💡: 添加本模型的触发词提示**
        
    -   **🏷: 使用本模型的预览图提示**
        
-   还支持Extra Network的缩略图模式
    
-   始终显示附加按钮的选项，因此现在它们可以与触摸屏一起使用。

# 安装

**每次安装或更新此扩展时，您都需要关闭 SD Webui 并重新启动它。只是“重新加载用户界面”是行不通的。**

# 如何使用

**首先，将您的 SD Webui 更新到最新版本！**

此扩展需要获取额外网络的卡 ID。**这是自 2023-02-06 以来添加的。**如果你的 SD webui 是较早的版本，你需要更新它！

**安装后，**转到扩展选项卡“Civitai Helper”。有一个名为“**扫描模型**”的按钮。

![](https://imagecache.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/15d4ae4d-2e9e-4c3b-6ae6-c9dcb1191700/width=525/15d4ae4d-2e9e-4c3b-6ae6-c9dcb1191700)

**点击它**，插件会扫描你所有的模型生成SHA256 hash，并使用这个hash从civitai获取模型信息和预览图片。

**扫描完成后，**

**打开 SD webui 的内置“Extra Network”选项卡，以显示模型卡。**

![](https://imagecache.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/80b602aa-b1d6-4d29-ad62-f4a96b2f4d00/width=525/80b602aa-b1d6-4d29-ad62-f4a96b2f4d00)

将鼠标移到模型卡的底部。它将显示 4 个图标按钮：

-   🖼: 将“替换预览”文字修改为该图标
    
-   🌐:**在新标签页中打开此模型的 Civitai 网址**
    
-   💡:**添加本模型的触发词提示**
    
-   🏷:**使用本模型的预览图提示**
    

**如果这些按钮不存在，请单击“刷新 Civitai Helper”按钮将它们取回。**

![](https://imagecache.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ad4718fd-72d8-404d-2d09-6e0e96b3c300/width=525/ad4718fd-72d8-404d-2d09-6e0e96b3c300)

每次刷新额外的网络选项卡时，它都会删除此扩展的所有其他按钮。您需要单击`Refresh Civitai Helper`按钮将它们带回来。