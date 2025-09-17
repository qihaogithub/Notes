教程汇总
[https://www.hachina.io/](https://www.hachina.io/)

#  [[安装homeassistant]]

# [[安装hacs]]

# [[ZigBee2MQTT]]
# [[HA中通过Mosquitto安装MQTT服务器]]

# [[手动安装插件]]

[[使用阿里云镜像加速器]]
# 添加设备
## Xiaomi Miot Auto
[https://www.bilibili.com/video/BV1t8411M7oz/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d](https://www.bilibili.com/video/BV1t8411M7oz/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)


## 接入智能音响
### 巴法云
[https://www.bilibili.com/video/BV1mF411L7MK/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d](https://www.bilibili.com/video/BV1mF411L7MK/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)
### HassLife
接入天猫精灵/小爱同学的另一种办法
https://www.blear.cn/article/tmall-homeassistant
https://hass.blear.cn/register.php
## [[Node-RED]]

# 主题

[https://www.bilibili.com/video/BV1pk4y1G7vd/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d](https://www.bilibili.com/video/BV1pk4y1G7vd/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)

# 问题解决

## 报错被阻止执行，系统不正常

```
'AddonManager.install' blocked from execution, system is not healthy - supervisor
```
在配置文件根目录下 (如：/usr/share/hassio) 新建一个文件 jobs. Json，将以下代码复制粘贴进去。 {"ignore_conditions": ["healthy"]}
原文： https://tieba.baidu.com/p/8290518017