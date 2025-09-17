# RSS资讯后端服务文档

## 概述
本文档描述了如何创建一个RSS订阅解析服务。该服务提供HTTP API接口，可以获取和解析RSS订阅内容，主要用于为Dify工作流提供RSS解析能力。

## 功能特性
- RSS订阅内容解析
- 支持多种RSS格式
- 提供RESTful API接口
- 错误处理和日志记录
- 可配置的缓存机制

## 技术架构
- 开发语言：Python 3.8+
- Web框架：Flask
- RSS解析：feedparser
- 服务器：gunicorn
- 部署环境：宝塔面板

## 实现步骤

### 1. 环境准备
1. Python环境（推荐Python 3.8+）
2. 安装必要的依赖：
```bash
pip install flask feedparser requests gunicorn
```

### 2. 项目结构
```
rss-service/
├── app.py          # 主应用文件
├── requirements.txt # 依赖文件
├── config.py       # 配置文件
├── gunicorn.conf.py # gunicorn配置文件
└── utils/          # 工具函数目录
    └── __init__.py
```

### 3. 核心代码实现

#### 3.1 配置文件 (config.py)
```python
class Config:
    # 服务配置
    PORT = 5000
    HOST = '0.0.0.0'
    
    # RSS解析配置
    RSS_TIMEOUT = 30  # RSS请求超时时间
    MAX_ENTRIES = 50  # 最大返回条目数
    
    # 缓存配置
    ENABLE_CACHE = False
    CACHE_TIMEOUT = 300  # 缓存时间（秒）
```

#### 3.2 主应用代码 (app.py)
```python
from flask import Flask, jsonify, request
import feedparser
from datetime import datetime
from config import Config

app = Flask(__name__)

@app.route('/rss', methods=['GET'])
def get_rss():
    """
    获取并解析RSS源
    
    Query Parameters:
        url (required): RSS源URL
        max_entries (optional): 最大返回条目数，默认50
    
    Returns:
        JSON对象，包含RSS源信息和文章列表
    """
    rss_url = request.args.get('url')
    max_entries = int(request.args.get('max_entries', Config.MAX_ENTRIES))
    
    if not rss_url:
        return jsonify({
            "success": False,
            "error": "Missing RSS URL"
        }), 400
    
    try:
        # 设置超时时间
        feedparser.PARSE_TIMEOUT = Config.RSS_TIMEOUT
        feed = feedparser.parse(rss_url)
        
        # 检查feed是否有效
        if feed.get('bozo_exception'):
            return jsonify({
                "success": False,
                "error": str(feed['bozo_exception'])
            }), 400
        
        entries = []
        for entry in feed.entries[:max_entries]:
            entry_data = {
                "title": entry.get('title', ''),
                "link": entry.get('link', ''),
                "published": entry.get('published', ''),
                "summary": entry.get('summary', ''),
                "author": entry.get('author', ''),
                "tags": [tag.term for tag in entry.get('tags', [])],
                "content": entry.get('content', [{}])[0].get('value', ''),
                "fetch_time": datetime.now().isoformat()
            }
            entries.append(entry_data)
            
        return jsonify({
            "success": True,
            "feed_info": {
                "title": feed.feed.get('title', ''),
                "description": feed.feed.get('description', ''),
                "language": feed.feed.get('language', ''),
                "updated": feed.feed.get('updated', '')
            },
            "entries": entries
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT)
```

#### 3.3 gunicorn配置 (gunicorn.conf.py)
```python
# gunicorn配置文件
workers = 4  # 根据服务器配置调整
bind = "0.0.0.0:5000"
timeout = 120
worker_class = 'sync'  # 使用同步工作模式
max_requests = 1000    # 工作进程重启之前处理的最大请求数
```

### 4. API接口说明

#### 4.1 获取RSS内容
- **接口**: `/rss`
- **方法**: GET
- **参数**:
  - url (必填): RSS源URL
  - max_entries (可选): 最大返回条目数，默认50
- **返回示例**:
```json
{
    "success": true,
    "feed_info": {
        "title": "示例RSS源",
        "description": "RSS源描述",
        "language": "zh-cn",
        "updated": "2024-01-01T12:00:00Z"
    },
    "entries": [
        {
            "title": "文章标题",
            "link": "文章链接",
            "published": "发布时间",
            "summary": "文章摘要",
            "author": "作者",
            "tags": ["标签1", "标签2"],
            "content": "文章内容",
            "fetch_time": "获取时间"
        }
    ]
}
```

### 5. 部署说明

#### 5.1 宝塔面板部署步骤
1. 创建网站目录：/www/wwwroot/rss-service
2. 上传项目文件到该目录
3. 在宝塔Python项目管理器中添加项目：
   - 项目路径：/www/wwwroot/rss-service
   - Python版本：3.8+
   - 启动方式：gunicorn
   - 启动文件：app.py
   - 端口：5000

#### 5.2 依赖安装
```bash
pip install -r requirements.txt
```

### 6. 维护和监控

#### 6.1 日志管理
- 检查gunicorn日志
- 监控应用错误日志
- 定期清理日志文件

#### 6.2 性能优化
- 添加缓存机制
- 优化RSS解析逻辑
- 调整gunicorn工作进程数

#### 6.3 安全建议
- 限制API访问频率
- 配置防火墙规则
- 定期更新依赖包
- 使用HTTPS协议

## 常见问题

### 问题1：RSS解析超时
- 检查RSS源的响应时间
- 调整超时配置
- 考虑使用异步请求

### 问题2：内存占用过高
- 调整最大返回条目数
- 优化数据处理逻辑
- 及时释放资源

### 问题3：服务响应慢
- 添加缓存机制
- 优化数据结构
- 调整gunicorn配置
