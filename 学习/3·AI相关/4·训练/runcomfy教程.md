该 ComfyUI FLUX LoRA 训练工作流程使您能够使用自己的数据集对现有的 FLUX 模型进行微调。通过本详细指南，您将学习如何准备您的训练数据、设置工作流程、配置必要的参数并执行训练过程。充分发挥 FLUX AI 模型的潜力，并创建与您的愿景完美对齐的定制输出。

FLUX LoRA 在 AI 社区中获得了极大的欢迎，特别是在那些希望用自己的数据集微调 AI 模型的人群中。这种方法使您能够轻松地将现有的 FLUX 模型适应于您的独特数据集，使其高度可定制并适用于各种创意项目。如果您已经熟悉 ComfyUI，使用 ComfyUI FLUX LoRA 训练工作流程来训练您的 FLUX LoRA 模型将会非常简单。这一工作流程和相关节点由 Kijai 创建，因此我们对他的贡献表示衷心的感谢！请查看 [Kijai's GitHub](https://github.com/kijai/ComfyUI-FluxTrainer/tree/main) 了解更多信息。

[runcomfy教程](runcomfy教程.md#comfyui-flux-lora-训练教程)ComfyUI FLUX LoRA 训练教程
-------------------------------------------------

ComfyUI FLUX LoRA 训练工作流程是一个强大的过程，专为训练 FLUX LoRA 模型而设计。使用 ComfyUI 进行训练具有多个优势，特别是对于已经熟悉其界面的用户。通过 FLUX LoRA 训练，您可以使用相同的模型进行推理，确保在相同的 Python 环境中工作时不会出现兼容性问题。此外，您还可以构建工作流程以比较不同设置，增强您的训练过程。本教程将指导您设置和使用 ComfyUI 中的 FLUX LoRA 训练。

我们将涵盖：

1.  准备您的 FLUX LoRA 训练数据集
2.  FLUX LoRA 训练过程
3.  执行 FLUX LoRA 训练
4.  如何以及在哪里使用 FLUX 和 FLUX LoRA 模型

[runcomfy教程](runcomfy教程.md#1-准备您的-flux-lora-训练数据集)1\. 准备您的 FLUX LoRA 训练数据集
---------------------------------------------------

在准备您的 FLUX LoRA 训练数据时，确保您拥有高质量的目标主体图像是至关重要的。

在本示例中，我们正在训练一个 FLUX LoRA 模型以生成特定影响者的图像。为此，您需要一组该影响者在各种姿势和环境下的高质量图像。使用 [ComfyUI Consistent Character workflow](https://www.runcomfy.com/comfyui-workflows/create-consistent-characters-within-comfyui) 是收集这些图像的便捷方式，它可以轻松生成一组显示相同角色在不同姿势下的一致外观的图像。对于我们的训练数据集，我们选择了五张在各种姿势和环境下的高质量影响者图像，确保数据集足够强大以便 FLUX LoRA 训练学习生成一致且准确的输出所需的复杂细节。

### [runcomfy教程](runcomfy教程.md#获取训练数据的过程)获取训练数据的过程

![](https://cdn.runcomfy.com/workflow_assets/1123/readme01.webp)

### [runcomfy教程](runcomfy教程.md#训练数据示例)训练数据示例

![](https://cdn.runcomfy.com/workflow_assets/1123/readme02.webp)

您也可以根据您的具体需求收集自己的数据集——FLUX LoRA 训练具有灵活性，并且适用于各种类型的数据。

[runcomfy教程](runcomfy教程.md#2-flux-lora-训练过程)2\. FLUX LoRA 训练过程
---------------------------------------

FLUX LoRA 训练工作流程包括多个关键节点，这些节点协同工作以训练和验证您的模型。以下是主要节点的详细概述，分为三个部分：数据集、设置与初始化、训练。

### [runcomfy教程](runcomfy教程.md#21-设置-flux-lora-训练的数据集)2.1. 设置 FLUX LoRA 训练的数据集

数据集部分包含两个基本节点，帮助您配置和自定义您的训练数据：**TrainDatasetGeneralConfig** 和 **TrainDatasetAdd**。

### [runcomfy教程](runcomfy教程.md#211-traindatasetgeneralconfig)2.1.1. TrainDatasetGeneralConfig

![](https://cdn.runcomfy.com/workflow_assets/1123/readme03.webp)

**TrainDatasetGeneralConfig** 节点是定义 FLUX LoRA 训练中训练数据集整体设置的地方。此节点使您可以控制数据增强和预处理的各个方面。例如，您可以选择启用或禁用 **颜色增强**，这可以帮助提高模型在不同颜色变化中的泛化能力。同样，您可以切换 **翻转增强** 以随机水平翻转图像，提供更丰富的训练样本。此外，您还可以选择 **打乱每个图像所关联的标题**，引入随机性并减少过拟合。**标题丢弃率** 允许您在训练过程中随机丢弃标题，这可以帮助模型更强大地应对缺失或不完整的标题。

### [runcomfy教程](runcomfy教程.md#212-traindatasetadd)2.1.2. TrainDatasetAdd

![](https://cdn.runcomfy.com/workflow_assets/1123/readme04.webp)

**TrainDatasetAdd** 节点是您指定每个要包含在 FLUX LoRA 训练中的单个数据集详细信息的地方。

#### [runcomfy教程](runcomfy教程.md#输入目录训练数据集路径)输入目录：训练数据集路径

为了充分利用此节点，妥善组织您的训练数据是很重要的。使用 RunComfy 的文件浏览器时，将训练数据放在 `/home/user/ComfyUI/input/{file-name}` 目录中，其中 `{file-name}` 是您为数据集指定的有意义的名称。

一旦将训练数据放置在适当的目录中，您需要在 **TrainDatasetAdd** 节点的 `image_dir` 参数中提供该目录的路径。这告诉节点在哪里找到您的训练图像。

![](https://cdn.runcomfy.com/workflow_assets/1123/readme05.webp)
 ![](https://cdn.runcomfy.com/workflow_assets/1123/readme06.webp)

#### [runcomfy教程](runcomfy教程.md#类别标记)类别标记

![](https://cdn.runcomfy.com/workflow_assets/1123/readme07.webp)

如果您的数据集受益于使用特定的类别标记或触发词，您可以在 `class_tokens` 参数中输入它们。类别标记是附加在每个标题前面的特殊词语或短语，有助于指导模型的生成过程。例如，如果您正在训练一个包含各种动物种类的数据集，您可以使用 "dog"、"cat" 或 "bird" 这样的类别标记来指示生成图像中所需的动物。当您在提示中使用这些类别标记时，您可以控制希望模型生成的特定方面。

#### [runcomfy教程](runcomfy教程.md#设置分辨率宽度和高度批量大小)设置分辨率（宽度和高度）、批量大小

除了 `image_dir` 和 `class_tokens` 参数外，**TrainDatasetAdd** 节点还提供了其他几个选项来微调您的数据集。您可以设置图像的分辨率（宽度和高度）、指定训练的批量大小，以及确定数据集在每个 epoch 中应重复的次数。

#### [runcomfy教程](runcomfy教程.md#多个数据集)多个数据集

![](https://cdn.runcomfy.com/workflow_assets/1123/readme08.webp)

FLUX LoRA 训练的一个强大功能是能够无缝组合多个数据集。在 FLUX LoRA 训练工作流程中，有三个 **TrainDatasetAdd** 节点按顺序连接。每个节点代表一个具有其独特设置的不同数据集。通过将这些节点连接在一起，您可以创建一个丰富且多样化的训练集，包含来自各种来源的图像和标题。

为了说明这一点，让我们考虑一个场景，您有三个单独的数据集：一个用于猫，一个用于狗，另一个用于熊。您可以设置三个 TrainDatasetAdd 节点，每个节点专用于其中一个数据集。在第一个节点中，您将在 `image_dir` 参数中指定 "cats" 数据集的路径，将 `class token` 设置为 "cat"，并根据您的需求调整其他参数，如分辨率和批量大小。同样，您将配置第二个和第三个节点，分别用于 "dogs" 和 "bears" 数据集。

这种方法使 FLUX LoRA 训练过程能够利用多样化的图像，提升模型在不同类别中的泛化能力。

#### [runcomfy教程](runcomfy教程.md#示例)示例

在我们的示例中，我们仅使用一个数据集来训练模型，因此我们启用了一个 **TrainDatasetAdd** 节点并绕过了其他两个。以下是设置方法：

![](https://cdn.runcomfy.com/workflow_assets/1123/readme09.webp)

### [runcomfy教程](runcomfy教程.md#22-设置与初始化)2.2. 设置与初始化

设置与初始化部分是您配置 FLUX LoRA 训练的关键组件和参数的地方。此部分包括几个基本节点，它们共同工作以设置您的训练环境。

### [runcomfy教程](runcomfy教程.md#221-fluxtrainmodelselect)2.2.1. FluxTrainModelSelect

![](https://cdn.runcomfy.com/workflow_assets/1123/readme10.webp)

首先，您有 **FluxTrainModelSelect** 节点，负责选择在 FLUX LoRA 训练期间使用的 FLUX 模型。此节点允许您指定四个关键模型的路径：transformer、VAE（变分自动编码器）、CLIP\_L（对比语言-图像预训练）和 T 5（文本到文本转换器）。这些模型构成了 FLUX 训练过程的骨干，并且都已在 RunComfy 平台上设置。

### [runcomfy教程](runcomfy教程.md#222-optimizerconfig)2.2.2. OptimizerConfig

![](https://cdn.runcomfy.com/workflow_assets/1123/readme11.webp)

**OptimizerConfig** 节点对于在 FLUX LoRA 训练中设置优化器至关重要，优化器决定了模型参数在训练期间的更新方式。您可以选择优化器类型（例如 AdamW、CAME），设置最大梯度范数以防止梯度爆炸，并选择学习率调度器（例如 constant、cosine annealing）。此外，您还可以微调优化器特定参数，如预热步骤和调度器功率，并提供额外参数以进一步自定义。

如果您更喜欢 Adafactor 优化器，它以内存效率和处理大模型的能力而闻名，您可以使用 **OptimizerConfigAdafactor** 节点。

### [runcomfy教程](runcomfy教程.md#223-initfluxloratraining)2.2.3. **InitFluxLoRATraining**

![](https://cdn.runcomfy.com/workflow_assets/1123/readme12.webp)

**InitFluxLoRATraining** 节点是所有关键组件汇聚以启动 FLUX LoRA 训练过程的中心枢纽。

#### [runcomfy教程](runcomfy教程.md#输出目录flux-lora-路径)输出目录：FLUX LoRA 路径

在 InitFluxLoRATraining 节点中，您需要指定的关键事项之一是输出目录，即保存训练模型的位置。在 RunComfy 平台上，您可以选择 `/home/user/ComfyUI/output/{file_name}` 作为输出位置。训练完成后，您可以在文件浏览器中查看它。

![](https://cdn.runcomfy.com/workflow_assets/1123/readme13.webp)
 ![](https://cdn.runcomfy.com/workflow_assets/1123/readme14.webp)

#### [runcomfy教程](runcomfy教程.md#网络维度和学习率)网络维度和学习率

接下来，您需要设置网络维度和学习率。网络维度决定了您的 LoRA 网络的大小和复杂性，而学习率控制了您的模型学习和适应的速度。

#### [runcomfy教程](runcomfy教程.md#最大训练步骤)最大训练步骤

另一个重要参数是 `max_train_steps`。它决定了您希望训练过程运行的时间长度，或者换句话说，您希望模型在完全训练完成之前采取的步骤数。您可以根据您的具体需求和数据集的大小调整此值。这是找到模型学到足够知识以生成出色输出的最佳点的关键。

### [runcomfy教程](runcomfy教程.md#234-fluxtrainvalidationsettings)2.3.4. FluxTrainValidationSettings

![](https://cdn.runcomfy.com/workflow_assets/1123/readme15.webp)

最后，**FluxTrainValidationSettings** 节点允许您配置在 FLUX LoRA 训练过程中评估模型性能的验证设置。您可以设置验证步骤数、图像大小、引导比例和种子以确保可重复性。此外，您可以选择时间步采样方法并调整 sigmoid 比例和偏移参数，以控制时间步调度并提高生成图像的质量。

[runcomfy教程](runcomfy教程.md#3-训练)3\. 训练
---------------

FLUX LoRA 训练的训练部分是魔法发生的地方。它分为四个部分：Train\_01、Train\_02、Train\_03 和 Train\_04。每个部分代表 FLUX LoRA 训练过程的不同阶段，允许您逐步优化和改进模型。

### [runcomfy教程](runcomfy教程.md#31-train_01)3.1. Train\_01

![](https://cdn.runcomfy.com/workflow_assets/1123/readme16.webp)

让我们从 **Train\_01** 开始。这是初始训练循环进行的地方。本部分的核心是 **FluxTrainLoop** 节点，负责执行指定步骤数的训练循环。在本示例中，我们设置为 250 步，但您可以根据需要进行调整。训练循环完成后，训练好的模型将传递给 **FluxTrainSave** 节点，该节点定期保存模型。这确保您在训练的不同阶段拥有模型的检查点，这对于跟踪进度和从任何意外中恢复非常有用。

但训练不仅仅是保存模型。我们还需要验证其性能，以了解其表现如何。这就是 **FluxTrainValidate** 节点的作用。它使用验证数据集测试训练好的模型。此数据集与训练数据分开，有助于评估模型对未见示例的泛化能力。**FluxTrainValidate** 节点根据验证数据生成示例图像，给您提供此阶段模型输出的视觉表示。

为了跟踪训练进度，我们有 **VisualizeLoss** 节点。此节点可视化训练损失随时间的变化，使您可以看到模型的学习情况以及是否收敛到一个好的解决方案。就像有一个私人教练跟踪您的进度并帮助您保持正轨。

### [runcomfy教程](runcomfy教程.md#32-train_02train_03train_04)3.2. Train\_02、Train\_03、Train\_04

在 FLUX LoRA 训练的 **Train\_02** 中，输出进一步训练指定的额外步数（例如 250 步）。**Train\_03** 和 **Train\_04** 遵循类似的模式，更新连接以实现平稳进展。每个阶段输出一个 FLUX LoRA 模型，允许您测试和比较性能。

#### [runcomfy教程](runcomfy教程.md#示例-1)示例

在我们的示例中，我们选择只使用 **Train\_01** 和 **Train\_02**，每个运行 250 步。我们暂时绕过了 **Train\_03** 和 **Train\_04**。但请随时根据您的具体需求和资源进行实验和调整训练部分和步骤数。

![](https://cdn.runcomfy.com/workflow_assets/1123/readme17.webp)

[runcomfy教程](runcomfy教程.md#4-如何以及在哪里使用-flux-和-flux-lora-模型)4\. 如何以及在哪里使用 FLUX 和 FLUX LoRA 模型
---------------------------------------------------------------------

一旦您拥有 FLUX LoRA 模型，您可以将其纳入 [FLUX LoRA workflow](https://www.runcomfy.com/comfyui-workflows/comfyui-flux-realismlora-workflow-photorealistic-ai-images)。用您训练的模型替换现有的 LoRA 模型，然后测试结果以评估其性能。

#### [runcomfy教程](runcomfy教程.md#示例-2)示例

在我们的示例中，我们使用 FLUX LoRA 工作流程通过应用 FLUX LoRA 模型并观察其性能来生成更多影响者图像。

![](https://cdn.runcomfy.com/workflow_assets/1123/readme18.webp)

[runcomfy教程](runcomfy教程.md#许可)许可
---------

查看许可文件：

[flux/model\_licenses/LICENSE-FLUX1-dev](https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev)

[flux/model\_licenses/LICENSE-FLUX1-schnell](https://github.com/black-jsonmodel_licenses/LICENSE-FLUX1-schnell)

FLUX. 1 \[dev\] 模型由 Black Forest Labs. Inc. 根据 FLUX. 1 \[dev\] 非商业许可授权。版权归 Black Forest Labs. Inc. 所有。

在任何情况下，Black Forest Labs, Inc. 均不对因使用此模型而产生的任何索赔、损害或其他责任承担任何责任，无论是在合同诉讼、侵权行为或其他方面。