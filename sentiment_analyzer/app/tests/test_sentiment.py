from app.services.sentiment import analyze_sentiment

def test_positive():
    assert analyze_sentiment("I feel happy") == "positive"

def test_negative():
    assert analyze_sentiment("I feel bad") == "negative"

def test_neutral():
    assert analyze_sentiment("Just a regular day") == "neutral"