from core.deepseek_client import DeepSeekClient

client = DeepSeekClient()

reply1 = client.chat("我叫小民，喜欢喝白茶")
print("第一轮：", reply1)

print("-" * 50)

reply2 = client.chat("我喜欢喝什么茶？请只回答茶的名字，不要多说其他的。", max_tokens=20)
print("第二轮：", reply2)