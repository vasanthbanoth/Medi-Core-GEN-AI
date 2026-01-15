import voyageai
from langchain.embeddings.base import Embeddings
import os

class VoyageAIEmbeddings(Embeddings):
    def __init__(self, model_name="voyage-3.5-lite", device="cpu"):
        self.client = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))
        self.model_name = model_name
        self.device = device

    def embed_documents(self, texts):
        response = self.client.embed(
            texts,                 # positional argument
            model=self.model_name,
            input_type="document"
        )
        # Access the embeddings via the .embeddings attribute
        return response.embeddings

    def embed_query(self, query):
        response = self.client.embed(
            [query],
            model=self.model_name,
            input_type="query"
        )
        return response.embeddings[0]
