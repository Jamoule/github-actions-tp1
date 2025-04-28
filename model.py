def predict_sentiment(text):
    """Predicts the sentiment of a given text.

    Args:
        text: The input string.

    Returns:
        'positive', 'negative', or 'neutral' sentiment.
    """
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral" 