# 🚀 Trade Opportunities API

A FastAPI-based backend service that analyzes market data and generates **trade opportunity insights** for different sectors in India using AI.

---

## 📌 Overview

This API accepts a sector name (e.g., `pharmaceuticals`, `technology`) and returns a **structured markdown report** with:

* Market Overview
* Key Trends
* Trade Opportunities
* Risks
* Future Outlook

The system integrates **real-time data collection** with **AI-driven analysis**.

---

## 🧠 Architecture

```
Client → FastAPI → Service Layer
                    ├── Data Collector (DuckDuckGo)
                    ├── AI Analyzer (Azure OpenAI)
                    └── Report Generator (Markdown)
```

---

## ⚙️ Tech Stack

* **FastAPI** – Backend framework
* **Azure OpenAI** – AI analysis
* **DuckDuckGo Search (ddgs)** – Market data collection
* **Python** – Core language

---

## 🔐 Features

* ✅ API Key Authentication
* ✅ Session Management (in-memory)
* ✅ Rate Limiting (per user)
* ✅ Input Validation
* ✅ Error Handling
* ✅ Clean Modular Architecture

---

## 📡 API Endpoint

### 🔍 Analyze Sector

```
GET /analyze/{sector}
```

### Query Params:

| Param   | Required | Description                |
| ------- | -------- | -------------------------- |
| api_key | ✅        | Use `test123` or `demo123` |

---

## 📥 Example Request

```
GET /analyze/pharmaceuticals?api_key=test123
```

---

## 📤 Example Response

```json
{
  "report": "# 📊 Pharma Sector Analysis (India)\n\n## Market Overview\n..."
}
```

---

## 🚦 Rate Limiting

* Max **5 requests per minute per API key**
* Exceeding limit returns:

```json
{
  "detail": "Rate limit exceeded. Try again later."
}
```

---

## 🧠 How It Works

1. User sends sector input
2. System fetches latest market data via DuckDuckGo
3. Data is processed by Azure OpenAI
4. AI generates structured trade insights
5. Markdown report is returned

---

## 🔧 Setup Instructions

### 1. Clone Repo

```bash
git clone <your-repo-url>
cd trade-opportunities-api
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create `.env` file:

```env
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

---

### 5. Run Server

```bash
uvicorn app.main:app --reload
```

---

### 6. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🔑 API Keys (Demo)

Use any of the following:

* `test123`
* `demo123`

---

## ⚠️ Notes

* Uses **in-memory storage** (no database required)
* Sessions reset when server restarts
* Designed for demonstration and assignment purposes

---

## 🎯 Future Improvements

* JWT-based authentication
* Database integration
* Caching for faster responses
* Advanced scraping for richer data

---

## 👨‍💻 Author

Built as part of a backend assignment to demonstrate:

* API design
* AI integration
* System architecture
* Backend engineering best practices

---
