# Gold Market Analysis Bot

This project is a **LangGraph-based** workflow that:
- Fetches the latest gold prices (current + past 10 days)
- Searches for recent global gold market news
- Analyzes the data using Google Gemini via LangChain
- Cleans and formats the output for readability
- Emails the report directly to your inbox

---

## 📌 Features
- **Price Fetching** – Metals API & Alpha Vantage for global gold rates
- **News Search** – Tavily Search API with recent, relevant news
- **Automated Analysis** – Using `langchain_google_genai` (Gemini 2.5 flash)
- **Output Cleaning** – Removes markdown, extra characters, and formats nicely
- **Email Delivery** – Sends the final report using SMTP

---

## ⚙️ Setup

### 1.Install Dependencies
```bash
pip install -r requirements.txt
```

### 2.Add Your API Keys & Email Config to .env
```bash
METAL_PRICE_API=your_metals_api_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key

EMAIL_USER=youremail@gmail.com
EMAIL_PASS=yourapppassword
EMAIL_TO=recipientemail@gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### 3.Run the Bot
```bash
python main.py
```

### Purpose
I created this project as a practice exercise for LangGraph, combining multiple tools into an automated workflow that can fetch, analyze, and send financial market insights.