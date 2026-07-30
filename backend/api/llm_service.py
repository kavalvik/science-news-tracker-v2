from openai import OpenAI
import os

print("OPENROUTER_API_KEY exists:", bool(os.getenv('OPENROUTER_API_KEY')))

class LLMService:
    def __init__(self):
        #self.client = OpenAI(
        #    base_url="https://openrouter.ai/api/v1",
        #    api_key=os.getenv('OPENROUTER_API_KEY'),
        #)
        pass
    
    def ask_with_context(self, question, context_documents):
        #prompt = f"""
        return f"""Привет! Я получил твой вопрос: "{question}"
Я нашёл в базе знаний следующие релевантные документы (первые 200 символов каждого):
{context_documents[:500] if context_documents else "Нет релевантных документов."}
... (здесь должен быть ответ от LLM, но пока это заглушка)"""

#КОНТЕКСТ:
#{context_documents}

#ВОПРОС: {question}

#ОТВЕТ:"""
        
       # response = self.client.chat.completions.create(
       #     model="openrouter/free",
       #     messages=[{"role": "user", "content": prompt}]
        #)
        #return response.choices[0].message.content