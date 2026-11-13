import json
import os
import time
from datetime import datetime

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from google import genai

from prompts import FUNCTIONS

# ---------- Setup ----------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-3.8-flash"  # change if Google renamesretires the model
  # backup model is tried if the first is busyFEEDBACK_FILE = "feedback.json"
MODELS = [MODEL, "gemini-flash-latest"]
FEEDBACK_FILE = "feedback.json"

st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="wide")


# ---------- Helpers ----------
def ask_ai(prompt: str) -> str:
    client = genai.Client(api_key=API_KEY)
    last_error = None
    for model in MODELS:
        for attempt in range(3):
            try:
                return client.models.generate_content(
                    model=model, contents=prompt
                ).text
            except Exception as e:
                last_error = e
                if "503" in str(e) or "UNAVAILABLE" in str(e):
                    time.sleep(2 * (attempt + 1))  # wait 2s, 4s, 6s then retry
                else:
                    break  # a different error: skip to the next model
    raise last_error

def load_feedback() -> list:
    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []  # empty or broken file: start fresh
    return []


def save_feedback(helpful: bool):
    """Callback for the Yes/No buttons."""
    last = st.session_state.last
    data = load_feedback()
    data.append(
        {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "function": last["function"],
            "style": last["style"],
            "helpful": helpful,
        }
    )
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    st.session_state.feedback_given = True


# ---------- Session state ----------
if "last" not in st.session_state:
    st.session_state.last = None
if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = False

# ---------- Sidebar: user guide ----------
with st.sidebar:
    st.header("📖 How to use")
    st.markdown(
        """
1. Choose a **function**
2. Choose a **prompt style**
3. Type or paste your input
4. Click **Generate**
5. Tell us if the answer was **helpful**
        """
    )
    st.divider()
    st.caption(f"Model: {MODEL}")

# ---------- Main page ----------
st.title("🤖 AI Assistant")
st.write("Answer questions, summarize text, or generate creative content.")

tab_assistant, tab_feedback = st.tabs(["Assistant", "Feedback Analysis"])

# ===== Tab 1: Assistant =====
with tab_assistant:
    col1, col2 = st.columns(2)
    with col1:
        function = st.selectbox("1️⃣ Choose a function", list(FUNCTIONS.keys()))
    with col2:
        style = st.selectbox(
            "2️⃣ Choose a prompt style", list(FUNCTIONS[function]["prompts"].keys())
        )

    with st.expander("See the prompt template being used"):
        st.code(FUNCTIONS[function]["prompts"][style], language="text")

    user_text = st.text_area(
        "3️⃣ Your input",
        height=180,
        placeholder=FUNCTIONS[function]["placeholder"],
    )

    if st.button("✨ Generate", type="primary"):
        if not API_KEY:
            st.error("GEMINI_API_KEY not found. Add it to your .env file.")
        elif not user_text.strip():
            st.warning("Please enter some text first.")
        else:
            prompt = FUNCTIONS[function]["prompts"][style].format(text=user_text)
            with st.spinner("Thinking..."):
                try:
                    reply = ask_ai(prompt)
                    st.session_state.last = {
                        "function": function,
                        "style": style,
                        "response": reply,
                    }
                    st.session_state.feedback_given = False
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

    # Show the latest response + feedback buttons
    if st.session_state.last:
        st.subheader("Response")
        st.info(
            f"{st.session_state.last['function']} → {st.session_state.last['style']}"
        )
        st.markdown(st.session_state.last["response"])

        st.divider()
        if st.session_state.feedback_given:
            st.success("Thanks for your feedback! 🙏")
        else:
            st.write("**Was this response helpful?**")
            b1, b2, _ = st.columns([1, 1, 6])
            b1.button("👍 Yes", on_click=save_feedback, args=(True,))
            b2.button("👎 No", on_click=save_feedback, args=(False,))

         # ===== Tab 2: Feedback analysis =====
with tab_feedback:
    st.subheader("How are the prompts performing?")
    data = load_feedback()

    if not data:
        st.write("No feedback yet. Use the assistant and rate some responses!")
    else:
        df = pd.DataFrame(data)
        stats = (
            df.groupby(["function", "style"])["helpful"]
            .agg(responses="count", helpful_yes="sum")
            .reset_index()
        )
        stats["helpful_%"] = (stats["helpful_yes"] / stats["responses"] * 100).round(1)

        st.dataframe(stats, use_container_width=True, hide_index=True)
        st.bar_chart(stats.set_index("style")["helpful_%"])

        st.subheader("💡 Suggested prompt improvements")
        weak = stats[stats["helpful_%"] < 60]
        if weak.empty:
            st.success("All prompt styles are performing well (60%+ helpful).")
        else:
            for _, row in weak.iterrows():
                st.warning(
                    f"**{row['function']} → {row['style']}** is only "
                    f"{row['helpful_%']}% helpful. Try making this prompt more "
                    f"specific (add length, tone, or format instructions)."
                )

        with st.expander("Raw feedback log"):
            st.dataframe(df, use_container_width=True, hide_index=True)   