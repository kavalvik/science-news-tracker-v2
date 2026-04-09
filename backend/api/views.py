from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import KnowledgeBase

kb = KnowledgeBase()

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    if not query:
        return Response({'error': 'Query is required'}, status=400)
    
    results = kb.search(query)
    return Response(results)