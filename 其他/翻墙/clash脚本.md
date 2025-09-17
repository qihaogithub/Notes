
```
// 国内DNS服务器
const domesticNameservers = [
  "https://dns.alidns.com/dns-query", // 阿里云公共DNS
  "https://doh.pub/dns-query", // 腾讯DNSPod
  "https://doh.360.cn/dns-query", // 360安全DNS
];
// 国外DNS服务器
const foreignNameservers = [
  "https://1.1.1.1/dns-query", // Cloudflare(主)
  "https://1.0.0.1/dns-query", // Cloudflare(备)
  "https://208.67.222.222/dns-query", // OpenDNS(主)
  "https://208.67.220.220/dns-query", // OpenDNS(备)
  "https://194.242.2.2/dns-query", // Mullvad(主)
  "https://194.242.2.3/dns-query", // Mullvad(备)
];
// DNS配置
const dnsConfig = {
  enable: true,
  listen: "0.0.0.0:1053",
  ipv6: true,
  "use-system-hosts": false,
  "cache-algorithm": "arc",
  "enhanced-mode": "fake-ip",
  "fake-ip-range": "198.18.0.1/16",
  "fake-ip-filter": [
    // 本地主机/设备
    "+.lan",
    "+.local",
    // Windows网络出现小地球图标
    "+.msftconnecttest.com",
    "+.msftncsi.com",
    // QQ快速登录检测失败
    "localhost.ptlogin2.qq.com",
    "localhost.sec.qq.com",
    // 微信快速登录检测失败
    "localhost.work.weixin.qq.com",
  ],
  "default-nameserver": ["223.5.5.5", "119.29.29.29", "1.1.1.1", "8.8.8.8"],
  nameserver: [...domesticNameservers, ...foreignNameservers],
  "proxy-server-nameserver": [...domesticNameservers, ...foreignNameservers],
  "nameserver-policy": {
    "geosite:private,cn,geolocation-cn": domesticNameservers,
    "geosite:google,youtube,telegram,gfw,geolocation-!cn": foreignNameservers,
  },
};
// 规则集通用配置
const ruleProviderCommon = {
  type: "http",
  format: "yaml",
  interval: 86400,
};
// 规则集配置
const ruleProviders = {
  reject: {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/reject.txt",
    path: "./ruleset/loyalsoldier/reject.yaml",
  },
  icloud: {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/icloud.txt",
    path: "./ruleset/loyalsoldier/icloud.yaml",
  },
  apple: {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/apple.txt",
    path: "./ruleset/loyalsoldier/apple.yaml",
  },
  google: {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/google.txt",
    path: "./ruleset/loyalsoldier/google.yaml",
  },
  proxy: {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt",
    path: "./ruleset/loyalsoldier/proxy.yaml",
  },
  direct: {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/direct.txt",
    path: "./ruleset/loyalsoldier/direct.yaml",
  },
  private: {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/private.txt",
    path: "./ruleset/loyalsoldier/private.yaml",
  },
  gfw: {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/gfw.txt",
    path: "./ruleset/loyalsoldier/gfw.yaml",
  },
  "tld-not-cn": {
    ...ruleProviderCommon,
    behavior: "domain",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/tld-not-cn.txt",
    path: "./ruleset/loyalsoldier/tld-not-cn.yaml",
  },
  telegramcidr: {
    ...ruleProviderCommon,
    behavior: "ipcidr",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/telegramcidr.txt",
    path: "./ruleset/loyalsoldier/telegramcidr.yaml",
  },
  cncidr: {
    ...ruleProviderCommon,
    behavior: "ipcidr",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/cncidr.txt",
    path: "./ruleset/loyalsoldier/cncidr.yaml",
  },
  lancidr: {
    ...ruleProviderCommon,
    behavior: "ipcidr",
    url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/lancidr.txt",
    path: "./ruleset/loyalsoldier/lancidr.yaml",
  },
  // applications: {
  //   ...ruleProviderCommon,
  //   behavior: "classical",
  //   url: "https://fastly.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/applications.txt",
  //   path: "./ruleset/loyalsoldier/applications.yaml",
  // },
  openai: {
    ...ruleProviderCommon,
    behavior: "classical",
    url: "https://fastly.jsdelivr.net/gh/blackmatrix7/ios_rule_script@master/rule/Clash/OpenAI/OpenAI.yaml",
    path: "./ruleset/blackmatrix7/openai.yaml",
  },
};
// 规则
const rules = [
  // 自定义规则
  // 自定义直联规则
  "DOMAIN-KEYWORD,youdao,DIRECT",
  "DOMAIN-SUFFIX,coze.cn,DIRECT",
  // 自定义代理规则
  "DOMAIN-SUFFIX,v2rayssr.com,节点选择", // 一个博客，大陆ip不让访问
  "DOMAIN-SUFFIX,openaipublic.blob.core.windows.net,节点选择",
  "DOMAIN-SUFFIX,notebooklm.google,节点选择",
  // adobe 域名
  // "DOMAIN-KEYWORD,adobe,REJECT",
  "DOMAIN-SUFFIX,adobe.com,Adobe",
  "DOMAIN-SUFFIX,adobe.io,Adobe",
  "DOMAIN-SUFFIX,adobelogin.com,Adobe",
  "DOMAIN-SUFFIX,adobeid-na1.services.adobe.com,Adobe",
  "DOMAIN-SUFFIX,adobeoobe.com,Adobe",
  // # figma
  // "DOMAIN-KEYWORD,figma",
  "DOMAIN-SUFFIX,figma.com,🎨 Figma",
  "DOMAIN-SUFFIX,figma.net,🎨 Figma",
  // anthropic
  "DOMAIN-KEYWORD,anthropic,ChatGPT",
  "DOMAIN-SUFFIX,claude.ai,ChatGPT",
  "DOMAIN,servd-anthropic-website.b-cdn.net,ChatGPT",
  // groq
  "DOMAIN-KEYWORD,groq,ChatGPT",
  // gemini
  "DOMAIN-SUFFIX,googleapis.com,ChatGPT",
  "DOMAIN-SUFFIX,aistudio.google.com,ChatGPT",
  // cursor
  "DOMAIN-KEYWORD,cursor,节点选择",
  // google
  "DOMAIN-SUFFIX,googleapis.cn,节点选择", // Google服务
  "DOMAIN-SUFFIX,gstatic.com,节点选择", // Google静态资源
  "DOMAIN-SUFFIX,xn--ngstr-lra8j.com,节点选择", // Google Play下载服务
  "DOMAIN-SUFFIX,github.io,节点选择", // Github Pages
  "DOMAIN,v2rayse.com,节点选择", // V2rayse节点工具
  // blackmatrix7 规则集
  "RULE-SET,openai,ChatGPT",
  // Loyalsoldier 规则集
  // "RULE-SET,applications,全局直连",
  "RULE-SET,private,全局直连",
  "RULE-SET,reject,广告过滤",
  "RULE-SET,icloud,微软服务",
  "RULE-SET,apple,苹果服务",
  "RULE-SET,google,谷歌服务",
  "RULE-SET,proxy,节点选择",
  "RULE-SET,gfw,节点选择",
  "RULE-SET,tld-not-cn,节点选择",
  "RULE-SET,direct,全局直连",
  "RULE-SET,lancidr,全局直连,no-resolve",
  "RULE-SET,cncidr,全局直连,no-resolve",
  "RULE-SET,telegramcidr,电报消息,no-resolve",
  // 其他规则
  "GEOIP,LAN,全局直连,no-resolve",
  "GEOIP,CN,全局直连,no-resolve",
  "MATCH,漏网之鱼",
];
// 代理组通用配置
const groupBaseOption = {
  interval: 300, // 表示每 300 秒进行一次检测
  timeout: 3000, // 表示检测超时时间
  url: "https://www.google.com/generate_204",
  lazy: true,
  "max-failed-times": 3,
  hidden: false,
};

// 程序入口
function main(config) {
  const proxyCount = config?.proxies?.length ?? 0;
  const proxyProviderCount =
    typeof config?.["proxy-providers"] === "object"
      ? Object.keys(config["proxy-providers"]).length
      : 0;
  if (proxyCount === 0 && proxyProviderCount === 0) {
    throw new Error("配置文件中未找到任何代理");
  }

  // 覆盖原配置中DNS配置
  config["dns"] = dnsConfig;

  // 覆盖原配置中的代理组
  config["proxy-groups"] = [
    {
      ...groupBaseOption,
      name: "节点选择",
      type: "select",
      proxies: ["延迟选优", "故障转移", "负载均衡(散列)", "负载均衡(轮询)"],
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/adjust.svg",
    },
    {
      ...groupBaseOption,
      name: "🎨 Figma",
      type: "select",
      url: "https://www.figma.com",
      interval: 300,
      tolerance: 50,
      proxies: ["节点选择", "延迟选优"],
      "include-all": true,
      icon: "https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202412111622083.svg",
    },
    {
      ...groupBaseOption,
      name: "Adobe",
      type: "select",
      proxies: ["全局拦截", "全局直连", "延迟选优"],
      "include-all": true,
      icon: "https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202412111631129.svg",
    },
    {
      ...groupBaseOption,
      name: "延迟选优",
      type: "url-test",
      tolerance: 100,
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/speed.svg",
    },
    {
      ...groupBaseOption,
      name: "故障转移",
      type: "fallback",
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/ambulance.svg",
    },
    {
      ...groupBaseOption,
      name: "负载均衡(散列)",
      type: "load-balance",
      strategy: "consistent-hashing",
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/merry_go.svg",
    },
    {
      ...groupBaseOption,
      name: "负载均衡(轮询)",
      type: "load-balance",
      strategy: "round-robin",
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/balance.svg",
    },
    {
      ...groupBaseOption,
      name: "谷歌服务",
      type: "select",
      proxies: [
        "节点选择",
        "延迟选优",
        "故障转移",
        "负载均衡(散列)",
        "负载均衡(轮询)",
        "全局直连",
      ],
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/google.svg",
    },
    {
      ...groupBaseOption,
      name: "国外媒体",
      type: "select",
      proxies: [
        "节点选择",
        "延迟选优",
        "故障转移",
        "负载均衡(散列)",
        "负载均衡(轮询)",
        "全局直连",
      ],
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/youtube.svg",
    },
    {
      ...groupBaseOption,
      name: "电报消息",
      type: "select",
      proxies: [
        "节点选择",
        "延迟选优",
        "故障转移",
        "负载均衡(散列)",
        "负载均衡(轮询)",
        "全局直连",
      ],
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/telegram.svg",
    },
    {
      ...groupBaseOption,
      url: "https://chatgpt.com",
      "expected-status": "200",
      name: "ChatGPT",
      type: "select",
      "include-all": true,
      filter:
        "AD|🇦🇩|安道尔|AE|🇦🇪|阿联酋|AF|🇦🇫|阿富汗|AG|🇦🇬|安提瓜和巴布达|AL|🇦🇱|阿尔巴尼亚|AM|🇦🇲|亚美尼亚|AO|🇦🇴|安哥拉|AR|🇦🇷|阿根廷|AT|🇦🇹|奥地利|AU|🇦🇺|澳大利亚|AZ|🇦🇿|阿塞拜疆|BA|🇧🇦|波黑|BB|🇧🇧|巴巴多斯|BD|🇧🇩|孟加拉国|BE|🇧🇪|比利时|BF|🇧🇫|布基纳法索|BG|🇧🇬|保加利亚|BH|🇧🇭|巴林|BI|🇧🇮|布隆迪|BJ|🇧🇯|贝宁|BN|🇧🇳|文莱|BO|🇧🇴|玻利维亚|BR|🇧🇷|巴西|BS|🇧🇸|巴哈马|BT|🇧🇹|不丹|BW|🇧🇼|博茨瓦纳|BZ|🇧🇿|伯利兹|CA|🇨🇦|加拿大|CD|🇨🇩|刚果（金）|CF|🇨🇫|中非|CG|🇨🇬|刚果（布）|CH|🇨🇭|瑞士|CI|🇨🇮|科特迪瓦|CL|🇨🇱|智利|CM|🇨🇲|喀麦隆|CO|🇨🇴|哥伦比亚|CR|🇨🇷|哥斯达黎加|CV|🇨🇻|佛得角|CY|🇨🇾|塞浦路斯|CZ|🇨🇿|捷克|DE|🇩🇪|德国|DJ|🇩🇯|吉布提|DK|🇩🇰|丹麦|DM|🇩🇲|多米尼克|DO|🇩🇴|多米尼加|DZ|🇩🇿|阿尔及利亚|EC|🇪🇨|厄瓜多尔|EE|🇪🇪|爱沙尼亚|EG|🇪🇬|埃及|ER|🇪🇷|厄立特里亚|ES|🇪🇸|西班牙|ET|🇪🇹|埃塞俄比亚|FI|🇫🇮|芬兰|FJ|🇫🇯|斐济|FM|🇫🇲|密克罗尼西亚|FR|🇫🇷|法国|GA|🇬🇦|加蓬|GB|🇬🇧|英国|GD|🇬🇩|格林纳达|GE|🇬🇪|格鲁吉亚|GH|🇬🇭|加纳|GM|🇬🇲|冈比亚|GN|🇬🇳|几内亚|GQ|🇬🇶|赤道几内亚|GR|🇬🇷|希腊|GT|🇬🇹|危地马拉|GW|🇬🇼|几内亚比绍|GY|🇬🇾|圭亚那|HN|🇭🇳|洪都拉斯|HR|🇭🇷|克罗地亚|HT|🇭🇹|海地|HU|🇭🇺|匈牙利|ID|🇮🇩|印度尼西亚|IE|🇮🇪|爱尔兰|IL|🇮🇱|以色列|IN|🇮🇳|印度|IQ|🇮🇶|伊拉克|IS|🇮🇸|冰岛|IT|🇮🇹|意大利|JM|🇯🇲|牙买加|JO|🇯🇴|约旦|JP|🇯🇵|日本|KE|🇰🇪|肯尼亚|KG|🇰🇬|吉尔吉斯斯坦|KH|🇰🇭|柬埔寨|KI|🇰🇮|基里巴斯|KM|🇰🇲|科摩罗|KN|🇰🇳|圣基茨和尼维斯|KR|🇰🇷|韩国|KW|🇰🇼|科威特|KZ|🇰🇿|哈萨克斯坦|LA|🇱🇦|老挝|LB|🇱🇧|黎巴嫩|LC|🇱🇨|圣卢西亚|LI|🇱🇮|列支敦士登|LK|🇱🇰|斯里兰卡|LR|🇱🇷|利比里亚|LS|🇱🇸|莱索托|LT|🇱🇹|立陶宛|LU|🇱🇺|卢森堡|LV|🇱🇻|拉脱维亚|LY|🇱🇾|利比亚|MA|🇲🇦|摩洛哥|MC|🇲🇨|摩纳哥|MD|🇲🇩|摩尔多瓦|ME|🇲🇪|黑山|MG|🇲🇬|马达加斯加|MH|🇲🇭|马绍尔群岛|MK|🇲🇰|北马其顿|ML|🇲🇱|马里|MM|🇲🇲|缅甸|MN|🇲🇳|蒙古|MR|🇲🇷|毛里塔尼亚|MT|🇲🇹|马耳他|MU|🇲🇺|毛里求斯|MV|🇲🇻|马尔代夫|MW|🇲🇼|马拉维|MX|🇲🇽|墨西哥|MY|🇲🇾|马来西亚|MZ|🇲🇿|莫桑比克|NA|🇳🇦|纳米比亚|NE|🇳🇪|尼日尔|NG|🇳🇬|尼日利亚|NI|🇳🇮|尼加拉瓜|NL|🇳🇱|荷兰|NO|🇳🇴|挪威|NP|🇳🇵|尼泊尔|NR|🇳🇷|瑙鲁|NZ|🇳🇿|新西兰|OM|🇴🇲|阿曼|PA|🇵🇦|巴拿马|PE|🇵🇪|秘鲁|PG|🇵🇬|巴布亚新几内亚|PH|🇵🇭|菲律宾|PK|🇵🇰|巴基斯坦|PL|🇵🇱|波兰|PS|🇵🇸|巴勒斯坦|PT|🇵🇹|葡萄牙|PW|🇵🇼|帕劳|PY|🇵🇾|巴拉圭|QA|🇶🇦|卡塔尔|RO|🇷🇴|罗马尼亚|RS|🇷🇸|塞尔维亚|RW|🇷🇼|卢旺达|SA|🇸🇦|沙特阿拉伯|SB|🇸🇧|所罗门群岛|SC|🇸🇨|塞舌尔|SD|🇸🇩|苏丹|SE|🇸🇪|瑞典|SG|🇸🇬|新加坡|SI|🇸🇮|斯洛文尼亚|SK|🇸🇰|斯洛伐克|SL|🇸🇱|塞拉利昂|SM|🇸🇲|圣马力诺|SN|🇸🇳|塞内加尔|SO|🇸🇴|索马里|SR|🇸🇷|苏里南|SS|🇸🇸|南苏丹|ST|🇸🇹|圣多美和普林西比|SV|🇸🇻|萨尔瓦多|SZ|🇸🇿|斯威士兰|TD|🇹🇩|乍得|TG|🇹🇬|多哥|TH|🇹🇭|泰国|TJ|🇹🇯|塔吉克斯坦|TL|🇹🇱|东帝汶|TM|🇹🇲|土库曼斯坦|TN|🇹🇳|突尼斯|TO|🇹🇴|汤加|TR|🇹🇷|土耳其|TT|🇹🇹|特立尼达和多巴哥|TV|🇹🇻|图瓦卢|TW|🇹🇼|台湾|TZ|🇹🇿|坦桑尼亚|UA|🇺🇦|乌克兰|UG|🇺🇬|乌干达|US|🇺🇸|美国|UY|🇺🇾|乌拉圭|UZ|🇺🇿|乌兹别克斯坦|VA|🇻🇦|梵蒂冈|VC|🇻🇨|圣文森特和格林纳丁斯|VN|🇻🇳|越南|VU|🇻🇺|瓦努阿图|WS|🇼🇸|萨摩亚|YE|🇾🇪|也门|ZA|🇿🇦|南非|ZM|🇿🇲|赞比亚|ZW|🇿🇼|津巴布韦",
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/chatgpt.svg",
    },
    {
      ...groupBaseOption,
      name: "微软服务",
      type: "select",
      proxies: [
        "全局直连",
        "节点选择",
        "延迟选优",
        "故障转移",
        "负载均衡(散列)",
        "负载均衡(轮询)",
      ],
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/microsoft.svg",
    },
    {
      ...groupBaseOption,
      name: "苹果服务",
      type: "select",
      proxies: [
        "节点选择",
        "延迟选优",
        "故障转移",
        "负载均衡(散列)",
        "负载均衡(轮询)",
        "全局直连",
      ],
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/apple.svg",
    },
    {
      ...groupBaseOption,
      name: "广告过滤",
      type: "select",
      proxies: ["REJECT", "DIRECT"],
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/bug.svg",
    },
    {
      ...groupBaseOption,
      name: "全局直连",
      type: "select",
      proxies: [
        "DIRECT",
        "节点选择",
        "延迟选优",
        "故障转移",
        "负载均衡(散列)",
        "负载均衡(轮询)",
      ],
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/link.svg",
    },
    {
      ...groupBaseOption,
      name: "全局拦截",
      type: "select",
      proxies: ["REJECT", "DIRECT"],
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/block.svg",
    },
    {
      ...groupBaseOption,
      name: "漏网之鱼",
      type: "select",
      proxies: [
        "节点选择",
        "延迟选优",
        "故障转移",
        "负载均衡(散列)",
        "负载均衡(轮询)",
        "全局直连",
      ],
      "include-all": true,
      icon: "https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/fish.svg",
    },
  ];

  // 覆盖原配置中的规则
  config["rule-providers"] = ruleProviders;
  config["rules"] = rules;

  // 返回修改后的配置
  return config;
}

```