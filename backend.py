from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

app = FastAPI()

# Store ingested content
content_store = {}

openai_model = ChatOpenAI(openai_api_key="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", model_name="gpt-3.5-turbo")

class URLRequest(BaseModel):
    url: str

class QuestionRequest(BaseModel):
    question: str

def extract_text_from_url(url):
    """Fetch and extract text content from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text from all paragraphs
        text = " ".join([p.get_text() for p in soup.find_all("p")])
        return text if text else "No readable content found on the page."
    except requests.exceptions.RequestException as e:
        return str(e)

@app.post("/ingest/")
def ingest_url(data: URLRequest):
    """Ingest content from a URL and store it."""
    text_content = extract_text_from_url(data.url)
    if "No readable content" in text_content:
        raise HTTPException(status_code=400, detail="Failed to extract content.")
    
    content_store[data.url] = text_content
    return {"message": "Content ingested successfully!", "url": data.url}

@app.post("/ask/")
def ask_question(data: QuestionRequest):
    """Answer a question based on the ingested web content."""
    if not content_store:
        raise HTTPException(status_code=400, detail="No content has been ingested yet.")

    # Combine all stored webpage content
    combined_text = " ".join(content_store.values())

    # Ask OpenAI using the extracted content only
    messages = [
        SystemMessage(content="You are a helpful AI that answers based only on provided content."),
        HumanMessage(content=f"Content: {combined_text}\n\nQuestion: {data.question}")
    ]

    response = openai_model(messages)
    return {"answer": response.content}
