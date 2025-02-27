This project is a FastAPI-based web service that allows users to ingest content from a given URL and perform question-answering based on the ingested data. It provides a simple and efficient API for extracting and querying information using Python, FastAPI, and LangChain.

Features

1) Ingest URL Content – Extract text content from a provided URL and store it for later processing.
2) Ask Questions – Query the ingested content using natural language and receive relevant answers.
3) FastAPI Swagger UI – Interactive API documentation at http://127.0.0.1:8000/docs.
4) Asynchronous Processing – Uses FastAPI’s async capabilities for efficient request handling.

Tech Stack

Backend: FastAPI, Uvicorn, LangChain

Database: MongoDB / PostgreSQL (if applicable)

Frontend: React (if applicable)

Deployment: Docker, Render, or AWS (optional)

Setup & Installation

1) Install Dependencies

pip install fastapi uvicorn requests beautifulsoup4 langchain openai
 
2) Run the Server

uvicorn backend:app --reload

3) Test the API

Open Swagger UI: http://127.0.0.1:8000/docs

Use Postman or cURL to send API requests

API Endpoints

Method

Endpoint

Description

POST

/ingest/

Ingest content from a URL

POST

/ask/

Ask a question about ingested content

Future Enhancements

A) Add support for multiple data sources (PDFs, YouTube, etc.)
B) Improve retrieval-augmented generation (RAG) performance
C) Implement authentication & access control
