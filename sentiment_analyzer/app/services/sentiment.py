def analyze_sentiment(text: str) -> str:
    text = text.lower()
    if "happy" in text or "good" in text:
        return "positive"
    elif "sad" in text or "bad" in text:
        return "negative"
    else:
        return "neutral"