import requests
import json
from utils.config import get_api_key, get_model


class DeepSeekClient:
    def __init__(self, api_key=None, model=None):
        self.api_key = api_key or get_api_key()
        self.model = model or get_model()
        self.url = "https://api.deepseek.com/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        self.messages = []  # 保存对话历史

    def chat(self, user_input, system_prompt=None, stream=False, max_tokens=None):
        """发送消息，返回AI回复"""
        # 如果有系统提示词且是第一次，先加上
        if system_prompt and not self.messages:
            self.messages.append({"role": "system", "content": system_prompt})

        self.messages.append({"role": "user", "content": user_input})

        data = {
            "model": self.model,
            "messages": self.messages,
            "stream": stream
        }
        if max_tokens:
            data["max_tokens"] = max_tokens

        if stream:
            return self._stream_chat(data)
        else:
            return self._normal_chat(data)

    def _normal_chat(self, data):
        """普通模式"""
        response = requests.post(self.url, headers=self.headers, json=data)

        if response.status_code == 200:
            reply = response.json()['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": reply})
            return reply
        else:
            return f"错误：{response.status_code} - {response.text}"

    def _stream_chat(self, data):
        """流式模式，返回生成器"""
        response = requests.post(self.url, headers=self.headers, json=data, stream=True)

        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data: "):
                    chunk = decoded_line[6:]
                    if chunk == "[DONE]":
                        break
                    try:
                        obj = json.loads(chunk)
                        delta = obj["choices"][0]["delta"].get("content", "")
                        if delta:
                            yield delta
                    except:
                        pass

        # 流式结束后，把完整回复存进历史（这里简化处理，实际需要拼接）
        # 为了简单，流式模式不自动保存历史，需要手动管理

    def clear_history(self):
        """清空对话历史"""
        self.messages = []

    def set_system_prompt(self, prompt):
        """设置系统提示词（会清空历史）"""
        self.clear_history()
        self.messages.append({"role": "system", "content": prompt})

    def get_history(self):
        """获取对话历史"""
        return self.messages
