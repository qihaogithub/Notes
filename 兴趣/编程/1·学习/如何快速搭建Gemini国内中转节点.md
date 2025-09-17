---
title: "如何快速搭建Gemini国内中转节点"
source: "https://zhuanlan.zhihu.com/p/17087867915"
author:
  - "[[知乎专栏]]"
published:
created: 2025-01-17
description: "随着Gemini 2.0 在各大模型中崭露头角，很多国内的产品也希望可以接入Gemini，但是由于众所周知的原因，我需要一些方式方法才能完成这一步骤，同时，由于支持OpenAI的客户端工具远远超过支持Gemini，如何解决上述…"
tags:
  - "clippings"
---
随着[Gemini 2.0](https://zhida.zhihu.com/search?content_id=252439366&content_type=Article&match_order=1&q=Gemini+2.0&zhida_source=entity) 在各大模型中崭露头角，很多国内的产品也希望可以接入Gemini，但是由于众所周知的原因，我需要一些方式方法才能完成这一步骤，同时，由于支持OpenAI的客户端工具远远超过支持Gemini，如何解决上述两个问题，这里我们介绍一个基于[开源项目](https://zhida.zhihu.com/search?content_id=252439366&content_type=Article&match_order=1&q=%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE&zhida_source=entity)openai-gemini+cloudflare的方式搭建Gemini国内节点。

[Openai-Gemini](https://link.zhihu.com/?target=https%3A//github.com/ZhangWei-KUMO/openai-gemini)这款开源支持我们一键部署OpenAI格式的Gemini接口。点击Deploy on Cloudflare 之后我们来到部署页面。

![](https://pic1.zhimg.com/v2-e04293147e9b9228bdc15bd77b50b5a4_1440w.jpg)

图1 Cloudflare wokers部署界面

在部署页面中，我们首先填入Workers Account ID，这个ID位于Cloudflare的**Workers和Pages**页面的右侧栏中。在[api-Token](https://link.zhihu.com/?target=https%3A//dash.cloudflare.com/profile/api-tokens)页面中，我们创建一个token。首先，选择**编辑Cloudflare Workers** 模板。

![](https://pic3.zhimg.com/v2-4642d7cb4a62373aecfc09f07af3be16_1440w.jpg)

图2 Token配置页面

创建完成后填入，等待部署成功即可。之后进入Cloudflare的workers界面，我们给项目添加一个自定义的域名，方便我们在国内调用。

![](https://pic3.zhimg.com/v2-7de5aa4ea3b8a34f1e4d12d407e38bee_1440w.jpg)

图3 自定义域名页面

## 测试阶段

准备好你的域名和Gemini API KEY，执行脚本如下：

```bash
curl -H "Authorization: Bearer [API KEY]" 
https://[你的域名]/v1/models
```

如果输出的结果是一个数组，其中包含各类模型列表则表示你的国内中转节点设置成功了，如果你是基于OpenAI的[接口开发](https://zhida.zhihu.com/search?content_id=252439366&content_type=Article&match_order=1&q=%E6%8E%A5%E5%8F%A3%E5%BC%80%E5%8F%91&zhida_source=entity)或是使用OpenAI的客户端，填入自定义域名和API KEY就可以在国内自由使用了。

## Python测试

```python
import requests
import json
import os

# 你的 API 密钥，请替换为你实际的密钥
API_KEY = "xxxxx"

# API 的 base URL
BASE_URL = "https://xxxxx"

def generate_text(prompt, model="gemini-2.0-flash-exp"):
    """
    使用 Gemini API 生成文本。

    Args:
        prompt (str): 要发送给模型的提示。
        model (str): 使用的模型名称 (默认为 gemini-2.0-flash-exp)。

    Returns:
        str: 模型生成的文本。
        None: 如果请求失败则返回 None。
    """

    url = f"{BASE_URL}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            },{
                "role": "system",
                "content": "请假装是一个什么都不懂的老师"    
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status() # 抛出异常，方便捕获http错误
        response_data = response.json()

        if response_data.get('choices'):
            return response_data['choices'][0]['message']['content']
        else:
            print(f"Unexpected response structure: {response_data}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None

if __name__ == "__main__":
    test_prompt = "最近股票市场如何？"
    generated_text = generate_text(test_prompt)

    if generated_text:
      print("Generated text:\n", generated_text)
    else:
      print("Failed to generate text")
```

## Node.js测试

```js
const fetch = require('node-fetch');
require('dotenv').config(); // 用于加载 .env 文件

// 你的 API 密钥，请替换为你实际的密钥
const API_KEY = process.env.API_KEY || 'AIzaSyA8psZmQNVTAZORMMY5KRDCamDNtdd4uA0';

// API 的 base URL
const BASE_URL = 'https://gemini-api.tubex.chat';

/**
 * 使用 Gemini API 生成文本。
 * @param {string} prompt - 要发送给模型的提示。
 * @param {string} model - 使用的模型名称 (默认为 gemini-2.0-flash-exp)。
 * @returns {Promise<string|null>} 模型生成的文本，如果请求失败则返回 null。
 */
async function generateText(prompt, model = 'gemini-2.0-flash-exp') {
  const url = \`${BASE_URL}/v1/chat/completions\`;
  const headers = {
    'Authorization': \`Bearer ${API_KEY}\`,
    'Content-Type': 'application/json'
  };
  const data = {
    'model': model,
    'messages': [
      {
        'role': 'user',
        'content': prompt
      }
    ]
  };

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error(\`HTTP error! Status: ${response.status}, Message: ${errorText}\`);
      return null;
    }

    const responseData = await response.json();

    if (responseData && responseData.choices && responseData.choices.length > 0) {
      return responseData.choices[0].message.content;
    } else {
      console.error(\`Unexpected response structure: ${JSON.stringify(responseData)}\`);
      return null;
    }
  } catch (error) {
    console.error('Error calling API:', error);
    return null;
  }
}

async function main() {
  const testPrompt = 'Write a short poem about the moon.';
  const generatedText = await generateText(testPrompt);

  if (generatedText) {
    console.log('Generated text:\n', generatedText);
  } else {
    console.log('Failed to generate text.');
  }
}

main();
```