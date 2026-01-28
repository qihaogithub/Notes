# ComfyUI 管理器

**ComfyUI-Manager** 是一个旨在增强 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 可用性的扩展。它提供了管理功能，用于 **安装、移除、禁用和启用** ComfyUI 的各种自定义节点。此外，该扩展还提供了集线器功能和便捷功能，以便在 ComfyUI 中访问大量信息。

![菜单](misc/menu.jpg)

## 通知
* V2.48.1: 安全策略已更改。在“正常”安全级别下，允许下载列表中的模型。
* V2.47: 安全策略已更改。之前的“正常”现在变为“正常-”，“正常”不再允许高风险功能，即使您的 ComfyUI 是本地的。
* V2.37 显示在 GitHub 上活跃超过六个月的账户的 ✅ 标记。
* V2.33 应用了安全策略。
* V2.21 添加了 [cm-cli](docs/en/cm-cli.md) 工具。
* V2.18 至 V2.18.3 由于严重错误无法正常工作。建议这些版本的用户立即更新到 V2.18.4。请导航到 `ComfyUI/custom_nodes/ComfyUI-Manager` 目录并执行 `git pull` 进行更新。
* 您可以在 [ComfyUI 节点信息](https://ltdrdata.github.io/) 页面查看所有节点的信息。

## 安装

### 安装[方法1]（通用安装方法：仅 ComfyUI-Manager）

要在现有 ComfyUI 安装基础上安装 ComfyUI-Manager，您可以按照以下步骤操作：

1. 在终端（cmd）中进入 `ComfyUI/custom_nodes` 目录
2. 执行 `git clone https://github.com/ltdrdata/ComfyUI-Manager.git`
3. 重启 ComfyUI

### 安装方法[method2]（便携版 ComfyUI 的安装方法：仅限 ComfyUI-Manager）
1. 安装 git 
- 下载地址：https://git-scm.com/download/win
- 选择独立版本  
- 选项：使用 Windows 默认控制台窗口
2. 将 [scripts/install-manager-for-portable-version.bat](https://github.com/ltdrdata/ComfyUI-Manager/raw/main/scripts/install-manager-for-portable-version.bat) 下载到已安装的 `"ComfyUI_windows_portable"` 目录中
3. 双击 `install-manager-for-portable-version.bat` 批处理文件

![portable-install](misc/portable-install.png)


### 安装方法[method3]（通过 comfy-cli 安装：一次性安装 ComfyUI 和 ComfyUI-Manager）  
> 推荐：comfy-cli 提供了多种从命令行管理 ComfyUI 的功能。

* **前提条件：Python 3, git**

Windows:
```commandline
python -m venv venv
venv\Scripts\activate
pip install comfy-cli
comfy install
```

Linux/OSX:
```commandline
python -m venv venv
. venv/bin/activate
pip install comfy-cli
comfy install
```

> 本文是使用 ChatGPT 翻译的，如有遗漏请[**反馈**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new)。