---
column1:
  - AI
---
[使用教程](https://www.yuque.com/u32937722/qb6y63/kvgsxlsy7gqgfrz7)

# 准备工作  

## 去 discord 官网注册一个 discord 账号（类似于注册微信号）
discord官网链接:www.discord.com
·点击login
·点击注册

## 去 Midjourney 的官网加入他们的服务器。  
类似于有了微信号，但要加入群聊
官网链接：www.midjourney.com  
·点击Join the Beta
·点击接受邀请



## [[命令]]

##  [[后缀参数]]

## [[垫图操作]]

##  [[seed用法]]

## [[添加chatgpt 机器人]]
### 权重切分符与负面描述词反向描述词
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312174116.png)
结论1：英文双冒号（权重切分符）可以起到 「切分语义」的作用。

拆解：比如这里 hot dog 连起来本来意思是 「热狗」，但是用::切分后就变成了「一只感觉很热的狗」

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312174301.png)
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312174340.png)
--n0 后缀代表「负面/反向关键词」，效果等同于权重切分符加上数值 -0.5
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312174441.png)
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312174514.png)
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312174602.png)
另外，我们的 v1~v3 模型是不支持小数点的，但是 V4 可以，还有每一个部分权重加起来的总和必须是正数

### --tile 后缀参数生成无缝贴图
目前支持 v1~v3模型和 test testp 模型（以及即将到来的 v5 模型）
检查无缝贴图效果的网站：https://www.pycheung.com/checker/
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312175054.png)
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312175120.png)


### quality 后缀参数
1、系统默认加上--q1；除非你用 /prefer suffix 指令设置了默认后缀
2、注意：/prefer suffix 是用来设置每一次都会默认加在 prompt 末尾的词句；如果要去除，那就再输入一次 /prefer suffix 并道接回车） 
3、举例：/prefer suffix --v4--ar 16：9，那么每次输入7 prompt 就会默认加上 --v4 --ar 16：9

--q .5,意思就是0.5，所花费GPU时间正常的0.5倍，出来的画面会比较朦胧

--quality 有.251.5/1/2四种
但是数值越高并不代表像素越大，画质越高你需要根据具体主题自行决定，比如「建筑类」摄影照片（突出结构线条的）就可能需要q大一点

--v4 默认升档器用得最多（培加图像大小，同时平滑或细化细节） --upanime(是 niji 模型默认用到的升档器，当你加上之后，点击
U按钮就会使用这个升档器）
--upbeta （升档的图片很光滑）
--uplight（只添加少量的纹理）

v4和nji不支持--q2，所以写2也沒有用
quality 只影响初始四宫格
quality 影响GPU花费的时间 
quality 并不影响像素大小

### stylize 后缀参数
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312180223.png)
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312180300.png)




## 如何订阅付费Midjourney？
在频道对话框输入『 /subscribe 』，会跳出专属付费连结.


## 如何查看自己帐号资讯？
在频道对话框输入『 /info 』
 



## 产出连续人物
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230312193316.png)



## 生成图片是免费的吗？

A：新用户有25次的免费使用额度，超过的需要开会员，会员分10美刀和30美刀两种方式。

10美刀：每月可以生成200张图片，适合轻度使用者。

30美刀：每月生成的图片无限制，每月15小时的fast使用时长。

## fast模式和relax模式有何区别？

A：在输入框输入/fast或者/relax即可切换模式，默认是快模式。

fast模式：无需排队，一发送描述语到公屏上，立马生成。

relax模式：需要在服务器排队，有时快有时慢，排队完成自动生成。

# 万能描述公式
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230317160256.png)
