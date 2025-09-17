## mqtt

mqtt 填写
```
base_topic: zigbee2mqtt
server: mqtt://core-mosquitto:1883
user: homeassistant
password: sahNoh8too3uzigiefeidee4YohBai6eeWaeSiechohco6ookai7ael5ne3iebai
```
serial 填写
port: /dev/ttyACM0
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404010947514.png)


1、进入ZigBee2MQTT插件，在配置中的serial中添加port: /dev/ttyACM0，保存

2. 重启ZigBee2MQTT插件或者直接重启HomeAssistant系统

> 注1：
port: /dev/ttyACM0这行英文的意思是告诉zigbee2mqtt插件：zigbee网关的地址是dev目录下的ttyACM0设备
但ttyACM0这个地址是相对地址，并不绝对，在某些设备上也许表现出不同的设备名
您可以在HA系统的终端（Terminal & SSH加载项插件）执行ls /dev/ | grep tty命令查看该网关的设备名， 如果您不明白这是什么意思，也不会操作，那么请购买我们的HA服务器，我们已经配置好了这一切



```
port: /dev/ttyUSB0
```



如果想在设备与服务中进行管理，请按下图操作点击配置

点击配置

点击设备和服务

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403271834036.png)

点击MQTT

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403271834037.png)

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403271834038.png)

包括水浸传感器在内，这些都是ZigBee2MQTT插件下的设备

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403271834039.png)



