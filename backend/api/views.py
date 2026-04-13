from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import KnowledgeBase


from .llm_service import LLMService

# Создаём глобальные объекты
kb = KnowledgeBase()
llm = LLMService()

@api_view(['POST'])
def search(request):
    """Поиск похожих статей в базе знаний"""
    query = request.data.get('query', '')
    if not query:
        return Response({'error': 'Query is required'}, status=400)
    
    results = kb.search(query)
    return Response(results)

@api_view(['POST'])
def chat(request):
    """Чат-бот: ищет в базе знаний и отвечает через Gemini"""
    question = request.data.get('question', '')
    if not question:
        return Response({'error': 'Question is required'}, status=400)
    
    # 1. Ищем похожие статьи в базе знаний
    search_results = kb.search(question)
    
    # 2. Извлекаем текст найденных статей
    documents = search_results.get('documents', [[]])[0]
    context = "\n\n---\n\n".join(documents) if documents else "Нет релевантных документов."
    
    # 3. Отправляем в Gemini вопрос с контекстом
    answer = llm.ask_with_context(question, context)
    
    return Response({
        'question': question,
        'answer': answer,
        'sources': search_results.get('metadatas', [[]])[0]
    })