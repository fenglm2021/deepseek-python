# DeepSeek Python SDK

> 用 Python 接入 DeepSeek API 的示例代码合集，开箱即用的 AI 集成方案

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-API-purple.svg)](https://deepseek.com)

---

## ✨ 特性

- 🚀 **开箱即用** — 克隆即运行，无需复杂配置
- 💬 **多轮对话** — 自动管理对话历史
- 🌊 **流式输出** — 打字机效果体验
- 📚 **RAG支持** — 私有知识库问答
- 📖 **7个实战示例** — 覆盖日常开发场景

---

## 📦 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/fenglm2021/deepseek-python.git
cd deepseek-python
```

### 2. 创建虚拟环境
```bash
python -m venv venv
```

### 3. 激活虚拟环境

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 4. 安装依赖
```bash
pip install -r requirements.txt
```

### 5. 配置 API Key
在项目根目录创建 .env 文件，填入你的 DeepSeek API Key：
```bash
DEEPSEEK_API_KEY=your_api_key_here
```
> 💡 获取 API Key：platform.deepseek.com

### 6. 运行示例
```bash
python examples/01_hello_world.py
```

## 📁 项目结构

```bash
deepseek-python/
├── core/                         # 核心模块
│   ├── deepseek_client.py        # DeepSeekClient 封装类
│   └── rag.py                    # RAG 检索增强模块
├── examples/                     # 示例代码
│   ├── 01_hello_world.py         # 最简单的调用
│   ├── 02_multi_turn.py          # 多轮对话
│   ├── 03_stream.py              # 流式输出
│   ├── 04_summary.py             # 文章总结
│   ├── 05_daily_report.py        # 日报生成
│   ├── 06_customer_service.py    # 客服问答
│   └── 07_rag_qa.py              # RAG 知识库问答
├── utils/                        # 工具模块
│   └── config.py                 # 配置读取
├── data/                         # 数据文件
├── docs/                         # 文档
├── .env                          # 环境变量（API Key）
├── .gitignore                    # Git忽略文件
├── requirements.txt              # 依赖列表
└── README.md                     # 本文件
```

## 📚 示例列表

| 序号 | 文件 | 说明                   |
| :--- | :--- |:---------------------|
| 01 | `01_hello_world.py` | 最简单的调用，快速验证 API 连通性  |
| 02 | `02_multi_turn.py` | 多轮对话，带记忆的聊天体验        |
| 03 | `03_stream.py` | 流式输出，打字机效果           |
| 04 | `04_summary.py` | 文章总结，长文本摘要生成         |
| 05 | `05_daily_report.py` | 日报生成，自动整理工作内容        |
| 06 | `06_customer_service.py` | 客服问答，智能客服机器人         |
| 07 | `07_rag_qa.py` | RAG知识库问答，基于私有文档的智能问答 |

## 🛠️ 基础用法
```python
from core.deepseek_client import DeepSeekClient

# 初始化客户端
client = DeepSeekClient()

# 单轮对话
response = client.chat("你好，DeepSeek！")
print(response)

# 多轮对话（自动记忆上下文）
client.chat("我叫小明")
client.chat("我叫什么名字？")  # AI 会回答"小明"

# 流式输出
for chunk in client.chat("讲个笑话", stream=True):
    print(chunk, end="", flush=True)
```

## 📄 开源协议

本项目采用 MIT 协议 开源，你可以自由使用、修改、分发，甚至用于商业项目。

## 🙏 致谢

- DeepSeek — 提供强大的国产大模型 API
- 所有为本项目点 ⭐ 的朋友

## 📱 与我联系

如果这个项目对你有帮助，欢迎关注我的公众号，获取更多 AI 开发实战内容：

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/fenglm2021/deepseek-python/images/qrcode.png" width="200" alt="公众号二维码">
  <br>
  <b>扫码关注公众号：小民AI实战笔记</b>
  <br>
  <i>每周更新：AI 开发实战 | AI 应用案例</i>
</div>

### 公众号能给你什么？
| 内容             | 说明           |
|:---------------|:-------------|
| 🔥 本项目的深度解析    | 源码讲解、扩展用法    |
| 🧠 DeepSeek新功能 | 第一时间解读       |
| 🛠️ 更多实战案例     | 本项目的7个示例只是开始 |
| 💬 1对1答疑       | 公众号菜单可加我微信   |

## Happy Coding! 🚀
