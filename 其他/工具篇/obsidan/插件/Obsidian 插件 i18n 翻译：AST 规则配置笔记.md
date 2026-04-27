---
创建日期: 2026-04-27T11:55:16+08:00
修改日期: 2026-04-27T11:55:50+08:00
---


## 一、核心背景
- 插件：Obsidian i18n（用于汉化 Obsidian 第三方插件）
- 场景：汉化 JSX/TSX 打包后的文本，这类文本通常以 `children: "文本内容"` 的形式出现在 AST 中
- 限制：插件 AST 规则中无 `Literal` 选项，统一用 `ObjectProperty` 规则实现文本精准匹配

---

## 二、通用配置模板（所有 JSX 文本通用）
| 配置项 | 填写说明 | 示例 |
| :--- | :--- | :--- |
| 类型 | 固定选：`ObjectProperty (对象属性)` | ObjectProperty (对象属性) |
| 名称 | 固定填：`children`（所有 JSX 文本的键名都是 `children`） | children |
| 原文 | 复制插件代码中完整的待翻译文本（含标点、大小写） | Connect your subscription |
| 译文 | 填写通顺、符合软件使用场景的中文翻译 | 连接您的订阅 |

> 💡 关键说明：
> - 插件打包后的 JSX 文本，最终都会被处理为 `{ children: "xxx" }` 的对象属性
> - 用 `ObjectProperty + children` 组合，能精准命中所有界面文本，避免误匹配其他位置的同名字符串

---

## 三、本次示例：警告文本翻译配置
### 1. 待翻译原文
```
Anthropic has restricted third-party OAuth access, and there are reports of account bans when using subscription OAuth via third-party clients. See the README for full details and use at your own risk.
```

### 2. 推荐译文
```
Anthropic 已限制第三方 OAuth 访问，且有报告显示通过第三方客户端使用订阅 OAuth 可能导致账号封禁。详情请参阅 README，使用风险自负。
```

### 3. 完整规则配置
| 配置项 | 填写内容 |
| :--- | :--- |
| 类型 | ObjectProperty (对象属性) |
| 名称 | children |
| 原文 | Anthropic has restricted third-party OAuth access, and there are reports of account bans when using subscription OAuth via third-party clients. See the README for full details and use at your own risk. |
| 译文 | Anthropic 已限制第三方 OAuth 访问，且有报告显示通过第三方客户端使用订阅 OAuth 可能导致账号封禁。详情请参阅 README，使用风险自负。 |

---

## 四、备选方案：词典直接翻译（无需配置AST规则）
如果AST规则不生效，可直接在插件「词典」中添加条目，格式如下：
```json
{
  "Connect your subscription": "连接您的订阅",
  "Anthropic has restricted third-party OAuth access, and there are reports of account bans when using subscription OAuth via third-party clients. See the README for full details and use at your own risk.": "Anthropic 已限制第三方 OAuth 访问，且有报告显示通过第三方客户端使用订阅 OAuth 可能导致账号封禁。详情请参阅 README，使用风险自负。"
}
```

---

## 五、避坑指南
1.  **文本不要拆分**：被 HTML 标签、空格拆分的句子，直接填完整句子即可，插件会自动匹配拼接后的文本
2.  **优先用 ObjectProperty**：和插件打包后的结构匹配度最高，成功率远高于其他规则
3.  **大小写/标点必须一致**：原文的大小写、标点符号必须和代码中完全一致，否则规则不会生效
4.  **词典方案兜底**：如果AST规则反复不生效，直接用词典条目，简单粗暴不踩坑

---

## 六、后续可复用流程
1.  找到插件打包后的 JS 文件，定位待翻译文本
2.  复制完整原文（保留大小写、标点）
3.  按模板创建 `ObjectProperty` 规则，名称填 `children`
4.  填写译文并保存，重启 Obsidian 生效
5.  若未生效，直接添加词典条目兜底
