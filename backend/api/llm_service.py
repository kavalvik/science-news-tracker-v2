from openai import OpenAI
import os

print("OPENROUTER_API_KEY exists:", bool(os.getenv('OPENROUTER_API_KEY')))

class LLMService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv('OPENROUTER_API_KEY'),
        )
    
    def ask_with_context(self, question, context_documents):
        prompt = f"""
Ты — научный ассистент. Отвечай на вопросы, используя только предоставленный контекст.
Если ответа нет в контексте, скажи: "В базе знаний нет информации по этому вопросу."

КОНТЕКСТ:
{context_documents}

ВОПРОС: {question}

ОТВЕТ:"""
        
        response = self.client.chat.completions.create(
            model="openrouter/free",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content