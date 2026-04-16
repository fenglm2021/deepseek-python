import os
import chromadb
from chromadb.utils import embedding_functions
from core.deepseek_client import DeepSeekClient

# 设置镜像（仅用于 sentence-transformers 首次下载）
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'


class RAG:
    def __init__(self, docs_path=None):
        # 1. 初始化 embedding 函数（使用你指定的模型）
        self.embed_model_name = "BAAI/bge-small-zh-v1.5"
        self.embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=self.embed_model_name
        )

        # 2. 初始化向量库（持久化到 ./vector_db）
        self.client = chromadb.PersistentClient(path="./vector_db")

        # 3. 获取或创建 collection，并绑定 embedding 函数
        self.collection = self.client.get_or_create_collection(
            name="my_docs",
            embedding_function=self.embed_fn
        )

        # 4. 如果提供了文档路径，加载并向量化
        if docs_path:
            self.load_documents(docs_path)

    def load_documents(self, docs_path):
        """读取文档，切块，存入向量库（自动向量化）"""
        with open(docs_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 按段落切块
        chunks = [chunk.strip() for chunk in content.split('\n\n') if chunk.strip()]

        # 批量添加到 collection（自动用 embedding_fn 向量化）
        # 注意：Chroma 会自动处理 embedding，我们只需传 documents 和 ids
        self.collection.add(
            documents=chunks,
            ids=[f"doc_{i}" for i in range(len(chunks))]
        )
        print(f"✅已加载 {len(chunks)} 个文档块")

    def search(self, query, top_k=3):
        """检索最相关的 top_k 个文档块"""
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        # results['documents'] 是一个列表的列表，取第一个查询的结果
        return results['documents'][0] if results['documents'] else []

    def ask(self, query):
        """RAG问答：检索 + 生成"""
        # 1. 检索相关文档
        docs = self.search(query)

        if not docs:
            return "未找到相关文档内容。"

        # 2. 拼装提示词
        context = "\n\n".join(docs)
        prompt = f"""请根据以下文档内容回答问题。如果文档里没有相关信息，就说“文档中未找到相关内容”。

文档内容：
{context}

问题：{query}

回答："""

        # 3. 调用 DeepSeek
        llm = DeepSeekClient()
        answer = llm.chat(prompt)
        return answer
