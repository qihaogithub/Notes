serverAddr = "152.32.226.106"
serverPort = 7000
auth.method = "token"
auth.token = "60d8a83c544e6168db"

[[proxies]]
name = "tcp-8088"
type = "tcp"
localIP = "127.0.0.1"
localPort = 8088
remotePort = 8088

[[proxies]]
name = "tcp-bt-panel"
type = "tcp"
localIP = "192.168.31.251"
localPort = 21652
remotePort = 21652