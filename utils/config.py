import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()


def get_api_key():
    """获取 API Key"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("请在 .env 文件中设置 DEEPSEEK_API_KEY")
    return api_key


def get_model():
    """获取模型名称"""
    return os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
