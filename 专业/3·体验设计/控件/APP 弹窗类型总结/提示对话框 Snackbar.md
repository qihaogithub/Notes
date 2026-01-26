## 定义
[Material Design官方指南](https://m3.material.io/components/snackbar/overview)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404231019326.png)
Snack bar 是一种轻量的弹窗形式，被用来通知用户当前程序正在发生或即将发生的进程，它的内容一定是和用户当前操作相关的。

## 历史
在早期版本的 Android 操作系统中，开发者主要依赖 Toast 和 Dialog 等组件来向用户提供反馈。Toast 是一种简单的提示信息，它会在屏幕上短暂显示，但不允许用户交互。而 Dialog 则是一种更为复杂的对话框，会打断用户的当前操作，要求用户进行响应。然而，这些组件在提供即时反馈和保持界面连贯性方面存在一定的局限性。

随着 Android 操作系统的不断发展和 Material Design 设计理念的兴起，开发者开始寻求更加轻量级和非阻断性的反馈机制。在这种背景下，Snackbar 组件应运而生。Snackbar 最初作为 Material Design 的一部分被引入，它结合了 Toast 的短暂显示和 Dialog 的交互性，为用户提供了更加灵活和便捷的反馈方式。

随着时间的推移，Snackbar在Android应用中的使用逐渐普及，并成为UI设计中不可或缺的一部分。开发者开始探索Snackbar在不同场景下的应用，并不断优化其设计和交互方式。例如，Snackbar的显示位置、动画效果、样式和交互方式等都得到了不断的改进和完善。


## 规范

- 点心不应该打断用户的体验
- 通常出现在 UI 的底部
- 可以自动消失或者保持在屏幕上，直到用户采取行动


### 结构
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404231020558.png)
1. 容器
2. 支持文本
3. 行动（可选）
4. 关闭按钮（可选）
### 容器
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404231023819.png)
Snackbar容器使用带有阴影的纯色背景色来突出内容，容器应该完全不透明，以便文本标签保持清晰可辨。

### Leading

非必要元素，可选 Icon 、与内容强相关的图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7HrnvSgNWHQYLictJf1L38a4mWzlKOxb2j15QBRnCeIkhtbibgAztbPT5ngYFx7xYyUsEynX82SKhq2hwar5CpcA/640?wx_fmt=png&from=appmsg)

### Button

Button 采用独特色彩 / 样式，以突出其与文案的区别

非必要元素，可选 0-2 个操作（包含 Close）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7HrnvSgNWHQYLictJf1L38a4mWzlKOxb2TzxqdiaxMialbSXouPWicsjldiauibrdLqS0ZIIsBXBQ5pxyJ3JwQibVU4iag/640?wx_fmt=png&from=appmsg)

### Text

简洁明了，避免冗长和复杂的描述，同时确保用户在查看后不会感到干扰

文案内容推荐和当前进程/未来进程直接相关，可带引导性

推荐保持一行文案，移动端展示最多两行

首行文案推荐为标题，言简意赅；第二行文案为辅助说明（小字）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7HrnvSgNWHQYLictJf1L38a4mWzlKOxb2fSEFKKJEL4h0TU3OnOQ1n1fkbSlv6r010WZktUV17vIrnnJIcMjwTQ/640?wx_fmt=png&from=appmsg)

### 位置

建议显示在屏幕底部（高于安全边距 8 pt）

当同时有多个时，一个一个出现，一次只显示 1 个

避免其遮住导航、频繁使用的其他元素/组件

不可与 FAB 重叠，应该位于其上方（导航栏同理）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7HrnvSgNWHQYLictJf1L38a4mWzlKOxb2SJ37XaCIoVYjYzVqsuSE5p26wqLI2LIrG0BeWmeSdfDKrqN0SAibvlw/640?wx_fmt=png&from=appmsg)

### 持续时间

根据 Material Design Guideline，建议 4-10 s 自动消失

带 Close 可等待用户操作后消失

会自动消失的 Snackbar 建议不带 Close

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7HrnvSgNWHQYLictJf1L38a4mWzlKOxb2mwdf7Adibh7iacKiaz5RJ4Bj5XPkSA3kd9DnUbPRwDbGpt12DlOsmgO5w/640?wx_fmt=png&from=appmsg)


## 相关控件
Snackbar 和其他弹窗的区别
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404231007332.png)


## 相关文献

[那些底部弹起都算Snackbar么？](https://mp.weixin.qq.com/s/wwPlBrvc1YbdYJhReGxTJA)
