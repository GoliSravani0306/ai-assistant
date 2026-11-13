# 🤖 AI Assistant

A simple AI Assistant built with **Python, Streamlit and the Google Gemini API**.
It was created as a Prompt Engineering major project.

## Features

- **3 functions:** Answer Questions, Summarize Text, Generate Creative Content
- **9 prompts:** 3 different prompt styles for each function (varying in length, tone and complexity)
- **User-friendly interface:** choose a function and style, enter text, and view the response
- **Feedback loop:** 👍 / 👎 buttons after each response, saved in `feedback.json`
- **Feedback analysis:** a table, chart and suggestions showing which prompts need improvement

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

## How to run

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

## How to use

1. Choose a **function**.
2. Choose a **prompt style**.
3. Type or paste your input.
4. Click **Generate**.
5. Rate the response with 👍 or 👎.
6. Open the **Feedback Analysis** tab to see how each prompt is performing.

## Note

The free Gemini API has daily request limits. If you see a quota error, wait for it to reset or use a different model or API key.
