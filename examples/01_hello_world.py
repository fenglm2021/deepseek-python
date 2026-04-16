from core.deepseek_client import DeepSeekClient

client = DeepSeekClient()

reply = client.chat("你好，请介绍一下你自己")
print("DeepSeek说：", reply)
