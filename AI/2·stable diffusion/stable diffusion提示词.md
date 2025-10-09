
提示词内输入的东西就是你想要画的东西，反向提示词内输入的就是你不想要画的东西。

提示框内只能输入英文，所有符号都要使用英文半角，词语之间使用半角逗号隔开。

![超详细！外婆都能看懂的Stable Diffusion入门教程](https://image.uisdc.com/wp-content/uploads/2023/04/uisdc-wp-20230418-34.jpg)

一般来说越靠前的词汇权重就会越高，比如我这张图的提示词：

The personification of the Halloween holiday in the form of a cute girl with short hair and a villain's smile, (((cute girl))) cute hats, cute cheeks, unreal engine, highly detailed, artgerm digital illustration, woo tooth, studio ghibli, deviantart, sharp focus, artstation, by Alexei Vinogradov bakery, sweets, emerald eyes。

万圣节假期的拟人化形式是一个留着短发和恶棍笑容的可爱女孩，可爱的帽子，可爱的脸颊，虚幻的引擎，高度详细，艺术种子数字插图，woo tooth，吉卜力工作室，deviantart，锐利的焦点，artstation，由 Alexei Vinogradov 面包店，糖果，绿宝石般的眼睛。

第一句关键词词组：万圣节假期的拟人化形式是一个留着短发和恶棍笑容的可爱女孩。那生成的图片主体画面就会是万圣节短发可爱笑容女孩

![超详细！外婆都能看懂的Stable Diffusion入门教程](https://image.uisdc.com/wp-content/uploads/2023/04/uisdc-wp-20230418-35.jpg)

这里可能有用过 Midjourney 的小伙伴们就有疑问了，(((cute girl)))是什么意思，为啥有这么多括号，我来为大家解答下，这个是权重调节，类似 Midjourney 的 ::

① 最直接的权重调节就是调整词语顺序，越靠前权重越大，越靠后权重越低，上面说过。

② 可以通过下面的语法来对关键词设置权重，一般权重设置在 0.5~2 之间，可以通过选中词汇，按 ctrl+↑↓来快速调节权重，每次调节为 0.1，也可以直接输入。

![超详细！外婆都能看懂的Stable Diffusion入门教程](https://image.uisdc.com/wp-content/uploads/2023/04/uisdc-wp-20230418-36.jpg)

③ 加英文输入的（），一个括号代表这组关键词的权重是 1.1，两个括号是 1.1*1.1 的权重，不要加太多了哈。可以结合第二点固定权重，比如 (((cute girl: 1.2)))，那这个关键词的权重就很高了。

### 权重
以 girl 这个 Tag 作为例子。
(girl) 加权重，这里是 1.1 倍
((girl)) 加很多权重。1.1*1.1=1.21 倍
[girl] 减权重，一般用的少。减权重也一般就用下面的指定倍数。
(girl: 1.5) 指定倍数，这里是 1.5 倍的权重。
(girl: 0.9) 达到减权重的效果

