# Sentiment Analyzer

This project is a FastAPI-based web service that analyzes the sentiment of input text. It exposes a REST API endpoint (`/analyze`) that accepts text and returns the sentiment result (e.g., positive, negative, neutral).

---

## Features

- REST API for sentiment analysis
- Easy to run locally or with Docker
- Automatic code formatting and linting with pre-commit hooks
- Ready for CI/CD integration

---

## How to Run

### 1. Run Locally

**Prerequisites:**
- Python 3.10+
- `pip` package manager

**Steps:**
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```
3. Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI.

---

### 2. Run with Docker

**Prerequisites:**
- Docker installed

**Steps:**
1. Build the Docker image:
    ```bash
    docker build -t sentiment-analyzer .
    ```
2. Run the Docker container:
    ```bash
    docker run -p 8000:8000 sentiment-analyzer
    ```
3. Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI.

---

## Configuration & Setup Notes

- Environment variables can be set in a `.env` file at the project root. See `app/core/config.py` for configurable options.
- Pre-commit hooks are configured in `.pre-commit-config.yaml` for code formatting and linting.
- The main API endpoint is `/analyze` (POST), which accepts JSON:  
  ```json
  {
    "text": "Your text here"
  }