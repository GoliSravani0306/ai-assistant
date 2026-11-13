# 🤖 AI Assistant

A simple AI Assistant built with **Python, Streamlit and the Google Gemini API**.
It was created as a Prompt Engineering major project.

## 🔗 Live Demo

**👉 [Open the AI Assistant](https://ai-assistant-469o.onrender.com/)**

> The app is hosted on Render's free plan. If nobody has used it for a while, it goes to sleep, so the first load can take up to a minute. Please wait and refresh if needed.

## Features

- **3 functions:** Answer Questions, Summarize Text, Generate Creative Content
- **9 prompts:** 3 different prompt styles for each function (varying in length, tone and complexity)
- **User-friendly interface:** choose a function and style, enter text, and view the response
- **Feedback loop:** 👍 / 👎 buttons after each response, saved in `feedback.json`
- **Feedback analysis:** a table, chart and suggestions showing which prompts need improvement
- **Automatic retry:** if the AI model is busy, the app retries and switches to a backup model

## Prompt styles

| Function | Style 1 | Style 2 | Style 3 |
|---|---|---|---|
| Answer Questions | Short & direct | Detailed explanation | Explain like I'm 10 |
| Summarize Text | One-line summary | Bullet points | Detailed paragraph |
| Generate Creative Content | Short story | Poem | Sci-fi idea |

## Technologies used

- Python 3.10+
- Streamlit
- Google Gemini API (`google-genai`)
- python-dotenv
- pandas
- GitHub (code hosting) and Render (deployment)

## Project structure

```
ai_assistant/
├── app.py            # Streamlit app: interface, AI calls, feedback
├── prompts.py        # All 9 prompt templates
├── requirements.txt  # Libraries to install
├── .env.example      # Example of the .env file
├── .gitignore        # Keeps secret files out of GitHub
└── feedback.json     # Saved feedback (created by the app)
```

## How to use the app

1. Open the [live app](https://YOUR-RENDER-LINK.onrender.com).
2. Choose a **function**.
3. Choose a **prompt style**.
4. Type or paste your input.
5. Click **Generate**.
6. Rate the response with 👍 or 👎.
7. Open the **Feedback Analysis** tab to see how each prompt is performing.

## Run it on your own computer

1. **Clone or download** this repository.
2. **Install the libraries:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Get a free API key** from [Google AI Studio](https://aistudio.google.com/apikey).
4. **Create a file named `.env`** in the project folder and add:
   ```
   GEMINI_API_KEY=your_key_here
   ```
5. **Start the app:**
   ```bash
   python -m streamlit run app.py
   ```
6. Open `http://localhost:8501` in your browser.

## Deployment (Render)

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
- **Environment variable:** `GEMINI_API_KEY` (set in the Render dashboard, never in the code)

## Notes

- The free Gemini API has daily request limits. If you see a quota error, wait for it to reset or use a different model or API key.
- On Render's free plan, `feedback.json` is stored on temporary disk, so saved ratings are cleared when the app restarts or redeploys.
- The API key is never stored in this repository.

## Author

**Sravani Goli**
GitHub: [GoliSravani0306](https://github.com/GoliSravani0306)
