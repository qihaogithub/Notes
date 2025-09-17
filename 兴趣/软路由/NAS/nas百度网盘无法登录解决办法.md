1.在终端执行以下两条命令  
sudo docker exec baiduapp sed -i 's/$/|xargs -I {} echo {}1/' /sh/address.sh  
sudo docker exec baiduapp sh /sh/address.sh  
2.再执行下sudo docker restart baiduapp 这个重启下docker  
（注意命令只要执行一次，登录成功后就不能再执行了）

[原始网站地址](https://tieba.baidu.com/p/8850971049)