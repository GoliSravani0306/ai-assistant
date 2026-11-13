"""All prompt templates for the AI Assistant.

3 functions x 3 prompts each = 9 prompts.
Each prompt differs in length/specificity, tone/style and complexity.
"""

FUNCTIONS = {
    "Answer Questions": {
        "placeholder": "e.g. What is the capital of France?",
        "prompts": {
            "Short & direct": (
                "Answer the following question in one or two clear sentences. "
                "Be factual and do not add extra detail.\n\nQuestion: {text}"
            ),
            "Detailed explanation": (
                "You are a knowledgeable teacher. Give a detailed, well-structured "
                "answer with background, key points and an example where useful.\n\n"
                "Question: {text}"
            ),
            "Explain like I'm 10": (
                "Explain the answer in very simple, friendly words that a 10-year-old "
                "can understand. Use a fun everyday analogy.\n\nQuestion: {text}"
            ),
        },
    },
    "Summarize Text": {
        "placeholder": "Paste the article or text you want summarized...",
        "prompts": {
            "One-line summary": (
                "Summarize the following text in exactly one sentence.\n\n"
                "Text: {text}"
            ),
            "Bullet points": (
                "Summarize the main points of the following text as 5 concise "
                "bullet points.\n\nText: {text}"
            ),
            "Detailed paragraph": (
                "Write a detailed, formal summary of the following text in one or "
                "two paragraphs. Keep the original meaning and key facts.\n\n"
                "Text: {text}"
            ),
        },
    },
    "Generate Creative Content": {
        "placeholder": "e.g. a dragon and a princess / autumn / a robot on Mars",
        "prompts": {
            "Short story": (
                "Write a short, engaging story (about 150-200 words) with a clear "
                "beginning, middle and end about: {text}"
            ),
            "Poem": (
                "Write a creative rhyming poem of 12-16 lines with a warm, "
                "emotional tone about: {text}"
            ),
            "Sci-fi idea": (
                "Generate an original science-fiction novel idea based on: {text}. "
                "Include a title, a one-paragraph premise, the main character and "
                "the central conflict."
            ),
        },
    },
}