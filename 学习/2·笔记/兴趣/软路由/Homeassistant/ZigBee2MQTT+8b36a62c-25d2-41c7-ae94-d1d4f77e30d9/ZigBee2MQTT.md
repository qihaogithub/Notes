## 安装

加载项商店中添加库：

https://github.com/zigbee2mqtt/hassio-zigbee2mqtt

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403271834985.png)

加载项商店中安装Mosquitto broker，否则ZigBee2MQTT无法使用

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403271834986.png)

## 简介

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403271834987.png)

zigbee2mqtt官网：https://www.zigbee2mqtt.io/

支持的设备[https://www.zigbee2mqtt.io/supported-devices/](https://www.zigbee2mqtt.io/supported-devices/)

## cc2531

![https://www.hachina.io/15.zigbee%E8%AE%BE%E5%A4%87%E6%8E%A5%E5%85%A5/images/cc2531.jpg](cc2531.jpg)

- zigbee2mqtt支持各种zigbee dangle(adapter)

- cc2531是最常见的zigbee芯片

- zigbee dangle需要烧写固件，不同的dangle烧写固件的方法是不同的

插件地址

[https://github.com/zigbee2mqtt/hassio-zigbee2mqtt#installation](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt#installation)

设置教程

[https://www.yuque.com/yuqueyonghuc0smtf/uaz8rz/pbc20z4md5axb06g?singleDoc#](https://www.yuque.com/yuqueyonghuc0smtf/uaz8rz/pbc20z4md5axb06g?singleDoc#)

## 配置

[ Zigbee2MQTT配置](ZigBee2MQTT+8b36a62c-25d2-41c7-ae94-d1d4f77e30d9/+Zigbee2MQTT%E9%85%8D%E7%BD%AE%20074cde97-bfff-4e55-93d4-b2831b3b2796.md)



## 添加ZigBee终端设备

1、点击右上角的允许添加新设备(所有)，ZigBee网关会进入搜索设备状态（该状态会在四分钟后自动解除）
2、此时将ZigBee终端设备重置（依照ZigBee终端设备的说明书进行，一般是长按重置键直至指示灯闪烁）
3、然后将ZigBee终端设备尽量靠近ZigBee网关，即可添加成功



ZigBee2MQTT支持的欧瑞博设备

两位开关

[https://www.zigbee2mqtt.io/devices/T21W2Z.html](https://www.zigbee2mqtt.io/devices/T21W2Z.html)

三位开关

[https://www.zigbee2mqtt.io/devices/T30W3Z.html](https://www.zigbee2mqtt.io/devices/T30W3Z.html)

电动窗帘

[https://www.zigbee2mqtt.io/devices/W45CZ.html](https://www.zigbee2mqtt.io/devices/W45CZ.html)

智能紧急按钮

官方详情页[https://www.orvibo.com/cn/product/sos.html](https://www.orvibo.com/cn/product/sos.html)

## HomeAssistant中常用的几种连接zigbee设备的方式

- 设备厂商的网关（比如小米网关、Ikea的网关）

    - 通过HomeAssistant中的专用组件接入（比如[Xiaomi Aqara Gateway](https://www.home-assistant.io/integrations/xiaomi_aqara/)）

    - 仅支持厂家的zigbee设备

    - 可能需要通过隐秘的方法获得连接的key

- 支持Homekit的网关（比如小米多模网关）

    - 可通过[HomeKit Controller](https://www.home-assistant.io/integrations/homekit_controller/)组件接入

- zigbee2mqtt

    - 将zigbee协议转化成mqtt协议，通过mqtt组件接入HomeAssistant

    - 连接环节多，配置复杂

- deCONZ

    - zigbee网关硬件仅支持RaspBee或ConBee

    - 通过[deCONZ add-on](https://github.com/home-assistant/addons/tree/master/deconz)和[deCONZ组件](https://www.home-assistant.io/integrations/deconz/)接入

- ZHA

    - 直接通过HomeAssistant的[Zigbee Home Automation组件](https://www.home-assistant.io/integrations/zha/)接入

    - 无需安装额外的add-on或软件

    - 支持的硬件（zigbee网关和zigbee设备）比较广泛

    ![https://www.hachina.io/15.zigbee%E8%AE%BE%E5%A4%87%E6%8E%A5%E5%85%A5/images/zha.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403271834988.png)





支持新设备[https://www.zigbee2mqtt.io/advanced/support-new-devices/01_support_new_devices.html#_1-pairing-the-device-with-zigbee2mqtt](https://www.zigbee2mqtt.io/advanced/support-new-devices/01_support_new_devices.html#_1-pairing-the-device-with-zigbee2mqtt)

