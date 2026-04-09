from sentence_transformers import SentenceTransformer
import chromadb
from .models import Article

class KnowledgeBase:
    def __init__(self):
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("articles")
        self._load_articles()
    
    def _load_articles(self):
        articles = Article.objects.all()
        for article in articles:
            self.collection.add(
                documents=[article.content],
                metadatas=[{"title": article.title, "id": article.id}],
                ids=[str(article.id)]
            )
    
    def search(self, query, top_k=3):
        query_vector = self.model.encode(query).tolist()
        results = self.collection.query(query_embeddings=[query_vector], n_results=top_k)
        return results