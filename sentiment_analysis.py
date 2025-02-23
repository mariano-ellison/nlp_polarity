from textblob import TextBlob


def analyze_sentiment(text):
       blob = TextBlob(text)
       sentiment = blob.sentiment
       polarity = sentiment.polarity
       subjectivity = sentiment.subjectivity

       polarity_desc = "Positive" if polarity > 0.2 else "Negative" if polarity < -0.2 else "Neutral"
       subjectivity_desc = "Subjective (Opinion)" if subjectivity > 0.5 else "Objective (Factual)"

       return polarity_desc, subjectivity_desc, polarity, subjectivity

if __name__ == "__main__":
       # Sample text
       user_feedback = input("Enter text for sentiment analysis: ")
       polarity_desc, subjectivity_desc, polarity, subjectivity = analyze_sentiment(user_feedback)

       print(f"Sentiment: {polarity_desc} ({polarity})")
       print(f"Subjectivity: {subjectivity_desc} ({subjectivity})")