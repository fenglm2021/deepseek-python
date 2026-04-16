from core.deepseek_client import DeepSeekClient

client = DeepSeekClient()

work_log = """
今天：
- 修了一个bug，是登录页面的样式问题
- 开了产品需求会，确定了新功能的优先级
- 回了3封客户的邮件
- 看了两篇关于AI的公众号文章
"""

prompt = f"""
你是一个职场助手。请根据以下工作记录，帮我写一份工作日报。
要求：语言简洁，分点列出，每条前面加序号。

工作记录：
{work_log}
"""

report = client.chat(prompt, max_tokens=300)
print("=== 今日日报 ===\n", report)
