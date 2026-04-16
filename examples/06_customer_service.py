from core.deepseek_client import DeepSeekClient

# 带系统提示词的客服
client = DeepSeekClient()
client.set_system_prompt("你是一个耐心的客服助手，回答问题要简洁、友好。如果不知道答案，就说'我去问一下技术同事'。")

print("用户：你们的产品有试用版吗？")
print("客服：", client.chat("你们的产品有试用版吗？", max_tokens=50))

print("\n用户：多少钱一年？")
print("客服：", client.chat("多少钱一年？"))
