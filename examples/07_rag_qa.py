from core.rag import RAG

# 初始化RAG（会自动加载docs/company_policy.txt）
rag = RAG(docs_path="../docs/company_policy.txt")

# 测试几个问题
questions = [
    "年假有多少天？",
    "怎么请病假？",
    "加班工资怎么算？"
]

for q in questions:
    print(f"问题：{q}")
    print(f"回答：{rag.ask(q)}")
    print("-" * 50)
