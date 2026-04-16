from core.deepseek_client import DeepSeekClient

client = DeepSeekClient()

article = """
人工智能（AI）技术的发展正在深刻改变我们的生活和工作方式。
从早期的规则系统到现在的深度学习，AI已经能够处理越来越复杂的任务。
特别是在自然语言处理领域，大语言模型的出现让机器能够理解、生成甚至推理文本内容。
然而，AI的发展也带来了一系列挑战，包括数据隐私、算法偏见、就业影响等问题。
如何在技术进步的同时确保其安全、公平、可控，成为了学术界和产业界共同关注的焦点。
"""

summary = client.chat(f"请用3句话总结以下内容：\n{article}", max_tokens=100)
print("=== 文章总结 ===\n", summary)
