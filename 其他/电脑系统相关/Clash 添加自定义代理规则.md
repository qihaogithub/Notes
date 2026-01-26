订阅转换：
https://sub.suda-cdn.com/
https://acl4ssr-sub.github.io/
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230912111029.png)

suda 订阅链接
https://api.suda-cdn.com/sub?target=clash&url=https://subbs.susuda.sslcdnapp.net/link/wkAG7IzLQ9OATl2y?clash=2&new_name=true
雷霆订阅地址
https://api.leiting.app/api/v1/client/subscribe?token=d4c389eed920fff97583c9b1ee29d4e5
一元机场
https://sub3.smallstrawberry.com/api/v1/client/subscribe?token=9ac8aff3dd99c4a5993c6a3c2902a8f7



## 远程配置
订阅转换是放到远程配置那一列
https://raw.githubusercontent.com/qihaogithub/Rules/master/config/full.ini
## 自定义订阅链接
https://suo.st/MRSpJ3N
教程原文链接：
https://v2ex.com/t/949462
https://blog.xiaohack.org/4665.html
https://github.com/chinnsenn/ClashCustomRule


## 规则列表写法


```
custom_proxy_group=🚀 手动切换`select`(^(?!.*(IPV6|用户|本站|漏洞|永久虚通路)).*)
```

这看起来像是一个配置或设置字符串，可能是用于某种网络或代理服务的配置。让我解释其中的一些部分：
`custom_proxy_group`：这似乎是一个自定义代理组的名称或标识符。
`手动切换`：这可能指的是手动切换代理设置的操作或功能。
`select`(^(?!._(IPV6|用户|本站|漏洞|永久虚通路))._)：这是一个正则表达式，用于选择特定条件下的代理或过滤代理。该正则表达式的含义是排除包含"IPV6"、"用户"、"本站"、"漏洞"、"永久虚通路"等关键词的代理。


```
custom_proxy_group=♻️ 自动选择`url-test`(^(?!.*(IPV6|用户|本站|漏洞|永久虚通路)).*)`http://www.gstatic.com/generate_204`7200,5,50
```

1. `custom_proxy_group`：这仍然是一个自定义代理组的名称或标识符。
    
3. `自动选择`：这表示代理组将以自动方式选择代理，而不需要手动干预。
    
4. `url-test`(^(?!._(IPV6|用户|本站|漏洞|永久虚通路))._)`http://www.gstatic.com/generate_204`7200,5,50`：这是一个更为详细的配置，用于自动选择代理的方式：
    
    - `url-test`：这可能是一种代理选择的测试方式，它可能会检查指定的URL以确保代理的可用性。
        
    - `^(?!.*(IPV6|用户|本站|漏洞|永久虚通路)).*`：这是一个正则表达式，与之前相同，用于排除包含特定关键词的代理。
        
    - `http://www.gstatic.com/generate_204`：这是要测试的URL，以检查代理的可用性。
        
    - `7200,5,50`：这可能是有关代理测试的更多设置，但需要更多上下文来解释确切的含义。

##  故障转移和负载均衡

🔯 故障转移（Fallback）和🔮 负载均衡（Load Balancing）是网络代理或 VPN 服务中常见的两种策略，用于确保服务的稳定性和可用性。它们有不同的作用和目的：

1. 🔯 故障转移（Fallback）：
    
    - 故障转移是一种策略，用于在一个节点或服务器不可用时自动切换到备用节点或服务器。
    - 当您使用故障转移时，系统会检测主要节点的可用性。如果主要节点发生故障或不可用，系统会自动切换到备用节点，以确保服务的连续性。
    - 这对于保持服务的可用性非常重要，因为它允许在主要节点发生问题时无需手动干预即可切换到备用节点。
2. 🔮 负载均衡（Load Balancing）：
    
    - 负载均衡是一种策略，用于平衡服务器或节点之间的负载，以确保请求被均匀分配到不同的服务器上。
    - 当您使用负载均衡时，请求会根据一定的算法分配到可用的服务器上。这可以减轻单个服务器上的负载，提高系统的性能和可扩展性。
    - 负载均衡通常用于高流量的网络服务，以确保各个服务器都能充分利用，而不会出现过载或性能问题。

在您的Clash配置文件中，🔯 故障转移和🔮 负载均衡都是自定义代理组的一部分，用于定义节点选择策略。故障转移组将请求路由到备用节点，以防主要节点不可用。负载均衡组将请求均匀分配到多个节点，以确保负载平衡。

这些策略的选择取决于您的具体需求。如果您关心可用性和故障恢复，那么故障转移可能更适合您。如果您希望分散负载以提高性能，那么负载均衡可能更合适。

## yaml 基本语法
- DOMAIN-SUFFIX：域名后缀匹配
- DOMAIN：域名匹配
- DOMAIN-KEYWORD：域名关键字匹配
- IP-CIDR：IP 段匹配
- SRC-IP-CIDR：源 IP 段匹配
- GEOIP：GEOIP 数据库（国家代码）匹配
- DST-PORT：目标端口匹配
- SRC-PORT：源端口匹配
- PROCESS-NAME：源进程名匹配
- RULE-SET：Rule Provider 规则匹配
- MATCH：全匹配
### DOMAIN -SUFFIX 和 DOMAIN-KEYWORD
`DOMAIN-SUFFIX` 和 `DOMAIN-KEYWORD` 是 Clash 代理工具中用于匹配域名的两种不同规则类型，它们有以下不同点：

1. 匹配方式：
   - `DOMAIN-SUFFIX` 规则用于匹配域名的后缀，它匹配以指定后缀结尾的域名。例如，`DOMAIN-SUFFIX,example.com` 匹配所有以 ". Example. Com" 结尾的域名。
   - `DOMAIN-KEYWORD` 规则用于匹配域名中的关键词，它匹配包含指定关键词的域名。例如，`DOMAIN-KEYWORD,google` 匹配所有包含 "google" 关键词的域名。

2. 匹配精度：
   - `DOMAIN-SUFFIX` 规则通常用于匹配特定网站或服务的域名后缀，因此匹配精度较高，可以准确匹配特定的域名后缀。
   - `DOMAIN-KEYWORD` 规则用于匹配域名中的关键词，因此匹配精度较低，可能匹配到包含指定关键词的多个域名，不仅限于特定后缀。

3. 示例用途：
   - `DOMAIN-SUFFIX` 适用于需要将特定域名后缀的流量走代理的情况，例如将所有 ". Example. Com" 域名的流量定向到代理服务器。
   - `DOMAIN-KEYWORD` 适用于需要根据域名中包含的关键词来匹配流量的情况，例如将所有包含 "google" 关键词的域名的流量定向到代理服务器。

需要根据具体的代理需求和要匹配的域名特征来选择使用哪种规则类型。通常，`DOMAIN-SUFFIX` 用于较精确的域名匹配，而 `DOMAIN-KEYWORD` 用于更灵活的关键词匹配。