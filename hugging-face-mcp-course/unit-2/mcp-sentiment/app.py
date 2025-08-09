import json
import gradio as gr
from textblob import TextBlob
from typing import Any


def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text.

    Args:
       text (str): The text to analyze

    Returns:
       str: A JSON string containing polarity, subjectivity, and assessment
    """

    blob = TextBlob(text)
    sentiment: Any = blob.sentiment

    result = {
        "polarity": round(sentiment.polarity, 2),
        "subjectivity": round(sentiment.subjectivity, 2),
        "assessment": "positive"
        if sentiment.polarity > 0
        else "negative"
        if sentiment.polarity < 0
        else "neutral",
    }

    return json.dumps(result, indent=2)


# Create the Gradio interface
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Enter text to analyze..."),
    outputs=gr.Textbox(),
    title="Text Sentiment Analysis",
    description="Analyze the sentiment of your text using TextBlob",
)

# Launch the interface and MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
