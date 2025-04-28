from model import predict_sentiment

def test_predict_positive():
    """Tests the positive sentiment prediction."""
    assert predict_sentiment("I am happy today") == "positive"

def test_predict_negative():
    """Tests the negative sentiment prediction."""
    assert predict_sentiment("I feel sad") == "negative"

def test_predict_neutral():
    """Tests the neutral sentiment prediction."""
    assert predict_sentiment("The sky is blue") == "neutral" 