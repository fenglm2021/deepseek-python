from core.deepseek_client import DeepSeekClient

client = DeepSeekClient()

print("AI：", end="", flush=True)
for chunk in client.chat("写一首关于秋天的短诗", stream=True, max_tokens=100):
    print(chunk, end="", flush=True)
print()
